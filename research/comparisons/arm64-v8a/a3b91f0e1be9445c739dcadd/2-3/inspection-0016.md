# v15.7.4 → v16.0.0 · 要調査の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-3b7c6226aff8dc329632624e0ec614af"></a>

### [`0083928c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/0083928c.md) → [`0086b52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b52c.md) FUN_0086b52c

採用 · 移動量 `+0x322a0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004759a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008392a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/0083928c.md#insn-008392a0)
- 新版 `0086b540`（命令位置の公開資料なし）

~~~diff
- 008392a0 ["INT_ADD", "register:40f0:8", ["const:8392a0:8", "const:4:8"]]
- 008392a0 ["CALL", null, ["callee:0049883c:8"]]
+ 0086b540 ["INT_ADD", "register:40f0:8", ["const:86b540:8", "const:4:8"]]
+ 0086b540 ["CALL", null, ["callee:0049883c:8"]]
- 008392a0 bytes c1f1f097
+ 0086b540 bytes bfb4f097
~~~


<a id="compare-dbaf26392d44d788b6a50633787b96f1"></a>

### [`008392c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008392c8.md) → [`0086b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b568.md) FUN_0086b568

採用 · 移動量 `+0x322a0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) [`0047592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047592c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) [`004987c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004987c4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008392dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008392c8.md#insn-008392dc)
- 新版 `0086b57c`（命令位置の公開資料なし）

~~~diff
- 008392dc ["INT_ADD", "register:40f0:8", ["const:8392dc:8", "const:4:8"]]
- 008392dc ["CALL", null, ["callee:00498190:8"]]
+ 0086b57c ["INT_ADD", "register:40f0:8", ["const:86b57c:8", "const:4:8"]]
+ 0086b57c ["CALL", null, ["callee:00498190:8"]]
- 008392dc bytes 07f0f097
+ 0086b57c bytes 05b3f097
~~~


<a id="compare-1a42ed1b752103f9e9232156faa883b1"></a>

### [`00839a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md) → [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) FUN_0086bd78

採用 · 移動量 `+0x322ec` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008179e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008179e0.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`00839a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md) [`00a0b228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md) · 呼出先 4件 [`00839a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008497d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) · 呼出先 4件 [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md#insn-00839aa8) · [`00839ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md#insn-00839ab4) · [`00839ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md#insn-00839ac8)
- 新版 `0086bd94`（命令位置の公開資料なし） · `0086bda0`（命令位置の公開資料なし） · `0086bdb4`（命令位置の公開資料なし）

~~~diff
- 00839aa8 ["INT_ADD", "register:40f0:8", ["const:839aa8:8", "const:4:8"]]
- 00839aa8 ["CALL", null, ["local:b0:8"]]
+ 0086bd94 ["INT_ADD", "register:40f0:8", ["const:86bd94:8", "const:4:8"]]
+ 0086bd94 ["CALL", null, ["local:b0:8"]]
- 00839aa8 bytes f9ffff97
+ 0086bd94 bytes f9ffff97
- 00839ab4 ["INT_ADD", "register:40f0:8", ["const:839ab4:8", "const:4:8"]]
- 00839ab4 ["CALL", null, ["local:b0:8"]]
+ 0086bda0 ["INT_ADD", "register:40f0:8", ["const:86bda0:8", "const:4:8"]]
+ 0086bda0 ["CALL", null, ["local:b0:8"]]
- 00839ab4 bytes f6ffff97
+ 0086bda0 bytes f6ffff97
- 00839ac8 ["INT_ADD", "register:40f0:8", ["const:839ac8:8", "const:4:8"]]
- 00839ac8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0086bdb4 ["INT_ADD", "register:40f0:8", ["const:86bdb4:8", "const:4:8"]]
+ 0086bdb4 ["CALL", null, ["callee:00c538e0:8"]]
- 00839ac8 bytes f2740e94
+ 0086bdb4 bytes cb9e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86c85ddff07c24ec59c3561d9f21ddc"></a>

### [`00839b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md) → [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) FUN_0086be70

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md) · 呼出先 2件 [`00839b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) · 呼出先 2件 [`0086be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md#insn-00839ba0) · [`00839bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md#insn-00839bac) · [`00839bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b84.md#insn-00839bbc)
- 新版 `0086be8c`（命令位置の公開資料なし） · `0086be98`（命令位置の公開資料なし） · `0086bea8`（命令位置の公開資料なし）

~~~diff
- 00839ba0 ["INT_ADD", "register:40f0:8", ["const:839ba0:8", "const:4:8"]]
- 00839ba0 ["CALL", null, ["local:b0:8"]]
+ 0086be8c ["INT_ADD", "register:40f0:8", ["const:86be8c:8", "const:4:8"]]
+ 0086be8c ["CALL", null, ["local:b0:8"]]
- 00839ba0 bytes f9ffff97
+ 0086be8c bytes f9ffff97
- 00839bac ["INT_ADD", "register:40f0:8", ["const:839bac:8", "const:4:8"]]
- 00839bac ["CALL", null, ["local:b0:8"]]
+ 0086be98 ["INT_ADD", "register:40f0:8", ["const:86be98:8", "const:4:8"]]
+ 0086be98 ["CALL", null, ["local:b0:8"]]
- 00839bac bytes f6ffff97
+ 0086be98 bytes f6ffff97
- 00839bbc ["INT_ADD", "register:40f0:8", ["const:839bbc:8", "const:4:8"]]
- 00839bbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086bea8 ["INT_ADD", "register:40f0:8", ["const:86bea8:8", "const:4:8"]]
+ 0086bea8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839bbc bytes 29850e94
+ 0086bea8 bytes 02af0f94
~~~


<a id="compare-5c946ae473490a8a046254d2b2f8377c"></a>

### [`00839c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md) → [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) FUN_0086bf10

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md) · 呼出先 3件 [`00839c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md) [`00839c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) · 呼出先 3件 [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) [`0086bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md#insn-00839c44) · [`00839c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md#insn-00839c50) · [`00839c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md#insn-00839c58)
- 新版 `0086bf30`（命令位置の公開資料なし） · `0086bf3c`（命令位置の公開資料なし） · `0086bf44`（命令位置の公開資料なし）

~~~diff
- 00839c44 ["INT_ADD", "register:40f0:8", ["const:839c44:8", "const:4:8"]]
- 00839c44 ["CALL", null, ["local:b0:8"]]
+ 0086bf30 ["INT_ADD", "register:40f0:8", ["const:86bf30:8", "const:4:8"]]
+ 0086bf30 ["CALL", null, ["local:b0:8"]]
- 00839c44 bytes f8ffff97
+ 0086bf30 bytes f8ffff97
- 00839c50 ["INT_ADD", "register:40f0:8", ["const:839c50:8", "const:4:8"]]
- 00839c50 ["CALL", null, ["local:b0:8"]]
+ 0086bf3c ["INT_ADD", "register:40f0:8", ["const:86bf3c:8", "const:4:8"]]
+ 0086bf3c ["CALL", null, ["local:b0:8"]]
- 00839c50 bytes f5ffff97
+ 0086bf3c bytes f5ffff97
- 00839c58 ["INT_ADD", "register:40f0:8", ["const:839c58:8", "const:4:8"]]
- 00839c58 ["CALL", null, ["callee:0086bf5c:8"]]
+ 0086bf44 ["INT_ADD", "register:40f0:8", ["const:86bf44:8", "const:4:8"]]
+ 0086bf44 ["CALL", null, ["callee:0086bf5c:8"]]
- 00839c58 bytes 06000094
+ 0086bf44 bytes 06000094
~~~


<a id="compare-fc6396e38aa1da6fa068c82d68962b62"></a>

### [`00839c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md) → [`0086bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf5c.md) FUN_0086bf5c

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00839c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c24.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0086bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bf10.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md#insn-00839cbc) · [`00839ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md#insn-00839ccc) · [`00839cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md#insn-00839cd8)
- 新版 `0086bfa8`（命令位置の公開資料なし） · `0086bfb8`（命令位置の公開資料なし） · `0086bfc4`（命令位置の公開資料なし）

~~~diff
- 00839cbc ["INT_ADD", "register:40f0:8", ["const:839cbc:8", "const:4:8"]]
- 00839cbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086bfa8 ["INT_ADD", "register:40f0:8", ["const:86bfa8:8", "const:4:8"]]
+ 0086bfa8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839cbc bytes e9840e94
+ 0086bfa8 bytes c2ae0f94
- 00839ccc ["INT_ADD", "register:40f0:8", ["const:839ccc:8", "const:4:8"]]
- 00839ccc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086bfb8 ["INT_ADD", "register:40f0:8", ["const:86bfb8:8", "const:4:8"]]
+ 0086bfb8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839ccc bytes e5840e94
+ 0086bfb8 bytes beae0f94
- 00839cd8 ["INT_ADD", "register:40f0:8", ["const:839cd8:8", "const:4:8"]]
- 00839cd8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086bfc4 ["INT_ADD", "register:40f0:8", ["const:86bfc4:8", "const:4:8"]]
+ 0086bfc4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839cd8 bytes e2840e94
+ 0086bfc4 bytes bbae0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b617e2b5950768f49c115ea1e2a636"></a>

### [`00839e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e10.md) → [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) FUN_0086c0fc

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00839e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e10.md) · 呼出先 2件 [`00839e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e10.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) · 呼出先 2件 [`0086c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c0fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e10.md#insn-00839e30) · [`00839e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e10.md#insn-00839e3c)
- 新版 `0086c11c`（命令位置の公開資料なし） · `0086c128`（命令位置の公開資料なし）

~~~diff
- 00839e30 ["INT_ADD", "register:40f0:8", ["const:839e30:8", "const:4:8"]]
- 00839e30 ["CALL", null, ["local:b0:8"]]
+ 0086c11c ["INT_ADD", "register:40f0:8", ["const:86c11c:8", "const:4:8"]]
+ 0086c11c ["CALL", null, ["local:b0:8"]]
- 00839e30 bytes f8ffff97
+ 0086c11c bytes f8ffff97
- 00839e3c ["INT_ADD", "register:40f0:8", ["const:839e3c:8", "const:4:8"]]
- 00839e3c ["CALL", null, ["local:b0:8"]]
+ 0086c128 ["INT_ADD", "register:40f0:8", ["const:86c128:8", "const:4:8"]]
+ 0086c128 ["CALL", null, ["local:b0:8"]]
- 00839e3c bytes f5ffff97
+ 0086c128 bytes f5ffff97
~~~


<a id="compare-99c41552f7cb84330f635a11348ec87b"></a>

### [`00839e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md) → [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) FUN_0086c140

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00839e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md) · 呼出先 2件 [`00839e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) · 呼出先 2件 [`0086c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c140.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md#insn-00839e70) · [`00839e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md#insn-00839e7c) · [`00839e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839e54.md#insn-00839e8c)
- 新版 `0086c15c`（命令位置の公開資料なし） · `0086c168`（命令位置の公開資料なし） · `0086c178`（命令位置の公開資料なし）

~~~diff
- 00839e70 ["INT_ADD", "register:40f0:8", ["const:839e70:8", "const:4:8"]]
- 00839e70 ["CALL", null, ["local:b0:8"]]
+ 0086c15c ["INT_ADD", "register:40f0:8", ["const:86c15c:8", "const:4:8"]]
+ 0086c15c ["CALL", null, ["local:b0:8"]]
- 00839e70 bytes f9ffff97
+ 0086c15c bytes f9ffff97
- 00839e7c ["INT_ADD", "register:40f0:8", ["const:839e7c:8", "const:4:8"]]
- 00839e7c ["CALL", null, ["local:b0:8"]]
+ 0086c168 ["INT_ADD", "register:40f0:8", ["const:86c168:8", "const:4:8"]]
+ 0086c168 ["CALL", null, ["local:b0:8"]]
- 00839e7c bytes f6ffff97
+ 0086c168 bytes f6ffff97
- 00839e8c ["INT_ADD", "register:40f0:8", ["const:839e8c:8", "const:4:8"]]
- 00839e8c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086c178 ["INT_ADD", "register:40f0:8", ["const:86c178:8", "const:4:8"]]
+ 0086c178 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839e8c bytes 75840e94
+ 0086c178 bytes 4eae0f94
~~~


<a id="compare-eb3475fce8e65322beec4bca2536106d"></a>

### [`00839ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ea4.md) → [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) FUN_0086c190

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0082f5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f5a4.md) [`00839ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ea4.md) · 呼出先 2件 [`00839ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ea4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086151c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/0086151c.md) [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) · 呼出先 2件 [`0086c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c190.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ea4.md#insn-00839ec4) · [`00839ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ea4.md#insn-00839ed0)
- 新版 `0086c1b0`（命令位置の公開資料なし） · `0086c1bc`（命令位置の公開資料なし）

~~~diff
- 00839ec4 ["INT_ADD", "register:40f0:8", ["const:839ec4:8", "const:4:8"]]
- 00839ec4 ["CALL", null, ["local:b0:8"]]
+ 0086c1b0 ["INT_ADD", "register:40f0:8", ["const:86c1b0:8", "const:4:8"]]
+ 0086c1b0 ["CALL", null, ["local:b0:8"]]
- 00839ec4 bytes f8ffff97
+ 0086c1b0 bytes f8ffff97
- 00839ed0 ["INT_ADD", "register:40f0:8", ["const:839ed0:8", "const:4:8"]]
- 00839ed0 ["CALL", null, ["local:b0:8"]]
+ 0086c1bc ["INT_ADD", "register:40f0:8", ["const:86c1bc:8", "const:4:8"]]
+ 0086c1bc ["CALL", null, ["local:b0:8"]]
- 00839ed0 bytes f5ffff97
+ 0086c1bc bytes f5ffff97
~~~


<a id="compare-caa5b8cee570548878436fff2295142f"></a>

### [`00839ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md) → [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) FUN_0086c1d4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md) [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 2件 [`00839ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 2件 [`0086c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c1d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md#insn-00839f04) · [`00839f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md#insn-00839f10) · [`00839f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839ee8.md#insn-00839f20)
- 新版 `0086c1f0`（命令位置の公開資料なし） · `0086c1fc`（命令位置の公開資料なし） · `0086c20c`（命令位置の公開資料なし）

~~~diff
- 00839f04 ["INT_ADD", "register:40f0:8", ["const:839f04:8", "const:4:8"]]
- 00839f04 ["CALL", null, ["local:b0:8"]]
+ 0086c1f0 ["INT_ADD", "register:40f0:8", ["const:86c1f0:8", "const:4:8"]]
+ 0086c1f0 ["CALL", null, ["local:b0:8"]]
- 00839f04 bytes f9ffff97
+ 0086c1f0 bytes f9ffff97
- 00839f10 ["INT_ADD", "register:40f0:8", ["const:839f10:8", "const:4:8"]]
- 00839f10 ["CALL", null, ["local:b0:8"]]
+ 0086c1fc ["INT_ADD", "register:40f0:8", ["const:86c1fc:8", "const:4:8"]]
+ 0086c1fc ["CALL", null, ["local:b0:8"]]
- 00839f10 bytes f6ffff97
+ 0086c1fc bytes f6ffff97
- 00839f20 ["INT_ADD", "register:40f0:8", ["const:839f20:8", "const:4:8"]]
- 00839f20 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086c20c ["INT_ADD", "register:40f0:8", ["const:86c20c:8", "const:4:8"]]
+ 0086c20c ["CALL", null, ["callee:00c57ab0:8"]]
- 00839f20 bytes 50840e94
+ 0086c20c bytes 29ae0f94
~~~


<a id="compare-e3c7d52794aa43fecfd6b8f34eae5d16"></a>

### [`00839f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md) → [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) FUN_0086c224

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`0082ea34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082e/0082ea34.md) [`00839f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 3件 [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`00839f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`008609ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00860/008609ac.md) [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 3件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0086c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c224.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md#insn-00839f58) · [`00839f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md#insn-00839f64) · [`00839f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f38.md#insn-00839f70)
- 新版 `0086c244`（命令位置の公開資料なし） · `0086c250`（命令位置の公開資料なし） · `0086c25c`（命令位置の公開資料なし）

~~~diff
- 00839f58 ["INT_ADD", "register:40f0:8", ["const:839f58:8", "const:4:8"]]
- 00839f58 ["CALL", null, ["local:b0:8"]]
+ 0086c244 ["INT_ADD", "register:40f0:8", ["const:86c244:8", "const:4:8"]]
+ 0086c244 ["CALL", null, ["local:b0:8"]]
- 00839f58 bytes f8ffff97
+ 0086c244 bytes f8ffff97
- 00839f64 ["INT_ADD", "register:40f0:8", ["const:839f64:8", "const:4:8"]]
- 00839f64 ["CALL", null, ["local:b0:8"]]
+ 0086c250 ["INT_ADD", "register:40f0:8", ["const:86c250:8", "const:4:8"]]
+ 0086c250 ["CALL", null, ["local:b0:8"]]
- 00839f64 bytes f5ffff97
+ 0086c250 bytes f5ffff97
- 00839f70 ["INT_ADD", "register:40f0:8", ["const:839f70:8", "const:4:8"]]
- 00839f70 ["CALL", null, ["callee:00676a20:8"]]
+ 0086c25c ["INT_ADD", "register:40f0:8", ["const:86c25c:8", "const:4:8"]]
+ 0086c25c ["CALL", null, ["callee:00676a20:8"]]
- 00839f70 bytes f459f897
+ 0086c25c bytes f129f897
~~~


<a id="compare-a8c3e4f686b8f21a503ef962db3c9abe"></a>

### [`00839f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md) → [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) FUN_0086c274

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081e868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081e/0081e868.md) [`00839f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md) [`00839fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 2件 [`00839f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 7件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md#insn-00839fa8) · [`00839fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md#insn-00839fb4)
- 新版 `0086c294`（命令位置の公開資料なし） · `0086c2a0`（命令位置の公開資料なし）

~~~diff
- 00839fa8 ["INT_ADD", "register:40f0:8", ["const:839fa8:8", "const:4:8"]]
- 00839fa8 ["CALL", null, ["local:b0:8"]]
+ 0086c294 ["INT_ADD", "register:40f0:8", ["const:86c294:8", "const:4:8"]]
+ 0086c294 ["CALL", null, ["local:b0:8"]]
- 00839fa8 bytes f8ffff97
+ 0086c294 bytes f8ffff97
- 00839fb4 ["INT_ADD", "register:40f0:8", ["const:839fb4:8", "const:4:8"]]
- 00839fb4 ["CALL", null, ["local:b0:8"]]
+ 0086c2a0 ["INT_ADD", "register:40f0:8", ["const:86c2a0:8", "const:4:8"]]
+ 0086c2a0 ["CALL", null, ["local:b0:8"]]
- 00839fb4 bytes f5ffff97
+ 0086c2a0 bytes f5ffff97
~~~


<a id="compare-c73cd63156dc168599dd480429f967c8"></a>

### [`00839fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md) → [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) FUN_0086c2b8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081e868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081e/0081e868.md) [`00839fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 3件 [`00839f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md) [`00839fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0086c274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c274.md) [`0086c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c2b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md#insn-00839fec) · [`00839ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md#insn-00839ff8) · [`0083a004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839fcc.md#insn-0083a004)
- 新版 `0086c2d8`（命令位置の公開資料なし） · `0086c2e4`（命令位置の公開資料なし） · `0086c2f0`（命令位置の公開資料なし）

~~~diff
- 00839fec ["INT_ADD", "register:40f0:8", ["const:839fec:8", "const:4:8"]]
- 00839fec ["CALL", null, ["local:b0:8"]]
+ 0086c2d8 ["INT_ADD", "register:40f0:8", ["const:86c2d8:8", "const:4:8"]]
+ 0086c2d8 ["CALL", null, ["local:b0:8"]]
- 00839fec bytes f8ffff97
+ 0086c2d8 bytes f8ffff97
- 00839ff8 ["INT_ADD", "register:40f0:8", ["const:839ff8:8", "const:4:8"]]
- 00839ff8 ["CALL", null, ["local:b0:8"]]
+ 0086c2e4 ["INT_ADD", "register:40f0:8", ["const:86c2e4:8", "const:4:8"]]
+ 0086c2e4 ["CALL", null, ["local:b0:8"]]
- 00839ff8 bytes f5ffff97
+ 0086c2e4 bytes f5ffff97
- 0083a004 ["INT_ADD", "register:40f0:8", ["const:83a004:8", "const:4:8"]]
- 0083a004 ["CALL", null, ["callee:0086c274:8"]]
+ 0086c2f0 ["INT_ADD", "register:40f0:8", ["const:86c2f0:8", "const:4:8"]]
+ 0086c2f0 ["CALL", null, ["callee:0086c274:8"]]
- 0083a004 bytes e1ffff97
+ 0086c2f0 bytes e1ffff97
~~~


<a id="compare-0ac33b2c9bb670505db780ca90a1ab6d"></a>

### [`0083a01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a01c.md) → [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) FUN_0086c308

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0083a01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a01c.md) · 呼出先 2件 [`0083a01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a01c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) · 呼出先 2件 [`0086c308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c308.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083a03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a01c.md#insn-0083a03c) · [`0083a048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a01c.md#insn-0083a048)
- 新版 `0086c328`（命令位置の公開資料なし） · `0086c334`（命令位置の公開資料なし）

~~~diff
- 0083a03c ["INT_ADD", "register:40f0:8", ["const:83a03c:8", "const:4:8"]]
- 0083a03c ["CALL", null, ["local:b0:8"]]
+ 0086c328 ["INT_ADD", "register:40f0:8", ["const:86c328:8", "const:4:8"]]
+ 0086c328 ["CALL", null, ["local:b0:8"]]
- 0083a03c bytes f8ffff97
+ 0086c328 bytes f8ffff97
- 0083a048 ["INT_ADD", "register:40f0:8", ["const:83a048:8", "const:4:8"]]
- 0083a048 ["CALL", null, ["local:b0:8"]]
+ 0086c334 ["INT_ADD", "register:40f0:8", ["const:86c334:8", "const:4:8"]]
+ 0086c334 ["CALL", null, ["local:b0:8"]]
- 0083a048 bytes f5ffff97
+ 0086c334 bytes f5ffff97
~~~


<a id="compare-78f1af90a162d2db0c93029ab5dd5656"></a>

### [`0083a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a060.md) → [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) FUN_0086c34c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0083a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a060.md) · 呼出先 2件 [`0083a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a060.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) · 呼出先 2件 [`0086c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c34c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083a080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a060.md#insn-0083a080) · [`0083a08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a060.md#insn-0083a08c)
- 新版 `0086c36c`（命令位置の公開資料なし） · `0086c378`（命令位置の公開資料なし）

~~~diff
- 0083a080 ["INT_ADD", "register:40f0:8", ["const:83a080:8", "const:4:8"]]
- 0083a080 ["CALL", null, ["local:b0:8"]]
+ 0086c36c ["INT_ADD", "register:40f0:8", ["const:86c36c:8", "const:4:8"]]
+ 0086c36c ["CALL", null, ["local:b0:8"]]
- 0083a080 bytes f8ffff97
+ 0086c36c bytes f8ffff97
- 0083a08c ["INT_ADD", "register:40f0:8", ["const:83a08c:8", "const:4:8"]]
- 0083a08c ["CALL", null, ["local:b0:8"]]
+ 0086c378 ["INT_ADD", "register:40f0:8", ["const:86c378:8", "const:4:8"]]
+ 0086c378 ["CALL", null, ["local:b0:8"]]
- 0083a08c bytes f5ffff97
+ 0086c378 bytes f5ffff97
~~~


<a id="compare-3b97fa6a9eb664c81e7d59f37072ae20"></a>

### [`0083a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md) → [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) FUN_0086c390

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0083a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 3件 [`0083a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md) [`0083a0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 3件 [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md#insn-0083a0c4) · [`0083a0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md#insn-0083a0d0) · [`0083a0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md#insn-0083a0dc)
- 新版 `0086c3b0`（命令位置の公開資料なし） · `0086c3bc`（命令位置の公開資料なし） · `0086c3c8`（命令位置の公開資料なし）

~~~diff
- 0083a0c4 ["INT_ADD", "register:40f0:8", ["const:83a0c4:8", "const:4:8"]]
- 0083a0c4 ["CALL", null, ["local:b0:8"]]
+ 0086c3b0 ["INT_ADD", "register:40f0:8", ["const:86c3b0:8", "const:4:8"]]
+ 0086c3b0 ["CALL", null, ["local:b0:8"]]
- 0083a0c4 bytes f8ffff97
+ 0086c3b0 bytes f8ffff97
- 0083a0d0 ["INT_ADD", "register:40f0:8", ["const:83a0d0:8", "const:4:8"]]
- 0083a0d0 ["CALL", null, ["local:b0:8"]]
+ 0086c3bc ["INT_ADD", "register:40f0:8", ["const:86c3bc:8", "const:4:8"]]
+ 0086c3bc ["CALL", null, ["local:b0:8"]]
- 0083a0d0 bytes f5ffff97
+ 0086c3bc bytes f5ffff97
- 0083a0dc ["INT_ADD", "register:40f0:8", ["const:83a0dc:8", "const:4:8"]]
- 0083a0dc ["CALL", null, ["callee:0086c3e0:8"]]
+ 0086c3c8 ["INT_ADD", "register:40f0:8", ["const:86c3c8:8", "const:4:8"]]
+ 0086c3c8 ["CALL", null, ["callee:0086c3e0:8"]]
- 0083a0dc bytes 06000094
+ 0086c3c8 bytes 06000094
~~~


<a id="compare-150562dafbf1d126392a0c57f9b88d47"></a>

### [`0083a0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md) → [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) FUN_0086c3e0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0a4.md) [`0083a0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md) [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0083a0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0086c390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c390.md) [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`0086c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c3e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083a114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md#insn-0083a114) · [`0083a120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a0f4.md#insn-0083a120)
- 新版 `0086c400`（命令位置の公開資料なし） · `0086c40c`（命令位置の公開資料なし）

~~~diff
- 0083a114 ["INT_ADD", "register:40f0:8", ["const:83a114:8", "const:4:8"]]
- 0083a114 ["CALL", null, ["local:b0:8"]]
+ 0086c400 ["INT_ADD", "register:40f0:8", ["const:86c400:8", "const:4:8"]]
+ 0086c400 ["CALL", null, ["local:b0:8"]]
- 0083a114 bytes f8ffff97
+ 0086c400 bytes f8ffff97
- 0083a120 ["INT_ADD", "register:40f0:8", ["const:83a120:8", "const:4:8"]]
- 0083a120 ["CALL", null, ["local:b0:8"]]
+ 0086c40c ["INT_ADD", "register:40f0:8", ["const:86c40c:8", "const:4:8"]]
+ 0086c40c ["CALL", null, ["local:b0:8"]]
- 0083a120 bytes f5ffff97
+ 0086c40c bytes f5ffff97
~~~


<a id="compare-4541a3efe9b0291ac67248575a0ca69e"></a>

### [`0083a1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md) → [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) FUN_0086c4d8

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0083a1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md) · 呼出先 2件 [`0083a1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) · 呼出先 2件 [`0086c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c4d8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083a208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md#insn-0083a208) · [`0083a214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md#insn-0083a214) · [`0083a234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a1ec.md#insn-0083a234)
- 新版 `0086c4f4`（命令位置の公開資料なし） · `0086c500`（命令位置の公開資料なし） · `0086c520`（命令位置の公開資料なし）

~~~diff
- 0083a208 ["INT_ADD", "register:40f0:8", ["const:83a208:8", "const:4:8"]]
- 0083a208 ["CALL", null, ["local:b0:8"]]
+ 0086c4f4 ["INT_ADD", "register:40f0:8", ["const:86c4f4:8", "const:4:8"]]
+ 0086c4f4 ["CALL", null, ["local:b0:8"]]
- 0083a208 bytes f9ffff97
+ 0086c4f4 bytes f9ffff97
- 0083a214 ["INT_ADD", "register:40f0:8", ["const:83a214:8", "const:4:8"]]
- 0083a214 ["CALL", null, ["local:b0:8"]]
+ 0086c500 ["INT_ADD", "register:40f0:8", ["const:86c500:8", "const:4:8"]]
+ 0086c500 ["CALL", null, ["local:b0:8"]]
- 0083a214 bytes f6ffff97
+ 0086c500 bytes f6ffff97
- 0083a234 ["INT_ADD", "register:40f0:8", ["const:83a234:8", "const:4:8"]]
- 0083a234 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086c520 ["INT_ADD", "register:40f0:8", ["const:86c520:8", "const:4:8"]]
+ 0086c520 ["CALL", null, ["callee:00c57ab0:8"]]
- 0083a234 bytes 8b830e94
+ 0086c520 bytes 64ad0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ff2675910abd3d2e331a63009463c5"></a>

### [`0083fcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcc0.md) → [`00871fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fac.md) FUN_00871fac

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00833158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833158.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083fce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcc0.md#insn-0083fce0)
- 新版 `00871fcc`（命令位置の公開資料なし）

~~~diff
- 0083fce0 ["INT_ADD", "register:40f0:8", ["const:83fce0:8", "const:4:8"]]
- 0083fce0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00871fcc ["INT_ADD", "register:40f0:8", ["const:871fcc:8", "const:4:8"]]
+ 00871fcc ["CALL", null, ["callee:00c57ab0:8"]]
- 0083fce0 bytes e06c0e94
+ 00871fcc bytes b9960f94
~~~


<a id="compare-e09b0661c670b23b5ccdf6fe30190f08"></a>

### [`008406c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406c0.md) → [`008729ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729ac.md) FUN_008729ac

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00840274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008406d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406c0.md#insn-008406d0)
- 新版 `008729bc`（命令位置の公開資料なし）

~~~diff
- 008406d0 ["INT_ADD", "register:40f0:8", ["const:8406d0:8", "const:4:8"]]
- 008406d0 ["CALL", null, ["callee:00872560:8"]]
+ 008729bc ["INT_ADD", "register:40f0:8", ["const:8729bc:8", "const:4:8"]]
+ 008729bc ["CALL", null, ["callee:00872560:8"]]
- 008406d0 bytes e9feff97
+ 008729bc bytes e9feff97
~~~


<a id="compare-a56f42169d31c4cddead3f6373c134a7"></a>

### [`00842060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842060.md) → [`0087434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087434c.md) FUN_0087434c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084207c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842060.md#insn-0084207c) · [`0084209c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842060.md#insn-0084209c)
- 新版 `00874368`（命令位置の公開資料なし） · `00874388`（命令位置の公開資料なし）

~~~diff
- 0084207c ["INT_ADD", "register:40f0:8", ["const:84207c:8", "const:4:8"]]
- 0084207c ["CALL", null, ["callee:00c538e0:8"]]
+ 00874368 ["INT_ADD", "register:40f0:8", ["const:874368:8", "const:4:8"]]
+ 00874368 ["CALL", null, ["callee:00c538e0:8"]]
- 0084207c bytes 85530e94
+ 00874368 bytes 5e7d0f94
- 0084209c ["COPY", "register:0:8", ["register:4040:8"]]
- 0084209c ["INT_ADD", "register:40f0:8", ["const:84209c:8", "const:4:8"]]
- 0084209c ["CALLIND", null, ["register:0:8"]]
+ 00874388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874388 ["INT_ADD", "register:40f0:8", ["const:874388:8", "const:4:8"]]
+ 00874388 ["CALLIND", null, ["register:0:8"]]
- 0084209c bytes 00013fd6
+ 00874388 bytes 00013fd6
~~~


<a id="compare-6056419f7ae796f555d81ca7298fe8f5"></a>

### [`008420b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008420b0.md) → [`0087439c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/0087439c.md) FUN_0087439c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008420cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008420b0.md#insn-008420cc) · [`008420ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008420b0.md#insn-008420ec)
- 新版 `008743b8`（命令位置の公開資料なし） · `008743d8`（命令位置の公開資料なし）

~~~diff
- 008420cc ["INT_ADD", "register:40f0:8", ["const:8420cc:8", "const:4:8"]]
- 008420cc ["CALL", null, ["callee:00c538e0:8"]]
+ 008743b8 ["INT_ADD", "register:40f0:8", ["const:8743b8:8", "const:4:8"]]
+ 008743b8 ["CALL", null, ["callee:00c538e0:8"]]
- 008420cc bytes 71530e94
+ 008743b8 bytes 4a7d0f94
- 008420ec ["COPY", "register:0:8", ["register:4040:8"]]
- 008420ec ["INT_ADD", "register:40f0:8", ["const:8420ec:8", "const:4:8"]]
- 008420ec ["CALLIND", null, ["register:0:8"]]
+ 008743d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008743d8 ["INT_ADD", "register:40f0:8", ["const:8743d8:8", "const:4:8"]]
+ 008743d8 ["CALLIND", null, ["register:0:8"]]
- 008420ec bytes 00013fd6
+ 008743d8 bytes 00013fd6
~~~


<a id="compare-f2aa2ec72b71350e6c0ecbe3b2f2ef43"></a>

### [`008422ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md) → [`008745d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md) FUN_008745d8

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md#insn-00842330) · [`00842340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md#insn-00842340) · [`00842390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md#insn-00842390)
- 新版 `0087461c`（命令位置の公開資料なし） · `0087462c`（命令位置の公開資料なし） · `0087467c`（命令位置の公開資料なし）

~~~diff
- 00842330 ["INT_ADD", "register:40f0:8", ["const:842330:8", "const:4:8"]]
- 00842330 ["CALL", null, ["callee:008746a8:8"]]
+ 0087461c ["INT_ADD", "register:40f0:8", ["const:87461c:8", "const:4:8"]]
+ 0087461c ["CALL", null, ["callee:008746a8:8"]]
- 00842330 bytes 23000094
+ 0087461c bytes 23000094
- 00842340 ["INT_ADD", "register:40f0:8", ["const:842340:8", "const:4:8"]]
- 00842340 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0087462c ["INT_ADD", "register:40f0:8", ["const:87462c:8", "const:4:8"]]
+ 0087462c ["CALL", null, ["callee:00c57ab0:8"]]
- 00842340 bytes 48630e94
+ 0087462c bytes 218d0f94
- 00842390 ["INT_ADD", "register:40f0:8", ["const:842390:8", "const:4:8"]]
- 00842390 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0087467c ["INT_ADD", "register:40f0:8", ["const:87467c:8", "const:4:8"]]
+ 0087467c ["CALL", null, ["callee:00c57ae0:8"]]
- 00842390 bytes 40630e94
+ 0087467c bytes 198d0f94
~~~


<a id="compare-d2d60c18e62440f0b8cf894e8089c3e0"></a>

### [`0084256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084256c.md) → [`00874858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874858.md) FUN_00874858

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084256c.md#insn-00842588) · [`008425a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084256c.md#insn-008425a8)
- 新版 `00874874`（命令位置の公開資料なし） · `00874894`（命令位置の公開資料なし）

~~~diff
- 00842588 ["INT_ADD", "register:40f0:8", ["const:842588:8", "const:4:8"]]
- 00842588 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874874 ["INT_ADD", "register:40f0:8", ["const:874874:8", "const:4:8"]]
+ 00874874 ["CALL", null, ["callee:00c538e0:8"]]
- 00842588 bytes 42520e94
+ 00874874 bytes 1b7c0f94
- 008425a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008425a8 ["INT_ADD", "register:40f0:8", ["const:8425a8:8", "const:4:8"]]
- 008425a8 ["CALLIND", null, ["register:0:8"]]
+ 00874894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874894 ["INT_ADD", "register:40f0:8", ["const:874894:8", "const:4:8"]]
+ 00874894 ["CALLIND", null, ["register:0:8"]]
- 008425a8 bytes 00013fd6
+ 00874894 bytes 00013fd6
~~~


<a id="compare-f0ef9cf92455305728e1db3d7ec6ae2b"></a>

### [`00842708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842708.md) → [`008749f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md) FUN_008749f4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842708.md#insn-00842724) · [`00842744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842708.md#insn-00842744)
- 新版 `00874a10`（命令位置の公開資料なし） · `00874a30`（命令位置の公開資料なし）

~~~diff
- 00842724 ["INT_ADD", "register:40f0:8", ["const:842724:8", "const:4:8"]]
- 00842724 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874a10 ["INT_ADD", "register:40f0:8", ["const:874a10:8", "const:4:8"]]
+ 00874a10 ["CALL", null, ["callee:00c538e0:8"]]
- 00842724 bytes db510e94
+ 00874a10 bytes b47b0f94
- 00842744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00842744 ["INT_ADD", "register:40f0:8", ["const:842744:8", "const:4:8"]]
- 00842744 ["CALLIND", null, ["register:0:8"]]
+ 00874a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874a30 ["INT_ADD", "register:40f0:8", ["const:874a30:8", "const:4:8"]]
+ 00874a30 ["CALLIND", null, ["register:0:8"]]
- 00842744 bytes 00013fd6
+ 00874a30 bytes 00013fd6
~~~


<a id="compare-c256beda0d3dd847ae5251c6cfbbe4b1"></a>

### [`00842758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md) → [`00874a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md) FUN_00874a44

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md#insn-00842778) · [`0084278c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md#insn-0084278c) · [`00842794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md#insn-00842794)
- 新版 `00874a64`（命令位置の公開資料なし） · `00874a78`（命令位置の公開資料なし） · `00874a80`（命令位置の公開資料なし）

~~~diff
- 00842778 ["INT_ADD", "register:40f0:8", ["const:842778:8", "const:4:8"]]
- 00842778 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874a64 ["INT_ADD", "register:40f0:8", ["const:874a64:8", "const:4:8"]]
+ 00874a64 ["CALL", null, ["callee:00c538e0:8"]]
- 00842778 bytes c6510e94
+ 00874a64 bytes 9f7b0f94
- 0084278c ["COPY", "register:0:8", ["register:4040:8"]]
- 0084278c ["INT_ADD", "register:40f0:8", ["const:84278c:8", "const:4:8"]]
- 0084278c ["CALLIND", null, ["register:0:8"]]
+ 00874a78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874a78 ["INT_ADD", "register:40f0:8", ["const:874a78:8", "const:4:8"]]
+ 00874a78 ["CALLIND", null, ["register:0:8"]]
- 0084278c bytes 00013fd6
+ 00874a78 bytes 00013fd6
- 00842794 ["INT_ADD", "register:40f0:8", ["const:842794:8", "const:4:8"]]
- 00842794 ["CALL", null, ["callee:00c57a80:8"]]
+ 00874a80 ["INT_ADD", "register:40f0:8", ["const:874a80:8", "const:4:8"]]
+ 00874a80 ["CALL", null, ["callee:00c57a80:8"]]
- 00842794 bytes 27620e94
+ 00874a80 bytes 008c0f94
~~~


<a id="compare-e3b2d60bddabc1b798ae049f803e51bd"></a>

### [`008427e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008427e0.md) → [`00874acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874acc.md) FUN_00874acc

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008427fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008427e0.md#insn-008427fc) · [`0084281c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008427e0.md#insn-0084281c)
- 新版 `00874ae8`（命令位置の公開資料なし） · `00874b08`（命令位置の公開資料なし）

~~~diff
- 008427fc ["INT_ADD", "register:40f0:8", ["const:8427fc:8", "const:4:8"]]
- 008427fc ["CALL", null, ["callee:00c538e0:8"]]
+ 00874ae8 ["INT_ADD", "register:40f0:8", ["const:874ae8:8", "const:4:8"]]
+ 00874ae8 ["CALL", null, ["callee:00c538e0:8"]]
- 008427fc bytes a5510e94
+ 00874ae8 bytes 7e7b0f94
- 0084281c ["COPY", "register:0:8", ["register:4040:8"]]
- 0084281c ["INT_ADD", "register:40f0:8", ["const:84281c:8", "const:4:8"]]
- 0084281c ["CALLIND", null, ["register:0:8"]]
+ 00874b08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874b08 ["INT_ADD", "register:40f0:8", ["const:874b08:8", "const:4:8"]]
+ 00874b08 ["CALLIND", null, ["register:0:8"]]
- 0084281c bytes 00013fd6
+ 00874b08 bytes 00013fd6
~~~


<a id="compare-9c760513ca52e7485f67cccf0d765e9b"></a>

### [`0084297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084297c.md) → [`00874c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md) FUN_00874c68

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084297c.md#insn-00842998) · [`008429b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084297c.md#insn-008429b8)
- 新版 `00874c84`（命令位置の公開資料なし） · `00874ca4`（命令位置の公開資料なし）

~~~diff
- 00842998 ["INT_ADD", "register:40f0:8", ["const:842998:8", "const:4:8"]]
- 00842998 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874c84 ["INT_ADD", "register:40f0:8", ["const:874c84:8", "const:4:8"]]
+ 00874c84 ["CALL", null, ["callee:00c538e0:8"]]
- 00842998 bytes 3e510e94
+ 00874c84 bytes 177b0f94
- 008429b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008429b8 ["INT_ADD", "register:40f0:8", ["const:8429b8:8", "const:4:8"]]
- 008429b8 ["CALLIND", null, ["register:0:8"]]
+ 00874ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ca4 ["INT_ADD", "register:40f0:8", ["const:874ca4:8", "const:4:8"]]
+ 00874ca4 ["CALLIND", null, ["register:0:8"]]
- 008429b8 bytes 00013fd6
+ 00874ca4 bytes 00013fd6
~~~


<a id="compare-fb39deee9d0124034204efb73af6d4e6"></a>

### [`008429cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md) → [`00874cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md) FUN_00874cb8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008429ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md#insn-008429ec) · [`00842a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md#insn-00842a00) · [`00842a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md#insn-00842a08)
- 新版 `00874cd8`（命令位置の公開資料なし） · `00874cec`（命令位置の公開資料なし） · `00874cf4`（命令位置の公開資料なし）

~~~diff
- 008429ec ["INT_ADD", "register:40f0:8", ["const:8429ec:8", "const:4:8"]]
- 008429ec ["CALL", null, ["callee:00c538e0:8"]]
+ 00874cd8 ["INT_ADD", "register:40f0:8", ["const:874cd8:8", "const:4:8"]]
+ 00874cd8 ["CALL", null, ["callee:00c538e0:8"]]
- 008429ec bytes 29510e94
+ 00874cd8 bytes 027b0f94
- 00842a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00842a00 ["INT_ADD", "register:40f0:8", ["const:842a00:8", "const:4:8"]]
- 00842a00 ["CALLIND", null, ["register:0:8"]]
+ 00874cec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874cec ["INT_ADD", "register:40f0:8", ["const:874cec:8", "const:4:8"]]
+ 00874cec ["CALLIND", null, ["register:0:8"]]
- 00842a00 bytes 00013fd6
+ 00874cec bytes 00013fd6
- 00842a08 ["INT_ADD", "register:40f0:8", ["const:842a08:8", "const:4:8"]]
- 00842a08 ["CALL", null, ["callee:00c57a80:8"]]
+ 00874cf4 ["INT_ADD", "register:40f0:8", ["const:874cf4:8", "const:4:8"]]
+ 00874cf4 ["CALL", null, ["callee:00c57a80:8"]]
- 00842a08 bytes 8a610e94
+ 00874cf4 bytes 638b0f94
~~~


<a id="compare-46b870cbd0177f9026b5887f928d8336"></a>

### [`00842c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c18.md) → [`00874f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f04.md) FUN_00874f04

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c18.md#insn-00842c34) · [`00842c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c18.md#insn-00842c54)
- 新版 `00874f20`（命令位置の公開資料なし） · `00874f40`（命令位置の公開資料なし）

~~~diff
- 00842c34 ["INT_ADD", "register:40f0:8", ["const:842c34:8", "const:4:8"]]
- 00842c34 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874f20 ["INT_ADD", "register:40f0:8", ["const:874f20:8", "const:4:8"]]
+ 00874f20 ["CALL", null, ["callee:00c538e0:8"]]
- 00842c34 bytes 97500e94
+ 00874f20 bytes 707a0f94
- 00842c54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00842c54 ["INT_ADD", "register:40f0:8", ["const:842c54:8", "const:4:8"]]
- 00842c54 ["CALLIND", null, ["register:0:8"]]
+ 00874f40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874f40 ["INT_ADD", "register:40f0:8", ["const:874f40:8", "const:4:8"]]
+ 00874f40 ["CALLIND", null, ["register:0:8"]]
- 00842c54 bytes 00013fd6
+ 00874f40 bytes 00013fd6
~~~


<a id="compare-5eb046b5eb98c616efbe05b095515b29"></a>

### [`00842db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842db4.md) → [`008750a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md) FUN_008750a0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842db4.md#insn-00842dd0) · [`00842df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842db4.md#insn-00842df0)
- 新版 `008750bc`（命令位置の公開資料なし） · `008750dc`（命令位置の公開資料なし）

~~~diff
- 00842dd0 ["INT_ADD", "register:40f0:8", ["const:842dd0:8", "const:4:8"]]
- 00842dd0 ["CALL", null, ["callee:00c538e0:8"]]
+ 008750bc ["INT_ADD", "register:40f0:8", ["const:8750bc:8", "const:4:8"]]
+ 008750bc ["CALL", null, ["callee:00c538e0:8"]]
- 00842dd0 bytes 30500e94
+ 008750bc bytes 097a0f94
- 00842df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00842df0 ["INT_ADD", "register:40f0:8", ["const:842df0:8", "const:4:8"]]
- 00842df0 ["CALLIND", null, ["register:0:8"]]
+ 008750dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008750dc ["INT_ADD", "register:40f0:8", ["const:8750dc:8", "const:4:8"]]
+ 008750dc ["CALLIND", null, ["register:0:8"]]
- 00842df0 bytes 00013fd6
+ 008750dc bytes 00013fd6
~~~


<a id="compare-26477c871018c046eb9b7a1a3c44993c"></a>

### [`00842e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md) → [`008750f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md) FUN_008750f0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00842e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md#insn-00842e24) · [`00842e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md#insn-00842e38) · [`00842e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md#insn-00842e40)
- 新版 `00875110`（命令位置の公開資料なし） · `00875124`（命令位置の公開資料なし） · `0087512c`（命令位置の公開資料なし）

~~~diff
- 00842e24 ["INT_ADD", "register:40f0:8", ["const:842e24:8", "const:4:8"]]
- 00842e24 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875110 ["INT_ADD", "register:40f0:8", ["const:875110:8", "const:4:8"]]
+ 00875110 ["CALL", null, ["callee:00c538e0:8"]]
- 00842e24 bytes 1b500e94
+ 00875110 bytes f4790f94
- 00842e38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00842e38 ["INT_ADD", "register:40f0:8", ["const:842e38:8", "const:4:8"]]
- 00842e38 ["CALLIND", null, ["register:0:8"]]
+ 00875124 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875124 ["INT_ADD", "register:40f0:8", ["const:875124:8", "const:4:8"]]
+ 00875124 ["CALLIND", null, ["register:0:8"]]
- 00842e38 bytes 00013fd6
+ 00875124 bytes 00013fd6
- 00842e40 ["INT_ADD", "register:40f0:8", ["const:842e40:8", "const:4:8"]]
- 00842e40 ["CALL", null, ["callee:00c57a80:8"]]
+ 0087512c ["INT_ADD", "register:40f0:8", ["const:87512c:8", "const:4:8"]]
+ 0087512c ["CALL", null, ["callee:00c57a80:8"]]
- 00842e40 bytes 7c600e94
+ 0087512c bytes 558a0f94
~~~


<a id="compare-ca99349b96af18aca32648f6ff7b4c0f"></a>

### [`008430b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md) → [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md) FUN_0087539c

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`008432f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008755dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00843140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md#insn-00843140) · [`0084319c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md#insn-0084319c) · [`008431ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md#insn-008431ec)
- 新版 `0087542c`（命令位置の公開資料なし） · `00875488`（命令位置の公開資料なし） · `008754d8`（命令位置の公開資料なし）

~~~diff
- 00843140 ["INT_ADD", "register:40f0:8", ["const:843140:8", "const:4:8"]]
- 00843140 ["CALL", null, ["callee:00c57c50:8"]]
+ 0087542c ["INT_ADD", "register:40f0:8", ["const:87542c:8", "const:4:8"]]
+ 0087542c ["CALL", null, ["callee:00c57c50:8"]]
- 00843140 bytes 30600e94
+ 0087542c bytes 098a0f94
- 0084319c ["INT_ADD", "register:40f0:8", ["const:84319c:8", "const:4:8"]]
- 0084319c ["CALL", null, ["callee:00c57c50:8"]]
+ 00875488 ["INT_ADD", "register:40f0:8", ["const:875488:8", "const:4:8"]]
+ 00875488 ["CALL", null, ["callee:00c57c50:8"]]
- 0084319c bytes 19600e94
+ 00875488 bytes f2890f94
- 008431ec ["INT_ADD", "register:40f0:8", ["const:8431ec:8", "const:4:8"]]
- 008431ec ["CALL", null, ["callee:008755dc:8"]]
+ 008754d8 ["INT_ADD", "register:40f0:8", ["const:8754d8:8", "const:4:8"]]
+ 008754d8 ["CALL", null, ["callee:008755dc:8"]]
- 008431ec bytes 41000094
+ 008754d8 bytes 41000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9980cd49f65f6a6d61b2a46f989bab14"></a>

### [`00843c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c8c.md) → [`00875f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md) FUN_00875f78

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00843ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c8c.md#insn-00843ca8) · [`00843cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c8c.md#insn-00843cc8)
- 新版 `00875f94`（命令位置の公開資料なし） · `00875fb4`（命令位置の公開資料なし）

~~~diff
- 00843ca8 ["INT_ADD", "register:40f0:8", ["const:843ca8:8", "const:4:8"]]
- 00843ca8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875f94 ["INT_ADD", "register:40f0:8", ["const:875f94:8", "const:4:8"]]
+ 00875f94 ["CALL", null, ["callee:00c538e0:8"]]
- 00843ca8 bytes 7a4c0e94
+ 00875f94 bytes 53760f94
- 00843cc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00843cc8 ["INT_ADD", "register:40f0:8", ["const:843cc8:8", "const:4:8"]]
- 00843cc8 ["CALLIND", null, ["register:0:8"]]
+ 00875fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875fb4 ["INT_ADD", "register:40f0:8", ["const:875fb4:8", "const:4:8"]]
+ 00875fb4 ["CALLIND", null, ["register:0:8"]]
- 00843cc8 bytes 00013fd6
+ 00875fb4 bytes 00013fd6
~~~


<a id="compare-e06003199bc421e9cf086a209ddda0c1"></a>

### [`008458f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008458f4.md) → [`00877be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md) FUN_00877be0

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00845594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845594.md) · 呼出先 5件 [`0046866c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00877880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877880.md) · 呼出先 5件 [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00845938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008458f4.md#insn-00845938) · [`00845980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008458f4.md#insn-00845980) · [`008459a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008458f4.md#insn-008459a8)
- 新版 `00877c24`（命令位置の公開資料なし） · `00877c6c`（命令位置の公開資料なし） · `00877c94`（命令位置の公開資料なし）

~~~diff
- 00845938 ["INT_ADD", "register:40f0:8", ["const:845938:8", "const:4:8"]]
- 00845938 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00877c24 ["INT_ADD", "register:40f0:8", ["const:877c24:8", "const:4:8"]]
+ 00877c24 ["CALL", null, ["callee:00c57ab0:8"]]
- 00845938 bytes ca550e94
+ 00877c24 bytes a37f0f94
- 00845980 ["INT_ADD", "register:40f0:8", ["const:845980:8", "const:4:8"]]
- 00845980 ["CALL", null, ["callee:00c57a90:8"]]
+ 00877c6c ["INT_ADD", "register:40f0:8", ["const:877c6c:8", "const:4:8"]]
+ 00877c6c ["CALL", null, ["callee:00c57a90:8"]]
- 00845980 bytes b0550e94
+ 00877c6c bytes 897f0f94
- 008459a8 ["INT_ADD", "register:40f0:8", ["const:8459a8:8", "const:4:8"]]
- 008459a8 ["CALL", null, ["callee:00c57c00:8"]]
+ 00877c94 ["INT_ADD", "register:40f0:8", ["const:877c94:8", "const:4:8"]]
+ 00877c94 ["CALL", null, ["callee:00c57c00:8"]]
- 008459a8 bytes 02560e94
+ 00877c94 bytes db7f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be02e9716bce7c3601a350bb212c2fa"></a>

### [`00845f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f00.md) → [`008781ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md) FUN_008781ec

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008168a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008168a0.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`00822930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822930.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00848698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848698.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00845f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f00.md#insn-00845f10) · [`00845f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f00.md#insn-00845f20)
- 新版 `008781fc`（命令位置の公開資料なし） · `0087820c`（命令位置の公開資料なし）

~~~diff
- 00845f10 ["INT_ADD", "register:40f0:8", ["const:845f10:8", "const:4:8"]]
- 00845f10 ["CALL", null, ["callee:00c5a540:8"]]
+ 008781fc ["INT_ADD", "register:40f0:8", ["const:8781fc:8", "const:4:8"]]
+ 008781fc ["CALL", null, ["callee:00c5a540:8"]]
- 00845f10 bytes f85e0e94
+ 008781fc bytes d1880f94
- 00845f20 ["INT_ADD", "register:40f0:8", ["const:845f20:8", "const:4:8"]]
- 00845f20 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0087820c ["INT_ADD", "register:40f0:8", ["const:87820c:8", "const:4:8"]]
+ 0087820c ["CALL", null, ["callee:00c57ab0:8"]]
- 00845f20 bytes 50540e94
+ 0087820c bytes 297e0f94
~~~


<a id="compare-3b604570dc22fb01687f6e80d801b37a"></a>

### [`00849430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849430.md) → [`0087bee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bee8.md) FUN_0087bee8

採用 · 移動量 `+0x32ab8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849430.md#insn-00849470)
- 新版 `0087bf28`（命令位置の公開資料なし）

~~~diff
- 00849470 ["COPY", "register:0:8", ["register:4040:8"]]
- 00849470 ["INT_ADD", "register:40f0:8", ["const:849470:8", "const:4:8"]]
- 00849470 ["CALLIND", null, ["register:0:8"]]
+ 0087bf28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bf28 ["INT_ADD", "register:40f0:8", ["const:87bf28:8", "const:4:8"]]
+ 0087bf28 ["CALLIND", null, ["register:0:8"]]
- 00849470 bytes 00013fd6
+ 0087bf28 bytes 00013fd6
~~~


<a id="compare-c54df84c922a014af7d0a4e31d635e3e"></a>

### [`00849c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849c54.md) → [`0087cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087cbec.md) FUN_0087cbec

採用 · 移動量 `+0x32f98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/0084859c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849c54.md#insn-00849c94) · [`00849cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849c54.md#insn-00849cc0)
- 新版 `0087cc2c`（命令位置の公開資料なし） · `0087cc58`（命令位置の公開資料なし）

~~~diff
- 00849c94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00849c94 ["INT_ADD", "register:40f0:8", ["const:849c94:8", "const:4:8"]]
- 00849c94 ["CALLIND", null, ["register:0:8"]]
+ 0087cc2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cc2c ["INT_ADD", "register:40f0:8", ["const:87cc2c:8", "const:4:8"]]
+ 0087cc2c ["CALLIND", null, ["register:0:8"]]
- 00849c94 bytes 00013fd6
+ 0087cc2c bytes 00013fd6
- 00849cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00849cc0 ["INT_ADD", "register:40f0:8", ["const:849cc0:8", "const:4:8"]]
- 00849cc0 ["CALLIND", null, ["register:0:8"]]
+ 0087cc58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cc58 ["INT_ADD", "register:40f0:8", ["const:87cc58:8", "const:4:8"]]
+ 0087cc58 ["CALLIND", null, ["register:0:8"]]
- 00849cc0 bytes 00013fd6
+ 0087cc58 bytes 00013fd6
~~~


<a id="compare-1e705c931912bab5ae51e32db8cc7b4f"></a>

### [`0084a2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a2a4.md) → [`0087d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d23c.md) FUN_0087d23c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084a2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a2a4.md#insn-0084a2b4)
- 新版 `0087d24c`（命令位置の公開資料なし）

~~~diff
- 0084a2b4 ["INT_ADD", "register:40f0:8", ["const:84a2b4:8", "const:4:8"]]
- 0084a2b4 ["CALL", null, ["callee:00c5a6c0:8"]]
+ 0087d24c ["INT_ADD", "register:40f0:8", ["const:87d24c:8", "const:4:8"]]
+ 0087d24c ["CALL", null, ["callee:00c5a6c0:8"]]
- 0084a2b4 bytes 6f4e0e94
+ 0087d24c bytes 1d750f94
~~~


<a id="compare-66632c71026133a024682a157f6811c5"></a>

### [`0084b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b704.md) → [`0087e69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e69c.md) FUN_0087e69c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 1件 [`0084bbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md)
- 新版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 1件 [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084b71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b704.md#insn-0084b71c)
- 新版 `0087e6b4`（命令位置の公開資料なし）

~~~diff
- 0084b71c ["INT_ADD", "register:40f0:8", ["const:84b71c:8", "const:4:8"]]
- 0084b71c ["CALL", null, ["callee:0087eb7c:8"]]
+ 0087e6b4 ["INT_ADD", "register:40f0:8", ["const:87e6b4:8", "const:4:8"]]
+ 0087e6b4 ["CALL", null, ["callee:0087eb7c:8"]]
- 0084b71c bytes 32010094
+ 0087e6b4 bytes 32010094
~~~


<a id="compare-a681565ff4b0be1368d96a76d2f8c4c4"></a>

### [`0084bae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bae8.md) → [`0087ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ea80.md) FUN_0087ea80

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00739a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739a10.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 2件 [`0084a918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a918.md) [`0084bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bc70.md)
- 新版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00763d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763d18.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0087d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md) [`0087ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084bb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bae8.md#insn-0084bb08) · [`0084bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bae8.md#insn-0084bb1c)
- 新版 `0087eaa0`（命令位置の公開資料なし） · `0087eab4`（命令位置の公開資料なし）

~~~diff
- 0084bb08 ["INT_ADD", "register:40f0:8", ["const:84bb08:8", "const:4:8"]]
- 0084bb08 ["CALL", null, ["callee:0087ec08:8"]]
+ 0087eaa0 ["INT_ADD", "register:40f0:8", ["const:87eaa0:8", "const:4:8"]]
+ 0087eaa0 ["CALL", null, ["callee:0087ec08:8"]]
- 0084bb08 bytes 5a000094
+ 0087eaa0 bytes 5a000094
- 0084bb1c ["INT_ADD", "register:40f0:8", ["const:84bb1c:8", "const:4:8"]]
- 0084bb1c ["CALL", null, ["callee:0087d8b0:8"]]
+ 0087eab4 ["INT_ADD", "register:40f0:8", ["const:87eab4:8", "const:4:8"]]
+ 0087eab4 ["CALL", null, ["callee:0087d8b0:8"]]
- 0084bb1c bytes 7ffbff97
+ 0087eab4 bytes 7ffbff97
~~~


<a id="compare-723e1f8938d1368c0d6f9001bda52e63"></a>

### [`0084bb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bb48.md) → [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) FUN_0087eae0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009969b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/009969b8.md) · 呼出先 2件 [`0084a9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a9ec.md) [`0084bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bc70.md)
- 新版 呼出元 1件 [`009cc4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc4ac.md) · 呼出先 2件 [`0087d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md) [`0087ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ec08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084bb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bb48.md#insn-0084bb60)
- 新版 `0087eaf8`（命令位置の公開資料なし）

~~~diff
- 0084bb60 ["INT_ADD", "register:40f0:8", ["const:84bb60:8", "const:4:8"]]
- 0084bb60 ["CALL", null, ["callee:0087ec08:8"]]
+ 0087eaf8 ["INT_ADD", "register:40f0:8", ["const:87eaf8:8", "const:4:8"]]
+ 0087eaf8 ["CALL", null, ["callee:0087ec08:8"]]
- 0084bb60 bytes 44000094
+ 0087eaf8 bytes 44000094
~~~


<a id="compare-1659ba941a0643ef91a9bde515c6012e"></a>

### [`0084c0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md) → [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) FUN_0087f064

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0084c0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md) [`00b590b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md) · 呼出先 3件 [`0084c0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 2件 [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00bc85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md) · 呼出先 3件 [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084c0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md#insn-0084c0e8) · [`0084c0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md#insn-0084c0f4) · [`0084c100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md#insn-0084c100)
- 新版 `0087f080`（命令位置の公開資料なし） · `0087f08c`（命令位置の公開資料なし） · `0087f098`（命令位置の公開資料なし）

~~~diff
- 0084c0e8 ["INT_ADD", "register:40f0:8", ["const:84c0e8:8", "const:4:8"]]
- 0084c0e8 ["CALL", null, ["local:b0:8"]]
+ 0087f080 ["INT_ADD", "register:40f0:8", ["const:87f080:8", "const:4:8"]]
+ 0087f080 ["CALL", null, ["local:b0:8"]]
- 0084c0e8 bytes f9ffff97
+ 0087f080 bytes f9ffff97
- 0084c0f4 ["INT_ADD", "register:40f0:8", ["const:84c0f4:8", "const:4:8"]]
- 0084c0f4 ["CALL", null, ["local:b0:8"]]
+ 0087f08c ["INT_ADD", "register:40f0:8", ["const:87f08c:8", "const:4:8"]]
+ 0087f08c ["CALL", null, ["local:b0:8"]]
- 0084c0f4 bytes f6ffff97
+ 0087f08c bytes f6ffff97
- 0084c100 ["INT_ADD", "register:40f0:8", ["const:84c100:8", "const:4:8"]]
- 0084c100 ["CALL", null, ["callee:00c5a430:8"]]
+ 0087f098 ["INT_ADD", "register:40f0:8", ["const:87f098:8", "const:4:8"]]
+ 0087f098 ["CALL", null, ["callee:00c5a430:8"]]
- 0084c100 bytes 38460e94
+ 0087f098 bytes e66c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1745a5da96a13a9c8291e7af1364150e"></a>

### [`0084ec54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084ec54.md) → [`00881bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881bec.md) FUN_00881bec

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084ec70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084ec54.md#insn-0084ec70) · [`0084ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084ec54.md#insn-0084ec90)
- 新版 `00881c08`（命令位置の公開資料なし） · `00881c28`（命令位置の公開資料なし）

~~~diff
- 0084ec70 ["INT_ADD", "register:40f0:8", ["const:84ec70:8", "const:4:8"]]
- 0084ec70 ["CALL", null, ["callee:00c538e0:8"]]
+ 00881c08 ["INT_ADD", "register:40f0:8", ["const:881c08:8", "const:4:8"]]
+ 00881c08 ["CALL", null, ["callee:00c538e0:8"]]
- 0084ec70 bytes 88200e94
+ 00881c08 bytes 36470f94
- 0084ec90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084ec90 ["INT_ADD", "register:40f0:8", ["const:84ec90:8", "const:4:8"]]
- 0084ec90 ["CALLIND", null, ["register:0:8"]]
+ 00881c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00881c28 ["INT_ADD", "register:40f0:8", ["const:881c28:8", "const:4:8"]]
+ 00881c28 ["CALLIND", null, ["register:0:8"]]
- 0084ec90 bytes 00013fd6
+ 00881c28 bytes 00013fd6
~~~


<a id="compare-e1651ae48cbc1dcfe5eed5a5dcfc2ad9"></a>

### [`0084f63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f63c.md) → [`008825d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008825d4.md) FUN_008825d4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084f678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f63c.md#insn-0084f678)
- 新版 `00882610`（命令位置の公開資料なし）

~~~diff
- 0084f678 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084f678 ["INT_ADD", "register:40f0:8", ["const:84f678:8", "const:4:8"]]
- 0084f678 ["CALLIND", null, ["register:0:8"]]
+ 00882610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00882610 ["INT_ADD", "register:40f0:8", ["const:882610:8", "const:4:8"]]
+ 00882610 ["CALLIND", null, ["register:0:8"]]
- 0084f678 bytes 00013fd6
+ 00882610 bytes 00013fd6
~~~


<a id="compare-78e5e82b5c083e49cec4cba1496751cc"></a>

### [`00850a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850a7c.md) → [`00883a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a14.md) FUN_00883a14

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00850ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850a7c.md#insn-00850ab8) · [`00850acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850a7c.md#insn-00850acc) · [`00850ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850a7c.md#insn-00850ae0)
- 新版 `00883a50`（命令位置の公開資料なし） · `00883a64`（命令位置の公開資料なし） · `00883a78`（命令位置の公開資料なし）

~~~diff
- 00850ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00850ab8 ["INT_ADD", "register:40f0:8", ["const:850ab8:8", "const:4:8"]]
- 00850ab8 ["CALLIND", null, ["register:0:8"]]
+ 00883a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a50 ["INT_ADD", "register:40f0:8", ["const:883a50:8", "const:4:8"]]
+ 00883a50 ["CALLIND", null, ["register:0:8"]]
- 00850ab8 bytes 00013fd6
+ 00883a50 bytes 00013fd6
- 00850acc ["INT_ADD", "register:40f0:8", ["const:850acc:8", "const:4:8"]]
- 00850acc ["CALL", null, ["callee:00c538e0:8"]]
+ 00883a64 ["INT_ADD", "register:40f0:8", ["const:883a64:8", "const:4:8"]]
+ 00883a64 ["CALL", null, ["callee:00c538e0:8"]]
- 00850acc bytes f1180e94
+ 00883a64 bytes 9f3f0f94
- 00850ae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00850ae0 ["INT_ADD", "register:40f0:8", ["const:850ae0:8", "const:4:8"]]
- 00850ae0 ["CALLIND", null, ["register:0:8"]]
+ 00883a78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00883a78 ["INT_ADD", "register:40f0:8", ["const:883a78:8", "const:4:8"]]
+ 00883a78 ["CALLIND", null, ["register:0:8"]]
- 00850ae0 bytes 00013fd6
+ 00883a78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88252408fb32eef799d6546870dfb6b"></a>

### [`00851050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851050.md) → [`00883fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883fe8.md) FUN_00883fe8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085108c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851050.md#insn-0085108c) · [`008510a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851050.md#insn-008510a0) · [`008510c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851050.md#insn-008510c0)
- 新版 `00884024`（命令位置の公開資料なし） · `00884038`（命令位置の公開資料なし） · `00884058`（命令位置の公開資料なし）

~~~diff
- 0085108c ["COPY", "register:0:8", ["register:4040:8"]]
- 0085108c ["INT_ADD", "register:40f0:8", ["const:85108c:8", "const:4:8"]]
- 0085108c ["CALLIND", null, ["register:0:8"]]
+ 00884024 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884024 ["INT_ADD", "register:40f0:8", ["const:884024:8", "const:4:8"]]
+ 00884024 ["CALLIND", null, ["register:0:8"]]
- 0085108c bytes 00013fd6
+ 00884024 bytes 00013fd6
- 008510a0 ["INT_ADD", "register:40f0:8", ["const:8510a0:8", "const:4:8"]]
- 008510a0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00884038 ["INT_ADD", "register:40f0:8", ["const:884038:8", "const:4:8"]]
+ 00884038 ["CALL", null, ["callee:00c538e0:8"]]
- 008510a0 bytes 7c170e94
+ 00884038 bytes 2a3e0f94
- 008510c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008510c0 ["INT_ADD", "register:40f0:8", ["const:8510c0:8", "const:4:8"]]
- 008510c0 ["CALLIND", null, ["register:0:8"]]
+ 00884058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884058 ["INT_ADD", "register:40f0:8", ["const:884058:8", "const:4:8"]]
+ 00884058 ["CALLIND", null, ["register:0:8"]]
- 008510c0 bytes 00013fd6
+ 00884058 bytes 00013fd6
~~~


<a id="compare-6cf33392c24e82e0e80feeff76a63bfc"></a>

### [`008513c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008513c4.md) → [`0088435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088435c.md) FUN_0088435c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00850afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00851400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008513c4.md#insn-00851400) · [`00851414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008513c4.md#insn-00851414) · [`00851428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008513c4.md#insn-00851428)
- 新版 `00884398`（命令位置の公開資料なし） · `008843ac`（命令位置の公開資料なし） · `008843c0`（命令位置の公開資料なし）

~~~diff
- 00851400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00851400 ["INT_ADD", "register:40f0:8", ["const:851400:8", "const:4:8"]]
- 00851400 ["CALLIND", null, ["register:0:8"]]
+ 00884398 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884398 ["INT_ADD", "register:40f0:8", ["const:884398:8", "const:4:8"]]
+ 00884398 ["CALLIND", null, ["register:0:8"]]
- 00851400 bytes 00013fd6
+ 00884398 bytes 00013fd6
- 00851414 ["INT_ADD", "register:40f0:8", ["const:851414:8", "const:4:8"]]
- 00851414 ["CALL", null, ["callee:00c538e0:8"]]
+ 008843ac ["INT_ADD", "register:40f0:8", ["const:8843ac:8", "const:4:8"]]
+ 008843ac ["CALL", null, ["callee:00c538e0:8"]]
- 00851414 bytes 9f160e94
+ 008843ac bytes 4d3d0f94
- 00851428 ["COPY", "register:0:8", ["register:4040:8"]]
- 00851428 ["INT_ADD", "register:40f0:8", ["const:851428:8", "const:4:8"]]
- 00851428 ["CALLIND", null, ["register:0:8"]]
+ 008843c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008843c0 ["INT_ADD", "register:40f0:8", ["const:8843c0:8", "const:4:8"]]
+ 008843c0 ["CALLIND", null, ["register:0:8"]]
- 00851428 bytes 00013fd6
+ 008843c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be80cc466339a5cca9b7c912a07acd78"></a>

### [`0085228c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085228c.md) → [`00885224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885224.md) FUN_00885224

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008522c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085228c.md#insn-008522c8) · [`008522dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085228c.md#insn-008522dc) · [`008522fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085228c.md#insn-008522fc)
- 新版 `00885260`（命令位置の公開資料なし） · `00885274`（命令位置の公開資料なし） · `00885294`（命令位置の公開資料なし）

~~~diff
- 008522c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008522c8 ["INT_ADD", "register:40f0:8", ["const:8522c8:8", "const:4:8"]]
- 008522c8 ["CALLIND", null, ["register:0:8"]]
+ 00885260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885260 ["INT_ADD", "register:40f0:8", ["const:885260:8", "const:4:8"]]
+ 00885260 ["CALLIND", null, ["register:0:8"]]
- 008522c8 bytes 00013fd6
+ 00885260 bytes 00013fd6
- 008522dc ["INT_ADD", "register:40f0:8", ["const:8522dc:8", "const:4:8"]]
- 008522dc ["CALL", null, ["callee:00c538e0:8"]]
+ 00885274 ["INT_ADD", "register:40f0:8", ["const:885274:8", "const:4:8"]]
+ 00885274 ["CALL", null, ["callee:00c538e0:8"]]
- 008522dc bytes ed120e94
+ 00885274 bytes 9b390f94
- 008522fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008522fc ["INT_ADD", "register:40f0:8", ["const:8522fc:8", "const:4:8"]]
- 008522fc ["CALLIND", null, ["register:0:8"]]
+ 00885294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885294 ["INT_ADD", "register:40f0:8", ["const:885294:8", "const:4:8"]]
+ 00885294 ["CALLIND", null, ["register:0:8"]]
- 008522fc bytes 00013fd6
+ 00885294 bytes 00013fd6
~~~


<a id="compare-aebd8b1cfe3191131d76a1f6793cba52"></a>

### [`00852310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852310.md) → [`008852a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008852a8.md) FUN_008852a8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00851b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851b9c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00884b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085234c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852310.md#insn-0085234c) · [`00852360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852310.md#insn-00852360) · [`00852374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852310.md#insn-00852374)
- 新版 `008852e4`（命令位置の公開資料なし） · `008852f8`（命令位置の公開資料なし） · `0088530c`（命令位置の公開資料なし）

~~~diff
- 0085234c ["COPY", "register:0:8", ["register:4040:8"]]
- 0085234c ["INT_ADD", "register:40f0:8", ["const:85234c:8", "const:4:8"]]
- 0085234c ["CALLIND", null, ["register:0:8"]]
+ 008852e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008852e4 ["INT_ADD", "register:40f0:8", ["const:8852e4:8", "const:4:8"]]
+ 008852e4 ["CALLIND", null, ["register:0:8"]]
- 0085234c bytes 00013fd6
+ 008852e4 bytes 00013fd6
- 00852360 ["INT_ADD", "register:40f0:8", ["const:852360:8", "const:4:8"]]
- 00852360 ["CALL", null, ["callee:00c538e0:8"]]
+ 008852f8 ["INT_ADD", "register:40f0:8", ["const:8852f8:8", "const:4:8"]]
+ 008852f8 ["CALL", null, ["callee:00c538e0:8"]]
- 00852360 bytes cc120e94
+ 008852f8 bytes 7a390f94
- 00852374 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852374 ["INT_ADD", "register:40f0:8", ["const:852374:8", "const:4:8"]]
- 00852374 ["CALLIND", null, ["register:0:8"]]
+ 0088530c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088530c ["INT_ADD", "register:40f0:8", ["const:88530c:8", "const:4:8"]]
+ 0088530c ["CALLIND", null, ["register:0:8"]]
- 00852374 bytes 00013fd6
+ 0088530c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d65e8260ebc623d92a2f8673a183ac0"></a>

### [`00852634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852634.md) → [`008855cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008855cc.md) FUN_008855cc

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085265c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852634.md#insn-0085265c) · [`00852670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852634.md#insn-00852670) · [`00852678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852634.md#insn-00852678)
- 新版 `008855f4`（命令位置の公開資料なし） · `00885608`（命令位置の公開資料なし） · `00885610`（命令位置の公開資料なし）

~~~diff
- 0085265c ["INT_ADD", "register:40f0:8", ["const:85265c:8", "const:4:8"]]
- 0085265c ["CALL", null, ["callee:00c538e0:8"]]
+ 008855f4 ["INT_ADD", "register:40f0:8", ["const:8855f4:8", "const:4:8"]]
+ 008855f4 ["CALL", null, ["callee:00c538e0:8"]]
- 0085265c bytes 0d120e94
+ 008855f4 bytes bb380f94
- 00852670 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852670 ["INT_ADD", "register:40f0:8", ["const:852670:8", "const:4:8"]]
- 00852670 ["CALLIND", null, ["register:0:8"]]
+ 00885608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885608 ["INT_ADD", "register:40f0:8", ["const:885608:8", "const:4:8"]]
+ 00885608 ["CALLIND", null, ["register:0:8"]]
- 00852670 bytes 00013fd6
+ 00885608 bytes 00013fd6
- 00852678 ["INT_ADD", "register:40f0:8", ["const:852678:8", "const:4:8"]]
- 00852678 ["CALL", null, ["callee:00c57a80:8"]]
+ 00885610 ["INT_ADD", "register:40f0:8", ["const:885610:8", "const:4:8"]]
+ 00885610 ["CALL", null, ["callee:00c57a80:8"]]
- 00852678 bytes 6e220e94
+ 00885610 bytes 1c490f94
~~~


<a id="compare-2999a84ac383fcf9db71c1f2a8b8faf6"></a>

### [`008526c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008526c4.md) → [`0088565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/0088565c.md) FUN_0088565c

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008526ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008526c4.md#insn-008526ec) · [`00852700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008526c4.md#insn-00852700) · [`00852708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008526c4.md#insn-00852708)
- 新版 `00885684`（命令位置の公開資料なし） · `00885698`（命令位置の公開資料なし） · `008856a0`（命令位置の公開資料なし）

~~~diff
- 008526ec ["INT_ADD", "register:40f0:8", ["const:8526ec:8", "const:4:8"]]
- 008526ec ["CALL", null, ["callee:00c538e0:8"]]
+ 00885684 ["INT_ADD", "register:40f0:8", ["const:885684:8", "const:4:8"]]
+ 00885684 ["CALL", null, ["callee:00c538e0:8"]]
- 008526ec bytes e9110e94
+ 00885684 bytes 97380f94
- 00852700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852700 ["INT_ADD", "register:40f0:8", ["const:852700:8", "const:4:8"]]
- 00852700 ["CALLIND", null, ["register:0:8"]]
+ 00885698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885698 ["INT_ADD", "register:40f0:8", ["const:885698:8", "const:4:8"]]
+ 00885698 ["CALLIND", null, ["register:0:8"]]
- 00852700 bytes 00013fd6
+ 00885698 bytes 00013fd6
- 00852708 ["INT_ADD", "register:40f0:8", ["const:852708:8", "const:4:8"]]
- 00852708 ["CALL", null, ["callee:00c57a80:8"]]
+ 008856a0 ["INT_ADD", "register:40f0:8", ["const:8856a0:8", "const:4:8"]]
+ 008856a0 ["CALL", null, ["callee:00c57a80:8"]]
- 00852708 bytes 4a220e94
+ 008856a0 bytes f8480f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e13624b00c4d042c6e1cdbeef1a539"></a>

### [`00852ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ab8.md) → [`00885a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885a50.md) FUN_00885a50

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00852af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ab8.md#insn-00852af4) · [`00852b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ab8.md#insn-00852b08) · [`00852b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ab8.md#insn-00852b28)
- 新版 `00885a8c`（命令位置の公開資料なし） · `00885aa0`（命令位置の公開資料なし） · `00885ac0`（命令位置の公開資料なし）

~~~diff
- 00852af4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852af4 ["INT_ADD", "register:40f0:8", ["const:852af4:8", "const:4:8"]]
- 00852af4 ["CALLIND", null, ["register:0:8"]]
+ 00885a8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885a8c ["INT_ADD", "register:40f0:8", ["const:885a8c:8", "const:4:8"]]
+ 00885a8c ["CALLIND", null, ["register:0:8"]]
- 00852af4 bytes 00013fd6
+ 00885a8c bytes 00013fd6
- 00852b08 ["INT_ADD", "register:40f0:8", ["const:852b08:8", "const:4:8"]]
- 00852b08 ["CALL", null, ["callee:00c538e0:8"]]
+ 00885aa0 ["INT_ADD", "register:40f0:8", ["const:885aa0:8", "const:4:8"]]
+ 00885aa0 ["CALL", null, ["callee:00c538e0:8"]]
- 00852b08 bytes e2100e94
+ 00885aa0 bytes 90370f94
- 00852b28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852b28 ["INT_ADD", "register:40f0:8", ["const:852b28:8", "const:4:8"]]
- 00852b28 ["CALLIND", null, ["register:0:8"]]
+ 00885ac0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885ac0 ["INT_ADD", "register:40f0:8", ["const:885ac0:8", "const:4:8"]]
+ 00885ac0 ["CALLIND", null, ["register:0:8"]]
- 00852b28 bytes 00013fd6
+ 00885ac0 bytes 00013fd6
~~~


<a id="compare-a85efb85527c6d1aaf2bb2b363705f73"></a>

### [`00853164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853164.md) → [`008860fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008860fc.md) FUN_008860fc

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008531a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853164.md#insn-008531a0)
- 新版 `00886138`（命令位置の公開資料なし）

~~~diff
- 008531a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008531a0 ["INT_ADD", "register:40f0:8", ["const:8531a0:8", "const:4:8"]]
- 008531a0 ["CALLIND", null, ["register:0:8"]]
+ 00886138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886138 ["INT_ADD", "register:40f0:8", ["const:886138:8", "const:4:8"]]
+ 00886138 ["CALLIND", null, ["register:0:8"]]
- 008531a0 bytes 00013fd6
+ 00886138 bytes 00013fd6
~~~


<a id="compare-3587882d4a012ff1d8134796eb00d921"></a>

### [`008531c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008531c8.md) → [`00886160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md) FUN_00886160

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00853204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008531c8.md#insn-00853204) · [`00853214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008531c8.md#insn-00853214)
- 新版 `0088619c`（命令位置の公開資料なし） · `008861ac`（命令位置の公開資料なし）

~~~diff
- 00853204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00853204 ["INT_ADD", "register:40f0:8", ["const:853204:8", "const:4:8"]]
- 00853204 ["CALLIND", null, ["register:0:8"]]
+ 0088619c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088619c ["INT_ADD", "register:40f0:8", ["const:88619c:8", "const:4:8"]]
+ 0088619c ["CALLIND", null, ["register:0:8"]]
- 00853204 bytes 00013fd6
+ 0088619c bytes 00013fd6
- 00853214 ["INT_ADD", "register:40f0:8", ["const:853214:8", "const:4:8"]]
- 00853214 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008861ac ["INT_ADD", "register:40f0:8", ["const:8861ac:8", "const:4:8"]]
+ 008861ac ["CALL", null, ["callee:00c57ab0:8"]]
- 00853214 bytes 931f0e94
+ 008861ac bytes 41460f94
~~~


<a id="compare-b7c724c6066d5bd7eccd3c13faa657b4"></a>

### [`00853f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853f38.md) → [`00886ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886ed0.md) FUN_00886ed0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00853acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853acc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00886a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00853f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853f38.md#insn-00853f58)
- 新版 `00886ef0`（命令位置の公開資料なし）

~~~diff
- 00853f58 ["INT_ADD", "register:40f0:8", ["const:853f58:8", "const:4:8"]]
- 00853f58 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00886ef0 ["INT_ADD", "register:40f0:8", ["const:886ef0:8", "const:4:8"]]
+ 00886ef0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00853f58 bytes 421c0e94
+ 00886ef0 bytes f0420f94
~~~


<a id="compare-e8c4d31a66de6812385a8dda2307479b"></a>

### [`00855054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855054.md) → [`00887fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887fec.md) FUN_00887fec

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00855070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855054.md#insn-00855070) · [`00855090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855054.md#insn-00855090)
- 新版 `00888008`（命令位置の公開資料なし） · `00888028`（命令位置の公開資料なし）

~~~diff
- 00855070 ["INT_ADD", "register:40f0:8", ["const:855070:8", "const:4:8"]]
- 00855070 ["CALL", null, ["callee:00c538e0:8"]]
+ 00888008 ["INT_ADD", "register:40f0:8", ["const:888008:8", "const:4:8"]]
+ 00888008 ["CALL", null, ["callee:00c538e0:8"]]
- 00855070 bytes 88070e94
+ 00888008 bytes 362e0f94
- 00855090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00855090 ["INT_ADD", "register:40f0:8", ["const:855090:8", "const:4:8"]]
- 00855090 ["CALLIND", null, ["register:0:8"]]
+ 00888028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888028 ["INT_ADD", "register:40f0:8", ["const:888028:8", "const:4:8"]]
+ 00888028 ["CALLIND", null, ["register:0:8"]]
- 00855090 bytes 00013fd6
+ 00888028 bytes 00013fd6
~~~


<a id="compare-d954150f92e5edbd9b7bf1e7716cdbdb"></a>

### [`008550f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008550f4.md) → [`0088808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088808c.md) FUN_0088808c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00855110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008550f4.md#insn-00855110) · [`00855130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008550f4.md#insn-00855130)
- 新版 `008880a8`（命令位置の公開資料なし） · `008880c8`（命令位置の公開資料なし）

~~~diff
- 00855110 ["INT_ADD", "register:40f0:8", ["const:855110:8", "const:4:8"]]
- 00855110 ["CALL", null, ["callee:00c538e0:8"]]
+ 008880a8 ["INT_ADD", "register:40f0:8", ["const:8880a8:8", "const:4:8"]]
+ 008880a8 ["CALL", null, ["callee:00c538e0:8"]]
- 00855110 bytes 60070e94
+ 008880a8 bytes 0e2e0f94
- 00855130 ["COPY", "register:0:8", ["register:4040:8"]]
- 00855130 ["INT_ADD", "register:40f0:8", ["const:855130:8", "const:4:8"]]
- 00855130 ["CALLIND", null, ["register:0:8"]]
+ 008880c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008880c8 ["INT_ADD", "register:40f0:8", ["const:8880c8:8", "const:4:8"]]
+ 008880c8 ["CALLIND", null, ["register:0:8"]]
- 00855130 bytes 00013fd6
+ 008880c8 bytes 00013fd6
~~~


<a id="compare-69effcd32ab4cf313ef441e840dd821e"></a>

### [`008551e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008551e4.md) → [`0088817c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088817c.md) FUN_0088817c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00855200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008551e4.md#insn-00855200) · [`00855220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008551e4.md#insn-00855220)
- 新版 `00888198`（命令位置の公開資料なし） · `008881b8`（命令位置の公開資料なし）

~~~diff
- 00855200 ["INT_ADD", "register:40f0:8", ["const:855200:8", "const:4:8"]]
- 00855200 ["CALL", null, ["callee:00c538e0:8"]]
+ 00888198 ["INT_ADD", "register:40f0:8", ["const:888198:8", "const:4:8"]]
+ 00888198 ["CALL", null, ["callee:00c538e0:8"]]
- 00855200 bytes 24070e94
+ 00888198 bytes d22d0f94
- 00855220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00855220 ["INT_ADD", "register:40f0:8", ["const:855220:8", "const:4:8"]]
- 00855220 ["CALLIND", null, ["register:0:8"]]
+ 008881b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008881b8 ["INT_ADD", "register:40f0:8", ["const:8881b8:8", "const:4:8"]]
+ 008881b8 ["CALLIND", null, ["register:0:8"]]
- 00855220 bytes 00013fd6
+ 008881b8 bytes 00013fd6
~~~


<a id="compare-cce37ee5ca8dabce8aebe98cdec0d9fb"></a>

### [`0085c028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c028.md) → [`0088efc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088e/0088efc0.md) FUN_0088efc0

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085c06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c028.md#insn-0085c06c)
- 新版 `0088f004`（命令位置の公開資料なし）

~~~diff
- 0085c06c ["INT_ADD", "register:40f0:8", ["const:85c06c:8", "const:4:8"]]
- 0085c06c ["CALL", null, ["callee:00c57c50:8"]]
+ 0088f004 ["INT_ADD", "register:40f0:8", ["const:88f004:8", "const:4:8"]]
+ 0088f004 ["CALL", null, ["callee:00c57c50:8"]]
- 0085c06c bytes 65fc0d94
+ 0088f004 bytes 13230f94
~~~


<a id="compare-95497cbc03da5cadc868aa12ac5ccfae"></a>

### [`0085c360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c360.md) → [`0088f2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f2f8.md) FUN_0088f2f8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 1件 [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md)
- 新版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 1件 [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085c384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c360.md#insn-0085c384)
- 新版 `0088f31c`（命令位置の公開資料なし）

~~~diff
- 0085c384 ["INT_ADD", "register:40f0:8", ["const:85c384:8", "const:4:8"]]
- 0085c384 ["CALL", null, ["callee:00c5a4f0:8"]]
+ 0088f31c ["INT_ADD", "register:40f0:8", ["const:88f31c:8", "const:4:8"]]
+ 0088f31c ["CALL", null, ["callee:00c5a4f0:8"]]
- 0085c384 bytes c7050e94
+ 0088f31c bytes 752c0f94
~~~


<a id="compare-2753f2a1038f31b54b293ad8e2947166"></a>

### [`0085cafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cafc.md) → [`0088fa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa94.md) FUN_0088fa94

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085cb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cafc.md#insn-0085cb18) · [`0085cb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cafc.md#insn-0085cb38)
- 新版 `0088fab0`（命令位置の公開資料なし） · `0088fad0`（命令位置の公開資料なし）

~~~diff
- 0085cb18 ["INT_ADD", "register:40f0:8", ["const:85cb18:8", "const:4:8"]]
- 0085cb18 ["CALL", null, ["callee:00c538e0:8"]]
+ 0088fab0 ["INT_ADD", "register:40f0:8", ["const:88fab0:8", "const:4:8"]]
+ 0088fab0 ["CALL", null, ["callee:00c538e0:8"]]
- 0085cb18 bytes dee80d94
+ 0088fab0 bytes 8c0f0f94
- 0085cb38 ["COPY", "register:0:8", ["register:4040:8"]]
- 0085cb38 ["INT_ADD", "register:40f0:8", ["const:85cb38:8", "const:4:8"]]
- 0085cb38 ["CALLIND", null, ["register:0:8"]]
+ 0088fad0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fad0 ["INT_ADD", "register:40f0:8", ["const:88fad0:8", "const:4:8"]]
+ 0088fad0 ["CALLIND", null, ["register:0:8"]]
- 0085cb38 bytes 00013fd6
+ 0088fad0 bytes 00013fd6
~~~


<a id="compare-73bcec1c3d069751e648cc67d18c4c9c"></a>

### [`0085cc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc88.md) → [`0088fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md) FUN_0088fc20

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085c704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0088f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085cca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc88.md#insn-0085cca4) · [`0085ccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc88.md#insn-0085ccc4)
- 新版 `0088fc3c`（命令位置の公開資料なし） · `0088fc5c`（命令位置の公開資料なし）

~~~diff
- 0085cca4 ["INT_ADD", "register:40f0:8", ["const:85cca4:8", "const:4:8"]]
- 0085cca4 ["CALL", null, ["callee:00c538e0:8"]]
+ 0088fc3c ["INT_ADD", "register:40f0:8", ["const:88fc3c:8", "const:4:8"]]
+ 0088fc3c ["CALL", null, ["callee:00c538e0:8"]]
- 0085cca4 bytes 7be80d94
+ 0088fc3c bytes 290f0f94
- 0085ccc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0085ccc4 ["INT_ADD", "register:40f0:8", ["const:85ccc4:8", "const:4:8"]]
- 0085ccc4 ["CALLIND", null, ["register:0:8"]]
+ 0088fc5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fc5c ["INT_ADD", "register:40f0:8", ["const:88fc5c:8", "const:4:8"]]
+ 0088fc5c ["CALLIND", null, ["register:0:8"]]
- 0085ccc4 bytes 00013fd6
+ 0088fc5c bytes 00013fd6
~~~


<a id="compare-1086f38f38b0d940cdc935f7c7d77b04"></a>

### [`0085dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dd3c.md) → [`00890cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890cd4.md) FUN_00890cd4

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dd3c.md#insn-0085dd8c) · [`0085dd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085dd3c.md#insn-0085dd9c)
- 新版 `00890d24`（命令位置の公開資料なし） · `00890d34`（命令位置の公開資料なし）

~~~diff
- 0085dd8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0085dd8c ["INT_ADD", "register:40f0:8", ["const:85dd8c:8", "const:4:8"]]
- 0085dd8c ["CALLIND", null, ["register:0:8"]]
+ 00890d24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890d24 ["INT_ADD", "register:40f0:8", ["const:890d24:8", "const:4:8"]]
+ 00890d24 ["CALLIND", null, ["register:0:8"]]
- 0085dd8c bytes 00013fd6
+ 00890d24 bytes 00013fd6
- 0085dd9c ["INT_ADD", "register:40f0:8", ["const:85dd9c:8", "const:4:8"]]
- 0085dd9c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00890d34 ["INT_ADD", "register:40f0:8", ["const:890d34:8", "const:4:8"]]
+ 00890d34 ["CALL", null, ["callee:00c57ab0:8"]]
- 0085dd9c bytes b1f40d94
+ 00890d34 bytes 5f1b0f94
~~~


<a id="compare-a9c1ebd81417d263f5eca5114877915d"></a>

### [`0085fe9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe9c.md) → [`00892e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e34.md) FUN_00892e34

採用 · 移動量 `+0x32f98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085febc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe9c.md#insn-0085febc)
- 新版 `00892e54`（命令位置の公開資料なし）

~~~diff
- 0085febc ["INT_ADD", "register:40f0:8", ["const:85febc:8", "const:4:8"]]
- 0085febc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00892e54 ["INT_ADD", "register:40f0:8", ["const:892e54:8", "const:4:8"]]
+ 00892e54 ["CALL", null, ["callee:00c57ab0:8"]]
- 0085febc bytes 69ec0d94
+ 00892e54 bytes 17130f94
~~~


<a id="compare-4428cde93fbe3e09265fc66ef8b97a3a"></a>

### [`00878678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878678.md) → [`008ab818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab818.md) FUN_008ab818

採用 · 移動量 `+0x331a0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00878690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878678.md#insn-00878690)
- 新版 `008ab830`（命令位置の公開資料なし）

~~~diff
- 00878690 ["INT_ADD", "register:40f0:8", ["const:878690:8", "const:4:8"]]
- 00878690 ["CALL", null, ["callee:005c175c:8"]]
+ 008ab830 ["INT_ADD", "register:40f0:8", ["const:8ab830:8", "const:4:8"]]
+ 008ab830 ["CALL", null, ["callee:005c175c:8"]]
- 00878690 bytes a792f497
+ 008ab830 bytes cb57f497
~~~


<a id="compare-3219f032000d92ef5e45462bd1c7d290"></a>

### [`0087d7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md) → [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) FUN_008b0994

採用 · 移動量 `+0x331a0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`0087d7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md) · 呼出先 3件 [`0087d7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md) [`0087d844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d844.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) · 呼出先 3件 [`008b0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0994.md) [`008b09e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b09e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087d814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md#insn-0087d814) · [`0087d820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md#insn-0087d820) · [`0087d82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d7f4.md#insn-0087d82c)
- 新版 `008b09b4`（命令位置の公開資料なし） · `008b09c0`（命令位置の公開資料なし） · `008b09cc`（命令位置の公開資料なし）

~~~diff
- 0087d814 ["INT_ADD", "register:40f0:8", ["const:87d814:8", "const:4:8"]]
- 0087d814 ["CALL", null, ["local:b0:8"]]
+ 008b09b4 ["INT_ADD", "register:40f0:8", ["const:8b09b4:8", "const:4:8"]]
+ 008b09b4 ["CALL", null, ["local:b0:8"]]
- 0087d814 bytes f8ffff97
+ 008b09b4 bytes f8ffff97
- 0087d820 ["INT_ADD", "register:40f0:8", ["const:87d820:8", "const:4:8"]]
- 0087d820 ["CALL", null, ["local:b0:8"]]
+ 008b09c0 ["INT_ADD", "register:40f0:8", ["const:8b09c0:8", "const:4:8"]]
+ 008b09c0 ["CALL", null, ["local:b0:8"]]
- 0087d820 bytes f5ffff97
+ 008b09c0 bytes f5ffff97
- 0087d82c ["INT_ADD", "register:40f0:8", ["const:87d82c:8", "const:4:8"]]
- 0087d82c ["CALL", null, ["callee:008b09e4:8"]]
+ 008b09cc ["INT_ADD", "register:40f0:8", ["const:8b09cc:8", "const:4:8"]]
+ 008b09cc ["CALL", null, ["callee:008b09e4:8"]]
- 0087d82c bytes 06000094
+ 008b09cc bytes 06000094
~~~


<a id="compare-9c4c1b73534def7ba01ab55cb252fb60"></a>

### [`00886348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886348.md) → [`008b9588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md) FUN_008b9588

採用 · 移動量 `+0x33240` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 18件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005ef020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005ef020.md) [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md) [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) · 呼出先 2件 [`00888f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888f6c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 22件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) · 呼出先 2件 [`008bc1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc1fc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886348.md#insn-00886388) · [`008863b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886348.md#insn-008863b4) · [`008863c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886348.md#insn-008863c4)
- 新版 `008b95c8`（命令位置の公開資料なし） · `008b95f4`（命令位置の公開資料なし） · `008b9604`（命令位置の公開資料なし）

~~~diff
- 00886388 ["COPY", "register:0:8", ["register:4048:8"]]
- 00886388 ["INT_ADD", "register:40f0:8", ["const:886388:8", "const:4:8"]]
- 00886388 ["CALLIND", null, ["register:0:8"]]
+ 008b95c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b95c8 ["INT_ADD", "register:40f0:8", ["const:8b95c8:8", "const:4:8"]]
+ 008b95c8 ["CALLIND", null, ["register:0:8"]]
- 00886388 bytes 20013fd6
+ 008b95c8 bytes 20013fd6
- 008863b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008863b4 ["INT_ADD", "register:40f0:8", ["const:8863b4:8", "const:4:8"]]
- 008863b4 ["CALLIND", null, ["register:0:8"]]
+ 008b95f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b95f4 ["INT_ADD", "register:40f0:8", ["const:8b95f4:8", "const:4:8"]]
+ 008b95f4 ["CALLIND", null, ["register:0:8"]]
- 008863b4 bytes 00013fd6
+ 008b95f4 bytes 00013fd6
- 008863c4 ["INT_ADD", "register:40f0:8", ["const:8863c4:8", "const:4:8"]]
- 008863c4 ["CALL", null, ["callee:008bc1fc:8"]]
+ 008b9604 ["INT_ADD", "register:40f0:8", ["const:8b9604:8", "const:4:8"]]
+ 008b9604 ["CALL", null, ["callee:008bc1fc:8"]]
- 008863c4 bytes ea0a0094
+ 008b9604 bytes fe0a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdb2a19bce5c0527b956ced97c72767c"></a>

### [`00886420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886420.md) → [`008b9660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md) FUN_008b9660

採用 · 移動量 `+0x33240` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 33件 [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) [`0060ef2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060ef2c.md) [`00649c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649c54.md) [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md) · 呼出先 2件 [`008890d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008890d4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 38件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`00634a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md) [`0066ff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) · 呼出先 2件 [`008bc364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc364.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00886460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886420.md#insn-00886460) · [`0088648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886420.md#insn-0088648c) · [`0088649c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886420.md#insn-0088649c)
- 新版 `008b96a0`（命令位置の公開資料なし） · `008b96cc`（命令位置の公開資料なし） · `008b96dc`（命令位置の公開資料なし）

~~~diff
- 00886460 ["COPY", "register:0:8", ["register:4048:8"]]
- 00886460 ["INT_ADD", "register:40f0:8", ["const:886460:8", "const:4:8"]]
- 00886460 ["CALLIND", null, ["register:0:8"]]
+ 008b96a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008b96a0 ["INT_ADD", "register:40f0:8", ["const:8b96a0:8", "const:4:8"]]
+ 008b96a0 ["CALLIND", null, ["register:0:8"]]
- 00886460 bytes 20013fd6
+ 008b96a0 bytes 20013fd6
- 0088648c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088648c ["INT_ADD", "register:40f0:8", ["const:88648c:8", "const:4:8"]]
- 0088648c ["CALLIND", null, ["register:0:8"]]
+ 008b96cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b96cc ["INT_ADD", "register:40f0:8", ["const:8b96cc:8", "const:4:8"]]
+ 008b96cc ["CALLIND", null, ["register:0:8"]]
- 0088648c bytes 00013fd6
+ 008b96cc bytes 00013fd6
- 0088649c ["INT_ADD", "register:40f0:8", ["const:88649c:8", "const:4:8"]]
- 0088649c ["CALL", null, ["callee:008bc364:8"]]
+ 008b96dc ["INT_ADD", "register:40f0:8", ["const:8b96dc:8", "const:4:8"]]
+ 008b96dc ["CALL", null, ["callee:008bc364:8"]]
- 0088649c bytes 0e0b0094
+ 008b96dc bytes 220b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ade829acceb62f2ceccd9eea0dace65d"></a>

### [`008879b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879b8.md) → [`008bac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac48.md) FUN_008bac48

採用 · 移動量 `+0x33290` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00887594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887594.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`00887e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887e18.md) · 呼出先 2件 [`00837b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837b84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md) [`008bb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb0a8.md) · 呼出先 2件 [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008879d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879b8.md#insn-008879d4)
- 新版 `008bac64`（命令位置の公開資料なし）

~~~diff
- 008879d4 ["INT_ADD", "register:40f0:8", ["const:8879d4:8", "const:4:8"]]
- 008879d4 ["CALL", null, ["callee:00869afc:8"]]
+ 008bac64 ["INT_ADD", "register:40f0:8", ["const:8bac64:8", "const:4:8"]]
+ 008bac64 ["CALL", null, ["callee:00869afc:8"]]
- 008879d4 bytes 6cc0fe97
+ 008bac64 bytes a6bbfe97
~~~


<a id="compare-b78fa8b675b53e1d879e43f1f63127ef"></a>

### [`0088878c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088878c.md) → [`008bba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bba1c.md) FUN_008bba1c

採用 · 移動量 `+0x33290` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00879b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md) · 呼出先 2件 [`00837b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837b84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008acd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acd10.md) · 呼出先 2件 [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008887d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088878c.md#insn-008887d0) · [`008887d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/0088878c.md#insn-008887d8)
- 新版 `008bba60`（命令位置の公開資料なし） · `008bba68`（命令位置の公開資料なし）

~~~diff
- 008887d0 ["INT_ADD", "register:40f0:8", ["const:8887d0:8", "const:4:8"]]
- 008887d0 ["CALL", null, ["callee:00869afc:8"]]
+ 008bba60 ["INT_ADD", "register:40f0:8", ["const:8bba60:8", "const:4:8"]]
+ 008bba60 ["CALL", null, ["callee:00869afc:8"]]
- 008887d0 bytes edbcfe97
+ 008bba60 bytes 27b8fe97
- 008887d8 ["INT_ADD", "register:40f0:8", ["const:8887d8:8", "const:4:8"]]
- 008887d8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008bba68 ["INT_ADD", "register:40f0:8", ["const:8bba68:8", "const:4:8"]]
+ 008bba68 ["CALL", null, ["callee:00c57ab0:8"]]
- 008887d8 bytes 224a0d94
+ 008bba68 bytes 12700e94
~~~


<a id="compare-e39cde0ed9b0da67a454c47f87b437ad"></a>

### [`00888998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888998.md) → [`008bbc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bbc28.md) FUN_008bbc28

採用 · 移動量 `+0x33290` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00885170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885170.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008b8310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b8310.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888998.md#insn-00888a04) · [`00888a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888998.md#insn-00888a14) · [`00888a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888998.md#insn-00888a34)
- 新版 `008bbc94`（命令位置の公開資料なし） · `008bbca4`（命令位置の公開資料なし） · `008bbcc4`（命令位置の公開資料なし）

~~~diff
- 00888a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888a04 ["INT_ADD", "register:40f0:8", ["const:888a04:8", "const:4:8"]]
- 00888a04 ["CALLIND", null, ["register:0:8"]]
+ 008bbc94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bbc94 ["INT_ADD", "register:40f0:8", ["const:8bbc94:8", "const:4:8"]]
+ 008bbc94 ["CALLIND", null, ["register:0:8"]]
- 00888a04 bytes 00013fd6
+ 008bbc94 bytes 00013fd6
- 00888a14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888a14 ["INT_ADD", "register:40f0:8", ["const:888a14:8", "const:4:8"]]
- 00888a14 ["CALLIND", null, ["register:0:8"]]
+ 008bbca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bbca4 ["INT_ADD", "register:40f0:8", ["const:8bbca4:8", "const:4:8"]]
+ 008bbca4 ["CALLIND", null, ["register:0:8"]]
- 00888a14 bytes 00013fd6
+ 008bbca4 bytes 00013fd6
- 00888a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888a34 ["INT_ADD", "register:40f0:8", ["const:888a34:8", "const:4:8"]]
- 00888a34 ["CALLIND", null, ["register:0:8"]]
+ 008bbcc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bbcc4 ["INT_ADD", "register:40f0:8", ["const:8bbcc4:8", "const:4:8"]]
+ 008bbcc4 ["CALLIND", null, ["register:0:8"]]
- 00888a34 bytes 00013fd6
+ 008bbcc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa6106245583fb612635c33478db681"></a>

### [`00888d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888d30.md) → [`008bbfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bbfc0.md) FUN_008bbfc0

採用 · 移動量 `+0x33290` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00888b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888b00.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008bbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bbd90.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888d30.md#insn-00888dbc) · [`00888e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888d30.md#insn-00888e04) · [`00888e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888d30.md#insn-00888e18)
- 新版 `008bc04c`（命令位置の公開資料なし） · `008bc094`（命令位置の公開資料なし） · `008bc0a8`（命令位置の公開資料なし）

~~~diff
- 00888dbc ["INT_ADD", "register:40f0:8", ["const:888dbc:8", "const:4:8"]]
- 00888dbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 008bc04c ["INT_ADD", "register:40f0:8", ["const:8bc04c:8", "const:4:8"]]
+ 008bc04c ["CALL", null, ["callee:00c57ab0:8"]]
- 00888dbc bytes a9480d94
+ 008bc04c bytes 996e0e94
- 00888e04 ["INT_ADD", "register:40f0:8", ["const:888e04:8", "const:4:8"]]
- 00888e04 ["CALL", null, ["callee:00c538e0:8"]]
+ 008bc094 ["INT_ADD", "register:40f0:8", ["const:8bc094:8", "const:4:8"]]
+ 008bc094 ["CALL", null, ["callee:00c538e0:8"]]
- 00888e04 bytes 23380d94
+ 008bc094 bytes 135e0e94
- 00888e18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888e18 ["INT_ADD", "register:40f0:8", ["const:888e18:8", "const:4:8"]]
- 00888e18 ["CALLIND", null, ["register:0:8"]]
+ 008bc0a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bc0a8 ["INT_ADD", "register:40f0:8", ["const:8bc0a8:8", "const:4:8"]]
+ 008bc0a8 ["CALLIND", null, ["register:0:8"]]
- 00888e18 bytes 00013fd6
+ 008bc0a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6930b358bb75e55ba8946dec326b2003"></a>

### [`00888e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888e78.md) → [`008bc108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc108.md) FUN_008bc108

採用 · 移動量 `+0x33290` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00888eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888e78.md#insn-00888eec) · [`00888f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888e78.md#insn-00888f00) · [`00888f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888e78.md#insn-00888f08)
- 新版 `008bc17c`（命令位置の公開資料なし） · `008bc190`（命令位置の公開資料なし） · `008bc198`（命令位置の公開資料なし）

~~~diff
- 00888eec ["INT_ADD", "register:40f0:8", ["const:888eec:8", "const:4:8"]]
- 00888eec ["CALL", null, ["callee:00c538e0:8"]]
+ 008bc17c ["INT_ADD", "register:40f0:8", ["const:8bc17c:8", "const:4:8"]]
+ 008bc17c ["CALL", null, ["callee:00c538e0:8"]]
- 00888eec bytes e9370d94
+ 008bc17c bytes d95d0e94
- 00888f00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888f00 ["INT_ADD", "register:40f0:8", ["const:888f00:8", "const:4:8"]]
- 00888f00 ["CALLIND", null, ["register:0:8"]]
+ 008bc190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bc190 ["INT_ADD", "register:40f0:8", ["const:8bc190:8", "const:4:8"]]
+ 008bc190 ["CALLIND", null, ["register:0:8"]]
- 00888f00 bytes 00013fd6
+ 008bc190 bytes 00013fd6
- 00888f08 ["INT_ADD", "register:40f0:8", ["const:888f08:8", "const:4:8"]]
- 00888f08 ["CALL", null, ["callee:00c57a80:8"]]
+ 008bc198 ["INT_ADD", "register:40f0:8", ["const:8bc198:8", "const:4:8"]]
+ 008bc198 ["CALL", null, ["callee:00c57a80:8"]]
- 00888f08 bytes 4a480d94
+ 008bc198 bytes 3a6e0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49ae85e70d4f89c59b4040846b11173a"></a>

### [`008890d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008890d4.md) → [`008bc364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc364.md) FUN_008bc364

採用 · 移動量 `+0x33290` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00886420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886420.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008b9660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00889140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008890d4.md#insn-00889140) · [`00889150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008890d4.md#insn-00889150) · [`00889170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008890d4.md#insn-00889170)
- 新版 `008bc3d0`（命令位置の公開資料なし） · `008bc3e0`（命令位置の公開資料なし） · `008bc400`（命令位置の公開資料なし）

~~~diff
- 00889140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889140 ["INT_ADD", "register:40f0:8", ["const:889140:8", "const:4:8"]]
- 00889140 ["CALLIND", null, ["register:0:8"]]
+ 008bc3d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bc3d0 ["INT_ADD", "register:40f0:8", ["const:8bc3d0:8", "const:4:8"]]
+ 008bc3d0 ["CALLIND", null, ["register:0:8"]]
- 00889140 bytes 00013fd6
+ 008bc3d0 bytes 00013fd6
- 00889150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889150 ["INT_ADD", "register:40f0:8", ["const:889150:8", "const:4:8"]]
- 00889150 ["CALLIND", null, ["register:0:8"]]
+ 008bc3e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bc3e0 ["INT_ADD", "register:40f0:8", ["const:8bc3e0:8", "const:4:8"]]
+ 008bc3e0 ["CALLIND", null, ["register:0:8"]]
- 00889150 bytes 00013fd6
+ 008bc3e0 bytes 00013fd6
- 00889170 ["COPY", "register:0:8", ["register:4040:8"]]
- 00889170 ["INT_ADD", "register:40f0:8", ["const:889170:8", "const:4:8"]]
- 00889170 ["CALLIND", null, ["register:0:8"]]
+ 008bc400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008bc400 ["INT_ADD", "register:40f0:8", ["const:8bc400:8", "const:4:8"]]
+ 008bc400 ["CALLIND", null, ["register:0:8"]]
- 00889170 bytes 00013fd6
+ 008bc400 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b57458dc59a582adbc3476b7507ad73b"></a>

### [`0089de40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089de40.md) → [`008d1cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1cd8.md) FUN_008d1cd8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 3件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`009d8aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d8/009d8aa4.md) [`009dbaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbaf8.md)
- 新版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 3件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a389f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389f4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0089de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089de40.md#insn-0089de50) · [`0089de58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089de40.md#insn-0089de58) · [`0089de64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089de40.md#insn-0089de64)
- 新版 `008d1ce8`（命令位置の公開資料なし） · `008d1cf0`（命令位置の公開資料なし） · `008d1cfc`（命令位置の公開資料なし）

~~~diff
- 0089de50 ["INT_ADD", "register:40f0:8", ["const:89de50:8", "const:4:8"]]
- 0089de50 ["CALL", null, ["callee:00a359a0:8"]]
+ 008d1ce8 ["INT_ADD", "register:40f0:8", ["const:8d1ce8:8", "const:4:8"]]
+ 008d1ce8 ["CALL", null, ["callee:00a359a0:8"]]
- 0089de50 bytes 15eb0494
+ 008d1ce8 bytes 2e8f0594
- 0089de58 ["INT_ADD", "register:40f0:8", ["const:89de58:8", "const:4:8"]]
- 0089de58 ["CALL", null, ["callee:0048ce44:8"]]
+ 008d1cf0 ["INT_ADD", "register:40f0:8", ["const:8d1cf0:8", "const:4:8"]]
+ 008d1cf0 ["CALL", null, ["callee:0048ce44:8"]]
- 0089de58 bytes 5530ef97
+ 008d1cf0 bytes 55ecee97
- 0089de64 ["INT_ADD", "register:40f0:8", ["const:89de64:8", "const:4:8"]]
- 0089de64 ["CALL", null, ["callee:00a389f4:8"]]
+ 008d1cfc ["INT_ADD", "register:40f0:8", ["const:8d1cfc:8", "const:4:8"]]
+ 008d1cfc ["CALL", null, ["callee:00a389f4:8"]]
- 0089de64 bytes 25f70494
+ 008d1cfc bytes 3e9b0594
~~~


<a id="compare-8826847c0e2ed633b9e4c21e37b3b8a9"></a>

### [`008a2c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2c5c.md) → [`008d6af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6af4.md) FUN_008d6af4

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a2c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2c5c.md#insn-008a2c78) · [`008a2c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2c5c.md#insn-008a2c98)
- 新版 `008d6b10`（命令位置の公開資料なし） · `008d6b30`（命令位置の公開資料なし）

~~~diff
- 008a2c78 ["INT_ADD", "register:40f0:8", ["const:8a2c78:8", "const:4:8"]]
- 008a2c78 ["CALL", null, ["callee:00c538e0:8"]]
+ 008d6b10 ["INT_ADD", "register:40f0:8", ["const:8d6b10:8", "const:4:8"]]
+ 008d6b10 ["CALL", null, ["callee:00c538e0:8"]]
- 008a2c78 bytes 86d00c94
+ 008d6b10 bytes 74f30d94
- 008a2c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a2c98 ["INT_ADD", "register:40f0:8", ["const:8a2c98:8", "const:4:8"]]
- 008a2c98 ["CALLIND", null, ["register:0:8"]]
+ 008d6b30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d6b30 ["INT_ADD", "register:40f0:8", ["const:8d6b30:8", "const:4:8"]]
+ 008d6b30 ["CALLIND", null, ["register:0:8"]]
- 008a2c98 bytes 00013fd6
+ 008d6b30 bytes 00013fd6
~~~


<a id="compare-68516156672695c7fe76cd37d51441e7"></a>

### [`008a59d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a59d8.md) → [`008d9870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9870.md) FUN_008d9870

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089eb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089e/0089eb04.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a59f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a59d8.md#insn-008a59f8)
- 新版 `008d9890`（命令位置の公開資料なし）

~~~diff
- 008a59f8 ["INT_ADD", "register:40f0:8", ["const:8a59f8:8", "const:4:8"]]
- 008a59f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008d9890 ["INT_ADD", "register:40f0:8", ["const:8d9890:8", "const:4:8"]]
+ 008d9890 ["CALL", null, ["callee:00c57ab0:8"]]
- 008a59f8 bytes 9ad50c94
+ 008d9890 bytes 88f80d94
~~~


<a id="compare-d62a1daf4abb20a0755f5632e05afc3c"></a>

### [`008a6720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6720.md) → [`008da5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da5b8.md) FUN_008da5b8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6720.md#insn-008a675c)
- 新版 `008da5f4`（命令位置の公開資料なし）

~~~diff
- 008a675c ["COPY", "register:0:8", ["register:4040:8"]]
- 008a675c ["INT_ADD", "register:40f0:8", ["const:8a675c:8", "const:4:8"]]
- 008a675c ["CALLIND", null, ["register:0:8"]]
+ 008da5f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da5f4 ["INT_ADD", "register:40f0:8", ["const:8da5f4:8", "const:4:8"]]
+ 008da5f4 ["CALLIND", null, ["register:0:8"]]
- 008a675c bytes 00013fd6
+ 008da5f4 bytes 00013fd6
~~~


<a id="compare-ddfada2d30f4d634143e1faedaea75c7"></a>

### [`008a6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e24.md) → [`008dacbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dacbc.md) FUN_008dacbc

採用 · 移動量 `+0x33e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e24.md#insn-008a6e60)
- 新版 `008dacf8`（命令位置の公開資料なし）

~~~diff
- 008a6e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a6e60 ["INT_ADD", "register:40f0:8", ["const:8a6e60:8", "const:4:8"]]
- 008a6e60 ["CALLIND", null, ["register:0:8"]]
+ 008dacf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dacf8 ["INT_ADD", "register:40f0:8", ["const:8dacf8:8", "const:4:8"]]
+ 008dacf8 ["CALLIND", null, ["register:0:8"]]
- 008a6e60 bytes 00013fd6
+ 008dacf8 bytes 00013fd6
~~~


<a id="compare-0936ff0003b49999ba2d46a77da39cea"></a>

### [`008ac5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md) → [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) FUN_008e0458

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00837ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md) [`008ac754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac754.md) [`008ac9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac9ec.md) [`008aca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008aca00.md)
- 新版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00869f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md) [`008e05f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e05f8.md) [`008e0890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0890.md) [`008e08a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e08a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ac638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md#insn-008ac638) · [`008ac65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md#insn-008ac65c) · [`008ac68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md#insn-008ac68c)
- 新版 `008e04dc`（命令位置の公開資料なし） · `008e0500`（命令位置の公開資料なし） · `008e0530`（命令位置の公開資料なし）

~~~diff
- 008ac638 ["INT_ADD", "register:40f0:8", ["const:8ac638:8", "const:4:8"]]
- 008ac638 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e04dc ["INT_ADD", "register:40f0:8", ["const:8e04dc:8", "const:4:8"]]
+ 008e04dc ["CALL", null, ["callee:00c57a90:8"]]
- 008ac638 bytes 82ba0c94
+ 008e04dc bytes 6ddd0d94
- 008ac65c ["INT_ADD", "register:40f0:8", ["const:8ac65c:8", "const:4:8"]]
- 008ac65c ["CALL", null, ["callee:008e05f8:8"]]
+ 008e0500 ["INT_ADD", "register:40f0:8", ["const:8e0500:8", "const:4:8"]]
+ 008e0500 ["CALL", null, ["callee:008e05f8:8"]]
- 008ac65c bytes 3e000094
+ 008e0500 bytes 3e000094
- 008ac68c ["INT_ADD", "register:40f0:8", ["const:8ac68c:8", "const:4:8"]]
- 008ac68c ["CALL", null, ["callee:008e08a4:8"]]
+ 008e0530 ["INT_ADD", "register:40f0:8", ["const:8e0530:8", "const:4:8"]]
+ 008e0530 ["CALL", null, ["callee:008e08a4:8"]]
- 008ac68c bytes dd000094
+ 008e0530 bytes dd000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c81c4d87e009b6dd4c2e8c6c265d488b"></a>

### [`008ac998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac998.md) → [`008e083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e083c.md) FUN_008e083c

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837ff8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ac9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac998.md#insn-008ac9bc)
- 新版 `008e0860`（命令位置の公開資料なし）

~~~diff
- 008ac9bc ["INT_ADD", "register:40f0:8", ["const:8ac9bc:8", "const:4:8"]]
- 008ac9bc ["CALL", null, ["callee:00869f70:8"]]
+ 008e0860 ["INT_ADD", "register:40f0:8", ["const:8e0860:8", "const:4:8"]]
+ 008e0860 ["CALL", null, ["callee:00869f70:8"]]
- 008ac9bc bytes 8f2dfe97
+ 008e0860 bytes c425fe97
~~~


<a id="compare-af5412d6a467f6f0fbd562244da4339e"></a>

### [`008adfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008adfe8.md) → [`008e1e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1e8c.md) FUN_008e1e8c

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ae12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008adfe8.md#insn-008ae12c) · [`008ae160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008adfe8.md#insn-008ae160) · [`008ae1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008adfe8.md#insn-008ae1b0)
- 新版 `008e1fd0`（命令位置の公開資料なし） · `008e2004`（命令位置の公開資料なし） · `008e2054`（命令位置の公開資料なし）

~~~diff
- 008ae12c ["INT_ADD", "register:40f0:8", ["const:8ae12c:8", "const:4:8"]]
- 008ae12c ["CALL", null, ["callee:00c57a90:8"]]
+ 008e1fd0 ["INT_ADD", "register:40f0:8", ["const:8e1fd0:8", "const:4:8"]]
+ 008e1fd0 ["CALL", null, ["callee:00c57a90:8"]]
- 008ae12c bytes c5b30c94
+ 008e1fd0 bytes b0d60d94
- 008ae160 ["INT_ADD", "register:40f0:8", ["const:8ae160:8", "const:4:8"]]
- 008ae160 ["CALL", null, ["callee:0043bb64:8"]]
+ 008e2004 ["INT_ADD", "register:40f0:8", ["const:8e2004:8", "const:4:8"]]
+ 008e2004 ["CALL", null, ["callee:0043bb64:8"]]
- 008ae160 bytes c1abed97
+ 008e2004 bytes d866ed97
- 008ae1b0 ["INT_ADD", "register:40f0:8", ["const:8ae1b0:8", "const:4:8"]]
- 008ae1b0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e2054 ["INT_ADD", "register:40f0:8", ["const:8e2054:8", "const:4:8"]]
+ 008e2054 ["CALL", null, ["callee:00c57a90:8"]]
- 008ae1b0 bytes a4b30c94
+ 008e2054 bytes 8fd60d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc400e0d1a1e4544766ec93671c9c31"></a>

### [`008ae7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae7ac.md) → [`008e2650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2650.md) FUN_008e2650

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) · 呼出先 3件 [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) · 呼出先 3件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ae7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae7ac.md#insn-008ae7d0) · [`008ae80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae7ac.md#insn-008ae80c) · [`008ae828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae7ac.md#insn-008ae828)
- 新版 `008e2674`（命令位置の公開資料なし） · `008e26b0`（命令位置の公開資料なし） · `008e26cc`（命令位置の公開資料なし）

~~~diff
- 008ae7d0 ["INT_ADD", "register:40f0:8", ["const:8ae7d0:8", "const:4:8"]]
- 008ae7d0 ["CALL", null, ["callee:0046d770:8"]]
+ 008e2674 ["INT_ADD", "register:40f0:8", ["const:8e2674:8", "const:4:8"]]
+ 008e2674 ["CALL", null, ["callee:0046d770:8"]]
- 008ae7d0 bytes 4270ee97
+ 008e2674 bytes 3f2cee97
- 008ae80c ["INT_ADD", "register:40f0:8", ["const:8ae80c:8", "const:4:8"]]
- 008ae80c ["CALL", null, ["callee:00c57a90:8"]]
+ 008e26b0 ["INT_ADD", "register:40f0:8", ["const:8e26b0:8", "const:4:8"]]
+ 008e26b0 ["CALL", null, ["callee:00c57a90:8"]]
- 008ae80c bytes 0db20c94
+ 008e26b0 bytes f8d40d94
- 008ae828 ["INT_ADD", "register:40f0:8", ["const:8ae828:8", "const:4:8"]]
- 008ae828 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e26cc ["INT_ADD", "register:40f0:8", ["const:8e26cc:8", "const:4:8"]]
+ 008e26cc ["CALL", null, ["callee:00c57a90:8"]]
- 008ae828 bytes 06b20c94
+ 008e26cc bytes f1d40d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf67688d2d43910b1385e42509ae1331"></a>

### [`008af0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md) → [`008e2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2f58.md) FUN_008e2f58

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`008b4224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`008e80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008af0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md#insn-008af0f4) · [`008af104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md#insn-008af104) · [`008af12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md#insn-008af12c)
- 新版 `008e2f98`（命令位置の公開資料なし） · `008e2fa8`（命令位置の公開資料なし） · `008e2fd0`（命令位置の公開資料なし）

~~~diff
- 008af0f4 ["INT_ADD", "register:40f0:8", ["const:8af0f4:8", "const:4:8"]]
- 008af0f4 ["CALL", null, ["callee:004878fc:8"]]
+ 008e2f98 ["INT_ADD", "register:40f0:8", ["const:8e2f98:8", "const:4:8"]]
+ 008e2f98 ["CALL", null, ["callee:004878fc:8"]]
- 008af0f4 bytes 5cd6ee97
+ 008e2f98 bytes 5992ee97
- 008af104 ["INT_ADD", "register:40f0:8", ["const:8af104:8", "const:4:8"]]
- 008af104 ["CALL", null, ["callee:004878fc:8"]]
+ 008e2fa8 ["INT_ADD", "register:40f0:8", ["const:8e2fa8:8", "const:4:8"]]
+ 008e2fa8 ["CALL", null, ["callee:004878fc:8"]]
- 008af104 bytes 58d6ee97
+ 008e2fa8 bytes 5592ee97
- 008af12c ["COPY", "register:0:8", ["register:4040:8"]]
- 008af12c ["INT_ADD", "register:40f0:8", ["const:8af12c:8", "const:4:8"]]
- 008af12c ["CALLIND", null, ["register:0:8"]]
+ 008e2fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008e2fd0 ["INT_ADD", "register:40f0:8", ["const:8e2fd0:8", "const:4:8"]]
+ 008e2fd0 ["CALLIND", null, ["register:0:8"]]
- 008af12c bytes 00013fd6
+ 008e2fd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d6f6a9c19c195e166a5ee3e3bf56739"></a>

### [`008af2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af2d4.md) → [`008e3178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3178.md) FUN_008e3178

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 1件 [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008af2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af2d4.md#insn-008af2f8) · [`008af308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af2d4.md#insn-008af308) · [`008af318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af2d4.md#insn-008af318)
- 新版 `008e319c`（命令位置の公開資料なし） · `008e31ac`（命令位置の公開資料なし） · `008e31bc`（命令位置の公開資料なし）

~~~diff
- 008af2f8 ["INT_ADD", "register:40f0:8", ["const:8af2f8:8", "const:4:8"]]
- 008af2f8 ["CALL", null, ["callee:004878fc:8"]]
+ 008e319c ["INT_ADD", "register:40f0:8", ["const:8e319c:8", "const:4:8"]]
+ 008e319c ["CALL", null, ["callee:004878fc:8"]]
- 008af2f8 bytes dbd5ee97
+ 008e319c bytes d891ee97
- 008af308 ["INT_ADD", "register:40f0:8", ["const:8af308:8", "const:4:8"]]
- 008af308 ["CALL", null, ["callee:004878fc:8"]]
+ 008e31ac ["INT_ADD", "register:40f0:8", ["const:8e31ac:8", "const:4:8"]]
+ 008e31ac ["CALL", null, ["callee:004878fc:8"]]
- 008af308 bytes d7d5ee97
+ 008e31ac bytes d491ee97
- 008af318 ["INT_ADD", "register:40f0:8", ["const:8af318:8", "const:4:8"]]
- 008af318 ["CALL", null, ["callee:004878fc:8"]]
+ 008e31bc ["INT_ADD", "register:40f0:8", ["const:8e31bc:8", "const:4:8"]]
+ 008e31bc ["CALL", null, ["callee:004878fc:8"]]
- 008af318 bytes d3d5ee97
+ 008e31bc bytes d091ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edca81d3b71c0ade17b3ddb5524bf329"></a>

### [`008b03dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b03dc.md) → [`008e4280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4280.md) FUN_008e4280

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 2件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b0440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b03dc.md#insn-008b0440) · [`008b0448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b03dc.md#insn-008b0448) · [`008b0454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b03dc.md#insn-008b0454)
- 新版 `008e42e4`（命令位置の公開資料なし） · `008e42ec`（命令位置の公開資料なし） · `008e42f8`（命令位置の公開資料なし）

~~~diff
- 008b0440 ["INT_ADD", "register:40f0:8", ["const:8b0440:8", "const:4:8"]]
- 008b0440 ["CALL", null, ["callee:0046eeb8:8"]]
+ 008e42e4 ["INT_ADD", "register:40f0:8", ["const:8e42e4:8", "const:4:8"]]
+ 008e42e4 ["CALL", null, ["callee:0046eeb8:8"]]
- 008b0440 bytes f86eee97
+ 008e42e4 bytes f52aee97
- 008b0448 ["INT_ADD", "register:40f0:8", ["const:8b0448:8", "const:4:8"]]
- 008b0448 ["CALL", null, ["callee:0046e784:8"]]
+ 008e42ec ["INT_ADD", "register:40f0:8", ["const:8e42ec:8", "const:4:8"]]
+ 008e42ec ["CALL", null, ["callee:0046e784:8"]]
- 008b0448 bytes 296dee97
+ 008e42ec bytes 2629ee97
- 008b0454 ["INT_ADD", "register:40f0:8", ["const:8b0454:8", "const:4:8"]]
- 008b0454 ["CALL", null, ["callee:0046e784:8"]]
+ 008e42f8 ["INT_ADD", "register:40f0:8", ["const:8e42f8:8", "const:4:8"]]
+ 008e42f8 ["CALL", null, ["callee:0046e784:8"]]
- 008b0454 bytes 266dee97
+ 008e42f8 bytes 2329ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73983f693c4787ceefd1de495e58e1ef"></a>

### [`008b0520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0520.md) → [`008e43c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43c4.md) FUN_008e43c4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00836c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836c68.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00868be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b0538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0520.md#insn-008b0538)
- 新版 `008e43dc`（命令位置の公開資料なし）

~~~diff
- 008b0538 ["INT_ADD", "register:40f0:8", ["const:8b0538:8", "const:4:8"]]
- 008b0538 ["CALL", null, ["callee:00868be0:8"]]
+ 008e43dc ["INT_ADD", "register:40f0:8", ["const:8e43dc:8", "const:4:8"]]
+ 008e43dc ["CALL", null, ["callee:00868be0:8"]]
- 008b0538 bytes cc19fe97
+ 008e43dc bytes 0112fe97
~~~


<a id="compare-a44c0b3d728bb6a826f300a038d0cbbb"></a>

### [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) → [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) FUN_008e43f4

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008afd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008afd10.md) [`008b5580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5580.md) · 呼出先 12件 [`008b42b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b42b0.md) [`008b4328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md) [`008b4574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4574.md) [`008b45fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md) [`008b4610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md)
- 新版 呼出元 2件 [`008e3bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3bb4.md) [`008e9424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9424.md) · 呼出先 12件 [`008e8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8154.md) [`008e81cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e81cc.md) [`008e8418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8418.md) [`008e84a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md) [`008e84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b059c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md#insn-008b059c) · [`008b05f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md#insn-008b05f0) · [`008b0614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md#insn-008b0614)
- 新版 `008e4440`（命令位置の公開資料なし） · `008e4494`（命令位置の公開資料なし） · `008e44b8`（命令位置の公開資料なし）

~~~diff
- 008b059c ["INT_ADD", "register:40f0:8", ["const:8b059c:8", "const:4:8"]]
- 008b059c ["CALL", null, ["callee:008e81cc:8"]]
+ 008e4440 ["INT_ADD", "register:40f0:8", ["const:8e4440:8", "const:4:8"]]
+ 008e4440 ["CALL", null, ["callee:008e81cc:8"]]
- 008b059c bytes 630f0094
+ 008e4440 bytes 630f0094
- 008b05f0 ["INT_ADD", "register:40f0:8", ["const:8b05f0:8", "const:4:8"]]
- 008b05f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e4494 ["INT_ADD", "register:40f0:8", ["const:8e4494:8", "const:4:8"]]
+ 008e4494 ["CALL", null, ["callee:00c57a90:8"]]
- 008b05f0 bytes 94aa0c94
+ 008e4494 bytes 7fcd0d94
- 008b0614 ["INT_ADD", "register:40f0:8", ["const:8b0614:8", "const:4:8"]]
- 008b0614 ["CALL", null, ["callee:008e84b4:8"]]
+ 008e44b8 ["INT_ADD", "register:40f0:8", ["const:8e44b8:8", "const:4:8"]]
+ 008e44b8 ["CALL", null, ["callee:008e84b4:8"]]
- 008b0614 bytes ff0f0094
+ 008e44b8 bytes ff0f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5dc0fb6e561a179af474a747cfcaff0"></a>

### [`008b1074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1074.md) → [`008e4f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4f18.md) FUN_008e4f18

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b10f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1074.md#insn-008b10f4) · [`008b114c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1074.md#insn-008b114c) · [`008b11a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1074.md#insn-008b11a0)
- 新版 `008e4f98`（命令位置の公開資料なし） · `008e4ff0`（命令位置の公開資料なし） · `008e5044`（命令位置の公開資料なし）

~~~diff
- 008b10f4 ["INT_ADD", "register:40f0:8", ["const:8b10f4:8", "const:4:8"]]
- 008b10f4 ["CALL", null, ["callee:0043bae0:8"]]
+ 008e4f98 ["INT_ADD", "register:40f0:8", ["const:8e4f98:8", "const:4:8"]]
+ 008e4f98 ["CALL", null, ["callee:0043bae0:8"]]
- 008b10f4 bytes bb9fed97
+ 008e4f98 bytes d25aed97
- 008b114c ["INT_ADD", "register:40f0:8", ["const:8b114c:8", "const:4:8"]]
- 008b114c ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e4ff0 ["INT_ADD", "register:40f0:8", ["const:8e4ff0:8", "const:4:8"]]
+ 008e4ff0 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b114c bytes c5a70c94
+ 008e4ff0 bytes b0ca0d94
- 008b11a0 ["INT_ADD", "register:40f0:8", ["const:8b11a0:8", "const:4:8"]]
- 008b11a0 ["CALL", null, ["callee:00c57ae0:8"]]
+ 008e5044 ["INT_ADD", "register:40f0:8", ["const:8e5044:8", "const:4:8"]]
+ 008e5044 ["CALL", null, ["callee:00c57ae0:8"]]
- 008b11a0 bytes bca70c94
+ 008e5044 bytes a7ca0d94
~~~


<a id="compare-3e8ba2619f98f5b7a67e1c794cbb5d80"></a>

### [`008b1d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1d14.md) → [`008e5bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5bb8.md) FUN_008e5bb8

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b1d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1d14.md#insn-008b1d5c)
- 新版 `008e5c00`（命令位置の公開資料なし）

~~~diff
- 008b1d5c ["INT_ADD", "register:40f0:8", ["const:8b1d5c:8", "const:4:8"]]
- 008b1d5c ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e5c00 ["INT_ADD", "register:40f0:8", ["const:8e5c00:8", "const:4:8"]]
+ 008e5c00 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b1d5c bytes c1a40c94
+ 008e5c00 bytes acc70d94
~~~


<a id="compare-c202abf4a81a0b17229f9d6569469fe8"></a>

### [`008b1d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1d8c.md) → [`008e5c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5c30.md) FUN_008e5c30

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b1dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1d8c.md#insn-008b1dd4)
- 新版 `008e5c78`（命令位置の公開資料なし）

~~~diff
- 008b1dd4 ["INT_ADD", "register:40f0:8", ["const:8b1dd4:8", "const:4:8"]]
- 008b1dd4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e5c78 ["INT_ADD", "register:40f0:8", ["const:8e5c78:8", "const:4:8"]]
+ 008e5c78 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b1dd4 bytes a3a40c94
+ 008e5c78 bytes 8ec70d94
~~~


<a id="compare-d35cf941e5f2e9b8927bf83e27927efa"></a>

### [`008b1e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1e04.md) → [`008e5ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5ca8.md) FUN_008e5ca8

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b1eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1e04.md#insn-008b1eac) · [`008b1ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1e04.md#insn-008b1ed0) · [`008b1f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1e04.md#insn-008b1f38)
- 新版 `008e5d50`（命令位置の公開資料なし） · `008e5d74`（命令位置の公開資料なし） · `008e5ddc`（命令位置の公開資料なし）

~~~diff
- 008b1eac ["INT_ADD", "register:40f0:8", ["const:8b1eac:8", "const:4:8"]]
- 008b1eac ["CALL", null, ["callee:0043bae0:8"]]
+ 008e5d50 ["INT_ADD", "register:40f0:8", ["const:8e5d50:8", "const:4:8"]]
+ 008e5d50 ["CALL", null, ["callee:0043bae0:8"]]
- 008b1eac bytes 4d9ced97
+ 008e5d50 bytes 6457ed97
- 008b1ed0 ["INT_ADD", "register:40f0:8", ["const:8b1ed0:8", "const:4:8"]]
- 008b1ed0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e5d74 ["INT_ADD", "register:40f0:8", ["const:8e5d74:8", "const:4:8"]]
+ 008e5d74 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b1ed0 bytes 64a40c94
+ 008e5d74 bytes 4fc70d94
- 008b1f38 ["INT_ADD", "register:40f0:8", ["const:8b1f38:8", "const:4:8"]]
- 008b1f38 ["CALL", null, ["callee:00c57ae0:8"]]
+ 008e5ddc ["INT_ADD", "register:40f0:8", ["const:8e5ddc:8", "const:4:8"]]
+ 008e5ddc ["CALL", null, ["callee:00c57ae0:8"]]
- 008b1f38 bytes 56a40c94
+ 008e5ddc bytes 41c70d94
~~~


<a id="compare-bdab651ddba912b4b52d1c1d79277cad"></a>

### [`008b4238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4238.md) → [`008e80dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80dc.md) FUN_008e80dc

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4238.md#insn-008b4280)
- 新版 `008e8124`（命令位置の公開資料なし）

~~~diff
- 008b4280 ["INT_ADD", "register:40f0:8", ["const:8b4280:8", "const:4:8"]]
- 008b4280 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8124 ["INT_ADD", "register:40f0:8", ["const:8e8124:8", "const:4:8"]]
+ 008e8124 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4280 bytes 789b0c94
+ 008e8124 bytes 63be0d94
~~~


<a id="compare-cd63c284c29f645e540e273c228276b5"></a>

### [`008b42b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b42b0.md) → [`008e8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8154.md) FUN_008e8154

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b42f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b42b0.md#insn-008b42f8)
- 新版 `008e819c`（命令位置の公開資料なし）

~~~diff
- 008b42f8 ["INT_ADD", "register:40f0:8", ["const:8b42f8:8", "const:4:8"]]
- 008b42f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e819c ["INT_ADD", "register:40f0:8", ["const:8e819c:8", "const:4:8"]]
+ 008e819c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b42f8 bytes 5a9b0c94
+ 008e819c bytes 45be0d94
~~~


<a id="compare-21eba683caabb9ed5d10be1d3a8ce3e9"></a>

### [`008b4328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md) → [`008e81cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e81cc.md) FUN_008e81cc

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`008b4484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4484.md) [`008b450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008e8328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8328.md) [`008e83b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md#insn-008b4374) · [`008b43f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md#insn-008b43f4) · [`008b4444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md#insn-008b4444)
- 新版 `008e8218`（命令位置の公開資料なし） · `008e8298`（命令位置の公開資料なし） · `008e82e8`（命令位置の公開資料なし）

~~~diff
- 008b4374 ["INT_ADD", "register:40f0:8", ["const:8b4374:8", "const:4:8"]]
- 008b4374 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e8218 ["INT_ADD", "register:40f0:8", ["const:8e8218:8", "const:4:8"]]
+ 008e8218 ["CALL", null, ["callee:00c57a90:8"]]
- 008b4374 bytes 339b0c94
+ 008e8218 bytes 1ebe0d94
- 008b43f4 ["INT_ADD", "register:40f0:8", ["const:8b43f4:8", "const:4:8"]]
- 008b43f4 ["CALL", null, ["callee:0043bae0:8"]]
+ 008e8298 ["INT_ADD", "register:40f0:8", ["const:8e8298:8", "const:4:8"]]
+ 008e8298 ["CALL", null, ["callee:0043bae0:8"]]
- 008b43f4 bytes fb92ed97
+ 008e8298 bytes 124eed97
- 008b4444 ["INT_ADD", "register:40f0:8", ["const:8b4444:8", "const:4:8"]]
- 008b4444 ["CALL", null, ["callee:008e83b0:8"]]
+ 008e82e8 ["INT_ADD", "register:40f0:8", ["const:8e82e8:8", "const:4:8"]]
+ 008e82e8 ["CALL", null, ["callee:008e83b0:8"]]
- 008b4444 bytes 32000094
+ 008e82e8 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7586095d078682de6e5c30758b3f3931"></a>

### [`008b4484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4484.md) → [`008e8328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8328.md) FUN_008e8328

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b4328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e81cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e81cc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b44e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4484.md#insn-008b44e8)
- 新版 `008e838c`（命令位置の公開資料なし）

~~~diff
- 008b44e8 ["INT_ADD", "register:40f0:8", ["const:8b44e8:8", "const:4:8"]]
- 008b44e8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e838c ["INT_ADD", "register:40f0:8", ["const:8e838c:8", "const:4:8"]]
+ 008e838c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b44e8 bytes de9a0c94
+ 008e838c bytes c9bd0d94
~~~


<a id="compare-b5d7ea6f0fd892926a00cfdc2b4fbb61"></a>

### [`008b4520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4520.md) → [`008e83c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83c4.md) FUN_008e83c4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b4560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4520.md#insn-008b4560)
- 新版 `008e8404`（命令位置の公開資料なし）

~~~diff
- 008b4560 ["INT_ADD", "register:40f0:8", ["const:8b4560:8", "const:4:8"]]
- 008b4560 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e8404 ["INT_ADD", "register:40f0:8", ["const:8e8404:8", "const:4:8"]]
+ 008e8404 ["CALL", null, ["callee:00c57ab0:8"]]
- 008b4560 bytes c09a0c94
+ 008e8404 bytes abbd0d94
~~~


<a id="compare-0e0ccd2d962da44e3393dcedbe0c26d9"></a>

### [`008b4574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4574.md) → [`008e8418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8418.md) FUN_008e8418

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b45d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4574.md#insn-008b45d8)
- 新版 `008e847c`（命令位置の公開資料なし）

~~~diff
- 008b45d8 ["INT_ADD", "register:40f0:8", ["const:8b45d8:8", "const:4:8"]]
- 008b45d8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008e847c ["INT_ADD", "register:40f0:8", ["const:8e847c:8", "const:4:8"]]
+ 008e847c ["CALL", null, ["callee:00c57ab0:8"]]
- 008b45d8 bytes a29a0c94
+ 008e847c bytes 8dbd0d94
~~~


<a id="compare-33be1a798a17d97b357953f272c8eeff"></a>

### [`008b4610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md) → [`008e84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84b4.md) FUN_008e84b4

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 7件 [`008b4224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md) [`008b4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4778.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 7件 [`008e80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md) [`008e861c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e861c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b46cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md#insn-008b46cc) · [`008b46e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md#insn-008b46e4) · [`008b4738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md#insn-008b4738)
- 新版 `008e8570`（命令位置の公開資料なし） · `008e8588`（命令位置の公開資料なし） · `008e85dc`（命令位置の公開資料なし）

~~~diff
- 008b46cc ["INT_ADD", "register:40f0:8", ["const:8b46cc:8", "const:4:8"]]
- 008b46cc ["CALL", null, ["callee:00c57a90:8"]]
+ 008e8570 ["INT_ADD", "register:40f0:8", ["const:8e8570:8", "const:4:8"]]
+ 008e8570 ["CALL", null, ["callee:00c57a90:8"]]
- 008b46cc bytes 5d9a0c94
+ 008e8570 bytes 48bd0d94
- 008b46e4 ["INT_ADD", "register:40f0:8", ["const:8b46e4:8", "const:4:8"]]
- 008b46e4 ["CALL", null, ["callee:00c57c00:8"]]
+ 008e8588 ["INT_ADD", "register:40f0:8", ["const:8e8588:8", "const:4:8"]]
+ 008e8588 ["CALL", null, ["callee:00c57c00:8"]]
- 008b46e4 bytes b39a0c94
+ 008e8588 bytes 9ebd0d94
- 008b4738 ["INT_ADD", "register:40f0:8", ["const:8b4738:8", "const:4:8"]]
- 008b4738 ["CALL", null, ["callee:008e80c8:8"]]
+ 008e85dc ["INT_ADD", "register:40f0:8", ["const:8e85dc:8", "const:4:8"]]
+ 008e85dc ["CALL", null, ["callee:008e80c8:8"]]
- 008b4738 bytes bbfeff97
+ 008e85dc bytes bbfeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

