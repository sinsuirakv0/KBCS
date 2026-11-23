# v16.0.0 → v16.0.1 · 要調査の変更候補 (28)

[一覧の目次](README.md)

<a id="compare-08dadb1a9a899c5b2414b55534ae89ab"></a>

### [`00849b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b58.md) → [`00849b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md) FUN_00849b98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0086a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b58.md#insn-00849b70) · [`00849b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b58.md#insn-00849b7c)
- 新版 `00849bb0`（命令位置の公開資料なし） · `00849bbc`（命令位置の公開資料なし）

~~~diff
- 00849b70 ["INT_ADD", "register:40f0:8", ["const:849b70:8", "const:4:8"]]
- 00849b70 ["CALL", null, ["callee:00676a60:8"]]
+ 00849bb0 ["INT_ADD", "register:40f0:8", ["const:849bb0:8", "const:4:8"]]
+ 00849bb0 ["CALL", null, ["callee:00676a60:8"]]
- 00849b70 bytes acb3f897
+ 00849bb0 bytes acb3f897
- 00849b7c ["INT_ADD", "register:40f0:8", ["const:849b7c:8", "const:4:8"]]
- 00849b7c ["CALL", null, ["callee:005c3e7c:8"]]
+ 00849bbc ["INT_ADD", "register:40f0:8", ["const:849bbc:8", "const:4:8"]]
+ 00849bbc ["CALL", null, ["callee:005c3e7c:8"]]
- 00849b7c bytes b0e8f597
+ 00849bbc bytes b0e8f597
~~~


<a id="compare-7667e8b870f4c5f4cb9db7cc82776352"></a>

### [`00849b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b94.md) → [`00849bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md) FUN_00849bd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00726350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726350.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b94.md#insn-00849bac) · [`00849bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b94.md#insn-00849bb8)
- 新版 `00849bec`（命令位置の公開資料なし） · `00849bf8`（命令位置の公開資料なし）

~~~diff
- 00849bac ["INT_ADD", "register:40f0:8", ["const:849bac:8", "const:4:8"]]
- 00849bac ["CALL", null, ["callee:00676a60:8"]]
+ 00849bec ["INT_ADD", "register:40f0:8", ["const:849bec:8", "const:4:8"]]
+ 00849bec ["CALL", null, ["callee:00676a60:8"]]
- 00849bac bytes 9db3f897
+ 00849bec bytes 9db3f897
- 00849bb8 ["INT_ADD", "register:40f0:8", ["const:849bb8:8", "const:4:8"]]
- 00849bb8 ["CALL", null, ["callee:005c179c:8"]]
+ 00849bf8 ["INT_ADD", "register:40f0:8", ["const:849bf8:8", "const:4:8"]]
+ 00849bf8 ["CALL", null, ["callee:005c179c:8"]]
- 00849bb8 bytes e9def597
+ 00849bf8 bytes e9def597
~~~


<a id="compare-d7bab732b6d01b21297d1c965a2943a9"></a>

### [`00849bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md) → [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) FUN_00849c10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md) [`0086ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md#insn-00849bf0) · [`00849c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md#insn-00849c04) · [`00849c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md#insn-00849c0c)
- 新版 `00849c30`（命令位置の公開資料なし） · `00849c44`（命令位置の公開資料なし） · `00849c4c`（命令位置の公開資料なし）

~~~diff
- 00849bf0 ["INT_ADD", "register:40f0:8", ["const:849bf0:8", "const:4:8"]]
- 00849bf0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00849c30 ["INT_ADD", "register:40f0:8", ["const:849c30:8", "const:4:8"]]
+ 00849c30 ["CALL", null, ["callee:00c53d00:8"]]
- 00849bf0 bytes 3c271094
+ 00849c30 bytes 34281094
- 00849c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00849c04 ["INT_ADD", "register:40f0:8", ["const:849c04:8", "const:4:8"]]
- 00849c04 ["CALLIND", null, ["register:0:8"]]
+ 00849c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00849c44 ["INT_ADD", "register:40f0:8", ["const:849c44:8", "const:4:8"]]
+ 00849c44 ["CALLIND", null, ["register:0:8"]]
- 00849c04 bytes 00013fd6
+ 00849c44 bytes 00013fd6
- 00849c0c ["INT_ADD", "register:40f0:8", ["const:849c0c:8", "const:4:8"]]
- 00849c0c ["CALL", null, ["callee:00c57e80:8"]]
+ 00849c4c ["INT_ADD", "register:40f0:8", ["const:849c4c:8", "const:4:8"]]
+ 00849c4c ["CALL", null, ["callee:00c57e80:8"]]
- 00849c0c bytes 9d371094
+ 00849c4c bytes 8d381094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4729cb6dd18aac43cddc530051748e33"></a>

### [`00849c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md) → [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) FUN_00849c98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0080e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e700.md) [`0080e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e860.md) [`0080e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e9c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md#insn-00849c70) · [`00849c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c58.md#insn-00849c7c)
- 新版 `00849cb0`（命令位置の公開資料なし） · `00849cbc`（命令位置の公開資料なし）

~~~diff
- 00849c70 ["INT_ADD", "register:40f0:8", ["const:849c70:8", "const:4:8"]]
- 00849c70 ["CALL", null, ["callee:0080ea00:8"]]
+ 00849cb0 ["INT_ADD", "register:40f0:8", ["const:849cb0:8", "const:4:8"]]
+ 00849cb0 ["CALL", null, ["callee:0080ea00:8"]]
- 00849c70 bytes 5413ff97
+ 00849cb0 bytes 5413ff97
- 00849c7c ["INT_ADD", "register:40f0:8", ["const:849c7c:8", "const:4:8"]]
- 00849c7c ["CALL", null, ["callee:0080e8a0:8"]]
+ 00849cbc ["INT_ADD", "register:40f0:8", ["const:849cbc:8", "const:4:8"]]
+ 00849cbc ["CALL", null, ["callee:0080e8a0:8"]]
- 00849c7c bytes f912ff97
+ 00849cbc bytes f912ff97
~~~


<a id="compare-193b44e70d8b97a6720d1ab16212bb0e"></a>

### [`00856cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856cb0.md) → [`00856cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856cf0.md) FUN_00856cf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00856cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856cb0.md#insn-00856cf0) · [`00856d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856cb0.md#insn-00856d58) · [`00856d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856cb0.md#insn-00856d7c)
- 新版 `00856d30`（命令位置の公開資料なし） · `00856d98`（命令位置の公開資料なし） · `00856dbc`（命令位置の公開資料なし）

~~~diff
- 00856cf0 ["INT_ADD", "register:40f0:8", ["const:856cf0:8", "const:4:8"]]
- 00856cf0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00856d30 ["INT_ADD", "register:40f0:8", ["const:856d30:8", "const:4:8"]]
+ 00856d30 ["CALL", null, ["callee:00c57eb0:8"]]
- 00856cf0 bytes 70031094
+ 00856d30 bytes 60041094
- 00856d58 ["INT_ADD", "register:40f0:8", ["const:856d58:8", "const:4:8"]]
- 00856d58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00856d98 ["INT_ADD", "register:40f0:8", ["const:856d98:8", "const:4:8"]]
+ 00856d98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00856d58 bytes 56031094
+ 00856d98 bytes 46041094
- 00856d7c ["INT_ADD", "register:40f0:8", ["const:856d7c:8", "const:4:8"]]
- 00856d7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00856dbc ["INT_ADD", "register:40f0:8", ["const:856dbc:8", "const:4:8"]]
+ 00856dbc ["CALL", null, ["callee:00c57eb0:8"]]
- 00856d7c bytes 4d031094
+ 00856dbc bytes 3d041094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf3b9d3a0dcf6a228b9172c91cd6aaa"></a>

### [`00859ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859ab8.md) → [`00859af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859af8.md) FUN_00859af8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00859ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859ab8.md#insn-00859ad8) · [`00859af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859ab8.md#insn-00859af8)
- 新版 `00859b18`（命令位置の公開資料なし） · `00859b38`（命令位置の公開資料なし）

~~~diff
- 00859ad8 ["INT_ADD", "register:40f0:8", ["const:859ad8:8", "const:4:8"]]
- 00859ad8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00859b18 ["INT_ADD", "register:40f0:8", ["const:859b18:8", "const:4:8"]]
+ 00859b18 ["CALL", null, ["callee:00c53d00:8"]]
- 00859ad8 bytes 82e70f94
+ 00859b18 bytes 7ae80f94
- 00859af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00859af8 ["INT_ADD", "register:40f0:8", ["const:859af8:8", "const:4:8"]]
- 00859af8 ["CALLIND", null, ["register:0:8"]]
+ 00859b38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00859b38 ["INT_ADD", "register:40f0:8", ["const:859b38:8", "const:4:8"]]
+ 00859b38 ["CALLIND", null, ["register:0:8"]]
- 00859af8 bytes 00013fd6
+ 00859b38 bytes 00013fd6
~~~


<a id="compare-cd1503752ecf90b50ceaa3717ddbc127"></a>

