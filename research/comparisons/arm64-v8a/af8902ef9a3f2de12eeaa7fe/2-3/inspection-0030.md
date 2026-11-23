# v16.0.0 → v16.0.1 · 要調査の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-3ac720b0365499350d0517845b112d45"></a>

### [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) → [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) FUN_0087ebbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0087e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e690.md) [`0087e69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e69c.md) [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) · 呼出先 4件 [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0087e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6d0.md) [`0087e6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6dc.md) [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) · 呼出先 4件 [`0087ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ebbc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087eb98) · [`0087eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087eba4) · [`0087ebb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087ebb8)
- 新版 `0087ebd8`（命令位置の公開資料なし） · `0087ebe4`（命令位置の公開資料なし） · `0087ebf8`（命令位置の公開資料なし）

~~~diff
- 0087eb98 ["INT_ADD", "register:40f0:8", ["const:87eb98:8", "const:4:8"]]
- 0087eb98 ["CALL", null, ["local:b0:8"]]
+ 0087ebd8 ["INT_ADD", "register:40f0:8", ["const:87ebd8:8", "const:4:8"]]
+ 0087ebd8 ["CALL", null, ["local:b0:8"]]
- 0087eb98 bytes f9ffff97
+ 0087ebd8 bytes f9ffff97
- 0087eba4 ["INT_ADD", "register:40f0:8", ["const:87eba4:8", "const:4:8"]]
- 0087eba4 ["CALL", null, ["local:b0:8"]]
+ 0087ebe4 ["INT_ADD", "register:40f0:8", ["const:87ebe4:8", "const:4:8"]]
+ 0087ebe4 ["CALL", null, ["local:b0:8"]]
- 0087eba4 bytes f6ffff97
+ 0087ebe4 bytes f6ffff97
- 0087ebb8 ["INT_ADD", "register:40f0:8", ["const:87ebb8:8", "const:4:8"]]
- 0087ebb8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0087ebf8 ["INT_ADD", "register:40f0:8", ["const:87ebf8:8", "const:4:8"]]
+ 0087ebf8 ["CALL", null, ["callee:00c53d00:8"]]
- 0087ebb8 bytes 4a530f94
+ 0087ebf8 bytes 42540f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a778a06142c0e0410720cecdea38152"></a>

### [`0087ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md) → [`0087ec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ec48.md) FUN_0087ec48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0087ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md) [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) [`0087eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eb20.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ec74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md#insn-0087ec74) · [`0087ecd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md#insn-0087ecd0)
- 新版 `0087ecb4`（命令位置の公開資料なし） · `0087ed10`（命令位置の公開資料なし）

~~~diff
- 0087ec74 ["INT_ADD", "register:40f0:8", ["const:87ec74:8", "const:4:8"]]
- 0087ec74 ["CALL", null, ["callee:00c58050:8"]]
+ 0087ecb4 ["INT_ADD", "register:40f0:8", ["const:87ecb4:8", "const:4:8"]]
+ 0087ecb4 ["CALL", null, ["callee:00c58050:8"]]
- 0087ec74 bytes f7630f94
+ 0087ecb4 bytes e7640f94
- 0087ecd0 ["INT_ADD", "register:40f0:8", ["const:87ecd0:8", "const:4:8"]]
- 0087ecd0 ["CALL", null, ["callee:00c58050:8"]]
+ 0087ed10 ["INT_ADD", "register:40f0:8", ["const:87ed10:8", "const:4:8"]]
+ 0087ed10 ["CALL", null, ["callee:00c58050:8"]]
- 0087ecd0 bytes e0630f94
+ 0087ed10 bytes d0640f94
~~~


<a id="compare-c892b5884fcacd17a272afde726a29e2"></a>

### [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) → [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) FUN_0087ed4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0087ee38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0087ee78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md#insn-0087ed40) · [`0087ed60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md#insn-0087ed60) · [`0087ed9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md#insn-0087ed9c)
- 新版 `0087ed80`（命令位置の公開資料なし） · `0087eda0`（命令位置の公開資料なし） · `0087eddc`（命令位置の公開資料なし）

~~~diff
- 0087ed40 ["INT_ADD", "register:40f0:8", ["const:87ed40:8", "const:4:8"]]
- 0087ed40 ["CALL", null, ["callee:0087ee78:8"]]
+ 0087ed80 ["INT_ADD", "register:40f0:8", ["const:87ed80:8", "const:4:8"]]
+ 0087ed80 ["CALL", null, ["callee:0087ee78:8"]]
- 0087ed40 bytes 3e000094
+ 0087ed80 bytes 3e000094
- 0087ed60 ["INT_ADD", "register:40f0:8", ["const:87ed60:8", "const:4:8"]]
- 0087ed60 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087eda0 ["INT_ADD", "register:40f0:8", ["const:87eda0:8", "const:4:8"]]
+ 0087eda0 ["CALL", null, ["callee:00c57e90:8"]]
- 0087ed60 bytes 4c630f94
+ 0087eda0 bytes 3c640f94
- 0087ed9c ["INT_ADD", "register:40f0:8", ["const:87ed9c:8", "const:4:8"]]
- 0087ed9c ["CALL", null, ["callee:0043bb20:8"]]
+ 0087eddc ["INT_ADD", "register:40f0:8", ["const:87eddc:8", "const:4:8"]]
+ 0087eddc ["CALL", null, ["callee:0043bb20:8"]]
- 0087ed9c bytes 51f3ee97
+ 0087eddc bytes 51f3ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff49843d447f1e5e54a3e96f643788cd"></a>

### [`0087ee38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md) → [`0087ee78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ee78.md) FUN_0087ee78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md#insn-0087eebc) · [`0087eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md#insn-0087eee8)
- 新版 `0087eefc`（命令位置の公開資料なし） · `0087ef28`（命令位置の公開資料なし）

~~~diff
- 0087eebc ["INT_ADD", "register:40f0:8", ["const:87eebc:8", "const:4:8"]]
- 0087eebc ["CALL", null, ["callee:00c58050:8"]]
+ 0087eefc ["INT_ADD", "register:40f0:8", ["const:87eefc:8", "const:4:8"]]
+ 0087eefc ["CALL", null, ["callee:00c58050:8"]]
- 0087eebc bytes 65630f94
+ 0087eefc bytes 55640f94
- 0087eee8 ["INT_ADD", "register:40f0:8", ["const:87eee8:8", "const:4:8"]]
- 0087eee8 ["CALL", null, ["callee:00c58050:8"]]
+ 0087ef28 ["INT_ADD", "register:40f0:8", ["const:87ef28:8", "const:4:8"]]
+ 0087ef28 ["CALL", null, ["callee:00c58050:8"]]
- 0087eee8 bytes 5a630f94
+ 0087ef28 bytes 4a640f94
~~~


<a id="compare-1f3a334210227036b67c933193f14476"></a>

### [`0087ef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ef3c.md) → [`0087ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ef7c.md) FUN_0087ef7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087ef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ef3c.md#insn-0087ef6c) · [`0087ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ef3c.md#insn-0087ef80) · [`0087ef88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ef3c.md#insn-0087ef88)
- 新版 `0087efac`（命令位置の公開資料なし） · `0087efc0`（命令位置の公開資料なし） · `0087efc8`（命令位置の公開資料なし）

~~~diff
- 0087ef6c ["INT_ADD", "register:40f0:8", ["const:87ef6c:8", "const:4:8"]]
- 0087ef6c ["CALL", null, ["callee:00c53d00:8"]]
+ 0087efac ["INT_ADD", "register:40f0:8", ["const:87efac:8", "const:4:8"]]
+ 0087efac ["CALL", null, ["callee:00c53d00:8"]]
- 0087ef6c bytes 5d520f94
+ 0087efac bytes 55530f94
- 0087ef80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087ef80 ["INT_ADD", "register:40f0:8", ["const:87ef80:8", "const:4:8"]]
- 0087ef80 ["CALLIND", null, ["register:0:8"]]
+ 0087efc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087efc0 ["INT_ADD", "register:40f0:8", ["const:87efc0:8", "const:4:8"]]
+ 0087efc0 ["CALLIND", null, ["register:0:8"]]
- 0087ef80 bytes 00013fd6
+ 0087efc0 bytes 00013fd6
- 0087ef88 ["INT_ADD", "register:40f0:8", ["const:87ef88:8", "const:4:8"]]
- 0087ef88 ["CALL", null, ["callee:00c57e80:8"]]
+ 0087efc8 ["INT_ADD", "register:40f0:8", ["const:87efc8:8", "const:4:8"]]
+ 0087efc8 ["CALL", null, ["callee:00c57e80:8"]]
- 0087ef88 bytes be620f94
+ 0087efc8 bytes ae630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-765724698609d7703089b4b0bb1b4c57"></a>

