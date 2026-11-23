# v15.7.4 → v16.0.0 · 要調査の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-1c92f2703c7bf4a5522642a38d8c7bdb"></a>

### [`00506de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506de0.md) → [`00529c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529c78.md) FUN_00529c78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00506e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506de0.md#insn-00506e2c) · [`00506e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506de0.md#insn-00506e40) · [`00506e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506de0.md#insn-00506e48)
- 新版 `00529cc4`（命令位置の公開資料なし） · `00529cd8`（命令位置の公開資料なし） · `00529ce0`（命令位置の公開資料なし）

~~~diff
- 00506e2c ["INT_ADD", "register:40f0:8", ["const:506e2c:8", "const:4:8"]]
- 00506e2c ["CALL", null, ["callee:00c538e0:8"]]
+ 00529cc4 ["INT_ADD", "register:40f0:8", ["const:529cc4:8", "const:4:8"]]
+ 00529cc4 ["CALL", null, ["callee:00c538e0:8"]]
- 00506e2c bytes 19401b94
+ 00529cc4 bytes 07a71c94
- 00506e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00506e40 ["INT_ADD", "register:40f0:8", ["const:506e40:8", "const:4:8"]]
- 00506e40 ["CALLIND", null, ["register:0:8"]]
+ 00529cd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00529cd8 ["INT_ADD", "register:40f0:8", ["const:529cd8:8", "const:4:8"]]
+ 00529cd8 ["CALLIND", null, ["register:0:8"]]
- 00506e40 bytes 00013fd6
+ 00529cd8 bytes 00013fd6
- 00506e48 ["INT_ADD", "register:40f0:8", ["const:506e48:8", "const:4:8"]]
- 00506e48 ["CALL", null, ["callee:00c57a80:8"]]
+ 00529ce0 ["INT_ADD", "register:40f0:8", ["const:529ce0:8", "const:4:8"]]
+ 00529ce0 ["CALL", null, ["callee:00c57a80:8"]]
- 00506e48 bytes 7a501b94
+ 00529ce0 bytes 68b71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed506ba2a514f2227f496daed5fe2f24"></a>

### [`00508168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508168.md) → [`0052b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b000.md) FUN_0052b000

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508168.md#insn-00508184) · [`005081a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508168.md#insn-005081a4)
- 新版 `0052b01c`（命令位置の公開資料なし） · `0052b03c`（命令位置の公開資料なし）

~~~diff
- 00508184 ["INT_ADD", "register:40f0:8", ["const:508184:8", "const:4:8"]]
- 00508184 ["CALL", null, ["callee:00c538e0:8"]]
+ 0052b01c ["INT_ADD", "register:40f0:8", ["const:52b01c:8", "const:4:8"]]
+ 0052b01c ["CALL", null, ["callee:00c538e0:8"]]
- 00508184 bytes 433b1b94
+ 0052b01c bytes 31a21c94
- 005081a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005081a4 ["INT_ADD", "register:40f0:8", ["const:5081a4:8", "const:4:8"]]
- 005081a4 ["CALLIND", null, ["register:0:8"]]
+ 0052b03c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b03c ["INT_ADD", "register:40f0:8", ["const:52b03c:8", "const:4:8"]]
+ 0052b03c ["CALLIND", null, ["register:0:8"]]
- 005081a4 bytes 00013fd6
+ 0052b03c bytes 00013fd6
~~~


<a id="compare-ddb52a348bb156376ca213b517d6bec4"></a>

### [`005081b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/005081b8.md) → [`0052b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b050.md) FUN_0052b050

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00508204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/005081b8.md#insn-00508204) · [`00508218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/005081b8.md#insn-00508218) · [`00508220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/005081b8.md#insn-00508220)
- 新版 `0052b09c`（命令位置の公開資料なし） · `0052b0b0`（命令位置の公開資料なし） · `0052b0b8`（命令位置の公開資料なし）

~~~diff
- 00508204 ["INT_ADD", "register:40f0:8", ["const:508204:8", "const:4:8"]]
- 00508204 ["CALL", null, ["callee:00c538e0:8"]]
+ 0052b09c ["INT_ADD", "register:40f0:8", ["const:52b09c:8", "const:4:8"]]
+ 0052b09c ["CALL", null, ["callee:00c538e0:8"]]
- 00508204 bytes 233b1b94
+ 0052b09c bytes 11a21c94
- 00508218 ["COPY", "register:0:8", ["register:4040:8"]]
- 00508218 ["INT_ADD", "register:40f0:8", ["const:508218:8", "const:4:8"]]
- 00508218 ["CALLIND", null, ["register:0:8"]]
+ 0052b0b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b0b0 ["INT_ADD", "register:40f0:8", ["const:52b0b0:8", "const:4:8"]]
+ 0052b0b0 ["CALLIND", null, ["register:0:8"]]
- 00508218 bytes 00013fd6
+ 0052b0b0 bytes 00013fd6
- 00508220 ["INT_ADD", "register:40f0:8", ["const:508220:8", "const:4:8"]]
- 00508220 ["CALL", null, ["callee:00c57a80:8"]]
+ 0052b0b8 ["INT_ADD", "register:40f0:8", ["const:52b0b8:8", "const:4:8"]]
+ 0052b0b8 ["CALL", null, ["callee:00c57a80:8"]]
- 00508220 bytes 844b1b94
+ 0052b0b8 bytes 72b21c94
~~~


<a id="compare-c880a390703525b34979a5b20b76c384"></a>

### [`0050936c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md) → [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) FUN_0052c204

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) [`005095f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/005095f0.md) [`0052be2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md) · 呼出先 4件 [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c488.md) [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) · 呼出先 4件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005093b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md#insn-005093b8) · [`005093cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md#insn-005093cc) · [`005093d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md#insn-005093d4)
- 新版 `0052c250`（命令位置の公開資料なし） · `0052c264`（命令位置の公開資料なし） · `0052c26c`（命令位置の公開資料なし）

~~~diff
- 005093b8 ["INT_ADD", "register:40f0:8", ["const:5093b8:8", "const:4:8"]]
- 005093b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0052c250 ["INT_ADD", "register:40f0:8", ["const:52c250:8", "const:4:8"]]
+ 0052c250 ["CALL", null, ["callee:00c538e0:8"]]
- 005093b8 bytes b6361b94
+ 0052c250 bytes a49d1c94
- 005093cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005093cc ["INT_ADD", "register:40f0:8", ["const:5093cc:8", "const:4:8"]]
- 005093cc ["CALLIND", null, ["register:0:8"]]
+ 0052c264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c264 ["INT_ADD", "register:40f0:8", ["const:52c264:8", "const:4:8"]]
+ 0052c264 ["CALLIND", null, ["register:0:8"]]
- 005093cc bytes 00013fd6
+ 0052c264 bytes 00013fd6
- 005093d4 ["INT_ADD", "register:40f0:8", ["const:5093d4:8", "const:4:8"]]
- 005093d4 ["CALL", null, ["callee:00c57a80:8"]]
+ 0052c26c ["INT_ADD", "register:40f0:8", ["const:52c26c:8", "const:4:8"]]
+ 0052c26c ["CALL", null, ["callee:00c57a80:8"]]
- 005093d4 bytes 17471b94
+ 0052c26c bytes 05ae1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ea19b4c021c3117ae3636f337db644"></a>