### [`0085ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085a/0085ad60.md) → [`0085ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ada0.md) FUN_0085ada0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006bf84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md) · 呼出先 2件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md)
- 新版 呼出元 1件 [`006bf88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf88c.md) · 呼出先 2件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085ad7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085a/0085ad60.md#insn-0085ad7c)
- 新版 `0085adbc`（命令位置の公開資料なし）

~~~diff
- 0085ad7c ["INT_ADD", "register:40f0:8", ["const:85ad7c:8", "const:4:8"]]
- 0085ad7c ["CALL", null, ["callee:00467860:8"]]
+ 0085adbc ["INT_ADD", "register:40f0:8", ["const:85adbc:8", "const:4:8"]]
+ 0085adbc ["CALL", null, ["callee:00467860:8"]]
- 0085ad7c bytes a932f097
+ 0085adbc bytes a932f097
~~~


<a id="compare-fb6d9a3cb110668e76b08d84f5a408dc"></a>

### [`0085b2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md) → [`0085b2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md) FUN_0085b2f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0086dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dea4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md#insn-0085b314) · [`0085b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md#insn-0085b328) · [`0085b35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md#insn-0085b35c)
- 新版 `0085b354`（命令位置の公開資料なし） · `0085b368`（命令位置の公開資料なし） · `0085b39c`（命令位置の公開資料なし）

~~~diff
- 0085b314 ["INT_ADD", "register:40f0:8", ["const:85b314:8", "const:4:8"]]
- 0085b314 ["CALL", null, ["callee:0043bb20:8"]]
+ 0085b354 ["INT_ADD", "register:40f0:8", ["const:85b354:8", "const:4:8"]]
+ 0085b354 ["CALL", null, ["callee:0043bb20:8"]]
- 0085b314 bytes f381ef97
+ 0085b354 bytes f381ef97
- 0085b328 ["INT_ADD", "register:40f0:8", ["const:85b328:8", "const:4:8"]]
- 0085b328 ["CALL", null, ["callee:0043bb20:8"]]
+ 0085b368 ["INT_ADD", "register:40f0:8", ["const:85b368:8", "const:4:8"]]
+ 0085b368 ["CALL", null, ["callee:0043bb20:8"]]
- 0085b328 bytes ee81ef97
+ 0085b368 bytes ee81ef97
- 0085b35c ["INT_ADD", "register:40f0:8", ["const:85b35c:8", "const:4:8"]]
- 0085b35c ["CALL", null, ["callee:0086dea4:8"]]
+ 0085b39c ["INT_ADD", "register:40f0:8", ["const:85b39c:8", "const:4:8"]]
+ 0085b39c ["CALL", null, ["callee:0086dea4:8"]]
- 0085b35c bytes c24a0094
+ 0085b39c bytes c24a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba526524bab46afff5bff7d24f6fbb7e"></a>

### [`0085bec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md) → [`0085bf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md) FUN_0085bf08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a955d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a955d0.md) · 呼出先 3件 [`00ab8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 3件 [`00ab91b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab91b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085bf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md#insn-0085bf90) · [`0085bfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md#insn-0085bfa0) · [`0085bfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md#insn-0085bfbc)
- 新版 `0085bfd0`（命令位置の公開資料なし） · `0085bfe0`（命令位置の公開資料なし） · `0085bffc`（命令位置の公開資料なし）

~~~diff
- 0085bf90 ["INT_ADD", "register:40f0:8", ["const:85bf90:8", "const:4:8"]]
- 0085bf90 ["CALL", null, ["callee:00ab91b8:8"]]
+ 0085bfd0 ["INT_ADD", "register:40f0:8", ["const:85bfd0:8", "const:4:8"]]
+ 0085bfd0 ["CALL", null, ["callee:00ab91b8:8"]]
- 0085bf90 bytes 0b740994
+ 0085bfd0 bytes 7a740994
- 0085bfa0 ["INT_ADD", "register:40f0:8", ["const:85bfa0:8", "const:4:8"]]
- 0085bfa0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0085bfe0 ["INT_ADD", "register:40f0:8", ["const:85bfe0:8", "const:4:8"]]
+ 0085bfe0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0085bfa0 bytes c4ee0f94
+ 0085bfe0 bytes b4ef0f94
- 0085bfbc ["INT_ADD", "register:40f0:8", ["const:85bfbc:8", "const:4:8"]]
- 0085bfbc ["CALL", null, ["callee:00ab91b8:8"]]
+ 0085bffc ["INT_ADD", "register:40f0:8", ["const:85bffc:8", "const:4:8"]]
+ 0085bffc ["CALL", null, ["callee:00ab91b8:8"]]
- 0085bfbc bytes 00740994
+ 0085bffc bytes 6f740994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2a25e874b81624a624c879da6b945d"></a>

### [`008655c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008655c8.md) → [`00865608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865608.md) FUN_00865608

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008655e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008655c8.md#insn-008655e4) · [`00865604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008655c8.md#insn-00865604)
- 新版 `00865624`（命令位置の公開資料なし） · `00865644`（命令位置の公開資料なし）

~~~diff
- 008655e4 ["INT_ADD", "register:40f0:8", ["const:8655e4:8", "const:4:8"]]
- 008655e4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00865624 ["INT_ADD", "register:40f0:8", ["const:865624:8", "const:4:8"]]
+ 00865624 ["CALL", null, ["callee:00c53d00:8"]]
- 008655e4 bytes bfb80f94
+ 00865624 bytes b7b90f94
- 00865604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00865604 ["INT_ADD", "register:40f0:8", ["const:865604:8", "const:4:8"]]
- 00865604 ["CALLIND", null, ["register:0:8"]]
+ 00865644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00865644 ["INT_ADD", "register:40f0:8", ["const:865644:8", "const:4:8"]]
+ 00865644 ["CALLIND", null, ["register:0:8"]]
- 00865604 bytes 00013fd6
+ 00865644 bytes 00013fd6
~~~


<a id="compare-fea687cf25c7606c06470ef412eafd1c"></a>

### [`00865618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865618.md) → [`00865658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865658.md) FUN_00865658

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865618.md#insn-00865634) · [`00865654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865618.md#insn-00865654)
- 新版 `00865674`（命令位置の公開資料なし） · `00865694`（命令位置の公開資料なし）

~~~diff
- 00865634 ["INT_ADD", "register:40f0:8", ["const:865634:8", "const:4:8"]]
- 00865634 ["CALL", null, ["callee:00c53d00:8"]]
+ 00865674 ["INT_ADD", "register:40f0:8", ["const:865674:8", "const:4:8"]]
+ 00865674 ["CALL", null, ["callee:00c53d00:8"]]
- 00865634 bytes abb80f94
+ 00865674 bytes a3b90f94
- 00865654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00865654 ["INT_ADD", "register:40f0:8", ["const:865654:8", "const:4:8"]]
- 00865654 ["CALLIND", null, ["register:0:8"]]
+ 00865694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00865694 ["INT_ADD", "register:40f0:8", ["const:865694:8", "const:4:8"]]
+ 00865694 ["CALLIND", null, ["register:0:8"]]
- 00865654 bytes 00013fd6
+ 00865694 bytes 00013fd6
~~~


<a id="compare-34beb357cdb3059ac670a461cc2272c9"></a>

### [`00865a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md) → [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) FUN_00865a84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00865a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 2件 [`00865a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 2件 [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md#insn-00865a60) · [`00865a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md#insn-00865a6c) · [`00865a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865a44.md#insn-00865a7c)
- 新版 `00865aa0`（命令位置の公開資料なし） · `00865aac`（命令位置の公開資料なし） · `00865abc`（命令位置の公開資料なし）

~~~diff
- 00865a60 ["INT_ADD", "register:40f0:8", ["const:865a60:8", "const:4:8"]]
- 00865a60 ["CALL", null, ["local:b0:8"]]
+ 00865aa0 ["INT_ADD", "register:40f0:8", ["const:865aa0:8", "const:4:8"]]
+ 00865aa0 ["CALL", null, ["local:b0:8"]]
- 00865a60 bytes f9ffff97
+ 00865aa0 bytes f9ffff97
- 00865a6c ["INT_ADD", "register:40f0:8", ["const:865a6c:8", "const:4:8"]]
- 00865a6c ["CALL", null, ["local:b0:8"]]
+ 00865aac ["INT_ADD", "register:40f0:8", ["const:865aac:8", "const:4:8"]]
+ 00865aac ["CALL", null, ["local:b0:8"]]
- 00865a6c bytes f6ffff97
+ 00865aac bytes f6ffff97
- 00865a7c ["INT_ADD", "register:40f0:8", ["const:865a7c:8", "const:4:8"]]
- 00865a7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865abc ["INT_ADD", "register:40f0:8", ["const:865abc:8", "const:4:8"]]
+ 00865abc ["CALL", null, ["callee:00c57eb0:8"]]
- 00865a7c bytes 0dc80f94
+ 00865abc bytes fdc80f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5603188455ca9d84b3c59d68fa201a5c"></a>

### [`00865c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md) → [`00865ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md) FUN_00865ca8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) · 呼出先 5件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md) [`00652c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c8c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00630ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630ba4.md) [`00652ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652ccc.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md#insn-00865c88) · [`00865c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md#insn-00865c94) · [`00865cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md#insn-00865cd0)
- 新版 `00865cc8`（命令位置の公開資料なし） · `00865cd4`（命令位置の公開資料なし） · `00865d10`（命令位置の公開資料なし）

~~~diff
- 00865c88 ["INT_ADD", "register:40f0:8", ["const:865c88:8", "const:4:8"]]
- 00865c88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865cc8 ["INT_ADD", "register:40f0:8", ["const:865cc8:8", "const:4:8"]]
+ 00865cc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00865c88 bytes 8ac70f94
+ 00865cc8 bytes 7ac80f94
- 00865c94 ["INT_ADD", "register:40f0:8", ["const:865c94:8", "const:4:8"]]
- 00865c94 ["CALL", null, ["callee:00630ba4:8"]]
+ 00865cd4 ["INT_ADD", "register:40f0:8", ["const:865cd4:8", "const:4:8"]]
+ 00865cd4 ["CALL", null, ["callee:00630ba4:8"]]
- 00865c94 bytes b42bf797
+ 00865cd4 bytes b42bf797
- 00865cd0 ["INT_ADD", "register:40f0:8", ["const:865cd0:8", "const:4:8"]]
- 00865cd0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865d10 ["INT_ADD", "register:40f0:8", ["const:865d10:8", "const:4:8"]]
+ 00865d10 ["CALL", null, ["callee:00c57eb0:8"]]
- 00865cd0 bytes 78c70f94
+ 00865d10 bytes 68c80f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-190e0f8d68c49fa93031d01625be46d9"></a>

### [`00865d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865d64.md) → [`00865da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865da4.md) FUN_00865da4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865d64.md#insn-00865dac) · [`00865dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865d64.md#insn-00865dbc) · [`00865dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865d64.md#insn-00865dcc)
- 新版 `00865dec`（命令位置の公開資料なし） · `00865dfc`（命令位置の公開資料なし） · `00865e0c`（命令位置の公開資料なし）

~~~diff
- 00865dac ["INT_ADD", "register:40f0:8", ["const:865dac:8", "const:4:8"]]
- 00865dac ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865dec ["INT_ADD", "register:40f0:8", ["const:865dec:8", "const:4:8"]]
+ 00865dec ["CALL", null, ["callee:00c57eb0:8"]]
- 00865dac bytes 41c70f94
+ 00865dec bytes 31c80f94
- 00865dbc ["INT_ADD", "register:40f0:8", ["const:865dbc:8", "const:4:8"]]
- 00865dbc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865dfc ["INT_ADD", "register:40f0:8", ["const:865dfc:8", "const:4:8"]]
+ 00865dfc ["CALL", null, ["callee:00c57eb0:8"]]
- 00865dbc bytes 3dc70f94
+ 00865dfc bytes 2dc80f94
- 00865dcc ["INT_ADD", "register:40f0:8", ["const:865dcc:8", "const:4:8"]]
- 00865dcc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00865e0c ["INT_ADD", "register:40f0:8", ["const:865e0c:8", "const:4:8"]]
+ 00865e0c ["CALL", null, ["callee:00c57eb0:8"]]
- 00865dcc bytes 39c70f94
+ 00865e0c bytes 29c80f94
~~~


<a id="compare-d904607f882b049b31c92f057347b6a9"></a>

### [`00865dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865dfc.md) → [`00865e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865e3c.md) FUN_00865e3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865dfc.md#insn-00865e70) · [`00865e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865dfc.md#insn-00865e78) · [`00865e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865dfc.md#insn-00865e84)
- 新版 `00865eb0`（命令位置の公開資料なし） · `00865eb8`（命令位置の公開資料なし） · `00865ec4`（命令位置の公開資料なし）

~~~diff
- 00865e70 ["INT_ADD", "register:40f0:8", ["const:865e70:8", "const:4:8"]]
- 00865e70 ["CALL", null, ["callee:0046eef8:8"]]
+ 00865eb0 ["INT_ADD", "register:40f0:8", ["const:865eb0:8", "const:4:8"]]
+ 00865eb0 ["CALL", null, ["callee:0046eef8:8"]]
- 00865e70 bytes 1224f097
+ 00865eb0 bytes 1224f097
- 00865e78 ["INT_ADD", "register:40f0:8", ["const:865e78:8", "const:4:8"]]
- 00865e78 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00865eb8 ["INT_ADD", "register:40f0:8", ["const:865eb8:8", "const:4:8"]]
+ 00865eb8 ["CALL", null, ["callee:0046e7c4:8"]]
- 00865e78 bytes 4322f097
+ 00865eb8 bytes 4322f097
- 00865e84 ["INT_ADD", "register:40f0:8", ["const:865e84:8", "const:4:8"]]
- 00865e84 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00865ec4 ["INT_ADD", "register:40f0:8", ["const:865ec4:8", "const:4:8"]]
+ 00865ec4 ["CALL", null, ["callee:0046e7c4:8"]]
- 00865e84 bytes 4022f097
+ 00865ec4 bytes 4022f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aa5239aa7f4437fb7ebcbf4fff4b18e"></a>

### [`00865f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865f94.md) → [`00865fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865fd4.md) FUN_00865fd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865f94.md#insn-00865fa8) · [`00865fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865f94.md#insn-00865fb0) · [`00865fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865f94.md#insn-00865fb8)
- 新版 `00865fe8`（命令位置の公開資料なし） · `00865ff0`（命令位置の公開資料なし） · `00865ff8`（命令位置の公開資料なし）

~~~diff
- 00865fa8 ["INT_ADD", "register:40f0:8", ["const:865fa8:8", "const:4:8"]]
- 00865fa8 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00865fe8 ["INT_ADD", "register:40f0:8", ["const:865fe8:8", "const:4:8"]]
+ 00865fe8 ["CALL", null, ["callee:0046e8a4:8"]]
- 00865fa8 bytes 2f22f097
+ 00865fe8 bytes 2f22f097
- 00865fb0 ["INT_ADD", "register:40f0:8", ["const:865fb0:8", "const:4:8"]]
- 00865fb0 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00865ff0 ["INT_ADD", "register:40f0:8", ["const:865ff0:8", "const:4:8"]]
+ 00865ff0 ["CALL", null, ["callee:0046e8a4:8"]]
- 00865fb0 bytes 2d22f097
+ 00865ff0 bytes 2d22f097
- 00865fb8 ["INT_ADD", "register:40f0:8", ["const:865fb8:8", "const:4:8"]]
- 00865fb8 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00865ff8 ["INT_ADD", "register:40f0:8", ["const:865ff8:8", "const:4:8"]]
+ 00865ff8 ["CALL", null, ["callee:0046e8a4:8"]]
- 00865fb8 bytes 2b22f097
+ 00865ff8 bytes 2b22f097
~~~


<a id="compare-99cba2ae75a549c50189a570ee90fc48"></a>

### [`00865fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865fcc.md) → [`0086600c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/0086600c.md) FUN_0086600c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865fcc.md#insn-00865fec) · [`00866000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865fcc.md#insn-00866000) · [`00866008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865fcc.md#insn-00866008)
- 新版 `0086602c`（命令位置の公開資料なし） · `00866040`（命令位置の公開資料なし） · `00866048`（命令位置の公開資料なし）

~~~diff
- 00865fec ["INT_ADD", "register:40f0:8", ["const:865fec:8", "const:4:8"]]
- 00865fec ["CALL", null, ["callee:00c53d00:8"]]
+ 0086602c ["INT_ADD", "register:40f0:8", ["const:86602c:8", "const:4:8"]]
+ 0086602c ["CALL", null, ["callee:00c53d00:8"]]
- 00865fec bytes 3db60f94
+ 0086602c bytes 35b70f94
- 00866000 ["COPY", "register:0:8", ["register:4040:8"]]
- 00866000 ["INT_ADD", "register:40f0:8", ["const:866000:8", "const:4:8"]]
- 00866000 ["CALLIND", null, ["register:0:8"]]
+ 00866040 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00866040 ["INT_ADD", "register:40f0:8", ["const:866040:8", "const:4:8"]]
+ 00866040 ["CALLIND", null, ["register:0:8"]]
- 00866000 bytes 00013fd6
+ 00866040 bytes 00013fd6
- 00866008 ["INT_ADD", "register:40f0:8", ["const:866008:8", "const:4:8"]]
- 00866008 ["CALL", null, ["callee:00c57e80:8"]]
+ 00866048 ["INT_ADD", "register:40f0:8", ["const:866048:8", "const:4:8"]]
+ 00866048 ["CALL", null, ["callee:00c57e80:8"]]
- 00866008 bytes 9ec60f94
+ 00866048 bytes 8ec70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cac39d9e3655ff99aac03404d1805bf"></a>

### [`008660bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md) → [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) FUN_008660fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 5件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`008676d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md) [`008678ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md) [`008679c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 5件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md) [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086611c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md#insn-0086611c) · [`00866128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md#insn-00866128) · [`00866134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md#insn-00866134)
- 新版 `0086615c`（命令位置の公開資料なし） · `00866168`（命令位置の公開資料なし） · `00866174`（命令位置の公開資料なし）

~~~diff
- 0086611c ["INT_ADD", "register:40f0:8", ["const:86611c:8", "const:4:8"]]
- 0086611c ["CALL", null, ["callee:0046eef8:8"]]
+ 0086615c ["INT_ADD", "register:40f0:8", ["const:86615c:8", "const:4:8"]]
+ 0086615c ["CALL", null, ["callee:0046eef8:8"]]
- 0086611c bytes 6723f097
+ 0086615c bytes 6723f097
- 00866128 ["INT_ADD", "register:40f0:8", ["const:866128:8", "const:4:8"]]
- 00866128 ["CALL", null, ["callee:0046eef8:8"]]
+ 00866168 ["INT_ADD", "register:40f0:8", ["const:866168:8", "const:4:8"]]
+ 00866168 ["CALL", null, ["callee:0046eef8:8"]]
- 00866128 bytes 6423f097
+ 00866168 bytes 6423f097
- 00866134 ["INT_ADD", "register:40f0:8", ["const:866134:8", "const:4:8"]]
- 00866134 ["CALL", null, ["callee:0046eef8:8"]]
+ 00866174 ["INT_ADD", "register:40f0:8", ["const:866174:8", "const:4:8"]]
+ 00866174 ["CALL", null, ["callee:0046eef8:8"]]
- 00866134 bytes 6123f097
+ 00866174 bytes 6123f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-119d404d108c2e8b00d2cd9b1cc1ba4f"></a>

### [`00866a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md) → [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) FUN_00866a6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 4件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`008676d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md) [`00867f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867f1c.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 4件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) [`00867f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00866aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md#insn-00866aac) · [`00866ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md#insn-00866ab4) · [`00866bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md#insn-00866bb4)
- 新版 `00866aec`（命令位置の公開資料なし） · `00866af4`（命令位置の公開資料なし） · `00866bf4`（命令位置の公開資料なし）

~~~diff
- 00866aac ["INT_ADD", "register:40f0:8", ["const:866aac:8", "const:4:8"]]
- 00866aac ["CALL", null, ["callee:00867714:8"]]
+ 00866aec ["INT_ADD", "register:40f0:8", ["const:866aec:8", "const:4:8"]]
+ 00866aec ["CALL", null, ["callee:00867714:8"]]
- 00866aac bytes 0a030094
+ 00866aec bytes 0a030094
- 00866ab4 ["INT_ADD", "register:40f0:8", ["const:866ab4:8", "const:4:8"]]
- 00866ab4 ["CALL", null, ["callee:00867f5c:8"]]
+ 00866af4 ["INT_ADD", "register:40f0:8", ["const:866af4:8", "const:4:8"]]
+ 00866af4 ["CALL", null, ["callee:00867f5c:8"]]
- 00866ab4 bytes 1a050094
+ 00866af4 bytes 1a050094
- 00866bb4 ["INT_ADD", "register:40f0:8", ["const:866bb4:8", "const:4:8"]]
- 00866bb4 ["CALL", null, ["callee:0046eef8:8"]]
+ 00866bf4 ["INT_ADD", "register:40f0:8", ["const:866bf4:8", "const:4:8"]]
+ 00866bf4 ["CALL", null, ["callee:0046eef8:8"]]
- 00866bb4 bytes c120f097
+ 00866bf4 bytes c120f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad5010b8782db7f979751083bc7c20c"></a>

### [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) → [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) FUN_00866d48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md) · 呼出先 17件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 17件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00866d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md#insn-00866d28) · [`00866d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md#insn-00866d3c) · [`00866d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md#insn-00866d50)
- 新版 `00866d68`（命令位置の公開資料なし） · `00866d7c`（命令位置の公開資料なし） · `00866d90`（命令位置の公開資料なし）

~~~diff
- 00866d28 ["INT_ADD", "register:40f0:8", ["const:866d28:8", "const:4:8"]]
- 00866d28 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00866d68 ["INT_ADD", "register:40f0:8", ["const:866d68:8", "const:4:8"]]
+ 00866d68 ["CALL", null, ["callee:005c3e7c:8"]]
- 00866d28 bytes 4574f597
+ 00866d68 bytes 4574f597
- 00866d3c ["INT_ADD", "register:40f0:8", ["const:866d3c:8", "const:4:8"]]
- 00866d3c ["CALL", null, ["callee:00c53d00:8"]]
+ 00866d7c ["INT_ADD", "register:40f0:8", ["const:866d7c:8", "const:4:8"]]
+ 00866d7c ["CALL", null, ["callee:00c53d00:8"]]
- 00866d3c bytes e9b20f94
+ 00866d7c bytes e1b30f94
- 00866d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00866d50 ["INT_ADD", "register:40f0:8", ["const:866d50:8", "const:4:8"]]
- 00866d50 ["CALLIND", null, ["register:0:8"]]
+ 00866d90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00866d90 ["INT_ADD", "register:40f0:8", ["const:866d90:8", "const:4:8"]]
+ 00866d90 ["CALLIND", null, ["register:0:8"]]
- 00866d50 bytes 00013fd6
+ 00866d90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f8cbf82764e8c6a7864846132c584c"></a>

### [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) → [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) FUN_00867068

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md) · 呼出先 17件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 17件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md#insn-00867048) · [`00867060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md#insn-00867060) · [`00867074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md#insn-00867074)
- 新版 `00867088`（命令位置の公開資料なし） · `008670a0`（命令位置の公開資料なし） · `008670b4`（命令位置の公開資料なし）

~~~diff
- 00867048 ["INT_ADD", "register:40f0:8", ["const:867048:8", "const:4:8"]]
- 00867048 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00867088 ["INT_ADD", "register:40f0:8", ["const:867088:8", "const:4:8"]]
+ 00867088 ["CALL", null, ["callee:00c57eb0:8"]]
- 00867048 bytes 9ac20f94
+ 00867088 bytes 8ac30f94
- 00867060 ["INT_ADD", "register:40f0:8", ["const:867060:8", "const:4:8"]]
- 00867060 ["CALL", null, ["callee:00c53d00:8"]]
+ 008670a0 ["INT_ADD", "register:40f0:8", ["const:8670a0:8", "const:4:8"]]
+ 008670a0 ["CALL", null, ["callee:00c53d00:8"]]
- 00867060 bytes 20b20f94
+ 008670a0 bytes 18b30f94
- 00867074 ["COPY", "register:0:8", ["register:4040:8"]]
- 00867074 ["INT_ADD", "register:40f0:8", ["const:867074:8", "const:4:8"]]
- 00867074 ["CALLIND", null, ["register:0:8"]]
+ 008670b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008670b4 ["INT_ADD", "register:40f0:8", ["const:8670b4:8", "const:4:8"]]
+ 008670b4 ["CALLIND", null, ["register:0:8"]]
- 00867074 bytes 00013fd6
+ 008670b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec4471d03c4063be20373aa37d617d1"></a>

### [`008676d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md) → [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) FUN_00867714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008660bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md) [`00866a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 2件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md#insn-00867700) · [`00867708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md#insn-00867708) · [`00867714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008676d4.md#insn-00867714)
- 新版 `00867740`（命令位置の公開資料なし） · `00867748`（命令位置の公開資料なし） · `00867754`（命令位置の公開資料なし）

~~~diff
- 00867700 ["INT_ADD", "register:40f0:8", ["const:867700:8", "const:4:8"]]
- 00867700 ["CALL", null, ["callee:0046eef8:8"]]
+ 00867740 ["INT_ADD", "register:40f0:8", ["const:867740:8", "const:4:8"]]
+ 00867740 ["CALL", null, ["callee:0046eef8:8"]]
- 00867700 bytes ee1df097
+ 00867740 bytes ee1df097
- 00867708 ["INT_ADD", "register:40f0:8", ["const:867708:8", "const:4:8"]]
- 00867708 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00867748 ["INT_ADD", "register:40f0:8", ["const:867748:8", "const:4:8"]]
+ 00867748 ["CALL", null, ["callee:0046e7c4:8"]]
- 00867708 bytes 1f1cf097
+ 00867748 bytes 1f1cf097
- 00867714 ["INT_ADD", "register:40f0:8", ["const:867714:8", "const:4:8"]]
- 00867714 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00867754 ["INT_ADD", "register:40f0:8", ["const:867754:8", "const:4:8"]]
+ 00867754 ["CALL", null, ["callee:0046e7c4:8"]]
- 00867714 bytes 1c1cf097
+ 00867754 bytes 1c1cf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25f08037492964e593a099619459d319"></a>

### [`008678ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md) → [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md) FUN_008678ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008660bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md) [`008679c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 2件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008678d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md#insn-008678d8) · [`008678e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md#insn-008678e0) · [`008678ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md#insn-008678ec)
- 新版 `00867918`（命令位置の公開資料なし） · `00867920`（命令位置の公開資料なし） · `0086792c`（命令位置の公開資料なし）

~~~diff
- 008678d8 ["INT_ADD", "register:40f0:8", ["const:8678d8:8", "const:4:8"]]
- 008678d8 ["CALL", null, ["callee:0046eef8:8"]]
+ 00867918 ["INT_ADD", "register:40f0:8", ["const:867918:8", "const:4:8"]]
+ 00867918 ["CALL", null, ["callee:0046eef8:8"]]
- 008678d8 bytes 781df097
+ 00867918 bytes 781df097
- 008678e0 ["INT_ADD", "register:40f0:8", ["const:8678e0:8", "const:4:8"]]
- 008678e0 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00867920 ["INT_ADD", "register:40f0:8", ["const:867920:8", "const:4:8"]]
+ 00867920 ["CALL", null, ["callee:0046e7c4:8"]]
- 008678e0 bytes a91bf097
+ 00867920 bytes a91bf097
- 008678ec ["INT_ADD", "register:40f0:8", ["const:8678ec:8", "const:4:8"]]
- 008678ec ["CALL", null, ["callee:0046e7c4:8"]]
+ 0086792c ["INT_ADD", "register:40f0:8", ["const:86792c:8", "const:4:8"]]
+ 0086792c ["CALL", null, ["callee:0046e7c4:8"]]
- 008678ec bytes a61bf097
+ 0086792c bytes a61bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c8591871fda9370d996e0124d52a86"></a>

### [`008679c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md) → [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md) FUN_00867a08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008660bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/008660bc.md) · 呼出先 3件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`008678ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008678ac.md)
- 新版 呼出元 1件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) · 呼出先 3件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008679e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md#insn-008679e0) · [`008679f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md#insn-008679f8) · [`00867a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/008679c8.md#insn-00867a00)
- 新版 `00867a20`（命令位置の公開資料なし） · `00867a38`（命令位置の公開資料なし） · `00867a40`（命令位置の公開資料なし）

~~~diff
- 008679e0 ["INT_ADD", "register:40f0:8", ["const:8679e0:8", "const:4:8"]]
- 008679e0 ["CALL", null, ["callee:008678ec:8"]]
+ 00867a20 ["INT_ADD", "register:40f0:8", ["const:867a20:8", "const:4:8"]]
+ 00867a20 ["CALL", null, ["callee:008678ec:8"]]
- 008679e0 bytes b3ffff97
+ 00867a20 bytes b3ffff97
- 008679f8 ["INT_ADD", "register:40f0:8", ["const:8679f8:8", "const:4:8"]]
- 008679f8 ["CALL", null, ["callee:0046eef8:8"]]
+ 00867a38 ["INT_ADD", "register:40f0:8", ["const:867a38:8", "const:4:8"]]
+ 00867a38 ["CALL", null, ["callee:0046eef8:8"]]
- 008679f8 bytes 301df097
+ 00867a38 bytes 301df097
- 00867a00 ["INT_ADD", "register:40f0:8", ["const:867a00:8", "const:4:8"]]
- 00867a00 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00867a40 ["INT_ADD", "register:40f0:8", ["const:867a40:8", "const:4:8"]]
+ 00867a40 ["CALL", null, ["callee:0046e7c4:8"]]
- 00867a00 bytes 611bf097
+ 00867a40 bytes 611bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62afc0510e14b1d1e4664c762f96d92a"></a>

### [`00867b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867b18.md) → [`00867b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867b58.md) FUN_00867b58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) · 呼出先 3件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 3件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867b18.md#insn-00867b54) · [`00867b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867b18.md#insn-00867b5c) · [`00867b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867b18.md#insn-00867b8c)
- 新版 `00867b94`（命令位置の公開資料なし） · `00867b9c`（命令位置の公開資料なし） · `00867bcc`（命令位置の公開資料なし）

~~~diff
- 00867b54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00867b54 ["INT_ADD", "register:40f0:8", ["const:867b54:8", "const:4:8"]]
- 00867b54 ["CALLIND", null, ["register:0:8"]]
+ 00867b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00867b94 ["INT_ADD", "register:40f0:8", ["const:867b94:8", "const:4:8"]]
+ 00867b94 ["CALLIND", null, ["register:0:8"]]
- 00867b54 bytes 00013fd6
+ 00867b94 bytes 00013fd6
- 00867b5c ["INT_ADD", "register:40f0:8", ["const:867b5c:8", "const:4:8"]]
- 00867b5c ["CALL", null, ["callee:0067e5e8:8"]]
+ 00867b9c ["INT_ADD", "register:40f0:8", ["const:867b9c:8", "const:4:8"]]
+ 00867b9c ["CALL", null, ["callee:0067e5e8:8"]]
- 00867b5c bytes 935af897
+ 00867b9c bytes 935af897
- 00867b8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00867b8c ["INT_ADD", "register:40f0:8", ["const:867b8c:8", "const:4:8"]]
- 00867b8c ["CALLIND", null, ["register:0:8"]]
+ 00867bcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00867bcc ["INT_ADD", "register:40f0:8", ["const:867bcc:8", "const:4:8"]]
+ 00867bcc ["CALLIND", null, ["register:0:8"]]
- 00867b8c bytes 00013fd6
+ 00867bcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a676f32d77b91952b8f37c6af383a75c"></a>