### [`0087eff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md) → [`0087f038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md) FUN_0087f038

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)
- 新版 呼出元 1件 [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087f014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md#insn-0087f014) · [`0087f02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md#insn-0087f02c) · [`0087f034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md#insn-0087f034)
- 新版 `0087f054`（命令位置の公開資料なし） · `0087f06c`（命令位置の公開資料なし） · `0087f074`（命令位置の公開資料なし）

~~~diff
- 0087f014 ["INT_ADD", "register:40f0:8", ["const:87f014:8", "const:4:8"]]
- 0087f014 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087f054 ["INT_ADD", "register:40f0:8", ["const:87f054:8", "const:4:8"]]
+ 0087f054 ["CALL", null, ["callee:00c57eb0:8"]]
- 0087f014 bytes a7620f94
+ 0087f054 bytes 97630f94
- 0087f02c ["INT_ADD", "register:40f0:8", ["const:87f02c:8", "const:4:8"]]
- 0087f02c ["CALL", null, ["callee:00c5a830:8"]]
+ 0087f06c ["INT_ADD", "register:40f0:8", ["const:87f06c:8", "const:4:8"]]
+ 0087f06c ["CALL", null, ["callee:00c5a830:8"]]
- 0087f02c bytes 016d0f94
+ 0087f06c bytes f16d0f94
- 0087f034 ["INT_ADD", "register:40f0:8", ["const:87f034:8", "const:4:8"]]
- 0087f034 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087f074 ["INT_ADD", "register:40f0:8", ["const:87f074:8", "const:4:8"]]
+ 0087f074 ["CALL", null, ["callee:00c57eb0:8"]]
- 0087f034 bytes 9f620f94
+ 0087f074 bytes 8f630f94
~~~


<a id="compare-4bb79ee775cbf7cfd3910d98e9058054"></a>

### [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) → [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) FUN_0087f0a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00bc85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md) · 呼出先 3件 [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)
- 新版 呼出元 2件 [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00bc89d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md) · 呼出先 3件 [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087f080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md#insn-0087f080) · [`0087f08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md#insn-0087f08c) · [`0087f098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md#insn-0087f098)
- 新版 `0087f0c0`（命令位置の公開資料なし） · `0087f0cc`（命令位置の公開資料なし） · `0087f0d8`（命令位置の公開資料なし）

~~~diff
- 0087f080 ["INT_ADD", "register:40f0:8", ["const:87f080:8", "const:4:8"]]
- 0087f080 ["CALL", null, ["local:b0:8"]]
+ 0087f0c0 ["INT_ADD", "register:40f0:8", ["const:87f0c0:8", "const:4:8"]]
+ 0087f0c0 ["CALL", null, ["local:b0:8"]]
- 0087f080 bytes f9ffff97
+ 0087f0c0 bytes f9ffff97
- 0087f08c ["INT_ADD", "register:40f0:8", ["const:87f08c:8", "const:4:8"]]
- 0087f08c ["CALL", null, ["local:b0:8"]]
+ 0087f0cc ["INT_ADD", "register:40f0:8", ["const:87f0cc:8", "const:4:8"]]
+ 0087f0cc ["CALL", null, ["local:b0:8"]]
- 0087f08c bytes f6ffff97
+ 0087f0cc bytes f6ffff97
- 0087f098 ["INT_ADD", "register:40f0:8", ["const:87f098:8", "const:4:8"]]
- 0087f098 ["CALL", null, ["callee:00c5a830:8"]]
+ 0087f0d8 ["INT_ADD", "register:40f0:8", ["const:87f0d8:8", "const:4:8"]]
+ 0087f0d8 ["CALL", null, ["callee:00c5a830:8"]]
- 0087f098 bytes e66c0f94
+ 0087f0d8 bytes d66d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea59f2132b49a029712cfa294413937a"></a>

### [`00880bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md) → [`00880bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880bec.md) FUN_00880bec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00880be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880be8) · [`00880bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880bfc) · [`00880c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880c1c)
- 新版 `00880c28`（命令位置の公開資料なし） · `00880c3c`（命令位置の公開資料なし） · `00880c5c`（命令位置の公開資料なし）

~~~diff
- 00880be8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880be8 ["INT_ADD", "register:40f0:8", ["const:880be8:8", "const:4:8"]]
- 00880be8 ["CALLIND", null, ["register:0:8"]]
+ 00880c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880c28 ["INT_ADD", "register:40f0:8", ["const:880c28:8", "const:4:8"]]
+ 00880c28 ["CALLIND", null, ["register:0:8"]]
- 00880be8 bytes 00013fd6
+ 00880c28 bytes 00013fd6
- 00880bfc ["INT_ADD", "register:40f0:8", ["const:880bfc:8", "const:4:8"]]
- 00880bfc ["CALL", null, ["callee:00c53d00:8"]]
+ 00880c3c ["INT_ADD", "register:40f0:8", ["const:880c3c:8", "const:4:8"]]
+ 00880c3c ["CALL", null, ["callee:00c53d00:8"]]
- 00880bfc bytes 394b0f94
+ 00880c3c bytes 314c0f94
- 00880c1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00880c1c ["INT_ADD", "register:40f0:8", ["const:880c1c:8", "const:4:8"]]
- 00880c1c ["CALLIND", null, ["register:0:8"]]
+ 00880c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880c5c ["INT_ADD", "register:40f0:8", ["const:880c5c:8", "const:4:8"]]
+ 00880c5c ["CALLIND", null, ["register:0:8"]]
- 00880c1c bytes 00013fd6
+ 00880c5c bytes 00013fd6
~~~


<a id="compare-19a0e3c668a99021eaa66fb3f8af6043"></a>

### [`00880c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880c30.md) → [`00880c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880c70.md) FUN_00880c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00880c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880c30.md#insn-00880c6c) · [`00880c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880c30.md#insn-00880c80) · [`00880ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880c30.md#insn-00880ca0)
- 新版 `00880cac`（命令位置の公開資料なし） · `00880cc0`（命令位置の公開資料なし） · `00880ce0`（命令位置の公開資料なし）

~~~diff
- 00880c6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00880c6c ["INT_ADD", "register:40f0:8", ["const:880c6c:8", "const:4:8"]]
- 00880c6c ["CALLIND", null, ["register:0:8"]]
+ 00880cac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880cac ["INT_ADD", "register:40f0:8", ["const:880cac:8", "const:4:8"]]
+ 00880cac ["CALLIND", null, ["register:0:8"]]
- 00880c6c bytes 00013fd6
+ 00880cac bytes 00013fd6
- 00880c80 ["INT_ADD", "register:40f0:8", ["const:880c80:8", "const:4:8"]]
- 00880c80 ["CALL", null, ["callee:00c53d00:8"]]
+ 00880cc0 ["INT_ADD", "register:40f0:8", ["const:880cc0:8", "const:4:8"]]
+ 00880cc0 ["CALL", null, ["callee:00c53d00:8"]]
- 00880c80 bytes 184b0f94
+ 00880cc0 bytes 104c0f94
- 00880ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00880ca0 ["INT_ADD", "register:40f0:8", ["const:880ca0:8", "const:4:8"]]
- 00880ca0 ["CALLIND", null, ["register:0:8"]]
+ 00880ce0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880ce0 ["INT_ADD", "register:40f0:8", ["const:880ce0:8", "const:4:8"]]
+ 00880ce0 ["CALLIND", null, ["register:0:8"]]
- 00880ca0 bytes 00013fd6
+ 00880ce0 bytes 00013fd6
~~~


<a id="compare-a29dad012b8a8227f6f26c7232deffca"></a>

### [`00880fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880fd4.md) → [`00881014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881014.md) FUN_00881014

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00880ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880fd4.md#insn-00880ff4) · [`00881008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880fd4.md#insn-00881008) · [`00881010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880fd4.md#insn-00881010)
- 新版 `00881034`（命令位置の公開資料なし） · `00881048`（命令位置の公開資料なし） · `00881050`（命令位置の公開資料なし）

~~~diff
- 00880ff4 ["INT_ADD", "register:40f0:8", ["const:880ff4:8", "const:4:8"]]
- 00880ff4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00881034 ["INT_ADD", "register:40f0:8", ["const:881034:8", "const:4:8"]]
+ 00881034 ["CALL", null, ["callee:00c53d00:8"]]
- 00880ff4 bytes 3b4a0f94
+ 00881034 bytes 334b0f94
- 00881008 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881008 ["INT_ADD", "register:40f0:8", ["const:881008:8", "const:4:8"]]
- 00881008 ["CALLIND", null, ["register:0:8"]]
+ 00881048 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00881048 ["INT_ADD", "register:40f0:8", ["const:881048:8", "const:4:8"]]
+ 00881048 ["CALLIND", null, ["register:0:8"]]
- 00881008 bytes 00013fd6
+ 00881048 bytes 00013fd6
- 00881010 ["INT_ADD", "register:40f0:8", ["const:881010:8", "const:4:8"]]
- 00881010 ["CALL", null, ["callee:00c57e80:8"]]
+ 00881050 ["INT_ADD", "register:40f0:8", ["const:881050:8", "const:4:8"]]
+ 00881050 ["CALL", null, ["callee:00c57e80:8"]]
- 00881010 bytes 9c5a0f94
+ 00881050 bytes 8c5b0f94
~~~


<a id="compare-6ea7ee784aaaf3b1b4cd1b592bea2384"></a>

### [`0088130c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/0088130c.md) → [`0088134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/0088134c.md) FUN_0088134c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/0088130c.md#insn-00881348)
- 新版 `00881388`（命令位置の公開資料なし）

~~~diff
- 00881348 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881348 ["INT_ADD", "register:40f0:8", ["const:881348:8", "const:4:8"]]
- 00881348 ["CALLIND", null, ["register:0:8"]]
+ 00881388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00881388 ["INT_ADD", "register:40f0:8", ["const:881388:8", "const:4:8"]]
+ 00881388 ["CALLIND", null, ["register:0:8"]]
- 00881348 bytes 00013fd6
+ 00881388 bytes 00013fd6
~~~


<a id="compare-c6eb0fd40b3f9f5ed6e5ca5849d7479a"></a>

### [`00881bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881bec.md) → [`00881c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c2c.md) FUN_00881c2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881bec.md#insn-00881c08) · [`00881c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881bec.md#insn-00881c28)
- 新版 `00881c48`（命令位置の公開資料なし） · `00881c68`（命令位置の公開資料なし）

~~~diff
- 00881c08 ["INT_ADD", "register:40f0:8", ["const:881c08:8", "const:4:8"]]
- 00881c08 ["CALL", null, ["callee:00c53d00:8"]]
+ 00881c48 ["INT_ADD", "register:40f0:8", ["const:881c48:8", "const:4:8"]]
+ 00881c48 ["CALL", null, ["callee:00c53d00:8"]]
- 00881c08 bytes 36470f94
+ 00881c48 bytes 2e480f94
- 00881c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881c28 ["INT_ADD", "register:40f0:8", ["const:881c28:8", "const:4:8"]]
- 00881c28 ["CALLIND", null, ["register:0:8"]]
+ 00881c68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00881c68 ["INT_ADD", "register:40f0:8", ["const:881c68:8", "const:4:8"]]
+ 00881c68 ["CALLIND", null, ["register:0:8"]]
- 00881c28 bytes 00013fd6
+ 00881c68 bytes 00013fd6
~~~


<a id="compare-8f3fad55835082a449cc2e4a5a60c8bc"></a>

### [`00881fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881fbc.md) → [`00881ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881ffc.md) FUN_00881ffc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00881fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881fbc.md#insn-00881fcc) · [`00881fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881fbc.md#insn-00881fe4)
- 新版 `0088200c`（命令位置の公開資料なし） · `00882024`（命令位置の公開資料なし）

~~~diff
- 00881fcc ["INT_ADD", "register:40f0:8", ["const:881fcc:8", "const:4:8"]]
- 00881fcc ["CALL", null, ["callee:008514f8:8"]]
+ 0088200c ["INT_ADD", "register:40f0:8", ["const:88200c:8", "const:4:8"]]
+ 0088200c ["CALL", null, ["callee:008514f8:8"]]
- 00881fcc bytes 3b3dff97
+ 0088200c bytes 3b3dff97
- 00881fe4 ["INT_ADD", "register:40f0:8", ["const:881fe4:8", "const:4:8"]]
- 00881fe4 ["CALL", null, ["callee:008514f8:8"]]
+ 00882024 ["INT_ADD", "register:40f0:8", ["const:882024:8", "const:4:8"]]
+ 00882024 ["CALL", null, ["callee:008514f8:8"]]
- 00881fe4 bytes 353dff97
+ 00882024 bytes 353dff97
~~~


<a id="compare-b5c18c784e9151139a97d628b6031060"></a>

### [`00882090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882090.md) → [`008820d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008820d0.md) FUN_008820d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`007697b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md) [`00769c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769c98.md) [`00769ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769ca4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`007697f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007697f4.md) [`00769cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769cd8.md) [`00769ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769ce4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008820a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882090.md#insn-008820a0) · [`008820b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882090.md#insn-008820b8) · [`008820bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882090.md#insn-008820bc)
- 新版 `008820e0`（命令位置の公開資料なし） · `008820f8`（命令位置の公開資料なし） · `008820fc`（命令位置の公開資料なし）

~~~diff
- 008820a0 ["INT_ADD", "register:40f0:8", ["const:8820a0:8", "const:4:8"]]
- 008820a0 ["CALL", null, ["callee:008514f8:8"]]
+ 008820e0 ["INT_ADD", "register:40f0:8", ["const:8820e0:8", "const:4:8"]]
+ 008820e0 ["CALL", null, ["callee:008514f8:8"]]
- 008820a0 bytes 063dff97
+ 008820e0 bytes 063dff97
- 008820b8 ["INT_ADD", "register:40f0:8", ["const:8820b8:8", "const:4:8"]]
- 008820b8 ["CALL", null, ["callee:008514f8:8"]]
+ 008820f8 ["INT_ADD", "register:40f0:8", ["const:8820f8:8", "const:4:8"]]
+ 008820f8 ["CALL", null, ["callee:008514f8:8"]]
- 008820b8 bytes 003dff97
+ 008820f8 bytes 003dff97
- 008820bc ["INT_ADD", "register:40f0:8", ["const:8820bc:8", "const:4:8"]]
- 008820bc ["CALL", null, ["callee:00769cd8:8"]]
+ 008820fc ["INT_ADD", "register:40f0:8", ["const:8820fc:8", "const:4:8"]]
+ 008820fc ["CALL", null, ["callee:00769cd8:8"]]
- 008820bc bytes f79efb97
+ 008820fc bytes f79efb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de215020d51c9ee95db94562a2b29996"></a>

### [`008820f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008820f4.md) → [`00882134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882134.md) FUN_00882134

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008820f4.md#insn-00882104)
- 新版 `00882144`（命令位置の公開資料なし）

~~~diff
- 00882104 ["INT_ADD", "register:40f0:8", ["const:882104:8", "const:4:8"]]
- 00882104 ["CALL", null, ["callee:008514f8:8"]]
+ 00882144 ["INT_ADD", "register:40f0:8", ["const:882144:8", "const:4:8"]]
+ 00882144 ["CALL", null, ["callee:008514f8:8"]]
- 00882104 bytes ed3cff97
+ 00882144 bytes ed3cff97
~~~


<a id="compare-1dc17c9fabce7bd6527c3c8c84264be5"></a>

### [`00882208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882208.md) → [`00882248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882248.md) FUN_00882248

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086d63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d63c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0086d67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d67c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882208.md#insn-00882218)
- 新版 `00882258`（命令位置の公開資料なし）

~~~diff
- 00882218 ["INT_ADD", "register:40f0:8", ["const:882218:8", "const:4:8"]]
- 00882218 ["CALL", null, ["callee:008514f8:8"]]
+ 00882258 ["INT_ADD", "register:40f0:8", ["const:882258:8", "const:4:8"]]
+ 00882258 ["CALL", null, ["callee:008514f8:8"]]
- 00882218 bytes a83cff97
+ 00882258 bytes a83cff97
~~~


<a id="compare-da42261d64db07c6717660f5bf58c543"></a>

### [`008825d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008825d4.md) → [`00882614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882614.md) FUN_00882614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0088018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008825d4.md#insn-00882610)
- 新版 `00882650`（命令位置の公開資料なし）

~~~diff
- 00882610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00882610 ["INT_ADD", "register:40f0:8", ["const:882610:8", "const:4:8"]]
- 00882610 ["CALLIND", null, ["register:0:8"]]
+ 00882650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00882650 ["INT_ADD", "register:40f0:8", ["const:882650:8", "const:4:8"]]
+ 00882650 ["CALLIND", null, ["register:0:8"]]
- 00882610 bytes 00013fd6
+ 00882650 bytes 00013fd6
~~~


<a id="compare-b92224ab8b199fd662ec517ae9bdbd0f"></a>

### [`00882d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d00.md) → [`00882d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882d40.md) FUN_00882d40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00882d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d00.md#insn-00882d20)
- 新版 `00882d60`（命令位置の公開資料なし）

~~~diff
- 00882d20 ["INT_ADD", "register:40f0:8", ["const:882d20:8", "const:4:8"]]
- 00882d20 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00882d60 ["INT_ADD", "register:40f0:8", ["const:882d60:8", "const:4:8"]]
+ 00882d60 ["CALL", null, ["callee:00c57eb0:8"]]
- 00882d20 bytes 64530f94
+ 00882d60 bytes 54540f94
~~~


<a id="compare-2a785bf7b2906b359b03f1b028c47ef9"></a>

### [`00883990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883990.md) → [`008839d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/008839d0.md) FUN_008839d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008839cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883990.md#insn-008839cc) · [`008839e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883990.md#insn-008839e0) · [`00883a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883990.md#insn-00883a00)
- 新版 `00883a0c`（命令位置の公開資料なし） · `00883a20`（命令位置の公開資料なし） · `00883a40`（命令位置の公開資料なし）

~~~diff
- 008839cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008839cc ["INT_ADD", "register:40f0:8", ["const:8839cc:8", "const:4:8"]]
- 008839cc ["CALLIND", null, ["register:0:8"]]
+ 00883a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a0c ["INT_ADD", "register:40f0:8", ["const:883a0c:8", "const:4:8"]]
+ 00883a0c ["CALLIND", null, ["register:0:8"]]
- 008839cc bytes 00013fd6
+ 00883a0c bytes 00013fd6
- 008839e0 ["INT_ADD", "register:40f0:8", ["const:8839e0:8", "const:4:8"]]
- 008839e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00883a20 ["INT_ADD", "register:40f0:8", ["const:883a20:8", "const:4:8"]]
+ 00883a20 ["CALL", null, ["callee:00c53d00:8"]]
- 008839e0 bytes c03f0f94
+ 00883a20 bytes b8400f94
- 00883a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a00 ["INT_ADD", "register:40f0:8", ["const:883a00:8", "const:4:8"]]
- 00883a00 ["CALLIND", null, ["register:0:8"]]
+ 00883a40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a40 ["INT_ADD", "register:40f0:8", ["const:883a40:8", "const:4:8"]]
+ 00883a40 ["CALLIND", null, ["register:0:8"]]
- 00883a00 bytes 00013fd6
+ 00883a40 bytes 00013fd6
~~~


<a id="compare-37c1cacf9eff856d297c73e26d21ce2e"></a>

### [`00883a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a14.md) → [`00883a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883a54.md) FUN_00883a54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00883a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a14.md#insn-00883a50) · [`00883a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a14.md#insn-00883a64) · [`00883a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a14.md#insn-00883a78)
- 新版 `00883a90`（命令位置の公開資料なし） · `00883aa4`（命令位置の公開資料なし） · `00883ab8`（命令位置の公開資料なし）

~~~diff
- 00883a50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a50 ["INT_ADD", "register:40f0:8", ["const:883a50:8", "const:4:8"]]
- 00883a50 ["CALLIND", null, ["register:0:8"]]
+ 00883a90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a90 ["INT_ADD", "register:40f0:8", ["const:883a90:8", "const:4:8"]]
+ 00883a90 ["CALLIND", null, ["register:0:8"]]
- 00883a50 bytes 00013fd6
+ 00883a90 bytes 00013fd6
- 00883a64 ["INT_ADD", "register:40f0:8", ["const:883a64:8", "const:4:8"]]
- 00883a64 ["CALL", null, ["callee:00c53d00:8"]]
+ 00883aa4 ["INT_ADD", "register:40f0:8", ["const:883aa4:8", "const:4:8"]]
+ 00883aa4 ["CALL", null, ["callee:00c53d00:8"]]
- 00883a64 bytes 9f3f0f94
+ 00883aa4 bytes 97400f94
- 00883a78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883a78 ["INT_ADD", "register:40f0:8", ["const:883a78:8", "const:4:8"]]
- 00883a78 ["CALLIND", null, ["register:0:8"]]
+ 00883ab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883ab8 ["INT_ADD", "register:40f0:8", ["const:883ab8:8", "const:4:8"]]
+ 00883ab8 ["CALLIND", null, ["register:0:8"]]
- 00883a78 bytes 00013fd6
+ 00883ab8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818d35a076aaab5d73ed5a8edda63df4"></a>

### [`00883f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md) → [`00883fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883fa4.md) FUN_00883fa4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00883fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883fa0) · [`00883fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883fb4) · [`00883fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883fd4)
- 新版 `00883fe0`（命令位置の公開資料なし） · `00883ff4`（命令位置の公開資料なし） · `00884014`（命令位置の公開資料なし）

~~~diff
- 00883fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883fa0 ["INT_ADD", "register:40f0:8", ["const:883fa0:8", "const:4:8"]]
- 00883fa0 ["CALLIND", null, ["register:0:8"]]
+ 00883fe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883fe0 ["INT_ADD", "register:40f0:8", ["const:883fe0:8", "const:4:8"]]
+ 00883fe0 ["CALLIND", null, ["register:0:8"]]
- 00883fa0 bytes 00013fd6
+ 00883fe0 bytes 00013fd6
- 00883fb4 ["INT_ADD", "register:40f0:8", ["const:883fb4:8", "const:4:8"]]
- 00883fb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00883ff4 ["INT_ADD", "register:40f0:8", ["const:883ff4:8", "const:4:8"]]
+ 00883ff4 ["CALL", null, ["callee:00c53d00:8"]]
- 00883fb4 bytes 4b3e0f94
+ 00883ff4 bytes 433f0f94
- 00883fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883fd4 ["INT_ADD", "register:40f0:8", ["const:883fd4:8", "const:4:8"]]
- 00883fd4 ["CALLIND", null, ["register:0:8"]]
+ 00884014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884014 ["INT_ADD", "register:40f0:8", ["const:884014:8", "const:4:8"]]
+ 00884014 ["CALLIND", null, ["register:0:8"]]
- 00883fd4 bytes 00013fd6
+ 00884014 bytes 00013fd6
~~~


<a id="compare-9894c0ca90b99ffba428f7020da0ae08"></a>

### [`00883fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883fe8.md) → [`00884028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884028.md) FUN_00884028

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883fe8.md#insn-00884024) · [`00884038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883fe8.md#insn-00884038) · [`00884058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883fe8.md#insn-00884058)
- 新版 `00884064`（命令位置の公開資料なし） · `00884078`（命令位置の公開資料なし） · `00884098`（命令位置の公開資料なし）

~~~diff
- 00884024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884024 ["INT_ADD", "register:40f0:8", ["const:884024:8", "const:4:8"]]
- 00884024 ["CALLIND", null, ["register:0:8"]]
+ 00884064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884064 ["INT_ADD", "register:40f0:8", ["const:884064:8", "const:4:8"]]
+ 00884064 ["CALLIND", null, ["register:0:8"]]
- 00884024 bytes 00013fd6
+ 00884064 bytes 00013fd6
- 00884038 ["INT_ADD", "register:40f0:8", ["const:884038:8", "const:4:8"]]
- 00884038 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884078 ["INT_ADD", "register:40f0:8", ["const:884078:8", "const:4:8"]]
+ 00884078 ["CALL", null, ["callee:00c53d00:8"]]
- 00884038 bytes 2a3e0f94
+ 00884078 bytes 223f0f94
- 00884058 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884058 ["INT_ADD", "register:40f0:8", ["const:884058:8", "const:4:8"]]
- 00884058 ["CALLIND", null, ["register:0:8"]]
+ 00884098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884098 ["INT_ADD", "register:40f0:8", ["const:884098:8", "const:4:8"]]
+ 00884098 ["CALLIND", null, ["register:0:8"]]
- 00884058 bytes 00013fd6
+ 00884098 bytes 00013fd6
~~~


<a id="compare-6e336b72d12b328b31a90b8b091cc0ae"></a>

### [`008842d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008842d8.md) → [`00884318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884318.md) FUN_00884318

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008842d8.md#insn-00884314) · [`00884328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008842d8.md#insn-00884328) · [`00884348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008842d8.md#insn-00884348)
- 新版 `00884354`（命令位置の公開資料なし） · `00884368`（命令位置の公開資料なし） · `00884388`（命令位置の公開資料なし）

~~~diff
- 00884314 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884314 ["INT_ADD", "register:40f0:8", ["const:884314:8", "const:4:8"]]
- 00884314 ["CALLIND", null, ["register:0:8"]]
+ 00884354 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884354 ["INT_ADD", "register:40f0:8", ["const:884354:8", "const:4:8"]]
+ 00884354 ["CALLIND", null, ["register:0:8"]]
- 00884314 bytes 00013fd6
+ 00884354 bytes 00013fd6
- 00884328 ["INT_ADD", "register:40f0:8", ["const:884328:8", "const:4:8"]]
- 00884328 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884368 ["INT_ADD", "register:40f0:8", ["const:884368:8", "const:4:8"]]
+ 00884368 ["CALL", null, ["callee:00c53d00:8"]]
- 00884328 bytes 6e3d0f94
+ 00884368 bytes 663e0f94
- 00884348 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884348 ["INT_ADD", "register:40f0:8", ["const:884348:8", "const:4:8"]]
- 00884348 ["CALLIND", null, ["register:0:8"]]
+ 00884388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884388 ["INT_ADD", "register:40f0:8", ["const:884388:8", "const:4:8"]]
+ 00884388 ["CALLIND", null, ["register:0:8"]]
- 00884348 bytes 00013fd6
+ 00884388 bytes 00013fd6
~~~


<a id="compare-7c574309d3adaacae430d9d38812b814"></a>

### [`0088435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088435c.md) → [`0088439c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088439c.md) FUN_0088439c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088435c.md#insn-00884398) · [`008843ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088435c.md#insn-008843ac) · [`008843c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088435c.md#insn-008843c0)
- 新版 `008843d8`（命令位置の公開資料なし） · `008843ec`（命令位置の公開資料なし） · `00884400`（命令位置の公開資料なし）

~~~diff
- 00884398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884398 ["INT_ADD", "register:40f0:8", ["const:884398:8", "const:4:8"]]
- 00884398 ["CALLIND", null, ["register:0:8"]]
+ 008843d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008843d8 ["INT_ADD", "register:40f0:8", ["const:8843d8:8", "const:4:8"]]
+ 008843d8 ["CALLIND", null, ["register:0:8"]]
- 00884398 bytes 00013fd6
+ 008843d8 bytes 00013fd6
- 008843ac ["INT_ADD", "register:40f0:8", ["const:8843ac:8", "const:4:8"]]
- 008843ac ["CALL", null, ["callee:00c53d00:8"]]
+ 008843ec ["INT_ADD", "register:40f0:8", ["const:8843ec:8", "const:4:8"]]
+ 008843ec ["CALL", null, ["callee:00c53d00:8"]]
- 008843ac bytes 4d3d0f94
+ 008843ec bytes 453e0f94
- 008843c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008843c0 ["INT_ADD", "register:40f0:8", ["const:8843c0:8", "const:4:8"]]
- 008843c0 ["CALLIND", null, ["register:0:8"]]
+ 00884400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884400 ["INT_ADD", "register:40f0:8", ["const:884400:8", "const:4:8"]]
+ 00884400 ["CALLIND", null, ["register:0:8"]]
- 008843c0 bytes 00013fd6
+ 00884400 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70bd8946337067598b2434ffcb81125"></a>

### [`00884684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884684.md) → [`008846c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008846c4.md) FUN_008846c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008846c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884684.md#insn-008846c0) · [`008846d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884684.md#insn-008846d4) · [`008846f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884684.md#insn-008846f4)
- 新版 `00884700`（命令位置の公開資料なし） · `00884714`（命令位置の公開資料なし） · `00884734`（命令位置の公開資料なし）

~~~diff
- 008846c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008846c0 ["INT_ADD", "register:40f0:8", ["const:8846c0:8", "const:4:8"]]
- 008846c0 ["CALLIND", null, ["register:0:8"]]
+ 00884700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884700 ["INT_ADD", "register:40f0:8", ["const:884700:8", "const:4:8"]]
+ 00884700 ["CALLIND", null, ["register:0:8"]]
- 008846c0 bytes 00013fd6
+ 00884700 bytes 00013fd6
- 008846d4 ["INT_ADD", "register:40f0:8", ["const:8846d4:8", "const:4:8"]]
- 008846d4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884714 ["INT_ADD", "register:40f0:8", ["const:884714:8", "const:4:8"]]
+ 00884714 ["CALL", null, ["callee:00c53d00:8"]]
- 008846d4 bytes 833c0f94
+ 00884714 bytes 7b3d0f94
- 008846f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008846f4 ["INT_ADD", "register:40f0:8", ["const:8846f4:8", "const:4:8"]]
- 008846f4 ["CALLIND", null, ["register:0:8"]]
+ 00884734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884734 ["INT_ADD", "register:40f0:8", ["const:884734:8", "const:4:8"]]
+ 00884734 ["CALLIND", null, ["register:0:8"]]
- 008846f4 bytes 00013fd6
+ 00884734 bytes 00013fd6
~~~


<a id="compare-b7040100cbfe5afeb1ea3c47a17ed025"></a>

### [`00884708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884708.md) → [`00884748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884748.md) FUN_00884748

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884708.md#insn-00884744) · [`00884758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884708.md#insn-00884758) · [`0088476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884708.md#insn-0088476c)
- 新版 `00884784`（命令位置の公開資料なし） · `00884798`（命令位置の公開資料なし） · `008847ac`（命令位置の公開資料なし）

~~~diff
- 00884744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884744 ["INT_ADD", "register:40f0:8", ["const:884744:8", "const:4:8"]]
- 00884744 ["CALLIND", null, ["register:0:8"]]
+ 00884784 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884784 ["INT_ADD", "register:40f0:8", ["const:884784:8", "const:4:8"]]
+ 00884784 ["CALLIND", null, ["register:0:8"]]
- 00884744 bytes 00013fd6
+ 00884784 bytes 00013fd6
- 00884758 ["INT_ADD", "register:40f0:8", ["const:884758:8", "const:4:8"]]
- 00884758 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884798 ["INT_ADD", "register:40f0:8", ["const:884798:8", "const:4:8"]]
+ 00884798 ["CALL", null, ["callee:00c53d00:8"]]
- 00884758 bytes 623c0f94
+ 00884798 bytes 5a3d0f94
- 0088476c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088476c ["INT_ADD", "register:40f0:8", ["const:88476c:8", "const:4:8"]]
- 0088476c ["CALLIND", null, ["register:0:8"]]
+ 008847ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 008847ac ["INT_ADD", "register:40f0:8", ["const:8847ac:8", "const:4:8"]]
+ 008847ac ["CALLIND", null, ["register:0:8"]]
- 0088476c bytes 00013fd6
+ 008847ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09a80174b9a4148135a1f286be1cc17"></a>

### [`00884a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884a30.md) → [`00884a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884a70.md) FUN_00884a70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884a30.md#insn-00884a6c) · [`00884a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884a30.md#insn-00884a80) · [`00884aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884a30.md#insn-00884aa0)
- 新版 `00884aac`（命令位置の公開資料なし） · `00884ac0`（命令位置の公開資料なし） · `00884ae0`（命令位置の公開資料なし）

~~~diff
- 00884a6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00884a6c ["INT_ADD", "register:40f0:8", ["const:884a6c:8", "const:4:8"]]
- 00884a6c ["CALLIND", null, ["register:0:8"]]
+ 00884aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884aac ["INT_ADD", "register:40f0:8", ["const:884aac:8", "const:4:8"]]
+ 00884aac ["CALLIND", null, ["register:0:8"]]
- 00884a6c bytes 00013fd6
+ 00884aac bytes 00013fd6
- 00884a80 ["INT_ADD", "register:40f0:8", ["const:884a80:8", "const:4:8"]]
- 00884a80 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884ac0 ["INT_ADD", "register:40f0:8", ["const:884ac0:8", "const:4:8"]]
+ 00884ac0 ["CALL", null, ["callee:00c53d00:8"]]
- 00884a80 bytes 983b0f94
+ 00884ac0 bytes 903c0f94
- 00884aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884aa0 ["INT_ADD", "register:40f0:8", ["const:884aa0:8", "const:4:8"]]
- 00884aa0 ["CALLIND", null, ["register:0:8"]]
+ 00884ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884ae0 ["INT_ADD", "register:40f0:8", ["const:884ae0:8", "const:4:8"]]
+ 00884ae0 ["CALLIND", null, ["register:0:8"]]
- 00884aa0 bytes 00013fd6
+ 00884ae0 bytes 00013fd6
~~~


<a id="compare-436be6e43fab4a4a794a9cfc6979c1e7"></a>

### [`00884ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884ab4.md) → [`00884af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884af4.md) FUN_00884af4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884ab4.md#insn-00884af0) · [`00884b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884ab4.md#insn-00884b04) · [`00884b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884ab4.md#insn-00884b18)
- 新版 `00884b30`（命令位置の公開資料なし） · `00884b44`（命令位置の公開資料なし） · `00884b58`（命令位置の公開資料なし）

~~~diff
- 00884af0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884af0 ["INT_ADD", "register:40f0:8", ["const:884af0:8", "const:4:8"]]
- 00884af0 ["CALLIND", null, ["register:0:8"]]
+ 00884b30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884b30 ["INT_ADD", "register:40f0:8", ["const:884b30:8", "const:4:8"]]
+ 00884b30 ["CALLIND", null, ["register:0:8"]]
- 00884af0 bytes 00013fd6
+ 00884b30 bytes 00013fd6
- 00884b04 ["INT_ADD", "register:40f0:8", ["const:884b04:8", "const:4:8"]]
- 00884b04 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884b44 ["INT_ADD", "register:40f0:8", ["const:884b44:8", "const:4:8"]]
+ 00884b44 ["CALL", null, ["callee:00c53d00:8"]]
- 00884b04 bytes 773b0f94
+ 00884b44 bytes 6f3c0f94
- 00884b18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884b18 ["INT_ADD", "register:40f0:8", ["const:884b18:8", "const:4:8"]]
- 00884b18 ["CALLIND", null, ["register:0:8"]]
+ 00884b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884b58 ["INT_ADD", "register:40f0:8", ["const:884b58:8", "const:4:8"]]
+ 00884b58 ["CALLIND", null, ["register:0:8"]]
- 00884b18 bytes 00013fd6
+ 00884b58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f84a416dafcd158dc81f9ce6c3bf262"></a>

### [`00884f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md) → [`00884f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884f74.md) FUN_00884f74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00884f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884f70) · [`00884f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884f84) · [`00884fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884fa4)
- 新版 `00884fb0`（命令位置の公開資料なし） · `00884fc4`（命令位置の公開資料なし） · `00884fe4`（命令位置の公開資料なし）

~~~diff
- 00884f70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884f70 ["INT_ADD", "register:40f0:8", ["const:884f70:8", "const:4:8"]]
- 00884f70 ["CALLIND", null, ["register:0:8"]]
+ 00884fb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884fb0 ["INT_ADD", "register:40f0:8", ["const:884fb0:8", "const:4:8"]]
+ 00884fb0 ["CALLIND", null, ["register:0:8"]]
- 00884f70 bytes 00013fd6
+ 00884fb0 bytes 00013fd6
- 00884f84 ["INT_ADD", "register:40f0:8", ["const:884f84:8", "const:4:8"]]
- 00884f84 ["CALL", null, ["callee:00c53d00:8"]]
+ 00884fc4 ["INT_ADD", "register:40f0:8", ["const:884fc4:8", "const:4:8"]]
+ 00884fc4 ["CALL", null, ["callee:00c53d00:8"]]
- 00884f84 bytes 573a0f94
+ 00884fc4 bytes 4f3b0f94
- 00884fa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884fa4 ["INT_ADD", "register:40f0:8", ["const:884fa4:8", "const:4:8"]]
- 00884fa4 ["CALLIND", null, ["register:0:8"]]
+ 00884fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884fe4 ["INT_ADD", "register:40f0:8", ["const:884fe4:8", "const:4:8"]]
+ 00884fe4 ["CALLIND", null, ["register:0:8"]]
- 00884fa4 bytes 00013fd6
+ 00884fe4 bytes 00013fd6
~~~


<a id="compare-2a5daa59fd4d5e1a36060e1ac4fa991c"></a>

### [`00885224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885224.md) → [`00885264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885264.md) FUN_00885264

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885224.md#insn-00885260) · [`00885274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885224.md#insn-00885274) · [`00885294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885224.md#insn-00885294)
- 新版 `008852a0`（命令位置の公開資料なし） · `008852b4`（命令位置の公開資料なし） · `008852d4`（命令位置の公開資料なし）

~~~diff
- 00885260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885260 ["INT_ADD", "register:40f0:8", ["const:885260:8", "const:4:8"]]
- 00885260 ["CALLIND", null, ["register:0:8"]]
+ 008852a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008852a0 ["INT_ADD", "register:40f0:8", ["const:8852a0:8", "const:4:8"]]
+ 008852a0 ["CALLIND", null, ["register:0:8"]]
- 00885260 bytes 00013fd6
+ 008852a0 bytes 00013fd6
- 00885274 ["INT_ADD", "register:40f0:8", ["const:885274:8", "const:4:8"]]
- 00885274 ["CALL", null, ["callee:00c53d00:8"]]
+ 008852b4 ["INT_ADD", "register:40f0:8", ["const:8852b4:8", "const:4:8"]]
+ 008852b4 ["CALL", null, ["callee:00c53d00:8"]]
- 00885274 bytes 9b390f94
+ 008852b4 bytes 933a0f94
- 00885294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885294 ["INT_ADD", "register:40f0:8", ["const:885294:8", "const:4:8"]]
- 00885294 ["CALLIND", null, ["register:0:8"]]
+ 008852d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008852d4 ["INT_ADD", "register:40f0:8", ["const:8852d4:8", "const:4:8"]]
+ 008852d4 ["CALLIND", null, ["register:0:8"]]
- 00885294 bytes 00013fd6
+ 008852d4 bytes 00013fd6
~~~


<a id="compare-73db73851378fed40560bcf5f7237847"></a>

### [`008852a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008852a8.md) → [`008852e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/008852e8.md) FUN_008852e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00884b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00884b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008852a8.md#insn-008852e4) · [`008852f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008852a8.md#insn-008852f8) · [`0088530c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008852a8.md#insn-0088530c)
- 新版 `00885324`（命令位置の公開資料なし） · `00885338`（命令位置の公開資料なし） · `0088534c`（命令位置の公開資料なし）

~~~diff
- 008852e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008852e4 ["INT_ADD", "register:40f0:8", ["const:8852e4:8", "const:4:8"]]
- 008852e4 ["CALLIND", null, ["register:0:8"]]
+ 00885324 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885324 ["INT_ADD", "register:40f0:8", ["const:885324:8", "const:4:8"]]
+ 00885324 ["CALLIND", null, ["register:0:8"]]
- 008852e4 bytes 00013fd6
+ 00885324 bytes 00013fd6
- 008852f8 ["INT_ADD", "register:40f0:8", ["const:8852f8:8", "const:4:8"]]
- 008852f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885338 ["INT_ADD", "register:40f0:8", ["const:885338:8", "const:4:8"]]
+ 00885338 ["CALL", null, ["callee:00c53d00:8"]]
- 008852f8 bytes 7a390f94
+ 00885338 bytes 723a0f94
- 0088530c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088530c ["INT_ADD", "register:40f0:8", ["const:88530c:8", "const:4:8"]]
- 0088530c ["CALLIND", null, ["register:0:8"]]
+ 0088534c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088534c ["INT_ADD", "register:40f0:8", ["const:88534c:8", "const:4:8"]]
+ 0088534c ["CALLIND", null, ["register:0:8"]]
- 0088530c bytes 00013fd6
+ 0088534c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f84dd8722fc6e94a5643fbc3679fe56f"></a>

### [`008855cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008855cc.md) → [`0088560c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088560c.md) FUN_0088560c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008855f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008855cc.md#insn-008855f4) · [`00885608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008855cc.md#insn-00885608) · [`00885610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008855cc.md#insn-00885610)
- 新版 `00885634`（命令位置の公開資料なし） · `00885648`（命令位置の公開資料なし） · `00885650`（命令位置の公開資料なし）

~~~diff
- 008855f4 ["INT_ADD", "register:40f0:8", ["const:8855f4:8", "const:4:8"]]
- 008855f4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885634 ["INT_ADD", "register:40f0:8", ["const:885634:8", "const:4:8"]]
+ 00885634 ["CALL", null, ["callee:00c53d00:8"]]
- 008855f4 bytes bb380f94
+ 00885634 bytes b3390f94
- 00885608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885608 ["INT_ADD", "register:40f0:8", ["const:885608:8", "const:4:8"]]
- 00885608 ["CALLIND", null, ["register:0:8"]]
+ 00885648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885648 ["INT_ADD", "register:40f0:8", ["const:885648:8", "const:4:8"]]
+ 00885648 ["CALLIND", null, ["register:0:8"]]
- 00885608 bytes 00013fd6
+ 00885648 bytes 00013fd6
- 00885610 ["INT_ADD", "register:40f0:8", ["const:885610:8", "const:4:8"]]
- 00885610 ["CALL", null, ["callee:00c57e80:8"]]
+ 00885650 ["INT_ADD", "register:40f0:8", ["const:885650:8", "const:4:8"]]
+ 00885650 ["CALL", null, ["callee:00c57e80:8"]]
- 00885610 bytes 1c490f94
+ 00885650 bytes 0c4a0f94
~~~


<a id="compare-99a49efaa63da926c423853ffeb7db66"></a>

### [`0088565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088565c.md) → [`0088569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/0088569c.md) FUN_0088569c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088565c.md#insn-00885684) · [`00885698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088565c.md#insn-00885698) · [`008856a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088565c.md#insn-008856a0)
- 新版 `008856c4`（命令位置の公開資料なし） · `008856d8`（命令位置の公開資料なし） · `008856e0`（命令位置の公開資料なし）

~~~diff
- 00885684 ["INT_ADD", "register:40f0:8", ["const:885684:8", "const:4:8"]]
- 00885684 ["CALL", null, ["callee:00c53d00:8"]]
+ 008856c4 ["INT_ADD", "register:40f0:8", ["const:8856c4:8", "const:4:8"]]
+ 008856c4 ["CALL", null, ["callee:00c53d00:8"]]
- 00885684 bytes 97380f94
+ 008856c4 bytes 8f390f94
- 00885698 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885698 ["INT_ADD", "register:40f0:8", ["const:885698:8", "const:4:8"]]
- 00885698 ["CALLIND", null, ["register:0:8"]]
+ 008856d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008856d8 ["INT_ADD", "register:40f0:8", ["const:8856d8:8", "const:4:8"]]
+ 008856d8 ["CALLIND", null, ["register:0:8"]]
- 00885698 bytes 00013fd6
+ 008856d8 bytes 00013fd6
- 008856a0 ["INT_ADD", "register:40f0:8", ["const:8856a0:8", "const:4:8"]]
- 008856a0 ["CALL", null, ["callee:00c57e80:8"]]
+ 008856e0 ["INT_ADD", "register:40f0:8", ["const:8856e0:8", "const:4:8"]]
+ 008856e0 ["CALL", null, ["callee:00c57e80:8"]]
- 008856a0 bytes f8480f94
+ 008856e0 bytes e8490f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b470944cf35172da10b7c9e92db786a7"></a>

### [`00885a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885a50.md) → [`00885a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885a90.md) FUN_00885a90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885a50.md#insn-00885a8c) · [`00885aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885a50.md#insn-00885aa0) · [`00885ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885a50.md#insn-00885ac0)
- 新版 `00885acc`（命令位置の公開資料なし） · `00885ae0`（命令位置の公開資料なし） · `00885b00`（命令位置の公開資料なし）

~~~diff
- 00885a8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00885a8c ["INT_ADD", "register:40f0:8", ["const:885a8c:8", "const:4:8"]]
- 00885a8c ["CALLIND", null, ["register:0:8"]]
+ 00885acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885acc ["INT_ADD", "register:40f0:8", ["const:885acc:8", "const:4:8"]]
+ 00885acc ["CALLIND", null, ["register:0:8"]]
- 00885a8c bytes 00013fd6
+ 00885acc bytes 00013fd6
- 00885aa0 ["INT_ADD", "register:40f0:8", ["const:885aa0:8", "const:4:8"]]
- 00885aa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885ae0 ["INT_ADD", "register:40f0:8", ["const:885ae0:8", "const:4:8"]]
+ 00885ae0 ["CALL", null, ["callee:00c53d00:8"]]
- 00885aa0 bytes 90370f94
+ 00885ae0 bytes 88380f94
- 00885ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885ac0 ["INT_ADD", "register:40f0:8", ["const:885ac0:8", "const:4:8"]]
- 00885ac0 ["CALLIND", null, ["register:0:8"]]
+ 00885b00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b00 ["INT_ADD", "register:40f0:8", ["const:885b00:8", "const:4:8"]]
+ 00885b00 ["CALLIND", null, ["register:0:8"]]
- 00885ac0 bytes 00013fd6
+ 00885b00 bytes 00013fd6
~~~


<a id="compare-929e52a9dbc5322ce02faeed78b3df97"></a>

### [`00885d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885d40.md) → [`00885d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885d80.md) FUN_00885d80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885d40.md#insn-00885d7c) · [`00885d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885d40.md#insn-00885d90) · [`00885db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885d40.md#insn-00885db0)
- 新版 `00885dbc`（命令位置の公開資料なし） · `00885dd0`（命令位置の公開資料なし） · `00885df0`（命令位置の公開資料なし）

~~~diff
- 00885d7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00885d7c ["INT_ADD", "register:40f0:8", ["const:885d7c:8", "const:4:8"]]
- 00885d7c ["CALLIND", null, ["register:0:8"]]
+ 00885dbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885dbc ["INT_ADD", "register:40f0:8", ["const:885dbc:8", "const:4:8"]]
+ 00885dbc ["CALLIND", null, ["register:0:8"]]
- 00885d7c bytes 00013fd6
+ 00885dbc bytes 00013fd6
- 00885d90 ["INT_ADD", "register:40f0:8", ["const:885d90:8", "const:4:8"]]
- 00885d90 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885dd0 ["INT_ADD", "register:40f0:8", ["const:885dd0:8", "const:4:8"]]
+ 00885dd0 ["CALL", null, ["callee:00c53d00:8"]]
- 00885d90 bytes d4360f94
+ 00885dd0 bytes cc370f94
- 00885db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885db0 ["INT_ADD", "register:40f0:8", ["const:885db0:8", "const:4:8"]]
- 00885db0 ["CALLIND", null, ["register:0:8"]]
+ 00885df0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885df0 ["INT_ADD", "register:40f0:8", ["const:885df0:8", "const:4:8"]]
+ 00885df0 ["CALLIND", null, ["register:0:8"]]
- 00885db0 bytes 00013fd6
+ 00885df0 bytes 00013fd6
~~~


<a id="compare-10f8364859df3fcf039ee68e79d36369"></a>

### [`00885dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885dc4.md) → [`00885e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885e04.md) FUN_00885e04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00885e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885dc4.md#insn-00885e00) · [`00885e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885dc4.md#insn-00885e14) · [`00885e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885dc4.md#insn-00885e28)
- 新版 `00885e40`（命令位置の公開資料なし） · `00885e54`（命令位置の公開資料なし） · `00885e68`（命令位置の公開資料なし）

~~~diff
- 00885e00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e00 ["INT_ADD", "register:40f0:8", ["const:885e00:8", "const:4:8"]]
- 00885e00 ["CALLIND", null, ["register:0:8"]]
+ 00885e40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885e40 ["INT_ADD", "register:40f0:8", ["const:885e40:8", "const:4:8"]]
+ 00885e40 ["CALLIND", null, ["register:0:8"]]
- 00885e00 bytes 00013fd6
+ 00885e40 bytes 00013fd6
- 00885e14 ["INT_ADD", "register:40f0:8", ["const:885e14:8", "const:4:8"]]
- 00885e14 ["CALL", null, ["callee:00c53d00:8"]]
+ 00885e54 ["INT_ADD", "register:40f0:8", ["const:885e54:8", "const:4:8"]]
+ 00885e54 ["CALL", null, ["callee:00c53d00:8"]]
- 00885e14 bytes b3360f94
+ 00885e54 bytes ab370f94
- 00885e28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e28 ["INT_ADD", "register:40f0:8", ["const:885e28:8", "const:4:8"]]
- 00885e28 ["CALLIND", null, ["register:0:8"]]
+ 00885e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885e68 ["INT_ADD", "register:40f0:8", ["const:885e68:8", "const:4:8"]]
+ 00885e68 ["CALLIND", null, ["register:0:8"]]
- 00885e28 bytes 00013fd6
+ 00885e68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe48dd8cefd007645d1a004f3509ad48"></a>

### [`008860fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008860fc.md) → [`0088613c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/0088613c.md) FUN_0088613c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008860fc.md#insn-00886138)
- 新版 `00886178`（命令位置の公開資料なし）

~~~diff
- 00886138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886138 ["INT_ADD", "register:40f0:8", ["const:886138:8", "const:4:8"]]
- 00886138 ["CALLIND", null, ["register:0:8"]]
+ 00886178 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886178 ["INT_ADD", "register:40f0:8", ["const:886178:8", "const:4:8"]]
+ 00886178 ["CALLIND", null, ["register:0:8"]]
- 00886138 bytes 00013fd6
+ 00886178 bytes 00013fd6
~~~


<a id="compare-7bc8a423f27fa8f7c24ed0082a395ac2"></a>

### [`00886160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md) → [`008861a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md) FUN_008861a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md#insn-0088619c) · [`008861ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md#insn-008861ac)
- 新版 `008861dc`（命令位置の公開資料なし） · `008861ec`（命令位置の公開資料なし）

~~~diff
- 0088619c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088619c ["INT_ADD", "register:40f0:8", ["const:88619c:8", "const:4:8"]]
- 0088619c ["CALLIND", null, ["register:0:8"]]
+ 008861dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008861dc ["INT_ADD", "register:40f0:8", ["const:8861dc:8", "const:4:8"]]
+ 008861dc ["CALLIND", null, ["register:0:8"]]
- 0088619c bytes 00013fd6
+ 008861dc bytes 00013fd6
- 008861ac ["INT_ADD", "register:40f0:8", ["const:8861ac:8", "const:4:8"]]
- 008861ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 008861ec ["INT_ADD", "register:40f0:8", ["const:8861ec:8", "const:4:8"]]
+ 008861ec ["CALL", null, ["callee:00c57eb0:8"]]
- 008861ac bytes 41460f94
+ 008861ec bytes 31470f94
~~~


<a id="compare-46ee35b71ac7adf82ae7ff65a9b02169"></a>

### [`00886668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886668.md) → [`008866a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866a8.md) FUN_008866a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008861c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008866a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886668.md#insn-008866a4)
- 新版 `008866e4`（命令位置の公開資料なし）

~~~diff
- 008866a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008866a4 ["INT_ADD", "register:40f0:8", ["const:8866a4:8", "const:4:8"]]
- 008866a4 ["CALLIND", null, ["register:0:8"]]
+ 008866e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008866e4 ["INT_ADD", "register:40f0:8", ["const:8866e4:8", "const:4:8"]]
+ 008866e4 ["CALLIND", null, ["register:0:8"]]
- 008866a4 bytes 00013fd6
+ 008866e4 bytes 00013fd6
~~~


<a id="compare-eee223a74bfd859408e36fb2cf68afb4"></a>

### [`008866b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md) → [`008866f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008866f8.md) FUN_008866f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md#insn-00886758) · [`00886780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md#insn-00886780) · [`00886798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md#insn-00886798)
- 新版 `00886798`（命令位置の公開資料なし） · `008867c0`（命令位置の公開資料なし） · `008867d8`（命令位置の公開資料なし）

~~~diff
- 00886758 ["INT_ADD", "register:40f0:8", ["const:886758:8", "const:4:8"]]
- 00886758 ["CALL", null, ["callee:0043bb20:8"]]
+ 00886798 ["INT_ADD", "register:40f0:8", ["const:886798:8", "const:4:8"]]
+ 00886798 ["CALL", null, ["callee:0043bb20:8"]]
- 00886758 bytes e2d4ee97
+ 00886798 bytes e2d4ee97
- 00886780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886780 ["INT_ADD", "register:40f0:8", ["const:886780:8", "const:4:8"]]
- 00886780 ["CALLIND", null, ["register:0:8"]]
+ 008867c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008867c0 ["INT_ADD", "register:40f0:8", ["const:8867c0:8", "const:4:8"]]
+ 008867c0 ["CALLIND", null, ["register:0:8"]]
- 00886780 bytes 00013fd6
+ 008867c0 bytes 00013fd6
- 00886798 ["INT_ADD", "register:40f0:8", ["const:886798:8", "const:4:8"]]
- 00886798 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008867d8 ["INT_ADD", "register:40f0:8", ["const:8867d8:8", "const:4:8"]]
+ 008867d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00886798 bytes c6440f94
+ 008867d8 bytes b6450f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b513d70bc663831d1427b17674685db8"></a>

### [`008869c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008869c4.md) → [`00886a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a04.md) FUN_00886a04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008869e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008869c4.md#insn-008869e0) · [`00886a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008869c4.md#insn-00886a00)
- 新版 `00886a20`（命令位置の公開資料なし） · `00886a40`（命令位置の公開資料なし）

~~~diff
- 008869e0 ["INT_ADD", "register:40f0:8", ["const:8869e0:8", "const:4:8"]]
- 008869e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00886a20 ["INT_ADD", "register:40f0:8", ["const:886a20:8", "const:4:8"]]
+ 00886a20 ["CALL", null, ["callee:00c53d00:8"]]
- 008869e0 bytes c0330f94
+ 00886a20 bytes b8340f94
- 00886a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886a00 ["INT_ADD", "register:40f0:8", ["const:886a00:8", "const:4:8"]]
- 00886a00 ["CALLIND", null, ["register:0:8"]]
+ 00886a40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886a40 ["INT_ADD", "register:40f0:8", ["const:886a40:8", "const:4:8"]]
+ 00886a40 ["CALLIND", null, ["register:0:8"]]
- 00886a00 bytes 00013fd6
+ 00886a40 bytes 00013fd6
~~~


<a id="compare-97b268b29e56dd3163c8fed0a91b54db"></a>

### [`00886a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a14.md) → [`00886a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886a54.md) FUN_00886a54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a14.md#insn-00886a34) · [`00886a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a14.md#insn-00886a48) · [`00886a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a14.md#insn-00886a50)
- 新版 `00886a74`（命令位置の公開資料なし） · `00886a88`（命令位置の公開資料なし） · `00886a90`（命令位置の公開資料なし）

~~~diff
- 00886a34 ["INT_ADD", "register:40f0:8", ["const:886a34:8", "const:4:8"]]
- 00886a34 ["CALL", null, ["callee:00c53d00:8"]]
+ 00886a74 ["INT_ADD", "register:40f0:8", ["const:886a74:8", "const:4:8"]]
+ 00886a74 ["CALL", null, ["callee:00c53d00:8"]]
- 00886a34 bytes ab330f94
+ 00886a74 bytes a3340f94
- 00886a48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886a48 ["INT_ADD", "register:40f0:8", ["const:886a48:8", "const:4:8"]]
- 00886a48 ["CALLIND", null, ["register:0:8"]]
+ 00886a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886a88 ["INT_ADD", "register:40f0:8", ["const:886a88:8", "const:4:8"]]
+ 00886a88 ["CALLIND", null, ["register:0:8"]]
- 00886a48 bytes 00013fd6
+ 00886a88 bytes 00013fd6
- 00886a50 ["INT_ADD", "register:40f0:8", ["const:886a50:8", "const:4:8"]]
- 00886a50 ["CALL", null, ["callee:00c57e80:8"]]
+ 00886a90 ["INT_ADD", "register:40f0:8", ["const:886a90:8", "const:4:8"]]
+ 00886a90 ["CALL", null, ["callee:00c57e80:8"]]
- 00886a50 bytes 0c440f94
+ 00886a90 bytes fc440f94
~~~


<a id="compare-a074afb06ac0b3185a512fd9a7c3934d"></a>

### [`00886ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886ed0.md) → [`00886f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f10.md) FUN_00886f10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00886a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886ed0.md#insn-00886ef0)
- 新版 `00886f30`（命令位置の公開資料なし）

~~~diff
- 00886ef0 ["INT_ADD", "register:40f0:8", ["const:886ef0:8", "const:4:8"]]
- 00886ef0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00886f30 ["INT_ADD", "register:40f0:8", ["const:886f30:8", "const:4:8"]]
+ 00886f30 ["CALL", null, ["callee:00c57eb0:8"]]
- 00886ef0 bytes f0420f94
+ 00886f30 bytes e0430f94
~~~


<a id="compare-6afd88767c47118ed7f50f1d5f9108dc"></a>

### [`008876e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md) → [`00887724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md) FUN_00887724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848710.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · 呼出先 4件 [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848750.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 4件 [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088770c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md#insn-0088770c) · [`00887720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md#insn-00887720) · [`0088773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md#insn-0088773c)
- 新版 `0088774c`（命令位置の公開資料なし） · `00887760`（命令位置の公開資料なし） · `0088777c`（命令位置の公開資料なし）

~~~diff
- 0088770c ["INT_ADD", "register:40f0:8", ["const:88770c:8", "const:4:8"]]
- 0088770c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088774c ["INT_ADD", "register:40f0:8", ["const:88774c:8", "const:4:8"]]
+ 0088774c ["CALL", null, ["callee:00c57eb0:8"]]
- 0088770c bytes e9400f94
+ 0088774c bytes d9410f94
- 00887720 ["INT_ADD", "register:40f0:8", ["const:887720:8", "const:4:8"]]
- 00887720 ["CALL", null, ["callee:006a2b78:8"]]
+ 00887760 ["INT_ADD", "register:40f0:8", ["const:887760:8", "const:4:8"]]
+ 00887760 ["CALL", null, ["callee:006a2b78:8"]]
- 00887720 bytes 066df897
+ 00887760 bytes 066df897
- 0088773c ["INT_ADD", "register:40f0:8", ["const:88773c:8", "const:4:8"]]
- 0088773c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088777c ["INT_ADD", "register:40f0:8", ["const:88777c:8", "const:4:8"]]
+ 0088777c ["CALL", null, ["callee:00c57eb0:8"]]
- 0088773c bytes dd400f94
+ 0088777c bytes cd410f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-362abf3116a29c75a0de58dc753c6969"></a>

### [`00887fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887fec.md) → [`0088802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md) FUN_0088802c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887fec.md#insn-00888008) · [`00888028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887fec.md#insn-00888028)
- 新版 `00888048`（命令位置の公開資料なし） · `00888068`（命令位置の公開資料なし）

~~~diff
- 00888008 ["INT_ADD", "register:40f0:8", ["const:888008:8", "const:4:8"]]
- 00888008 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888048 ["INT_ADD", "register:40f0:8", ["const:888048:8", "const:4:8"]]
+ 00888048 ["CALL", null, ["callee:00c53d00:8"]]
- 00888008 bytes 362e0f94
+ 00888048 bytes 2e2f0f94
- 00888028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888028 ["INT_ADD", "register:40f0:8", ["const:888028:8", "const:4:8"]]
- 00888028 ["CALLIND", null, ["register:0:8"]]
+ 00888068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888068 ["INT_ADD", "register:40f0:8", ["const:888068:8", "const:4:8"]]
+ 00888068 ["CALLIND", null, ["register:0:8"]]
- 00888028 bytes 00013fd6
+ 00888068 bytes 00013fd6
~~~


<a id="compare-29b090513883212f3edc6e8e769f1e3a"></a>

### [`0088803c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088803c.md) → [`0088807c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088807c.md) FUN_0088807c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088803c.md#insn-00888058) · [`00888078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088803c.md#insn-00888078)
- 新版 `00888098`（命令位置の公開資料なし） · `008880b8`（命令位置の公開資料なし）

~~~diff
- 00888058 ["INT_ADD", "register:40f0:8", ["const:888058:8", "const:4:8"]]
- 00888058 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888098 ["INT_ADD", "register:40f0:8", ["const:888098:8", "const:4:8"]]
+ 00888098 ["CALL", null, ["callee:00c53d00:8"]]
- 00888058 bytes 222e0f94
+ 00888098 bytes 1a2f0f94
- 00888078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888078 ["INT_ADD", "register:40f0:8", ["const:888078:8", "const:4:8"]]
- 00888078 ["CALLIND", null, ["register:0:8"]]
+ 008880b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008880b8 ["INT_ADD", "register:40f0:8", ["const:8880b8:8", "const:4:8"]]
+ 008880b8 ["CALLIND", null, ["register:0:8"]]
- 00888078 bytes 00013fd6
+ 008880b8 bytes 00013fd6
~~~


<a id="compare-d8b613a69aad2858b56eb789e6adf1ec"></a>

### [`0088808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088808c.md) → [`008880cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008880cc.md) FUN_008880cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008880a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088808c.md#insn-008880a8) · [`008880c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088808c.md#insn-008880c8)
- 新版 `008880e8`（命令位置の公開資料なし） · `00888108`（命令位置の公開資料なし）

~~~diff
- 008880a8 ["INT_ADD", "register:40f0:8", ["const:8880a8:8", "const:4:8"]]
- 008880a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 008880e8 ["INT_ADD", "register:40f0:8", ["const:8880e8:8", "const:4:8"]]
+ 008880e8 ["CALL", null, ["callee:00c53d00:8"]]
- 008880a8 bytes 0e2e0f94
+ 008880e8 bytes 062f0f94
- 008880c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008880c8 ["INT_ADD", "register:40f0:8", ["const:8880c8:8", "const:4:8"]]
- 008880c8 ["CALLIND", null, ["register:0:8"]]
+ 00888108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888108 ["INT_ADD", "register:40f0:8", ["const:888108:8", "const:4:8"]]
+ 00888108 ["CALLIND", null, ["register:0:8"]]
- 008880c8 bytes 00013fd6
+ 00888108 bytes 00013fd6
~~~


<a id="compare-d948f8d8fcd92fbb7a1b1997fffc67c1"></a>

### [`008880dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008880dc.md) → [`0088811c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088811c.md) FUN_0088811c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008880f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008880dc.md#insn-008880f8) · [`00888118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008880dc.md#insn-00888118)
- 新版 `00888138`（命令位置の公開資料なし） · `00888158`（命令位置の公開資料なし）

~~~diff
- 008880f8 ["INT_ADD", "register:40f0:8", ["const:8880f8:8", "const:4:8"]]
- 008880f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888138 ["INT_ADD", "register:40f0:8", ["const:888138:8", "const:4:8"]]
+ 00888138 ["CALL", null, ["callee:00c53d00:8"]]
- 008880f8 bytes fa2d0f94
+ 00888138 bytes f22e0f94
- 00888118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888118 ["INT_ADD", "register:40f0:8", ["const:888118:8", "const:4:8"]]
- 00888118 ["CALLIND", null, ["register:0:8"]]
+ 00888158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888158 ["INT_ADD", "register:40f0:8", ["const:888158:8", "const:4:8"]]
+ 00888158 ["CALLIND", null, ["register:0:8"]]
- 00888118 bytes 00013fd6
+ 00888158 bytes 00013fd6
~~~


<a id="compare-911d3b4a371eeca6818798c76756519a"></a>

### [`0088812c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088812c.md) → [`0088816c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088816c.md) FUN_0088816c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088812c.md#insn-00888148) · [`00888168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088812c.md#insn-00888168)
- 新版 `00888188`（命令位置の公開資料なし） · `008881a8`（命令位置の公開資料なし）

~~~diff
- 00888148 ["INT_ADD", "register:40f0:8", ["const:888148:8", "const:4:8"]]
- 00888148 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888188 ["INT_ADD", "register:40f0:8", ["const:888188:8", "const:4:8"]]
+ 00888188 ["CALL", null, ["callee:00c53d00:8"]]
- 00888148 bytes e62d0f94
+ 00888188 bytes de2e0f94
- 00888168 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888168 ["INT_ADD", "register:40f0:8", ["const:888168:8", "const:4:8"]]
- 00888168 ["CALLIND", null, ["register:0:8"]]
+ 008881a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008881a8 ["INT_ADD", "register:40f0:8", ["const:8881a8:8", "const:4:8"]]
+ 008881a8 ["CALLIND", null, ["register:0:8"]]
- 00888168 bytes 00013fd6
+ 008881a8 bytes 00013fd6
~~~


<a id="compare-948db29907d93a67f2936359b68b9dfb"></a>

### [`0088817c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088817c.md) → [`008881bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008881bc.md) FUN_008881bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088817c.md#insn-00888198) · [`008881b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088817c.md#insn-008881b8)
- 新版 `008881d8`（命令位置の公開資料なし） · `008881f8`（命令位置の公開資料なし）

~~~diff
- 00888198 ["INT_ADD", "register:40f0:8", ["const:888198:8", "const:4:8"]]
- 00888198 ["CALL", null, ["callee:00c53d00:8"]]
+ 008881d8 ["INT_ADD", "register:40f0:8", ["const:8881d8:8", "const:4:8"]]
+ 008881d8 ["CALL", null, ["callee:00c53d00:8"]]
- 00888198 bytes d22d0f94
+ 008881d8 bytes ca2e0f94
- 008881b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008881b8 ["INT_ADD", "register:40f0:8", ["const:8881b8:8", "const:4:8"]]
- 008881b8 ["CALLIND", null, ["register:0:8"]]
+ 008881f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008881f8 ["INT_ADD", "register:40f0:8", ["const:8881f8:8", "const:4:8"]]
+ 008881f8 ["CALLIND", null, ["register:0:8"]]
- 008881b8 bytes 00013fd6
+ 008881f8 bytes 00013fd6
~~~


<a id="compare-f67ac7fbe546af3c7047027edefafc7e"></a>

### [`008881cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008881cc.md) → [`0088820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088820c.md) FUN_0088820c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008881e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008881cc.md#insn-008881e8) · [`00888208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008881cc.md#insn-00888208)
- 新版 `00888228`（命令位置の公開資料なし） · `00888248`（命令位置の公開資料なし）

~~~diff
- 008881e8 ["INT_ADD", "register:40f0:8", ["const:8881e8:8", "const:4:8"]]
- 008881e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888228 ["INT_ADD", "register:40f0:8", ["const:888228:8", "const:4:8"]]
+ 00888228 ["CALL", null, ["callee:00c53d00:8"]]
- 008881e8 bytes be2d0f94
+ 00888228 bytes b62e0f94
- 00888208 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888208 ["INT_ADD", "register:40f0:8", ["const:888208:8", "const:4:8"]]
- 00888208 ["CALLIND", null, ["register:0:8"]]
+ 00888248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888248 ["INT_ADD", "register:40f0:8", ["const:888248:8", "const:4:8"]]
+ 00888248 ["CALLIND", null, ["register:0:8"]]
- 00888208 bytes 00013fd6
+ 00888248 bytes 00013fd6
~~~


<a id="compare-23eb8b5e0492edb13da16afcd5d9d6a6"></a>

### [`0088821c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088821c.md) → [`0088825c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088825c.md) FUN_0088825c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088821c.md#insn-00888238) · [`00888258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088821c.md#insn-00888258)
- 新版 `00888278`（命令位置の公開資料なし） · `00888298`（命令位置の公開資料なし）

~~~diff
- 00888238 ["INT_ADD", "register:40f0:8", ["const:888238:8", "const:4:8"]]
- 00888238 ["CALL", null, ["callee:00c53d00:8"]]
+ 00888278 ["INT_ADD", "register:40f0:8", ["const:888278:8", "const:4:8"]]
+ 00888278 ["CALL", null, ["callee:00c53d00:8"]]
- 00888238 bytes aa2d0f94
+ 00888278 bytes a22e0f94
- 00888258 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888258 ["INT_ADD", "register:40f0:8", ["const:888258:8", "const:4:8"]]
- 00888258 ["CALLIND", null, ["register:0:8"]]
+ 00888298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888298 ["INT_ADD", "register:40f0:8", ["const:888298:8", "const:4:8"]]
+ 00888298 ["CALLIND", null, ["register:0:8"]]
- 00888258 bytes 00013fd6
+ 00888298 bytes 00013fd6
~~~


<a id="compare-1ec27516f554431bedc8aac0a6b34813"></a>

### [`0088826c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088826c.md) → [`008882ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008882ac.md) FUN_008882ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00616910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md) [`00626484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`00b375f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md)
- 新版 呼出元 10件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) [`006264c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264c4.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00b37a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37a18.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088826c.md#insn-00888378) · [`00888380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088826c.md#insn-00888380)
- 新版 `008883b8`（命令位置の公開資料なし） · `008883c0`（命令位置の公開資料なし）

~~~diff
- 00888378 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888378 ["INT_ADD", "register:40f0:8", ["const:888378:8", "const:4:8"]]
- 00888378 ["CALLIND", null, ["register:0:8"]]
+ 008883b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008883b8 ["INT_ADD", "register:40f0:8", ["const:8883b8:8", "const:4:8"]]
+ 008883b8 ["CALLIND", null, ["register:0:8"]]
- 00888378 bytes 00013fd6
+ 008883b8 bytes 00013fd6
- 00888380 ["INT_ADD", "register:40f0:8", ["const:888380:8", "const:4:8"]]
- 00888380 ["CALL", null, ["callee:00b37a18:8"]]
+ 008883c0 ["INT_ADD", "register:40f0:8", ["const:8883c0:8", "const:4:8"]]
+ 008883c0 ["CALL", null, ["callee:00b37a18:8"]]
- 00888380 bytes 9cbc0a94
+ 008883c0 bytes 96bd0a94
~~~


<a id="compare-3f8800bd14bb56a1170f040010e70582"></a>

### [`00888780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888780.md) → [`008887c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008887c0.md) FUN_008887c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888780.md#insn-00888808) · [`00888810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888780.md#insn-00888810)
- 新版 `00888848`（命令位置の公開資料なし） · `00888850`（命令位置の公開資料なし）

~~~diff
- 00888808 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888808 ["INT_ADD", "register:40f0:8", ["const:888808:8", "const:4:8"]]
- 00888808 ["CALLIND", null, ["register:0:8"]]
+ 00888848 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888848 ["INT_ADD", "register:40f0:8", ["const:888848:8", "const:4:8"]]
+ 00888848 ["CALLIND", null, ["register:0:8"]]
- 00888808 bytes 00013fd6
+ 00888848 bytes 00013fd6
- 00888810 ["INT_ADD", "register:40f0:8", ["const:888810:8", "const:4:8"]]
- 00888810 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00888850 ["INT_ADD", "register:40f0:8", ["const:888850:8", "const:4:8"]]
+ 00888850 ["CALL", null, ["callee:00c57ee0:8"]]
- 00888810 bytes b43c0f94
+ 00888850 bytes a43d0f94
~~~


<a id="compare-00c9e33040df5a3b38d38313807209d1"></a>

### [`00888e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888e3c.md) → [`00888e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md) FUN_00888e7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888e3c.md#insn-00888ea8) · [`00888eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888e3c.md#insn-00888eb8) · [`00888ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888e3c.md#insn-00888ed8)
- 新版 `00888ee8`（命令位置の公開資料なし） · `00888ef8`（命令位置の公開資料なし） · `00888f18`（命令位置の公開資料なし）

~~~diff
- 00888ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888ea8 ["INT_ADD", "register:40f0:8", ["const:888ea8:8", "const:4:8"]]
- 00888ea8 ["CALLIND", null, ["register:0:8"]]
+ 00888ee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888ee8 ["INT_ADD", "register:40f0:8", ["const:888ee8:8", "const:4:8"]]
+ 00888ee8 ["CALLIND", null, ["register:0:8"]]
- 00888ea8 bytes 00013fd6
+ 00888ee8 bytes 00013fd6
- 00888eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888eb8 ["INT_ADD", "register:40f0:8", ["const:888eb8:8", "const:4:8"]]
- 00888eb8 ["CALLIND", null, ["register:0:8"]]
+ 00888ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888ef8 ["INT_ADD", "register:40f0:8", ["const:888ef8:8", "const:4:8"]]
+ 00888ef8 ["CALLIND", null, ["register:0:8"]]
- 00888eb8 bytes 00013fd6
+ 00888ef8 bytes 00013fd6
- 00888ed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888ed8 ["INT_ADD", "register:40f0:8", ["const:888ed8:8", "const:4:8"]]
- 00888ed8 ["CALLIND", null, ["register:0:8"]]
+ 00888f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888f18 ["INT_ADD", "register:40f0:8", ["const:888f18:8", "const:4:8"]]
+ 00888f18 ["CALLIND", null, ["register:0:8"]]
- 00888ed8 bytes 00013fd6
+ 00888f18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33f22d8317013c78647325658c166cb4"></a>

### [`00889030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889030.md) → [`00889070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889070.md) FUN_00889070

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088909c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889030.md#insn-0088909c) · [`008890ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889030.md#insn-008890ac) · [`008890cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/00889030.md#insn-008890cc)
- 新版 `008890dc`（命令位置の公開資料なし） · `008890ec`（命令位置の公開資料なし） · `0088910c`（命令位置の公開資料なし）

~~~diff
- 0088909c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088909c ["INT_ADD", "register:40f0:8", ["const:88909c:8", "const:4:8"]]
- 0088909c ["CALLIND", null, ["register:0:8"]]
+ 008890dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008890dc ["INT_ADD", "register:40f0:8", ["const:8890dc:8", "const:4:8"]]
+ 008890dc ["CALLIND", null, ["register:0:8"]]
- 0088909c bytes 00013fd6
+ 008890dc bytes 00013fd6
- 008890ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008890ac ["INT_ADD", "register:40f0:8", ["const:8890ac:8", "const:4:8"]]
- 008890ac ["CALLIND", null, ["register:0:8"]]
+ 008890ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008890ec ["INT_ADD", "register:40f0:8", ["const:8890ec:8", "const:4:8"]]
+ 008890ec ["CALLIND", null, ["register:0:8"]]
- 008890ac bytes 00013fd6
+ 008890ec bytes 00013fd6
- 008890cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008890cc ["INT_ADD", "register:40f0:8", ["const:8890cc:8", "const:4:8"]]
- 008890cc ["CALLIND", null, ["register:0:8"]]
+ 0088910c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088910c ["INT_ADD", "register:40f0:8", ["const:88910c:8", "const:4:8"]]
+ 0088910c ["CALLIND", null, ["register:0:8"]]
- 008890cc bytes 00013fd6
+ 0088910c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ca43243b6ad9f25222f312e2537162"></a>

### [`0088952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088952c.md) → [`0088956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088956c.md) FUN_0088956c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00b37760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00889598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088952c.md#insn-00889598) · [`008895a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088952c.md#insn-008895a8) · [`008895c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00889/0088952c.md#insn-008895c8)
- 新版 `008895d8`（命令位置の公開資料なし） · `008895e8`（命令位置の公開資料なし） · `00889608`（命令位置の公開資料なし）

~~~diff
- 00889598 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889598 ["INT_ADD", "register:40f0:8", ["const:889598:8", "const:4:8"]]
- 00889598 ["CALLIND", null, ["register:0:8"]]
+ 008895d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008895d8 ["INT_ADD", "register:40f0:8", ["const:8895d8:8", "const:4:8"]]
+ 008895d8 ["CALLIND", null, ["register:0:8"]]
- 00889598 bytes 00013fd6
+ 008895d8 bytes 00013fd6
- 008895a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008895a8 ["INT_ADD", "register:40f0:8", ["const:8895a8:8", "const:4:8"]]
- 008895a8 ["CALLIND", null, ["register:0:8"]]
+ 008895e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008895e8 ["INT_ADD", "register:40f0:8", ["const:8895e8:8", "const:4:8"]]
+ 008895e8 ["CALLIND", null, ["register:0:8"]]
- 008895a8 bytes 00013fd6
+ 008895e8 bytes 00013fd6
- 008895c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008895c8 ["INT_ADD", "register:40f0:8", ["const:8895c8:8", "const:4:8"]]
- 008895c8 ["CALLIND", null, ["register:0:8"]]
+ 00889608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00889608 ["INT_ADD", "register:40f0:8", ["const:889608:8", "const:4:8"]]
+ 00889608 ["CALLIND", null, ["register:0:8"]]
- 008895c8 bytes 00013fd6
+ 00889608 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f544f67a91943dc1d7864e1407a9d6"></a>

### [`0088a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a348.md) → [`0088a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a388.md) FUN_0088a388

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b37760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a348.md#insn-0088a378) · [`0088a3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a348.md#insn-0088a3a4) · [`0088a3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a348.md#insn-0088a3d4)
- 新版 `0088a3b8`（命令位置の公開資料なし） · `0088a3e4`（命令位置の公開資料なし） · `0088a414`（命令位置の公開資料なし）

~~~diff
- 0088a378 ["INT_ADD", "register:40f0:8", ["const:88a378:8", "const:4:8"]]
- 0088a378 ["CALL", null, ["callee:00b37b88:8"]]
+ 0088a3b8 ["INT_ADD", "register:40f0:8", ["const:88a3b8:8", "const:4:8"]]
+ 0088a3b8 ["CALL", null, ["callee:00b37b88:8"]]
- 0088a378 bytes fab40a94
+ 0088a3b8 bytes f4b50a94
- 0088a3a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a3a4 ["INT_ADD", "register:40f0:8", ["const:88a3a4:8", "const:4:8"]]
- 0088a3a4 ["CALLIND", null, ["register:0:8"]]
+ 0088a3e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a3e4 ["INT_ADD", "register:40f0:8", ["const:88a3e4:8", "const:4:8"]]
+ 0088a3e4 ["CALLIND", null, ["register:0:8"]]
- 0088a3a4 bytes 00013fd6
+ 0088a3e4 bytes 00013fd6
- 0088a3d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a3d4 ["INT_ADD", "register:40f0:8", ["const:88a3d4:8", "const:4:8"]]
- 0088a3d4 ["CALLIND", null, ["register:0:8"]]
+ 0088a414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a414 ["INT_ADD", "register:40f0:8", ["const:88a414:8", "const:4:8"]]
+ 0088a414 ["CALLIND", null, ["register:0:8"]]
- 0088a3d4 bytes 00013fd6
+ 0088a414 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6db28234874205bc578a21a439c099a"></a>

### [`0088a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a4a0.md) → [`0088a4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a4e0.md) FUN_0088a4e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 5件 [`0088a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a5f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 5件 [`0088a630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a630.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a4a0.md#insn-0088a594) · [`0088a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a4a0.md#insn-0088a5bc) · [`0088a5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a4a0.md#insn-0088a5d0)
- 新版 `0088a5d4`（命令位置の公開資料なし） · `0088a5fc`（命令位置の公開資料なし） · `0088a610`（命令位置の公開資料なし）

~~~diff
- 0088a594 ["INT_ADD", "register:40f0:8", ["const:88a594:8", "const:4:8"]]
- 0088a594 ["CALL", null, ["callee:0088a630:8"]]
+ 0088a5d4 ["INT_ADD", "register:40f0:8", ["const:88a5d4:8", "const:4:8"]]
+ 0088a5d4 ["CALL", null, ["callee:0088a630:8"]]
- 0088a594 bytes 17000094
+ 0088a5d4 bytes 17000094
- 0088a5bc ["INT_ADD", "register:40f0:8", ["const:88a5bc:8", "const:4:8"]]
- 0088a5bc ["CALL", null, ["callee:00c53d00:8"]]
+ 0088a5fc ["INT_ADD", "register:40f0:8", ["const:88a5fc:8", "const:4:8"]]
+ 0088a5fc ["CALL", null, ["callee:00c53d00:8"]]
- 0088a5bc bytes c9240f94
+ 0088a5fc bytes c1250f94
- 0088a5d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a5d0 ["INT_ADD", "register:40f0:8", ["const:88a5d0:8", "const:4:8"]]
- 0088a5d0 ["CALLIND", null, ["register:0:8"]]
+ 0088a610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a610 ["INT_ADD", "register:40f0:8", ["const:88a610:8", "const:4:8"]]
+ 0088a610 ["CALLIND", null, ["register:0:8"]]
- 0088a5d0 bytes 00013fd6
+ 0088a610 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93df89f931d0e051a2423ae436522c28"></a>

### [`0088a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a724.md) → [`0088a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a764.md) FUN_0088a764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a724.md#insn-0088a754) · [`0088a768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a724.md#insn-0088a768) · [`0088a770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a724.md#insn-0088a770)
- 新版 `0088a794`（命令位置の公開資料なし） · `0088a7a8`（命令位置の公開資料なし） · `0088a7b0`（命令位置の公開資料なし）

~~~diff
- 0088a754 ["INT_ADD", "register:40f0:8", ["const:88a754:8", "const:4:8"]]
- 0088a754 ["CALL", null, ["callee:00c53d00:8"]]
+ 0088a794 ["INT_ADD", "register:40f0:8", ["const:88a794:8", "const:4:8"]]
+ 0088a794 ["CALL", null, ["callee:00c53d00:8"]]
- 0088a754 bytes 63240f94
+ 0088a794 bytes 5b250f94
- 0088a768 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088a768 ["INT_ADD", "register:40f0:8", ["const:88a768:8", "const:4:8"]]
- 0088a768 ["CALLIND", null, ["register:0:8"]]
+ 0088a7a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088a7a8 ["INT_ADD", "register:40f0:8", ["const:88a7a8:8", "const:4:8"]]
+ 0088a7a8 ["CALLIND", null, ["register:0:8"]]
- 0088a768 bytes 00013fd6
+ 0088a7a8 bytes 00013fd6
- 0088a770 ["INT_ADD", "register:40f0:8", ["const:88a770:8", "const:4:8"]]
- 0088a770 ["CALL", null, ["callee:00c57e80:8"]]
+ 0088a7b0 ["INT_ADD", "register:40f0:8", ["const:88a7b0:8", "const:4:8"]]
+ 0088a7b0 ["CALL", null, ["callee:00c57e80:8"]]
- 0088a770 bytes c4340f94
+ 0088a7b0 bytes b4350f94
~~~


<a id="compare-b760a6e211ac64646147f941a0fb0fa9"></a>

### [`0088a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8b0.md) → [`0088a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md) FUN_0088a8f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 4件 [`0088abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088abcc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 4件 [`0088ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8b0.md#insn-0088a994) · [`0088aa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8b0.md#insn-0088aa34) · [`0088aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8b0.md#insn-0088aa50)
- 新版 `0088a9d4`（命令位置の公開資料なし） · `0088aa74`（命令位置の公開資料なし） · `0088aa90`（命令位置の公開資料なし）

~~~diff
- 0088a994 ["INT_ADD", "register:40f0:8", ["const:88a994:8", "const:4:8"]]
- 0088a994 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088a9d4 ["INT_ADD", "register:40f0:8", ["const:88a9d4:8", "const:4:8"]]
+ 0088a9d4 ["CALL", null, ["callee:00c57e90:8"]]
- 0088a994 bytes 3f340f94
+ 0088a9d4 bytes 2f350f94
- 0088aa34 ["INT_ADD", "register:40f0:8", ["const:88aa34:8", "const:4:8"]]
- 0088aa34 ["CALL", null, ["callee:00c5a820:8"]]
+ 0088aa74 ["INT_ADD", "register:40f0:8", ["const:88aa74:8", "const:4:8"]]
+ 0088aa74 ["CALL", null, ["callee:00c5a820:8"]]
- 0088aa34 bytes 7b3e0f94
+ 0088aa74 bytes 6b3f0f94
- 0088aa50 ["INT_ADD", "register:40f0:8", ["const:88aa50:8", "const:4:8"]]
- 0088aa50 ["CALL", null, ["callee:0088ac0c:8"]]
+ 0088aa90 ["INT_ADD", "register:40f0:8", ["const:88aa90:8", "const:4:8"]]
+ 0088aa90 ["CALL", null, ["callee:0088ac0c:8"]]
- 0088aa50 bytes 5f000094
+ 0088aa90 bytes 5f000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6948152e59c93cf2e76e2064669921"></a>

### [`0088abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088abcc.md) → [`0088ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ac0c.md) FUN_0088ac0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8b0.md) · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0088a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8f0.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088abf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088abcc.md#insn-0088abf0) · [`0088ac04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088abcc.md#insn-0088ac04) · [`0088ac64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088abcc.md#insn-0088ac64)
- 新版 `0088ac30`（命令位置の公開資料なし） · `0088ac44`（命令位置の公開資料なし） · `0088aca4`（命令位置の公開資料なし）

~~~diff
- 0088abf0 ["INT_ADD", "register:40f0:8", ["const:88abf0:8", "const:4:8"]]
- 0088abf0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088ac30 ["INT_ADD", "register:40f0:8", ["const:88ac30:8", "const:4:8"]]
+ 0088ac30 ["CALL", null, ["callee:00c57e90:8"]]
- 0088abf0 bytes a8330f94
+ 0088ac30 bytes 98340f94
- 0088ac04 ["INT_ADD", "register:40f0:8", ["const:88ac04:8", "const:4:8"]]
- 0088ac04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088ac44 ["INT_ADD", "register:40f0:8", ["const:88ac44:8", "const:4:8"]]
+ 0088ac44 ["CALL", null, ["callee:00c57eb0:8"]]
- 0088ac04 bytes ab330f94
+ 0088ac44 bytes 9b340f94
- 0088ac64 ["INT_ADD", "register:40f0:8", ["const:88ac64:8", "const:4:8"]]
- 0088ac64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088aca4 ["INT_ADD", "register:40f0:8", ["const:88aca4:8", "const:4:8"]]
+ 0088aca4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0088ac64 bytes 93330f94
+ 0088aca4 bytes 83340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9f268842df2add7b0f12b49ad40ac4d"></a>

### [`0088b900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b900.md) → [`0088b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b940.md) FUN_0088b940

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088b954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b900.md#insn-0088b954) · [`0088b988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b900.md#insn-0088b988) · [`0088b98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b900.md#insn-0088b98c)
- 新版 `0088b994`（命令位置の公開資料なし） · `0088b9c8`（命令位置の公開資料なし） · `0088b9cc`（命令位置の公開資料なし）

~~~diff
- 0088b954 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088b954 ["INT_ADD", "register:40f0:8", ["const:88b954:8", "const:4:8"]]
- 0088b954 ["CALLIND", null, ["register:0:8"]]
+ 0088b994 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088b994 ["INT_ADD", "register:40f0:8", ["const:88b994:8", "const:4:8"]]
+ 0088b994 ["CALLIND", null, ["register:0:8"]]
- 0088b954 bytes 00013fd6
+ 0088b994 bytes 00013fd6
- 0088b988 ["INT_ADD", "register:40f0:8", ["const:88b988:8", "const:4:8"]]
- 0088b988 ["CALL", null, ["callee:00459d74:8"]]
+ 0088b9c8 ["INT_ADD", "register:40f0:8", ["const:88b9c8:8", "const:4:8"]]
+ 0088b9c8 ["CALL", null, ["callee:00459d74:8"]]
- 0088b988 bytes eb38ef97
+ 0088b9c8 bytes eb38ef97
- 0088b98c ["INT_ADD", "register:40f0:8", ["const:88b98c:8", "const:4:8"]]
- 0088b98c ["CALL", null, ["callee:00c57ee0:8"]]
+ 0088b9cc ["INT_ADD", "register:40f0:8", ["const:88b9cc:8", "const:4:8"]]
+ 0088b9cc ["CALL", null, ["callee:00c57ee0:8"]]
- 0088b98c bytes 55300f94
+ 0088b9cc bytes 45310f94
~~~


<a id="compare-32f17d01d4ebcb153151285ed3469898"></a>

### [`0088ba10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba10.md) → [`0088ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba50.md) FUN_0088ba50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba10.md#insn-0088ba50) · [`0088ba84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba10.md#insn-0088ba84) · [`0088ba88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088ba10.md#insn-0088ba88)
- 新版 `0088ba90`（命令位置の公開資料なし） · `0088bac4`（命令位置の公開資料なし） · `0088bac8`（命令位置の公開資料なし）

~~~diff
- 0088ba50 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088ba50 ["INT_ADD", "register:40f0:8", ["const:88ba50:8", "const:4:8"]]
- 0088ba50 ["CALLIND", null, ["register:0:8"]]
+ 0088ba90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088ba90 ["INT_ADD", "register:40f0:8", ["const:88ba90:8", "const:4:8"]]
+ 0088ba90 ["CALLIND", null, ["register:0:8"]]
- 0088ba50 bytes 00013fd6
+ 0088ba90 bytes 00013fd6
- 0088ba84 ["INT_ADD", "register:40f0:8", ["const:88ba84:8", "const:4:8"]]
- 0088ba84 ["CALL", null, ["callee:00459d74:8"]]
+ 0088bac4 ["INT_ADD", "register:40f0:8", ["const:88bac4:8", "const:4:8"]]
+ 0088bac4 ["CALL", null, ["callee:00459d74:8"]]
- 0088ba84 bytes ac38ef97
+ 0088bac4 bytes ac38ef97
- 0088ba88 ["INT_ADD", "register:40f0:8", ["const:88ba88:8", "const:4:8"]]
- 0088ba88 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0088bac8 ["INT_ADD", "register:40f0:8", ["const:88bac8:8", "const:4:8"]]
+ 0088bac8 ["CALL", null, ["callee:00c57ee0:8"]]
- 0088ba88 bytes 16300f94
+ 0088bac8 bytes 06310f94
~~~


<a id="compare-95b994aa864295b9a774aa9edbf46765"></a>

### [`0088bb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bb08.md) → [`0088bb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb48.md) FUN_0088bb48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088bb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bb08.md#insn-0088bb2c)
- 新版 `0088bb6c`（命令位置の公開資料なし）

~~~diff
- 0088bb2c ["INT_ADD", "register:40f0:8", ["const:88bb2c:8", "const:4:8"]]
- 0088bb2c ["CALL", null, ["callee:00459d74:8"]]
+ 0088bb6c ["INT_ADD", "register:40f0:8", ["const:88bb6c:8", "const:4:8"]]
+ 0088bb6c ["CALL", null, ["callee:00459d74:8"]]
- 0088bb2c bytes 8238ef97
+ 0088bb6c bytes 8238ef97
~~~


<a id="compare-211b96e7aef17f19728518614ff7d196"></a>

### [`0088bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md) → [`0088bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md) FUN_0088bbec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00b375f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md) [`00b37760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b37760.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00b37a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37a18.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088bbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md#insn-0088bbd4) · [`0088bbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md#insn-0088bbf0) · [`0088bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md#insn-0088bc1c)
- 新版 `0088bc14`（命令位置の公開資料なし） · `0088bc30`（命令位置の公開資料なし） · `0088bc5c`（命令位置の公開資料なし）

~~~diff
- 0088bbd4 ["INT_ADD", "register:40f0:8", ["const:88bbd4:8", "const:4:8"]]
- 0088bbd4 ["CALL", null, ["callee:00b37a18:8"]]
+ 0088bc14 ["INT_ADD", "register:40f0:8", ["const:88bc14:8", "const:4:8"]]
+ 0088bc14 ["CALL", null, ["callee:00b37a18:8"]]
- 0088bbd4 bytes 87ae0a94
+ 0088bc14 bytes 81af0a94
- 0088bbf0 ["INT_ADD", "register:40f0:8", ["const:88bbf0:8", "const:4:8"]]
- 0088bbf0 ["CALL", null, ["callee:00b37b88:8"]]
+ 0088bc30 ["INT_ADD", "register:40f0:8", ["const:88bc30:8", "const:4:8"]]
+ 0088bc30 ["CALL", null, ["callee:00b37b88:8"]]
- 0088bbf0 bytes dcae0a94
+ 0088bc30 bytes d6af0a94
- 0088bc1c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088bc1c ["INT_ADD", "register:40f0:8", ["const:88bc1c:8", "const:4:8"]]
- 0088bc1c ["CALLIND", null, ["register:0:8"]]
+ 0088bc5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088bc5c ["INT_ADD", "register:40f0:8", ["const:88bc5c:8", "const:4:8"]]
+ 0088bc5c ["CALLIND", null, ["register:0:8"]]
- 0088bc1c bytes 00013fd6
+ 0088bc5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98d9023a07e6653370e38ce1599dfe8"></a>

### [`0088ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088ee80.md) → [`0088eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088e/0088eec0.md) FUN_0088eec0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088ef30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088ee80.md#insn-0088ef30) · [`0088ef84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088ee80.md#insn-0088ef84) · [`0088ef98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088ee80.md#insn-0088ef98)
- 新版 `0088ef70`（命令位置の公開資料なし） · `0088efc4`（命令位置の公開資料なし） · `0088efd8`（命令位置の公開資料なし）

~~~diff
- 0088ef30 ["INT_ADD", "register:40f0:8", ["const:88ef30:8", "const:4:8"]]
- 0088ef30 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088ef70 ["INT_ADD", "register:40f0:8", ["const:88ef70:8", "const:4:8"]]
+ 0088ef70 ["CALL", null, ["callee:00c57e90:8"]]
- 0088ef30 bytes d8220f94
+ 0088ef70 bytes c8230f94
- 0088ef84 ["INT_ADD", "register:40f0:8", ["const:88ef84:8", "const:4:8"]]
- 0088ef84 ["CALL", null, ["callee:00c58000:8"]]
+ 0088efc4 ["INT_ADD", "register:40f0:8", ["const:88efc4:8", "const:4:8"]]
+ 0088efc4 ["CALL", null, ["callee:00c58000:8"]]
- 0088ef84 bytes 1f230f94
+ 0088efc4 bytes 0f240f94
- 0088ef98 ["INT_ADD", "register:40f0:8", ["const:88ef98:8", "const:4:8"]]
- 0088ef98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088efd8 ["INT_ADD", "register:40f0:8", ["const:88efd8:8", "const:4:8"]]
+ 0088efd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0088ef98 bytes c6220f94
+ 0088efd8 bytes b6230f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331391d1cc2e5908f7f387d8d26d4b03"></a>

### [`0088efc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088efc0.md) → [`0088f000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f000.md) FUN_0088f000

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088efc0.md#insn-0088f004)
- 新版 `0088f044`（命令位置の公開資料なし）

~~~diff
- 0088f004 ["INT_ADD", "register:40f0:8", ["const:88f004:8", "const:4:8"]]
- 0088f004 ["CALL", null, ["callee:00c58050:8"]]
+ 0088f044 ["INT_ADD", "register:40f0:8", ["const:88f044:8", "const:4:8"]]
+ 0088f044 ["CALL", null, ["callee:00c58050:8"]]
- 0088f004 bytes 13230f94
+ 0088f044 bytes 03240f94
~~~


<a id="compare-6cc57fd2592e745b9edfc86ebc64872a"></a>

### [`0088f080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md) → [`0088f0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f0c0.md) FUN_0088f0c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0063947c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/0063947c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md#insn-0088f0b4) · [`0088f0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md#insn-0088f0c8) · [`0088f118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md#insn-0088f118)
- 新版 `0088f0f4`（命令位置の公開資料なし） · `0088f108`（命令位置の公開資料なし） · `0088f158`（命令位置の公開資料なし）

~~~diff
- 0088f0b4 ["INT_ADD", "register:40f0:8", ["const:88f0b4:8", "const:4:8"]]
- 0088f0b4 ["CALL", null, ["callee:006394bc:8"]]
+ 0088f0f4 ["INT_ADD", "register:40f0:8", ["const:88f0f4:8", "const:4:8"]]
+ 0088f0f4 ["CALL", null, ["callee:006394bc:8"]]
- 0088f0b4 bytes f2a8f697
+ 0088f0f4 bytes f2a8f697
- 0088f0c8 ["INT_ADD", "register:40f0:8", ["const:88f0c8:8", "const:4:8"]]
- 0088f0c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088f108 ["INT_ADD", "register:40f0:8", ["const:88f108:8", "const:4:8"]]
+ 0088f108 ["CALL", null, ["callee:00c57e90:8"]]
- 0088f0c8 bytes 72220f94
+ 0088f108 bytes 62230f94
- 0088f118 ["INT_ADD", "register:40f0:8", ["const:88f118:8", "const:4:8"]]
- 0088f118 ["CALL", null, ["callee:0043bba4:8"]]
+ 0088f158 ["INT_ADD", "register:40f0:8", ["const:88f158:8", "const:4:8"]]
+ 0088f158 ["CALL", null, ["callee:0043bba4:8"]]
- 0088f118 bytes 93b2ee97
+ 0088f158 bytes 93b2ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507cfa6d2ba651e0327939fba4efa902"></a>

### [`0088f158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f158.md) → [`0088f198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f198.md) FUN_0088f198

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f158.md#insn-0088f1d0) · [`0088f1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f158.md#insn-0088f1f8)
- 新版 `0088f210`（命令位置の公開資料なし） · `0088f238`（命令位置の公開資料なし）

~~~diff
- 0088f1d0 ["INT_ADD", "register:40f0:8", ["const:88f1d0:8", "const:4:8"]]
- 0088f1d0 ["CALL", null, ["callee:00c58050:8"]]
+ 0088f210 ["INT_ADD", "register:40f0:8", ["const:88f210:8", "const:4:8"]]
+ 0088f210 ["CALL", null, ["callee:00c58050:8"]]
- 0088f1d0 bytes a0220f94
+ 0088f210 bytes 90230f94
- 0088f1f8 ["INT_ADD", "register:40f0:8", ["const:88f1f8:8", "const:4:8"]]
- 0088f1f8 ["CALL", null, ["callee:00c58050:8"]]
+ 0088f238 ["INT_ADD", "register:40f0:8", ["const:88f238:8", "const:4:8"]]
+ 0088f238 ["CALL", null, ["callee:00c58050:8"]]
- 0088f1f8 bytes 96220f94
+ 0088f238 bytes 86230f94
~~~


<a id="compare-0931d3545bb37363bd6817ff20e27246"></a>

### [`0088f2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md) → [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) FUN_0088f2f4

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 2件 [`0046d66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d66c.md) [`005642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005642a0.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 2件 [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md) [`005642e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005642e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md#insn-0088f2c4) · [`0088f2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2b4.md#insn-0088f2dc)
- 新版 `0088f304`（命令位置の公開資料なし） · `0088f31c`（命令位置の公開資料なし）

~~~diff
- 0088f2c4 ["INT_ADD", "register:40f0:8", ["const:88f2c4:8", "const:4:8"]]
- 0088f2c4 ["CALL", null, ["callee:0046d6ac:8"]]
+ 0088f304 ["INT_ADD", "register:40f0:8", ["const:88f304:8", "const:4:8"]]
+ 0088f304 ["CALL", null, ["callee:0046d6ac:8"]]
- 0088f2c4 bytes ea78ef97
+ 0088f304 bytes ea78ef97
- 0088f2dc ["INT_ADD", "register:40f0:8", ["const:88f2dc:8", "const:4:8"]]
- 0088f2dc ["CALL", null, ["callee:005642e0:8"]]
+ 0088f31c ["INT_ADD", "register:40f0:8", ["const:88f31c:8", "const:4:8"]]
+ 0088f31c ["CALL", null, ["callee:005642e0:8"]]
- 0088f2dc bytes f153f397
+ 0088f31c bytes f153f397
~~~


<a id="compare-43f9aa44d16eb1b7f824385ebb3d0272"></a>

### [`0088f2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2f8.md) → [`0088f338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f338.md) FUN_0088f338

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 1件 [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)
- 新版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 1件 [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2f8.md#insn-0088f31c)
- 新版 `0088f35c`（命令位置の公開資料なし）

~~~diff
- 0088f31c ["INT_ADD", "register:40f0:8", ["const:88f31c:8", "const:4:8"]]
- 0088f31c ["CALL", null, ["callee:00c5a8f0:8"]]
+ 0088f35c ["INT_ADD", "register:40f0:8", ["const:88f35c:8", "const:4:8"]]
+ 0088f35c ["CALL", null, ["callee:00c5a8f0:8"]]
- 0088f31c bytes 752c0f94
+ 0088f35c bytes 652d0f94
~~~


<a id="compare-4f2376421737a47a5bab7231ee139fca"></a>

### [`0088f340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f340.md) → [`0088f380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f380.md) FUN_0088f380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f340.md#insn-0088f384) · [`0088f394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f340.md#insn-0088f394) · [`0088f3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f340.md#insn-0088f3a0)
- 新版 `0088f3c4`（命令位置の公開資料なし） · `0088f3d4`（命令位置の公開資料なし） · `0088f3e0`（命令位置の公開資料なし）

~~~diff
- 0088f384 ["INT_ADD", "register:40f0:8", ["const:88f384:8", "const:4:8"]]
- 0088f384 ["CALL", null, ["callee:00c5a830:8"]]
+ 0088f3c4 ["INT_ADD", "register:40f0:8", ["const:88f3c4:8", "const:4:8"]]
+ 0088f3c4 ["CALL", null, ["callee:00c5a830:8"]]
- 0088f384 bytes 2b2c0f94
+ 0088f3c4 bytes 1b2d0f94
- 0088f394 ["INT_ADD", "register:40f0:8", ["const:88f394:8", "const:4:8"]]
- 0088f394 ["CALL", null, ["callee:00c5a840:8"]]
+ 0088f3d4 ["INT_ADD", "register:40f0:8", ["const:88f3d4:8", "const:4:8"]]
+ 0088f3d4 ["CALL", null, ["callee:00c5a840:8"]]
- 0088f394 bytes 2b2c0f94
+ 0088f3d4 bytes 1b2d0f94
- 0088f3a0 ["INT_ADD", "register:40f0:8", ["const:88f3a0:8", "const:4:8"]]
- 0088f3a0 ["CALL", null, ["callee:00c5a830:8"]]
+ 0088f3e0 ["INT_ADD", "register:40f0:8", ["const:88f3e0:8", "const:4:8"]]
+ 0088f3e0 ["CALL", null, ["callee:00c5a830:8"]]
- 0088f3a0 bytes 242c0f94
+ 0088f3e0 bytes 142d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a923730f46204689660ee06c3f0bb9e"></a>

### [`0088fa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa94.md) → [`0088fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fad8.md) FUN_0088fad8

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa94.md#insn-0088fab0) · [`0088fad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa94.md#insn-0088fad0)
- 新版 `0088faf4`（命令位置の公開資料なし） · `0088fb14`（命令位置の公開資料なし）

~~~diff
- 0088fab0 ["INT_ADD", "register:40f0:8", ["const:88fab0:8", "const:4:8"]]
- 0088fab0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0088faf4 ["INT_ADD", "register:40f0:8", ["const:88faf4:8", "const:4:8"]]
+ 0088faf4 ["CALL", null, ["callee:00c53d00:8"]]
- 0088fab0 bytes 8c0f0f94
+ 0088faf4 bytes 83100f94
- 0088fad0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fad0 ["INT_ADD", "register:40f0:8", ["const:88fad0:8", "const:4:8"]]
- 0088fad0 ["CALLIND", null, ["register:0:8"]]
+ 0088fb14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fb14 ["INT_ADD", "register:40f0:8", ["const:88fb14:8", "const:4:8"]]
+ 0088fb14 ["CALLIND", null, ["register:0:8"]]
- 0088fad0 bytes 00013fd6
+ 0088fb14 bytes 00013fd6
~~~


<a id="compare-aa6cdb10540c1c89e178781c34da75d9"></a>

### [`0088fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md) → [`0088fc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md) FUN_0088fc64

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md#insn-0088fc3c) · [`0088fc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md#insn-0088fc5c)
- 新版 `0088fc80`（命令位置の公開資料なし） · `0088fca0`（命令位置の公開資料なし）

~~~diff
- 0088fc3c ["INT_ADD", "register:40f0:8", ["const:88fc3c:8", "const:4:8"]]
- 0088fc3c ["CALL", null, ["callee:00c53d00:8"]]
+ 0088fc80 ["INT_ADD", "register:40f0:8", ["const:88fc80:8", "const:4:8"]]
+ 0088fc80 ["CALL", null, ["callee:00c53d00:8"]]
- 0088fc3c bytes 290f0f94
+ 0088fc80 bytes 20100f94
- 0088fc5c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fc5c ["INT_ADD", "register:40f0:8", ["const:88fc5c:8", "const:4:8"]]
- 0088fc5c ["CALLIND", null, ["register:0:8"]]
+ 0088fca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fca0 ["INT_ADD", "register:40f0:8", ["const:88fca0:8", "const:4:8"]]
+ 0088fca0 ["CALLIND", null, ["register:0:8"]]
- 0088fc5c bytes 00013fd6
+ 0088fca0 bytes 00013fd6
~~~


<a id="compare-1985a9cde087799871adce8f552e3901"></a>

### [`0088fc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc70.md) → [`0088fcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fcb4.md) FUN_0088fcb4

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0088f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088fc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc70.md#insn-0088fc90) · [`0088fca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc70.md#insn-0088fca4) · [`0088fcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc70.md#insn-0088fcac)
- 新版 `0088fcd4`（命令位置の公開資料なし） · `0088fce8`（命令位置の公開資料なし） · `0088fcf0`（命令位置の公開資料なし）

~~~diff
- 0088fc90 ["INT_ADD", "register:40f0:8", ["const:88fc90:8", "const:4:8"]]
- 0088fc90 ["CALL", null, ["callee:00c53d00:8"]]
+ 0088fcd4 ["INT_ADD", "register:40f0:8", ["const:88fcd4:8", "const:4:8"]]
+ 0088fcd4 ["CALL", null, ["callee:00c53d00:8"]]
- 0088fc90 bytes 140f0f94
+ 0088fcd4 bytes 0b100f94
- 0088fca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fca4 ["INT_ADD", "register:40f0:8", ["const:88fca4:8", "const:4:8"]]
- 0088fca4 ["CALLIND", null, ["register:0:8"]]
+ 0088fce8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fce8 ["INT_ADD", "register:40f0:8", ["const:88fce8:8", "const:4:8"]]
+ 0088fce8 ["CALLIND", null, ["register:0:8"]]
- 0088fca4 bytes 00013fd6
+ 0088fce8 bytes 00013fd6
- 0088fcac ["INT_ADD", "register:40f0:8", ["const:88fcac:8", "const:4:8"]]
- 0088fcac ["CALL", null, ["callee:00c57e80:8"]]
+ 0088fcf0 ["INT_ADD", "register:40f0:8", ["const:88fcf0:8", "const:4:8"]]
+ 0088fcf0 ["CALL", null, ["callee:00c57e80:8"]]
- 0088fcac bytes 751f0f94
+ 0088fcf0 bytes 64200f94
~~~


<a id="compare-0ec7eed2f3f1bcc90126950f14934627"></a>

### [`00890cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890cd4.md) → [`00890d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d18.md) FUN_00890d18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00890d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890cd4.md#insn-00890d24) · [`00890d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890cd4.md#insn-00890d34)
- 新版 `00890d68`（命令位置の公開資料なし） · `00890d78`（命令位置の公開資料なし）

~~~diff
- 00890d24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890d24 ["INT_ADD", "register:40f0:8", ["const:890d24:8", "const:4:8"]]
- 00890d24 ["CALLIND", null, ["register:0:8"]]
+ 00890d68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890d68 ["INT_ADD", "register:40f0:8", ["const:890d68:8", "const:4:8"]]
+ 00890d68 ["CALLIND", null, ["register:0:8"]]
- 00890d24 bytes 00013fd6
+ 00890d68 bytes 00013fd6
- 00890d34 ["INT_ADD", "register:40f0:8", ["const:890d34:8", "const:4:8"]]
- 00890d34 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00890d78 ["INT_ADD", "register:40f0:8", ["const:890d78:8", "const:4:8"]]
+ 00890d78 ["CALL", null, ["callee:00c57eb0:8"]]
- 00890d34 bytes 5f1b0f94
+ 00890d78 bytes 4e1c0f94
~~~


<a id="compare-afc5cd2ed01b9dea7172af5c6782f2be"></a>

### [`00892e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e34.md) → [`00892e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892e78.md) FUN_00892e78

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00892e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e34.md#insn-00892e54)
- 新版 `00892e98`（命令位置の公開資料なし）

~~~diff
- 00892e54 ["INT_ADD", "register:40f0:8", ["const:892e54:8", "const:4:8"]]
- 00892e54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00892e98 ["INT_ADD", "register:40f0:8", ["const:892e98:8", "const:4:8"]]
+ 00892e98 ["CALL", null, ["callee:00c57eb0:8"]]
- 00892e54 bytes 17130f94
+ 00892e98 bytes 06140f94
~~~


<a id="compare-f0c728f4d75a61fe9d70d3e87969739e"></a>

### [`008933a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008933a4.md) → [`008933e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008933e8.md) FUN_008933e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008bb4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4cc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008bb510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008933c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008933a4.md#insn-008933c0) · [`008933cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008933a4.md#insn-008933cc) · [`008933d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008933a4.md#insn-008933d4)
- 新版 `00893404`（命令位置の公開資料なし） · `00893410`（命令位置の公開資料なし） · `00893418`（命令位置の公開資料なし）

~~~diff
- 008933c0 ["INT_ADD", "register:40f0:8", ["const:8933c0:8", "const:4:8"]]
- 008933c0 ["CALL", null, ["callee:008514f8:8"]]
+ 00893404 ["INT_ADD", "register:40f0:8", ["const:893404:8", "const:4:8"]]
+ 00893404 ["CALL", null, ["callee:008514f8:8"]]
- 008933c0 bytes 3ef8fe97
+ 00893404 bytes 3df8fe97
- 008933cc ["INT_ADD", "register:40f0:8", ["const:8933cc:8", "const:4:8"]]
- 008933cc ["CALL", null, ["callee:008bb510:8"]]
+ 00893410 ["INT_ADD", "register:40f0:8", ["const:893410:8", "const:4:8"]]
+ 00893410 ["CALL", null, ["callee:008bb510:8"]]
- 008933cc bytes 40a00094
+ 00893410 bytes 40a00094
- 008933d4 ["INT_ADD", "register:40f0:8", ["const:8933d4:8", "const:4:8"]]
- 008933d4 ["CALL", null, ["callee:008514f8:8"]]
+ 00893418 ["INT_ADD", "register:40f0:8", ["const:893418:8", "const:4:8"]]
+ 00893418 ["CALL", null, ["callee:008514f8:8"]]
- 008933d4 bytes 39f8fe97
+ 00893418 bytes 38f8fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efbd8e7a42d8f5dc03a0eca4c406552"></a>

### [`008976ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/008976ac.md) → [`008976f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/008976f0.md) FUN_008976f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00897714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/008976ac.md#insn-00897714) · [`00897754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/008976ac.md#insn-00897754)
- 新版 `00897758`（命令位置の公開資料なし） · `00897798`（命令位置の公開資料なし）

~~~diff
- 00897714 ["INT_ADD", "register:40f0:8", ["const:897714:8", "const:4:8"]]
- 00897714 ["CALL", null, ["callee:00c57e90:8"]]
+ 00897758 ["INT_ADD", "register:40f0:8", ["const:897758:8", "const:4:8"]]
+ 00897758 ["CALL", null, ["callee:00c57e90:8"]]
- 00897714 bytes df000f94
+ 00897758 bytes ce010f94
- 00897754 ["INT_ADD", "register:40f0:8", ["const:897754:8", "const:4:8"]]
- 00897754 ["CALL", null, ["callee:0043bba4:8"]]
+ 00897798 ["INT_ADD", "register:40f0:8", ["const:897798:8", "const:4:8"]]
+ 00897798 ["CALL", null, ["callee:0043bba4:8"]]
- 00897754 bytes 0491ee97
+ 00897798 bytes 0391ee97
~~~


<a id="compare-92697f49eb4ab416ab2e36d685233bff"></a>

### [`0089777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md) → [`008977c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/008977c0.md) FUN_008977c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 2件 [`008a40c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 2件 [`008a4108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4108.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008977f4",
      "incomplete_value": true,
      "site": "008977fc",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008977b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md#insn-008977b8) · [`008977e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md#insn-008977e4) · [`008977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md#insn-008977f4)
- 新版 `008977fc`（命令位置の公開資料なし） · `00897828`（命令位置の公開資料なし） · `00897838`（命令位置の公開資料なし）

~~~diff
- 008977b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 008977b8 ["INT_ADD", "register:40f0:8", ["const:8977b8:8", "const:4:8"]]
- 008977b8 ["CALLIND", null, ["register:0:8"]]
+ 008977fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 008977fc ["INT_ADD", "register:40f0:8", ["const:8977fc:8", "const:4:8"]]
+ 008977fc ["CALLIND", null, ["register:0:8"]]
- 008977b8 bytes 20013fd6
+ 008977fc bytes 20013fd6
- 008977e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008977e4 ["INT_ADD", "register:40f0:8", ["const:8977e4:8", "const:4:8"]]
- 008977e4 ["CALLIND", null, ["register:0:8"]]
+ 00897828 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00897828 ["INT_ADD", "register:40f0:8", ["const:897828:8", "const:4:8"]]
+ 00897828 ["CALLIND", null, ["register:0:8"]]
- 008977e4 bytes 00013fd6
+ 00897828 bytes 00013fd6
- 008977f4 ["INT_ADD", "register:40f0:8", ["const:8977f4:8", "const:4:8"]]
- 008977f4 ["CALL", null, ["callee:008a4108:8"]]
+ 00897838 ["INT_ADD", "register:40f0:8", ["const:897838:8", "const:4:8"]]
+ 00897838 ["CALL", null, ["callee:008a4108:8"]]
- 008977f4 bytes 34320094
+ 00897838 bytes 34320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beeac1e96fd7cadf562364025cef0c31"></a>

### [`008a3cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3cb8.md) → [`008a3cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3cfc.md) FUN_008a3cfc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a3cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3cb8.md#insn-008a3cf0)
- 新版 `008a3d34`（命令位置の公開資料なし）

~~~diff
- 008a3cf0 ["INT_ADD", "register:40f0:8", ["const:8a3cf0:8", "const:4:8"]]
- 008a3cf0 ["CALL", null, ["callee:00748b30:8"]]
+ 008a3d34 ["INT_ADD", "register:40f0:8", ["const:8a3d34:8", "const:4:8"]]
+ 008a3d34 ["CALL", null, ["callee:00748b30:8"]]
- 008a3cf0 bytes 8093fa97
+ 008a3d34 bytes 7f93fa97
~~~


<a id="compare-0408d7235b2fc5701f80e308f3a98a78"></a>

### [`008ab818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab818.md) → [`008ab85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab85c.md) FUN_008ab85c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ab830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab818.md#insn-008ab830)
- 新版 `008ab874`（命令位置の公開資料なし）

~~~diff
- 008ab830 ["INT_ADD", "register:40f0:8", ["const:8ab830:8", "const:4:8"]]
- 008ab830 ["CALL", null, ["callee:005c179c:8"]]
+ 008ab874 ["INT_ADD", "register:40f0:8", ["const:8ab874:8", "const:4:8"]]
+ 008ab874 ["CALL", null, ["callee:005c179c:8"]]
- 008ab830 bytes cb57f497
+ 008ab874 bytes ca57f497
~~~


<a id="compare-1e7334c1f8741475fc09c0c8e7678d53"></a>

### [`008ab8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md) → [`008ab8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab8e8.md) FUN_008ab8e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ab8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md#insn-008ab8c4) · [`008ab8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md#insn-008ab8c8) · [`008ab8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md#insn-008ab8d8)
- 新版 `008ab908`（命令位置の公開資料なし） · `008ab90c`（命令位置の公開資料なし） · `008ab91c`（命令位置の公開資料なし）

~~~diff
- 008ab8c4 ["INT_ADD", "register:40f0:8", ["const:8ab8c4:8", "const:4:8"]]
- 008ab8c4 ["CALL", null, ["callee:0058fb80:8"]]
+ 008ab908 ["INT_ADD", "register:40f0:8", ["const:8ab908:8", "const:4:8"]]
+ 008ab908 ["CALL", null, ["callee:0058fb80:8"]]
- 008ab8c4 bytes 9f90f397
+ 008ab908 bytes 9e90f397
- 008ab8c8 ["INT_ADD", "register:40f0:8", ["const:8ab8c8:8", "const:4:8"]]
- 008ab8c8 ["CALL", null, ["callee:008514f8:8"]]
+ 008ab90c ["INT_ADD", "register:40f0:8", ["const:8ab90c:8", "const:4:8"]]
+ 008ab90c ["CALL", null, ["callee:008514f8:8"]]
- 008ab8c8 bytes fc96fe97
+ 008ab90c bytes fb96fe97
- 008ab8d8 ["INT_ADD", "register:40f0:8", ["const:8ab8d8:8", "const:4:8"]]
- 008ab8d8 ["CALL", null, ["callee:008514f8:8"]]
+ 008ab91c ["INT_ADD", "register:40f0:8", ["const:8ab91c:8", "const:4:8"]]
+ 008ab91c ["CALL", null, ["callee:008514f8:8"]]
- 008ab8d8 bytes f896fe97
+ 008ab91c bytes f796fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b9c5196b6b3009427c895c1bc4f7a7"></a>

### [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) → [`008b09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b09d8.md) FUN_008b09d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) · 呼出先 3件 [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) [`008b09e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`008b09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b09d8.md) · 呼出先 3件 [`008b09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b09d8.md) [`008b0a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0a28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b09b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md#insn-008b09b4) · [`008b09c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md#insn-008b09c0) · [`008b09cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md#insn-008b09cc)
- 新版 `008b09f8`（命令位置の公開資料なし） · `008b0a04`（命令位置の公開資料なし） · `008b0a10`（命令位置の公開資料なし）

~~~diff
- 008b09b4 ["INT_ADD", "register:40f0:8", ["const:8b09b4:8", "const:4:8"]]
- 008b09b4 ["CALL", null, ["local:b0:8"]]
+ 008b09f8 ["INT_ADD", "register:40f0:8", ["const:8b09f8:8", "const:4:8"]]
+ 008b09f8 ["CALL", null, ["local:b0:8"]]
- 008b09b4 bytes f8ffff97
+ 008b09f8 bytes f8ffff97
- 008b09c0 ["INT_ADD", "register:40f0:8", ["const:8b09c0:8", "const:4:8"]]
- 008b09c0 ["CALL", null, ["local:b0:8"]]
+ 008b0a04 ["INT_ADD", "register:40f0:8", ["const:8b0a04:8", "const:4:8"]]
+ 008b0a04 ["CALL", null, ["local:b0:8"]]
- 008b09c0 bytes f5ffff97
+ 008b0a04 bytes f5ffff97
- 008b09cc ["INT_ADD", "register:40f0:8", ["const:8b09cc:8", "const:4:8"]]
- 008b09cc ["CALL", null, ["callee:008b0a28:8"]]
+ 008b0a10 ["INT_ADD", "register:40f0:8", ["const:8b0a10:8", "const:4:8"]]
+ 008b0a10 ["CALL", null, ["callee:008b0a28:8"]]
- 008b09cc bytes 06000094
+ 008b0a10 bytes 06000094
~~~


<a id="compare-837b2d996b85f3a0e4069f2432ab4738"></a>

### [`008b09e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md) → [`008b0a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0a28.md) FUN_008b0a28

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) [`008b09e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md) · 呼出先 2件 [`008b09e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`008b09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b09d8.md) [`008b0a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0a28.md) · 呼出先 2件 [`008b0a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0a28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b0a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md#insn-008b0a04) · [`008b0a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md#insn-008b0a10)
- 新版 `008b0a48`（命令位置の公開資料なし） · `008b0a54`（命令位置の公開資料なし）

~~~diff
- 008b0a04 ["INT_ADD", "register:40f0:8", ["const:8b0a04:8", "const:4:8"]]
- 008b0a04 ["CALL", null, ["local:b0:8"]]
+ 008b0a48 ["INT_ADD", "register:40f0:8", ["const:8b0a48:8", "const:4:8"]]
+ 008b0a48 ["CALL", null, ["local:b0:8"]]
- 008b0a04 bytes f8ffff97
+ 008b0a48 bytes f8ffff97
- 008b0a10 ["INT_ADD", "register:40f0:8", ["const:8b0a10:8", "const:4:8"]]
- 008b0a10 ["CALL", null, ["local:b0:8"]]
+ 008b0a54 ["INT_ADD", "register:40f0:8", ["const:8b0a54:8", "const:4:8"]]
+ 008b0a54 ["CALL", null, ["local:b0:8"]]
- 008b0a10 bytes f5ffff97
+ 008b0a54 bytes f5ffff97
~~~


<a id="compare-60297a7a026a25ae3075474590fffb91"></a>

### [`008b6ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ce0.md) → [`008b6d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d24.md) FUN_008b6d24

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md) · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ce0.md#insn-008b6d1c) · [`008b6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ce0.md#insn-008b6d50) · [`008b6d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ce0.md#insn-008b6d54)
- 新版 `008b6d60`（命令位置の公開資料なし） · `008b6d94`（命令位置の公開資料なし） · `008b6d98`（命令位置の公開資料なし）

~~~diff
- 008b6d1c ["COPY", "register:0:8", ["register:4040:8"]]
- 008b6d1c ["INT_ADD", "register:40f0:8", ["const:8b6d1c:8", "const:4:8"]]
- 008b6d1c ["CALLIND", null, ["register:0:8"]]
+ 008b6d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b6d60 ["INT_ADD", "register:40f0:8", ["const:8b6d60:8", "const:4:8"]]
+ 008b6d60 ["CALLIND", null, ["register:0:8"]]
- 008b6d1c bytes 00013fd6
+ 008b6d60 bytes 00013fd6
- 008b6d50 ["INT_ADD", "register:40f0:8", ["const:8b6d50:8", "const:4:8"]]
- 008b6d50 ["CALL", null, ["callee:00459d74:8"]]
+ 008b6d94 ["INT_ADD", "register:40f0:8", ["const:8b6d94:8", "const:4:8"]]
+ 008b6d94 ["CALL", null, ["callee:00459d74:8"]]
- 008b6d50 bytes f98bee97
+ 008b6d94 bytes f88bee97
- 008b6d54 ["INT_ADD", "register:40f0:8", ["const:8b6d54:8", "const:4:8"]]
- 008b6d54 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008b6d98 ["INT_ADD", "register:40f0:8", ["const:8b6d98:8", "const:4:8"]]
+ 008b6d98 ["CALL", null, ["callee:00c57ee0:8"]]
- 008b6d54 bytes 63830e94
+ 008b6d98 bytes 52840e94
~~~


<a id="compare-d339f2d0570ba4f3b71eade1a0cce634"></a>

### [`008b6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md) → [`008b6ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ec4.md) FUN_008b6ec4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00786c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md) · 呼出先 1件 [`00813f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813f98.md)
- 新版 呼出元 1件 [`00786cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786cd4.md) · 呼出先 1件 [`00813fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813fd8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md#insn-008b6eb8)
- 新版 `008b6efc`（命令位置の公開資料なし）

~~~diff
- 008b6eb8 ["INT_ADD", "register:40f0:8", ["const:8b6eb8:8", "const:4:8"]]
- 008b6eb8 ["CALL", null, ["callee:00813fd8:8"]]
+ 008b6efc ["INT_ADD", "register:40f0:8", ["const:8b6efc:8", "const:4:8"]]
+ 008b6efc ["CALL", null, ["callee:00813fd8:8"]]
- 008b6eb8 bytes 3874fd97
+ 008b6efc bytes 3774fd97
~~~


<a id="compare-95113bb50affa5a465fe3b71a0cc8d83"></a>

### [`008b6f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f14.md) → [`008b6f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f58.md) FUN_008b6f58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006a9724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a9/006a9724.md) [`007f6fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6fb4.md) · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`006a9764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a9/006a9764.md) [`007f6ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6ff4.md) · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f14.md#insn-008b6f6c) · [`008b6fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f14.md#insn-008b6fa0) · [`008b6fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f14.md#insn-008b6fa4)
- 新版 `008b6fb0`（命令位置の公開資料なし） · `008b6fe4`（命令位置の公開資料なし） · `008b6fe8`（命令位置の公開資料なし）

~~~diff
- 008b6f6c ["COPY", "register:0:8", ["register:4048:8"]]
- 008b6f6c ["INT_ADD", "register:40f0:8", ["const:8b6f6c:8", "const:4:8"]]
- 008b6f6c ["CALLIND", null, ["register:0:8"]]
+ 008b6fb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b6fb0 ["INT_ADD", "register:40f0:8", ["const:8b6fb0:8", "const:4:8"]]
+ 008b6fb0 ["CALLIND", null, ["register:0:8"]]
- 008b6f6c bytes 20013fd6
+ 008b6fb0 bytes 20013fd6
- 008b6fa0 ["INT_ADD", "register:40f0:8", ["const:8b6fa0:8", "const:4:8"]]
- 008b6fa0 ["CALL", null, ["callee:00459d74:8"]]
+ 008b6fe4 ["INT_ADD", "register:40f0:8", ["const:8b6fe4:8", "const:4:8"]]
+ 008b6fe4 ["CALL", null, ["callee:00459d74:8"]]
- 008b6fa0 bytes 658bee97
+ 008b6fe4 bytes 648bee97
- 008b6fa4 ["INT_ADD", "register:40f0:8", ["const:8b6fa4:8", "const:4:8"]]
- 008b6fa4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008b6fe8 ["INT_ADD", "register:40f0:8", ["const:8b6fe8:8", "const:4:8"]]
+ 008b6fe8 ["CALL", null, ["callee:00c57ee0:8"]]
- 008b6fa4 bytes cf820e94
+ 008b6fe8 bytes be830e94
~~~


<a id="compare-1ed42fbe0a6e04df51653aa17884e64e"></a>

### [`008b7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md) → [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) FUN_008b7994

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 1件 [`00869a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869a34.md)
- 新版 呼出元 14件 [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006b380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b380c.md) [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 1件 [`00869a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869a74.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b7968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md#insn-008b7968)
- 新版 `008b79ac`（命令位置の公開資料なし）

~~~diff
- 008b7968 ["INT_ADD", "register:40f0:8", ["const:8b7968:8", "const:4:8"]]
- 008b7968 ["CALL", null, ["callee:00869a74:8"]]
+ 008b79ac ["INT_ADD", "register:40f0:8", ["const:8b79ac:8", "const:4:8"]]
+ 008b79ac ["CALL", null, ["callee:00869a74:8"]]
- 008b7968 bytes 33c8fe97
+ 008b79ac bytes 32c8fe97
~~~


<a id="compare-a8c1910f98adba83352ff3b0c1bee094"></a>

### [`008b7c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7c08.md) → [`008b7c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7c4c.md) FUN_008b7c4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`008b7388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`008b73cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b73cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b7cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7c08.md#insn-008b7cb8) · [`008b7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7c08.md#insn-008b7cc0) · [`008b7cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7c08.md#insn-008b7cc8)
- 新版 `008b7cfc`（命令位置の公開資料なし） · `008b7d04`（命令位置の公開資料なし） · `008b7d0c`（命令位置の公開資料なし）

~~~diff
- 008b7cb8 ["INT_ADD", "register:40f0:8", ["const:8b7cb8:8", "const:4:8"]]
- 008b7cb8 ["CALL", null, ["callee:00494610:8"]]
+ 008b7cfc ["INT_ADD", "register:40f0:8", ["const:8b7cfc:8", "const:4:8"]]
+ 008b7cfc ["CALL", null, ["callee:00494610:8"]]
- 008b7cb8 bytes 4672ef97
+ 008b7cfc bytes 4572ef97
- 008b7cc0 ["INT_ADD", "register:40f0:8", ["const:8b7cc0:8", "const:4:8"]]
- 008b7cc0 ["CALL", null, ["callee:008b73cc:8"]]
+ 008b7d04 ["INT_ADD", "register:40f0:8", ["const:8b7d04:8", "const:4:8"]]
+ 008b7d04 ["CALL", null, ["callee:008b73cc:8"]]
- 008b7cc0 bytes b2fdff97
+ 008b7d04 bytes b2fdff97
- 008b7cc8 ["INT_ADD", "register:40f0:8", ["const:8b7cc8:8", "const:4:8"]]
- 008b7cc8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008b7d0c ["INT_ADD", "register:40f0:8", ["const:8b7d0c:8", "const:4:8"]]
+ 008b7d0c ["CALL", null, ["callee:00c57eb0:8"]]
- 008b7cc8 bytes 7a7f0e94
+ 008b7d0c bytes 69800e94
~~~


<a id="compare-412e75598a59f98bd52fb2eb5a65c14f"></a>

### [`008b82c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b82c0.md) → [`008b8304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b8/008b8304.md) FUN_008b8304

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b82dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b82c0.md#insn-008b82dc) · [`008b82fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b82c0.md#insn-008b82fc)
- 新版 `008b8320`（命令位置の公開資料なし） · `008b8340`（命令位置の公開資料なし）

~~~diff
- 008b82dc ["INT_ADD", "register:40f0:8", ["const:8b82dc:8", "const:4:8"]]
- 008b82dc ["CALL", null, ["callee:00c53d00:8"]]
+ 008b8320 ["INT_ADD", "register:40f0:8", ["const:8b8320:8", "const:4:8"]]
+ 008b8320 ["CALL", null, ["callee:00c53d00:8"]]
- 008b82dc bytes 816d0e94
+ 008b8320 bytes 786e0e94
- 008b82fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008b82fc ["INT_ADD", "register:40f0:8", ["const:8b82fc:8", "const:4:8"]]
- 008b82fc ["CALLIND", null, ["register:0:8"]]
+ 008b8340 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b8340 ["INT_ADD", "register:40f0:8", ["const:8b8340:8", "const:4:8"]]
+ 008b8340 ["CALLIND", null, ["register:0:8"]]
- 008b82fc bytes 00013fd6
+ 008b8340 bytes 00013fd6
~~~


<a id="compare-eca3766b7b53420dbb084d42e9bbdc55"></a>

### [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md) → [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) FUN_008b9298

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00627c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) · 呼出先 2件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 54件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00627cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627cb4.md) [`0068e754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) · 呼出先 2件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md#insn-008b927c) · [`008b92a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md#insn-008b92a4)
- 新版 `008b92c0`（命令位置の公開資料なし） · `008b92e8`（命令位置の公開資料なし）

~~~diff
- 008b927c ["INT_ADD", "register:40f0:8", ["const:8b927c:8", "const:4:8"]]
- 008b927c ["CALL", null, ["callee:0046daf4:8"]]
+ 008b92c0 ["INT_ADD", "register:40f0:8", ["const:8b92c0:8", "const:4:8"]]
+ 008b92c0 ["CALL", null, ["callee:0046daf4:8"]]
- 008b927c bytes 0ed2ee97
+ 008b92c0 bytes 0dd2ee97
- 008b92a4 ["INT_ADD", "register:40f0:8", ["const:8b92a4:8", "const:4:8"]]
- 008b92a4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008b92e8 ["INT_ADD", "register:40f0:8", ["const:8b92e8:8", "const:4:8"]]
+ 008b92e8 ["CALL", null, ["callee:00c57ee0:8"]]
- 008b92a4 bytes 0f7a0e94
+ 008b92e8 bytes fe7a0e94
~~~


<a id="compare-f2100e11ae62e80d1812783d90ac1e20"></a>

### [`008b92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b92a8.md) → [`008b92ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b92ec.md) FUN_008b92ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`006954cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md) [`006966d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006966d0.md) [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) [`0069923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/0069923c.md) [`006af708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006af/006af708.md) · 呼出先 3件 [`0046daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daac.md) [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 14件 [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) [`00696710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696710.md) [`00697fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697fd4.md) [`0069927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069927c.md) [`006af748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af748.md) · 呼出先 3件 [`0046daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daec.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b93c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b92a8.md#insn-008b93c4) · [`008b9490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b92a8.md#insn-008b9490) · [`008b94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b92a8.md#insn-008b94b8)
- 新版 `008b9408`（命令位置の公開資料なし） · `008b94d4`（命令位置の公開資料なし） · `008b94fc`（命令位置の公開資料なし）

~~~diff
- 008b93c4 ["INT_ADD", "register:40f0:8", ["const:8b93c4:8", "const:4:8"]]
- 008b93c4 ["CALL", null, ["callee:0046daec:8"]]
+ 008b9408 ["INT_ADD", "register:40f0:8", ["const:8b9408:8", "const:4:8"]]
+ 008b9408 ["CALL", null, ["callee:0046daec:8"]]
- 008b93c4 bytes bad1ee97
+ 008b9408 bytes b9d1ee97
- 008b9490 ["INT_ADD", "register:40f0:8", ["const:8b9490:8", "const:4:8"]]
- 008b9490 ["CALL", null, ["callee:0046daf4:8"]]
+ 008b94d4 ["INT_ADD", "register:40f0:8", ["const:8b94d4:8", "const:4:8"]]
+ 008b94d4 ["CALL", null, ["callee:0046daf4:8"]]
- 008b9490 bytes 89d1ee97
+ 008b94d4 bytes 88d1ee97
- 008b94b8 ["INT_ADD", "register:40f0:8", ["const:8b94b8:8", "const:4:8"]]
- 008b94b8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008b94fc ["INT_ADD", "register:40f0:8", ["const:8b94fc:8", "const:4:8"]]
+ 008b94fc ["CALL", null, ["callee:00c57ee0:8"]]
- 008b94b8 bytes 8a790e94
+ 008b94fc bytes 797a0e94
~~~


<a id="compare-7b1476d16a1ae36e0cc1ff57a80253ac"></a>

### [`008b9588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md) → [`008b95cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b95cc.md) FUN_008b95cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 22件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) · 呼出先 2件 [`008bc1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc1fc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 22件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0068e754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) [`0068f5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068f/0068f5d8.md) · 呼出先 2件 [`008bc240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bc/008bc240.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b95c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md#insn-008b95c8) · [`008b95f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md#insn-008b95f4) · [`008b9604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md#insn-008b9604)
- 新版 `008b960c`（命令位置の公開資料なし） · `008b9638`（命令位置の公開資料なし） · `008b9648`（命令位置の公開資料なし）

~~~diff
- 008b95c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 008b95c8 ["INT_ADD", "register:40f0:8", ["const:8b95c8:8", "const:4:8"]]
- 008b95c8 ["CALLIND", null, ["register:0:8"]]
+ 008b960c ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b960c ["INT_ADD", "register:40f0:8", ["const:8b960c:8", "const:4:8"]]
+ 008b960c ["CALLIND", null, ["register:0:8"]]
- 008b95c8 bytes 20013fd6
+ 008b960c bytes 20013fd6
- 008b95f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b95f4 ["INT_ADD", "register:40f0:8", ["const:8b95f4:8", "const:4:8"]]
- 008b95f4 ["CALLIND", null, ["register:0:8"]]
+ 008b9638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b9638 ["INT_ADD", "register:40f0:8", ["const:8b9638:8", "const:4:8"]]
+ 008b9638 ["CALLIND", null, ["register:0:8"]]
- 008b95f4 bytes 00013fd6
+ 008b9638 bytes 00013fd6
- 008b9604 ["INT_ADD", "register:40f0:8", ["const:8b9604:8", "const:4:8"]]
- 008b9604 ["CALL", null, ["callee:008bc240:8"]]
+ 008b9648 ["INT_ADD", "register:40f0:8", ["const:8b9648:8", "const:4:8"]]
+ 008b9648 ["CALL", null, ["callee:008bc240:8"]]
- 008b9604 bytes fe0a0094
+ 008b9648 bytes fe0a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5b28fd0c48279872ba70d5cd35ac85"></a>

### [`008b9660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md) → [`008b96a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b96a4.md) FUN_008b96a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 38件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`00634a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md) [`0066ff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) · 呼出先 2件 [`008bc364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc364.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 38件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`00634a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00634/00634a64.md) [`0066ff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066ff74.md) [`0068e754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068e754.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md) · 呼出先 2件 [`008bc3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bc/008bc3a8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b96a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md#insn-008b96a0) · [`008b96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md#insn-008b96cc) · [`008b96dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md#insn-008b96dc)
- 新版 `008b96e4`（命令位置の公開資料なし） · `008b9710`（命令位置の公開資料なし） · `008b9720`（命令位置の公開資料なし）

~~~diff
- 008b96a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 008b96a0 ["INT_ADD", "register:40f0:8", ["const:8b96a0:8", "const:4:8"]]
- 008b96a0 ["CALLIND", null, ["register:0:8"]]
+ 008b96e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b96e4 ["INT_ADD", "register:40f0:8", ["const:8b96e4:8", "const:4:8"]]
+ 008b96e4 ["CALLIND", null, ["register:0:8"]]
- 008b96a0 bytes 20013fd6
+ 008b96e4 bytes 20013fd6
- 008b96cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008b96cc ["INT_ADD", "register:40f0:8", ["const:8b96cc:8", "const:4:8"]]
- 008b96cc ["CALLIND", null, ["register:0:8"]]
+ 008b9710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b9710 ["INT_ADD", "register:40f0:8", ["const:8b9710:8", "const:4:8"]]
+ 008b9710 ["CALLIND", null, ["register:0:8"]]
- 008b96cc bytes 00013fd6
+ 008b9710 bytes 00013fd6
- 008b96dc ["INT_ADD", "register:40f0:8", ["const:8b96dc:8", "const:4:8"]]
- 008b96dc ["CALL", null, ["callee:008bc3a8:8"]]
+ 008b9720 ["INT_ADD", "register:40f0:8", ["const:8b9720:8", "const:4:8"]]
+ 008b9720 ["CALL", null, ["callee:008bc3a8:8"]]
- 008b96dc bytes 220b0094
+ 008b9720 bytes 220b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e87c232f0aa2aa2281261280f86d057"></a>

### [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) → [`008ba868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008ba868.md) FUN_008ba868

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 66件 [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b8310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b8310.md) [`008bac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac48.md) [`008bc4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc4cc.md)
- 新版 呼出元 66件 [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b8354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b8/008b8354.md) [`008bac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bac8c.md) [`008bc510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bc/008bc510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ba86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md#insn-008ba86c) · [`008ba8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md#insn-008ba8b8) · [`008ba8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md#insn-008ba8e8)
- 新版 `008ba8b0`（命令位置の公開資料なし） · `008ba8fc`（命令位置の公開資料なし） · `008ba92c`（命令位置の公開資料なし）

~~~diff
- 008ba86c ["INT_ADD", "register:40f0:8", ["const:8ba86c:8", "const:4:8"]]
- 008ba86c ["CALL", null, ["callee:00c57e90:8"]]
+ 008ba8b0 ["INT_ADD", "register:40f0:8", ["const:8ba8b0:8", "const:4:8"]]
+ 008ba8b0 ["CALL", null, ["callee:00c57e90:8"]]
- 008ba86c bytes 89740e94
+ 008ba8b0 bytes 78750e94
- 008ba8b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ba8b8 ["INT_ADD", "register:40f0:8", ["const:8ba8b8:8", "const:4:8"]]
- 008ba8b8 ["CALLIND", null, ["register:0:8"]]
+ 008ba8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ba8fc ["INT_ADD", "register:40f0:8", ["const:8ba8fc:8", "const:4:8"]]
+ 008ba8fc ["CALLIND", null, ["register:0:8"]]
- 008ba8b8 bytes 00013fd6
+ 008ba8fc bytes 00013fd6
- 008ba8e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ba8e8 ["INT_ADD", "register:40f0:8", ["const:8ba8e8:8", "const:4:8"]]
- 008ba8e8 ["CALLIND", null, ["register:0:8"]]
+ 008ba92c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008ba92c ["INT_ADD", "register:40f0:8", ["const:8ba92c:8", "const:4:8"]]
+ 008ba92c ["CALLIND", null, ["register:0:8"]]
- 008ba8e8 bytes 00013fd6
+ 008ba92c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba74624fc10a72d30b63750d906d84c8"></a>

### [`008bac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac48.md) → [`008bac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bac8c.md) FUN_008bac8c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md) [`008bb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb0a8.md) · 呼出先 2件 [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`008ba868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008ba868.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md) [`008bb0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb0ec.md) · 呼出先 2件 [`00869b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bac64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac48.md#insn-008bac64)
- 新版 `008baca8`（命令位置の公開資料なし）

~~~diff
- 008bac64 ["INT_ADD", "register:40f0:8", ["const:8bac64:8", "const:4:8"]]
- 008bac64 ["CALL", null, ["callee:00869b3c:8"]]
+ 008baca8 ["INT_ADD", "register:40f0:8", ["const:8baca8:8", "const:4:8"]]
+ 008baca8 ["CALL", null, ["callee:00869b3c:8"]]
- 008bac64 bytes a6bbfe97
+ 008baca8 bytes a5bbfe97
~~~


<a id="compare-0851f8670c6e8d3de26996f5d6bbe76d"></a>

### [`008bb9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb9b0.md) → [`008bb9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb9f4.md) FUN_008bb9f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 1件 [`008b9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9ce8.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 1件 [`008b9d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9d2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bba04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb9b0.md#insn-008bba04)
- 新版 `008bba48`（命令位置の公開資料なし）

~~~diff
- 008bba04 ["INT_ADD", "register:40f0:8", ["const:8bba04:8", "const:4:8"]]
- 008bba04 ["CALL", null, ["callee:008b9d2c:8"]]
+ 008bba48 ["INT_ADD", "register:40f0:8", ["const:8bba48:8", "const:4:8"]]
+ 008bba48 ["CALL", null, ["callee:008b9d2c:8"]]
- 008bba04 bytes b9f8ff97
+ 008bba48 bytes b9f8ff97
~~~


<a id="compare-8f7ef7e98afbd7932a478dd47758936c"></a>

### [`008bba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bba1c.md) → [`008bba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bba60.md) FUN_008bba60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008acd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acd10.md) · 呼出先 2件 [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008acd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acd54.md) · 呼出先 2件 [`00869b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008bba60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bba1c.md#insn-008bba60) · [`008bba68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bba1c.md#insn-008bba68)
- 新版 `008bbaa4`（命令位置の公開資料なし） · `008bbaac`（命令位置の公開資料なし）

~~~diff
- 008bba60 ["INT_ADD", "register:40f0:8", ["const:8bba60:8", "const:4:8"]]
- 008bba60 ["CALL", null, ["callee:00869b3c:8"]]
+ 008bbaa4 ["INT_ADD", "register:40f0:8", ["const:8bbaa4:8", "const:4:8"]]
+ 008bbaa4 ["CALL", null, ["callee:00869b3c:8"]]
- 008bba60 bytes 27b8fe97
+ 008bbaa4 bytes 26b8fe97
- 008bba68 ["INT_ADD", "register:40f0:8", ["const:8bba68:8", "const:4:8"]]
- 008bba68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008bbaac ["INT_ADD", "register:40f0:8", ["const:8bbaac:8", "const:4:8"]]
+ 008bbaac ["CALL", null, ["callee:00c57eb0:8"]]
- 008bba68 bytes 12700e94
+ 008bbaac bytes 01710e94
~~~