### [`0050947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md) → [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) FUN_0052c314

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 7件 [`00504ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md) [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`0052bcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052bcb4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 7件 [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005094d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md#insn-005094d0) · [`005094f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md#insn-005094f4) · [`00509520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md#insn-00509520)
- 新版 `0052c368`（命令位置の公開資料なし） · `0052c38c`（命令位置の公開資料なし） · `0052c3b8`（命令位置の公開資料なし）

~~~diff
- 005094d0 ["INT_ADD", "register:40f0:8", ["const:5094d0:8", "const:4:8"]]
- 005094d0 ["CALL", null, ["callee:0054eb4c:8"]]
+ 0052c368 ["INT_ADD", "register:40f0:8", ["const:52c368:8", "const:4:8"]]
+ 0052c368 ["CALL", null, ["callee:0054eb4c:8"]]
- 005094d0 bytes f9890094
+ 0052c368 bytes f9890094
- 005094f4 ["INT_ADD", "register:40f0:8", ["const:5094f4:8", "const:4:8"]]
- 005094f4 ["CALL", null, ["callee:0054eb4c:8"]]
+ 0052c38c ["INT_ADD", "register:40f0:8", ["const:52c38c:8", "const:4:8"]]
+ 0052c38c ["CALL", null, ["callee:0054eb4c:8"]]
- 005094f4 bytes f0890094
+ 0052c38c bytes f0890094
- 00509520 ["INT_ADD", "register:40f0:8", ["const:509520:8", "const:4:8"]]
- 00509520 ["CALL", null, ["callee:00c57a90:8"]]
+ 0052c3b8 ["INT_ADD", "register:40f0:8", ["const:52c3b8:8", "const:4:8"]]
+ 0052c3b8 ["CALL", null, ["callee:00c57a90:8"]]
- 00509520 bytes c8461b94
+ 0052c3b8 bytes b6ad1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb2d84442bf98325ce239a5675ca1706"></a>

### [`005095f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/005095f0.md) → [`0052c488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c488.md) FUN_0052c488

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050936c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/005095f0.md#insn-00509624)
- 新版 `0052c4bc`（命令位置の公開資料なし）

~~~diff
- 00509624 ["INT_ADD", "register:40f0:8", ["const:509624:8", "const:4:8"]]
- 00509624 ["CALL", null, ["callee:0052c204:8"]]
+ 0052c4bc ["INT_ADD", "register:40f0:8", ["const:52c4bc:8", "const:4:8"]]
+ 0052c4bc ["CALL", null, ["callee:0052c204:8"]]
- 00509624 bytes 52ffff97
+ 0052c4bc bytes 52ffff97
~~~


<a id="compare-88c070c885a77398b70263b9cedb2335"></a>

### [`00509658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509658.md) → [`0052c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c4f0.md) FUN_0052c4f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050969c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509658.md#insn-0050969c) · [`005096e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509658.md#insn-005096e4) · [`005096f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509658.md#insn-005096f8)
- 新版 `0052c534`（命令位置の公開資料なし） · `0052c57c`（命令位置の公開資料なし） · `0052c590`（命令位置の公開資料なし）

~~~diff
- 0050969c ["INT_ADD", "register:40f0:8", ["const:50969c:8", "const:4:8"]]
- 0050969c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052c534 ["INT_ADD", "register:40f0:8", ["const:52c534:8", "const:4:8"]]
+ 0052c534 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050969c bytes 71461b94
+ 0052c534 bytes 5fad1c94
- 005096e4 ["INT_ADD", "register:40f0:8", ["const:5096e4:8", "const:4:8"]]
- 005096e4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0052c57c ["INT_ADD", "register:40f0:8", ["const:52c57c:8", "const:4:8"]]
+ 0052c57c ["CALL", null, ["callee:00c538e0:8"]]
- 005096e4 bytes eb351b94
+ 0052c57c bytes d99c1c94
- 005096f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005096f8 ["INT_ADD", "register:40f0:8", ["const:5096f8:8", "const:4:8"]]
- 005096f8 ["CALLIND", null, ["register:0:8"]]
+ 0052c590 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c590 ["INT_ADD", "register:40f0:8", ["const:52c590:8", "const:4:8"]]
+ 0052c590 ["CALLIND", null, ["register:0:8"]]
- 005096f8 bytes 00013fd6
+ 0052c590 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dd8e07379228a51b208bf9d9cd588bc"></a>

### [`00509740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509740.md) → [`0052c5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c5d8.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS6_9a

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0052c038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c038.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054eed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eed0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050979c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509740.md#insn-0050979c) · [`005097c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509740.md#insn-005097c8) · [`005097f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509740.md#insn-005097f8)
- 新版 `0052c634`（命令位置の公開資料なし） · `0052c660`（命令位置の公開資料なし） · `0052c690`（命令位置の公開資料なし）

~~~diff
- 0050979c ["INT_ADD", "register:40f0:8", ["const:50979c:8", "const:4:8"]]
- 0050979c ["CALL", null, ["callee:0054eed0:8"]]
+ 0052c634 ["INT_ADD", "register:40f0:8", ["const:52c634:8", "const:4:8"]]
+ 0052c634 ["CALL", null, ["callee:0054eed0:8"]]
- 0050979c bytes 278a0094
+ 0052c634 bytes 278a0094
- 005097c8 ["INT_ADD", "register:40f0:8", ["const:5097c8:8", "const:4:8"]]
- 005097c8 ["CALL", null, ["callee:00c59b40:8"]]
+ 0052c660 ["INT_ADD", "register:40f0:8", ["const:52c660:8", "const:4:8"]]
+ 0052c660 ["CALL", null, ["callee:00c59b40:8"]]
- 005097c8 bytes 4a4e1b94
+ 0052c660 bytes 38b51c94
- 005097f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005097f8 ["INT_ADD", "register:40f0:8", ["const:5097f8:8", "const:4:8"]]
- 005097f8 ["CALLIND", null, ["register:0:8"]]
+ 0052c690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c690 ["INT_ADD", "register:40f0:8", ["const:52c690:8", "const:4:8"]]
+ 0052c690 ["CALLIND", null, ["register:0:8"]]
- 005097f8 bytes 00013fd6
+ 0052c690 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9d6e57925bf02c316fb21d1014a930"></a>

### [`0050986c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050986c.md) → [`0052c704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c704.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS_17Cer

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005098c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050986c.md#insn-005098c0) · [`005098fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050986c.md#insn-005098fc) · [`00509958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050986c.md#insn-00509958)
- 新版 `0052c758`（命令位置の公開資料なし） · `0052c794`（命令位置の公開資料なし） · `0052c7f0`（命令位置の公開資料なし）

~~~diff
- 005098c0 ["INT_ADD", "register:40f0:8", ["const:5098c0:8", "const:4:8"]]
- 005098c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0052c758 ["INT_ADD", "register:40f0:8", ["const:52c758:8", "const:4:8"]]
+ 0052c758 ["CALL", null, ["callee:00c57a90:8"]]
- 005098c0 bytes e0451b94
+ 0052c758 bytes ceac1c94
- 005098fc ["INT_ADD", "register:40f0:8", ["const:5098fc:8", "const:4:8"]]
- 005098fc ["CALL", null, ["callee:00c59b40:8"]]
+ 0052c794 ["INT_ADD", "register:40f0:8", ["const:52c794:8", "const:4:8"]]
+ 0052c794 ["CALL", null, ["callee:00c59b40:8"]]
- 005098fc bytes fd4d1b94
+ 0052c794 bytes ebb41c94
- 00509958 ["INT_ADD", "register:40f0:8", ["const:509958:8", "const:4:8"]]
- 00509958 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0052c7f0 ["INT_ADD", "register:40f0:8", ["const:52c7f0:8", "const:4:8"]]
+ 0052c7f0 ["CALL", null, ["callee:00c57ae0:8"]]
- 00509958 bytes ce451b94
+ 0052c7f0 bytes bcac1c94
~~~


<a id="compare-0d7e25be5908f409ad26dc8deb27b9a8"></a>

### [`0050995c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050995c.md) → [`0052c7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c7f4.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNS_17Certificate_StoreERKNSt6__ndk112basic_strin

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0052c038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c038.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054eed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eed0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005099b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050995c.md#insn-005099b8) · [`005099c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050995c.md#insn-005099c4) · [`00509a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050995c.md#insn-00509a00)
- 新版 `0052c850`（命令位置の公開資料なし） · `0052c85c`（命令位置の公開資料なし） · `0052c898`（命令位置の公開資料なし）

~~~diff
- 005099b8 ["INT_ADD", "register:40f0:8", ["const:5099b8:8", "const:4:8"]]
- 005099b8 ["CALL", null, ["callee:0054eed0:8"]]
+ 0052c850 ["INT_ADD", "register:40f0:8", ["const:52c850:8", "const:4:8"]]
+ 0052c850 ["CALL", null, ["callee:0054eed0:8"]]
- 005099b8 bytes a0890094
+ 0052c850 bytes a0890094
- 005099c4 ["INT_ADD", "register:40f0:8", ["const:5099c4:8", "const:4:8"]]
- 005099c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0052c85c ["INT_ADD", "register:40f0:8", ["const:52c85c:8", "const:4:8"]]
+ 0052c85c ["CALL", null, ["callee:00c57a90:8"]]
- 005099c4 bytes 9f451b94
+ 0052c85c bytes 8dac1c94
- 00509a00 ["INT_ADD", "register:40f0:8", ["const:509a00:8", "const:4:8"]]
- 00509a00 ["CALL", null, ["callee:00c59b40:8"]]
+ 0052c898 ["INT_ADD", "register:40f0:8", ["const:52c898:8", "const:4:8"]]
+ 0052c898 ["CALL", null, ["callee:00c59b40:8"]]
- 00509a00 bytes bc4d1b94
+ 0052c898 bytes aab41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24b88a8707bd4f77b7fa33be8ad99ce3"></a>

### [`00509ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md) → [`0052c958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md) _ZN5Botan28Path_Validation_RestrictionsC1Ebmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md#insn-00509b3c) · [`00509b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md#insn-00509b54) · [`00509b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md#insn-00509b88)
- 新版 `0052c9d4`（命令位置の公開資料なし） · `0052c9ec`（命令位置の公開資料なし） · `0052ca20`（命令位置の公開資料なし）

~~~diff
- 00509b3c ["INT_ADD", "register:40f0:8", ["const:509b3c:8", "const:4:8"]]
- 00509b3c ["CALL", null, ["callee:0054a5d4:8"]]
+ 0052c9d4 ["INT_ADD", "register:40f0:8", ["const:52c9d4:8", "const:4:8"]]
+ 0052c9d4 ["CALL", null, ["callee:0054a5d4:8"]]
- 00509b3c bytes 00770094
+ 0052c9d4 bytes 00770094
- 00509b54 ["INT_ADD", "register:40f0:8", ["const:509b54:8", "const:4:8"]]
- 00509b54 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052c9ec ["INT_ADD", "register:40f0:8", ["const:52c9ec:8", "const:4:8"]]
+ 0052c9ec ["CALL", null, ["callee:00c57ab0:8"]]
- 00509b54 bytes 43451b94
+ 0052c9ec bytes 31ac1c94
- 00509b88 ["INT_ADD", "register:40f0:8", ["const:509b88:8", "const:4:8"]]
- 00509b88 ["CALL", null, ["callee:0054a5d4:8"]]
+ 0052ca20 ["INT_ADD", "register:40f0:8", ["const:52ca20:8", "const:4:8"]]
+ 0052ca20 ["CALL", null, ["callee:0054a5d4:8"]]
- 00509b88 bytes ed760094
+ 0052ca20 bytes ed760094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9199b5bdc83ea1a525be8a213e4418d"></a>

### [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) → [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) _ZN5Botan22Path_Validation_ResultC1ENSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd100.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004deee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004deee0.md) [`00504ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md) [`0051c458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c458.md) [`0051c66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c66c.md)
- 新版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b50.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00501d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md) [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`0053f2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md) [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00509f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md#insn-00509f78) · [`00509fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md#insn-00509fa8) · [`00509fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md#insn-00509fb8)
- 新版 `0052ce10`（命令位置の公開資料なし） · `0052ce40`（命令位置の公開資料なし） · `0052ce50`（命令位置の公開資料なし）

~~~diff
- 00509f78 ["INT_ADD", "register:40f0:8", ["const:509f78:8", "const:4:8"]]
- 00509f78 ["CALL", null, ["callee:0054eb4c:8"]]
+ 0052ce10 ["INT_ADD", "register:40f0:8", ["const:52ce10:8", "const:4:8"]]
+ 0052ce10 ["CALL", null, ["callee:0054eb4c:8"]]
- 00509f78 bytes 4f870094
+ 0052ce10 bytes 4f870094
- 00509fa8 ["INT_ADD", "register:40f0:8", ["const:509fa8:8", "const:4:8"]]
- 00509fa8 ["CALL", null, ["callee:0053f2f0:8"]]
+ 0052ce40 ["INT_ADD", "register:40f0:8", ["const:52ce40:8", "const:4:8"]]
+ 0052ce40 ["CALL", null, ["callee:0053f2f0:8"]]
- 00509fa8 bytes 2c490094
+ 0052ce40 bytes 2c490094
- 00509fb8 ["INT_ADD", "register:40f0:8", ["const:509fb8:8", "const:4:8"]]
- 00509fb8 ["CALL", null, ["callee:0053f7d0:8"]]
+ 0052ce50 ["INT_ADD", "register:40f0:8", ["const:52ce50:8", "const:4:8"]]
+ 0052ce50 ["CALL", null, ["callee:0053f7d0:8"]]
- 00509fb8 bytes 604a0094
+ 0052ce50 bytes 604a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa36817bec479ebb3bb509c0d660c13"></a>

### [`0050a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md) → [`0052d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) _ZNK5Botan22Path_Validation_Result14trusted_hashesEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050a420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md#insn-0050a420) · [`0050a430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md#insn-0050a430) · [`0050a450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md#insn-0050a450)
- 新版 `0052d2b8`（命令位置の公開資料なし） · `0052d2c8`（命令位置の公開資料なし） · `0052d2e8`（命令位置の公開資料なし）

~~~diff
- 0050a420 ["INT_ADD", "register:40f0:8", ["const:50a420:8", "const:4:8"]]
- 0050a420 ["CALL", null, ["callee:00c59a90:8"]]
+ 0052d2b8 ["INT_ADD", "register:40f0:8", ["const:52d2b8:8", "const:4:8"]]
+ 0052d2b8 ["CALL", null, ["callee:00c59a90:8"]]
- 0050a420 bytes 084b1b94
+ 0052d2b8 bytes f6b11c94
- 0050a430 ["INT_ADD", "register:40f0:8", ["const:50a430:8", "const:4:8"]]
- 0050a430 ["CALL", null, ["callee:0054a5d4:8"]]
+ 0052d2c8 ["INT_ADD", "register:40f0:8", ["const:52d2c8:8", "const:4:8"]]
+ 0052d2c8 ["CALL", null, ["callee:0054a5d4:8"]]
- 0050a430 bytes c3740094
+ 0052d2c8 bytes c3740094
- 0050a450 ["INT_ADD", "register:40f0:8", ["const:50a450:8", "const:4:8"]]
- 0050a450 ["CALL", null, ["callee:00c57a90:8"]]
+ 0052d2e8 ["INT_ADD", "register:40f0:8", ["const:52d2e8:8", "const:4:8"]]
+ 0052d2e8 ["CALL", null, ["callee:00c57a90:8"]]
- 0050a450 bytes fc421b94
+ 0052d2e8 bytes eaa91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e81fa129ebbc101eb1cd934b15cebe"></a>

### [`0050ad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ad34.md) → [`0052dbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dbcc.md) FUN_0052dbcc

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ad58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ad34.md#insn-0050ad58) · [`0050ada0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ad34.md#insn-0050ada0) · [`0050adc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ad34.md#insn-0050adc0)
- 新版 `0052dbf0`（命令位置の公開資料なし） · `0052dc38`（命令位置の公開資料なし） · `0052dc58`（命令位置の公開資料なし）

~~~diff
- 0050ad58 ["INT_ADD", "register:40f0:8", ["const:50ad58:8", "const:4:8"]]
- 0050ad58 ["CALL", null, ["callee:00c57be0:8"]]
+ 0052dbf0 ["INT_ADD", "register:40f0:8", ["const:52dbf0:8", "const:4:8"]]
+ 0052dbf0 ["CALL", null, ["callee:00c57be0:8"]]
- 0050ad58 bytes 0e411b94
+ 0052dbf0 bytes fca71c94
- 0050ada0 ["INT_ADD", "register:40f0:8", ["const:50ada0:8", "const:4:8"]]
- 0050ada0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0052dc38 ["INT_ADD", "register:40f0:8", ["const:52dc38:8", "const:4:8"]]
+ 0052dc38 ["CALL", null, ["callee:00c57a90:8"]]
- 0050ada0 bytes a8401b94
+ 0052dc38 bytes 96a71c94
- 0050adc0 ["INT_ADD", "register:40f0:8", ["const:50adc0:8", "const:4:8"]]
- 0050adc0 ["CALL", null, ["callee:00c57b40:8"]]
+ 0052dc58 ["INT_ADD", "register:40f0:8", ["const:52dc58:8", "const:4:8"]]
+ 0052dc58 ["CALL", null, ["callee:00c57b40:8"]]
- 0050adc0 bytes cc401b94
+ 0052dc58 bytes baa71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8aca7bb011e0355cda6a419e59fe93e"></a>

### [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) → [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) FUN_0052dcc0

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 57件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) [`005a7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md) [`005b6778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00518dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md) [`0052c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c2bc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 63件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) [`005db448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db448.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ae78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md#insn-0050ae78) · [`0050aea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md#insn-0050aea8) · [`0050aec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md#insn-0050aec4)
- 新版 `0052dd10`（命令位置の公開資料なし） · `0052dd40`（命令位置の公開資料なし） · `0052dd5c`（命令位置の公開資料なし）

~~~diff
- 0050ae78 ["INT_ADD", "register:40f0:8", ["const:50ae78:8", "const:4:8"]]
- 0050ae78 ["CALL", null, ["callee:0043bb64:8"]]
+ 0052dd10 ["INT_ADD", "register:40f0:8", ["const:52dd10:8", "const:4:8"]]
+ 0052dd10 ["CALL", null, ["callee:0043bb64:8"]]
- 0050ae78 bytes 7b38fc97
+ 0052dd10 bytes 9537fc97
- 0050aea8 ["INT_ADD", "register:40f0:8", ["const:50aea8:8", "const:4:8"]]
- 0050aea8 ["CALL", null, ["callee:0054f154:8"]]
+ 0052dd40 ["INT_ADD", "register:40f0:8", ["const:52dd40:8", "const:4:8"]]
+ 0052dd40 ["CALL", null, ["callee:0054f154:8"]]
- 0050aea8 bytes 05850094
+ 0052dd40 bytes 05850094
- 0050aec4 ["INT_ADD", "register:40f0:8", ["const:50aec4:8", "const:4:8"]]
- 0050aec4 ["CALL", null, ["callee:0053bc70:8"]]
+ 0052dd5c ["INT_ADD", "register:40f0:8", ["const:52dd5c:8", "const:4:8"]]
+ 0052dd5c ["CALL", null, ["callee:0053bc70:8"]]
- 0050aec4 bytes c5370094
+ 0052dd5c bytes c5370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c5921a32ad9fd00c6388f3503c482a4"></a>

### [`0050c0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c0a4.md) → [`0052ef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef3c.md) FUN_0052ef3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c0a4.md#insn-0050c0c0)
- 新版 `0052ef58`（命令位置の公開資料なし）

~~~diff
- 0050c0c0 ["INT_ADD", "register:40f0:8", ["const:50c0c0:8", "const:4:8"]]
- 0050c0c0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052ef58 ["INT_ADD", "register:40f0:8", ["const:52ef58:8", "const:4:8"]]
+ 0052ef58 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050c0c0 bytes e83b1b94
+ 0052ef58 bytes d6a21c94
~~~


<a id="compare-e941672b56ddbbcd0d7b806bfc44df0b"></a>

### [`0050c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c1dc.md) → [`0052f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f074.md) FUN_0052f074

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050c0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c0e8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c1dc.md#insn-0050c1ec)
- 新版 `0052f084`（命令位置の公開資料なし）

~~~diff
- 0050c1ec ["INT_ADD", "register:40f0:8", ["const:50c1ec:8", "const:4:8"]]
- 0050c1ec ["CALL", null, ["callee:0052ef80:8"]]
+ 0052f084 ["INT_ADD", "register:40f0:8", ["const:52f084:8", "const:4:8"]]
+ 0052f084 ["CALL", null, ["callee:0052ef80:8"]]
- 0050c1ec bytes bfffff97
+ 0052f084 bytes bfffff97
~~~


<a id="compare-8c3f49a94130410eae0ae5c4cdbc3f81"></a>

### [`0050c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c4c8.md) → [`0052f360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f360.md) FUN_0052f360

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050c3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c3d4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c4c8.md#insn-0050c4d8)
- 新版 `0052f370`（命令位置の公開資料なし）

~~~diff
- 0050c4d8 ["INT_ADD", "register:40f0:8", ["const:50c4d8:8", "const:4:8"]]
- 0050c4d8 ["CALL", null, ["callee:0052f26c:8"]]
+ 0052f370 ["INT_ADD", "register:40f0:8", ["const:52f370:8", "const:4:8"]]
+ 0052f370 ["CALL", null, ["callee:0052f26c:8"]]
- 0050c4d8 bytes bfffff97
+ 0052f370 bytes bfffff97
~~~


<a id="compare-7f26f9d4b8d52ff5400b242383b451f5"></a>

### [`0050c7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c7b4.md) → [`0052f64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f64c.md) FUN_0052f64c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050c6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c6c0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050c7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c7b4.md#insn-0050c7c4)
- 新版 `0052f65c`（命令位置の公開資料なし）

~~~diff
- 0050c7c4 ["INT_ADD", "register:40f0:8", ["const:50c7c4:8", "const:4:8"]]
- 0050c7c4 ["CALL", null, ["callee:0052f558:8"]]
+ 0052f65c ["INT_ADD", "register:40f0:8", ["const:52f65c:8", "const:4:8"]]
+ 0052f65c ["CALL", null, ["callee:0052f558:8"]]
- 0050c7c4 bytes bfffff97
+ 0052f65c bytes bfffff97
~~~


<a id="compare-c03c55c73cccb822e52c1fefec368656"></a>

### [`0050cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cea4.md) → [`0052fd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd3c.md) FUN_0052fd3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cea4.md#insn-0050cec0) · [`0050ced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cea4.md#insn-0050ced0)
- 新版 `0052fd58`（命令位置の公開資料なし） · `0052fd68`（命令位置の公開資料なし）

~~~diff
- 0050cec0 ["INT_ADD", "register:40f0:8", ["const:50cec0:8", "const:4:8"]]
- 0050cec0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fd58 ["INT_ADD", "register:40f0:8", ["const:52fd58:8", "const:4:8"]]
+ 0052fd58 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cec0 bytes 68381b94
+ 0052fd58 bytes 569f1c94
- 0050ced0 ["INT_ADD", "register:40f0:8", ["const:50ced0:8", "const:4:8"]]
- 0050ced0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fd68 ["INT_ADD", "register:40f0:8", ["const:52fd68:8", "const:4:8"]]
+ 0052fd68 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050ced0 bytes 64381b94
+ 0052fd68 bytes 529f1c94
~~~


<a id="compare-85bffa0f651fb34cfb2d2c6d89a5430f"></a>

### [`0050cee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cee4.md) → [`0052fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd7c.md) FUN_0052fd7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cee4.md#insn-0050cf04)
- 新版 `0052fd9c`（命令位置の公開資料なし）

~~~diff
- 0050cf04 ["INT_ADD", "register:40f0:8", ["const:50cf04:8", "const:4:8"]]
- 0050cf04 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fd9c ["INT_ADD", "register:40f0:8", ["const:52fd9c:8", "const:4:8"]]
+ 0052fd9c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cf04 bytes 57381b94
+ 0052fd9c bytes 459f1c94
~~~


<a id="compare-32c46af9519fa9d1d54d3d75b341a0df"></a>

### [`0050cf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf18.md) → [`0052fdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdb0.md) FUN_0052fdb0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf18.md#insn-0050cf34) · [`0050cf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf18.md#insn-0050cf44)
- 新版 `0052fdcc`（命令位置の公開資料なし） · `0052fddc`（命令位置の公開資料なし）

~~~diff
- 0050cf34 ["INT_ADD", "register:40f0:8", ["const:50cf34:8", "const:4:8"]]
- 0050cf34 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fdcc ["INT_ADD", "register:40f0:8", ["const:52fdcc:8", "const:4:8"]]
+ 0052fdcc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cf34 bytes 4b381b94
+ 0052fdcc bytes 399f1c94
- 0050cf44 ["INT_ADD", "register:40f0:8", ["const:50cf44:8", "const:4:8"]]
- 0050cf44 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fddc ["INT_ADD", "register:40f0:8", ["const:52fddc:8", "const:4:8"]]
+ 0052fddc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cf44 bytes 47381b94
+ 0052fddc bytes 359f1c94
~~~


<a id="compare-36d10ce1216ed1cd33216c8d4ab7073d"></a>

### [`0050cf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf58.md) → [`0052fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdf0.md) FUN_0052fdf0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf58.md#insn-0050cf74) · [`0050cf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf58.md#insn-0050cf84)
- 新版 `0052fe0c`（命令位置の公開資料なし） · `0052fe1c`（命令位置の公開資料なし）

~~~diff
- 0050cf74 ["INT_ADD", "register:40f0:8", ["const:50cf74:8", "const:4:8"]]
- 0050cf74 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fe0c ["INT_ADD", "register:40f0:8", ["const:52fe0c:8", "const:4:8"]]
+ 0052fe0c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cf74 bytes 3b381b94
+ 0052fe0c bytes 299f1c94
- 0050cf84 ["INT_ADD", "register:40f0:8", ["const:50cf84:8", "const:4:8"]]
- 0050cf84 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
+ 0052fe1c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050cf84 bytes 37381b94
+ 0052fe1c bytes 259f1c94
~~~


<a id="compare-560af587be9d766ccbee3d34cb586e11"></a>

### [`0050d4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d4e4.md) → [`0053037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053037c.md) FUN_0053037c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050d410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d410.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005302a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050d4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d4e4.md#insn-0050d4f4)
- 新版 `0053038c`（命令位置の公開資料なし）

~~~diff
- 0050d4f4 ["INT_ADD", "register:40f0:8", ["const:50d4f4:8", "const:4:8"]]
- 0050d4f4 ["CALL", null, ["callee:005302a8:8"]]
+ 0053038c ["INT_ADD", "register:40f0:8", ["const:53038c:8", "const:4:8"]]
+ 0053038c ["CALL", null, ["callee:005302a8:8"]]
- 0050d4f4 bytes c7ffff97
+ 0053038c bytes c7ffff97
~~~


<a id="compare-ccdd6c7fc52e071119d82809a3bea34d"></a>

### [`0050d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d508.md) → [`005303a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md) FUN_005303a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004a8d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d508.md#insn-0050d518) · [`0050d520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d508.md#insn-0050d520)
- 新版 `005303b0`（命令位置の公開資料なし） · `005303b8`（命令位置の公開資料なし）

~~~diff
- 0050d518 ["INT_ADD", "register:40f0:8", ["const:50d518:8", "const:4:8"]]
- 0050d518 ["CALL", null, ["callee:00c57a90:8"]]
+ 005303b0 ["INT_ADD", "register:40f0:8", ["const:5303b0:8", "const:4:8"]]
+ 005303b0 ["CALL", null, ["callee:00c57a90:8"]]
- 0050d518 bytes ca361b94
+ 005303b0 bytes b89d1c94
- 0050d520 ["INT_ADD", "register:40f0:8", ["const:50d520:8", "const:4:8"]]
- 0050d520 ["CALL", null, ["callee:004cbc10:8"]]
+ 005303b8 ["INT_ADD", "register:40f0:8", ["const:5303b8:8", "const:4:8"]]
+ 005303b8 ["CALL", null, ["callee:004cbc10:8"]]
- 0050d520 bytes 166efe97
+ 005303b8 bytes 166efe97
~~~


<a id="compare-7ce104d631c3756e75e1bdf0b129a046"></a>

### [`0050d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d564.md) → [`005303fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303fc.md) FUN_005303fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d564.md#insn-0050d580) · [`0050d58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d564.md#insn-0050d58c)
- 新版 `00530418`（命令位置の公開資料なし） · `00530424`（命令位置の公開資料なし）

~~~diff
- 0050d580 ["INT_ADD", "register:40f0:8", ["const:50d580:8", "const:4:8"]]
- 0050d580 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00530418 ["INT_ADD", "register:40f0:8", ["const:530418:8", "const:4:8"]]
+ 00530418 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050d580 bytes b8361b94
+ 00530418 bytes a69d1c94
- 0050d58c ["INT_ADD", "register:40f0:8", ["const:50d58c:8", "const:4:8"]]
- 0050d58c ["CALL", null, ["callee:0053af50:8"]]
+ 00530424 ["INT_ADD", "register:40f0:8", ["const:530424:8", "const:4:8"]]
+ 00530424 ["CALL", null, ["callee:0053af50:8"]]
- 0050d58c bytes cb2a0094
+ 00530424 bytes cb2a0094
~~~


<a id="compare-cfa3a8ae638f8ea8829ad888addb43f6"></a>

### [`0050d738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d738.md) → [`005305d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005305d0.md) FUN_005305d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050d760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d738.md#insn-0050d760)
- 新版 `005305f8`（命令位置の公開資料なし）

~~~diff
- 0050d760 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d760 ["INT_ADD", "register:40f0:8", ["const:50d760:8", "const:4:8"]]
- 0050d760 ["CALLIND", null, ["register:0:8"]]
+ 005305f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005305f8 ["INT_ADD", "register:40f0:8", ["const:5305f8:8", "const:4:8"]]
+ 005305f8 ["CALLIND", null, ["register:0:8"]]
- 0050d760 bytes 20013fd6
+ 005305f8 bytes 20013fd6
~~~


<a id="compare-e6a5bc389b0cad7db2ba10d396b26c96"></a>

### [`0050d9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d9e0.md) → [`00530878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md) FUN_00530878

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050d9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d9e0.md#insn-0050d9f0)
- 新版 `00530888`（命令位置の公開資料なし）

~~~diff
- 0050d9f0 ["INT_ADD", "register:40f0:8", ["const:50d9f0:8", "const:4:8"]]
- 0050d9f0 ["CALL", null, ["callee:0053078c:8"]]
+ 00530888 ["INT_ADD", "register:40f0:8", ["const:530888:8", "const:4:8"]]
+ 00530888 ["CALL", null, ["callee:0053078c:8"]]
- 0050d9f0 bytes c1ffff97
+ 00530888 bytes c1ffff97
~~~


<a id="compare-d379533a9a672be35530f68167bc2ce4"></a>

### [`0050da74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da74.md) → [`0053090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md) FUN_0053090c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050da88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da74.md#insn-0050da88)
- 新版 `00530920`（命令位置の公開資料なし）

~~~diff
- 0050da88 ["INT_ADD", "register:40f0:8", ["const:50da88:8", "const:4:8"]]
- 0050da88 ["CALL", null, ["callee:0053078c:8"]]
+ 00530920 ["INT_ADD", "register:40f0:8", ["const:530920:8", "const:4:8"]]
+ 00530920 ["CALL", null, ["callee:0053078c:8"]]
- 0050da88 bytes 9bffff97
+ 00530920 bytes 9bffff97
~~~


<a id="compare-65085ab2923e99947ddfafc4fb797bd4"></a>

### [`0050db70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db70.md) → [`00530a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md) FUN_00530a08

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050da9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050db80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db70.md#insn-0050db80)
- 新版 `00530a18`（命令位置の公開資料なし）

~~~diff
- 0050db80 ["INT_ADD", "register:40f0:8", ["const:50db80:8", "const:4:8"]]
- 0050db80 ["CALL", null, ["callee:00530934:8"]]
+ 00530a18 ["INT_ADD", "register:40f0:8", ["const:530a18:8", "const:4:8"]]
+ 00530a18 ["CALL", null, ["callee:00530934:8"]]
- 0050db80 bytes c7ffff97
+ 00530a18 bytes c7ffff97
~~~


<a id="compare-20a18ad7072357246e9e1f0cdf8802b8"></a>

### [`0050db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db94.md) → [`00530a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md) FUN_00530a2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004a8854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050dba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db94.md#insn-0050dba4) · [`0050dbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db94.md#insn-0050dbac)
- 新版 `00530a3c`（命令位置の公開資料なし） · `00530a44`（命令位置の公開資料なし）

~~~diff
- 0050dba4 ["INT_ADD", "register:40f0:8", ["const:50dba4:8", "const:4:8"]]
- 0050dba4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00530a3c ["INT_ADD", "register:40f0:8", ["const:530a3c:8", "const:4:8"]]
+ 00530a3c ["CALL", null, ["callee:00c57a90:8"]]
- 0050dba4 bytes 27351b94
+ 00530a3c bytes 159c1c94
- 0050dbac ["INT_ADD", "register:40f0:8", ["const:50dbac:8", "const:4:8"]]
- 0050dbac ["CALL", null, ["callee:004cb6ec:8"]]
+ 00530a44 ["INT_ADD", "register:40f0:8", ["const:530a44:8", "const:4:8"]]
+ 00530a44 ["CALL", null, ["callee:004cb6ec:8"]]
- 0050dbac bytes 2a6bfe97
+ 00530a44 bytes 2a6bfe97
~~~


<a id="compare-cf067b3779d911260a9a9003c61459f3"></a>

### [`0050dee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dee4.md) → [`00530d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md) FUN_00530d7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004a8bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dee4.md#insn-0050def4) · [`0050defc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dee4.md#insn-0050defc)
- 新版 `00530d8c`（命令位置の公開資料なし） · `00530d94`（命令位置の公開資料なし）

~~~diff
- 0050def4 ["INT_ADD", "register:40f0:8", ["const:50def4:8", "const:4:8"]]
- 0050def4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00530d8c ["INT_ADD", "register:40f0:8", ["const:530d8c:8", "const:4:8"]]
+ 00530d8c ["CALL", null, ["callee:00c57a90:8"]]
- 0050def4 bytes 53341b94
+ 00530d8c bytes 419b1c94
- 0050defc ["INT_ADD", "register:40f0:8", ["const:50defc:8", "const:4:8"]]
- 0050defc ["CALL", null, ["callee:004cba5c:8"]]
+ 00530d94 ["INT_ADD", "register:40f0:8", ["const:530d94:8", "const:4:8"]]
+ 00530d94 ["CALL", null, ["callee:004cba5c:8"]]
- 0050defc bytes 326bfe97
+ 00530d94 bytes 326bfe97
~~~


<a id="compare-6880e4c4d2313989bc69c2147f9fc4f3"></a>

### [`0050df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050df4c.md) → [`00530de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530de4.md) FUN_00530de4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050df68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050df4c.md#insn-0050df68) · [`0050dfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050df4c.md#insn-0050dfa0) · [`0050dfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050df4c.md#insn-0050dfb0)
- 新版 `00530e00`（命令位置の公開資料なし） · `00530e38`（命令位置の公開資料なし） · `00530e48`（命令位置の公開資料なし）

~~~diff
- 0050df68 ["INT_ADD", "register:40f0:8", ["const:50df68:8", "const:4:8"]]
- 0050df68 ["CALL", null, ["callee:0053b3e4:8"]]
+ 00530e00 ["INT_ADD", "register:40f0:8", ["const:530e00:8", "const:4:8"]]
+ 00530e00 ["CALL", null, ["callee:0053b3e4:8"]]
- 0050df68 bytes 79290094
+ 00530e00 bytes 79290094
- 0050dfa0 ["INT_ADD", "register:40f0:8", ["const:50dfa0:8", "const:4:8"]]
- 0050dfa0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00530e38 ["INT_ADD", "register:40f0:8", ["const:530e38:8", "const:4:8"]]
+ 00530e38 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050dfa0 bytes 30341b94
+ 00530e38 bytes 1e9b1c94
- 0050dfb0 ["INT_ADD", "register:40f0:8", ["const:50dfb0:8", "const:4:8"]]
- 0050dfb0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00530e48 ["INT_ADD", "register:40f0:8", ["const:530e48:8", "const:4:8"]]
+ 00530e48 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050dfb0 bytes 2c341b94
+ 00530e48 bytes 1a9b1c94
~~~


<a id="compare-74895b84f7faa2dbe5bf643489950296"></a>

### [`0050e3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e3f8.md) → [`00531290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531290.md) FUN_00531290

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e3f8.md#insn-0050e418)
- 新版 `005312b0`（命令位置の公開資料なし）

~~~diff
- 0050e418 ["INT_ADD", "register:40f0:8", ["const:50e418:8", "const:4:8"]]
- 0050e418 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005312b0 ["INT_ADD", "register:40f0:8", ["const:5312b0:8", "const:4:8"]]
+ 005312b0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050e418 bytes 12331b94
+ 005312b0 bytes 009a1c94
~~~


<a id="compare-f9b4959fd5764d986cc87352dee8742c"></a>

### [`0050e600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e600.md) → [`00531498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531498.md) FUN_00531498

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e600.md#insn-0050e620)
- 新版 `005314b8`（命令位置の公開資料なし）

~~~diff
- 0050e620 ["INT_ADD", "register:40f0:8", ["const:50e620:8", "const:4:8"]]
- 0050e620 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005314b8 ["INT_ADD", "register:40f0:8", ["const:5314b8:8", "const:4:8"]]
+ 005314b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050e620 bytes 90321b94
+ 005314b8 bytes 7e991c94
~~~


<a id="compare-6307d45366c9f5e83bbb09243c134664"></a>

### [`0050e644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e644.md) → [`005314dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314dc.md) FUN_005314dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e644.md#insn-0050e65c) · [`0050e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e644.md#insn-0050e668)
- 新版 `005314f4`（命令位置の公開資料なし） · `00531500`（命令位置の公開資料なし）

~~~diff
- 0050e65c ["INT_ADD", "register:40f0:8", ["const:50e65c:8", "const:4:8"]]
- 0050e65c ["CALL", null, ["callee:0053af50:8"]]
+ 005314f4 ["INT_ADD", "register:40f0:8", ["const:5314f4:8", "const:4:8"]]
+ 005314f4 ["CALL", null, ["callee:0053af50:8"]]
- 0050e65c bytes 97260094
+ 005314f4 bytes 97260094
- 0050e668 ["INT_ADD", "register:40f0:8", ["const:50e668:8", "const:4:8"]]
- 0050e668 ["CALL", null, ["callee:0046d450:8"]]
+ 00531500 ["INT_ADD", "register:40f0:8", ["const:531500:8", "const:4:8"]]
+ 00531500 ["CALL", null, ["callee:0046d450:8"]]
- 0050e668 bytes d4effc97
+ 00531500 bytes d4effc97
~~~


<a id="compare-f854835d722239aa9f6b72d67f15f645"></a>

### [`0050e7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e7cc.md) → [`00531664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531664.md) FUN_00531664

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e7cc.md#insn-0050e7e4)
- 新版 `0053167c`（命令位置の公開資料なし）

~~~diff
- 0050e7e4 ["INT_ADD", "register:40f0:8", ["const:50e7e4:8", "const:4:8"]]
- 0050e7e4 ["CALL", null, ["callee:0053af50:8"]]
+ 0053167c ["INT_ADD", "register:40f0:8", ["const:53167c:8", "const:4:8"]]
+ 0053167c ["CALL", null, ["callee:0053af50:8"]]
- 0050e7e4 bytes 35260094
+ 0053167c bytes 35260094
~~~


<a id="compare-2c9394f3675669f7f9f7fdf750f02ae9"></a>

### [`0050e7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e7fc.md) → [`00531694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531694.md) FUN_00531694

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e7fc.md#insn-0050e814) · [`0050e820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e7fc.md#insn-0050e820)
- 新版 `005316ac`（命令位置の公開資料なし） · `005316b8`（命令位置の公開資料なし）

~~~diff
- 0050e814 ["INT_ADD", "register:40f0:8", ["const:50e814:8", "const:4:8"]]
- 0050e814 ["CALL", null, ["callee:0053af50:8"]]
+ 005316ac ["INT_ADD", "register:40f0:8", ["const:5316ac:8", "const:4:8"]]
+ 005316ac ["CALL", null, ["callee:0053af50:8"]]
- 0050e814 bytes 29260094
+ 005316ac bytes 29260094
- 0050e820 ["INT_ADD", "register:40f0:8", ["const:50e820:8", "const:4:8"]]
- 0050e820 ["CALL", null, ["callee:0046d450:8"]]
+ 005316b8 ["INT_ADD", "register:40f0:8", ["const:5316b8:8", "const:4:8"]]
+ 005316b8 ["CALL", null, ["callee:0046d450:8"]]
- 0050e820 bytes 66effc97
+ 005316b8 bytes 66effc97
~~~


<a id="compare-3c644b252cc3e5ab831116868c746d16"></a>

### [`0050e99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e99c.md) → [`00531834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531834.md) FUN_00531834

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e99c.md#insn-0050e9b4)
- 新版 `0053184c`（命令位置の公開資料なし）

~~~diff
- 0050e9b4 ["INT_ADD", "register:40f0:8", ["const:50e9b4:8", "const:4:8"]]
- 0050e9b4 ["CALL", null, ["callee:0053af50:8"]]
+ 0053184c ["INT_ADD", "register:40f0:8", ["const:53184c:8", "const:4:8"]]
+ 0053184c ["CALL", null, ["callee:0053af50:8"]]
- 0050e9b4 bytes c1250094
+ 0053184c bytes c1250094
~~~


<a id="compare-d305b8bf817bc1836211c01526b262af"></a>

### [`0050e9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e9cc.md) → [`00531864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531864.md) FUN_00531864

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050e9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e9cc.md#insn-0050e9e4) · [`0050e9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e9cc.md#insn-0050e9f0)
- 新版 `0053187c`（命令位置の公開資料なし） · `00531888`（命令位置の公開資料なし）

~~~diff
- 0050e9e4 ["INT_ADD", "register:40f0:8", ["const:50e9e4:8", "const:4:8"]]
- 0050e9e4 ["CALL", null, ["callee:0053af50:8"]]
+ 0053187c ["INT_ADD", "register:40f0:8", ["const:53187c:8", "const:4:8"]]
+ 0053187c ["CALL", null, ["callee:0053af50:8"]]
- 0050e9e4 bytes b5250094
+ 0053187c bytes b5250094
- 0050e9f0 ["INT_ADD", "register:40f0:8", ["const:50e9f0:8", "const:4:8"]]
- 0050e9f0 ["CALL", null, ["callee:0046d450:8"]]
+ 00531888 ["INT_ADD", "register:40f0:8", ["const:531888:8", "const:4:8"]]
+ 00531888 ["CALL", null, ["callee:0046d450:8"]]
- 0050e9f0 bytes f2eefc97
+ 00531888 bytes f2eefc97
~~~


<a id="compare-b0747085794e6c282c222844a8b3e843"></a>

### [`0050ec34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ec34.md) → [`00531acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531acc.md) FUN_00531acc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ec7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ec34.md#insn-0050ec7c)
- 新版 `00531b14`（命令位置の公開資料なし）

~~~diff
- 0050ec7c ["INT_ADD", "register:40f0:8", ["const:50ec7c:8", "const:4:8"]]
- 0050ec7c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00531b14 ["INT_ADD", "register:40f0:8", ["const:531b14:8", "const:4:8"]]
+ 00531b14 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050ec7c bytes f9301b94
+ 00531b14 bytes e7971c94
~~~


<a id="compare-81ec469d136c279bf694088ecec8f45a"></a>

### [`0050ecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ecac.md) → [`00531b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md) FUN_00531b44

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004ec514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ecf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ecac.md#insn-0050ecf4) · [`0050ed04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ecac.md#insn-0050ed04)
- 新版 `00531b8c`（命令位置の公開資料なし） · `00531b9c`（命令位置の公開資料なし）

~~~diff
- 0050ecf4 ["INT_ADD", "register:40f0:8", ["const:50ecf4:8", "const:4:8"]]
- 0050ecf4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00531b8c ["INT_ADD", "register:40f0:8", ["const:531b8c:8", "const:4:8"]]
+ 00531b8c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050ecf4 bytes db301b94
+ 00531b8c bytes c9971c94
- 0050ed04 ["INT_ADD", "register:40f0:8", ["const:50ed04:8", "const:4:8"]]
- 0050ed04 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00531b9c ["INT_ADD", "register:40f0:8", ["const:531b9c:8", "const:4:8"]]
+ 00531b9c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050ed04 bytes d7301b94
+ 00531b9c bytes c5971c94
~~~


<a id="compare-65720baf94c9601619313653e9c6dcf4"></a>

### [`0050ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee5c.md) → [`00531cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cf4.md) FUN_00531cf4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004f7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050ee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee5c.md#insn-0050ee70)
- 新版 `00531d08`（命令位置の公開資料なし）

~~~diff
- 0050ee70 ["INT_ADD", "register:40f0:8", ["const:50ee70:8", "const:4:8"]]
- 0050ee70 ["CALL", null, ["callee:0051ac84:8"]]
+ 00531d08 ["INT_ADD", "register:40f0:8", ["const:531d08:8", "const:4:8"]]
+ 00531d08 ["CALL", null, ["callee:0051ac84:8"]]
- 0050ee70 bytes dfa3ff97
+ 00531d08 bytes dfa3ff97
~~~


<a id="compare-ae48c559584bf05763c1759d1ae75cd1"></a>

### [`0050f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f0a4.md) → [`00531f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531f3c.md) FUN_00531f3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f0a4.md#insn-0050f0ec)
- 新版 `00531f84`（命令位置の公開資料なし）

~~~diff
- 0050f0ec ["INT_ADD", "register:40f0:8", ["const:50f0ec:8", "const:4:8"]]
- 0050f0ec ["CALL", null, ["callee:00c57ab0:8"]]
+ 00531f84 ["INT_ADD", "register:40f0:8", ["const:531f84:8", "const:4:8"]]
+ 00531f84 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f0ec bytes dd2f1b94
+ 00531f84 bytes cb961c94
~~~


<a id="compare-e3f6aeb644cfdd6819104325ca8c2355"></a>

### [`0050f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f11c.md) → [`00531fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531fb4.md) FUN_00531fb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f11c.md#insn-0050f164) · [`0050f174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f11c.md#insn-0050f174)
- 新版 `00531ffc`（命令位置の公開資料なし） · `0053200c`（命令位置の公開資料なし）

~~~diff
- 0050f164 ["INT_ADD", "register:40f0:8", ["const:50f164:8", "const:4:8"]]
- 0050f164 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00531ffc ["INT_ADD", "register:40f0:8", ["const:531ffc:8", "const:4:8"]]
+ 00531ffc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f164 bytes bf2f1b94
+ 00531ffc bytes ad961c94
- 0050f174 ["INT_ADD", "register:40f0:8", ["const:50f174:8", "const:4:8"]]
- 0050f174 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053200c ["INT_ADD", "register:40f0:8", ["const:53200c:8", "const:4:8"]]
+ 0053200c ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f174 bytes bb2f1b94
+ 0053200c bytes a9961c94
~~~


<a id="compare-8e4bf1115a5191695e37bac31e6c3412"></a>

### [`0050f35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f35c.md) → [`005321f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005321f4.md) FUN_005321f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f35c.md#insn-0050f3a8) · [`0050f3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f35c.md#insn-0050f3b8)
- 新版 `00532240`（命令位置の公開資料なし） · `00532250`（命令位置の公開資料なし）

~~~diff
- 0050f3a8 ["INT_ADD", "register:40f0:8", ["const:50f3a8:8", "const:4:8"]]
- 0050f3a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532240 ["INT_ADD", "register:40f0:8", ["const:532240:8", "const:4:8"]]
+ 00532240 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f3a8 bytes 2e2f1b94
+ 00532240 bytes 1c961c94
- 0050f3b8 ["INT_ADD", "register:40f0:8", ["const:50f3b8:8", "const:4:8"]]
- 0050f3b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532250 ["INT_ADD", "register:40f0:8", ["const:532250:8", "const:4:8"]]
+ 00532250 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f3b8 bytes 2a2f1b94
+ 00532250 bytes 18961c94
~~~


<a id="compare-a14d2e873e9b1eeefc7b43c97b15b2e4"></a>

### [`0050f3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f3e8.md) → [`00532280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532280.md) FUN_00532280

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f3e8.md#insn-0050f434) · [`0050f444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f3e8.md#insn-0050f444) · [`0050f454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f3e8.md#insn-0050f454)
- 新版 `005322cc`（命令位置の公開資料なし） · `005322dc`（命令位置の公開資料なし） · `005322ec`（命令位置の公開資料なし）

~~~diff
- 0050f434 ["INT_ADD", "register:40f0:8", ["const:50f434:8", "const:4:8"]]
- 0050f434 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005322cc ["INT_ADD", "register:40f0:8", ["const:5322cc:8", "const:4:8"]]
+ 005322cc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f434 bytes 0b2f1b94
+ 005322cc bytes f9951c94
- 0050f444 ["INT_ADD", "register:40f0:8", ["const:50f444:8", "const:4:8"]]
- 0050f444 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005322dc ["INT_ADD", "register:40f0:8", ["const:5322dc:8", "const:4:8"]]
+ 005322dc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f444 bytes 072f1b94
+ 005322dc bytes f5951c94
- 0050f454 ["INT_ADD", "register:40f0:8", ["const:50f454:8", "const:4:8"]]
- 0050f454 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005322ec ["INT_ADD", "register:40f0:8", ["const:5322ec:8", "const:4:8"]]
+ 005322ec ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f454 bytes 032f1b94
+ 005322ec bytes f1951c94
~~~


<a id="compare-3cc85eb989e4256aa2fb9532894b78ff"></a>

### [`0050f7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f7e8.md) → [`00532680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532680.md) FUN_00532680

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f7e8.md#insn-0050f834) · [`0050f844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f7e8.md#insn-0050f844) · [`0050f86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f7e8.md#insn-0050f86c)
- 新版 `005326cc`（命令位置の公開資料なし） · `005326dc`（命令位置の公開資料なし） · `00532704`（命令位置の公開資料なし）

~~~diff
- 0050f834 ["INT_ADD", "register:40f0:8", ["const:50f834:8", "const:4:8"]]
- 0050f834 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005326cc ["INT_ADD", "register:40f0:8", ["const:5326cc:8", "const:4:8"]]
+ 005326cc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f834 bytes 0b2e1b94
+ 005326cc bytes f9941c94
- 0050f844 ["INT_ADD", "register:40f0:8", ["const:50f844:8", "const:4:8"]]
- 0050f844 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005326dc ["INT_ADD", "register:40f0:8", ["const:5326dc:8", "const:4:8"]]
+ 005326dc ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f844 bytes 072e1b94
+ 005326dc bytes f5941c94
- 0050f86c ["INT_ADD", "register:40f0:8", ["const:50f86c:8", "const:4:8"]]
- 0050f86c ["CALL", null, ["callee:0053af50:8"]]
+ 00532704 ["INT_ADD", "register:40f0:8", ["const:532704:8", "const:4:8"]]
+ 00532704 ["CALL", null, ["callee:0053af50:8"]]
- 0050f86c bytes 13220094
+ 00532704 bytes 13220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ef2b1f8c36673b39007f978f873950"></a>

### [`0050f8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f8b4.md) → [`0053274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053274c.md) FUN_0053274c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f8b4.md#insn-0050f900) · [`0050f910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f8b4.md#insn-0050f910) · [`0050f938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f8b4.md#insn-0050f938)
- 新版 `00532798`（命令位置の公開資料なし） · `005327a8`（命令位置の公開資料なし） · `005327d0`（命令位置の公開資料なし）

~~~diff
- 0050f900 ["INT_ADD", "register:40f0:8", ["const:50f900:8", "const:4:8"]]
- 0050f900 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532798 ["INT_ADD", "register:40f0:8", ["const:532798:8", "const:4:8"]]
+ 00532798 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f900 bytes d82d1b94
+ 00532798 bytes c6941c94
- 0050f910 ["INT_ADD", "register:40f0:8", ["const:50f910:8", "const:4:8"]]
- 0050f910 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005327a8 ["INT_ADD", "register:40f0:8", ["const:5327a8:8", "const:4:8"]]
+ 005327a8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050f910 bytes d42d1b94
+ 005327a8 bytes c2941c94
- 0050f938 ["INT_ADD", "register:40f0:8", ["const:50f938:8", "const:4:8"]]
- 0050f938 ["CALL", null, ["callee:0053af50:8"]]
+ 005327d0 ["INT_ADD", "register:40f0:8", ["const:5327d0:8", "const:4:8"]]
+ 005327d0 ["CALL", null, ["callee:0053af50:8"]]
- 0050f938 bytes e0210094
+ 005327d0 bytes e0210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35190233cd936c8c406718b8567bf0b4"></a>

### [`0050f988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f988.md) → [`00532820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532820.md) FUN_00532820

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f988.md#insn-0050f9a0)
- 新版 `00532838`（命令位置の公開資料なし）

~~~diff
- 0050f9a0 ["INT_ADD", "register:40f0:8", ["const:50f9a0:8", "const:4:8"]]
- 0050f9a0 ["CALL", null, ["callee:0053af50:8"]]
+ 00532838 ["INT_ADD", "register:40f0:8", ["const:532838:8", "const:4:8"]]
+ 00532838 ["CALL", null, ["callee:0053af50:8"]]
- 0050f9a0 bytes c6210094
+ 00532838 bytes c6210094
~~~


<a id="compare-e40b501119ecfbdfece974ceba51f211"></a>

### [`0050f9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9b8.md) → [`00532850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532850.md) FUN_00532850

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050f9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9b8.md#insn-0050f9d0) · [`0050f9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9b8.md#insn-0050f9dc)
- 新版 `00532868`（命令位置の公開資料なし） · `00532874`（命令位置の公開資料なし）

~~~diff
- 0050f9d0 ["INT_ADD", "register:40f0:8", ["const:50f9d0:8", "const:4:8"]]
- 0050f9d0 ["CALL", null, ["callee:0053af50:8"]]
+ 00532868 ["INT_ADD", "register:40f0:8", ["const:532868:8", "const:4:8"]]
+ 00532868 ["CALL", null, ["callee:0053af50:8"]]
- 0050f9d0 bytes ba210094
+ 00532868 bytes ba210094
- 0050f9dc ["INT_ADD", "register:40f0:8", ["const:50f9dc:8", "const:4:8"]]
- 0050f9dc ["CALL", null, ["callee:0046d450:8"]]
+ 00532874 ["INT_ADD", "register:40f0:8", ["const:532874:8", "const:4:8"]]
+ 00532874 ["CALL", null, ["callee:0046d450:8"]]
- 0050f9dc bytes f7eafc97
+ 00532874 bytes f7eafc97
~~~


<a id="compare-bdd53dc82d00ae5bf292ffd021d588b8"></a>

### [`0050fb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fb48.md) → [`005329e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005329e0.md) FUN_005329e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fb48.md#insn-0050fb60)
- 新版 `005329f8`（命令位置の公開資料なし）

~~~diff
- 0050fb60 ["INT_ADD", "register:40f0:8", ["const:50fb60:8", "const:4:8"]]
- 0050fb60 ["CALL", null, ["callee:0053af50:8"]]
+ 005329f8 ["INT_ADD", "register:40f0:8", ["const:5329f8:8", "const:4:8"]]
+ 005329f8 ["CALL", null, ["callee:0053af50:8"]]
- 0050fb60 bytes 56210094
+ 005329f8 bytes 56210094
~~~


<a id="compare-a7cfd56e1b38574b9ad4f01720ed6354"></a>

### [`0050fb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fb78.md) → [`00532a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532a10.md) FUN_00532a10

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fb78.md#insn-0050fb90) · [`0050fb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fb78.md#insn-0050fb9c)
- 新版 `00532a28`（命令位置の公開資料なし） · `00532a34`（命令位置の公開資料なし）

~~~diff
- 0050fb90 ["INT_ADD", "register:40f0:8", ["const:50fb90:8", "const:4:8"]]
- 0050fb90 ["CALL", null, ["callee:0053af50:8"]]
+ 00532a28 ["INT_ADD", "register:40f0:8", ["const:532a28:8", "const:4:8"]]
+ 00532a28 ["CALL", null, ["callee:0053af50:8"]]
- 0050fb90 bytes 4a210094
+ 00532a28 bytes 4a210094
- 0050fb9c ["INT_ADD", "register:40f0:8", ["const:50fb9c:8", "const:4:8"]]
- 0050fb9c ["CALL", null, ["callee:0046d450:8"]]
+ 00532a34 ["INT_ADD", "register:40f0:8", ["const:532a34:8", "const:4:8"]]
+ 00532a34 ["CALL", null, ["callee:0046d450:8"]]
- 0050fb9c bytes 87eafc97
+ 00532a34 bytes 87eafc97
~~~


<a id="compare-cbd594817cd87886fbc04e4de277f9b4"></a>

### [`0050fd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fd34.md) → [`00532bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532bcc.md) FUN_00532bcc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0051d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fdbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fd34.md#insn-0050fdbc) · [`0050fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fd34.md#insn-0050fdf4) · [`0050fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fd34.md#insn-0050fe18)
- 新版 `00532c54`（命令位置の公開資料なし） · `00532c8c`（命令位置の公開資料なし） · `00532cb0`（命令位置の公開資料なし）

~~~diff
- 0050fdbc ["INT_ADD", "register:40f0:8", ["const:50fdbc:8", "const:4:8"]]
- 0050fdbc ["CALL", null, ["callee:00c57a90:8"]]
+ 00532c54 ["INT_ADD", "register:40f0:8", ["const:532c54:8", "const:4:8"]]
+ 00532c54 ["CALL", null, ["callee:00c57a90:8"]]
- 0050fdbc bytes a12c1b94
+ 00532c54 bytes 8f931c94
- 0050fdf4 ["INT_ADD", "register:40f0:8", ["const:50fdf4:8", "const:4:8"]]
- 0050fdf4 ["CALL", null, ["callee:0043bb64:8"]]
+ 00532c8c ["INT_ADD", "register:40f0:8", ["const:532c8c:8", "const:4:8"]]
+ 00532c8c ["CALL", null, ["callee:0043bb64:8"]]
- 0050fdf4 bytes 9c24fc97
+ 00532c8c bytes b623fc97
- 0050fe18 ["INT_ADD", "register:40f0:8", ["const:50fe18:8", "const:4:8"]]
- 0050fe18 ["CALL", null, ["callee:0054087c:8"]]
+ 00532cb0 ["INT_ADD", "register:40f0:8", ["const:532cb0:8", "const:4:8"]]
+ 00532cb0 ["CALL", null, ["callee:0054087c:8"]]
- 0050fe18 bytes f3360094
+ 00532cb0 bytes f3360094
~~~


<a id="compare-a875f83350bd72a7dd27b0d4f1a1efdb"></a>

### [`0050fe1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fe1c.md) → [`00532cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cb4.md) FUN_00532cb4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fe1c.md#insn-0050fe38)
- 新版 `00532cd0`（命令位置の公開資料なし）

~~~diff
- 0050fe38 ["INT_ADD", "register:40f0:8", ["const:50fe38:8", "const:4:8"]]
- 0050fe38 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532cd0 ["INT_ADD", "register:40f0:8", ["const:532cd0:8", "const:4:8"]]
+ 00532cd0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050fe38 bytes 8a2c1b94
+ 00532cd0 bytes 78931c94
~~~


<a id="compare-17a1d9c7349510d78dc3b0860a9ebfbc"></a>

### [`0050fe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fe60.md) → [`00532cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cf8.md) FUN_00532cf8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0050fe7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fe60.md#insn-0050fe7c) · [`0050fe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fe60.md#insn-0050fe8c)
- 新版 `00532d14`（命令位置の公開資料なし） · `00532d24`（命令位置の公開資料なし）

~~~diff
- 0050fe7c ["INT_ADD", "register:40f0:8", ["const:50fe7c:8", "const:4:8"]]
- 0050fe7c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532d14 ["INT_ADD", "register:40f0:8", ["const:532d14:8", "const:4:8"]]
+ 00532d14 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050fe7c bytes 792c1b94
+ 00532d14 bytes 67931c94
- 0050fe8c ["INT_ADD", "register:40f0:8", ["const:50fe8c:8", "const:4:8"]]
- 0050fe8c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00532d24 ["INT_ADD", "register:40f0:8", ["const:532d24:8", "const:4:8"]]
+ 00532d24 ["CALL", null, ["callee:00c57ab0:8"]]
- 0050fe8c bytes 752c1b94
+ 00532d24 bytes 63931c94
~~~


<a id="compare-231c03d7a2f2969a556c994cfb415c29"></a>

### [`00510074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510074.md) → [`00532f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md) FUN_00532f0c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510074.md#insn-00510084)
- 新版 `00532f1c`（命令位置の公開資料なし）

~~~diff
- 00510084 ["INT_ADD", "register:40f0:8", ["const:510084:8", "const:4:8"]]
- 00510084 ["CALL", null, ["callee:00532e3c:8"]]
+ 00532f1c ["INT_ADD", "register:40f0:8", ["const:532f1c:8", "const:4:8"]]
+ 00532f1c ["CALL", null, ["callee:00532e3c:8"]]
- 00510084 bytes c8ffff97
+ 00532f1c bytes c8ffff97
~~~


<a id="compare-ed9bea8507d9b4cdc20e8b6be7f3825c"></a>

### [`00510254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510254.md) → [`005330ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md) FUN_005330ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005100e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510254.md#insn-00510264)
- 新版 `005330fc`（命令位置の公開資料なし）

~~~diff
- 00510264 ["INT_ADD", "register:40f0:8", ["const:510264:8", "const:4:8"]]
- 00510264 ["CALL", null, ["callee:00532f78:8"]]
+ 005330fc ["INT_ADD", "register:40f0:8", ["const:5330fc:8", "const:4:8"]]
+ 005330fc ["CALL", null, ["callee:00532f78:8"]]
- 00510264 bytes 9fffff97
+ 005330fc bytes 9fffff97
~~~


<a id="compare-ab9cd7794ed91eeb4b37a104fb72ee3e"></a>

### [`00510278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510278.md) → [`00533110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533110.md) FUN_00533110

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510278.md#insn-00510294) · [`005102a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510278.md#insn-005102a4)
- 新版 `0053312c`（命令位置の公開資料なし） · `0053313c`（命令位置の公開資料なし）

~~~diff
- 00510294 ["INT_ADD", "register:40f0:8", ["const:510294:8", "const:4:8"]]
- 00510294 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053312c ["INT_ADD", "register:40f0:8", ["const:53312c:8", "const:4:8"]]
+ 0053312c ["CALL", null, ["callee:00c57ab0:8"]]
- 00510294 bytes 732b1b94
+ 0053312c bytes 61921c94
- 005102a4 ["INT_ADD", "register:40f0:8", ["const:5102a4:8", "const:4:8"]]
- 005102a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053313c ["INT_ADD", "register:40f0:8", ["const:53313c:8", "const:4:8"]]
+ 0053313c ["CALL", null, ["callee:00c57ab0:8"]]
- 005102a4 bytes 6f2b1b94
+ 0053313c bytes 5d921c94
~~~


<a id="compare-73690e61fef64f51d9599f0866e043de"></a>

### [`005102b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005102b8.md) → [`00533150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533150.md) FUN_00533150

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005102d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005102b8.md#insn-005102d4) · [`005102e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005102b8.md#insn-005102e4)
- 新版 `0053316c`（命令位置の公開資料なし） · `0053317c`（命令位置の公開資料なし）

~~~diff
- 005102d4 ["INT_ADD", "register:40f0:8", ["const:5102d4:8", "const:4:8"]]
- 005102d4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053316c ["INT_ADD", "register:40f0:8", ["const:53316c:8", "const:4:8"]]
+ 0053316c ["CALL", null, ["callee:00c57ab0:8"]]
- 005102d4 bytes 632b1b94
+ 0053316c bytes 51921c94
- 005102e4 ["INT_ADD", "register:40f0:8", ["const:5102e4:8", "const:4:8"]]
- 005102e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
+ 0053317c ["CALL", null, ["callee:00c57ab0:8"]]
- 005102e4 bytes 5f2b1b94
+ 0053317c bytes 4d921c94
~~~


<a id="compare-11381d1351bfcf9e29bda3722ec23716"></a>

### [`005102f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005102f8.md) → [`00533190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533190.md) FUN_00533190

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005102f8.md#insn-00510314)
- 新版 `005331ac`（命令位置の公開資料なし）

~~~diff
- 00510314 ["INT_ADD", "register:40f0:8", ["const:510314:8", "const:4:8"]]
- 00510314 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
+ 005331ac ["CALL", null, ["callee:00c57ab0:8"]]
- 00510314 bytes 532b1b94
+ 005331ac bytes 41921c94
~~~


<a id="compare-e7df59dd122c49e5734d57110ccc41d7"></a>

### [`00510344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510344.md) → [`005331dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005331dc.md) FUN_005331dc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510344.md#insn-00510360) · [`00510378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510344.md#insn-00510378)
- 新版 `005331f8`（命令位置の公開資料なし） · `00533210`（命令位置の公開資料なし）

~~~diff
- 00510360 ["INT_ADD", "register:40f0:8", ["const:510360:8", "const:4:8"]]
- 00510360 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005331f8 ["INT_ADD", "register:40f0:8", ["const:5331f8:8", "const:4:8"]]
+ 005331f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00510360 bytes 402b1b94
+ 005331f8 bytes 2e921c94
- 00510378 ["COPY", "register:0:8", ["register:4040:8"]]
- 00510378 ["INT_ADD", "register:40f0:8", ["const:510378:8", "const:4:8"]]
- 00510378 ["CALLIND", null, ["register:0:8"]]
+ 00533210 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00533210 ["INT_ADD", "register:40f0:8", ["const:533210:8", "const:4:8"]]
+ 00533210 ["CALLIND", null, ["register:0:8"]]
- 00510378 bytes 00013fd6
+ 00533210 bytes 00013fd6
~~~


<a id="compare-276f5d2f3c6ac62efb4d0ce5e5aefd23"></a>

### [`005104e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md) → [`00533378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md) FUN_00533378

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md#insn-00510504) · [`00510514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md#insn-00510514) · [`00510524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md#insn-00510524)
- 新版 `0053339c`（命令位置の公開資料なし） · `005333ac`（命令位置の公開資料なし） · `005333bc`（命令位置の公開資料なし）

~~~diff
- 00510504 ["INT_ADD", "register:40f0:8", ["const:510504:8", "const:4:8"]]
- 00510504 ["CALL", null, ["callee:00c57a90:8"]]
+ 0053339c ["INT_ADD", "register:40f0:8", ["const:53339c:8", "const:4:8"]]
+ 0053339c ["CALL", null, ["callee:00c57a90:8"]]
- 00510504 bytes cf2a1b94
+ 0053339c bytes bd911c94
- 00510514 ["INT_ADD", "register:40f0:8", ["const:510514:8", "const:4:8"]]
- 00510514 ["CALL", null, ["callee:00c59100:8"]]
+ 005333ac ["INT_ADD", "register:40f0:8", ["const:5333ac:8", "const:4:8"]]
+ 005333ac ["CALL", null, ["callee:00c59100:8"]]
- 00510514 bytes 67301b94
+ 005333ac bytes 55971c94
- 00510524 ["INT_ADD", "register:40f0:8", ["const:510524:8", "const:4:8"]]
- 00510524 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005333bc ["INT_ADD", "register:40f0:8", ["const:5333bc:8", "const:4:8"]]
+ 005333bc ["CALL", null, ["callee:00c57ab0:8"]]
- 00510524 bytes cf2a1b94
+ 005333bc bytes bd911c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2d1d150a7cfa6eb361e09d0deee9cb2"></a>

### [`005106a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005106a4.md) → [`0053353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053353c.md) FUN_0053353c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005106cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005106a4.md#insn-005106cc)
- 新版 `00533564`（命令位置の公開資料なし）

~~~diff
- 005106cc ["COPY", "register:0:8", ["register:4048:8"]]
- 005106cc ["INT_ADD", "register:40f0:8", ["const:5106cc:8", "const:4:8"]]
- 005106cc ["CALLIND", null, ["register:0:8"]]
+ 00533564 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533564 ["INT_ADD", "register:40f0:8", ["const:533564:8", "const:4:8"]]
+ 00533564 ["CALLIND", null, ["register:0:8"]]
- 005106cc bytes 20013fd6
+ 00533564 bytes 20013fd6
~~~


<a id="compare-f96b577b009f34a85d43ef9ac825f8b1"></a>

### [`00510820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510820.md) → [`005336b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005336b8.md) FUN_005336b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510820.md#insn-00510834) · [`0051084c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510820.md#insn-0051084c) · [`0051085c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510820.md#insn-0051085c)
- 新版 `005336cc`（命令位置の公開資料なし） · `005336e4`（命令位置の公開資料なし） · `005336f4`（命令位置の公開資料なし）

~~~diff
- 00510834 ["INT_ADD", "register:40f0:8", ["const:510834:8", "const:4:8"]]
- 00510834 ["CALL", null, ["callee:00c57a90:8"]]
+ 005336cc ["INT_ADD", "register:40f0:8", ["const:5336cc:8", "const:4:8"]]
+ 005336cc ["CALL", null, ["callee:00c57a90:8"]]
- 00510834 bytes 032a1b94
+ 005336cc bytes f1901c94
- 0051084c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051084c ["INT_ADD", "register:40f0:8", ["const:51084c:8", "const:4:8"]]
- 0051084c ["CALLIND", null, ["register:0:8"]]
+ 005336e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005336e4 ["INT_ADD", "register:40f0:8", ["const:5336e4:8", "const:4:8"]]
+ 005336e4 ["CALLIND", null, ["register:0:8"]]
- 0051084c bytes 20013fd6
+ 005336e4 bytes 20013fd6
- 0051085c ["INT_ADD", "register:40f0:8", ["const:51085c:8", "const:4:8"]]
- 0051085c ["CALL", null, ["callee:00c59130:8"]]
+ 005336f4 ["INT_ADD", "register:40f0:8", ["const:5336f4:8", "const:4:8"]]
+ 005336f4 ["CALL", null, ["callee:00c59130:8"]]
- 0051085c bytes a12f1b94
+ 005336f4 bytes 8f961c94
~~~


<a id="compare-91bb7c1ff35bfb2f256140252e7899ee"></a>

### [`00510960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510960.md) → [`005337f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md) FUN_005337f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00510894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510960.md#insn-00510970)
- 新版 `00533808`（命令位置の公開資料なし）

~~~diff
- 00510970 ["INT_ADD", "register:40f0:8", ["const:510970:8", "const:4:8"]]
- 00510970 ["CALL", null, ["callee:0053372c:8"]]
+ 00533808 ["INT_ADD", "register:40f0:8", ["const:533808:8", "const:4:8"]]
+ 00533808 ["CALL", null, ["callee:0053372c:8"]]
- 00510970 bytes c9ffff97
+ 00533808 bytes c9ffff97
~~~


<a id="compare-ab246aeb1aa7494d06f83ff3f6b36da5"></a>

### [`00510be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510be8.md) → [`00533a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md) FUN_00533a80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00510acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510be8.md#insn-00510bf8)
- 新版 `00533a90`（命令位置の公開資料なし）

~~~diff
- 00510bf8 ["INT_ADD", "register:40f0:8", ["const:510bf8:8", "const:4:8"]]
- 00510bf8 ["CALL", null, ["callee:00533964:8"]]
+ 00533a90 ["INT_ADD", "register:40f0:8", ["const:533a90:8", "const:4:8"]]
+ 00533a90 ["CALL", null, ["callee:00533964:8"]]
- 00510bf8 bytes b5ffff97
+ 00533a90 bytes b5ffff97
~~~


<a id="compare-3b133f16212d57e315ac08ea31e85cd2"></a>

### [`00510c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c14.md) → [`00533aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md) FUN_00533aac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00510acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00510c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c14.md#insn-00510c28)
- 新版 `00533ac0`（命令位置の公開資料なし）

~~~diff
- 00510c28 ["INT_ADD", "register:40f0:8", ["const:510c28:8", "const:4:8"]]
- 00510c28 ["CALL", null, ["callee:00533964:8"]]
+ 00533ac0 ["INT_ADD", "register:40f0:8", ["const:533ac0:8", "const:4:8"]]
+ 00533ac0 ["CALL", null, ["callee:00533964:8"]]
- 00510c28 bytes a9ffff97
+ 00533ac0 bytes a9ffff97
~~~


<a id="compare-882e55ea7c1ff6b7d9bca4ab6348b19b"></a>

### [`0051179c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051179c.md) → [`00534634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534634.md) FUN_00534634

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005117e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051179c.md#insn-005117e8) · [`005117fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051179c.md#insn-005117fc) · [`00511804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051179c.md#insn-00511804)
- 新版 `00534680`（命令位置の公開資料なし） · `00534694`（命令位置の公開資料なし） · `0053469c`（命令位置の公開資料なし）

~~~diff
- 005117e8 ["INT_ADD", "register:40f0:8", ["const:5117e8:8", "const:4:8"]]
- 005117e8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00534680 ["INT_ADD", "register:40f0:8", ["const:534680:8", "const:4:8"]]
+ 00534680 ["CALL", null, ["callee:00c538e0:8"]]
- 005117e8 bytes aa151b94
+ 00534680 bytes 987c1c94
- 005117fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005117fc ["INT_ADD", "register:40f0:8", ["const:5117fc:8", "const:4:8"]]
- 005117fc ["CALLIND", null, ["register:0:8"]]
+ 00534694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00534694 ["INT_ADD", "register:40f0:8", ["const:534694:8", "const:4:8"]]
+ 00534694 ["CALLIND", null, ["register:0:8"]]
- 005117fc bytes 00013fd6
+ 00534694 bytes 00013fd6
- 00511804 ["INT_ADD", "register:40f0:8", ["const:511804:8", "const:4:8"]]
- 00511804 ["CALL", null, ["callee:00c57a80:8"]]
+ 0053469c ["INT_ADD", "register:40f0:8", ["const:53469c:8", "const:4:8"]]
+ 0053469c ["CALL", null, ["callee:00c57a80:8"]]
- 00511804 bytes 0b261b94
+ 0053469c bytes f98c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9364d415a51400769f9e979bf809a3"></a>

### [`00511894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511894.md) → [`0053472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053472c.md) FUN_0053472c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005118b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511894.md#insn-005118b0) · [`005118d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511894.md#insn-005118d0)
- 新版 `00534748`（命令位置の公開資料なし） · `00534768`（命令位置の公開資料なし）

~~~diff
- 005118b0 ["INT_ADD", "register:40f0:8", ["const:5118b0:8", "const:4:8"]]
- 005118b0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00534748 ["INT_ADD", "register:40f0:8", ["const:534748:8", "const:4:8"]]
+ 00534748 ["CALL", null, ["callee:00c538e0:8"]]
- 005118b0 bytes 78151b94
+ 00534748 bytes 667c1c94
- 005118d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005118d0 ["INT_ADD", "register:40f0:8", ["const:5118d0:8", "const:4:8"]]
- 005118d0 ["CALLIND", null, ["register:0:8"]]
+ 00534768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00534768 ["INT_ADD", "register:40f0:8", ["const:534768:8", "const:4:8"]]
+ 00534768 ["CALLIND", null, ["register:0:8"]]
- 005118d0 bytes 00013fd6
+ 00534768 bytes 00013fd6
~~~


<a id="compare-11b3657ff46f6227a46089fa0f6fe473"></a>

### [`005118e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005118e4.md) → [`0053477c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053477c.md) FUN_0053477c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00511904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005118e4.md#insn-00511904) · [`00511918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005118e4.md#insn-00511918) · [`00511920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005118e4.md#insn-00511920)
- 新版 `0053479c`（命令位置の公開資料なし） · `005347b0`（命令位置の公開資料なし） · `005347b8`（命令位置の公開資料なし）

~~~diff
- 00511904 ["INT_ADD", "register:40f0:8", ["const:511904:8", "const:4:8"]]
- 00511904 ["CALL", null, ["callee:00c538e0:8"]]
+ 0053479c ["INT_ADD", "register:40f0:8", ["const:53479c:8", "const:4:8"]]
+ 0053479c ["CALL", null, ["callee:00c538e0:8"]]
- 00511904 bytes 63151b94
+ 0053479c bytes 517c1c94
- 00511918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00511918 ["INT_ADD", "register:40f0:8", ["const:511918:8", "const:4:8"]]
- 00511918 ["CALLIND", null, ["register:0:8"]]
+ 005347b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005347b0 ["INT_ADD", "register:40f0:8", ["const:5347b0:8", "const:4:8"]]
+ 005347b0 ["CALLIND", null, ["register:0:8"]]
- 00511918 bytes 00013fd6
+ 005347b0 bytes 00013fd6
- 00511920 ["INT_ADD", "register:40f0:8", ["const:511920:8", "const:4:8"]]
- 00511920 ["CALL", null, ["callee:00c57a80:8"]]
+ 005347b8 ["INT_ADD", "register:40f0:8", ["const:5347b8:8", "const:4:8"]]
+ 005347b8 ["CALL", null, ["callee:00c57a80:8"]]
- 00511920 bytes c4251b94
+ 005347b8 bytes b28c1c94
~~~


<a id="compare-c1805b0181f76c059affedda5b363b01"></a>

### [`005121d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005121d0.md) → [`00535068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535068.md) FUN_00535068

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005121f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005121d0.md#insn-005121f4)
- 新版 `0053508c`（命令位置の公開資料なし）

~~~diff
- 005121f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005121f4 ["INT_ADD", "register:40f0:8", ["const:5121f4:8", "const:4:8"]]
- 005121f4 ["CALLIND", null, ["register:0:8"]]
+ 0053508c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053508c ["INT_ADD", "register:40f0:8", ["const:53508c:8", "const:4:8"]]
+ 0053508c ["CALLIND", null, ["register:0:8"]]
- 005121f4 bytes 00013fd6
+ 0053508c bytes 00013fd6
~~~


<a id="compare-2596c2c352554a8003696e7c816c3f2e"></a>

### [`00512208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512208.md) → [`005350a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350a0.md) FUN_005350a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512208.md#insn-0051222c) · [`00512234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512208.md#insn-00512234)
- 新版 `005350c4`（命令位置の公開資料なし） · `005350cc`（命令位置の公開資料なし）

~~~diff
- 0051222c ["COPY", "register:0:8", ["register:4040:8"]]
- 0051222c ["INT_ADD", "register:40f0:8", ["const:51222c:8", "const:4:8"]]
- 0051222c ["CALLIND", null, ["register:0:8"]]
+ 005350c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005350c4 ["INT_ADD", "register:40f0:8", ["const:5350c4:8", "const:4:8"]]
+ 005350c4 ["CALLIND", null, ["register:0:8"]]
- 0051222c bytes 00013fd6
+ 005350c4 bytes 00013fd6
- 00512234 ["INT_ADD", "register:40f0:8", ["const:512234:8", "const:4:8"]]
- 00512234 ["CALL", null, ["callee:00c57a60:8"]]
+ 005350cc ["INT_ADD", "register:40f0:8", ["const:5350cc:8", "const:4:8"]]
+ 005350cc ["CALL", null, ["callee:00c57a60:8"]]
- 00512234 bytes 77231b94
+ 005350cc bytes 658a1c94
~~~


<a id="compare-fb7a05866d736ff5bcdf2581e7e81863"></a>

### [`00512248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512248.md) → [`005350e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005350e0.md) FUN_005350e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512248.md#insn-00512268) · [`00512280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512248.md#insn-00512280)
- 新版 `00535100`（命令位置の公開資料なし） · `00535118`（命令位置の公開資料なし）

~~~diff
- 00512268 ["INT_ADD", "register:40f0:8", ["const:512268:8", "const:4:8"]]
- 00512268 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00535100 ["INT_ADD", "register:40f0:8", ["const:535100:8", "const:4:8"]]
+ 00535100 ["CALL", null, ["callee:00c57ce0:8"]]
- 00512268 bytes 0a241b94
+ 00535100 bytes f88a1c94
- 00512280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512280 ["INT_ADD", "register:40f0:8", ["const:512280:8", "const:4:8"]]
- 00512280 ["CALLIND", null, ["register:0:8"]]
+ 00535118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535118 ["INT_ADD", "register:40f0:8", ["const:535118:8", "const:4:8"]]
+ 00535118 ["CALLIND", null, ["register:0:8"]]
- 00512280 bytes 00013fd6
+ 00535118 bytes 00013fd6
~~~


<a id="compare-251dc41b595d2b54178e0ab0f6bce43d"></a>

### [`005122ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005122ac.md) → [`00535144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535144.md) FUN_00535144

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005122cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005122ac.md#insn-005122cc) · [`005122e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005122ac.md#insn-005122e4)
- 新版 `00535164`（命令位置の公開資料なし） · `0053517c`（命令位置の公開資料なし）

~~~diff
- 005122cc ["INT_ADD", "register:40f0:8", ["const:5122cc:8", "const:4:8"]]
- 005122cc ["CALL", null, ["callee:00c57ce0:8"]]
+ 00535164 ["INT_ADD", "register:40f0:8", ["const:535164:8", "const:4:8"]]
+ 00535164 ["CALL", null, ["callee:00c57ce0:8"]]
- 005122cc bytes f1231b94
+ 00535164 bytes df8a1c94
- 005122e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005122e4 ["INT_ADD", "register:40f0:8", ["const:5122e4:8", "const:4:8"]]
- 005122e4 ["CALLIND", null, ["register:0:8"]]
+ 0053517c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053517c ["INT_ADD", "register:40f0:8", ["const:53517c:8", "const:4:8"]]
+ 0053517c ["CALLIND", null, ["register:0:8"]]
- 005122e4 bytes 00013fd6
+ 0053517c bytes 00013fd6
~~~


<a id="compare-e67bac4c1bc6492115280fd67b5ea41b"></a>

### [`00512310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512310.md) → [`005351a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351a8.md) FUN_005351a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512310.md#insn-00512328) · [`0051233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512310.md#insn-0051233c)
- 新版 `005351c0`（命令位置の公開資料なし） · `005351d4`（命令位置の公開資料なし）

~~~diff
- 00512328 ["INT_ADD", "register:40f0:8", ["const:512328:8", "const:4:8"]]
- 00512328 ["CALL", null, ["callee:00c57ce0:8"]]
+ 005351c0 ["INT_ADD", "register:40f0:8", ["const:5351c0:8", "const:4:8"]]
+ 005351c0 ["CALL", null, ["callee:00c57ce0:8"]]
- 00512328 bytes da231b94
+ 005351c0 bytes c88a1c94
- 0051233c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051233c ["INT_ADD", "register:40f0:8", ["const:51233c:8", "const:4:8"]]
- 0051233c ["CALLIND", null, ["register:0:8"]]
+ 005351d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005351d4 ["INT_ADD", "register:40f0:8", ["const:5351d4:8", "const:4:8"]]
+ 005351d4 ["CALLIND", null, ["register:0:8"]]
- 0051233c bytes 20013fd6
+ 005351d4 bytes 20013fd6
~~~


<a id="compare-b8b9be91207367742a6dcff81e92fdbe"></a>

### [`00512364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512364.md) → [`005351fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005351fc.md) FUN_005351fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00512378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512364.md#insn-00512378) · [`00512388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512364.md#insn-00512388)
- 新版 `00535210`（命令位置の公開資料なし） · `00535220`（命令位置の公開資料なし）

~~~diff
- 00512378 ["INT_ADD", "register:40f0:8", ["const:512378:8", "const:4:8"]]
- 00512378 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00535210 ["INT_ADD", "register:40f0:8", ["const:535210:8", "const:4:8"]]
+ 00535210 ["CALL", null, ["callee:00c57ce0:8"]]
- 00512378 bytes c6231b94
+ 00535210 bytes b48a1c94
- 00512388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512388 ["INT_ADD", "register:40f0:8", ["const:512388:8", "const:4:8"]]
- 00512388 ["CALLIND", null, ["register:0:8"]]
+ 00535220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535220 ["INT_ADD", "register:40f0:8", ["const:535220:8", "const:4:8"]]
+ 00535220 ["CALLIND", null, ["register:0:8"]]
- 00512388 bytes 00013fd6
+ 00535220 bytes 00013fd6
~~~


<a id="compare-f0e1b2b9dad54c54beff28bb060e9243"></a>

### [`005123b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005123b0.md) → [`00535248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535248.md) FUN_00535248

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005123c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005123b0.md#insn-005123c4) · [`005123d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005123b0.md#insn-005123d4) · [`005123e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005123b0.md#insn-005123e0)
- 新版 `0053525c`（命令位置の公開資料なし） · `0053526c`（命令位置の公開資料なし） · `00535278`（命令位置の公開資料なし）

~~~diff
- 005123c4 ["INT_ADD", "register:40f0:8", ["const:5123c4:8", "const:4:8"]]
- 005123c4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0053525c ["INT_ADD", "register:40f0:8", ["const:53525c:8", "const:4:8"]]
+ 0053525c ["CALL", null, ["callee:00c57ce0:8"]]
- 005123c4 bytes b3231b94
+ 0053525c bytes a18a1c94
- 005123d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005123d4 ["INT_ADD", "register:40f0:8", ["const:5123d4:8", "const:4:8"]]
- 005123d4 ["CALLIND", null, ["register:0:8"]]
+ 0053526c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053526c ["INT_ADD", "register:40f0:8", ["const:53526c:8", "const:4:8"]]
+ 0053526c ["CALLIND", null, ["register:0:8"]]
- 005123d4 bytes 00013fd6
+ 0053526c bytes 00013fd6
- 005123e0 ["INT_ADD", "register:40f0:8", ["const:5123e0:8", "const:4:8"]]
- 005123e0 ["CALL", null, ["callee:00c57cf0:8"]]
+ 00535278 ["INT_ADD", "register:40f0:8", ["const:535278:8", "const:4:8"]]
+ 00535278 ["CALL", null, ["callee:00c57cf0:8"]]
- 005123e0 bytes b0231b94
+ 00535278 bytes 9e8a1c94
~~~


<a id="compare-a00e0f63d42a3283791b3259d21fdffa"></a>

### [`00512408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512408.md) → [`005352a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005352a0.md) FUN_005352a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512408.md#insn-0051242c) · [`00512448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512408.md#insn-00512448) · [`00512454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512408.md#insn-00512454)
- 新版 `005352c4`（命令位置の公開資料なし） · `005352e0`（命令位置の公開資料なし） · `005352ec`（命令位置の公開資料なし）

~~~diff
- 0051242c ["INT_ADD", "register:40f0:8", ["const:51242c:8", "const:4:8"]]
- 0051242c ["CALL", null, ["callee:00c57ce0:8"]]
+ 005352c4 ["INT_ADD", "register:40f0:8", ["const:5352c4:8", "const:4:8"]]
+ 005352c4 ["CALL", null, ["callee:00c57ce0:8"]]
- 0051242c bytes 99231b94
+ 005352c4 bytes 878a1c94
- 00512448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00512448 ["INT_ADD", "register:40f0:8", ["const:512448:8", "const:4:8"]]
- 00512448 ["CALLIND", null, ["register:0:8"]]
+ 005352e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005352e0 ["INT_ADD", "register:40f0:8", ["const:5352e0:8", "const:4:8"]]
+ 005352e0 ["CALLIND", null, ["register:0:8"]]
- 00512448 bytes 00013fd6
+ 005352e0 bytes 00013fd6
- 00512454 ["INT_ADD", "register:40f0:8", ["const:512454:8", "const:4:8"]]
- 00512454 ["CALL", null, ["callee:00c57cf0:8"]]
+ 005352ec ["INT_ADD", "register:40f0:8", ["const:5352ec:8", "const:4:8"]]
+ 005352ec ["CALL", null, ["callee:00c57cf0:8"]]
- 00512454 bytes 93231b94
+ 005352ec bytes 818a1c94
~~~


<a id="compare-f1b0cf43f042de1840e01661f8b74a3f"></a>

### [`005134cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005134cc.md) → [`00536364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536364.md) FUN_00536364

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005134f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005134cc.md#insn-005134f4)
- 新版 `0053638c`（命令位置の公開資料なし）

~~~diff
- 005134f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005134f4 ["INT_ADD", "register:40f0:8", ["const:5134f4:8", "const:4:8"]]
- 005134f4 ["CALLIND", null, ["register:0:8"]]
+ 0053638c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053638c ["INT_ADD", "register:40f0:8", ["const:53638c:8", "const:4:8"]]
+ 0053638c ["CALLIND", null, ["register:0:8"]]
- 005134f4 bytes 20013fd6
+ 0053638c bytes 20013fd6
~~~


<a id="compare-4805b4b40400d6ec8f75b171252987b0"></a>

### [`00513a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513a04.md) → [`0053689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053689c.md) FUN_0053689c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c8d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00513a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513a04.md#insn-00513a28) · [`00513a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513a04.md#insn-00513a70) · [`00513a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513a04.md#insn-00513a90)
- 新版 `005368c0`（命令位置の公開資料なし） · `00536908`（命令位置の公開資料なし） · `00536928`（命令位置の公開資料なし）

~~~diff
- 00513a28 ["INT_ADD", "register:40f0:8", ["const:513a28:8", "const:4:8"]]
- 00513a28 ["CALL", null, ["callee:00c57be0:8"]]
+ 005368c0 ["INT_ADD", "register:40f0:8", ["const:5368c0:8", "const:4:8"]]
+ 005368c0 ["CALL", null, ["callee:00c57be0:8"]]
- 00513a28 bytes da1d1b94
+ 005368c0 bytes c8841c94
- 00513a70 ["INT_ADD", "register:40f0:8", ["const:513a70:8", "const:4:8"]]
- 00513a70 ["CALL", null, ["callee:00c57a90:8"]]
+ 00536908 ["INT_ADD", "register:40f0:8", ["const:536908:8", "const:4:8"]]
+ 00536908 ["CALL", null, ["callee:00c57a90:8"]]
- 00513a70 bytes 741d1b94
+ 00536908 bytes 62841c94
- 00513a90 ["INT_ADD", "register:40f0:8", ["const:513a90:8", "const:4:8"]]
- 00513a90 ["CALL", null, ["callee:00c57b40:8"]]
+ 00536928 ["INT_ADD", "register:40f0:8", ["const:536928:8", "const:4:8"]]
+ 00536928 ["CALL", null, ["callee:00c57b40:8"]]
- 00513a90 bytes 981d1b94
+ 00536928 bytes 86841c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd29596fc0e8e14de3ec2884a3bfd888"></a>

### [`00514ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514ae8.md) → [`00537980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537980.md) FUN_00537980

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md) [`00bdc4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md) [`00c58f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00514b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514ae8.md#insn-00514b00)
- 新版 `00537998`（命令位置の公開資料なし）

~~~diff
- 00514b00 ["INT_ADD", "register:40f0:8", ["const:514b00:8", "const:4:8"]]
- 00514b00 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00537998 ["INT_ADD", "register:40f0:8", ["const:537998:8", "const:4:8"]]
+ 00537998 ["CALL", null, ["callee:00c58ef0:8"]]
- 00514b00 bytes 681e1b94
+ 00537998 bytes 56851c94
~~~


<a id="compare-f763d2531337b5087fce9c37a56c3dd6"></a>

### [`00516b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516b3c.md) → [`005399d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/005399d4.md) FUN_005399d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00516b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516b3c.md#insn-00516b50)
- 新版 `005399e8`（命令位置の公開資料なし）

~~~diff
- 00516b50 ["INT_ADD", "register:40f0:8", ["const:516b50:8", "const:4:8"]]
- 00516b50 ["CALL", null, ["callee:00c593d0:8"]]
+ 005399e8 ["INT_ADD", "register:40f0:8", ["const:5399e8:8", "const:4:8"]]
+ 005399e8 ["CALL", null, ["callee:00c593d0:8"]]
- 00516b50 bytes 8c171b94
+ 005399e8 bytes 7a7e1c94
~~~


<a id="compare-b836a7235ff86c72c4cae63000f51b30"></a>

### [`00516f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516f90.md) → [`00539e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539e28.md) FUN_00539e28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00516fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516f90.md#insn-00516fd4) · [`00517004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516f90.md#insn-00517004) · [`00517038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516f90.md#insn-00517038)
- 新版 `00539e6c`（命令位置の公開資料なし） · `00539e9c`（命令位置の公開資料なし） · `00539ed0`（命令位置の公開資料なし）

~~~diff
- 00516fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516fd4 ["INT_ADD", "register:40f0:8", ["const:516fd4:8", "const:4:8"]]
- 00516fd4 ["CALLIND", null, ["register:0:8"]]
+ 00539e6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00539e6c ["INT_ADD", "register:40f0:8", ["const:539e6c:8", "const:4:8"]]
+ 00539e6c ["CALLIND", null, ["register:0:8"]]
- 00516fd4 bytes 00013fd6
+ 00539e6c bytes 00013fd6
- 00517004 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517004 ["INT_ADD", "register:40f0:8", ["const:517004:8", "const:4:8"]]
- 00517004 ["CALLIND", null, ["register:0:8"]]
+ 00539e9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00539e9c ["INT_ADD", "register:40f0:8", ["const:539e9c:8", "const:4:8"]]
+ 00539e9c ["CALLIND", null, ["register:0:8"]]
- 00517004 bytes 00013fd6
+ 00539e9c bytes 00013fd6
- 00517038 ["INT_ADD", "register:40f0:8", ["const:517038:8", "const:4:8"]]
- 00517038 ["CALL", null, ["callee:00459d34:8"]]
+ 00539ed0 ["INT_ADD", "register:40f0:8", ["const:539ed0:8", "const:4:8"]]
+ 00539ed0 ["CALL", null, ["callee:00459d34:8"]]
- 00517038 bytes 997ffc97
+ 00539ed0 bytes 997ffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-985b52072de19b8ee63d51955c134568"></a>

### [`00517044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md) → [`00539edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md) FUN_00539edc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004d9024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005170e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md#insn-005170e0) · [`0051712c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md#insn-0051712c) · [`00517178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md#insn-00517178)
- 新版 `00539f78`（命令位置の公開資料なし） · `00539fc4`（命令位置の公開資料なし） · `0053a010`（命令位置の公開資料なし）

~~~diff
- 005170e0 ["INT_ADD", "register:40f0:8", ["const:5170e0:8", "const:4:8"]]
- 005170e0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00539f78 ["INT_ADD", "register:40f0:8", ["const:539f78:8", "const:4:8"]]
+ 00539f78 ["CALL", null, ["callee:00c57ab0:8"]]
- 005170e0 bytes e00f1b94
+ 00539f78 bytes ce761c94
- 0051712c ["INT_ADD", "register:40f0:8", ["const:51712c:8", "const:4:8"]]
- 0051712c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00539fc4 ["INT_ADD", "register:40f0:8", ["const:539fc4:8", "const:4:8"]]
+ 00539fc4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051712c bytes cd0f1b94
+ 00539fc4 bytes bb761c94
- 00517178 ["INT_ADD", "register:40f0:8", ["const:517178:8", "const:4:8"]]
- 00517178 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053a010 ["INT_ADD", "register:40f0:8", ["const:53a010:8", "const:4:8"]]
+ 0053a010 ["CALL", null, ["callee:00c57ab0:8"]]
- 00517178 bytes ba0f1b94
+ 0053a010 bytes a8761c94
~~~


<a id="compare-3f4e12c14dd2f710d809c800628dfa3e"></a>

### [`005171dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md) → [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) FUN_0053a074

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004d9024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051769c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/0051769c.md) [`00517824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517824.md) [`005179b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005179b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md) [`0053a6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md) [`0053a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md#insn-00517274) · [`005172b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md#insn-005172b8) · [`005172c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md#insn-005172c8)
- 新版 `0053a10c`（命令位置の公開資料なし） · `0053a150`（命令位置の公開資料なし） · `0053a160`（命令位置の公開資料なし）

~~~diff
- 00517274 ["INT_ADD", "register:40f0:8", ["const:517274:8", "const:4:8"]]
- 00517274 ["CALL", null, ["callee:00c57b40:8"]]
+ 0053a10c ["INT_ADD", "register:40f0:8", ["const:53a10c:8", "const:4:8"]]
+ 0053a10c ["CALL", null, ["callee:00c57b40:8"]]
- 00517274 bytes 9f0f1b94
+ 0053a10c bytes 8d761c94
- 005172b8 ["INT_ADD", "register:40f0:8", ["const:5172b8:8", "const:4:8"]]
- 005172b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0053a150 ["INT_ADD", "register:40f0:8", ["const:53a150:8", "const:4:8"]]
+ 0053a150 ["CALL", null, ["callee:00c57a90:8"]]
- 005172b8 bytes 620f1b94
+ 0053a150 bytes 50761c94
- 005172c8 ["INT_ADD", "register:40f0:8", ["const:5172c8:8", "const:4:8"]]
- 005172c8 ["CALL", null, ["callee:0053a534:8"]]
+ 0053a160 ["INT_ADD", "register:40f0:8", ["const:53a160:8", "const:4:8"]]
+ 0053a160 ["CALL", null, ["callee:0053a534:8"]]
- 005172c8 bytes f5000094
+ 0053a160 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93cfb3b2c42f81b65dfae8ca306884e4"></a>

### [`0051769c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/0051769c.md) → [`0053a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a534.md) FUN_0053a534

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005171dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/0051769c.md#insn-00517704) · [`0051773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/0051769c.md#insn-0051773c) · [`005177ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/0051769c.md#insn-005177ec)
- 新版 `0053a59c`（命令位置の公開資料なし） · `0053a5d4`（命令位置の公開資料なし） · `0053a684`（命令位置の公開資料なし）

~~~diff
- 00517704 ["INT_ADD", "register:40f0:8", ["const:517704:8", "const:4:8"]]
- 00517704 ["CALL", null, ["callee:00c57b40:8"]]
+ 0053a59c ["INT_ADD", "register:40f0:8", ["const:53a59c:8", "const:4:8"]]
+ 0053a59c ["CALL", null, ["callee:00c57b40:8"]]
- 00517704 bytes 7b0e1b94
+ 0053a59c bytes 69751c94
- 0051773c ["INT_ADD", "register:40f0:8", ["const:51773c:8", "const:4:8"]]
- 0051773c ["CALL", null, ["callee:00c57a90:8"]]
+ 0053a5d4 ["INT_ADD", "register:40f0:8", ["const:53a5d4:8", "const:4:8"]]
+ 0053a5d4 ["CALL", null, ["callee:00c57a90:8"]]
- 0051773c bytes 410e1b94
+ 0053a5d4 bytes 2f751c94
- 005177ec ["INT_ADD", "register:40f0:8", ["const:5177ec:8", "const:4:8"]]
- 005177ec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053a684 ["INT_ADD", "register:40f0:8", ["const:53a684:8", "const:4:8"]]
+ 0053a684 ["CALL", null, ["callee:00c57ab0:8"]]
- 005177ec bytes 1d0e1b94
+ 0053a684 bytes 0b751c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d03aac576469a56987cd3c86a9b1256"></a>

### [`00517824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517824.md) → [`0053a6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a6bc.md) FUN_0053a6bc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005171dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517824.md#insn-00517894) · [`005178cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517824.md#insn-005178cc) · [`0051797c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517824.md#insn-0051797c)
- 新版 `0053a72c`（命令位置の公開資料なし） · `0053a764`（命令位置の公開資料なし） · `0053a814`（命令位置の公開資料なし）

~~~diff
- 00517894 ["INT_ADD", "register:40f0:8", ["const:517894:8", "const:4:8"]]
- 00517894 ["CALL", null, ["callee:00c57b40:8"]]
+ 0053a72c ["INT_ADD", "register:40f0:8", ["const:53a72c:8", "const:4:8"]]
+ 0053a72c ["CALL", null, ["callee:00c57b40:8"]]
- 00517894 bytes 170e1b94
+ 0053a72c bytes 05751c94
- 005178cc ["INT_ADD", "register:40f0:8", ["const:5178cc:8", "const:4:8"]]
- 005178cc ["CALL", null, ["callee:00c57a90:8"]]
+ 0053a764 ["INT_ADD", "register:40f0:8", ["const:53a764:8", "const:4:8"]]
+ 0053a764 ["CALL", null, ["callee:00c57a90:8"]]
- 005178cc bytes dd0d1b94
+ 0053a764 bytes cb741c94
- 0051797c ["INT_ADD", "register:40f0:8", ["const:51797c:8", "const:4:8"]]
- 0051797c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053a814 ["INT_ADD", "register:40f0:8", ["const:53a814:8", "const:4:8"]]
+ 0053a814 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051797c bytes b90d1b94
+ 0053a814 bytes a7741c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f5ffb6b1657021f4ad433f36b920f1"></a>

### [`005179b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005179b0.md) → [`0053a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a848.md) FUN_0053a848

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005171dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005179b0.md#insn-00517a20) · [`00517a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005179b0.md#insn-00517a58) · [`00517b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005179b0.md#insn-00517b08)
- 新版 `0053a8b8`（命令位置の公開資料なし） · `0053a8f0`（命令位置の公開資料なし） · `0053a9a0`（命令位置の公開資料なし）

~~~diff
- 00517a20 ["INT_ADD", "register:40f0:8", ["const:517a20:8", "const:4:8"]]
- 00517a20 ["CALL", null, ["callee:00c57b40:8"]]
+ 0053a8b8 ["INT_ADD", "register:40f0:8", ["const:53a8b8:8", "const:4:8"]]
+ 0053a8b8 ["CALL", null, ["callee:00c57b40:8"]]
- 00517a20 bytes b40d1b94
+ 0053a8b8 bytes a2741c94
- 00517a58 ["INT_ADD", "register:40f0:8", ["const:517a58:8", "const:4:8"]]
- 00517a58 ["CALL", null, ["callee:00c57a90:8"]]
+ 0053a8f0 ["INT_ADD", "register:40f0:8", ["const:53a8f0:8", "const:4:8"]]
+ 0053a8f0 ["CALL", null, ["callee:00c57a90:8"]]
- 00517a58 bytes 7a0d1b94
+ 0053a8f0 bytes 68741c94
- 00517b08 ["INT_ADD", "register:40f0:8", ["const:517b08:8", "const:4:8"]]
- 00517b08 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053a9a0 ["INT_ADD", "register:40f0:8", ["const:53a9a0:8", "const:4:8"]]
+ 0053a9a0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00517b08 bytes 560d1b94
+ 0053a9a0 bytes 44741c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a72c0f4a6f1c460f62f500fed43dbbfa"></a>

### [`00517bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md) → [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) FUN_0053aa64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) [`004fb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb4c0.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00517ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517ccc.md) [`00517f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517f4c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 6件 [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053ab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ab64.md) [`0053ade4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ade4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md#insn-00517c04) · [`00517c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md#insn-00517c1c) · [`00517c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md#insn-00517c38)
- 新版 `0053aa9c`（命令位置の公開資料なし） · `0053aab4`（命令位置の公開資料なし） · `0053aad0`（命令位置の公開資料なし）

~~~diff
- 00517c04 ["INT_ADD", "register:40f0:8", ["const:517c04:8", "const:4:8"]]
- 00517c04 ["CALL", null, ["callee:00c57a90:8"]]
+ 0053aa9c ["INT_ADD", "register:40f0:8", ["const:53aa9c:8", "const:4:8"]]
+ 0053aa9c ["CALL", null, ["callee:00c57a90:8"]]
- 00517c04 bytes 0f0d1b94
+ 0053aa9c bytes fd731c94
- 00517c1c ["INT_ADD", "register:40f0:8", ["const:517c1c:8", "const:4:8"]]
- 00517c1c ["CALL", null, ["callee:0053ade4:8"]]
+ 0053aab4 ["INT_ADD", "register:40f0:8", ["const:53aab4:8", "const:4:8"]]
+ 0053aab4 ["CALL", null, ["callee:0053ade4:8"]]
- 00517c1c bytes cc000094
+ 0053aab4 bytes cc000094
- 00517c38 ["INT_ADD", "register:40f0:8", ["const:517c38:8", "const:4:8"]]
- 00517c38 ["CALL", null, ["callee:0053ab64:8"]]
+ 0053aad0 ["INT_ADD", "register:40f0:8", ["const:53aad0:8", "const:4:8"]]
+ 0053aad0 ["CALL", null, ["callee:0053ab64:8"]]
- 00517c38 bytes 25000094
+ 0053aad0 bytes 25000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652a71a41a9ba7d63d98f82fd26c7045"></a>

### [`00517ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517ee0.md) → [`0053ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053ad78.md) FUN_0053ad78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00517f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517ee0.md#insn-00517f0c) · [`00517f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517ee0.md#insn-00517f1c) · [`00517f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517ee0.md#insn-00517f2c)
- 新版 `0053ada4`（命令位置の公開資料なし） · `0053adb4`（命令位置の公開資料なし） · `0053adc4`（命令位置の公開資料なし）

~~~diff
- 00517f0c ["INT_ADD", "register:40f0:8", ["const:517f0c:8", "const:4:8"]]
- 00517f0c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053ada4 ["INT_ADD", "register:40f0:8", ["const:53ada4:8", "const:4:8"]]
+ 0053ada4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00517f0c bytes 550c1b94
+ 0053ada4 bytes 43731c94
- 00517f1c ["INT_ADD", "register:40f0:8", ["const:517f1c:8", "const:4:8"]]
- 00517f1c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053adb4 ["INT_ADD", "register:40f0:8", ["const:53adb4:8", "const:4:8"]]
+ 0053adb4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00517f1c bytes 510c1b94
+ 0053adb4 bytes 3f731c94
- 00517f2c ["INT_ADD", "register:40f0:8", ["const:517f2c:8", "const:4:8"]]
- 00517f2c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053adc4 ["INT_ADD", "register:40f0:8", ["const:53adc4:8", "const:4:8"]]
+ 0053adc4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00517f2c bytes 4d0c1b94
+ 0053adc4 bytes 3b731c94
~~~


<a id="compare-e7440765083a14507da86160410395ea"></a>

### [`005184e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005184e0.md) → [`0053b378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b378.md) FUN_0053b378

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00518508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005184e0.md#insn-00518508)
- 新版 `0053b3a0`（命令位置の公開資料なし）

~~~diff
- 00518508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00518508 ["INT_ADD", "register:40f0:8", ["const:518508:8", "const:4:8"]]
- 00518508 ["CALLIND", null, ["register:0:8"]]
+ 0053b3a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053b3a0 ["INT_ADD", "register:40f0:8", ["const:53b3a0:8", "const:4:8"]]
+ 0053b3a0 ["CALLIND", null, ["register:0:8"]]
- 00518508 bytes 00013fd6
+ 0053b3a0 bytes 00013fd6
~~~


<a id="compare-9ae5144c6f6e85b8aab1cc71f40a5320"></a>

### [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) → [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) FUN_0053b3e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004e8484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md) [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`004ef204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md) · 呼出先 4件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 17件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`0051209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md) · 呼出先 4件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00518568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md#insn-00518568) · [`00518574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md#insn-00518574) · [`00518584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md#insn-00518584)
- 新版 `0053b400`（命令位置の公開資料なし） · `0053b40c`（命令位置の公開資料なし） · `0053b41c`（命令位置の公開資料なし）

~~~diff
- 00518568 ["INT_ADD", "register:40f0:8", ["const:518568:8", "const:4:8"]]
- 00518568 ["CALL", null, ["local:b0:8"]]
+ 0053b400 ["INT_ADD", "register:40f0:8", ["const:53b400:8", "const:4:8"]]
+ 0053b400 ["CALL", null, ["local:b0:8"]]
- 00518568 bytes f9ffff97
+ 0053b400 bytes f9ffff97
- 00518574 ["INT_ADD", "register:40f0:8", ["const:518574:8", "const:4:8"]]
- 00518574 ["CALL", null, ["local:b0:8"]]
+ 0053b40c ["INT_ADD", "register:40f0:8", ["const:53b40c:8", "const:4:8"]]
+ 0053b40c ["CALL", null, ["local:b0:8"]]
- 00518574 bytes f6ffff97
+ 0053b40c bytes f6ffff97
- 00518584 ["INT_ADD", "register:40f0:8", ["const:518584:8", "const:4:8"]]
- 00518584 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053b41c ["INT_ADD", "register:40f0:8", ["const:53b41c:8", "const:4:8"]]
+ 0053b41c ["CALL", null, ["callee:00c57ab0:8"]]
- 00518584 bytes b70a1b94
+ 0053b41c bytes a5711c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528e7f5a476abb99055f58596ccf48e6"></a>

### [`00518dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md) → [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) FUN_0053bc70

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`00518c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md) [`00519bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519bb0.md) [`006fc134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fc134.md) [`0090ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090ff0c.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) [`00726234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726234.md) [`00944e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944e18.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00518df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md#insn-00518df8) · [`00518e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md#insn-00518e2c) · [`00518e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md#insn-00518e58)
- 新版 `0053bc90`（命令位置の公開資料なし） · `0053bcc4`（命令位置の公開資料なし） · `0053bcf0`（命令位置の公開資料なし）

~~~diff
- 00518df8 ["INT_ADD", "register:40f0:8", ["const:518df8:8", "const:4:8"]]
- 00518df8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0053bc90 ["INT_ADD", "register:40f0:8", ["const:53bc90:8", "const:4:8"]]
+ 0053bc90 ["CALL", null, ["callee:00c57a90:8"]]
- 00518df8 bytes 92081b94
+ 0053bc90 bytes 806f1c94
- 00518e2c ["INT_ADD", "register:40f0:8", ["const:518e2c:8", "const:4:8"]]
- 00518e2c ["CALL", null, ["callee:0043bae0:8"]]
+ 0053bcc4 ["INT_ADD", "register:40f0:8", ["const:53bcc4:8", "const:4:8"]]
+ 0053bcc4 ["CALL", null, ["callee:0043bae0:8"]]
- 00518e2c bytes 6d00fc97
+ 0053bcc4 bytes 87fffb97
- 00518e58 ["INT_ADD", "register:40f0:8", ["const:518e58:8", "const:4:8"]]
- 00518e58 ["CALL", null, ["callee:0043bae0:8"]]
+ 0053bcf0 ["INT_ADD", "register:40f0:8", ["const:53bcf0:8", "const:4:8"]]
+ 0053bcf0 ["CALL", null, ["callee:0043bae0:8"]]
- 00518e58 bytes 6200fc97
+ 0053bcf0 bytes 7cfffb97
~~~


<a id="compare-45140d3a9228c4a07883e512ea5b9e9e"></a>

### [`00519248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519248.md) → [`0053c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c0e0.md) FUN_0053c0e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00519260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519248.md#insn-00519260)
- 新版 `0053c0f8`（命令位置の公開資料なし）

~~~diff
- 00519260 ["INT_ADD", "register:40f0:8", ["const:519260:8", "const:4:8"]]
- 00519260 ["CALL", null, ["callee:0053af50:8"]]
+ 0053c0f8 ["INT_ADD", "register:40f0:8", ["const:53c0f8:8", "const:4:8"]]
+ 0053c0f8 ["CALL", null, ["callee:0053af50:8"]]
- 00519260 bytes 96fbff97
+ 0053c0f8 bytes 96fbff97
~~~


<a id="compare-a1b360900960b5a6bbd7b90366ce6769"></a>

### [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) → [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) FUN_00540694

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004ec514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md) [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) [`0050eb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md) [`0050ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) [`005319ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md) [`00531e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051d860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md#insn-0051d860)
- 新版 `005406f8`（命令位置の公開資料なし）

~~~diff
- 0051d860 ["INT_ADD", "register:40f0:8", ["const:51d860:8", "const:4:8"]]
- 0051d860 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005406f8 ["INT_ADD", "register:40f0:8", ["const:5406f8:8", "const:4:8"]]
+ 005406f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051d860 bytes 00f61a94
+ 005406f8 bytes ee5c1c94
~~~


<a id="compare-f9eb87b343dc01f4d8be00056504af5c"></a>

### [`00522cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522cdc.md) → [`00545b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md) FUN_00545b74

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004cb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522cdc.md#insn-00522cfc)
- 新版 `00545b94`（命令位置の公開資料なし）

~~~diff
- 00522cfc ["INT_ADD", "register:40f0:8", ["const:522cfc:8", "const:4:8"]]
- 00522cfc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00545b94 ["INT_ADD", "register:40f0:8", ["const:545b94:8", "const:4:8"]]
+ 00545b94 ["CALL", null, ["callee:00c57ab0:8"]]
- 00522cfc bytes d9e01a94
+ 00545b94 bytes c7471c94
~~~


<a id="compare-9e965dbec68d5bae717337dd85747ab6"></a>

### [`00529360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md) → [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) FUN_0054c1f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00529360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md) · 呼出先 2件 [`00529360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) · 呼出先 2件 [`0054c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052937c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md#insn-0052937c) · [`00529388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md#insn-00529388) · [`00529398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529360.md#insn-00529398)
- 新版 `0054c214`（命令位置の公開資料なし） · `0054c220`（命令位置の公開資料なし） · `0054c230`（命令位置の公開資料なし）

~~~diff
- 0052937c ["INT_ADD", "register:40f0:8", ["const:52937c:8", "const:4:8"]]
- 0052937c ["CALL", null, ["local:b0:8"]]
+ 0054c214 ["INT_ADD", "register:40f0:8", ["const:54c214:8", "const:4:8"]]
+ 0054c214 ["CALL", null, ["local:b0:8"]]
- 0052937c bytes f9ffff97
+ 0054c214 bytes f9ffff97
- 00529388 ["INT_ADD", "register:40f0:8", ["const:529388:8", "const:4:8"]]
- 00529388 ["CALL", null, ["local:b0:8"]]
+ 0054c220 ["INT_ADD", "register:40f0:8", ["const:54c220:8", "const:4:8"]]
+ 0054c220 ["CALL", null, ["local:b0:8"]]
- 00529388 bytes f6ffff97
+ 0054c220 bytes f6ffff97
- 00529398 ["INT_ADD", "register:40f0:8", ["const:529398:8", "const:4:8"]]
- 00529398 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054c230 ["INT_ADD", "register:40f0:8", ["const:54c230:8", "const:4:8"]]
+ 0054c230 ["CALL", null, ["callee:00c57ab0:8"]]
- 00529398 bytes 32c71a94
+ 0054c230 bytes 202e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac2631bbaace10585f30b8bb8f1e808"></a>

### [`005293c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005293c0.md) → [`0054c258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c258.md) FUN_0054c258

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004f4238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4238.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0052953c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052953c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005170d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054c3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c3d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005294c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005293c0.md#insn-005294c4) · [`005294f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005293c0.md#insn-005294f0) · [`00529538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005293c0.md#insn-00529538)
- 新版 `0054c35c`（命令位置の公開資料なし） · `0054c388`（命令位置の公開資料なし） · `0054c3d0`（命令位置の公開資料なし）

~~~diff
- 005294c4 ["INT_ADD", "register:40f0:8", ["const:5294c4:8", "const:4:8"]]
- 005294c4 ["CALL", null, ["callee:0054c3d4:8"]]
+ 0054c35c ["INT_ADD", "register:40f0:8", ["const:54c35c:8", "const:4:8"]]
+ 0054c35c ["CALL", null, ["callee:0054c3d4:8"]]
- 005294c4 bytes 1e000094
+ 0054c35c bytes 1e000094
- 005294f0 ["INT_ADD", "register:40f0:8", ["const:5294f0:8", "const:4:8"]]
- 005294f0 ["CALL", null, ["callee:0043bb64:8"]]
+ 0054c388 ["INT_ADD", "register:40f0:8", ["const:54c388:8", "const:4:8"]]
+ 0054c388 ["CALL", null, ["callee:0043bb64:8"]]
- 005294f0 bytes ddbefb97
+ 0054c388 bytes f7bdfb97
- 00529538 ["INT_ADD", "register:40f0:8", ["const:529538:8", "const:4:8"]]
- 00529538 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0054c3d0 ["INT_ADD", "register:40f0:8", ["const:54c3d0:8", "const:4:8"]]
+ 0054c3d0 ["CALL", null, ["callee:00c57ae0:8"]]
- 00529538 bytes d6c61a94
+ 0054c3d0 bytes c42d1c94
~~~


<a id="compare-e09b12a6205e0075c72b575212cf09c4"></a>

### [`00529630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529630.md) → [`0054c4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c4c8.md) FUN_0054c4c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052953c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052953c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054c3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c3d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529630.md#insn-0052965c) · [`0052966c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529630.md#insn-0052966c)
- 新版 `0054c4f4`（命令位置の公開資料なし） · `0054c504`（命令位置の公開資料なし）

~~~diff
- 0052965c ["INT_ADD", "register:40f0:8", ["const:52965c:8", "const:4:8"]]
- 0052965c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054c4f4 ["INT_ADD", "register:40f0:8", ["const:54c4f4:8", "const:4:8"]]
+ 0054c4f4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052965c bytes 81c61a94
+ 0054c4f4 bytes 6f2d1c94
- 0052966c ["INT_ADD", "register:40f0:8", ["const:52966c:8", "const:4:8"]]
- 0052966c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054c504 ["INT_ADD", "register:40f0:8", ["const:54c504:8", "const:4:8"]]
+ 0054c504 ["CALL", null, ["callee:00c57ab0:8"]]
- 0052966c bytes 7dc61a94
+ 0054c504 bytes 6b2d1c94
~~~