### [`00867c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867c4c.md) → [`00867c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md) FUN_00867c8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) · 呼出先 6件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00867db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867db8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00867df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867c4c.md#insn-00867c80) · [`00867c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867c4c.md#insn-00867c88) · [`00867c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867c4c.md#insn-00867c90)
- 新版 `00867cc0`（命令位置の公開資料なし） · `00867cc8`（命令位置の公開資料なし） · `00867cd0`（命令位置の公開資料なし）

~~~diff
- 00867c80 ["INT_ADD", "register:40f0:8", ["const:867c80:8", "const:4:8"]]
- 00867c80 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00867cc0 ["INT_ADD", "register:40f0:8", ["const:867cc0:8", "const:4:8"]]
+ 00867cc0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00867c80 bytes 8cbf0f94
+ 00867cc0 bytes 7cc00f94
- 00867c88 ["INT_ADD", "register:40f0:8", ["const:867c88:8", "const:4:8"]]
- 00867c88 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00867cc8 ["INT_ADD", "register:40f0:8", ["const:867cc8:8", "const:4:8"]]
+ 00867cc8 ["CALL", null, ["callee:0046e8a4:8"]]
- 00867c88 bytes f71af097
+ 00867cc8 bytes f71af097
- 00867c90 ["INT_ADD", "register:40f0:8", ["const:867c90:8", "const:4:8"]]
- 00867c90 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00867cd0 ["INT_ADD", "register:40f0:8", ["const:867cd0:8", "const:4:8"]]
+ 00867cd0 ["CALL", null, ["callee:0046e8a4:8"]]
- 00867c90 bytes f51af097
+ 00867cd0 bytes f51af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7e0a60a855c346f00b3932379c2391"></a>

### [`00867db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867db8.md) → [`00867df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md) FUN_00867df8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) [`00867c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867c4c.md) · 呼出先 4件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00867c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md) · 呼出先 4件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867db8.md#insn-00867dcc) · [`00867dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867db8.md#insn-00867dd4) · [`00867ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867db8.md#insn-00867ddc)
- 新版 `00867e0c`（命令位置の公開資料なし） · `00867e14`（命令位置の公開資料なし） · `00867e1c`（命令位置の公開資料なし）

~~~diff
- 00867dcc ["INT_ADD", "register:40f0:8", ["const:867dcc:8", "const:4:8"]]
- 00867dcc ["CALL", null, ["callee:0046e8a4:8"]]
+ 00867e0c ["INT_ADD", "register:40f0:8", ["const:867e0c:8", "const:4:8"]]
+ 00867e0c ["CALL", null, ["callee:0046e8a4:8"]]
- 00867dcc bytes a61af097
+ 00867e0c bytes a61af097
- 00867dd4 ["INT_ADD", "register:40f0:8", ["const:867dd4:8", "const:4:8"]]
- 00867dd4 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00867e14 ["INT_ADD", "register:40f0:8", ["const:867e14:8", "const:4:8"]]
+ 00867e14 ["CALL", null, ["callee:0046e8a4:8"]]
- 00867dd4 bytes a41af097
+ 00867e14 bytes a41af097
- 00867ddc ["INT_ADD", "register:40f0:8", ["const:867ddc:8", "const:4:8"]]
- 00867ddc ["CALL", null, ["callee:0046e8a4:8"]]
+ 00867e1c ["INT_ADD", "register:40f0:8", ["const:867e1c:8", "const:4:8"]]
+ 00867e1c ["CALL", null, ["callee:0046e8a4:8"]]
- 00867ddc bytes a21af097
+ 00867e1c bytes a21af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dbf16b2d9ded75417fd28df2d49679e"></a>

### [`00867ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867ed8.md) → [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) FUN_00867f18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) [`00867ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867ed8.md) [`00b12c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12c08.md) · 呼出先 2件 [`00867ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867ed8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) [`00b13030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md) · 呼出先 2件 [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867ed8.md#insn-00867ef8) · [`00867f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867ed8.md#insn-00867f04)
- 新版 `00867f38`（命令位置の公開資料なし） · `00867f44`（命令位置の公開資料なし）

~~~diff
- 00867ef8 ["INT_ADD", "register:40f0:8", ["const:867ef8:8", "const:4:8"]]
- 00867ef8 ["CALL", null, ["local:b0:8"]]
+ 00867f38 ["INT_ADD", "register:40f0:8", ["const:867f38:8", "const:4:8"]]
+ 00867f38 ["CALL", null, ["local:b0:8"]]
- 00867ef8 bytes f8ffff97
+ 00867f38 bytes f8ffff97
- 00867f04 ["INT_ADD", "register:40f0:8", ["const:867f04:8", "const:4:8"]]
- 00867f04 ["CALL", null, ["local:b0:8"]]
+ 00867f44 ["INT_ADD", "register:40f0:8", ["const:867f44:8", "const:4:8"]]
+ 00867f44 ["CALL", null, ["local:b0:8"]]
- 00867f04 bytes f5ffff97
+ 00867f44 bytes f5ffff97
~~~


<a id="compare-d30fc8f977bb548d0e78106979bc0984"></a>

### [`00867f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867f1c.md) → [`00867f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md) FUN_00867f5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00866a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866a2c.md) · 呼出先 3件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md)
- 新版 呼出元 1件 [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) · 呼出先 3件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867f1c.md#insn-00867f44) · [`00867f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867f1c.md#insn-00867f5c) · [`00867f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867f1c.md#insn-00867f64)
- 新版 `00867f84`（命令位置の公開資料なし） · `00867f9c`（命令位置の公開資料なし） · `00867fa4`（命令位置の公開資料なし）

~~~diff
- 00867f44 ["INT_ADD", "register:40f0:8", ["const:867f44:8", "const:4:8"]]
- 00867f44 ["CALL", null, ["callee:005e8198:8"]]
+ 00867f84 ["INT_ADD", "register:40f0:8", ["const:867f84:8", "const:4:8"]]
+ 00867f84 ["CALL", null, ["callee:005e8198:8"]]
- 00867f44 bytes 8500f697
+ 00867f84 bytes 8500f697
- 00867f5c ["INT_ADD", "register:40f0:8", ["const:867f5c:8", "const:4:8"]]
- 00867f5c ["CALL", null, ["callee:0046eef8:8"]]
+ 00867f9c ["INT_ADD", "register:40f0:8", ["const:867f9c:8", "const:4:8"]]
+ 00867f9c ["CALL", null, ["callee:0046eef8:8"]]
- 00867f5c bytes d71bf097
+ 00867f9c bytes d71bf097
- 00867f64 ["INT_ADD", "register:40f0:8", ["const:867f64:8", "const:4:8"]]
- 00867f64 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00867fa4 ["INT_ADD", "register:40f0:8", ["const:867fa4:8", "const:4:8"]]
+ 00867fa4 ["CALL", null, ["callee:0046e7c4:8"]]
- 00867f64 bytes 081af097
+ 00867fa4 bytes 081af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b56738505563d4349f9294715aa0d1"></a>

### [`00868084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868084.md) → [`008680c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008680c4.md) FUN_008680c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) · 呼出先 3件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 3件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008680c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868084.md#insn-008680c0) · [`008680c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868084.md#insn-008680c8) · [`008680f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868084.md#insn-008680f8)
- 新版 `00868100`（命令位置の公開資料なし） · `00868108`（命令位置の公開資料なし） · `00868138`（命令位置の公開資料なし）

~~~diff
- 008680c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008680c0 ["INT_ADD", "register:40f0:8", ["const:8680c0:8", "const:4:8"]]
- 008680c0 ["CALLIND", null, ["register:0:8"]]
+ 00868100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868100 ["INT_ADD", "register:40f0:8", ["const:868100:8", "const:4:8"]]
+ 00868100 ["CALLIND", null, ["register:0:8"]]
- 008680c0 bytes 00013fd6
+ 00868100 bytes 00013fd6
- 008680c8 ["INT_ADD", "register:40f0:8", ["const:8680c8:8", "const:4:8"]]
- 008680c8 ["CALL", null, ["callee:0067e5e8:8"]]
+ 00868108 ["INT_ADD", "register:40f0:8", ["const:868108:8", "const:4:8"]]
+ 00868108 ["CALL", null, ["callee:0067e5e8:8"]]
- 008680c8 bytes 3859f897
+ 00868108 bytes 3859f897
- 008680f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008680f8 ["INT_ADD", "register:40f0:8", ["const:8680f8:8", "const:4:8"]]
- 008680f8 ["CALLIND", null, ["register:0:8"]]
+ 00868138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868138 ["INT_ADD", "register:40f0:8", ["const:868138:8", "const:4:8"]]
+ 00868138 ["CALLIND", null, ["register:0:8"]]
- 008680f8 bytes 00013fd6
+ 00868138 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cc3ccc06bd568f336999c07caa6c78b"></a>

### [`008681f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008681f4.md) → [`00868234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md) FUN_00868234

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) · 呼出先 3件 [`00868698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868698.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 3件 [`008686d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008681f4.md#insn-00868214) · [`00868228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008681f4.md#insn-00868228) · [`00868230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008681f4.md#insn-00868230)
- 新版 `00868254`（命令位置の公開資料なし） · `00868268`（命令位置の公開資料なし） · `00868270`（命令位置の公開資料なし）

~~~diff
- 00868214 ["INT_ADD", "register:40f0:8", ["const:868214:8", "const:4:8"]]
- 00868214 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868254 ["INT_ADD", "register:40f0:8", ["const:868254:8", "const:4:8"]]
+ 00868254 ["CALL", null, ["callee:00c53d00:8"]]
- 00868214 bytes b3ad0f94
+ 00868254 bytes abae0f94
- 00868228 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868228 ["INT_ADD", "register:40f0:8", ["const:868228:8", "const:4:8"]]
- 00868228 ["CALLIND", null, ["register:0:8"]]
+ 00868268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868268 ["INT_ADD", "register:40f0:8", ["const:868268:8", "const:4:8"]]
+ 00868268 ["CALLIND", null, ["register:0:8"]]
- 00868228 bytes 00013fd6
+ 00868268 bytes 00013fd6
- 00868230 ["INT_ADD", "register:40f0:8", ["const:868230:8", "const:4:8"]]
- 00868230 ["CALL", null, ["callee:00c57e80:8"]]
+ 00868270 ["INT_ADD", "register:40f0:8", ["const:868270:8", "const:4:8"]]
+ 00868270 ["CALL", null, ["callee:00c57e80:8"]]
- 00868230 bytes 14be0f94
+ 00868270 bytes 04bf0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b50f2e7f302a3486a8b0e3df9f0ddca"></a>

### [`0086837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/0086837c.md) → [`008683bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008683bc.md) FUN_008683bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) · 呼出先 5件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 5件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/0086837c.md#insn-00868390) · [`00868398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/0086837c.md#insn-00868398) · [`008683a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/0086837c.md#insn-008683a0)
- 新版 `008683d0`（命令位置の公開資料なし） · `008683d8`（命令位置の公開資料なし） · `008683e0`（命令位置の公開資料なし）

~~~diff
- 00868390 ["INT_ADD", "register:40f0:8", ["const:868390:8", "const:4:8"]]
- 00868390 ["CALL", null, ["callee:0046e8a4:8"]]
+ 008683d0 ["INT_ADD", "register:40f0:8", ["const:8683d0:8", "const:4:8"]]
+ 008683d0 ["CALL", null, ["callee:0046e8a4:8"]]
- 00868390 bytes 3519f097
+ 008683d0 bytes 3519f097
- 00868398 ["INT_ADD", "register:40f0:8", ["const:868398:8", "const:4:8"]]
- 00868398 ["CALL", null, ["callee:0046e8a4:8"]]
+ 008683d8 ["INT_ADD", "register:40f0:8", ["const:8683d8:8", "const:4:8"]]
+ 008683d8 ["CALL", null, ["callee:0046e8a4:8"]]
- 00868398 bytes 3319f097
+ 008683d8 bytes 3319f097
- 008683a0 ["INT_ADD", "register:40f0:8", ["const:8683a0:8", "const:4:8"]]
- 008683a0 ["CALL", null, ["callee:0046e8a4:8"]]
+ 008683e0 ["INT_ADD", "register:40f0:8", ["const:8683e0:8", "const:4:8"]]
+ 008683e0 ["CALL", null, ["callee:0046e8a4:8"]]
- 008683a0 bytes 3119f097
+ 008683e0 bytes 3119f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d5d2274ce5de20cbe87244d6ae1019a"></a>

### [`008684b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008684b0.md) → [`008684f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008684f0.md) FUN_008684f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) · 呼出先 4件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 4件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008684c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008684b0.md#insn-008684c4) · [`008684cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008684b0.md#insn-008684cc) · [`008684e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008684b0.md#insn-008684e0)
- 新版 `00868504`（命令位置の公開資料なし） · `0086850c`（命令位置の公開資料なし） · `00868520`（命令位置の公開資料なし）

~~~diff
- 008684c4 ["INT_ADD", "register:40f0:8", ["const:8684c4:8", "const:4:8"]]
- 008684c4 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00868504 ["INT_ADD", "register:40f0:8", ["const:868504:8", "const:4:8"]]
+ 00868504 ["CALL", null, ["callee:0046e8a4:8"]]
- 008684c4 bytes e818f097
+ 00868504 bytes e818f097
- 008684cc ["INT_ADD", "register:40f0:8", ["const:8684cc:8", "const:4:8"]]
- 008684cc ["CALL", null, ["callee:0046efdc:8"]]
+ 0086850c ["INT_ADD", "register:40f0:8", ["const:86850c:8", "const:4:8"]]
+ 0086850c ["CALL", null, ["callee:0046efdc:8"]]
- 008684cc bytes b41af097
+ 0086850c bytes b41af097
- 008684e0 ["INT_ADD", "register:40f0:8", ["const:8684e0:8", "const:4:8"]]
- 008684e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868520 ["INT_ADD", "register:40f0:8", ["const:868520:8", "const:4:8"]]
+ 00868520 ["CALL", null, ["callee:00c53d00:8"]]
- 008684e0 bytes 00ad0f94
+ 00868520 bytes f8ad0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80aeab1d36dd624d1090697a24c59fc8"></a>

### [`00868620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868620.md) → [`00868660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868660.md) FUN_00868660

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868620.md#insn-00868668)
- 新版 `008686a8`（命令位置の公開資料なし）

~~~diff
- 00868668 ["INT_ADD", "register:40f0:8", ["const:868668:8", "const:4:8"]]
- 00868668 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008686a8 ["INT_ADD", "register:40f0:8", ["const:8686a8:8", "const:4:8"]]
+ 008686a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00868668 bytes 12bd0f94
+ 008686a8 bytes 02be0f94
~~~


<a id="compare-959ef473afaaa0c854aff47f02663669"></a>

### [`00868698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868698.md) → [`008686d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md) FUN_008686d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008681f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008681f4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00868234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008686e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868698.md#insn-008686e4) · [`008686f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868698.md#insn-008686f8) · [`00868700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868698.md#insn-00868700)
- 新版 `00868724`（命令位置の公開資料なし） · `00868738`（命令位置の公開資料なし） · `00868740`（命令位置の公開資料なし）

~~~diff
- 008686e4 ["INT_ADD", "register:40f0:8", ["const:8686e4:8", "const:4:8"]]
- 008686e4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868724 ["INT_ADD", "register:40f0:8", ["const:868724:8", "const:4:8"]]
+ 00868724 ["CALL", null, ["callee:00c53d00:8"]]
- 008686e4 bytes 7fac0f94
+ 00868724 bytes 77ad0f94
- 008686f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008686f8 ["INT_ADD", "register:40f0:8", ["const:8686f8:8", "const:4:8"]]
- 008686f8 ["CALLIND", null, ["register:0:8"]]
+ 00868738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868738 ["INT_ADD", "register:40f0:8", ["const:868738:8", "const:4:8"]]
+ 00868738 ["CALLIND", null, ["register:0:8"]]
- 008686f8 bytes 00013fd6
+ 00868738 bytes 00013fd6
- 00868700 ["INT_ADD", "register:40f0:8", ["const:868700:8", "const:4:8"]]
- 00868700 ["CALL", null, ["callee:00c57e80:8"]]
+ 00868740 ["INT_ADD", "register:40f0:8", ["const:868740:8", "const:4:8"]]
+ 00868740 ["CALL", null, ["callee:00c57e80:8"]]
- 00868700 bytes e0bc0f94
+ 00868740 bytes d0bd0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4c9cc647da9305bb3bbdf3a2ab8442"></a>

### [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) → [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) FUN_00868840

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) · 呼出先 2件 [`00868800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) · 呼出先 2件 [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md#insn-00868820) · [`0086882c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868800.md#insn-0086882c)
- 新版 `00868860`（命令位置の公開資料なし） · `0086886c`（命令位置の公開資料なし）

~~~diff
- 00868820 ["INT_ADD", "register:40f0:8", ["const:868820:8", "const:4:8"]]
- 00868820 ["CALL", null, ["local:b0:8"]]
+ 00868860 ["INT_ADD", "register:40f0:8", ["const:868860:8", "const:4:8"]]
+ 00868860 ["CALL", null, ["local:b0:8"]]
- 00868820 bytes f8ffff97
+ 00868860 bytes f8ffff97
- 0086882c ["INT_ADD", "register:40f0:8", ["const:86882c:8", "const:4:8"]]
- 0086882c ["CALL", null, ["local:b0:8"]]
+ 0086886c ["INT_ADD", "register:40f0:8", ["const:86886c:8", "const:4:8"]]
+ 0086886c ["CALL", null, ["local:b0:8"]]
- 0086882c bytes f5ffff97
+ 0086886c bytes f5ffff97
~~~


<a id="compare-cbfdc96befca18736e788a59a5caac1b"></a>

### [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) → [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) FUN_00868884

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) · 呼出先 2件 [`00868844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) · 呼出先 2件 [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md#insn-00868864) · [`00868870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868844.md#insn-00868870)
- 新版 `008688a4`（命令位置の公開資料なし） · `008688b0`（命令位置の公開資料なし）

~~~diff
- 00868864 ["INT_ADD", "register:40f0:8", ["const:868864:8", "const:4:8"]]
- 00868864 ["CALL", null, ["local:b0:8"]]
+ 008688a4 ["INT_ADD", "register:40f0:8", ["const:8688a4:8", "const:4:8"]]
+ 008688a4 ["CALL", null, ["local:b0:8"]]
- 00868864 bytes f8ffff97
+ 008688a4 bytes f8ffff97
- 00868870 ["INT_ADD", "register:40f0:8", ["const:868870:8", "const:4:8"]]
- 00868870 ["CALL", null, ["local:b0:8"]]
+ 008688b0 ["INT_ADD", "register:40f0:8", ["const:8688b0:8", "const:4:8"]]
+ 008688b0 ["CALL", null, ["local:b0:8"]]
- 00868870 bytes f5ffff97
+ 008688b0 bytes f5ffff97
~~~


<a id="compare-9794bd1c733cea99c8ed6a10d5896773"></a>

### [`00868888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868888.md) → [`008688c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008688c8.md) FUN_008688c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008688d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868888.md#insn-008688d4) · [`008688e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868888.md#insn-008688e8) · [`008688f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868888.md#insn-008688f0)
- 新版 `00868914`（命令位置の公開資料なし） · `00868928`（命令位置の公開資料なし） · `00868930`（命令位置の公開資料なし）

~~~diff
- 008688d4 ["INT_ADD", "register:40f0:8", ["const:8688d4:8", "const:4:8"]]
- 008688d4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868914 ["INT_ADD", "register:40f0:8", ["const:868914:8", "const:4:8"]]
+ 00868914 ["CALL", null, ["callee:00c53d00:8"]]
- 008688d4 bytes 03ac0f94
+ 00868914 bytes fbac0f94
- 008688e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008688e8 ["INT_ADD", "register:40f0:8", ["const:8688e8:8", "const:4:8"]]
- 008688e8 ["CALLIND", null, ["register:0:8"]]
+ 00868928 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868928 ["INT_ADD", "register:40f0:8", ["const:868928:8", "const:4:8"]]
+ 00868928 ["CALLIND", null, ["register:0:8"]]
- 008688e8 bytes 00013fd6
+ 00868928 bytes 00013fd6
- 008688f0 ["INT_ADD", "register:40f0:8", ["const:8688f0:8", "const:4:8"]]
- 008688f0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00868930 ["INT_ADD", "register:40f0:8", ["const:868930:8", "const:4:8"]]
+ 00868930 ["CALL", null, ["callee:00c57e80:8"]]
- 008688f0 bytes 64bc0f94
+ 00868930 bytes 54bd0f94
~~~


<a id="compare-d28d26b3e5b6b227d84089bc86fa205c"></a>

### [`00868920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868920.md) → [`00868960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868960.md) FUN_00868960

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846964.md) · 呼出先 7件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006fb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb034.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`008469a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008469a4.md) · 呼出先 7件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868920.md#insn-0086893c) · [`0086894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868920.md#insn-0086894c) · [`00868958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868920.md#insn-00868958)
- 新版 `0086897c`（命令位置の公開資料なし） · `0086898c`（命令位置の公開資料なし） · `00868998`（命令位置の公開資料なし）

~~~diff
- 0086893c ["INT_ADD", "register:40f0:8", ["const:86893c:8", "const:4:8"]]
- 0086893c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086897c ["INT_ADD", "register:40f0:8", ["const:86897c:8", "const:4:8"]]
+ 0086897c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086893c bytes 5dbc0f94
+ 0086897c bytes 4dbd0f94
- 0086894c ["INT_ADD", "register:40f0:8", ["const:86894c:8", "const:4:8"]]
- 0086894c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086898c ["INT_ADD", "register:40f0:8", ["const:86898c:8", "const:4:8"]]
+ 0086898c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086894c bytes 59bc0f94
+ 0086898c bytes 49bd0f94
- 00868958 ["INT_ADD", "register:40f0:8", ["const:868958:8", "const:4:8"]]
- 00868958 ["CALL", null, ["callee:006fb074:8"]]
+ 00868998 ["INT_ADD", "register:40f0:8", ["const:868998:8", "const:4:8"]]
+ 00868998 ["CALL", null, ["callee:006fb074:8"]]
- 00868958 bytes b749fa97
+ 00868998 bytes b749fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7470a48c9a1c3e64b9d151e6d4fe488"></a>

### [`008689b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md) → [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) FUN_008689f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md) · 呼出先 8件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00868a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md) [`00868be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md)
- 新版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 8件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00868ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md) [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008689d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md#insn-008689d4) · [`008689dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md#insn-008689dc) · [`008689f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md#insn-008689f0)
- 新版 `00868a14`（命令位置の公開資料なし） · `00868a1c`（命令位置の公開資料なし） · `00868a30`（命令位置の公開資料なし）

~~~diff
- 008689d4 ["INT_ADD", "register:40f0:8", ["const:8689d4:8", "const:4:8"]]
- 008689d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00868a14 ["INT_ADD", "register:40f0:8", ["const:868a14:8", "const:4:8"]]
+ 00868a14 ["CALL", null, ["callee:00c57eb0:8"]]
- 008689d4 bytes 37bc0f94
+ 00868a14 bytes 27bd0f94
- 008689dc ["INT_ADD", "register:40f0:8", ["const:8689dc:8", "const:4:8"]]
- 008689dc ["CALL", null, ["callee:00868ac0:8"]]
+ 00868a1c ["INT_ADD", "register:40f0:8", ["const:868a1c:8", "const:4:8"]]
+ 00868a1c ["CALL", null, ["callee:00868ac0:8"]]
- 008689dc bytes 29000094
+ 00868a1c bytes 29000094
- 008689f0 ["INT_ADD", "register:40f0:8", ["const:8689f0:8", "const:4:8"]]
- 008689f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868a30 ["INT_ADD", "register:40f0:8", ["const:868a30:8", "const:4:8"]]
+ 00868a30 ["CALL", null, ["callee:00c53d00:8"]]
- 008689f0 bytes bcab0f94
+ 00868a30 bytes b4ac0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68803a96809ab037a883a65b70653eee"></a>

### [`00868a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md) → [`00868ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md) FUN_00868ac0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008689b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md) [`008e3bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md) [`008e9424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) [`008e3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3d50.md) [`008e95c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e95c0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md#insn-00868ac8) · [`00868ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md#insn-00868ad8) · [`00868b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md#insn-00868b10)
- 新版 `00868b08`（命令位置の公開資料なし） · `00868b18`（命令位置の公開資料なし） · `00868b50`（命令位置の公開資料なし）

~~~diff
- 00868ac8 ["INT_ADD", "register:40f0:8", ["const:868ac8:8", "const:4:8"]]
- 00868ac8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00868b08 ["INT_ADD", "register:40f0:8", ["const:868b08:8", "const:4:8"]]
+ 00868b08 ["CALL", null, ["callee:00c57eb0:8"]]
- 00868ac8 bytes fabb0f94
+ 00868b08 bytes eabc0f94
- 00868ad8 ["INT_ADD", "register:40f0:8", ["const:868ad8:8", "const:4:8"]]
- 00868ad8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00868b18 ["INT_ADD", "register:40f0:8", ["const:868b18:8", "const:4:8"]]
+ 00868b18 ["CALL", null, ["callee:00c57eb0:8"]]
- 00868ad8 bytes f6bb0f94
+ 00868b18 bytes e6bc0f94
- 00868b10 ["INT_ADD", "register:40f0:8", ["const:868b10:8", "const:4:8"]]
- 00868b10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00868b50 ["INT_ADD", "register:40f0:8", ["const:868b50:8", "const:4:8"]]
+ 00868b50 ["CALL", null, ["callee:00c57eb0:8"]]
- 00868b10 bytes e8bb0f94
+ 00868b50 bytes d8bc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c422a0d88ecd8ecb52f9a4bee87c451"></a>

### [`00868be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md) → [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) FUN_00868c20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`008689b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md) [`00868be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md) [`008e1ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md) [`008e43c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43c4.md) · 呼出先 2件 [`00868be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) [`008e1d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e1/008e1d44.md) [`008e4560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4560.md) · 呼出先 2件 [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md#insn-00868c00) · [`00868c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md#insn-00868c0c)
- 新版 `00868c40`（命令位置の公開資料なし） · `00868c4c`（命令位置の公開資料なし）

~~~diff
- 00868c00 ["INT_ADD", "register:40f0:8", ["const:868c00:8", "const:4:8"]]
- 00868c00 ["CALL", null, ["local:b0:8"]]
+ 00868c40 ["INT_ADD", "register:40f0:8", ["const:868c40:8", "const:4:8"]]
+ 00868c40 ["CALL", null, ["local:b0:8"]]
- 00868c00 bytes f8ffff97
+ 00868c40 bytes f8ffff97
- 00868c0c ["INT_ADD", "register:40f0:8", ["const:868c0c:8", "const:4:8"]]
- 00868c0c ["CALL", null, ["local:b0:8"]]
+ 00868c4c ["INT_ADD", "register:40f0:8", ["const:868c4c:8", "const:4:8"]]
+ 00868c4c ["CALL", null, ["local:b0:8"]]
- 00868c0c bytes f5ffff97
+ 00868c4c bytes f5ffff97
~~~


<a id="compare-dc3f042c69d5740cd8041f2d0e2c8ff7"></a>

### [`00868c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md) → [`00868c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md) FUN_00868c64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084725c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md) · 呼出先 5件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00868f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) · 呼出先 5件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md#insn-00868c48) · [`00868c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md#insn-00868c5c) · [`00868c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md#insn-00868c64)
- 新版 `00868c88`（命令位置の公開資料なし） · `00868c9c`（命令位置の公開資料なし） · `00868ca4`（命令位置の公開資料なし）

~~~diff
- 00868c48 ["INT_ADD", "register:40f0:8", ["const:868c48:8", "const:4:8"]]
- 00868c48 ["CALL", null, ["callee:00c53d00:8"]]
+ 00868c88 ["INT_ADD", "register:40f0:8", ["const:868c88:8", "const:4:8"]]
+ 00868c88 ["CALL", null, ["callee:00c53d00:8"]]
- 00868c48 bytes 26ab0f94
+ 00868c88 bytes 1eac0f94
- 00868c5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00868c5c ["INT_ADD", "register:40f0:8", ["const:868c5c:8", "const:4:8"]]
- 00868c5c ["CALLIND", null, ["register:0:8"]]
+ 00868c9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868c9c ["INT_ADD", "register:40f0:8", ["const:868c9c:8", "const:4:8"]]
+ 00868c9c ["CALLIND", null, ["register:0:8"]]
- 00868c5c bytes 00013fd6
+ 00868c9c bytes 00013fd6
- 00868c64 ["INT_ADD", "register:40f0:8", ["const:868c64:8", "const:4:8"]]
- 00868c64 ["CALL", null, ["callee:00c57e80:8"]]
+ 00868ca4 ["INT_ADD", "register:40f0:8", ["const:868ca4:8", "const:4:8"]]
+ 00868ca4 ["CALL", null, ["callee:00c57e80:8"]]
- 00868c64 bytes 87bb0f94
+ 00868ca4 bytes 77bc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a9a4193de31c55454d6db5b5d7fed38"></a>

### [`00868d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868d0c.md) → [`00868d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md) FUN_00868d4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084725c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md) · 呼出先 7件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) · 呼出先 7件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868d0c.md#insn-00868d2c) · [`00868d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868d0c.md#insn-00868d40) · [`00868d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868d0c.md#insn-00868d48)
- 新版 `00868d6c`（命令位置の公開資料なし） · `00868d80`（命令位置の公開資料なし） · `00868d88`（命令位置の公開資料なし）

~~~diff
- 00868d2c ["INT_ADD", "register:40f0:8", ["const:868d2c:8", "const:4:8"]]
- 00868d2c ["CALL", null, ["callee:00c53d00:8"]]
+ 00868d6c ["INT_ADD", "register:40f0:8", ["const:868d6c:8", "const:4:8"]]
+ 00868d6c ["CALL", null, ["callee:00c53d00:8"]]
- 00868d2c bytes edaa0f94
+ 00868d6c bytes e5ab0f94
- 00868d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868d40 ["INT_ADD", "register:40f0:8", ["const:868d40:8", "const:4:8"]]
- 00868d40 ["CALLIND", null, ["register:0:8"]]
+ 00868d80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868d80 ["INT_ADD", "register:40f0:8", ["const:868d80:8", "const:4:8"]]
+ 00868d80 ["CALLIND", null, ["register:0:8"]]
- 00868d40 bytes 00013fd6
+ 00868d80 bytes 00013fd6
- 00868d48 ["INT_ADD", "register:40f0:8", ["const:868d48:8", "const:4:8"]]
- 00868d48 ["CALL", null, ["callee:00c57e80:8"]]
+ 00868d88 ["INT_ADD", "register:40f0:8", ["const:868d88:8", "const:4:8"]]
+ 00868d88 ["CALL", null, ["callee:00c57e80:8"]]
- 00868d48 bytes 4ebb0f94
+ 00868d88 bytes 3ebc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-608157b9c9c68164dc06035ff3d46de8"></a>

### [`00868f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md) → [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) FUN_00868fac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00868c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md) [`00868f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) · 呼出先 3件 [`00868f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md) [`00868fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868fb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00868c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md) [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 3件 [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`00868ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md#insn-00868f8c) · [`00868f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md#insn-00868f98) · [`00868fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md#insn-00868fa0)
- 新版 `00868fcc`（命令位置の公開資料なし） · `00868fd8`（命令位置の公開資料なし） · `00868fe0`（命令位置の公開資料なし）

~~~diff
- 00868f8c ["INT_ADD", "register:40f0:8", ["const:868f8c:8", "const:4:8"]]
- 00868f8c ["CALL", null, ["local:b0:8"]]
+ 00868fcc ["INT_ADD", "register:40f0:8", ["const:868fcc:8", "const:4:8"]]
+ 00868fcc ["CALL", null, ["local:b0:8"]]
- 00868f8c bytes f8ffff97
+ 00868fcc bytes f8ffff97
- 00868f98 ["INT_ADD", "register:40f0:8", ["const:868f98:8", "const:4:8"]]
- 00868f98 ["CALL", null, ["local:b0:8"]]
+ 00868fd8 ["INT_ADD", "register:40f0:8", ["const:868fd8:8", "const:4:8"]]
+ 00868fd8 ["CALL", null, ["local:b0:8"]]
- 00868f98 bytes f5ffff97
+ 00868fd8 bytes f5ffff97
- 00868fa0 ["INT_ADD", "register:40f0:8", ["const:868fa0:8", "const:4:8"]]
- 00868fa0 ["CALL", null, ["callee:00868ff8:8"]]
+ 00868fe0 ["INT_ADD", "register:40f0:8", ["const:868fe0:8", "const:4:8"]]
+ 00868fe0 ["CALL", null, ["callee:00868ff8:8"]]
- 00868fa0 bytes 06000094
+ 00868fe0 bytes 06000094
~~~


<a id="compare-356727de0307b75ba6e8d1110fcc6aef"></a>

### [`00868fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868fb8.md) → [`00868ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md) FUN_00868ff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00868f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868f6c.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) · 呼出先 3件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868fb8.md#insn-00868fd0) · [`00868fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868fb8.md#insn-00868fdc) · [`00868fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868fb8.md#insn-00868fe8)
- 新版 `00869010`（命令位置の公開資料なし） · `0086901c`（命令位置の公開資料なし） · `00869028`（命令位置の公開資料なし）

~~~diff
- 00868fd0 ["INT_ADD", "register:40f0:8", ["const:868fd0:8", "const:4:8"]]
- 00868fd0 ["CALL", null, ["callee:00676a60:8"]]
+ 00869010 ["INT_ADD", "register:40f0:8", ["const:869010:8", "const:4:8"]]
+ 00869010 ["CALL", null, ["callee:00676a60:8"]]
- 00868fd0 bytes 9436f897
+ 00869010 bytes 9436f897
- 00868fdc ["INT_ADD", "register:40f0:8", ["const:868fdc:8", "const:4:8"]]
- 00868fdc ["CALL", null, ["callee:00676a60:8"]]
+ 0086901c ["INT_ADD", "register:40f0:8", ["const:86901c:8", "const:4:8"]]
+ 0086901c ["CALL", null, ["callee:00676a60:8"]]
- 00868fdc bytes 9136f897
+ 0086901c bytes 9136f897
- 00868fe8 ["INT_ADD", "register:40f0:8", ["const:868fe8:8", "const:4:8"]]
- 00868fe8 ["CALL", null, ["callee:00676a60:8"]]
+ 00869028 ["INT_ADD", "register:40f0:8", ["const:869028:8", "const:4:8"]]
+ 00869028 ["CALL", null, ["callee:00676a60:8"]]
- 00868fe8 bytes 8e36f897
+ 00869028 bytes 8e36f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-158af3eb8132fc2847e8bc3ff0f98b05"></a>

### [`008690a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md) → [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) FUN_008690e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008690a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md) [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) · 呼出先 3件 [`008690a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md) [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) · 呼出先 3件 [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008690c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md#insn-008690c8) · [`008690d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md#insn-008690d4) · [`008690e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md#insn-008690e0)
- 新版 `00869108`（命令位置の公開資料なし） · `00869114`（命令位置の公開資料なし） · `00869120`（命令位置の公開資料なし）

~~~diff
- 008690c8 ["INT_ADD", "register:40f0:8", ["const:8690c8:8", "const:4:8"]]
- 008690c8 ["CALL", null, ["local:b0:8"]]
+ 00869108 ["INT_ADD", "register:40f0:8", ["const:869108:8", "const:4:8"]]
+ 00869108 ["CALL", null, ["local:b0:8"]]
- 008690c8 bytes f8ffff97
+ 00869108 bytes f8ffff97
- 008690d4 ["INT_ADD", "register:40f0:8", ["const:8690d4:8", "const:4:8"]]
- 008690d4 ["CALL", null, ["local:b0:8"]]
+ 00869114 ["INT_ADD", "register:40f0:8", ["const:869114:8", "const:4:8"]]
+ 00869114 ["CALL", null, ["local:b0:8"]]
- 008690d4 bytes f5ffff97
+ 00869114 bytes f5ffff97
- 008690e0 ["INT_ADD", "register:40f0:8", ["const:8690e0:8", "const:4:8"]]
- 008690e0 ["CALL", null, ["callee:00869138:8"]]
+ 00869120 ["INT_ADD", "register:40f0:8", ["const:869120:8", "const:4:8"]]
+ 00869120 ["CALL", null, ["callee:00869138:8"]]
- 008690e0 bytes 06000094
+ 00869120 bytes 06000094
~~~


<a id="compare-410c409994566b460dde28411fb88da6"></a>

### [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) → [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) FUN_00869138

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`008690a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690a8.md) [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) [`00a67a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a88.md) [`00a67e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67e1c.md) · 呼出先 2件 [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) [`00a67c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md) [`00a68014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68014.md) · 呼出先 2件 [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md#insn-00869114) · [`00869120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md#insn-00869120) · [`00869130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md#insn-00869130)
- 新版 `00869154`（命令位置の公開資料なし） · `00869160`（命令位置の公開資料なし） · `00869170`（命令位置の公開資料なし）

~~~diff
- 00869114 ["INT_ADD", "register:40f0:8", ["const:869114:8", "const:4:8"]]
- 00869114 ["CALL", null, ["local:b0:8"]]
+ 00869154 ["INT_ADD", "register:40f0:8", ["const:869154:8", "const:4:8"]]
+ 00869154 ["CALL", null, ["local:b0:8"]]
- 00869114 bytes f9ffff97
+ 00869154 bytes f9ffff97
- 00869120 ["INT_ADD", "register:40f0:8", ["const:869120:8", "const:4:8"]]
- 00869120 ["CALL", null, ["local:b0:8"]]
+ 00869160 ["INT_ADD", "register:40f0:8", ["const:869160:8", "const:4:8"]]
+ 00869160 ["CALL", null, ["local:b0:8"]]
- 00869120 bytes f6ffff97
+ 00869160 bytes f6ffff97
- 00869130 ["INT_ADD", "register:40f0:8", ["const:869130:8", "const:4:8"]]
- 00869130 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869170 ["INT_ADD", "register:40f0:8", ["const:869170:8", "const:4:8"]]
+ 00869170 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869130 bytes 60ba0f94
+ 00869170 bytes 50bb0f94
~~~


<a id="compare-17b8a69a99d503a8d15232ae64c8e41d"></a>

### [`00869148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md) → [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) FUN_00869188

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`008473a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md) [`00a37e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e00.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) [`00a39e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39e20.md) [`00a3a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a070.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a37ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ff8.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00a3a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md) [`00a3a268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a268.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md#insn-00869164) · [`00869170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md#insn-00869170) · [`008691a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md#insn-008691a8)
- 新版 `008691a4`（命令位置の公開資料なし） · `008691b0`（命令位置の公開資料なし） · `008691e8`（命令位置の公開資料なし）

~~~diff
- 00869164 ["INT_ADD", "register:40f0:8", ["const:869164:8", "const:4:8"]]
- 00869164 ["CALL", null, ["callee:0046d490:8"]]
+ 008691a4 ["INT_ADD", "register:40f0:8", ["const:8691a4:8", "const:4:8"]]
+ 008691a4 ["CALL", null, ["callee:0046d490:8"]]
- 00869164 bytes bb10f097
+ 008691a4 bytes bb10f097
- 00869170 ["INT_ADD", "register:40f0:8", ["const:869170:8", "const:4:8"]]
- 00869170 ["CALL", null, ["callee:0046d490:8"]]
+ 008691b0 ["INT_ADD", "register:40f0:8", ["const:8691b0:8", "const:4:8"]]
+ 008691b0 ["CALL", null, ["callee:0046d490:8"]]
- 00869170 bytes b810f097
+ 008691b0 bytes b810f097
- 008691a8 ["INT_ADD", "register:40f0:8", ["const:8691a8:8", "const:4:8"]]
- 008691a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008691e8 ["INT_ADD", "register:40f0:8", ["const:8691e8:8", "const:4:8"]]
+ 008691e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 008691a8 bytes 42ba0f94
+ 008691e8 bytes 32bb0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fba96943d95e800511a5464c1e367a1"></a>

### [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) → [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) FUN_00869228

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`008473a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md) [`00a37e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) [`00a39be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39be0.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a38064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00a39dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md#insn-00869220) · [`0086922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md#insn-0086922c) · [`00869238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md#insn-00869238)
- 新版 `00869260`（命令位置の公開資料なし） · `0086926c`（命令位置の公開資料なし） · `00869278`（命令位置の公開資料なし）

~~~diff
- 00869220 ["INT_ADD", "register:40f0:8", ["const:869220:8", "const:4:8"]]
- 00869220 ["CALL", null, ["callee:0046d490:8"]]
+ 00869260 ["INT_ADD", "register:40f0:8", ["const:869260:8", "const:4:8"]]
+ 00869260 ["CALL", null, ["callee:0046d490:8"]]
- 00869220 bytes 8c10f097
+ 00869260 bytes 8c10f097
- 0086922c ["INT_ADD", "register:40f0:8", ["const:86922c:8", "const:4:8"]]
- 0086922c ["CALL", null, ["callee:0046d490:8"]]
+ 0086926c ["INT_ADD", "register:40f0:8", ["const:86926c:8", "const:4:8"]]
+ 0086926c ["CALL", null, ["callee:0046d490:8"]]
- 0086922c bytes 8910f097
+ 0086926c bytes 8910f097
- 00869238 ["INT_ADD", "register:40f0:8", ["const:869238:8", "const:4:8"]]
- 00869238 ["CALL", null, ["callee:0046d490:8"]]
+ 00869278 ["INT_ADD", "register:40f0:8", ["const:869278:8", "const:4:8"]]
+ 00869278 ["CALL", null, ["callee:0046d490:8"]]
- 00869238 bytes 8610f097
+ 00869278 bytes 8610f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf736992c8e206361661cc848e36c51"></a>

### [`008692cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md) → [`0086930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md) FUN_0086930c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008473a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md) [`00a37ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37ed4.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a380cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a380cc.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md#insn-00869314) · [`00869330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md#insn-00869330) · [`00869368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md#insn-00869368)
- 新版 `00869354`（命令位置の公開資料なし） · `00869370`（命令位置の公開資料なし） · `008693a8`（命令位置の公開資料なし）

~~~diff
- 00869314 ["INT_ADD", "register:40f0:8", ["const:869314:8", "const:4:8"]]
- 00869314 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869354 ["INT_ADD", "register:40f0:8", ["const:869354:8", "const:4:8"]]
+ 00869354 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869314 bytes e7b90f94
+ 00869354 bytes d7ba0f94
- 00869330 ["INT_ADD", "register:40f0:8", ["const:869330:8", "const:4:8"]]
- 00869330 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869370 ["INT_ADD", "register:40f0:8", ["const:869370:8", "const:4:8"]]
+ 00869370 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869330 bytes e0b90f94
+ 00869370 bytes d0ba0f94
- 00869368 ["INT_ADD", "register:40f0:8", ["const:869368:8", "const:4:8"]]
- 00869368 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008693a8 ["INT_ADD", "register:40f0:8", ["const:8693a8:8", "const:4:8"]]
+ 008693a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869368 bytes d2b90f94
+ 008693a8 bytes c2ba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8c9771125ef02b5e3d61932aeb7f693"></a>

### [`00869380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md) → [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) FUN_008693c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md) [`00869380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md) · 呼出先 2件 [`00869380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474b0.md) [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) · 呼出先 2件 [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086939c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md#insn-0086939c) · [`008693a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md#insn-008693a8) · [`008693b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md#insn-008693b8)
- 新版 `008693dc`（命令位置の公開資料なし） · `008693e8`（命令位置の公開資料なし） · `008693f8`（命令位置の公開資料なし）

~~~diff
- 0086939c ["INT_ADD", "register:40f0:8", ["const:86939c:8", "const:4:8"]]
- 0086939c ["CALL", null, ["local:b0:8"]]
+ 008693dc ["INT_ADD", "register:40f0:8", ["const:8693dc:8", "const:4:8"]]
+ 008693dc ["CALL", null, ["local:b0:8"]]
- 0086939c bytes f9ffff97
+ 008693dc bytes f9ffff97
- 008693a8 ["INT_ADD", "register:40f0:8", ["const:8693a8:8", "const:4:8"]]
- 008693a8 ["CALL", null, ["local:b0:8"]]
+ 008693e8 ["INT_ADD", "register:40f0:8", ["const:8693e8:8", "const:4:8"]]
+ 008693e8 ["CALL", null, ["local:b0:8"]]
- 008693a8 bytes f6ffff97
+ 008693e8 bytes f6ffff97
- 008693b8 ["INT_ADD", "register:40f0:8", ["const:8693b8:8", "const:4:8"]]
- 008693b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008693f8 ["INT_ADD", "register:40f0:8", ["const:8693f8:8", "const:4:8"]]
+ 008693f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 008693b8 bytes beb90f94
+ 008693f8 bytes aeba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0227c4069617f2f44c7b157f9826940f"></a>

### [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) → [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) FUN_00869420

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md) [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) · 呼出先 2件 [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474b0.md) [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) · 呼出先 2件 [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md#insn-00869400) · [`0086940c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md#insn-0086940c)
- 新版 `00869440`（命令位置の公開資料なし） · `0086944c`（命令位置の公開資料なし）

~~~diff
- 00869400 ["INT_ADD", "register:40f0:8", ["const:869400:8", "const:4:8"]]
- 00869400 ["CALL", null, ["local:b0:8"]]
+ 00869440 ["INT_ADD", "register:40f0:8", ["const:869440:8", "const:4:8"]]
+ 00869440 ["CALL", null, ["local:b0:8"]]
- 00869400 bytes f8ffff97
+ 00869440 bytes f8ffff97
- 0086940c ["INT_ADD", "register:40f0:8", ["const:86940c:8", "const:4:8"]]
- 0086940c ["CALL", null, ["local:b0:8"]]
+ 0086944c ["INT_ADD", "register:40f0:8", ["const:86944c:8", "const:4:8"]]
+ 0086944c ["CALL", null, ["local:b0:8"]]
- 0086940c bytes f5ffff97
+ 0086944c bytes f5ffff97
~~~


<a id="compare-fcb3646aa281baea35b339f0999fc047"></a>

### [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) → [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) FUN_00869464

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) · 呼出先 2件 [`00869424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) · 呼出先 2件 [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md#insn-00869440) · [`0086944c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md#insn-0086944c) · [`0086945c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869424.md#insn-0086945c)
- 新版 `00869480`（命令位置の公開資料なし） · `0086948c`（命令位置の公開資料なし） · `0086949c`（命令位置の公開資料なし）

~~~diff
- 00869440 ["INT_ADD", "register:40f0:8", ["const:869440:8", "const:4:8"]]
- 00869440 ["CALL", null, ["local:b0:8"]]
+ 00869480 ["INT_ADD", "register:40f0:8", ["const:869480:8", "const:4:8"]]
+ 00869480 ["CALL", null, ["local:b0:8"]]
- 00869440 bytes f9ffff97
+ 00869480 bytes f9ffff97
- 0086944c ["INT_ADD", "register:40f0:8", ["const:86944c:8", "const:4:8"]]
- 0086944c ["CALL", null, ["local:b0:8"]]
+ 0086948c ["INT_ADD", "register:40f0:8", ["const:86948c:8", "const:4:8"]]
+ 0086948c ["CALL", null, ["local:b0:8"]]
- 0086944c bytes f6ffff97
+ 0086948c bytes f6ffff97
- 0086945c ["INT_ADD", "register:40f0:8", ["const:86945c:8", "const:4:8"]]
- 0086945c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086949c ["INT_ADD", "register:40f0:8", ["const:86949c:8", "const:4:8"]]
+ 0086949c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086945c bytes 95b90f94
+ 0086949c bytes 85ba0f94
~~~


<a id="compare-9353d9cb586d5e05e4dc03ba272a1705"></a>

### [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) → [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) FUN_008694b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084766c.md) [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) [`00aaf838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aaf/00aaf838.md) [`00ab07f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab07f8.md) · 呼出先 2件 [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008476ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008476ac.md) [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) [`00aafa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aaf/00aafa34.md) [`00ab09f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab09f4.md) · 呼出先 2件 [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md#insn-00869490) · [`0086949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md#insn-0086949c) · [`008694ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md#insn-008694ac)
- 新版 `008694d0`（命令位置の公開資料なし） · `008694dc`（命令位置の公開資料なし） · `008694ec`（命令位置の公開資料なし）

~~~diff
- 00869490 ["INT_ADD", "register:40f0:8", ["const:869490:8", "const:4:8"]]
- 00869490 ["CALL", null, ["local:b0:8"]]
+ 008694d0 ["INT_ADD", "register:40f0:8", ["const:8694d0:8", "const:4:8"]]
+ 008694d0 ["CALL", null, ["local:b0:8"]]
- 00869490 bytes f9ffff97
+ 008694d0 bytes f9ffff97
- 0086949c ["INT_ADD", "register:40f0:8", ["const:86949c:8", "const:4:8"]]
- 0086949c ["CALL", null, ["local:b0:8"]]
+ 008694dc ["INT_ADD", "register:40f0:8", ["const:8694dc:8", "const:4:8"]]
+ 008694dc ["CALL", null, ["local:b0:8"]]
- 0086949c bytes f6ffff97
+ 008694dc bytes f6ffff97
- 008694ac ["INT_ADD", "register:40f0:8", ["const:8694ac:8", "const:4:8"]]
- 008694ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 008694ec ["INT_ADD", "register:40f0:8", ["const:8694ec:8", "const:4:8"]]
+ 008694ec ["CALL", null, ["callee:00c57eb0:8"]]
- 008694ac bytes 81b90f94
+ 008694ec bytes 71ba0f94
~~~


<a id="compare-53886a778bee89477b8dc8214181331e"></a>

### [`008694c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008694c4.md) → [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) FUN_00869504

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`008694c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008694c4.md) · 呼出先 2件 [`008694c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008694c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) · 呼出先 2件 [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008694e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008694c4.md#insn-008694e4) · [`008694f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008694c4.md#insn-008694f0)
- 新版 `00869524`（命令位置の公開資料なし） · `00869530`（命令位置の公開資料なし）

~~~diff
- 008694e4 ["INT_ADD", "register:40f0:8", ["const:8694e4:8", "const:4:8"]]
- 008694e4 ["CALL", null, ["local:b0:8"]]
+ 00869524 ["INT_ADD", "register:40f0:8", ["const:869524:8", "const:4:8"]]
+ 00869524 ["CALL", null, ["local:b0:8"]]
- 008694e4 bytes f8ffff97
+ 00869524 bytes f8ffff97
- 008694f0 ["INT_ADD", "register:40f0:8", ["const:8694f0:8", "const:4:8"]]
- 008694f0 ["CALL", null, ["local:b0:8"]]
+ 00869530 ["INT_ADD", "register:40f0:8", ["const:869530:8", "const:4:8"]]
+ 00869530 ["CALL", null, ["local:b0:8"]]
- 008694f0 bytes f5ffff97
+ 00869530 bytes f5ffff97
~~~


<a id="compare-d4868a10934fcce8e6aa00161f7db8df"></a>

### [`00869508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869508.md) → [`00869548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md) FUN_00869548

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) · 呼出先 6件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869508.md#insn-00869554) · [`00869564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869508.md#insn-00869564) · [`00869574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869508.md#insn-00869574)
- 新版 `00869594`（命令位置の公開資料なし） · `008695a4`（命令位置の公開資料なし） · `008695b4`（命令位置の公開資料なし）

~~~diff
- 00869554 ["INT_ADD", "register:40f0:8", ["const:869554:8", "const:4:8"]]
- 00869554 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869594 ["INT_ADD", "register:40f0:8", ["const:869594:8", "const:4:8"]]
+ 00869594 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869554 bytes 57b90f94
+ 00869594 bytes 47ba0f94
- 00869564 ["INT_ADD", "register:40f0:8", ["const:869564:8", "const:4:8"]]
- 00869564 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008695a4 ["INT_ADD", "register:40f0:8", ["const:8695a4:8", "const:4:8"]]
+ 008695a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869564 bytes 53b90f94
+ 008695a4 bytes 43ba0f94
- 00869574 ["INT_ADD", "register:40f0:8", ["const:869574:8", "const:4:8"]]
- 00869574 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008695b4 ["INT_ADD", "register:40f0:8", ["const:8695b4:8", "const:4:8"]]
+ 008695b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869574 bytes 4fb90f94
+ 008695b4 bytes 3fba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1100cbf4fae60514c1ec7a635f050bf"></a>

### [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) → [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) FUN_00869784

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) · 呼出先 2件 [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) · 呼出先 2件 [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md#insn-00869764) · [`00869770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md#insn-00869770)
- 新版 `008697a4`（命令位置の公開資料なし） · `008697b0`（命令位置の公開資料なし）

~~~diff
- 00869764 ["INT_ADD", "register:40f0:8", ["const:869764:8", "const:4:8"]]
- 00869764 ["CALL", null, ["local:b0:8"]]
+ 008697a4 ["INT_ADD", "register:40f0:8", ["const:8697a4:8", "const:4:8"]]
+ 008697a4 ["CALL", null, ["local:b0:8"]]
- 00869764 bytes f8ffff97
+ 008697a4 bytes f8ffff97
- 00869770 ["INT_ADD", "register:40f0:8", ["const:869770:8", "const:4:8"]]
- 00869770 ["CALL", null, ["local:b0:8"]]
+ 008697b0 ["INT_ADD", "register:40f0:8", ["const:8697b0:8", "const:4:8"]]
+ 008697b0 ["CALL", null, ["local:b0:8"]]
- 00869770 bytes f5ffff97
+ 008697b0 bytes f5ffff97
~~~


<a id="compare-5dda72a6e3db54ad58178787d5674e2a"></a>

### [`00869788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md) → [`008697c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md) FUN_008697c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847af8.md) [`009bdb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md) [`009c03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03f0.md) [`009c0e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0e48.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847b38.md) [`009bdd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdd38.md) [`009c058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c058c.md) [`009c0fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0fe4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008697d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md#insn-008697d0) · [`008697e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md#insn-008697e0) · [`0086980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md#insn-0086980c)
- 新版 `00869810`（命令位置の公開資料なし） · `00869820`（命令位置の公開資料なし） · `0086984c`（命令位置の公開資料なし）

~~~diff
- 008697d0 ["INT_ADD", "register:40f0:8", ["const:8697d0:8", "const:4:8"]]
- 008697d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869810 ["INT_ADD", "register:40f0:8", ["const:869810:8", "const:4:8"]]
+ 00869810 ["CALL", null, ["callee:00c57eb0:8"]]
- 008697d0 bytes b8b80f94
+ 00869810 bytes a8b90f94
- 008697e0 ["INT_ADD", "register:40f0:8", ["const:8697e0:8", "const:4:8"]]
- 008697e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869820 ["INT_ADD", "register:40f0:8", ["const:869820:8", "const:4:8"]]
+ 00869820 ["CALL", null, ["callee:00c57eb0:8"]]
- 008697e0 bytes b4b80f94
+ 00869820 bytes a4b90f94
- 0086980c ["INT_ADD", "register:40f0:8", ["const:86980c:8", "const:4:8"]]
- 0086980c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086984c ["INT_ADD", "register:40f0:8", ["const:86984c:8", "const:4:8"]]
+ 0086984c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086980c bytes a9b80f94
+ 0086984c bytes 99b90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-819146f8e160bb173620d1be9858cda0"></a>

### [`00869948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md) → [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) FUN_00869988

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md) [`00a82d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82d34.md) · 呼出先 4件 [`00869948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) [`00a82f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a82/00a82f2c.md) · 呼出先 4件 [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086996c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md#insn-0086996c) · [`00869978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md#insn-00869978) · [`008699a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md#insn-008699a0)
- 新版 `008699ac`（命令位置の公開資料なし） · `008699b8`（命令位置の公開資料なし） · `008699e0`（命令位置の公開資料なし）

~~~diff
- 0086996c ["INT_ADD", "register:40f0:8", ["const:86996c:8", "const:4:8"]]
- 0086996c ["CALL", null, ["local:b0:8"]]
+ 008699ac ["INT_ADD", "register:40f0:8", ["const:8699ac:8", "const:4:8"]]
+ 008699ac ["CALL", null, ["local:b0:8"]]
- 0086996c bytes f7ffff97
+ 008699ac bytes f7ffff97
- 00869978 ["INT_ADD", "register:40f0:8", ["const:869978:8", "const:4:8"]]
- 00869978 ["CALL", null, ["local:b0:8"]]
+ 008699b8 ["INT_ADD", "register:40f0:8", ["const:8699b8:8", "const:4:8"]]
+ 008699b8 ["CALL", null, ["local:b0:8"]]
- 00869978 bytes f4ffff97
+ 008699b8 bytes f4ffff97
- 008699a0 ["INT_ADD", "register:40f0:8", ["const:8699a0:8", "const:4:8"]]
- 008699a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008699e0 ["INT_ADD", "register:40f0:8", ["const:8699e0:8", "const:4:8"]]
+ 008699e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 008699a0 bytes 44b80f94
+ 008699e0 bytes 34b90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6967404575f3fb5a21e142e8fe12e521"></a>

### [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) → [`00869b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md) FUN_00869b3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848210.md) [`008bac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac48.md) [`008bb4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4f8.md) [`008bba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bba1c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848250.md) [`008bac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bac8c.md) [`008bb53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb53c.md) [`008bba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bba60.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md#insn-00869b40) · [`00869b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md#insn-00869b70) · [`00869ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md#insn-00869ba0)
- 新版 `00869b80`（命令位置の公開資料なし） · `00869bb0`（命令位置の公開資料なし） · `00869be0`（命令位置の公開資料なし）

~~~diff
- 00869b40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869b40 ["INT_ADD", "register:40f0:8", ["const:869b40:8", "const:4:8"]]
- 00869b40 ["CALLIND", null, ["register:0:8"]]
+ 00869b80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869b80 ["INT_ADD", "register:40f0:8", ["const:869b80:8", "const:4:8"]]
+ 00869b80 ["CALLIND", null, ["register:0:8"]]
- 00869b40 bytes 00013fd6
+ 00869b80 bytes 00013fd6
- 00869b70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869b70 ["INT_ADD", "register:40f0:8", ["const:869b70:8", "const:4:8"]]
- 00869b70 ["CALLIND", null, ["register:0:8"]]
+ 00869bb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869bb0 ["INT_ADD", "register:40f0:8", ["const:869bb0:8", "const:4:8"]]
+ 00869bb0 ["CALLIND", null, ["register:0:8"]]
- 00869b70 bytes 00013fd6
+ 00869bb0 bytes 00013fd6
- 00869ba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869ba0 ["INT_ADD", "register:40f0:8", ["const:869ba0:8", "const:4:8"]]
- 00869ba0 ["CALLIND", null, ["register:0:8"]]
+ 00869be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869be0 ["INT_ADD", "register:40f0:8", ["const:869be0:8", "const:4:8"]]
+ 00869be0 ["CALLIND", null, ["register:0:8"]]
- 00869ba0 bytes 00013fd6
+ 00869be0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c1ca22240de3d9b53cf88a0b2f17bb"></a>

### [`00869c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869c64.md) → [`00869ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ca4.md) FUN_00869ca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869c64.md#insn-00869ca8) · [`00869cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869c64.md#insn-00869cb0) · [`00869cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869c64.md#insn-00869cf8)
- 新版 `00869ce8`（命令位置の公開資料なし） · `00869cf0`（命令位置の公開資料なし） · `00869d38`（命令位置の公開資料なし）

~~~diff
- 00869ca8 ["INT_ADD", "register:40f0:8", ["const:869ca8:8", "const:4:8"]]
- 00869ca8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869ce8 ["INT_ADD", "register:40f0:8", ["const:869ce8:8", "const:4:8"]]
+ 00869ce8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869ca8 bytes 82b70f94
+ 00869ce8 bytes 72b80f94
- 00869cb0 ["INT_ADD", "register:40f0:8", ["const:869cb0:8", "const:4:8"]]
- 00869cb0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869cf0 ["INT_ADD", "register:40f0:8", ["const:869cf0:8", "const:4:8"]]
+ 00869cf0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869cb0 bytes 80b70f94
+ 00869cf0 bytes 70b80f94
- 00869cf8 ["INT_ADD", "register:40f0:8", ["const:869cf8:8", "const:4:8"]]
- 00869cf8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869d38 ["INT_ADD", "register:40f0:8", ["const:869d38:8", "const:4:8"]]
+ 00869d38 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869cf8 bytes 6eb70f94
+ 00869d38 bytes 5eb80f94
~~~


<a id="compare-07cb694d00c8ea7c7f34547324a01c1c"></a>

### [`00869d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md) → [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) FUN_00869d7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008484b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484b8.md) [`00869d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md) · 呼出先 2件 [`00869d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008484f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008484f8.md) [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) · 呼出先 2件 [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md#insn-00869d5c) · [`00869d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md#insn-00869d68)
- 新版 `00869d9c`（命令位置の公開資料なし） · `00869da8`（命令位置の公開資料なし）

~~~diff
- 00869d5c ["INT_ADD", "register:40f0:8", ["const:869d5c:8", "const:4:8"]]
- 00869d5c ["CALL", null, ["local:b0:8"]]
+ 00869d9c ["INT_ADD", "register:40f0:8", ["const:869d9c:8", "const:4:8"]]
+ 00869d9c ["CALL", null, ["local:b0:8"]]
- 00869d5c bytes f8ffff97
+ 00869d9c bytes f8ffff97
- 00869d68 ["INT_ADD", "register:40f0:8", ["const:869d68:8", "const:4:8"]]
- 00869d68 ["CALL", null, ["local:b0:8"]]
+ 00869da8 ["INT_ADD", "register:40f0:8", ["const:869da8:8", "const:4:8"]]
+ 00869da8 ["CALL", null, ["local:b0:8"]]
- 00869d68 bytes f5ffff97
+ 00869da8 bytes f5ffff97
~~~


<a id="compare-1e090ac7e33dbf70fb060e68d0a42fa1"></a>

### [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) → [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) FUN_00869dc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) · 呼出先 3件 [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) [`00869dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) · 呼出先 3件 [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md#insn-00869da0) · [`00869dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md#insn-00869dac) · [`00869db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md#insn-00869db8)
- 新版 `00869de0`（命令位置の公開資料なし） · `00869dec`（命令位置の公開資料なし） · `00869df8`（命令位置の公開資料なし）

~~~diff
- 00869da0 ["INT_ADD", "register:40f0:8", ["const:869da0:8", "const:4:8"]]
- 00869da0 ["CALL", null, ["local:b0:8"]]
+ 00869de0 ["INT_ADD", "register:40f0:8", ["const:869de0:8", "const:4:8"]]
+ 00869de0 ["CALL", null, ["local:b0:8"]]
- 00869da0 bytes f8ffff97
+ 00869de0 bytes f8ffff97
- 00869dac ["INT_ADD", "register:40f0:8", ["const:869dac:8", "const:4:8"]]
- 00869dac ["CALL", null, ["local:b0:8"]]
+ 00869dec ["INT_ADD", "register:40f0:8", ["const:869dec:8", "const:4:8"]]
+ 00869dec ["CALL", null, ["local:b0:8"]]
- 00869dac bytes f5ffff97
+ 00869dec bytes f5ffff97
- 00869db8 ["INT_ADD", "register:40f0:8", ["const:869db8:8", "const:4:8"]]
- 00869db8 ["CALL", null, ["callee:00869e10:8"]]
+ 00869df8 ["INT_ADD", "register:40f0:8", ["const:869df8:8", "const:4:8"]]
+ 00869df8 ["CALL", null, ["callee:00869e10:8"]]
- 00869db8 bytes 06000094
+ 00869df8 bytes 06000094
~~~


<a id="compare-429ba10b021bda4e8022c6d80a39e10f"></a>

### [`00869dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md) → [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) FUN_00869e10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00869d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d80.md) [`00869dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md) · 呼出先 2件 [`00869dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) · 呼出先 2件 [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md#insn-00869df0) · [`00869dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869dd0.md#insn-00869dfc)
- 新版 `00869e30`（命令位置の公開資料なし） · `00869e3c`（命令位置の公開資料なし）

~~~diff
- 00869df0 ["INT_ADD", "register:40f0:8", ["const:869df0:8", "const:4:8"]]
- 00869df0 ["CALL", null, ["local:b0:8"]]
+ 00869e30 ["INT_ADD", "register:40f0:8", ["const:869e30:8", "const:4:8"]]
+ 00869e30 ["CALL", null, ["local:b0:8"]]
- 00869df0 bytes f8ffff97
+ 00869e30 bytes f8ffff97
- 00869dfc ["INT_ADD", "register:40f0:8", ["const:869dfc:8", "const:4:8"]]
- 00869dfc ["CALL", null, ["local:b0:8"]]
+ 00869e3c ["INT_ADD", "register:40f0:8", ["const:869e3c:8", "const:4:8"]]
+ 00869e3c ["CALL", null, ["local:b0:8"]]
- 00869dfc bytes f5ffff97
+ 00869e3c bytes f5ffff97
~~~


<a id="compare-81ed8fcb86798848e8ed61a647705ad2"></a>

### [`00869e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md) → [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) FUN_00869e54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md) [`00a2f434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md) · 呼出先 2件 [`00869e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) [`00a2f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f62c.md) · 呼出先 2件 [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md#insn-00869e30) · [`00869e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md#insn-00869e3c) · [`00869e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e14.md#insn-00869e4c)
- 新版 `00869e70`（命令位置の公開資料なし） · `00869e7c`（命令位置の公開資料なし） · `00869e8c`（命令位置の公開資料なし）

~~~diff
- 00869e30 ["INT_ADD", "register:40f0:8", ["const:869e30:8", "const:4:8"]]
- 00869e30 ["CALL", null, ["local:b0:8"]]
+ 00869e70 ["INT_ADD", "register:40f0:8", ["const:869e70:8", "const:4:8"]]
+ 00869e70 ["CALL", null, ["local:b0:8"]]
- 00869e30 bytes f9ffff97
+ 00869e70 bytes f9ffff97
- 00869e3c ["INT_ADD", "register:40f0:8", ["const:869e3c:8", "const:4:8"]]
- 00869e3c ["CALL", null, ["local:b0:8"]]
+ 00869e7c ["INT_ADD", "register:40f0:8", ["const:869e7c:8", "const:4:8"]]
+ 00869e7c ["CALL", null, ["local:b0:8"]]
- 00869e3c bytes f6ffff97
+ 00869e7c bytes f6ffff97
- 00869e4c ["INT_ADD", "register:40f0:8", ["const:869e4c:8", "const:4:8"]]
- 00869e4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869e8c ["INT_ADD", "register:40f0:8", ["const:869e8c:8", "const:4:8"]]
+ 00869e8c ["CALL", null, ["callee:00c57eb0:8"]]
- 00869e4c bytes 19b70f94
+ 00869e8c bytes 09b80f94
~~~


<a id="compare-50df4f59ce8d17b5d0637f753920a16e"></a>

### [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) → [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) FUN_00869ea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) [`00a62d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md) · 呼出先 3件 [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00869e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) [`00a62f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62f4c.md) · 呼出先 3件 [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md#insn-00869e84) · [`00869e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md#insn-00869e90) · [`00869e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869e64.md#insn-00869e9c)
- 新版 `00869ec4`（命令位置の公開資料なし） · `00869ed0`（命令位置の公開資料なし） · `00869edc`（命令位置の公開資料なし）

~~~diff
- 00869e84 ["INT_ADD", "register:40f0:8", ["const:869e84:8", "const:4:8"]]
- 00869e84 ["CALL", null, ["local:b0:8"]]
+ 00869ec4 ["INT_ADD", "register:40f0:8", ["const:869ec4:8", "const:4:8"]]
+ 00869ec4 ["CALL", null, ["local:b0:8"]]
- 00869e84 bytes f8ffff97
+ 00869ec4 bytes f8ffff97
- 00869e90 ["INT_ADD", "register:40f0:8", ["const:869e90:8", "const:4:8"]]
- 00869e90 ["CALL", null, ["local:b0:8"]]
+ 00869ed0 ["INT_ADD", "register:40f0:8", ["const:869ed0:8", "const:4:8"]]
+ 00869ed0 ["CALL", null, ["local:b0:8"]]
- 00869e90 bytes f5ffff97
+ 00869ed0 bytes f5ffff97
- 00869e9c ["INT_ADD", "register:40f0:8", ["const:869e9c:8", "const:4:8"]]
- 00869e9c ["CALL", null, ["callee:005c17e0:8"]]
+ 00869edc ["INT_ADD", "register:40f0:8", ["const:869edc:8", "const:4:8"]]
+ 00869edc ["CALL", null, ["callee:005c17e0:8"]]
- 00869e9c bytes 415ef597
+ 00869edc bytes 415ef597
~~~


<a id="compare-f8e2bb7abd2861c122fa37d23bd2532d"></a>

### [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) → [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) FUN_00869ef4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848788.md) [`009aa480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa480.md) [`009ac264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac264.md) [`009aca94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009aca94.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 10件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008487c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008487c8.md) [`009aa61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa61c.md) [`009ac400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac400.md) [`009acc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009acc30.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md#insn-00869f38) · [`00869f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md#insn-00869f48) · [`00869f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md#insn-00869f58)
- 新版 `00869f78`（命令位置の公開資料なし） · `00869f88`（命令位置の公開資料なし） · `00869f98`（命令位置の公開資料なし）

~~~diff
- 00869f38 ["INT_ADD", "register:40f0:8", ["const:869f38:8", "const:4:8"]]
- 00869f38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869f78 ["INT_ADD", "register:40f0:8", ["const:869f78:8", "const:4:8"]]
+ 00869f78 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869f38 bytes deb60f94
+ 00869f78 bytes ceb70f94
- 00869f48 ["INT_ADD", "register:40f0:8", ["const:869f48:8", "const:4:8"]]
- 00869f48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869f88 ["INT_ADD", "register:40f0:8", ["const:869f88:8", "const:4:8"]]
+ 00869f88 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869f48 bytes dab60f94
+ 00869f88 bytes cab70f94
- 00869f58 ["INT_ADD", "register:40f0:8", ["const:869f58:8", "const:4:8"]]
- 00869f58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00869f98 ["INT_ADD", "register:40f0:8", ["const:869f98:8", "const:4:8"]]
+ 00869f98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00869f58 bytes d6b60f94
+ 00869f98 bytes c6b70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be1044dd4fba21f9bcc1c58eeb43a7fc"></a>

### [`00869f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md) → [`00869fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md) FUN_00869fb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008487d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) [`008e083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e083c.md) · 呼出先 3件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848818.md) [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) [`008e05f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e05f4.md) [`008e09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e09d8.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md#insn-00869f88) · [`00869f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md#insn-00869f94) · [`00869fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md#insn-00869fa0)
- 新版 `00869fc8`（命令位置の公開資料なし） · `00869fd4`（命令位置の公開資料なし） · `00869fe0`（命令位置の公開資料なし）

~~~diff
- 00869f88 ["INT_ADD", "register:40f0:8", ["const:869f88:8", "const:4:8"]]
- 00869f88 ["CALL", null, ["callee:00676a60:8"]]
+ 00869fc8 ["INT_ADD", "register:40f0:8", ["const:869fc8:8", "const:4:8"]]
+ 00869fc8 ["CALL", null, ["callee:00676a60:8"]]
- 00869f88 bytes a632f897
+ 00869fc8 bytes a632f897
- 00869f94 ["INT_ADD", "register:40f0:8", ["const:869f94:8", "const:4:8"]]
- 00869f94 ["CALL", null, ["callee:00676a60:8"]]
+ 00869fd4 ["INT_ADD", "register:40f0:8", ["const:869fd4:8", "const:4:8"]]
+ 00869fd4 ["CALL", null, ["callee:00676a60:8"]]
- 00869f94 bytes a332f897
+ 00869fd4 bytes a332f897
- 00869fa0 ["INT_ADD", "register:40f0:8", ["const:869fa0:8", "const:4:8"]]
- 00869fa0 ["CALL", null, ["callee:00676a60:8"]]
+ 00869fe0 ["INT_ADD", "register:40f0:8", ["const:869fe0:8", "const:4:8"]]
+ 00869fe0 ["CALL", null, ["callee:00676a60:8"]]
- 00869fa0 bytes a032f897
+ 00869fe0 bytes a032f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514cabfd763ff5e4658008c855e548f6"></a>

### [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) → [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) FUN_0086a064

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084889c.md) [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) · 呼出先 2件 [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008488dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008488dc.md) [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) · 呼出先 2件 [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md#insn-0086a040) · [`0086a04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md#insn-0086a04c) · [`0086a05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md#insn-0086a05c)
- 新版 `0086a080`（命令位置の公開資料なし） · `0086a08c`（命令位置の公開資料なし） · `0086a09c`（命令位置の公開資料なし）

~~~diff
- 0086a040 ["INT_ADD", "register:40f0:8", ["const:86a040:8", "const:4:8"]]
- 0086a040 ["CALL", null, ["local:b0:8"]]
+ 0086a080 ["INT_ADD", "register:40f0:8", ["const:86a080:8", "const:4:8"]]
+ 0086a080 ["CALL", null, ["local:b0:8"]]
- 0086a040 bytes f9ffff97
+ 0086a080 bytes f9ffff97
- 0086a04c ["INT_ADD", "register:40f0:8", ["const:86a04c:8", "const:4:8"]]
- 0086a04c ["CALL", null, ["local:b0:8"]]
+ 0086a08c ["INT_ADD", "register:40f0:8", ["const:86a08c:8", "const:4:8"]]
+ 0086a08c ["CALL", null, ["local:b0:8"]]
- 0086a04c bytes f6ffff97
+ 0086a08c bytes f6ffff97
- 0086a05c ["INT_ADD", "register:40f0:8", ["const:86a05c:8", "const:4:8"]]
- 0086a05c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a09c ["INT_ADD", "register:40f0:8", ["const:86a09c:8", "const:4:8"]]
+ 0086a09c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a05c bytes 95b60f94
+ 0086a09c bytes 85b70f94
~~~


<a id="compare-d0994e536044ccb09fac420362829713"></a>

### [`0086a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a074.md) → [`0086a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md) FUN_0086a0b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008489ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00848a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848a2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a074.md#insn-0086a0c4) · [`0086a0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a074.md#insn-0086a0d4) · [`0086a0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a074.md#insn-0086a0e8)
- 新版 `0086a104`（命令位置の公開資料なし） · `0086a114`（命令位置の公開資料なし） · `0086a128`（命令位置の公開資料なし）

~~~diff
- 0086a0c4 ["INT_ADD", "register:40f0:8", ["const:86a0c4:8", "const:4:8"]]
- 0086a0c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a104 ["INT_ADD", "register:40f0:8", ["const:86a104:8", "const:4:8"]]
+ 0086a104 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a0c4 bytes 7bb60f94
+ 0086a104 bytes 6bb70f94
- 0086a0d4 ["INT_ADD", "register:40f0:8", ["const:86a0d4:8", "const:4:8"]]
- 0086a0d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a114 ["INT_ADD", "register:40f0:8", ["const:86a114:8", "const:4:8"]]
+ 0086a114 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a0d4 bytes 77b60f94
+ 0086a114 bytes 67b70f94
- 0086a0e8 ["INT_ADD", "register:40f0:8", ["const:86a0e8:8", "const:4:8"]]
- 0086a0e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a128 ["INT_ADD", "register:40f0:8", ["const:86a128:8", "const:4:8"]]
+ 0086a128 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a0e8 bytes 72b60f94
+ 0086a128 bytes 62b70f94
~~~


<a id="compare-3658cc77286d59653542163dc9541891"></a>

### [`0086a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md) → [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) FUN_0086a164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ae0.md) [`0086a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md) [`008fc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc454.md) [`008fceb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fceb8.md) · 呼出先 2件 [`0086a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b20.md) [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) [`008fd054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd054.md) · 呼出先 2件 [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md#insn-0086a144) · [`0086a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md#insn-0086a150)
- 新版 `0086a184`（命令位置の公開資料なし） · `0086a190`（命令位置の公開資料なし）

~~~diff
- 0086a144 ["INT_ADD", "register:40f0:8", ["const:86a144:8", "const:4:8"]]
- 0086a144 ["CALL", null, ["local:b0:8"]]
+ 0086a184 ["INT_ADD", "register:40f0:8", ["const:86a184:8", "const:4:8"]]
+ 0086a184 ["CALL", null, ["local:b0:8"]]
- 0086a144 bytes f8ffff97
+ 0086a184 bytes f8ffff97
- 0086a150 ["INT_ADD", "register:40f0:8", ["const:86a150:8", "const:4:8"]]
- 0086a150 ["CALL", null, ["local:b0:8"]]
+ 0086a190 ["INT_ADD", "register:40f0:8", ["const:86a190:8", "const:4:8"]]
+ 0086a190 ["CALL", null, ["local:b0:8"]]
- 0086a150 bytes f5ffff97
+ 0086a190 bytes f5ffff97
~~~


<a id="compare-ee324e8d720d5ba121ee7ce2c74965e2"></a>

### [`0086a168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md) → [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) FUN_0086a1a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md) [`0086a168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md) [`00a3a8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a8d0.md) [`00a3b68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3b/00a3b68c.md) · 呼出先 2件 [`0086a168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b98.md) [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) [`00a3b884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b884.md) · 呼出先 2件 [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md#insn-0086a188) · [`0086a194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md#insn-0086a194)
- 新版 `0086a1c8`（命令位置の公開資料なし） · `0086a1d4`（命令位置の公開資料なし）

~~~diff
- 0086a188 ["INT_ADD", "register:40f0:8", ["const:86a188:8", "const:4:8"]]
- 0086a188 ["CALL", null, ["local:b0:8"]]
+ 0086a1c8 ["INT_ADD", "register:40f0:8", ["const:86a1c8:8", "const:4:8"]]
+ 0086a1c8 ["CALL", null, ["local:b0:8"]]
- 0086a188 bytes f8ffff97
+ 0086a1c8 bytes f8ffff97
- 0086a194 ["INT_ADD", "register:40f0:8", ["const:86a194:8", "const:4:8"]]
- 0086a194 ["CALL", null, ["local:b0:8"]]
+ 0086a1d4 ["INT_ADD", "register:40f0:8", ["const:86a1d4:8", "const:4:8"]]
+ 0086a1d4 ["CALL", null, ["local:b0:8"]]
- 0086a194 bytes f5ffff97
+ 0086a1d4 bytes f5ffff97
~~~


<a id="compare-3bc8aa9909070bc80e27f42001b7e3d0"></a>

### [`0086a1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md) → [`0086a1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md) FUN_0086a1ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00848be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md) [`00abd670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd670.md) [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00848c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848c20.md) [`00abd86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd86c.md) [`00abd8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd8ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md#insn-0086a1dc) · [`0086a1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md#insn-0086a1ec) · [`0086a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md#insn-0086a1fc)
- 新版 `0086a21c`（命令位置の公開資料なし） · `0086a22c`（命令位置の公開資料なし） · `0086a23c`（命令位置の公開資料なし）

~~~diff
- 0086a1dc ["INT_ADD", "register:40f0:8", ["const:86a1dc:8", "const:4:8"]]
- 0086a1dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a21c ["INT_ADD", "register:40f0:8", ["const:86a21c:8", "const:4:8"]]
+ 0086a21c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a1dc bytes 35b60f94
+ 0086a21c bytes 25b70f94
- 0086a1ec ["INT_ADD", "register:40f0:8", ["const:86a1ec:8", "const:4:8"]]
- 0086a1ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a22c ["INT_ADD", "register:40f0:8", ["const:86a22c:8", "const:4:8"]]
+ 0086a22c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a1ec bytes 31b60f94
+ 0086a22c bytes 21b70f94
- 0086a1fc ["INT_ADD", "register:40f0:8", ["const:86a1fc:8", "const:4:8"]]
- 0086a1fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a23c ["INT_ADD", "register:40f0:8", ["const:86a23c:8", "const:4:8"]]
+ 0086a23c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a1fc bytes 2db60f94
+ 0086a23c bytes 1db70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c3124bf148180d65e33d43d5201153"></a>

### [`0086a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md) → [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) FUN_0086a278

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md) [`0086a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md) [`0092817c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00928/0092817c.md) · 呼出先 2件 [`0086a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848cfc.md) [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) [`00928318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00928/00928318.md) · 呼出先 2件 [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md#insn-0086a254) · [`0086a260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md#insn-0086a260) · [`0086a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md#insn-0086a270)
- 新版 `0086a294`（命令位置の公開資料なし） · `0086a2a0`（命令位置の公開資料なし） · `0086a2b0`（命令位置の公開資料なし）

~~~diff
- 0086a254 ["INT_ADD", "register:40f0:8", ["const:86a254:8", "const:4:8"]]
- 0086a254 ["CALL", null, ["local:b0:8"]]
+ 0086a294 ["INT_ADD", "register:40f0:8", ["const:86a294:8", "const:4:8"]]
+ 0086a294 ["CALL", null, ["local:b0:8"]]
- 0086a254 bytes f9ffff97
+ 0086a294 bytes f9ffff97
- 0086a260 ["INT_ADD", "register:40f0:8", ["const:86a260:8", "const:4:8"]]
- 0086a260 ["CALL", null, ["local:b0:8"]]
+ 0086a2a0 ["INT_ADD", "register:40f0:8", ["const:86a2a0:8", "const:4:8"]]
+ 0086a2a0 ["CALL", null, ["local:b0:8"]]
- 0086a260 bytes f6ffff97
+ 0086a2a0 bytes f6ffff97
- 0086a270 ["INT_ADD", "register:40f0:8", ["const:86a270:8", "const:4:8"]]
- 0086a270 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a2b0 ["INT_ADD", "register:40f0:8", ["const:86a2b0:8", "const:4:8"]]
+ 0086a2b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a270 bytes 10b60f94
+ 0086a2b0 bytes 00b70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5256c3d461216c9d7aacd3564bfac53c"></a>

### [`0086a298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a298.md) → [`0086a2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md) FUN_0086a2d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00848f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00848f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848f94.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a298.md#insn-0086a2e8) · [`0086a2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a298.md#insn-0086a2f8) · [`0086a30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a298.md#insn-0086a30c)
- 新版 `0086a328`（命令位置の公開資料なし） · `0086a338`（命令位置の公開資料なし） · `0086a34c`（命令位置の公開資料なし）

~~~diff
- 0086a2e8 ["INT_ADD", "register:40f0:8", ["const:86a2e8:8", "const:4:8"]]
- 0086a2e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a328 ["INT_ADD", "register:40f0:8", ["const:86a328:8", "const:4:8"]]
+ 0086a328 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a2e8 bytes f2b50f94
+ 0086a328 bytes e2b60f94
- 0086a2f8 ["INT_ADD", "register:40f0:8", ["const:86a2f8:8", "const:4:8"]]
- 0086a2f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a338 ["INT_ADD", "register:40f0:8", ["const:86a338:8", "const:4:8"]]
+ 0086a338 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a2f8 bytes eeb50f94
+ 0086a338 bytes deb60f94
- 0086a30c ["INT_ADD", "register:40f0:8", ["const:86a30c:8", "const:4:8"]]
- 0086a30c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a34c ["INT_ADD", "register:40f0:8", ["const:86a34c:8", "const:4:8"]]
+ 0086a34c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a30c bytes e9b50f94
+ 0086a34c bytes d9b60f94
~~~


<a id="compare-fa76a74ca829b0bbf4a6919982242299"></a>

### [`0086a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md) → [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) FUN_0086a388

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849294.md) [`0086a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md) [`00aa23ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa23ec.md) · 呼出先 2件 [`0086a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`00aa25e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa25e8.md) · 呼出先 2件 [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md#insn-0086a364) · [`0086a370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md#insn-0086a370) · [`0086a38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md#insn-0086a38c)
- 新版 `0086a3a4`（命令位置の公開資料なし） · `0086a3b0`（命令位置の公開資料なし） · `0086a3cc`（命令位置の公開資料なし）

~~~diff
- 0086a364 ["INT_ADD", "register:40f0:8", ["const:86a364:8", "const:4:8"]]
- 0086a364 ["CALL", null, ["local:b0:8"]]
+ 0086a3a4 ["INT_ADD", "register:40f0:8", ["const:86a3a4:8", "const:4:8"]]
+ 0086a3a4 ["CALL", null, ["local:b0:8"]]
- 0086a364 bytes f9ffff97
+ 0086a3a4 bytes f9ffff97
- 0086a370 ["INT_ADD", "register:40f0:8", ["const:86a370:8", "const:4:8"]]
- 0086a370 ["CALL", null, ["local:b0:8"]]
+ 0086a3b0 ["INT_ADD", "register:40f0:8", ["const:86a3b0:8", "const:4:8"]]
+ 0086a3b0 ["CALL", null, ["local:b0:8"]]
- 0086a370 bytes f6ffff97
+ 0086a3b0 bytes f6ffff97
- 0086a38c ["INT_ADD", "register:40f0:8", ["const:86a38c:8", "const:4:8"]]
- 0086a38c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a3cc ["INT_ADD", "register:40f0:8", ["const:86a3cc:8", "const:4:8"]]
+ 0086a3cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a38c bytes c9b50f94
+ 0086a3cc bytes b9b60f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-790b8fb0b13a4a54d30f06a03f8bcb96"></a>

### [`0086a3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md) → [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) FUN_0086a3ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008492c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492c4.md) [`0086a3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md) [`00b075a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md) · 呼出先 2件 [`0086a3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849304.md) [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) · 呼出先 2件 [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md#insn-0086a3c8) · [`0086a3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md#insn-0086a3d4) · [`0086a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md#insn-0086a3f0)
- 新版 `0086a408`（命令位置の公開資料なし） · `0086a414`（命令位置の公開資料なし） · `0086a430`（命令位置の公開資料なし）

~~~diff
- 0086a3c8 ["INT_ADD", "register:40f0:8", ["const:86a3c8:8", "const:4:8"]]
- 0086a3c8 ["CALL", null, ["local:b0:8"]]
+ 0086a408 ["INT_ADD", "register:40f0:8", ["const:86a408:8", "const:4:8"]]
+ 0086a408 ["CALL", null, ["local:b0:8"]]
- 0086a3c8 bytes f9ffff97
+ 0086a408 bytes f9ffff97
- 0086a3d4 ["INT_ADD", "register:40f0:8", ["const:86a3d4:8", "const:4:8"]]
- 0086a3d4 ["CALL", null, ["local:b0:8"]]
+ 0086a414 ["INT_ADD", "register:40f0:8", ["const:86a414:8", "const:4:8"]]
+ 0086a414 ["CALL", null, ["local:b0:8"]]
- 0086a3d4 bytes f6ffff97
+ 0086a414 bytes f6ffff97
- 0086a3f0 ["INT_ADD", "register:40f0:8", ["const:86a3f0:8", "const:4:8"]]
- 0086a3f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a430 ["INT_ADD", "register:40f0:8", ["const:86a430:8", "const:4:8"]]
+ 0086a430 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a3f0 bytes b0b50f94
+ 0086a430 bytes a0b60f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d3a1ee9182de61a8fe6b0a43aab804c"></a>

### [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) → [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) FUN_0086a460

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008493c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md) [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) [`009812a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md) · 呼出先 2件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 8件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) · 呼出先 2件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md#insn-0086a43c) · [`0086a448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md#insn-0086a448) · [`0086a458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md#insn-0086a458)
- 新版 `0086a47c`（命令位置の公開資料なし） · `0086a488`（命令位置の公開資料なし） · `0086a498`（命令位置の公開資料なし）

~~~diff
- 0086a43c ["INT_ADD", "register:40f0:8", ["const:86a43c:8", "const:4:8"]]
- 0086a43c ["CALL", null, ["local:b0:8"]]
+ 0086a47c ["INT_ADD", "register:40f0:8", ["const:86a47c:8", "const:4:8"]]
+ 0086a47c ["CALL", null, ["local:b0:8"]]
- 0086a43c bytes f9ffff97
+ 0086a47c bytes f9ffff97
- 0086a448 ["INT_ADD", "register:40f0:8", ["const:86a448:8", "const:4:8"]]
- 0086a448 ["CALL", null, ["local:b0:8"]]
+ 0086a488 ["INT_ADD", "register:40f0:8", ["const:86a488:8", "const:4:8"]]
+ 0086a488 ["CALL", null, ["local:b0:8"]]
- 0086a448 bytes f6ffff97
+ 0086a488 bytes f6ffff97
- 0086a458 ["INT_ADD", "register:40f0:8", ["const:86a458:8", "const:4:8"]]
- 0086a458 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a498 ["INT_ADD", "register:40f0:8", ["const:86a498:8", "const:4:8"]]
+ 0086a498 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a458 bytes 96b50f94
+ 0086a498 bytes 86b60f94
~~~


<a id="compare-58fbc2f8a675483738badc0a4200b78d"></a>

### [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) → [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) FUN_0086a4b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008493c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md) [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) [`00981530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md) · 呼出先 2件 [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`009816cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md) · 呼出先 2件 [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md#insn-0086a490) · [`0086a49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md#insn-0086a49c)
- 新版 `0086a4d0`（命令位置の公開資料なし） · `0086a4dc`（命令位置の公開資料なし）

~~~diff
- 0086a490 ["INT_ADD", "register:40f0:8", ["const:86a490:8", "const:4:8"]]
- 0086a490 ["CALL", null, ["local:b0:8"]]
+ 0086a4d0 ["INT_ADD", "register:40f0:8", ["const:86a4d0:8", "const:4:8"]]
+ 0086a4d0 ["CALL", null, ["local:b0:8"]]
- 0086a490 bytes f8ffff97
+ 0086a4d0 bytes f8ffff97
- 0086a49c ["INT_ADD", "register:40f0:8", ["const:86a49c:8", "const:4:8"]]
- 0086a49c ["CALL", null, ["local:b0:8"]]
+ 0086a4dc ["INT_ADD", "register:40f0:8", ["const:86a4dc:8", "const:4:8"]]
+ 0086a4dc ["CALL", null, ["local:b0:8"]]
- 0086a49c bytes f5ffff97
+ 0086a4dc bytes f5ffff97
~~~


<a id="compare-0c160cf472f409d764b38bbae0686fd3"></a>

### [`0086a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a4b4.md) → [`0086a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md) FUN_0086a4f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008493c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a4b4.md#insn-0086a504) · [`0086a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a4b4.md#insn-0086a514) · [`0086a528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a4b4.md#insn-0086a528)
- 新版 `0086a544`（命令位置の公開資料なし） · `0086a554`（命令位置の公開資料なし） · `0086a568`（命令位置の公開資料なし）

~~~diff
- 0086a504 ["INT_ADD", "register:40f0:8", ["const:86a504:8", "const:4:8"]]
- 0086a504 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a544 ["INT_ADD", "register:40f0:8", ["const:86a544:8", "const:4:8"]]
+ 0086a544 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a504 bytes 6bb50f94
+ 0086a544 bytes 5bb60f94
- 0086a514 ["INT_ADD", "register:40f0:8", ["const:86a514:8", "const:4:8"]]
- 0086a514 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a554 ["INT_ADD", "register:40f0:8", ["const:86a554:8", "const:4:8"]]
+ 0086a554 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a514 bytes 67b50f94
+ 0086a554 bytes 57b60f94
- 0086a528 ["INT_ADD", "register:40f0:8", ["const:86a528:8", "const:4:8"]]
- 0086a528 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a568 ["INT_ADD", "register:40f0:8", ["const:86a568:8", "const:4:8"]]
+ 0086a568 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a528 bytes 62b50f94
+ 0086a568 bytes 52b60f94
~~~


<a id="compare-c7e14162ec1a744b930395f982edf29b"></a>

### [`0086a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md) → [`0086a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md) FUN_0086a5a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md#insn-0086a5b4) · [`0086a5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md#insn-0086a5c4) · [`0086a5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md#insn-0086a5d8)
- 新版 `0086a5f4`（命令位置の公開資料なし） · `0086a604`（命令位置の公開資料なし） · `0086a618`（命令位置の公開資料なし）

~~~diff
- 0086a5b4 ["INT_ADD", "register:40f0:8", ["const:86a5b4:8", "const:4:8"]]
- 0086a5b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a5f4 ["INT_ADD", "register:40f0:8", ["const:86a5f4:8", "const:4:8"]]
+ 0086a5f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a5b4 bytes 3fb50f94
+ 0086a5f4 bytes 2fb60f94
- 0086a5c4 ["INT_ADD", "register:40f0:8", ["const:86a5c4:8", "const:4:8"]]
- 0086a5c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a604 ["INT_ADD", "register:40f0:8", ["const:86a604:8", "const:4:8"]]
+ 0086a604 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a5c4 bytes 3bb50f94
+ 0086a604 bytes 2bb60f94
- 0086a5d8 ["INT_ADD", "register:40f0:8", ["const:86a5d8:8", "const:4:8"]]
- 0086a5d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a618 ["INT_ADD", "register:40f0:8", ["const:86a618:8", "const:4:8"]]
+ 0086a618 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a5d8 bytes 36b50f94
+ 0086a618 bytes 26b60f94
~~~


<a id="compare-95d637dbfbab47620d569979b2b225df"></a>

### [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) → [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) FUN_0086a654

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md) [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) · 呼出先 2件 [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md) [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) · 呼出先 2件 [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md#insn-0086a630) · [`0086a63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md#insn-0086a63c) · [`0086a64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md#insn-0086a64c)
- 新版 `0086a670`（命令位置の公開資料なし） · `0086a67c`（命令位置の公開資料なし） · `0086a68c`（命令位置の公開資料なし）

~~~diff
- 0086a630 ["INT_ADD", "register:40f0:8", ["const:86a630:8", "const:4:8"]]
- 0086a630 ["CALL", null, ["local:b0:8"]]
+ 0086a670 ["INT_ADD", "register:40f0:8", ["const:86a670:8", "const:4:8"]]
+ 0086a670 ["CALL", null, ["local:b0:8"]]
- 0086a630 bytes f9ffff97
+ 0086a670 bytes f9ffff97
- 0086a63c ["INT_ADD", "register:40f0:8", ["const:86a63c:8", "const:4:8"]]
- 0086a63c ["CALL", null, ["local:b0:8"]]
+ 0086a67c ["INT_ADD", "register:40f0:8", ["const:86a67c:8", "const:4:8"]]
+ 0086a67c ["CALL", null, ["local:b0:8"]]
- 0086a63c bytes f6ffff97
+ 0086a67c bytes f6ffff97
- 0086a64c ["INT_ADD", "register:40f0:8", ["const:86a64c:8", "const:4:8"]]
- 0086a64c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a68c ["INT_ADD", "register:40f0:8", ["const:86a68c:8", "const:4:8"]]
+ 0086a68c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a64c bytes 19b50f94
+ 0086a68c bytes 09b60f94
~~~


<a id="compare-f86765ac8dec551e9972b823c3d5142b"></a>

### [`0086a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md) → [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) FUN_0086a6a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md) [`00a30de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30de8.md) · 呼出先 3件 [`0086a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md) [`0086a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`00a30fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30fe0.md) · 呼出先 3件 [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md#insn-0086a680) · [`0086a68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md#insn-0086a68c) · [`0086a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md#insn-0086a698)
- 新版 `0086a6c0`（命令位置の公開資料なし） · `0086a6cc`（命令位置の公開資料なし） · `0086a6d8`（命令位置の公開資料なし）

~~~diff
- 0086a680 ["INT_ADD", "register:40f0:8", ["const:86a680:8", "const:4:8"]]
- 0086a680 ["CALL", null, ["local:b0:8"]]
+ 0086a6c0 ["INT_ADD", "register:40f0:8", ["const:86a6c0:8", "const:4:8"]]
+ 0086a6c0 ["CALL", null, ["local:b0:8"]]
- 0086a680 bytes f9ffff97
+ 0086a6c0 bytes f9ffff97
- 0086a68c ["INT_ADD", "register:40f0:8", ["const:86a68c:8", "const:4:8"]]
- 0086a68c ["CALL", null, ["local:b0:8"]]
+ 0086a6cc ["INT_ADD", "register:40f0:8", ["const:86a6cc:8", "const:4:8"]]
+ 0086a6cc ["CALL", null, ["local:b0:8"]]
- 0086a68c bytes f6ffff97
+ 0086a6cc bytes f6ffff97
- 0086a698 ["INT_ADD", "register:40f0:8", ["const:86a698:8", "const:4:8"]]
- 0086a698 ["CALL", null, ["callee:0086a710:8"]]
+ 0086a6d8 ["INT_ADD", "register:40f0:8", ["const:86a6d8:8", "const:4:8"]]
+ 0086a6d8 ["CALL", null, ["callee:0086a710:8"]]
- 0086a698 bytes 0e000094
+ 0086a6d8 bytes 0e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc513c6600cc5547fcc0eaae3a68c291"></a>

### [`0086a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md) → [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) FUN_0086a710

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a664.md) [`0086a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md) · 呼出先 2件 [`0086a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) · 呼出先 2件 [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md#insn-0086a6ec) · [`0086a6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md#insn-0086a6f8) · [`0086a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a6d0.md#insn-0086a708)
- 新版 `0086a72c`（命令位置の公開資料なし） · `0086a738`（命令位置の公開資料なし） · `0086a748`（命令位置の公開資料なし）

~~~diff
- 0086a6ec ["INT_ADD", "register:40f0:8", ["const:86a6ec:8", "const:4:8"]]
- 0086a6ec ["CALL", null, ["local:b0:8"]]
+ 0086a72c ["INT_ADD", "register:40f0:8", ["const:86a72c:8", "const:4:8"]]
+ 0086a72c ["CALL", null, ["local:b0:8"]]
- 0086a6ec bytes f9ffff97
+ 0086a72c bytes f9ffff97
- 0086a6f8 ["INT_ADD", "register:40f0:8", ["const:86a6f8:8", "const:4:8"]]
- 0086a6f8 ["CALL", null, ["local:b0:8"]]
+ 0086a738 ["INT_ADD", "register:40f0:8", ["const:86a738:8", "const:4:8"]]
+ 0086a738 ["CALL", null, ["local:b0:8"]]
- 0086a6f8 bytes f6ffff97
+ 0086a738 bytes f6ffff97
- 0086a708 ["INT_ADD", "register:40f0:8", ["const:86a708:8", "const:4:8"]]
- 0086a708 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a748 ["INT_ADD", "register:40f0:8", ["const:86a748:8", "const:4:8"]]
+ 0086a748 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a708 bytes eab40f94
+ 0086a748 bytes dab50f94
~~~


<a id="compare-5cf80c6160f2c8f98d8a26d147fead7c"></a>

### [`0086a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md) → [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) FUN_0086a760

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md) [`0086a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md) · 呼出先 2件 [`0086a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md) [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) · 呼出先 2件 [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md#insn-0086a740) · [`0086a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md#insn-0086a74c)
- 新版 `0086a780`（命令位置の公開資料なし） · `0086a78c`（命令位置の公開資料なし）

~~~diff
- 0086a740 ["INT_ADD", "register:40f0:8", ["const:86a740:8", "const:4:8"]]
- 0086a740 ["CALL", null, ["local:b0:8"]]
+ 0086a780 ["INT_ADD", "register:40f0:8", ["const:86a780:8", "const:4:8"]]
+ 0086a780 ["CALL", null, ["local:b0:8"]]
- 0086a740 bytes f8ffff97
+ 0086a780 bytes f8ffff97
- 0086a74c ["INT_ADD", "register:40f0:8", ["const:86a74c:8", "const:4:8"]]
- 0086a74c ["CALL", null, ["local:b0:8"]]
+ 0086a78c ["INT_ADD", "register:40f0:8", ["const:86a78c:8", "const:4:8"]]
+ 0086a78c ["CALL", null, ["local:b0:8"]]
- 0086a74c bytes f5ffff97
+ 0086a78c bytes f5ffff97
~~~


<a id="compare-de5f5cfc163626d1f4e22ff3d0bd969b"></a>

### [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) → [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) FUN_0086a7a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a64.md) [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) [`00b091dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md) [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) · 呼出先 2件 [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 2件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md#insn-0086a784) · [`0086a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md#insn-0086a790) · [`0086a7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md#insn-0086a7cc)
- 新版 `0086a7c4`（命令位置の公開資料なし） · `0086a7d0`（命令位置の公開資料なし） · `0086a80c`（命令位置の公開資料なし）

~~~diff
- 0086a784 ["INT_ADD", "register:40f0:8", ["const:86a784:8", "const:4:8"]]
- 0086a784 ["CALL", null, ["local:b0:8"]]
+ 0086a7c4 ["INT_ADD", "register:40f0:8", ["const:86a7c4:8", "const:4:8"]]
+ 0086a7c4 ["CALL", null, ["local:b0:8"]]
- 0086a784 bytes f8ffff97
+ 0086a7c4 bytes f8ffff97
- 0086a790 ["INT_ADD", "register:40f0:8", ["const:86a790:8", "const:4:8"]]
- 0086a790 ["CALL", null, ["local:b0:8"]]
+ 0086a7d0 ["INT_ADD", "register:40f0:8", ["const:86a7d0:8", "const:4:8"]]
+ 0086a7d0 ["CALL", null, ["local:b0:8"]]
- 0086a790 bytes f5ffff97
+ 0086a7d0 bytes f5ffff97
- 0086a7cc ["INT_ADD", "register:40f0:8", ["const:86a7cc:8", "const:4:8"]]
- 0086a7cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a80c ["INT_ADD", "register:40f0:8", ["const:86a80c:8", "const:4:8"]]
+ 0086a80c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a7cc bytes b9b40f94
+ 0086a80c bytes a9b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d5cd662d725e412fde4817d50beba0c"></a>

### [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md) → [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) FUN_0086a838

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a64.md) [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md) [`00b091dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b091dc.md) [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) · 呼出先 2件 [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 2件 [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md#insn-0086a814) · [`0086a820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md#insn-0086a820) · [`0086a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md#insn-0086a830)
- 新版 `0086a854`（命令位置の公開資料なし） · `0086a860`（命令位置の公開資料なし） · `0086a870`（命令位置の公開資料なし）

~~~diff
- 0086a814 ["INT_ADD", "register:40f0:8", ["const:86a814:8", "const:4:8"]]
- 0086a814 ["CALL", null, ["local:b0:8"]]
+ 0086a854 ["INT_ADD", "register:40f0:8", ["const:86a854:8", "const:4:8"]]
+ 0086a854 ["CALL", null, ["local:b0:8"]]
- 0086a814 bytes f9ffff97
+ 0086a854 bytes f9ffff97
- 0086a820 ["INT_ADD", "register:40f0:8", ["const:86a820:8", "const:4:8"]]
- 0086a820 ["CALL", null, ["local:b0:8"]]
+ 0086a860 ["INT_ADD", "register:40f0:8", ["const:86a860:8", "const:4:8"]]
+ 0086a860 ["CALL", null, ["local:b0:8"]]
- 0086a820 bytes f6ffff97
+ 0086a860 bytes f6ffff97
- 0086a830 ["INT_ADD", "register:40f0:8", ["const:86a830:8", "const:4:8"]]
- 0086a830 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a870 ["INT_ADD", "register:40f0:8", ["const:86a870:8", "const:4:8"]]
+ 0086a870 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a830 bytes a0b40f94
+ 0086a870 bytes 90b50f94
~~~


<a id="compare-afbd27ed536555215ce18b960f80498f"></a>

### [`0086a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md) → [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) FUN_0086a888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) [`0086a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md) [`009c31b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c31b4.md) [`009c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7c20.md) · 呼出先 2件 [`0086a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`009c3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3350.md) [`009c7dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md) · 呼出先 2件 [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md#insn-0086a864) · [`0086a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md#insn-0086a870) · [`0086a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md#insn-0086a880)
- 新版 `0086a8a4`（命令位置の公開資料なし） · `0086a8b0`（命令位置の公開資料なし） · `0086a8c0`（命令位置の公開資料なし）

~~~diff
- 0086a864 ["INT_ADD", "register:40f0:8", ["const:86a864:8", "const:4:8"]]
- 0086a864 ["CALL", null, ["local:b0:8"]]
+ 0086a8a4 ["INT_ADD", "register:40f0:8", ["const:86a8a4:8", "const:4:8"]]
+ 0086a8a4 ["CALL", null, ["local:b0:8"]]
- 0086a864 bytes f9ffff97
+ 0086a8a4 bytes f9ffff97
- 0086a870 ["INT_ADD", "register:40f0:8", ["const:86a870:8", "const:4:8"]]
- 0086a870 ["CALL", null, ["local:b0:8"]]
+ 0086a8b0 ["INT_ADD", "register:40f0:8", ["const:86a8b0:8", "const:4:8"]]
+ 0086a8b0 ["CALL", null, ["local:b0:8"]]
- 0086a870 bytes f6ffff97
+ 0086a8b0 bytes f6ffff97
- 0086a880 ["INT_ADD", "register:40f0:8", ["const:86a880:8", "const:4:8"]]
- 0086a880 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a8c0 ["INT_ADD", "register:40f0:8", ["const:86a8c0:8", "const:4:8"]]
+ 0086a8c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a880 bytes 8cb40f94
+ 0086a8c0 bytes 7cb50f94
~~~


<a id="compare-e52c71a87ada29f0c35341df3d4ec1d1"></a>

### [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) → [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) FUN_0086a8d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) [`009c3240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c3240.md) · 呼出先 2件 [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`009c33dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c33dc.md) · 呼出先 2件 [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md#insn-0086a8b8) · [`0086a8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md#insn-0086a8c4)
- 新版 `0086a8f8`（命令位置の公開資料なし） · `0086a904`（命令位置の公開資料なし）

~~~diff
- 0086a8b8 ["INT_ADD", "register:40f0:8", ["const:86a8b8:8", "const:4:8"]]
- 0086a8b8 ["CALL", null, ["local:b0:8"]]
+ 0086a8f8 ["INT_ADD", "register:40f0:8", ["const:86a8f8:8", "const:4:8"]]
+ 0086a8f8 ["CALL", null, ["local:b0:8"]]
- 0086a8b8 bytes f8ffff97
+ 0086a8f8 bytes f8ffff97
- 0086a8c4 ["INT_ADD", "register:40f0:8", ["const:86a8c4:8", "const:4:8"]]
- 0086a8c4 ["CALL", null, ["local:b0:8"]]
+ 0086a904 ["INT_ADD", "register:40f0:8", ["const:86a904:8", "const:4:8"]]
+ 0086a904 ["CALL", null, ["local:b0:8"]]
- 0086a8c4 bytes f5ffff97
+ 0086a904 bytes f5ffff97
~~~


<a id="compare-bf212e2acc7fc107ccd6bce1658c2f7d"></a>

### [`0086a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md) → [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) FUN_0086a91c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b18.md) [`0086a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md) [`00936b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936b18.md) · 呼出先 3件 [`0086a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md) [`0086a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a928.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md) [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`00936cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/00936cb4.md) · 呼出先 3件 [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`0086a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md#insn-0086a8fc) · [`0086a908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md#insn-0086a908) · [`0086a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md#insn-0086a910)
- 新版 `0086a93c`（命令位置の公開資料なし） · `0086a948`（命令位置の公開資料なし） · `0086a950`（命令位置の公開資料なし）

~~~diff
- 0086a8fc ["INT_ADD", "register:40f0:8", ["const:86a8fc:8", "const:4:8"]]
- 0086a8fc ["CALL", null, ["local:b0:8"]]
+ 0086a93c ["INT_ADD", "register:40f0:8", ["const:86a93c:8", "const:4:8"]]
+ 0086a93c ["CALL", null, ["local:b0:8"]]
- 0086a8fc bytes f8ffff97
+ 0086a93c bytes f8ffff97
- 0086a908 ["INT_ADD", "register:40f0:8", ["const:86a908:8", "const:4:8"]]
- 0086a908 ["CALL", null, ["local:b0:8"]]
+ 0086a948 ["INT_ADD", "register:40f0:8", ["const:86a948:8", "const:4:8"]]
+ 0086a948 ["CALL", null, ["local:b0:8"]]
- 0086a908 bytes f5ffff97
+ 0086a948 bytes f5ffff97
- 0086a910 ["INT_ADD", "register:40f0:8", ["const:86a910:8", "const:4:8"]]
- 0086a910 ["CALL", null, ["callee:0086a968:8"]]
+ 0086a950 ["INT_ADD", "register:40f0:8", ["const:86a950:8", "const:4:8"]]
+ 0086a950 ["CALL", null, ["callee:0086a968:8"]]
- 0086a910 bytes 06000094
+ 0086a950 bytes 06000094
~~~


<a id="compare-2c0cef93ce9f9151070a5e340d50749e"></a>

### [`0086a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a928.md) → [`0086a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md) FUN_0086a968

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a928.md#insn-0086a95c) · [`0086a97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a928.md#insn-0086a97c) · [`0086a98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a928.md#insn-0086a98c)
- 新版 `0086a99c`（命令位置の公開資料なし） · `0086a9bc`（命令位置の公開資料なし） · `0086a9cc`（命令位置の公開資料なし）

~~~diff
- 0086a95c ["INT_ADD", "register:40f0:8", ["const:86a95c:8", "const:4:8"]]
- 0086a95c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a99c ["INT_ADD", "register:40f0:8", ["const:86a99c:8", "const:4:8"]]
+ 0086a99c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a95c bytes 55b40f94
+ 0086a99c bytes 45b50f94
- 0086a97c ["INT_ADD", "register:40f0:8", ["const:86a97c:8", "const:4:8"]]
- 0086a97c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a9bc ["INT_ADD", "register:40f0:8", ["const:86a9bc:8", "const:4:8"]]
+ 0086a9bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a97c bytes 4db40f94
+ 0086a9bc bytes 3db50f94
- 0086a98c ["INT_ADD", "register:40f0:8", ["const:86a98c:8", "const:4:8"]]
- 0086a98c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086a9cc ["INT_ADD", "register:40f0:8", ["const:86a9cc:8", "const:4:8"]]
+ 0086a9cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0086a98c bytes 49b40f94
+ 0086a9cc bytes 39b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41d4db768323655a72fb845b6b87db59"></a>

### [`0086a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md) → [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) FUN_0086a9f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b58.md) [`0086a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md) [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md) · 呼出先 2件 [`0086a9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md) [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) · 呼出先 2件 [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md#insn-0086a9d8) · [`0086a9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md#insn-0086a9e4) · [`0086aa1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a9b8.md#insn-0086aa1c)
- 新版 `0086aa18`（命令位置の公開資料なし） · `0086aa24`（命令位置の公開資料なし） · `0086aa5c`（命令位置の公開資料なし）

~~~diff
- 0086a9d8 ["INT_ADD", "register:40f0:8", ["const:86a9d8:8", "const:4:8"]]
- 0086a9d8 ["CALL", null, ["local:b0:8"]]
+ 0086aa18 ["INT_ADD", "register:40f0:8", ["const:86aa18:8", "const:4:8"]]
+ 0086aa18 ["CALL", null, ["local:b0:8"]]
- 0086a9d8 bytes f8ffff97
+ 0086aa18 bytes f8ffff97
- 0086a9e4 ["INT_ADD", "register:40f0:8", ["const:86a9e4:8", "const:4:8"]]
- 0086a9e4 ["CALL", null, ["local:b0:8"]]
+ 0086aa24 ["INT_ADD", "register:40f0:8", ["const:86aa24:8", "const:4:8"]]
+ 0086aa24 ["CALL", null, ["local:b0:8"]]
- 0086a9e4 bytes f5ffff97
+ 0086aa24 bytes f5ffff97
- 0086aa1c ["INT_ADD", "register:40f0:8", ["const:86aa1c:8", "const:4:8"]]
- 0086aa1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086aa5c ["INT_ADD", "register:40f0:8", ["const:86aa5c:8", "const:4:8"]]
+ 0086aa5c ["CALL", null, ["callee:00c57eb0:8"]]
- 0086aa1c bytes 25b40f94
+ 0086aa5c bytes 15b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5388aa56939e6eaf1cc6df66a0078c8"></a>

### [`0086aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa58.md) → [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) FUN_0086aa98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa58.md) [`00ab9d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9d20.md) · 呼出先 2件 [`0086aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa58.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) [`00ab9f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab9f1c.md) · 呼出先 2件 [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa58.md#insn-0086aa78) · [`0086aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa58.md#insn-0086aa84)
- 新版 `0086aab8`（命令位置の公開資料なし） · `0086aac4`（命令位置の公開資料なし）

~~~diff
- 0086aa78 ["INT_ADD", "register:40f0:8", ["const:86aa78:8", "const:4:8"]]
- 0086aa78 ["CALL", null, ["local:b0:8"]]
+ 0086aab8 ["INT_ADD", "register:40f0:8", ["const:86aab8:8", "const:4:8"]]
+ 0086aab8 ["CALL", null, ["local:b0:8"]]
- 0086aa78 bytes f8ffff97
+ 0086aab8 bytes f8ffff97
- 0086aa84 ["INT_ADD", "register:40f0:8", ["const:86aa84:8", "const:4:8"]]
- 0086aa84 ["CALL", null, ["local:b0:8"]]
+ 0086aac4 ["INT_ADD", "register:40f0:8", ["const:86aac4:8", "const:4:8"]]
+ 0086aac4 ["CALL", null, ["local:b0:8"]]
- 0086aa84 bytes f5ffff97
+ 0086aac4 bytes f5ffff97
~~~


<a id="compare-5ba76e62ba1cd8703b2a80316e51e596"></a>

### [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md) → [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) FUN_0086aadc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md) [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md) [`009e0038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0038.md) [`009e0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0bdc.md) · 呼出先 3件 [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md) [`0086aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`009e01d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md) [`009e0d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md) · 呼出先 3件 [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md#insn-0086aab8) · [`0086aac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md#insn-0086aac4) · [`0086aad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md#insn-0086aad4)
- 新版 `0086aaf8`（命令位置の公開資料なし） · `0086ab04`（命令位置の公開資料なし） · `0086ab14`（命令位置の公開資料なし）

~~~diff
- 0086aab8 ["INT_ADD", "register:40f0:8", ["const:86aab8:8", "const:4:8"]]
- 0086aab8 ["CALL", null, ["local:b0:8"]]
+ 0086aaf8 ["INT_ADD", "register:40f0:8", ["const:86aaf8:8", "const:4:8"]]
+ 0086aaf8 ["CALL", null, ["local:b0:8"]]
- 0086aab8 bytes f9ffff97
+ 0086aaf8 bytes f9ffff97
- 0086aac4 ["INT_ADD", "register:40f0:8", ["const:86aac4:8", "const:4:8"]]
- 0086aac4 ["CALL", null, ["local:b0:8"]]
+ 0086ab04 ["INT_ADD", "register:40f0:8", ["const:86ab04:8", "const:4:8"]]
+ 0086ab04 ["CALL", null, ["local:b0:8"]]
- 0086aac4 bytes f6ffff97
+ 0086ab04 bytes f6ffff97
- 0086aad4 ["INT_ADD", "register:40f0:8", ["const:86aad4:8", "const:4:8"]]
- 0086aad4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086ab14 ["INT_ADD", "register:40f0:8", ["const:86ab14:8", "const:4:8"]]
+ 0086ab14 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086aad4 bytes f7b30f94
+ 0086ab14 bytes e7b40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-219c7950dd6fe06fbace45be834c9b6d"></a>

### [`0086aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md) → [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) FUN_0086ab38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0086aa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aa9c.md) [`0086aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md) [`009dfc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc70.md) [`009e8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e8/009e8780.md) · 呼出先 3件 [`0086aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md) [`0086ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`009dfe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md) [`009e891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md) · 呼出先 3件 [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`0086abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ab14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md#insn-0086ab14) · [`0086ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md#insn-0086ab20) · [`0086ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md#insn-0086ab30)
- 新版 `0086ab54`（命令位置の公開資料なし） · `0086ab60`（命令位置の公開資料なし） · `0086ab70`（命令位置の公開資料なし）

~~~diff
- 0086ab14 ["INT_ADD", "register:40f0:8", ["const:86ab14:8", "const:4:8"]]
- 0086ab14 ["CALL", null, ["local:b0:8"]]
+ 0086ab54 ["INT_ADD", "register:40f0:8", ["const:86ab54:8", "const:4:8"]]
+ 0086ab54 ["CALL", null, ["local:b0:8"]]
- 0086ab14 bytes f9ffff97
+ 0086ab54 bytes f9ffff97
- 0086ab20 ["INT_ADD", "register:40f0:8", ["const:86ab20:8", "const:4:8"]]
- 0086ab20 ["CALL", null, ["local:b0:8"]]
+ 0086ab60 ["INT_ADD", "register:40f0:8", ["const:86ab60:8", "const:4:8"]]
+ 0086ab60 ["CALL", null, ["local:b0:8"]]
- 0086ab20 bytes f6ffff97
+ 0086ab60 bytes f6ffff97
- 0086ab30 ["INT_ADD", "register:40f0:8", ["const:86ab30:8", "const:4:8"]]
- 0086ab30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086ab70 ["INT_ADD", "register:40f0:8", ["const:86ab70:8", "const:4:8"]]
+ 0086ab70 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086ab30 bytes e0b30f94
+ 0086ab70 bytes d0b40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b5417b23bcaa5beea26fd74c921a10"></a>

### [`0086ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md) → [`0086abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md) FUN_0086abb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0086aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aaf8.md) [`009e10dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e1/009e10dc.md) [`009e21f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`009e238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ac14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md#insn-0086ac14) · [`0086ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md#insn-0086ac60) · [`0086acac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ab70.md#insn-0086acac)
- 新版 `0086ac54`（命令位置の公開資料なし） · `0086aca0`（命令位置の公開資料なし） · `0086acec`（命令位置の公開資料なし）

~~~diff
- 0086ac14 ["INT_ADD", "register:40f0:8", ["const:86ac14:8", "const:4:8"]]
- 0086ac14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086ac54 ["INT_ADD", "register:40f0:8", ["const:86ac54:8", "const:4:8"]]
+ 0086ac54 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086ac14 bytes a7b30f94
+ 0086ac54 bytes 97b40f94
- 0086ac60 ["INT_ADD", "register:40f0:8", ["const:86ac60:8", "const:4:8"]]
- 0086ac60 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086aca0 ["INT_ADD", "register:40f0:8", ["const:86aca0:8", "const:4:8"]]
+ 0086aca0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086ac60 bytes 94b30f94
+ 0086aca0 bytes 84b40f94
- 0086acac ["INT_ADD", "register:40f0:8", ["const:86acac:8", "const:4:8"]]
- 0086acac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086acec ["INT_ADD", "register:40f0:8", ["const:86acec:8", "const:4:8"]]
+ 0086acec ["CALL", null, ["callee:00c57eb0:8"]]
- 0086acac bytes 81b30f94
+ 0086acec bytes 71b40f94
~~~


<a id="compare-c1a82127561618812da3043d7e0e8dd3"></a>

### [`0086ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md) → [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) FUN_0086ad50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md) [`0086ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md) [`009e01e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e01e0.md) · 呼出先 2件 [`0086ad10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`009e037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md) · 呼出先 2件 [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md#insn-0086ad30) · [`0086ad3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md#insn-0086ad3c) · [`0086ad74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086ad10.md#insn-0086ad74)
- 新版 `0086ad70`（命令位置の公開資料なし） · `0086ad7c`（命令位置の公開資料なし） · `0086adb4`（命令位置の公開資料なし）

~~~diff
- 0086ad30 ["INT_ADD", "register:40f0:8", ["const:86ad30:8", "const:4:8"]]
- 0086ad30 ["CALL", null, ["local:b0:8"]]
+ 0086ad70 ["INT_ADD", "register:40f0:8", ["const:86ad70:8", "const:4:8"]]
+ 0086ad70 ["CALL", null, ["local:b0:8"]]
- 0086ad30 bytes f8ffff97
+ 0086ad70 bytes f8ffff97
- 0086ad3c ["INT_ADD", "register:40f0:8", ["const:86ad3c:8", "const:4:8"]]
- 0086ad3c ["CALL", null, ["local:b0:8"]]
+ 0086ad7c ["INT_ADD", "register:40f0:8", ["const:86ad7c:8", "const:4:8"]]
+ 0086ad7c ["CALL", null, ["local:b0:8"]]
- 0086ad3c bytes f5ffff97
+ 0086ad7c bytes f5ffff97
- 0086ad74 ["INT_ADD", "register:40f0:8", ["const:86ad74:8", "const:4:8"]]
- 0086ad74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0086adb4 ["INT_ADD", "register:40f0:8", ["const:86adb4:8", "const:4:8"]]
+ 0086adb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0086ad74 bytes 4fb30f94
+ 0086adb4 bytes 3fb40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117eb06f75d37fc0380cfbabb758f0d1"></a>

### [`0086aeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aeb4.md) → [`0086aef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aef4.md) FUN_0086aef4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086aeb4.md#insn-0086aed0)
- 新版 `0086af10`（命令位置の公開資料なし）

~~~diff
- 0086aed0 ["INT_ADD", "register:40f0:8", ["const:86aed0:8", "const:4:8"]]
- 0086aed0 ["CALL", null, ["callee:00c57e80:8"]]
+ 0086af10 ["INT_ADD", "register:40f0:8", ["const:86af10:8", "const:4:8"]]
+ 0086af10 ["CALL", null, ["callee:00c57e80:8"]]
- 0086aed0 bytes ecb20f94
+ 0086af10 bytes dcb30f94
~~~


<a id="compare-1ab81fe9cb36f46f28f884783f31707b"></a>

### [`0086b134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b134.md) → [`0086b174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b174.md) FUN_0086b174

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b134.md#insn-0086b150)
- 新版 `0086b190`（命令位置の公開資料なし）

~~~diff
- 0086b150 ["INT_ADD", "register:40f0:8", ["const:86b150:8", "const:4:8"]]
- 0086b150 ["CALL", null, ["callee:00c57e80:8"]]
+ 0086b190 ["INT_ADD", "register:40f0:8", ["const:86b190:8", "const:4:8"]]
+ 0086b190 ["CALL", null, ["callee:00c57e80:8"]]
- 0086b150 bytes 4cb20f94
+ 0086b190 bytes 3cb30f94
~~~


