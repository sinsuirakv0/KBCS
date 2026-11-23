# v16.0.0 → v16.0.1 · 要調査の変更候補 (27)

[一覧の目次](README.md)

<a id="compare-1aa0996e46fda0d31f04548e2ff5bcc7"></a>

### [`008399cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008399cc.md) → [`00839a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839a0c.md) FUN_00839a0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008399cc.md#insn-00839a34) · [`00839a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/008399cc.md#insn-00839a68)
- 新版 `00839a74`（命令位置の公開資料なし） · `00839aa8`（命令位置の公開資料なし）

~~~diff
- 00839a34 ["INT_ADD", "register:40f0:8", ["const:839a34:8", "const:4:8"]]
- 00839a34 ["CALL", null, ["callee:00c57e90:8"]]
+ 00839a74 ["INT_ADD", "register:40f0:8", ["const:839a74:8", "const:4:8"]]
+ 00839a74 ["CALL", null, ["callee:00c57e90:8"]]
- 00839a34 bytes 17781094
+ 00839a74 bytes 07791094
- 00839a68 ["INT_ADD", "register:40f0:8", ["const:839a68:8", "const:4:8"]]
- 00839a68 ["CALL", null, ["callee:0043bba4:8"]]
+ 00839aa8 ["INT_ADD", "register:40f0:8", ["const:839aa8:8", "const:4:8"]]
+ 00839aa8 ["CALL", null, ["callee:0043bba4:8"]]
- 00839a68 bytes 3f08f097
+ 00839aa8 bytes 3f08f097
~~~


<a id="compare-1ed555d11b1867c3a897a411795bbb89"></a>

### [`00839ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839ad8.md) → [`00839b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839b18.md) FUN_00839b18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a898d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a89/00a898d8.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a3767c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a3767c.md) [`00a37ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37ce4.md) [`00a389c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389c4.md)
- 新版 呼出元 1件 [`00a89ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a89/00a89ad0.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md) [`00a37874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37874.md) [`00a37edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37edc.md) [`00a38bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839ad8.md#insn-00839af4) · [`00839af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839ad8.md#insn-00839af8) · [`00839b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839ad8.md#insn-00839b14)
- 新版 `00839b34`（命令位置の公開資料なし） · `00839b38`（命令位置の公開資料なし） · `00839b54`（命令位置の公開資料なし）

~~~diff
- 00839af4 ["INT_ADD", "register:40f0:8", ["const:839af4:8", "const:4:8"]]
- 00839af4 ["CALL", null, ["callee:00a35b98:8"]]
+ 00839b34 ["INT_ADD", "register:40f0:8", ["const:839b34:8", "const:4:8"]]
+ 00839b34 ["CALL", null, ["callee:00a35b98:8"]]
- 00839af4 bytes abef0794
+ 00839b34 bytes 19f00794
- 00839af8 ["INT_ADD", "register:40f0:8", ["const:839af8:8", "const:4:8"]]
- 00839af8 ["CALL", null, ["callee:00a38bbc:8"]]
+ 00839b38 ["INT_ADD", "register:40f0:8", ["const:839b38:8", "const:4:8"]]
+ 00839b38 ["CALL", null, ["callee:00a38bbc:8"]]
- 00839af8 bytes b3fb0794
+ 00839b38 bytes 21fc0794
- 00839b14 ["INT_ADD", "register:40f0:8", ["const:839b14:8", "const:4:8"]]
- 00839b14 ["CALL", null, ["callee:0043bba4:8"]]
+ 00839b54 ["INT_ADD", "register:40f0:8", ["const:839b54:8", "const:4:8"]]
+ 00839b54 ["CALL", null, ["callee:0043bba4:8"]]
- 00839b14 bytes 1408f097
+ 00839b54 bytes 1408f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f462e947aa98e03762521144d5c3ba3b"></a>

### [`00839cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839cb8.md) → [`00839cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839cf8.md) FUN_00839cf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839cb8.md#insn-00839ce8)
- 新版 `00839d28`（命令位置の公開資料なし）

~~~diff
- 00839ce8 ["INT_ADD", "register:40f0:8", ["const:839ce8:8", "const:4:8"]]
- 00839ce8 ["CALL", null, ["callee:008514f8:8"]]
+ 00839d28 ["INT_ADD", "register:40f0:8", ["const:839d28:8", "const:4:8"]]
+ 00839d28 ["CALL", null, ["callee:008514f8:8"]]
- 00839ce8 bytes f45d0094
+ 00839d28 bytes f45d0094
~~~


<a id="compare-f8201f85c14e6d2a104f8b9dc6b6f26f"></a>

### [`00846488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846488.md) → [`008464c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008464c8.md) FUN_008464c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008464a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846488.md#insn-008464a0)
- 新版 `008464e0`（命令位置の公開資料なし）

~~~diff
- 008464a0 ["INT_ADD", "register:40f0:8", ["const:8464a0:8", "const:4:8"]]
- 008464a0 ["CALL", null, ["callee:005c3e7c:8"]]
+ 008464e0 ["INT_ADD", "register:40f0:8", ["const:8464e0:8", "const:4:8"]]
+ 008464e0 ["CALL", null, ["callee:005c3e7c:8"]]
- 008464a0 bytes 67f6f597
+ 008464e0 bytes 67f6f597
~~~


<a id="compare-751124de031a75a8f8822716c2e45b9a"></a>

### [`008464c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/008464c8.md) → [`00846508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846508.md) FUN_00846508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 1件 [`00b3ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba40.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 1件 [`00b3be68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008464d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/008464c8.md#insn-008464d8) · [`008464e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/008464c8.md#insn-008464e0) · [`008464e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/008464c8.md#insn-008464e8)
- 新版 `00846518`（命令位置の公開資料なし） · `00846520`（命令位置の公開資料なし） · `00846528`（命令位置の公開資料なし）

~~~diff
- 008464d8 ["INT_ADD", "register:40f0:8", ["const:8464d8:8", "const:4:8"]]
- 008464d8 ["CALL", null, ["callee:00b3be68:8"]]
+ 00846518 ["INT_ADD", "register:40f0:8", ["const:846518:8", "const:4:8"]]
+ 00846518 ["CALL", null, ["callee:00b3be68:8"]]
- 008464d8 bytes 5ad50b94
+ 00846518 bytes 54d60b94
- 008464e0 ["INT_ADD", "register:40f0:8", ["const:8464e0:8", "const:4:8"]]
- 008464e0 ["CALL", null, ["callee:00b3be68:8"]]
+ 00846520 ["INT_ADD", "register:40f0:8", ["const:846520:8", "const:4:8"]]
+ 00846520 ["CALL", null, ["callee:00b3be68:8"]]
- 008464e0 bytes 58d50b94
+ 00846520 bytes 52d60b94
- 008464e8 ["INT_ADD", "register:40f0:8", ["const:8464e8:8", "const:4:8"]]
- 008464e8 ["CALL", null, ["callee:00b3be68:8"]]
+ 00846528 ["INT_ADD", "register:40f0:8", ["const:846528:8", "const:4:8"]]
+ 00846528 ["CALL", null, ["callee:00b3be68:8"]]
- 008464e8 bytes 56d50b94
+ 00846528 bytes 50d60b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d4ac8b9191f11ec440c4a9bee061bc"></a>

### [`0084662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084662c.md) → [`0084666c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/0084666c.md) FUN_0084666c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008466b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084662c.md#insn-008466b8) · [`008466c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084662c.md#insn-008466c0)
- 新版 `008466f8`（命令位置の公開資料なし） · `00846700`（命令位置の公開資料なし）

~~~diff
- 008466b8 ["INT_ADD", "register:40f0:8", ["const:8466b8:8", "const:4:8"]]
- 008466b8 ["CALL", null, ["callee:0046eef8:8"]]
+ 008466f8 ["INT_ADD", "register:40f0:8", ["const:8466f8:8", "const:4:8"]]
+ 008466f8 ["CALL", null, ["callee:0046eef8:8"]]
- 008466b8 bytes 00a2f097
+ 008466f8 bytes 00a2f097
- 008466c0 ["INT_ADD", "register:40f0:8", ["const:8466c0:8", "const:4:8"]]
- 008466c0 ["CALL", null, ["callee:0046e7c4:8"]]
+ 00846700 ["INT_ADD", "register:40f0:8", ["const:846700:8", "const:4:8"]]
+ 00846700 ["CALL", null, ["callee:0046e7c4:8"]]
- 008466c0 bytes 31a0f097
+ 00846700 bytes 31a0f097
~~~


<a id="compare-79c4fdbfc10bfa3ec7ca4b3dc30ace49"></a>

### [`00846744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846744.md) → [`00846784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846784.md) FUN_00846784

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 2件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084676c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846744.md#insn-0084676c) · [`00846774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846744.md#insn-00846774) · [`0084677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846744.md#insn-0084677c)
- 新版 `008467ac`（命令位置の公開資料なし） · `008467b4`（命令位置の公開資料なし） · `008467bc`（命令位置の公開資料なし）

~~~diff
- 0084676c ["INT_ADD", "register:40f0:8", ["const:84676c:8", "const:4:8"]]
- 0084676c ["CALL", null, ["callee:0046eef8:8"]]
+ 008467ac ["INT_ADD", "register:40f0:8", ["const:8467ac:8", "const:4:8"]]
+ 008467ac ["CALL", null, ["callee:0046eef8:8"]]
- 0084676c bytes d3a1f097
+ 008467ac bytes d3a1f097
- 00846774 ["INT_ADD", "register:40f0:8", ["const:846774:8", "const:4:8"]]
- 00846774 ["CALL", null, ["callee:0046eef8:8"]]
+ 008467b4 ["INT_ADD", "register:40f0:8", ["const:8467b4:8", "const:4:8"]]
+ 008467b4 ["CALL", null, ["callee:0046eef8:8"]]
- 00846774 bytes d1a1f097
+ 008467b4 bytes d1a1f097
- 0084677c ["INT_ADD", "register:40f0:8", ["const:84677c:8", "const:4:8"]]
- 0084677c ["CALL", null, ["callee:0046e7c4:8"]]
+ 008467bc ["INT_ADD", "register:40f0:8", ["const:8467bc:8", "const:4:8"]]
+ 008467bc ["CALL", null, ["callee:0046e7c4:8"]]
- 0084677c bytes 02a0f097
+ 008467bc bytes 02a0f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c3e07a3ade4dff92bd8c1d1bb40cce"></a>

### [`0084688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084688c.md) → [`008468cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008468cc.md) FUN_008468cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084725c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md) · 呼出先 5件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) · 呼出先 5件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008468c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084688c.md#insn-008468c8) · [`008468d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084688c.md#insn-008468d8) · [`008468ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084688c.md#insn-008468ec)
- 新版 `00846908`（命令位置の公開資料なし） · `00846918`（命令位置の公開資料なし） · `0084692c`（命令位置の公開資料なし）

~~~diff
- 008468c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008468c8 ["INT_ADD", "register:40f0:8", ["const:8468c8:8", "const:4:8"]]
- 008468c8 ["CALLIND", null, ["register:0:8"]]
+ 00846908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00846908 ["INT_ADD", "register:40f0:8", ["const:846908:8", "const:4:8"]]
+ 00846908 ["CALLIND", null, ["register:0:8"]]
- 008468c8 bytes 00013fd6
+ 00846908 bytes 00013fd6
- 008468d8 ["INT_ADD", "register:40f0:8", ["const:8468d8:8", "const:4:8"]]
- 008468d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00846918 ["INT_ADD", "register:40f0:8", ["const:846918:8", "const:4:8"]]
+ 00846918 ["CALL", null, ["callee:00c57eb0:8"]]
- 008468d8 bytes 76441094
+ 00846918 bytes 66451094
- 008468ec ["INT_ADD", "register:40f0:8", ["const:8468ec:8", "const:4:8"]]
- 008468ec ["CALL", null, ["callee:00c53d00:8"]]
+ 0084692c ["INT_ADD", "register:40f0:8", ["const:84692c:8", "const:4:8"]]
+ 0084692c ["CALL", null, ["callee:00c53d00:8"]]
- 008468ec bytes fd331094
+ 0084692c bytes f5341094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74857cf3c201ba33b76e24534b609b42"></a>

### [`00846c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md) → [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) FUN_00846c50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 5件 [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) [`008689b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/008689b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 5件 [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00846c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md#insn-00846c34) · [`00846c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md#insn-00846c3c) · [`00846c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846c10.md#insn-00846c50)
- 新版 `00846c74`（命令位置の公開資料なし） · `00846c7c`（命令位置の公開資料なし） · `00846c90`（命令位置の公開資料なし）

~~~diff
- 00846c34 ["INT_ADD", "register:40f0:8", ["const:846c34:8", "const:4:8"]]
- 00846c34 ["CALL", null, ["callee:006a2b78:8"]]
+ 00846c74 ["INT_ADD", "register:40f0:8", ["const:846c74:8", "const:4:8"]]
+ 00846c74 ["CALL", null, ["callee:006a2b78:8"]]
- 00846c34 bytes c16ff997
+ 00846c74 bytes c16ff997
- 00846c3c ["INT_ADD", "register:40f0:8", ["const:846c3c:8", "const:4:8"]]
- 00846c3c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00846c7c ["INT_ADD", "register:40f0:8", ["const:846c7c:8", "const:4:8"]]
+ 00846c7c ["CALL", null, ["callee:00c57eb0:8"]]
- 00846c3c bytes 9d431094
+ 00846c7c bytes 8d441094
- 00846c50 ["INT_ADD", "register:40f0:8", ["const:846c50:8", "const:4:8"]]
- 00846c50 ["CALL", null, ["callee:006a2b78:8"]]
+ 00846c90 ["INT_ADD", "register:40f0:8", ["const:846c90:8", "const:4:8"]]
+ 00846c90 ["CALL", null, ["callee:006a2b78:8"]]
- 00846c50 bytes ba6ff997
+ 00846c90 bytes ba6ff997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e6fb2bf7612681baba0a21a86df4fe3"></a>

### [`00846cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md) → [`00846d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846d10.md) FUN_00846d10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 7件 [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`005d8c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md) [`0084769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 7件 [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`005d8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8c64.md) [`008476dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008476dc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00846ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md#insn-00846ce8) · [`00846cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md#insn-00846cf4) · [`00846d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md#insn-00846d00)
- 新版 `00846d28`（命令位置の公開資料なし） · `00846d34`（命令位置の公開資料なし） · `00846d40`（命令位置の公開資料なし）

~~~diff
- 00846ce8 ["INT_ADD", "register:40f0:8", ["const:846ce8:8", "const:4:8"]]
- 00846ce8 ["CALL", null, ["callee:008476dc:8"]]
+ 00846d28 ["INT_ADD", "register:40f0:8", ["const:846d28:8", "const:4:8"]]
+ 00846d28 ["CALL", null, ["callee:008476dc:8"]]
- 00846ce8 bytes 6d020094
+ 00846d28 bytes 6d020094
- 00846cf4 ["INT_ADD", "register:40f0:8", ["const:846cf4:8", "const:4:8"]]
- 00846cf4 ["CALL", null, ["callee:005b9ee4:8"]]
+ 00846d34 ["INT_ADD", "register:40f0:8", ["const:846d34:8", "const:4:8"]]
+ 00846d34 ["CALL", null, ["callee:005b9ee4:8"]]
- 00846cf4 bytes 6cccf597
+ 00846d34 bytes 6cccf597
- 00846d00 ["INT_ADD", "register:40f0:8", ["const:846d00:8", "const:4:8"]]
- 00846d00 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00846d40 ["INT_ADD", "register:40f0:8", ["const:846d40:8", "const:4:8"]]
+ 00846d40 ["CALL", null, ["callee:005c3e7c:8"]]
- 00846d00 bytes 4ff4f597
+ 00846d40 bytes 4ff4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f97ba54f6022992f75a9763cdfbb8f"></a>

### [`00846e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846e24.md) → [`00846e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846e64.md) FUN_00846e64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 5件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 5件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00846e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846e24.md#insn-00846e38) · [`00846e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846e24.md#insn-00846e40) · [`00846e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846e24.md#insn-00846e48)
- 新版 `00846e78`（命令位置の公開資料なし） · `00846e80`（命令位置の公開資料なし） · `00846e88`（命令位置の公開資料なし）

~~~diff
- 00846e38 ["INT_ADD", "register:40f0:8", ["const:846e38:8", "const:4:8"]]
- 00846e38 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00846e78 ["INT_ADD", "register:40f0:8", ["const:846e78:8", "const:4:8"]]
+ 00846e78 ["CALL", null, ["callee:0046e8a4:8"]]
- 00846e38 bytes 8b9ef097
+ 00846e78 bytes 8b9ef097
- 00846e40 ["INT_ADD", "register:40f0:8", ["const:846e40:8", "const:4:8"]]
- 00846e40 ["CALL", null, ["callee:0046efdc:8"]]
+ 00846e80 ["INT_ADD", "register:40f0:8", ["const:846e80:8", "const:4:8"]]
+ 00846e80 ["CALL", null, ["callee:0046efdc:8"]]
- 00846e40 bytes 57a0f097
+ 00846e80 bytes 57a0f097
- 00846e48 ["INT_ADD", "register:40f0:8", ["const:846e48:8", "const:4:8"]]
- 00846e48 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00846e88 ["INT_ADD", "register:40f0:8", ["const:846e88:8", "const:4:8"]]
+ 00846e88 ["CALL", null, ["callee:0046e8a4:8"]]
- 00846e48 bytes 879ef097
+ 00846e88 bytes 879ef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec727078939cd7364d6f572a35a92ecb"></a>

### [`00846f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846f64.md) → [`00846fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846fa4.md) FUN_00846fa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00846f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846f64.md#insn-00846f84) · [`00846f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846f64.md#insn-00846f98) · [`00846fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846f64.md#insn-00846fa0)
- 新版 `00846fc4`（命令位置の公開資料なし） · `00846fd8`（命令位置の公開資料なし） · `00846fe0`（命令位置の公開資料なし）

~~~diff
- 00846f84 ["INT_ADD", "register:40f0:8", ["const:846f84:8", "const:4:8"]]
- 00846f84 ["CALL", null, ["callee:00c53d00:8"]]
+ 00846fc4 ["INT_ADD", "register:40f0:8", ["const:846fc4:8", "const:4:8"]]
+ 00846fc4 ["CALL", null, ["callee:00c53d00:8"]]
- 00846f84 bytes 57321094
+ 00846fc4 bytes 4f331094
- 00846f98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00846f98 ["INT_ADD", "register:40f0:8", ["const:846f98:8", "const:4:8"]]
- 00846f98 ["CALLIND", null, ["register:0:8"]]
+ 00846fd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00846fd8 ["INT_ADD", "register:40f0:8", ["const:846fd8:8", "const:4:8"]]
+ 00846fd8 ["CALLIND", null, ["register:0:8"]]
- 00846f98 bytes 00013fd6
+ 00846fd8 bytes 00013fd6
- 00846fa0 ["INT_ADD", "register:40f0:8", ["const:846fa0:8", "const:4:8"]]
- 00846fa0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00846fe0 ["INT_ADD", "register:40f0:8", ["const:846fe0:8", "const:4:8"]]
+ 00846fe0 ["CALL", null, ["callee:00c57e80:8"]]
- 00846fa0 bytes b8421094
+ 00846fe0 bytes a8431094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-909737e3fd021dae67bb2f4691b5aa0b"></a>

### [`008470bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008470bc.md) → [`008470fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008470fc.md) FUN_008470fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008470f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008470bc.md#insn-008470f8)
- 新版 `00847138`（命令位置の公開資料なし）

~~~diff
- 008470f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008470f8 ["INT_ADD", "register:40f0:8", ["const:8470f8:8", "const:4:8"]]
- 008470f8 ["CALLIND", null, ["register:0:8"]]
+ 00847138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847138 ["INT_ADD", "register:40f0:8", ["const:847138:8", "const:4:8"]]
+ 00847138 ["CALLIND", null, ["register:0:8"]]
- 008470f8 bytes 00013fd6
+ 00847138 bytes 00013fd6
~~~


<a id="compare-f1e7774714bc6cc6119c71ce48e2ec3b"></a>

### [`00847218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847218.md) → [`00847258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847258.md) FUN_00847258

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847218.md#insn-00847234)
- 新版 `00847274`（命令位置の公開資料なし）

~~~diff
- 00847234 ["INT_ADD", "register:40f0:8", ["const:847234:8", "const:4:8"]]
- 00847234 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847274 ["INT_ADD", "register:40f0:8", ["const:847274:8", "const:4:8"]]
+ 00847274 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847234 bytes 1f421094
+ 00847274 bytes 0f431094
~~~


<a id="compare-83b9731295de67198d08c062426f79f1"></a>

### [`0084725c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md) → [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) FUN_0084729c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 6件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`0084688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/0084688c.md) [`00868c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868c24.md) [`00868d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868d0c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 6件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`008468cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008468cc.md) [`00868c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md) [`00868d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md#insn-00847270) · [`00847284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md#insn-00847284) · [`00847298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084725c.md#insn-00847298)
- 新版 `008472b0`（命令位置の公開資料なし） · `008472c4`（命令位置の公開資料なし） · `008472d8`（命令位置の公開資料なし）

~~~diff
- 00847270 ["INT_ADD", "register:40f0:8", ["const:847270:8", "const:4:8"]]
- 00847270 ["CALL", null, ["callee:008468cc:8"]]
+ 008472b0 ["INT_ADD", "register:40f0:8", ["const:8472b0:8", "const:4:8"]]
+ 008472b0 ["CALL", null, ["callee:008468cc:8"]]
- 00847270 bytes 87fdff97
+ 008472b0 bytes 87fdff97
- 00847284 ["INT_ADD", "register:40f0:8", ["const:847284:8", "const:4:8"]]
- 00847284 ["CALL", null, ["callee:00c53d00:8"]]
+ 008472c4 ["INT_ADD", "register:40f0:8", ["const:8472c4:8", "const:4:8"]]
+ 008472c4 ["CALL", null, ["callee:00c53d00:8"]]
- 00847284 bytes 97311094
+ 008472c4 bytes 8f321094
- 00847298 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847298 ["INT_ADD", "register:40f0:8", ["const:847298:8", "const:4:8"]]
- 00847298 ["CALLIND", null, ["register:0:8"]]
+ 008472d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008472d8 ["INT_ADD", "register:40f0:8", ["const:8472d8:8", "const:4:8"]]
+ 008472d8 ["CALLIND", null, ["register:0:8"]]
- 00847298 bytes 00013fd6
+ 008472d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d765b697ccb6c84a886ec23ff52672f1"></a>

### [`00847354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847354.md) → [`00847394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847394.md) FUN_00847394

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847354.md#insn-00847370) · [`00847390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847354.md#insn-00847390)
- 新版 `008473b0`（命令位置の公開資料なし） · `008473d0`（命令位置の公開資料なし）

~~~diff
- 00847370 ["INT_ADD", "register:40f0:8", ["const:847370:8", "const:4:8"]]
- 00847370 ["CALL", null, ["callee:00c53d00:8"]]
+ 008473b0 ["INT_ADD", "register:40f0:8", ["const:8473b0:8", "const:4:8"]]
+ 008473b0 ["CALL", null, ["callee:00c53d00:8"]]
- 00847370 bytes 5c311094
+ 008473b0 bytes 54321094
- 00847390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847390 ["INT_ADD", "register:40f0:8", ["const:847390:8", "const:4:8"]]
- 00847390 ["CALLIND", null, ["register:0:8"]]
+ 008473d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008473d0 ["INT_ADD", "register:40f0:8", ["const:8473d0:8", "const:4:8"]]
+ 008473d0 ["CALLIND", null, ["register:0:8"]]
- 00847390 bytes 00013fd6
+ 008473d0 bytes 00013fd6
~~~


<a id="compare-80bbf16decdedd18a371d945e8331be5"></a>

### [`008473a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md) → [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) FUN_008473e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 4件 [`00869148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869148.md) [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) [`008692cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008692cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 4件 [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) [`0086930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008473c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md#insn-008473c4) · [`008473ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md#insn-008473ec) · [`00847400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008473a4.md#insn-00847400)
- 新版 `00847404`（命令位置の公開資料なし） · `0084742c`（命令位置の公開資料なし） · `00847440`（命令位置の公開資料なし）

~~~diff
- 008473c4 ["INT_ADD", "register:40f0:8", ["const:8473c4:8", "const:4:8"]]
- 008473c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847404 ["INT_ADD", "register:40f0:8", ["const:847404:8", "const:4:8"]]
+ 00847404 ["CALL", null, ["callee:00c57eb0:8"]]
- 008473c4 bytes bb411094
+ 00847404 bytes ab421094
- 008473ec ["INT_ADD", "register:40f0:8", ["const:8473ec:8", "const:4:8"]]
- 008473ec ["CALL", null, ["callee:00869188:8"]]
+ 0084742c ["INT_ADD", "register:40f0:8", ["const:84742c:8", "const:4:8"]]
+ 0084742c ["CALL", null, ["callee:00869188:8"]]
- 008473ec bytes 57870094
+ 0084742c bytes 57870094
- 00847400 ["INT_ADD", "register:40f0:8", ["const:847400:8", "const:4:8"]]
- 00847400 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847440 ["INT_ADD", "register:40f0:8", ["const:847440:8", "const:4:8"]]
+ 00847440 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847400 bytes ac411094
+ 00847440 bytes 9c421094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1ada8ae611da3418aa46450bdeb3be"></a>

### [`00847470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md) → [`008474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474b0.md) FUN_008474b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869380.md) [`008693e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008693e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847470.md#insn-00847488)
- 新版 `008474c8`（命令位置の公開資料なし）

~~~diff
- 00847488 ["INT_ADD", "register:40f0:8", ["const:847488:8", "const:4:8"]]
- 00847488 ["CALL", null, ["callee:008693c0:8"]]
+ 008474c8 ["INT_ADD", "register:40f0:8", ["const:8474c8:8", "const:4:8"]]
+ 008474c8 ["CALL", null, ["callee:008693c0:8"]]
- 00847488 bytes be870094
+ 008474c8 bytes be870094
~~~


<a id="compare-bfb7fa296843592ac75c2acaaa26bf45"></a>

### [`008474a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008474a0.md) → [`008474e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474e0.md) FUN_008474e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005fe258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe298.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008474ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008474a0.md#insn-008474ec) · [`008474f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008474a0.md#insn-008474f4)
- 新版 `0084752c`（命令位置の公開資料なし） · `00847534`（命令位置の公開資料なし）

~~~diff
- 008474ec ["INT_ADD", "register:40f0:8", ["const:8474ec:8", "const:4:8"]]
- 008474ec ["CALL", null, ["callee:005fe298:8"]]
+ 0084752c ["INT_ADD", "register:40f0:8", ["const:84752c:8", "const:4:8"]]
+ 0084752c ["CALL", null, ["callee:005fe298:8"]]
- 008474ec bytes 5bdbf697
+ 0084752c bytes 5bdbf697
- 008474f4 ["INT_ADD", "register:40f0:8", ["const:8474f4:8", "const:4:8"]]
- 008474f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847534 ["INT_ADD", "register:40f0:8", ["const:847534:8", "const:4:8"]]
+ 00847534 ["CALL", null, ["callee:00c57eb0:8"]]
- 008474f4 bytes 6f411094
+ 00847534 bytes 5f421094
~~~


<a id="compare-c21f7ea4d0898257a9e1146436d7bd3c"></a>

### [`00847524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847524.md) → [`00847564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847564.md) FUN_00847564

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847524.md#insn-00847568)
- 新版 `008475a8`（命令位置の公開資料なし）

~~~diff
- 00847568 ["INT_ADD", "register:40f0:8", ["const:847568:8", "const:4:8"]]
- 00847568 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008475a8 ["INT_ADD", "register:40f0:8", ["const:8475a8:8", "const:4:8"]]
+ 008475a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847568 bytes 52411094
+ 008475a8 bytes 42421094
~~~


<a id="compare-30efe508c7b00367aa85ebc504a3ee0e"></a>

### [`00847598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847598.md) → [`008475d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008475d8.md) FUN_008475d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008475e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847598.md#insn-008475e4) · [`008475ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847598.md#insn-008475ec)
- 新版 `00847624`（命令位置の公開資料なし） · `0084762c`（命令位置の公開資料なし）

~~~diff
- 008475e4 ["INT_ADD", "register:40f0:8", ["const:8475e4:8", "const:4:8"]]
- 008475e4 ["CALL", null, ["callee:005c179c:8"]]
+ 00847624 ["INT_ADD", "register:40f0:8", ["const:847624:8", "const:4:8"]]
+ 00847624 ["CALL", null, ["callee:005c179c:8"]]
- 008475e4 bytes 5ee8f597
+ 00847624 bytes 5ee8f597
- 008475ec ["INT_ADD", "register:40f0:8", ["const:8475ec:8", "const:4:8"]]
- 008475ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0084762c ["INT_ADD", "register:40f0:8", ["const:84762c:8", "const:4:8"]]
+ 0084762c ["CALL", null, ["callee:00c57eb0:8"]]
- 008475ec bytes 31411094
+ 0084762c bytes 21421094
~~~


<a id="compare-54688fa99522c0e25da93948a82cd43f"></a>

### [`0084761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084761c.md) → [`0084765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084765c.md) FUN_0084765c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084761c.md#insn-00847638) · [`00847658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084761c.md#insn-00847658)
- 新版 `00847678`（命令位置の公開資料なし） · `00847698`（命令位置の公開資料なし）

~~~diff
- 00847638 ["INT_ADD", "register:40f0:8", ["const:847638:8", "const:4:8"]]
- 00847638 ["CALL", null, ["callee:00c53d00:8"]]
+ 00847678 ["INT_ADD", "register:40f0:8", ["const:847678:8", "const:4:8"]]
+ 00847678 ["CALL", null, ["callee:00c53d00:8"]]
- 00847638 bytes aa301094
+ 00847678 bytes a2311094
- 00847658 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847658 ["INT_ADD", "register:40f0:8", ["const:847658:8", "const:4:8"]]
- 00847658 ["CALLIND", null, ["register:0:8"]]
+ 00847698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847698 ["INT_ADD", "register:40f0:8", ["const:847698:8", "const:4:8"]]
+ 00847698 ["CALLIND", null, ["register:0:8"]]
- 00847658 bytes 00013fd6
+ 00847698 bytes 00013fd6
~~~


<a id="compare-0f17f2ffa60159063d89f14de7cdaddb"></a>

### [`0084766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084766c.md) → [`008476ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008476ac.md) FUN_008476ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00869474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869474.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084766c.md#insn-00847684)
- 新版 `008476c4`（命令位置の公開資料なし）

~~~diff
- 00847684 ["INT_ADD", "register:40f0:8", ["const:847684:8", "const:4:8"]]
- 00847684 ["CALL", null, ["callee:008694b4:8"]]
+ 008476c4 ["INT_ADD", "register:40f0:8", ["const:8476c4:8", "const:4:8"]]
+ 008476c4 ["CALL", null, ["callee:008694b4:8"]]
- 00847684 bytes 7c870094
+ 008476c4 bytes 7c870094
~~~


<a id="compare-7bddb4c5a1bdbdc7a709b399891baf9e"></a>

### [`0084769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md) → [`008476dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008476dc.md) FUN_008476dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00846cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00846d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846d10.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008476d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md#insn-008476d8) · [`00847708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md#insn-00847708) · [`00847738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084769c.md#insn-00847738)
- 新版 `00847718`（命令位置の公開資料なし） · `00847748`（命令位置の公開資料なし） · `00847778`（命令位置の公開資料なし）

~~~diff
- 008476d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008476d8 ["INT_ADD", "register:40f0:8", ["const:8476d8:8", "const:4:8"]]
- 008476d8 ["CALLIND", null, ["register:0:8"]]
+ 00847718 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847718 ["INT_ADD", "register:40f0:8", ["const:847718:8", "const:4:8"]]
+ 00847718 ["CALLIND", null, ["register:0:8"]]
- 008476d8 bytes 00013fd6
+ 00847718 bytes 00013fd6
- 00847708 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847708 ["INT_ADD", "register:40f0:8", ["const:847708:8", "const:4:8"]]
- 00847708 ["CALLIND", null, ["register:0:8"]]
+ 00847748 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847748 ["INT_ADD", "register:40f0:8", ["const:847748:8", "const:4:8"]]
+ 00847748 ["CALLIND", null, ["register:0:8"]]
- 00847708 bytes 00013fd6
+ 00847748 bytes 00013fd6
- 00847738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847738 ["INT_ADD", "register:40f0:8", ["const:847738:8", "const:4:8"]]
- 00847738 ["CALLIND", null, ["register:0:8"]]
+ 00847778 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847778 ["INT_ADD", "register:40f0:8", ["const:847778:8", "const:4:8"]]
+ 00847778 ["CALLIND", null, ["register:0:8"]]
- 00847738 bytes 00013fd6
+ 00847778 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9d8c32b13d0426a710e1fd748bed04"></a>

### [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) → [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) FUN_00847860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 11件 [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`008301e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008301e4.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 11件 [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00830224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830224.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md#insn-00847838) · [`00847844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md#insn-00847844) · [`00847850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md#insn-00847850)
- 新版 `00847878`（命令位置の公開資料なし） · `00847884`（命令位置の公開資料なし） · `00847890`（命令位置の公開資料なし）

~~~diff
- 00847838 ["INT_ADD", "register:40f0:8", ["const:847838:8", "const:4:8"]]
- 00847838 ["CALL", null, ["callee:00830554:8"]]
+ 00847878 ["INT_ADD", "register:40f0:8", ["const:847878:8", "const:4:8"]]
+ 00847878 ["CALL", null, ["callee:00830554:8"]]
- 00847838 bytes 37a3ff97
+ 00847878 bytes 37a3ff97
- 00847844 ["INT_ADD", "register:40f0:8", ["const:847844:8", "const:4:8"]]
- 00847844 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00847884 ["INT_ADD", "register:40f0:8", ["const:847884:8", "const:4:8"]]
+ 00847884 ["CALL", null, ["callee:005c3e7c:8"]]
- 00847844 bytes 7ef1f597
+ 00847884 bytes 7ef1f597
- 00847850 ["INT_ADD", "register:40f0:8", ["const:847850:8", "const:4:8"]]
- 00847850 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00847890 ["INT_ADD", "register:40f0:8", ["const:847890:8", "const:4:8"]]
+ 00847890 ["CALL", null, ["callee:005c3e7c:8"]]
- 00847850 bytes 7bf1f597
+ 00847890 bytes 7bf1f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-867073fd69157aef2f66992e0129090f"></a>

### [`00847928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847928.md) → [`00847968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847968.md) FUN_00847968

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847928.md#insn-00847974) · [`00847988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847928.md#insn-00847988) · [`00847990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847928.md#insn-00847990)
- 新版 `008479b4`（命令位置の公開資料なし） · `008479c8`（命令位置の公開資料なし） · `008479d0`（命令位置の公開資料なし）

~~~diff
- 00847974 ["INT_ADD", "register:40f0:8", ["const:847974:8", "const:4:8"]]
- 00847974 ["CALL", null, ["callee:00c53d00:8"]]
+ 008479b4 ["INT_ADD", "register:40f0:8", ["const:8479b4:8", "const:4:8"]]
+ 008479b4 ["CALL", null, ["callee:00c53d00:8"]]
- 00847974 bytes db2f1094
+ 008479b4 bytes d3301094
- 00847988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847988 ["INT_ADD", "register:40f0:8", ["const:847988:8", "const:4:8"]]
- 00847988 ["CALLIND", null, ["register:0:8"]]
+ 008479c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008479c8 ["INT_ADD", "register:40f0:8", ["const:8479c8:8", "const:4:8"]]
+ 008479c8 ["CALLIND", null, ["register:0:8"]]
- 00847988 bytes 00013fd6
+ 008479c8 bytes 00013fd6
- 00847990 ["INT_ADD", "register:40f0:8", ["const:847990:8", "const:4:8"]]
- 00847990 ["CALL", null, ["callee:00c57e80:8"]]
+ 008479d0 ["INT_ADD", "register:40f0:8", ["const:8479d0:8", "const:4:8"]]
+ 008479d0 ["CALL", null, ["callee:00c57e80:8"]]
- 00847990 bytes 3c401094
+ 008479d0 bytes 2c411094
~~~


<a id="compare-55caeb3f877239b799aff1e302ddd197"></a>

### [`008479c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479c0.md) → [`00847a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847a00.md) FUN_00847a00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008479dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479c0.md#insn-008479dc) · [`008479e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479c0.md#insn-008479e4)
- 新版 `00847a1c`（命令位置の公開資料なし） · `00847a24`（命令位置の公開資料なし）

~~~diff
- 008479dc ["INT_ADD", "register:40f0:8", ["const:8479dc:8", "const:4:8"]]
- 008479dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847a1c ["INT_ADD", "register:40f0:8", ["const:847a1c:8", "const:4:8"]]
+ 00847a1c ["CALL", null, ["callee:00c57eb0:8"]]
- 008479dc bytes 35401094
+ 00847a1c bytes 25411094
- 008479e4 ["INT_ADD", "register:40f0:8", ["const:8479e4:8", "const:4:8"]]
- 008479e4 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00847a24 ["INT_ADD", "register:40f0:8", ["const:847a24:8", "const:4:8"]]
+ 00847a24 ["CALL", null, ["callee:0046e8a4:8"]]
- 008479e4 bytes a09bf097
+ 00847a24 bytes a09bf097
~~~


<a id="compare-acebd189fe8d59fbf452a4cebd7c75ae"></a>

### [`008479f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479f8.md) → [`00847a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847a38.md) FUN_00847a38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479f8.md#insn-00847a38) · [`00847a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479f8.md#insn-00847a80)
- 新版 `00847a78`（命令位置の公開資料なし） · `00847ac0`（命令位置の公開資料なし）

~~~diff
- 00847a38 ["INT_ADD", "register:40f0:8", ["const:847a38:8", "const:4:8"]]
- 00847a38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847a78 ["INT_ADD", "register:40f0:8", ["const:847a78:8", "const:4:8"]]
+ 00847a78 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847a38 bytes 1e401094
+ 00847a78 bytes 0e411094
- 00847a80 ["INT_ADD", "register:40f0:8", ["const:847a80:8", "const:4:8"]]
- 00847a80 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847ac0 ["INT_ADD", "register:40f0:8", ["const:847ac0:8", "const:4:8"]]
+ 00847ac0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847a80 bytes 0c401094
+ 00847ac0 bytes fc401094
~~~


<a id="compare-2148cb9fd8ec18d1cfa2a8023ec14c36"></a>

### [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) → [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) FUN_00847af8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0062a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md) [`00865c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md) [`00869508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869508.md) [`00869744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869744.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0062a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a460.md) [`00865ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md) [`00869548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md) [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md#insn-00847ad0) · [`00847adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md#insn-00847adc) · [`00847ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md#insn-00847ae4)
- 新版 `00847b10`（命令位置の公開資料なし） · `00847b1c`（命令位置の公開資料なし） · `00847b24`（命令位置の公開資料なし）

~~~diff
- 00847ad0 ["INT_ADD", "register:40f0:8", ["const:847ad0:8", "const:4:8"]]
- 00847ad0 ["CALL", null, ["callee:0062a460:8"]]
+ 00847b10 ["INT_ADD", "register:40f0:8", ["const:847b10:8", "const:4:8"]]
+ 00847b10 ["CALL", null, ["callee:0062a460:8"]]
- 00847ad0 bytes 548af797
+ 00847b10 bytes 548af797
- 00847adc ["INT_ADD", "register:40f0:8", ["const:847adc:8", "const:4:8"]]
- 00847adc ["CALL", null, ["callee:00869784:8"]]
+ 00847b1c ["INT_ADD", "register:40f0:8", ["const:847b1c:8", "const:4:8"]]
+ 00847b1c ["CALL", null, ["callee:00869784:8"]]
- 00847adc bytes 1a870094
+ 00847b1c bytes 1a870094
- 00847ae4 ["INT_ADD", "register:40f0:8", ["const:847ae4:8", "const:4:8"]]
- 00847ae4 ["CALL", null, ["callee:00869548:8"]]
+ 00847b24 ["INT_ADD", "register:40f0:8", ["const:847b24:8", "const:4:8"]]
+ 00847b24 ["CALL", null, ["callee:00869548:8"]]
- 00847ae4 bytes 89860094
+ 00847b24 bytes 89860094
~~~


<a id="compare-6881cb0c5aa79c45a563ffbd1b7ecf2a"></a>

### [`00847af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847af8.md) → [`00847b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847b38.md) FUN_00847b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00869788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869788.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008697c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847af8.md#insn-00847b1c) · [`00847b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847af8.md#insn-00847b30) · [`00847b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847af8.md#insn-00847b44)
- 新版 `00847b5c`（命令位置の公開資料なし） · `00847b70`（命令位置の公開資料なし） · `00847b84`（命令位置の公開資料なし）

~~~diff
- 00847b1c ["INT_ADD", "register:40f0:8", ["const:847b1c:8", "const:4:8"]]
- 00847b1c ["CALL", null, ["callee:00c53d00:8"]]
+ 00847b5c ["INT_ADD", "register:40f0:8", ["const:847b5c:8", "const:4:8"]]
+ 00847b5c ["CALL", null, ["callee:00c53d00:8"]]
- 00847b1c bytes 712f1094
+ 00847b5c bytes 69301094
- 00847b30 ["INT_ADD", "register:40f0:8", ["const:847b30:8", "const:4:8"]]
- 00847b30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847b70 ["INT_ADD", "register:40f0:8", ["const:847b70:8", "const:4:8"]]
+ 00847b70 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847b30 bytes e03f1094
+ 00847b70 bytes d0401094
- 00847b44 ["INT_ADD", "register:40f0:8", ["const:847b44:8", "const:4:8"]]
- 00847b44 ["CALL", null, ["callee:00c53d00:8"]]
+ 00847b84 ["INT_ADD", "register:40f0:8", ["const:847b84:8", "const:4:8"]]
+ 00847b84 ["CALL", null, ["callee:00c53d00:8"]]
- 00847b44 bytes 672f1094
+ 00847b84 bytes 5f301094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b43cb2e82d652e310985021106a44f"></a>

### [`00847be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847be4.md) → [`00847c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847c24.md) FUN_00847c24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0078f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078f164.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0078f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f1a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847be4.md#insn-00847c00)
- 新版 `00847c40`（命令位置の公開資料なし）

~~~diff
- 00847c00 ["INT_ADD", "register:40f0:8", ["const:847c00:8", "const:4:8"]]
- 00847c00 ["CALL", null, ["callee:0078f1a4:8"]]
+ 00847c40 ["INT_ADD", "register:40f0:8", ["const:847c40:8", "const:4:8"]]
+ 00847c40 ["CALL", null, ["callee:0078f1a4:8"]]
- 00847c00 bytes 591dfd97
+ 00847c40 bytes 591dfd97
~~~


<a id="compare-9b78037b017af1915cdba1daea9ed057"></a>

### [`00847c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847c20.md) → [`00847c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847c60.md) FUN_00847c60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847c20.md#insn-00847c3c) · [`00847c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847c20.md#insn-00847c4c) · [`00847c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847c20.md#insn-00847c5c)
- 新版 `00847c7c`（命令位置の公開資料なし） · `00847c8c`（命令位置の公開資料なし） · `00847c9c`（命令位置の公開資料なし）

~~~diff
- 00847c3c ["INT_ADD", "register:40f0:8", ["const:847c3c:8", "const:4:8"]]
- 00847c3c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847c7c ["INT_ADD", "register:40f0:8", ["const:847c7c:8", "const:4:8"]]
+ 00847c7c ["CALL", null, ["callee:00c57eb0:8"]]
- 00847c3c bytes 9d3f1094
+ 00847c7c bytes 8d401094
- 00847c4c ["INT_ADD", "register:40f0:8", ["const:847c4c:8", "const:4:8"]]
- 00847c4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847c8c ["INT_ADD", "register:40f0:8", ["const:847c8c:8", "const:4:8"]]
+ 00847c8c ["CALL", null, ["callee:00c57eb0:8"]]
- 00847c4c bytes 993f1094
+ 00847c8c bytes 89401094
- 00847c5c ["INT_ADD", "register:40f0:8", ["const:847c5c:8", "const:4:8"]]
- 00847c5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847c9c ["INT_ADD", "register:40f0:8", ["const:847c9c:8", "const:4:8"]]
+ 00847c9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00847c5c bytes 953f1094
+ 00847c9c bytes 85401094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb9ada4be58f4ab470bfc9b97ac525b"></a>

### [`00847d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d1c.md) → [`00847d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847d5c.md) FUN_00847d5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d1c.md#insn-00847d68)
- 新版 `00847da8`（命令位置の公開資料なし）

~~~diff
- 00847d68 ["INT_ADD", "register:40f0:8", ["const:847d68:8", "const:4:8"]]
- 00847d68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847da8 ["INT_ADD", "register:40f0:8", ["const:847da8:8", "const:4:8"]]
+ 00847da8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847d68 bytes 523f1094
+ 00847da8 bytes 42401094
~~~


<a id="compare-f4d0d8eea8f557549580ff578fcacc7d"></a>

### [`00847d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d98.md) → [`00847dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847dd8.md) FUN_00847dd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d98.md#insn-00847dc4) · [`00847e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d98.md#insn-00847e08)
- 新版 `00847e04`（命令位置の公開資料なし） · `00847e48`（命令位置の公開資料なし）

~~~diff
- 00847dc4 ["INT_ADD", "register:40f0:8", ["const:847dc4:8", "const:4:8"]]
- 00847dc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847e04 ["INT_ADD", "register:40f0:8", ["const:847e04:8", "const:4:8"]]
+ 00847e04 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847dc4 bytes 3b3f1094
+ 00847e04 bytes 2b401094
- 00847e08 ["INT_ADD", "register:40f0:8", ["const:847e08:8", "const:4:8"]]
- 00847e08 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847e48 ["INT_ADD", "register:40f0:8", ["const:847e48:8", "const:4:8"]]
+ 00847e48 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847e08 bytes 2a3f1094
+ 00847e48 bytes 1a401094
~~~


<a id="compare-3b91fd89fa47c3512bd1221ed744067c"></a>

### [`00847e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e24.md) → [`00847e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847e64.md) FUN_00847e64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e24.md#insn-00847e68)
- 新版 `00847ea8`（命令位置の公開資料なし）

~~~diff
- 00847e68 ["INT_ADD", "register:40f0:8", ["const:847e68:8", "const:4:8"]]
- 00847e68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00847ea8 ["INT_ADD", "register:40f0:8", ["const:847ea8:8", "const:4:8"]]
+ 00847ea8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00847e68 bytes 123f1094
+ 00847ea8 bytes 02401094
~~~


<a id="compare-10a15f6c0d5546e51ba5d3a77ca4cbf1"></a>

### [`00847e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e98.md) → [`00847ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847ed8.md) FUN_00847ed8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e98.md#insn-00847eac) · [`00847eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847e98.md#insn-00847eb8)
- 新版 `00847eec`（命令位置の公開資料なし） · `00847ef8`（命令位置の公開資料なし）

~~~diff
- 00847eac ["INT_ADD", "register:40f0:8", ["const:847eac:8", "const:4:8"]]
- 00847eac ["CALL", null, ["callee:00672748:8"]]
+ 00847eec ["INT_ADD", "register:40f0:8", ["const:847eec:8", "const:4:8"]]
+ 00847eec ["CALL", null, ["callee:00672748:8"]]
- 00847eac bytes 17aaf897
+ 00847eec bytes 17aaf897
- 00847eb8 ["INT_ADD", "register:40f0:8", ["const:847eb8:8", "const:4:8"]]
- 00847eb8 ["CALL", null, ["callee:00676a60:8"]]
+ 00847ef8 ["INT_ADD", "register:40f0:8", ["const:847ef8:8", "const:4:8"]]
+ 00847ef8 ["CALL", null, ["callee:00676a60:8"]]
- 00847eb8 bytes dabaf897
+ 00847ef8 bytes dabaf897
~~~


<a id="compare-04a6c354ef0d5d2cdad48c39a724fb70"></a>

### [`00847ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ed0.md) → [`00847f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847f10.md) FUN_00847f10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ed0.md#insn-00847ee8)
- 新版 `00847f28`（命令位置の公開資料なし）

~~~diff
- 00847ee8 ["INT_ADD", "register:40f0:8", ["const:847ee8:8", "const:4:8"]]
- 00847ee8 ["CALL", null, ["callee:005c1bf0:8"]]
+ 00847f28 ["INT_ADD", "register:40f0:8", ["const:847f28:8", "const:4:8"]]
+ 00847f28 ["CALL", null, ["callee:005c1bf0:8"]]
- 00847ee8 bytes 32e7f597
+ 00847f28 bytes 32e7f597
~~~


<a id="compare-f5c86fea4982446f11a720b748554b07"></a>

### [`00847efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847efc.md) → [`00847f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847f3c.md) FUN_00847f3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847efc.md#insn-00847f34) · [`00847f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847efc.md#insn-00847f48) · [`00847f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847efc.md#insn-00847f50)
- 新版 `00847f74`（命令位置の公開資料なし） · `00847f88`（命令位置の公開資料なし） · `00847f90`（命令位置の公開資料なし）

~~~diff
- 00847f34 ["INT_ADD", "register:40f0:8", ["const:847f34:8", "const:4:8"]]
- 00847f34 ["CALL", null, ["callee:00c53d00:8"]]
+ 00847f74 ["INT_ADD", "register:40f0:8", ["const:847f74:8", "const:4:8"]]
+ 00847f74 ["CALL", null, ["callee:00c53d00:8"]]
- 00847f34 bytes 6b2e1094
+ 00847f74 bytes 632f1094
- 00847f48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847f48 ["INT_ADD", "register:40f0:8", ["const:847f48:8", "const:4:8"]]
- 00847f48 ["CALLIND", null, ["register:0:8"]]
+ 00847f88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847f88 ["INT_ADD", "register:40f0:8", ["const:847f88:8", "const:4:8"]]
+ 00847f88 ["CALLIND", null, ["register:0:8"]]
- 00847f48 bytes 00013fd6
+ 00847f88 bytes 00013fd6
- 00847f50 ["INT_ADD", "register:40f0:8", ["const:847f50:8", "const:4:8"]]
- 00847f50 ["CALL", null, ["callee:00c57e80:8"]]
+ 00847f90 ["INT_ADD", "register:40f0:8", ["const:847f90:8", "const:4:8"]]
+ 00847f90 ["CALL", null, ["callee:00c57e80:8"]]
- 00847f50 bytes cc3e1094
+ 00847f90 bytes bc3f1094
~~~


<a id="compare-2daf84f4bc5c8d1bfb4b6060754456a3"></a>

### [`00847f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md) → [`00847fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847fa8.md) FUN_00847fa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00847fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md#insn-00847fa0) · [`00847fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md#insn-00847fb4) · [`00847fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md#insn-00847fbc)
- 新版 `00847fe0`（命令位置の公開資料なし） · `00847ff4`（命令位置の公開資料なし） · `00847ffc`（命令位置の公開資料なし）

~~~diff
- 00847fa0 ["INT_ADD", "register:40f0:8", ["const:847fa0:8", "const:4:8"]]
- 00847fa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00847fe0 ["INT_ADD", "register:40f0:8", ["const:847fe0:8", "const:4:8"]]
+ 00847fe0 ["CALL", null, ["callee:00c53d00:8"]]
- 00847fa0 bytes 502e1094
+ 00847fe0 bytes 482f1094
- 00847fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00847fb4 ["INT_ADD", "register:40f0:8", ["const:847fb4:8", "const:4:8"]]
- 00847fb4 ["CALLIND", null, ["register:0:8"]]
+ 00847ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00847ff4 ["INT_ADD", "register:40f0:8", ["const:847ff4:8", "const:4:8"]]
+ 00847ff4 ["CALLIND", null, ["register:0:8"]]
- 00847fb4 bytes 00013fd6
+ 00847ff4 bytes 00013fd6
- 00847fbc ["INT_ADD", "register:40f0:8", ["const:847fbc:8", "const:4:8"]]
- 00847fbc ["CALL", null, ["callee:00c57e80:8"]]
+ 00847ffc ["INT_ADD", "register:40f0:8", ["const:847ffc:8", "const:4:8"]]
+ 00847ffc ["CALL", null, ["callee:00c57e80:8"]]
- 00847fbc bytes b13e1094
+ 00847ffc bytes a13f1094
~~~


<a id="compare-8baa8ab3c6cd719cbe80d0e611887a60"></a>

### [`00847fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md) → [`00848014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848014.md) FUN_00848014

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md#insn-0084800c) · [`00848020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md#insn-00848020) · [`00848028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md#insn-00848028)
- 新版 `0084804c`（命令位置の公開資料なし） · `00848060`（命令位置の公開資料なし） · `00848068`（命令位置の公開資料なし）

~~~diff
- 0084800c ["INT_ADD", "register:40f0:8", ["const:84800c:8", "const:4:8"]]
- 0084800c ["CALL", null, ["callee:00c53d00:8"]]
+ 0084804c ["INT_ADD", "register:40f0:8", ["const:84804c:8", "const:4:8"]]
+ 0084804c ["CALL", null, ["callee:00c53d00:8"]]
- 0084800c bytes 352e1094
+ 0084804c bytes 2d2f1094
- 00848020 ["COPY", "register:0:8", ["register:4040:8"]]
- 00848020 ["INT_ADD", "register:40f0:8", ["const:848020:8", "const:4:8"]]
- 00848020 ["CALLIND", null, ["register:0:8"]]
+ 00848060 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00848060 ["INT_ADD", "register:40f0:8", ["const:848060:8", "const:4:8"]]
+ 00848060 ["CALLIND", null, ["register:0:8"]]
- 00848020 bytes 00013fd6
+ 00848060 bytes 00013fd6
- 00848028 ["INT_ADD", "register:40f0:8", ["const:848028:8", "const:4:8"]]
- 00848028 ["CALL", null, ["callee:00c57e80:8"]]
+ 00848068 ["INT_ADD", "register:40f0:8", ["const:848068:8", "const:4:8"]]
+ 00848068 ["CALL", null, ["callee:00c57e80:8"]]
- 00848028 bytes 963e1094
+ 00848068 bytes 863f1094
~~~


<a id="compare-3a40baa4544fadca115060a9ec2173b8"></a>

### [`00848040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848040.md) → [`00848080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848080.md) FUN_00848080

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084805c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848040.md#insn-0084805c)
- 新版 `0084809c`（命令位置の公開資料なし）

~~~diff
- 0084805c ["INT_ADD", "register:40f0:8", ["const:84805c:8", "const:4:8"]]
- 0084805c ["CALL", null, ["callee:006a2b78:8"]]
+ 0084809c ["INT_ADD", "register:40f0:8", ["const:84809c:8", "const:4:8"]]
+ 0084809c ["CALL", null, ["callee:006a2b78:8"]]
- 0084805c bytes b76af997
+ 0084809c bytes b76af997
~~~


<a id="compare-d269c0de33d7c35c414aa2c3ee776482"></a>

### [`0084807c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084807c.md) → [`008480bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008480bc.md) FUN_008480bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008480b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084807c.md#insn-008480b4) · [`008480c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084807c.md#insn-008480c8) · [`008480d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084807c.md#insn-008480d0)
- 新版 `008480f4`（命令位置の公開資料なし） · `00848108`（命令位置の公開資料なし） · `00848110`（命令位置の公開資料なし）

~~~diff
- 008480b4 ["INT_ADD", "register:40f0:8", ["const:8480b4:8", "const:4:8"]]
- 008480b4 ["CALL", null, ["callee:00c53d00:8"]]
+ 008480f4 ["INT_ADD", "register:40f0:8", ["const:8480f4:8", "const:4:8"]]
+ 008480f4 ["CALL", null, ["callee:00c53d00:8"]]
- 008480b4 bytes 0b2e1094
+ 008480f4 bytes 032f1094
- 008480c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008480c8 ["INT_ADD", "register:40f0:8", ["const:8480c8:8", "const:4:8"]]
- 008480c8 ["CALLIND", null, ["register:0:8"]]
+ 00848108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00848108 ["INT_ADD", "register:40f0:8", ["const:848108:8", "const:4:8"]]
+ 00848108 ["CALLIND", null, ["register:0:8"]]
- 008480c8 bytes 00013fd6
+ 00848108 bytes 00013fd6
- 008480d0 ["INT_ADD", "register:40f0:8", ["const:8480d0:8", "const:4:8"]]
- 008480d0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00848110 ["INT_ADD", "register:40f0:8", ["const:848110:8", "const:4:8"]]
+ 00848110 ["CALL", null, ["callee:00c57e80:8"]]
- 008480d0 bytes 6c3e1094
+ 00848110 bytes 5c3f1094
~~~


<a id="compare-e25cf383c537c9bd2dac59762ce00019"></a>

### [`008480e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md) → [`00848128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848128.md) FUN_00848128

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 7件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0073ae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae08.md) [`0073ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073ae58.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 7件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0073ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae48.md) [`0073ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073ae98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md#insn-00848120) · [`0084812c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md#insn-0084812c) · [`00848148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008480e8.md#insn-00848148)
- 新版 `00848160`（命令位置の公開資料なし） · `0084816c`（命令位置の公開資料なし） · `00848188`（命令位置の公開資料なし）

~~~diff
- 00848120 ["INT_ADD", "register:40f0:8", ["const:848120:8", "const:4:8"]]
- 00848120 ["CALL", null, ["callee:005c179c:8"]]
+ 00848160 ["INT_ADD", "register:40f0:8", ["const:848160:8", "const:4:8"]]
+ 00848160 ["CALL", null, ["callee:005c179c:8"]]
- 00848120 bytes 8fe5f597
+ 00848160 bytes 8fe5f597
- 0084812c ["INT_ADD", "register:40f0:8", ["const:84812c:8", "const:4:8"]]
- 0084812c ["CALL", null, ["callee:005c179c:8"]]
+ 0084816c ["INT_ADD", "register:40f0:8", ["const:84816c:8", "const:4:8"]]
+ 0084816c ["CALL", null, ["callee:005c179c:8"]]
- 0084812c bytes 8ce5f597
+ 0084816c bytes 8ce5f597
- 00848148 ["INT_ADD", "register:40f0:8", ["const:848148:8", "const:4:8"]]
- 00848148 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848188 ["INT_ADD", "register:40f0:8", ["const:848188:8", "const:4:8"]]
+ 00848188 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848148 bytes 5a3e1094
+ 00848188 bytes 4a3f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed12fe66ecff71d45f8ae7524fbc1eca"></a>

### [`00848210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848210.md) → [`00848250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848250.md) FUN_00848250

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869afc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848210.md#insn-00848258) · [`00848260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848210.md#insn-00848260) · [`00848270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848210.md#insn-00848270)
- 新版 `00848298`（命令位置の公開資料なし） · `008482a0`（命令位置の公開資料なし） · `008482b0`（命令位置の公開資料なし）

~~~diff
- 00848258 ["INT_ADD", "register:40f0:8", ["const:848258:8", "const:4:8"]]
- 00848258 ["CALL", null, ["callee:00869b3c:8"]]
+ 00848298 ["INT_ADD", "register:40f0:8", ["const:848298:8", "const:4:8"]]
+ 00848298 ["CALL", null, ["callee:00869b3c:8"]]
- 00848258 bytes 29860094
+ 00848298 bytes 29860094
- 00848260 ["INT_ADD", "register:40f0:8", ["const:848260:8", "const:4:8"]]
- 00848260 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008482a0 ["INT_ADD", "register:40f0:8", ["const:8482a0:8", "const:4:8"]]
+ 008482a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848260 bytes 143e1094
+ 008482a0 bytes 043f1094
- 00848270 ["INT_ADD", "register:40f0:8", ["const:848270:8", "const:4:8"]]
- 00848270 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008482b0 ["INT_ADD", "register:40f0:8", ["const:8482b0:8", "const:4:8"]]
+ 008482b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848270 bytes 103e1094
+ 008482b0 bytes 003f1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a305c4a9c82424616e79675502d8309"></a>

### [`008482e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008482e0.md) → [`00848320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848320.md) FUN_00848320

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008482f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008482e0.md#insn-008482f4) · [`008482fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008482e0.md#insn-008482fc) · [`00848304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008482e0.md#insn-00848304)
- 新版 `00848334`（命令位置の公開資料なし） · `0084833c`（命令位置の公開資料なし） · `00848344`（命令位置の公開資料なし）

~~~diff
- 008482f4 ["INT_ADD", "register:40f0:8", ["const:8482f4:8", "const:4:8"]]
- 008482f4 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00848334 ["INT_ADD", "register:40f0:8", ["const:848334:8", "const:4:8"]]
+ 00848334 ["CALL", null, ["callee:0046e8a4:8"]]
- 008482f4 bytes 5c99f097
+ 00848334 bytes 5c99f097
- 008482fc ["INT_ADD", "register:40f0:8", ["const:8482fc:8", "const:4:8"]]
- 008482fc ["CALL", null, ["callee:0046e8a4:8"]]
+ 0084833c ["INT_ADD", "register:40f0:8", ["const:84833c:8", "const:4:8"]]
+ 0084833c ["CALL", null, ["callee:0046e8a4:8"]]
- 008482fc bytes 5a99f097
+ 0084833c bytes 5a99f097
- 00848304 ["INT_ADD", "register:40f0:8", ["const:848304:8", "const:4:8"]]
- 00848304 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00848344 ["INT_ADD", "register:40f0:8", ["const:848344:8", "const:4:8"]]
+ 00848344 ["CALL", null, ["callee:0046e8a4:8"]]
- 00848304 bytes 5899f097
+ 00848344 bytes 5899f097
~~~


<a id="compare-a0de6a0294328b19b828a1bbca603226"></a>

### [`00848318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848318.md) → [`00848358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848358.md) FUN_00848358

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084832c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848318.md#insn-0084832c) · [`00848334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848318.md#insn-00848334) · [`0084833c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848318.md#insn-0084833c)
- 新版 `0084836c`（命令位置の公開資料なし） · `00848374`（命令位置の公開資料なし） · `0084837c`（命令位置の公開資料なし）

~~~diff
- 0084832c ["INT_ADD", "register:40f0:8", ["const:84832c:8", "const:4:8"]]
- 0084832c ["CALL", null, ["callee:0046efdc:8"]]
+ 0084836c ["INT_ADD", "register:40f0:8", ["const:84836c:8", "const:4:8"]]
+ 0084836c ["CALL", null, ["callee:0046efdc:8"]]
- 0084832c bytes 1c9bf097
+ 0084836c bytes 1c9bf097
- 00848334 ["INT_ADD", "register:40f0:8", ["const:848334:8", "const:4:8"]]
- 00848334 ["CALL", null, ["callee:0046efdc:8"]]
+ 00848374 ["INT_ADD", "register:40f0:8", ["const:848374:8", "const:4:8"]]
+ 00848374 ["CALL", null, ["callee:0046efdc:8"]]
- 00848334 bytes 1a9bf097
+ 00848374 bytes 1a9bf097
- 0084833c ["INT_ADD", "register:40f0:8", ["const:84833c:8", "const:4:8"]]
- 0084833c ["CALL", null, ["callee:0046efdc:8"]]
+ 0084837c ["INT_ADD", "register:40f0:8", ["const:84837c:8", "const:4:8"]]
+ 0084837c ["CALL", null, ["callee:0046efdc:8"]]
- 0084833c bytes 189bf097
+ 0084837c bytes 189bf097
~~~


<a id="compare-4b665f8ba0b896785e9948c285a3b7af"></a>

### [`00848350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848350.md) → [`00848390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848390.md) FUN_00848390

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00810aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810aa8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00810ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810ae8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848350.md#insn-00848368) · [`00848378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848350.md#insn-00848378)
- 新版 `008483a8`（命令位置の公開資料なし） · `008483b8`（命令位置の公開資料なし）

~~~diff
- 00848368 ["INT_ADD", "register:40f0:8", ["const:848368:8", "const:4:8"]]
- 00848368 ["CALL", null, ["callee:00810ae8:8"]]
+ 008483a8 ["INT_ADD", "register:40f0:8", ["const:8483a8:8", "const:4:8"]]
+ 008483a8 ["CALL", null, ["callee:00810ae8:8"]]
- 00848368 bytes d021ff97
+ 008483a8 bytes d021ff97
- 00848378 ["INT_ADD", "register:40f0:8", ["const:848378:8", "const:4:8"]]
- 00848378 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008483b8 ["INT_ADD", "register:40f0:8", ["const:8483b8:8", "const:4:8"]]
+ 008483b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848378 bytes ce3d1094
+ 008483b8 bytes be3e1094
~~~


<a id="compare-76c03f9d237b4d94e92588484fbf260d"></a>

### [`008483a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008483a0.md) → [`008483e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008483e0.md) FUN_008483e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008483e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008483a0.md#insn-008483e0)
- 新版 `00848420`（命令位置の公開資料なし）

~~~diff
- 008483e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008483e0 ["INT_ADD", "register:40f0:8", ["const:8483e0:8", "const:4:8"]]
- 008483e0 ["CALLIND", null, ["register:0:8"]]
+ 00848420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00848420 ["INT_ADD", "register:40f0:8", ["const:848420:8", "const:4:8"]]
+ 00848420 ["CALLIND", null, ["register:0:8"]]
- 008483e0 bytes 00013fd6
+ 00848420 bytes 00013fd6
~~~


<a id="compare-027440d5f0028437283b9e3e2270a231"></a>

### [`00848430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848430.md) → [`00848470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848470.md) FUN_00848470

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848430.md#insn-00848478) · [`00848488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848430.md#insn-00848488)
- 新版 `008484b8`（命令位置の公開資料なし） · `008484c8`（命令位置の公開資料なし）

~~~diff
- 00848478 ["INT_ADD", "register:40f0:8", ["const:848478:8", "const:4:8"]]
- 00848478 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008484b8 ["INT_ADD", "register:40f0:8", ["const:8484b8:8", "const:4:8"]]
+ 008484b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848478 bytes 8e3d1094
+ 008484b8 bytes 7e3e1094
- 00848488 ["INT_ADD", "register:40f0:8", ["const:848488:8", "const:4:8"]]
- 00848488 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008484c8 ["INT_ADD", "register:40f0:8", ["const:8484c8:8", "const:4:8"]]
+ 008484c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848488 bytes 8a3d1094
+ 008484c8 bytes 7a3e1094
~~~


<a id="compare-558a724654ca6b4003545c08c6ee622c"></a>

### [`008484b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484b8.md) → [`008484f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008484f8.md) FUN_008484f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008484d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484b8.md#insn-008484d0)
- 新版 `00848510`（命令位置の公開資料なし）

~~~diff
- 008484d0 ["INT_ADD", "register:40f0:8", ["const:8484d0:8", "const:4:8"]]
- 008484d0 ["CALL", null, ["callee:00869d7c:8"]]
+ 00848510 ["INT_ADD", "register:40f0:8", ["const:848510:8", "const:4:8"]]
+ 00848510 ["CALL", null, ["callee:00869d7c:8"]]
- 008484d0 bytes 1b860094
+ 00848510 bytes 1b860094
~~~


<a id="compare-d2cebefd8883e49c9fda2eb977bccf5d"></a>

### [`008484f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484f8.md) → [`00848538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848538.md) FUN_00848538

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009a4cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a4/009a4cbc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009a4e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4e58.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484f8.md#insn-00848514)
- 新版 `00848554`（命令位置の公開資料なし）

~~~diff
- 00848514 ["INT_ADD", "register:40f0:8", ["const:848514:8", "const:4:8"]]
- 00848514 ["CALL", null, ["callee:009a4e58:8"]]
+ 00848554 ["INT_ADD", "register:40f0:8", ["const:848554:8", "const:4:8"]]
+ 00848554 ["CALL", null, ["callee:009a4e58:8"]]
- 00848514 bytes ea710594
+ 00848554 bytes 41720594
~~~


<a id="compare-e9778799518668ee6ff87de9a09bc75a"></a>

### [`00848534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848534.md) → [`00848574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848574.md) FUN_00848574

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`007ab33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab33c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`007ab37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab37c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848534.md#insn-00848550)
- 新版 `00848590`（命令位置の公開資料なし）

~~~diff
- 00848550 ["INT_ADD", "register:40f0:8", ["const:848550:8", "const:4:8"]]
- 00848550 ["CALL", null, ["callee:007ab37c:8"]]
+ 00848590 ["INT_ADD", "register:40f0:8", ["const:848590:8", "const:4:8"]]
+ 00848590 ["CALL", null, ["callee:007ab37c:8"]]
- 00848550 bytes 7b8bfd97
+ 00848590 bytes 7b8bfd97
~~~


<a id="compare-ad7d4eaf577efbac4ee04de42ad0b413"></a>

### [`00848570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848570.md) → [`008485b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008485b0.md) FUN_008485b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00797a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797a98.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00797ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084858c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848570.md#insn-0084858c)
- 新版 `008485cc`（命令位置の公開資料なし）

~~~diff
- 0084858c ["INT_ADD", "register:40f0:8", ["const:84858c:8", "const:4:8"]]
- 0084858c ["CALL", null, ["callee:00797ad8:8"]]
+ 008485cc ["INT_ADD", "register:40f0:8", ["const:8485cc:8", "const:4:8"]]
+ 008485cc ["CALL", null, ["callee:00797ad8:8"]]
- 0084858c bytes 433dfd97
+ 008485cc bytes 433dfd97
~~~


<a id="compare-44ce7c849f0028072284b41ae8879b72"></a>

### [`008485ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485ac.md) → [`008485ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008485ec.md) FUN_008485ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005b13a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b13a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008485c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485ac.md#insn-008485c8)
- 新版 `00848608`（命令位置の公開資料なし）

~~~diff
- 008485c8 ["INT_ADD", "register:40f0:8", ["const:8485c8:8", "const:4:8"]]
- 008485c8 ["CALL", null, ["callee:005b13a8:8"]]
+ 00848608 ["INT_ADD", "register:40f0:8", ["const:848608:8", "const:4:8"]]
+ 00848608 ["CALL", null, ["callee:005b13a8:8"]]
- 008485c8 bytes 68a3f597
+ 00848608 bytes 68a3f597
~~~


<a id="compare-a2c142f29e2f007b2aecfd874ca0b00e"></a>

### [`008485e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485e8.md) → [`00848628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848628.md) FUN_00848628

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0066295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/0066295c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0066299c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/0066299c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485e8.md#insn-00848608)
- 新版 `00848648`（命令位置の公開資料なし）

~~~diff
- 00848608 ["INT_ADD", "register:40f0:8", ["const:848608:8", "const:4:8"]]
- 00848608 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848648 ["INT_ADD", "register:40f0:8", ["const:848648:8", "const:4:8"]]
+ 00848648 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848608 bytes 2a3d1094
+ 00848648 bytes 1a3e1094
~~~


<a id="compare-77b85f198ca34cbb964eee5cefe0ed04"></a>

### [`00848620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848620.md) → [`00848660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848660.md) FUN_00848660

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0087e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e690.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0087e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e6d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848620.md#insn-0084863c)
- 新版 `0084867c`（命令位置の公開資料なし）

~~~diff
- 0084863c ["INT_ADD", "register:40f0:8", ["const:84863c:8", "const:4:8"]]
- 0084863c ["CALL", null, ["callee:0087e6d0:8"]]
+ 0084867c ["INT_ADD", "register:40f0:8", ["const:84867c:8", "const:4:8"]]
+ 0084867c ["CALL", null, ["callee:0087e6d0:8"]]
- 0084863c bytes 15d80094
+ 0084867c bytes 15d80094
~~~


<a id="compare-0714fb31d86be167ee4191f46fa6ec93"></a>

### [`0084865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084865c.md) → [`0084869c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/0084869c.md) FUN_0084869c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0087d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0087d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084865c.md#insn-00848678)
- 新版 `008486b8`（命令位置の公開資料なし）

~~~diff
- 00848678 ["INT_ADD", "register:40f0:8", ["const:848678:8", "const:4:8"]]
- 00848678 ["CALL", null, ["callee:0087d508:8"]]
+ 008486b8 ["INT_ADD", "register:40f0:8", ["const:8486b8:8", "const:4:8"]]
+ 008486b8 ["CALL", null, ["callee:0087d508:8"]]
- 00848678 bytes 94d30094
+ 008486b8 bytes 94d30094
~~~


<a id="compare-9d2f3b695aef5f02887d6d9fcf145df7"></a>

### [`00848698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848698.md) → [`008486d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008486d8.md) FUN_008486d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008781ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008781ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0087822c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/0087822c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848698.md#insn-008486b4)
- 新版 `008486f4`（命令位置の公開資料なし）

~~~diff
- 008486b4 ["INT_ADD", "register:40f0:8", ["const:8486b4:8", "const:4:8"]]
- 008486b4 ["CALL", null, ["callee:0087822c:8"]]
+ 008486f4 ["INT_ADD", "register:40f0:8", ["const:8486f4:8", "const:4:8"]]
+ 008486f4 ["CALL", null, ["callee:0087822c:8"]]
- 008486b4 bytes cebe0094
+ 008486f4 bytes cebe0094
~~~


<a id="compare-1eeb1458ffbbd20efece041bffb23b39"></a>

### [`008486d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008486d4.md) → [`00848714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848714.md) FUN_00848714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00890f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00890fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890fe0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008486f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008486d4.md#insn-008486f0)
- 新版 `00848730`（命令位置の公開資料なし）

~~~diff
- 008486f0 ["INT_ADD", "register:40f0:8", ["const:8486f0:8", "const:4:8"]]
- 008486f0 ["CALL", null, ["callee:00890fe0:8"]]
+ 00848730 ["INT_ADD", "register:40f0:8", ["const:848730:8", "const:4:8"]]
+ 00848730 ["CALL", null, ["callee:00890fe0:8"]]
- 008486f0 bytes 2b220194
+ 00848730 bytes 2c220194
~~~


<a id="compare-53d4e796d3909525000d49e4245c4a1f"></a>

### [`00848710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848710.md) → [`00848750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848750.md) FUN_00848750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008876e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/008876e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00887724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887724.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084872c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848710.md#insn-0084872c)
- 新版 `0084876c`（命令位置の公開資料なし）

~~~diff
- 0084872c ["INT_ADD", "register:40f0:8", ["const:84872c:8", "const:4:8"]]
- 0084872c ["CALL", null, ["callee:00887724:8"]]
+ 0084876c ["INT_ADD", "register:40f0:8", ["const:84876c:8", "const:4:8"]]
+ 0084876c ["CALL", null, ["callee:00887724:8"]]
- 0084872c bytes eefb0094
+ 0084876c bytes eefb0094
~~~


<a id="compare-6ee9f924a349c8754bacc8b7785e0321"></a>

### [`0084874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084874c.md) → [`0084878c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/0084878c.md) FUN_0084878c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009b86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b86d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009b886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b886c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084874c.md#insn-00848768)
- 新版 `008487a8`（命令位置の公開資料なし）

~~~diff
- 00848768 ["INT_ADD", "register:40f0:8", ["const:848768:8", "const:4:8"]]
- 00848768 ["CALL", null, ["callee:009b886c:8"]]
+ 008487a8 ["INT_ADD", "register:40f0:8", ["const:8487a8:8", "const:4:8"]]
+ 008487a8 ["CALL", null, ["callee:009b886c:8"]]
- 00848768 bytes dabf0594
+ 008487a8 bytes 31c00594
~~~


<a id="compare-b0f0641b37da7d3caeafab22bf513b76"></a>

### [`00848788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848788.md) → [`008487c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008487c8.md) FUN_008487c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008487a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848788.md#insn-008487a8) · [`008487b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848788.md#insn-008487b0)
- 新版 `008487e8`（命令位置の公開資料なし） · `008487f0`（命令位置の公開資料なし）

~~~diff
- 008487a8 ["INT_ADD", "register:40f0:8", ["const:8487a8:8", "const:4:8"]]
- 008487a8 ["CALL", null, ["callee:00869ef4:8"]]
+ 008487e8 ["INT_ADD", "register:40f0:8", ["const:8487e8:8", "const:4:8"]]
+ 008487e8 ["CALL", null, ["callee:00869ef4:8"]]
- 008487a8 bytes c3850094
+ 008487e8 bytes c3850094
- 008487b0 ["INT_ADD", "register:40f0:8", ["const:8487b0:8", "const:4:8"]]
- 008487b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008487f0 ["INT_ADD", "register:40f0:8", ["const:8487f0:8", "const:4:8"]]
+ 008487f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 008487b0 bytes c03c1094
+ 008487f0 bytes b03d1094
~~~


<a id="compare-ad1196020e71aa0464f500c29b29b864"></a>

### [`008487d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md) → [`00848818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848818.md) FUN_00848818

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869f70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md#insn-00848824) · [`00848834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md#insn-00848834) · [`00848844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008487d8.md#insn-00848844)
- 新版 `00848864`（命令位置の公開資料なし） · `00848874`（命令位置の公開資料なし） · `00848884`（命令位置の公開資料なし）

~~~diff
- 00848824 ["INT_ADD", "register:40f0:8", ["const:848824:8", "const:4:8"]]
- 00848824 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848864 ["INT_ADD", "register:40f0:8", ["const:848864:8", "const:4:8"]]
+ 00848864 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848824 bytes a33c1094
+ 00848864 bytes 933d1094
- 00848834 ["INT_ADD", "register:40f0:8", ["const:848834:8", "const:4:8"]]
- 00848834 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848874 ["INT_ADD", "register:40f0:8", ["const:848874:8", "const:4:8"]]
+ 00848874 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848834 bytes 9f3c1094
+ 00848874 bytes 8f3d1094
- 00848844 ["INT_ADD", "register:40f0:8", ["const:848844:8", "const:4:8"]]
- 00848844 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848884 ["INT_ADD", "register:40f0:8", ["const:848884:8", "const:4:8"]]
+ 00848884 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848844 bytes 9b3c1094
+ 00848884 bytes 8b3d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e919dd3a4bdbdd458dc47631697a7e38"></a>

### [`0084889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084889c.md) → [`008488dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008488dc.md) FUN_008488dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a024.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008488b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/0084889c.md#insn-008488b4)
- 新版 `008488f4`（命令位置の公開資料なし）

~~~diff
- 008488b4 ["INT_ADD", "register:40f0:8", ["const:8488b4:8", "const:4:8"]]
- 008488b4 ["CALL", null, ["callee:005c179c:8"]]
+ 008488f4 ["INT_ADD", "register:40f0:8", ["const:8488f4:8", "const:4:8"]]
+ 008488f4 ["CALL", null, ["callee:005c179c:8"]]
- 008488b4 bytes aae3f597
+ 008488f4 bytes aae3f597
~~~


<a id="compare-85c13413ad2f93b611e4a741f7b982a0"></a>

### [`008488cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008488cc.md) → [`0084890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/0084890c.md) FUN_0084890c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008488e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008488cc.md#insn-008488e8) · [`008488f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008488cc.md#insn-008488f8)
- 新版 `00848928`（命令位置の公開資料なし） · `00848938`（命令位置の公開資料なし）

~~~diff
- 008488e8 ["INT_ADD", "register:40f0:8", ["const:8488e8:8", "const:4:8"]]
- 008488e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848928 ["INT_ADD", "register:40f0:8", ["const:848928:8", "const:4:8"]]
+ 00848928 ["CALL", null, ["callee:00c57eb0:8"]]
- 008488e8 bytes 723c1094
+ 00848928 bytes 623d1094
- 008488f8 ["INT_ADD", "register:40f0:8", ["const:8488f8:8", "const:4:8"]]
- 008488f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848938 ["INT_ADD", "register:40f0:8", ["const:848938:8", "const:4:8"]]
+ 00848938 ["CALL", null, ["callee:00c57eb0:8"]]
- 008488f8 bytes 6e3c1094
+ 00848938 bytes 5e3d1094
~~~


<a id="compare-3552a3429aac7cc718f38e0f3abe2262"></a>

### [`00848920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848920.md) → [`00848960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848960.md) FUN_00848960

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 4件 [`005b9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ea4.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005ec020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 4件 [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005ec060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ec/005ec060.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848920.md#insn-0084893c) · [`00848948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848920.md#insn-00848948) · [`00848954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848920.md#insn-00848954)
- 新版 `0084897c`（命令位置の公開資料なし） · `00848988`（命令位置の公開資料なし） · `00848994`（命令位置の公開資料なし）

~~~diff
- 0084893c ["INT_ADD", "register:40f0:8", ["const:84893c:8", "const:4:8"]]
- 0084893c ["CALL", null, ["callee:005b9ee4:8"]]
+ 0084897c ["INT_ADD", "register:40f0:8", ["const:84897c:8", "const:4:8"]]
+ 0084897c ["CALL", null, ["callee:005b9ee4:8"]]
- 0084893c bytes 5ac5f597
+ 0084897c bytes 5ac5f597
- 00848948 ["INT_ADD", "register:40f0:8", ["const:848948:8", "const:4:8"]]
- 00848948 ["CALL", null, ["callee:005b9ee4:8"]]
+ 00848988 ["INT_ADD", "register:40f0:8", ["const:848988:8", "const:4:8"]]
+ 00848988 ["CALL", null, ["callee:005b9ee4:8"]]
- 00848948 bytes 57c5f597
+ 00848988 bytes 57c5f597
- 00848954 ["INT_ADD", "register:40f0:8", ["const:848954:8", "const:4:8"]]
- 00848954 ["CALL", null, ["callee:005b9ee4:8"]]
+ 00848994 ["INT_ADD", "register:40f0:8", ["const:848994:8", "const:4:8"]]
+ 00848994 ["CALL", null, ["callee:005b9ee4:8"]]
- 00848954 bytes 54c5f597
+ 00848994 bytes 54c5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33c0197903a5919b2cbc7d952b4cb07f"></a>

### [`008489ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md) → [`00848a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848a2c.md) FUN_00848a2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 7件 [`006a0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md) [`006a1468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1468.md) [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`0086a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a074.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 7件 [`006a0244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a0244.md) [`006a14a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a14a8.md) [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`0086a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md#insn-00848a20) · [`00848a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md#insn-00848a28) · [`00848a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md#insn-00848a64)
- 新版 `00848a60`（命令位置の公開資料なし） · `00848a68`（命令位置の公開資料なし） · `00848aa4`（命令位置の公開資料なし）

~~~diff
- 00848a20 ["INT_ADD", "register:40f0:8", ["const:848a20:8", "const:4:8"]]
- 00848a20 ["CALL", null, ["callee:006a2b78:8"]]
+ 00848a60 ["INT_ADD", "register:40f0:8", ["const:848a60:8", "const:4:8"]]
+ 00848a60 ["CALL", null, ["callee:006a2b78:8"]]
- 00848a20 bytes 4668f997
+ 00848a60 bytes 4668f997
- 00848a28 ["INT_ADD", "register:40f0:8", ["const:848a28:8", "const:4:8"]]
- 00848a28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848a68 ["INT_ADD", "register:40f0:8", ["const:848a68:8", "const:4:8"]]
+ 00848a68 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848a28 bytes 223c1094
+ 00848a68 bytes 123d1094
- 00848a64 ["INT_ADD", "register:40f0:8", ["const:848a64:8", "const:4:8"]]
- 00848a64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848aa4 ["INT_ADD", "register:40f0:8", ["const:848aa4:8", "const:4:8"]]
+ 00848aa4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848a64 bytes 133c1094
+ 00848aa4 bytes 033d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad8588136678208f760a04339cd83be"></a>

### [`00848ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ae0.md) → [`00848b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b20.md) FUN_00848b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a124.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ae0.md#insn-00848af8) · [`00848b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ae0.md#insn-00848b04)
- 新版 `00848b38`（命令位置の公開資料なし） · `00848b44`（命令位置の公開資料なし）

~~~diff
- 00848af8 ["INT_ADD", "register:40f0:8", ["const:848af8:8", "const:4:8"]]
- 00848af8 ["CALL", null, ["callee:005c179c:8"]]
+ 00848b38 ["INT_ADD", "register:40f0:8", ["const:848b38:8", "const:4:8"]]
+ 00848b38 ["CALL", null, ["callee:005c179c:8"]]
- 00848af8 bytes 19e3f597
+ 00848b38 bytes 19e3f597
- 00848b04 ["INT_ADD", "register:40f0:8", ["const:848b04:8", "const:4:8"]]
- 00848b04 ["CALL", null, ["callee:005c179c:8"]]
+ 00848b44 ["INT_ADD", "register:40f0:8", ["const:848b44:8", "const:4:8"]]
+ 00848b44 ["CALL", null, ["callee:005c179c:8"]]
- 00848b04 bytes 16e3f597
+ 00848b44 bytes 16e3f597
~~~


<a id="compare-cb12020785d335cff4bcb86fa411af74"></a>

### [`00848b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b1c.md) → [`00848b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b5c.md) FUN_00848b5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b1c.md#insn-00848b34) · [`00848b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b1c.md#insn-00848b40)
- 新版 `00848b74`（命令位置の公開資料なし） · `00848b80`（命令位置の公開資料なし）

~~~diff
- 00848b34 ["INT_ADD", "register:40f0:8", ["const:848b34:8", "const:4:8"]]
- 00848b34 ["CALL", null, ["callee:005c17e0:8"]]
+ 00848b74 ["INT_ADD", "register:40f0:8", ["const:848b74:8", "const:4:8"]]
+ 00848b74 ["CALL", null, ["callee:005c17e0:8"]]
- 00848b34 bytes 1be3f597
+ 00848b74 bytes 1be3f597
- 00848b40 ["INT_ADD", "register:40f0:8", ["const:848b40:8", "const:4:8"]]
- 00848b40 ["CALL", null, ["callee:00676a60:8"]]
+ 00848b80 ["INT_ADD", "register:40f0:8", ["const:848b80:8", "const:4:8"]]
+ 00848b80 ["CALL", null, ["callee:00676a60:8"]]
- 00848b40 bytes b8b7f897
+ 00848b80 bytes b8b7f897
~~~


<a id="compare-6912ec9beb8c3c62aed4f892ae0ac417"></a>

### [`00848b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md) → [`00848b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b98.md) FUN_00848b98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a168.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md#insn-00848b70) · [`00848b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md#insn-00848b7c) · [`00848b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848b58.md#insn-00848b8c)
- 新版 `00848bb0`（命令位置の公開資料なし） · `00848bbc`（命令位置の公開資料なし） · `00848bcc`（命令位置の公開資料なし）

~~~diff
- 00848b70 ["INT_ADD", "register:40f0:8", ["const:848b70:8", "const:4:8"]]
- 00848b70 ["CALL", null, ["callee:005c179c:8"]]
+ 00848bb0 ["INT_ADD", "register:40f0:8", ["const:848bb0:8", "const:4:8"]]
+ 00848bb0 ["CALL", null, ["callee:005c179c:8"]]
- 00848b70 bytes fbe2f597
+ 00848bb0 bytes fbe2f597
- 00848b7c ["INT_ADD", "register:40f0:8", ["const:848b7c:8", "const:4:8"]]
- 00848b7c ["CALL", null, ["callee:005c179c:8"]]
+ 00848bbc ["INT_ADD", "register:40f0:8", ["const:848bbc:8", "const:4:8"]]
+ 00848bbc ["CALL", null, ["callee:005c179c:8"]]
- 00848b7c bytes f8e2f597
+ 00848bbc bytes f8e2f597
- 00848b8c ["INT_ADD", "register:40f0:8", ["const:848b8c:8", "const:4:8"]]
- 00848b8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848bcc ["INT_ADD", "register:40f0:8", ["const:848bcc:8", "const:4:8"]]
+ 00848bcc ["CALL", null, ["callee:00c57eb0:8"]]
- 00848b8c bytes c93b1094
+ 00848bcc bytes b93c1094
~~~


<a id="compare-a95b92a294cf1069224f98aa99b96d08"></a>

### [`00848ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ba4.md) → [`00848be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848be4.md) FUN_00848be4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ba4.md#insn-00848bbc) · [`00848bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ba4.md#insn-00848bc8)
- 新版 `00848bfc`（命令位置の公開資料なし） · `00848c08`（命令位置の公開資料なし）

~~~diff
- 00848bbc ["INT_ADD", "register:40f0:8", ["const:848bbc:8", "const:4:8"]]
- 00848bbc ["CALL", null, ["callee:005c17e0:8"]]
+ 00848bfc ["INT_ADD", "register:40f0:8", ["const:848bfc:8", "const:4:8"]]
+ 00848bfc ["CALL", null, ["callee:005c17e0:8"]]
- 00848bbc bytes f9e2f597
+ 00848bfc bytes f9e2f597
- 00848bc8 ["INT_ADD", "register:40f0:8", ["const:848bc8:8", "const:4:8"]]
- 00848bc8 ["CALL", null, ["callee:00676a60:8"]]
+ 00848c08 ["INT_ADD", "register:40f0:8", ["const:848c08:8", "const:4:8"]]
+ 00848c08 ["CALL", null, ["callee:00676a60:8"]]
- 00848bc8 bytes 96b7f897
+ 00848c08 bytes 96b7f897
~~~


<a id="compare-f239db5e5132cc35ff30d6ff0e7e5e86"></a>

### [`00848be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md) → [`00848c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848c20.md) FUN_00848c20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 5件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 5件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md#insn-00848bf8) · [`00848c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md#insn-00848c00) · [`00848c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md#insn-00848c10)
- 新版 `00848c38`（命令位置の公開資料なし） · `00848c40`（命令位置の公開資料なし） · `00848c50`（命令位置の公開資料なし）

~~~diff
- 00848bf8 ["INT_ADD", "register:40f0:8", ["const:848bf8:8", "const:4:8"]]
- 00848bf8 ["CALL", null, ["callee:0046e8a4:8"]]
+ 00848c38 ["INT_ADD", "register:40f0:8", ["const:848c38:8", "const:4:8"]]
+ 00848c38 ["CALL", null, ["callee:0046e8a4:8"]]
- 00848bf8 bytes 1b97f097
+ 00848c38 bytes 1b97f097
- 00848c00 ["INT_ADD", "register:40f0:8", ["const:848c00:8", "const:4:8"]]
- 00848c00 ["CALL", null, ["callee:0046efdc:8"]]
+ 00848c40 ["INT_ADD", "register:40f0:8", ["const:848c40:8", "const:4:8"]]
+ 00848c40 ["CALL", null, ["callee:0046efdc:8"]]
- 00848c00 bytes e798f097
+ 00848c40 bytes e798f097
- 00848c10 ["INT_ADD", "register:40f0:8", ["const:848c10:8", "const:4:8"]]
- 00848c10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848c50 ["INT_ADD", "register:40f0:8", ["const:848c50:8", "const:4:8"]]
+ 00848c50 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848c10 bytes a83b1094
+ 00848c50 bytes 983c1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-380f073be0b45ba114738917835b5eb8"></a>

### [`00848cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md) → [`00848cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848cfc.md) FUN_00848cfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`0086a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a238.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md#insn-00848cdc) · [`00848ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md#insn-00848ce4) · [`00848cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848cbc.md#insn-00848cec)
- 新版 `00848d1c`（命令位置の公開資料なし） · `00848d24`（命令位置の公開資料なし） · `00848d2c`（命令位置の公開資料なし）

~~~diff
- 00848cdc ["INT_ADD", "register:40f0:8", ["const:848cdc:8", "const:4:8"]]
- 00848cdc ["CALL", null, ["callee:006a2b78:8"]]
+ 00848d1c ["INT_ADD", "register:40f0:8", ["const:848d1c:8", "const:4:8"]]
+ 00848d1c ["CALL", null, ["callee:006a2b78:8"]]
- 00848cdc bytes 9767f997
+ 00848d1c bytes 9767f997
- 00848ce4 ["INT_ADD", "register:40f0:8", ["const:848ce4:8", "const:4:8"]]
- 00848ce4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848d24 ["INT_ADD", "register:40f0:8", ["const:848d24:8", "const:4:8"]]
+ 00848d24 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848ce4 bytes 733b1094
+ 00848d24 bytes 633c1094
- 00848cec ["INT_ADD", "register:40f0:8", ["const:848cec:8", "const:4:8"]]
- 00848cec ["CALL", null, ["callee:00c57e60:8"]]
+ 00848d2c ["INT_ADD", "register:40f0:8", ["const:848d2c:8", "const:4:8"]]
+ 00848d2c ["CALL", null, ["callee:00c57e60:8"]]
- 00848cec bytes 5d3b1094
+ 00848d2c bytes 4d3c1094
~~~


<a id="compare-56a25dc69d1f094eebd1a8856b9738fe"></a>

### [`00848d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md) → [`00848d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848d44.md) FUN_00848d44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`00731968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731968.md) [`00731a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`007319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/007319a8.md) [`00731a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md#insn-00848d20) · [`00848d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md#insn-00848d54) · [`00848d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848d04.md#insn-00848d64)
- 新版 `00848d60`（命令位置の公開資料なし） · `00848d94`（命令位置の公開資料なし） · `00848da4`（命令位置の公開資料なし）

~~~diff
- 00848d20 ["INT_ADD", "register:40f0:8", ["const:848d20:8", "const:4:8"]]
- 00848d20 ["CALL", null, ["callee:00731a80:8"]]
+ 00848d60 ["INT_ADD", "register:40f0:8", ["const:848d60:8", "const:4:8"]]
+ 00848d60 ["CALL", null, ["callee:00731a80:8"]]
- 00848d20 bytes 48a3fb97
+ 00848d60 bytes 48a3fb97
- 00848d54 ["INT_ADD", "register:40f0:8", ["const:848d54:8", "const:4:8"]]
- 00848d54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848d94 ["INT_ADD", "register:40f0:8", ["const:848d94:8", "const:4:8"]]
+ 00848d94 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848d54 bytes 573b1094
+ 00848d94 bytes 473c1094
- 00848d64 ["INT_ADD", "register:40f0:8", ["const:848d64:8", "const:4:8"]]
- 00848d64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848da4 ["INT_ADD", "register:40f0:8", ["const:848da4:8", "const:4:8"]]
+ 00848da4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848d64 bytes 533b1094
+ 00848da4 bytes 433c1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30075e83df53a3880bbef9a4e623dc2a"></a>

### [`00848ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ee8.md) → [`00848f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848f28.md) FUN_00848f28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ee8.md#insn-00848f04) · [`00848f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ee8.md#insn-00848f14) · [`00848f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848ee8.md#insn-00848f24)
- 新版 `00848f44`（命令位置の公開資料なし） · `00848f54`（命令位置の公開資料なし） · `00848f64`（命令位置の公開資料なし）

~~~diff
- 00848f04 ["INT_ADD", "register:40f0:8", ["const:848f04:8", "const:4:8"]]
- 00848f04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848f44 ["INT_ADD", "register:40f0:8", ["const:848f44:8", "const:4:8"]]
+ 00848f44 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848f04 bytes eb3a1094
+ 00848f44 bytes db3b1094
- 00848f14 ["INT_ADD", "register:40f0:8", ["const:848f14:8", "const:4:8"]]
- 00848f14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848f54 ["INT_ADD", "register:40f0:8", ["const:848f54:8", "const:4:8"]]
+ 00848f54 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848f14 bytes e73a1094
+ 00848f54 bytes d73b1094
- 00848f24 ["INT_ADD", "register:40f0:8", ["const:848f24:8", "const:4:8"]]
- 00848f24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00848f64 ["INT_ADD", "register:40f0:8", ["const:848f64:8", "const:4:8"]]
+ 00848f64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00848f24 bytes e33a1094
+ 00848f64 bytes d33b1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-effeed96eed486f924bae22763c5b601"></a>

### [`00848f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md) → [`00848f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848f94.md) FUN_00848f94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 5件 [`006923f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md) [`00692440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md) [`0086a298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a298.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 5件 [`00692430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692430.md) [`00692480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692480.md) [`0086a2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00848f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md#insn-00848f84) · [`00848f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md#insn-00848f90) · [`00848fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md#insn-00848fa0)
- 新版 `00848fc4`（命令位置の公開資料なし） · `00848fd0`（命令位置の公開資料なし） · `00848fe0`（命令位置の公開資料なし）

~~~diff
- 00848f84 ["INT_ADD", "register:40f0:8", ["const:848f84:8", "const:4:8"]]
- 00848f84 ["CALL", null, ["callee:00692480:8"]]
+ 00848fc4 ["INT_ADD", "register:40f0:8", ["const:848fc4:8", "const:4:8"]]
+ 00848fc4 ["CALL", null, ["callee:00692480:8"]]
- 00848f84 bytes 2f25f997
+ 00848fc4 bytes 2f25f997
- 00848f90 ["INT_ADD", "register:40f0:8", ["const:848f90:8", "const:4:8"]]
- 00848f90 ["CALL", null, ["callee:00692430:8"]]
+ 00848fd0 ["INT_ADD", "register:40f0:8", ["const:848fd0:8", "const:4:8"]]
+ 00848fd0 ["CALL", null, ["callee:00692430:8"]]
- 00848f90 bytes 1825f997
+ 00848fd0 bytes 1825f997
- 00848fa0 ["INT_ADD", "register:40f0:8", ["const:848fa0:8", "const:4:8"]]
- 00848fa0 ["CALL", null, ["callee:0086a2d8:8"]]
+ 00848fe0 ["INT_ADD", "register:40f0:8", ["const:848fe0:8", "const:4:8"]]
+ 00848fe0 ["CALL", null, ["callee:0086a2d8:8"]]
- 00848fa0 bytes be840094
+ 00848fe0 bytes be840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563749161d2b14218adbbf299150e200"></a>

### [`008490ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008490ec.md) → [`0084912c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084912c.md) FUN_0084912c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008490ec.md#insn-00849134)
- 新版 `00849174`（命令位置の公開資料なし）

~~~diff
- 00849134 ["INT_ADD", "register:40f0:8", ["const:849134:8", "const:4:8"]]
- 00849134 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849174 ["INT_ADD", "register:40f0:8", ["const:849174:8", "const:4:8"]]
+ 00849174 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849134 bytes 5f3a1094
+ 00849174 bytes 4f3b1094
~~~


<a id="compare-f43277c55c005fce2275d9e3a6bee7e1"></a>

### [`00849164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849164.md) → [`008491a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008491a4.md) FUN_008491a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0080b2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b2e4.md) [`0080b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b328.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0080b324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b324.md) [`0080b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b368.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084917c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849164.md#insn-0084917c) · [`00849188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849164.md#insn-00849188)
- 新版 `008491bc`（命令位置の公開資料なし） · `008491c8`（命令位置の公開資料なし）

~~~diff
- 0084917c ["INT_ADD", "register:40f0:8", ["const:84917c:8", "const:4:8"]]
- 0084917c ["CALL", null, ["callee:005c179c:8"]]
+ 008491bc ["INT_ADD", "register:40f0:8", ["const:8491bc:8", "const:4:8"]]
+ 008491bc ["CALL", null, ["callee:005c179c:8"]]
- 0084917c bytes 78e1f597
+ 008491bc bytes 78e1f597
- 00849188 ["INT_ADD", "register:40f0:8", ["const:849188:8", "const:4:8"]]
- 00849188 ["CALL", null, ["callee:0080b324:8"]]
+ 008491c8 ["INT_ADD", "register:40f0:8", ["const:8491c8:8", "const:4:8"]]
+ 008491c8 ["CALL", null, ["callee:0080b324:8"]]
- 00849188 bytes 5708ff97
+ 008491c8 bytes 5708ff97
~~~


<a id="compare-f4a1ab09a98aefcaf5570b5b6f3eaab4"></a>

### [`008491a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491a0.md) → [`008491e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008491e0.md) FUN_008491e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00676a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a78.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676ab8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008491b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491a0.md#insn-008491b8) · [`008491c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491a0.md#insn-008491c4)
- 新版 `008491f8`（命令位置の公開資料なし） · `00849204`（命令位置の公開資料なし）

~~~diff
- 008491b8 ["INT_ADD", "register:40f0:8", ["const:8491b8:8", "const:4:8"]]
- 008491b8 ["CALL", null, ["callee:005c1bf0:8"]]
+ 008491f8 ["INT_ADD", "register:40f0:8", ["const:8491f8:8", "const:4:8"]]
+ 008491f8 ["CALL", null, ["callee:005c1bf0:8"]]
- 008491b8 bytes 7ee2f597
+ 008491f8 bytes 7ee2f597
- 008491c4 ["INT_ADD", "register:40f0:8", ["const:8491c4:8", "const:4:8"]]
- 008491c4 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00849204 ["INT_ADD", "register:40f0:8", ["const:849204:8", "const:4:8"]]
+ 00849204 ["CALL", null, ["callee:005c3e7c:8"]]
- 008491c4 bytes 1eebf597
+ 00849204 bytes 1eebf597
~~~


<a id="compare-6e6e7cad3948096d10b9bd8e19852852"></a>

### [`008491dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md) → [`0084921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084921c.md) FUN_0084921c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0067762c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/0067762c.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0067766c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/0067766c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008491f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md#insn-008491f4) · [`00849200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md#insn-00849200) · [`0084920c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md#insn-0084920c)
- 新版 `00849234`（命令位置の公開資料なし） · `00849240`（命令位置の公開資料なし） · `0084924c`（命令位置の公開資料なし）

~~~diff
- 008491f4 ["INT_ADD", "register:40f0:8", ["const:8491f4:8", "const:4:8"]]
- 008491f4 ["CALL", null, ["callee:00676a60:8"]]
+ 00849234 ["INT_ADD", "register:40f0:8", ["const:849234:8", "const:4:8"]]
+ 00849234 ["CALL", null, ["callee:00676a60:8"]]
- 008491f4 bytes 0bb6f897
+ 00849234 bytes 0bb6f897
- 00849200 ["INT_ADD", "register:40f0:8", ["const:849200:8", "const:4:8"]]
- 00849200 ["CALL", null, ["callee:005c179c:8"]]
+ 00849240 ["INT_ADD", "register:40f0:8", ["const:849240:8", "const:4:8"]]
+ 00849240 ["CALL", null, ["callee:005c179c:8"]]
- 00849200 bytes 57e1f597
+ 00849240 bytes 57e1f597
- 0084920c ["INT_ADD", "register:40f0:8", ["const:84920c:8", "const:4:8"]]
- 0084920c ["CALL", null, ["callee:005c179c:8"]]
+ 0084924c ["INT_ADD", "register:40f0:8", ["const:84924c:8", "const:4:8"]]
+ 0084924c ["CALL", null, ["callee:005c179c:8"]]
- 0084920c bytes 54e1f597
+ 0084924c bytes 54e1f597
~~~


<a id="compare-1911d2599b64f2643b2374005feb37aa"></a>

### [`00849224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849224.md) → [`00849264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849264.md) FUN_00849264

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0067c760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c760.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0067c7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c7a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849224.md#insn-00849268) · [`00849278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849224.md#insn-00849278)
- 新版 `008492a8`（命令位置の公開資料なし） · `008492b8`（命令位置の公開資料なし）

~~~diff
- 00849268 ["INT_ADD", "register:40f0:8", ["const:849268:8", "const:4:8"]]
- 00849268 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008492a8 ["INT_ADD", "register:40f0:8", ["const:8492a8:8", "const:4:8"]]
+ 008492a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849268 bytes 123a1094
+ 008492a8 bytes 023b1094
- 00849278 ["INT_ADD", "register:40f0:8", ["const:849278:8", "const:4:8"]]
- 00849278 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008492b8 ["INT_ADD", "register:40f0:8", ["const:8492b8:8", "const:4:8"]]
+ 008492b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849278 bytes 0e3a1094
+ 008492b8 bytes fe3a1094
~~~


<a id="compare-565b06dcd99cd5858f441a66a3e4b361"></a>

### [`00849294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849294.md) → [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) FUN_008492d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a348.md) [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008492ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849294.md#insn-008492ac)
- 新版 `008492ec`（命令位置の公開資料なし）

~~~diff
- 008492ac ["INT_ADD", "register:40f0:8", ["const:8492ac:8", "const:4:8"]]
- 008492ac ["CALL", null, ["callee:0086be6c:8"]]
+ 008492ec ["INT_ADD", "register:40f0:8", ["const:8492ec:8", "const:4:8"]]
+ 008492ec ["CALL", null, ["callee:0086be6c:8"]]
- 008492ac bytes e08a0094
+ 008492ec bytes e08a0094
~~~


<a id="compare-39be755d108eef1540ec3576827df388"></a>

### [`008492c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492c4.md) → [`00849304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849304.md) FUN_00849304

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a3ac.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008492dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492c4.md#insn-008492dc)
- 新版 `0084931c`（命令位置の公開資料なし）

~~~diff
- 008492dc ["INT_ADD", "register:40f0:8", ["const:8492dc:8", "const:4:8"]]
- 008492dc ["CALL", null, ["callee:005c179c:8"]]
+ 0084931c ["INT_ADD", "register:40f0:8", ["const:84931c:8", "const:4:8"]]
+ 0084931c ["CALL", null, ["callee:005c179c:8"]]
- 008492dc bytes 20e1f597
+ 0084931c bytes 20e1f597
~~~


<a id="compare-7a1ab44e2b0145d73a1512720f9a5079"></a>

### [`008492f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492f4.md) → [`00849334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849334.md) FUN_00849334

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009b396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b396c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009b3b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492f4.md#insn-00849310)
- 新版 `00849350`（命令位置の公開資料なし）

~~~diff
- 00849310 ["INT_ADD", "register:40f0:8", ["const:849310:8", "const:4:8"]]
- 00849310 ["CALL", null, ["callee:009b3b08:8"]]
+ 00849350 ["INT_ADD", "register:40f0:8", ["const:849350:8", "const:4:8"]]
+ 00849350 ["CALL", null, ["callee:009b3b08:8"]]
- 00849310 bytes 97a90594
+ 00849350 bytes eea90594
~~~


<a id="compare-d6f415111b9d691831268c5371360837"></a>

### [`00849330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md) → [`00849370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md) FUN_00849370

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`007477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/007477c4.md) [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md#insn-00849368) · [`0084937c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md#insn-0084937c) · [`00849388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849330.md#insn-00849388)
- 新版 `008493a8`（命令位置の公開資料なし） · `008493bc`（命令位置の公開資料なし） · `008493c8`（命令位置の公開資料なし）

~~~diff
- 00849368 ["INT_ADD", "register:40f0:8", ["const:849368:8", "const:4:8"]]
- 00849368 ["CALL", null, ["callee:00748b30:8"]]
+ 008493a8 ["INT_ADD", "register:40f0:8", ["const:8493a8:8", "const:4:8"]]
+ 008493a8 ["CALL", null, ["callee:00748b30:8"]]
- 00849368 bytes e2fdfb97
+ 008493a8 bytes e2fdfb97
- 0084937c ["INT_ADD", "register:40f0:8", ["const:84937c:8", "const:4:8"]]
- 0084937c ["CALL", null, ["callee:00c57eb0:8"]]
+ 008493bc ["INT_ADD", "register:40f0:8", ["const:8493bc:8", "const:4:8"]]
+ 008493bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0084937c bytes cd391094
+ 008493bc bytes bd3a1094
- 00849388 ["INT_ADD", "register:40f0:8", ["const:849388:8", "const:4:8"]]
- 00849388 ["CALL", null, ["callee:00676a60:8"]]
+ 008493c8 ["INT_ADD", "register:40f0:8", ["const:8493c8:8", "const:4:8"]]
+ 008493c8 ["CALL", null, ["callee:00676a60:8"]]
- 00849388 bytes a6b5f897
+ 008493c8 bytes a6b5f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14bbc7d93f0dde127ba90c2621d1b06"></a>

### [`008493c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md) → [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) FUN_00849400

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md) [`0086a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a4b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`0086a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008493f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md#insn-008493f0) · [`008493fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md#insn-008493fc) · [`00849408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008493c0.md#insn-00849408)
- 新版 `00849430`（命令位置の公開資料なし） · `0084943c`（命令位置の公開資料なし） · `00849448`（命令位置の公開資料なし）

~~~diff
- 008493f0 ["INT_ADD", "register:40f0:8", ["const:8493f0:8", "const:4:8"]]
- 008493f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849430 ["INT_ADD", "register:40f0:8", ["const:849430:8", "const:4:8"]]
+ 00849430 ["CALL", null, ["callee:00c57eb0:8"]]
- 008493f0 bytes b0391094
+ 00849430 bytes a03a1094
- 008493fc ["INT_ADD", "register:40f0:8", ["const:8493fc:8", "const:4:8"]]
- 008493fc ["CALL", null, ["callee:0086a460:8"]]
+ 0084943c ["INT_ADD", "register:40f0:8", ["const:84943c:8", "const:4:8"]]
+ 0084943c ["CALL", null, ["callee:0086a460:8"]]
- 008493fc bytes 09840094
+ 0084943c bytes 09840094
- 00849408 ["INT_ADD", "register:40f0:8", ["const:849408:8", "const:4:8"]]
- 00849408 ["CALL", null, ["callee:0086a4b0:8"]]
+ 00849448 ["INT_ADD", "register:40f0:8", ["const:849448:8", "const:4:8"]]
+ 00849448 ["CALL", null, ["callee:0086a4b0:8"]]
- 00849408 bytes 1a840094
+ 00849448 bytes 1a840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6bc12e8752c57e25eb8184817759194"></a>

### [`00849490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849490.md) → [`008494d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008494d0.md) FUN_008494d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008494b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849490.md#insn-008494b4) · [`008494c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849490.md#insn-008494c4) · [`008494d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849490.md#insn-008494d0)
- 新版 `008494f4`（命令位置の公開資料なし） · `00849504`（命令位置の公開資料なし） · `00849510`（命令位置の公開資料なし）

~~~diff
- 008494b4 ["INT_ADD", "register:40f0:8", ["const:8494b4:8", "const:4:8"]]
- 008494b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008494f4 ["INT_ADD", "register:40f0:8", ["const:8494f4:8", "const:4:8"]]
+ 008494f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 008494b4 bytes 7f391094
+ 008494f4 bytes 6f3a1094
- 008494c4 ["INT_ADD", "register:40f0:8", ["const:8494c4:8", "const:4:8"]]
- 008494c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849504 ["INT_ADD", "register:40f0:8", ["const:849504:8", "const:4:8"]]
+ 00849504 ["CALL", null, ["callee:00c57eb0:8"]]
- 008494c4 bytes 7b391094
+ 00849504 bytes 6b3a1094
- 008494d0 ["INT_ADD", "register:40f0:8", ["const:8494d0:8", "const:4:8"]]
- 008494d0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849510 ["INT_ADD", "register:40f0:8", ["const:849510:8", "const:4:8"]]
+ 00849510 ["CALL", null, ["callee:00c57eb0:8"]]
- 008494d0 bytes 78391094
+ 00849510 bytes 683a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0feb83c87c8d8dafc75404a5e3d8387"></a>

### [`008496f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008496f4.md) → [`00849734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849734.md) FUN_00849734

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008496f4.md#insn-00849710)
- 新版 `00849750`（命令位置の公開資料なし）

~~~diff
- 00849710 ["INT_ADD", "register:40f0:8", ["const:849710:8", "const:4:8"]]
- 00849710 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849750 ["INT_ADD", "register:40f0:8", ["const:849750:8", "const:4:8"]]
+ 00849750 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849710 bytes e8381094
+ 00849750 bytes d8391094
~~~


<a id="compare-bd2f6ff06c5cddb49f299d9f31b464e5"></a>

### [`00849738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md) → [`00849778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md) FUN_00849778

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`0086a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a564.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0086a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md#insn-00849760) · [`0084976c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md#insn-0084976c) · [`00849790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849738.md#insn-00849790)
- 新版 `008497a0`（命令位置の公開資料なし） · `008497ac`（命令位置の公開資料なし） · `008497d0`（命令位置の公開資料なし）

~~~diff
- 00849760 ["INT_ADD", "register:40f0:8", ["const:849760:8", "const:4:8"]]
- 00849760 ["CALL", null, ["callee:0073a304:8"]]
+ 008497a0 ["INT_ADD", "register:40f0:8", ["const:8497a0:8", "const:4:8"]]
+ 008497a0 ["CALL", null, ["callee:0073a304:8"]]
- 00849760 bytes d9c2fb97
+ 008497a0 bytes d9c2fb97
- 0084976c ["INT_ADD", "register:40f0:8", ["const:84976c:8", "const:4:8"]]
- 0084976c ["CALL", null, ["callee:0086a5a4:8"]]
+ 008497ac ["INT_ADD", "register:40f0:8", ["const:8497ac:8", "const:4:8"]]
+ 008497ac ["CALL", null, ["callee:0086a5a4:8"]]
- 0084976c bytes 7e830094
+ 008497ac bytes 7e830094
- 00849790 ["INT_ADD", "register:40f0:8", ["const:849790:8", "const:4:8"]]
- 00849790 ["CALL", null, ["callee:00c57ee0:8"]]
+ 008497d0 ["INT_ADD", "register:40f0:8", ["const:8497d0:8", "const:4:8"]]
+ 008497d0 ["CALL", null, ["callee:00c57ee0:8"]]
- 00849790 bytes d4381094
+ 008497d0 bytes c4391094
~~~


<a id="compare-2227dc813ec88a3c2fe730fdc1fa5ca4"></a>

### [`00849794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849794.md) → [`008497d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008497d4.md) FUN_008497d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008497b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849794.md#insn-008497b0)
- 新版 `008497f0`（命令位置の公開資料なし）

~~~diff
- 008497b0 ["INT_ADD", "register:40f0:8", ["const:8497b0:8", "const:4:8"]]
- 008497b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008497f0 ["INT_ADD", "register:40f0:8", ["const:8497f0:8", "const:4:8"]]
+ 008497f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 008497b0 bytes c0381094
+ 008497f0 bytes b0391094
~~~


<a id="compare-b8bcb2fab7601195b6dc22f9c61de224"></a>

### [`008497d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md) → [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) FUN_00849818

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008497f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md#insn-008497f8) · [`00849804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md#insn-00849804) · [`00849810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md#insn-00849810)
- 新版 `00849838`（命令位置の公開資料なし） · `00849844`（命令位置の公開資料なし） · `00849850`（命令位置の公開資料なし）

~~~diff
- 008497f8 ["INT_ADD", "register:40f0:8", ["const:8497f8:8", "const:4:8"]]
- 008497f8 ["CALL", null, ["callee:005c179c:8"]]
+ 00849838 ["INT_ADD", "register:40f0:8", ["const:849838:8", "const:4:8"]]
+ 00849838 ["CALL", null, ["callee:005c179c:8"]]
- 008497f8 bytes d9dff597
+ 00849838 bytes d9dff597
- 00849804 ["INT_ADD", "register:40f0:8", ["const:849804:8", "const:4:8"]]
- 00849804 ["CALL", null, ["callee:0086bb98:8"]]
+ 00849844 ["INT_ADD", "register:40f0:8", ["const:849844:8", "const:4:8"]]
+ 00849844 ["CALL", null, ["callee:0086bb98:8"]]
- 00849804 bytes d5880094
+ 00849844 bytes d5880094
- 00849810 ["INT_ADD", "register:40f0:8", ["const:849810:8", "const:4:8"]]
- 00849810 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00849850 ["INT_ADD", "register:40f0:8", ["const:849850:8", "const:4:8"]]
+ 00849850 ["CALL", null, ["callee:005c3e7c:8"]]
- 00849810 bytes 8be9f597
+ 00849850 bytes 8be9f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a45e82966a14724490370f2140607a8"></a>

### [`0084983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md) → [`0084987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md) FUN_0084987c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0066b99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b99c.md) [`0066ba64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba64.md) [`0086a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a614.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0066b9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b9dc.md) [`0066baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baa4.md) [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md#insn-00849858) · [`00849864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md#insn-00849864) · [`00849870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md#insn-00849870)
- 新版 `00849898`（命令位置の公開資料なし） · `008498a4`（命令位置の公開資料なし） · `008498b0`（命令位置の公開資料なし）

~~~diff
- 00849858 ["INT_ADD", "register:40f0:8", ["const:849858:8", "const:4:8"]]
- 00849858 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849898 ["INT_ADD", "register:40f0:8", ["const:849898:8", "const:4:8"]]
+ 00849898 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849858 bytes 96381094
+ 00849898 bytes 86391094
- 00849864 ["INT_ADD", "register:40f0:8", ["const:849864:8", "const:4:8"]]
- 00849864 ["CALL", null, ["callee:0086a654:8"]]
+ 008498a4 ["INT_ADD", "register:40f0:8", ["const:8498a4:8", "const:4:8"]]
+ 008498a4 ["CALL", null, ["callee:0086a654:8"]]
- 00849864 bytes 6c830094
+ 008498a4 bytes 6c830094
- 00849870 ["INT_ADD", "register:40f0:8", ["const:849870:8", "const:4:8"]]
- 00849870 ["CALL", null, ["callee:0066baa4:8"]]
+ 008498b0 ["INT_ADD", "register:40f0:8", ["const:8498b0:8", "const:4:8"]]
+ 008498b0 ["CALL", null, ["callee:0066baa4:8"]]
- 00849870 bytes 7d88f897
+ 008498b0 bytes 7d88f897
~~~


<a id="compare-3ff9647cc4b261d9bb43bbdaa4d0c71e"></a>

### [`00849888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849888.md) → [`008498c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498c8.md) FUN_008498c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006a6098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6098.md) [`006a60e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a60e8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006a60d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a60d8.md) [`006a6128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6128.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008498a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849888.md#insn-008498a0)
- 新版 `008498e0`（命令位置の公開資料なし）

~~~diff
- 008498a0 ["INT_ADD", "register:40f0:8", ["const:8498a0:8", "const:4:8"]]
- 008498a0 ["CALL", null, ["callee:006a60d8:8"]]
+ 008498e0 ["INT_ADD", "register:40f0:8", ["const:8498e0:8", "const:4:8"]]
+ 008498e0 ["CALL", null, ["callee:006a60d8:8"]]
- 008498a0 bytes fe71f997
+ 008498e0 bytes fe71f997
~~~


<a id="compare-73a75e4e7fcd8b7dacea439c15e0b3e7"></a>

### [`008498b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008498b8.md) → [`008498f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498f8.md) FUN_008498f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008498b8.md#insn-00849900) · [`00849910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008498b8.md#insn-00849910) · [`0084991c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008498b8.md#insn-0084991c)
- 新版 `00849940`（命令位置の公開資料なし） · `00849950`（命令位置の公開資料なし） · `0084995c`（命令位置の公開資料なし）

~~~diff
- 00849900 ["INT_ADD", "register:40f0:8", ["const:849900:8", "const:4:8"]]
- 00849900 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849940 ["INT_ADD", "register:40f0:8", ["const:849940:8", "const:4:8"]]
+ 00849940 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849900 bytes 6c381094
+ 00849940 bytes 5c391094
- 00849910 ["INT_ADD", "register:40f0:8", ["const:849910:8", "const:4:8"]]
- 00849910 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849950 ["INT_ADD", "register:40f0:8", ["const:849950:8", "const:4:8"]]
+ 00849950 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849910 bytes 68381094
+ 00849950 bytes 58391094
- 0084991c ["INT_ADD", "register:40f0:8", ["const:84991c:8", "const:4:8"]]
- 0084991c ["CALL", null, ["callee:005c179c:8"]]
+ 0084995c ["INT_ADD", "register:40f0:8", ["const:84995c:8", "const:4:8"]]
+ 0084995c ["CALL", null, ["callee:005c179c:8"]]
- 0084991c bytes 90dff597
+ 0084995c bytes 90dff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50cb46eb867547f32ac61b224994f0b0"></a>

### [`008499a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499a0.md) → [`008499e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008499e0.md) FUN_008499e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008499b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499a0.md#insn-008499b8)
- 新版 `008499f8`（命令位置の公開資料なし）

~~~diff
- 008499b8 ["INT_ADD", "register:40f0:8", ["const:8499b8:8", "const:4:8"]]
- 008499b8 ["CALL", null, ["callee:005c3e7c:8"]]
+ 008499f8 ["INT_ADD", "register:40f0:8", ["const:8499f8:8", "const:4:8"]]
+ 008499f8 ["CALL", null, ["callee:005c3e7c:8"]]
- 008499b8 bytes 21e9f597
+ 008499f8 bytes 21e9f597
~~~


<a id="compare-558024e4e263c2de74b0e5035b8ef368"></a>

### [`008499d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499d0.md) → [`00849a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a10.md) FUN_00849a10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008499f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008499d0.md#insn-008499f0)
- 新版 `00849a30`（命令位置の公開資料なし）

~~~diff
- 008499f0 ["INT_ADD", "register:40f0:8", ["const:8499f0:8", "const:4:8"]]
- 008499f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849a30 ["INT_ADD", "register:40f0:8", ["const:849a30:8", "const:4:8"]]
+ 00849a30 ["CALL", null, ["callee:00c57eb0:8"]]
- 008499f0 bytes 30381094
+ 00849a30 bytes 20391094
~~~


<a id="compare-cbdcce8c94a7e4c15070b58e6054a3b8"></a>

### [`00849a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md) → [`00849a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md) FUN_00849a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`0086a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a720.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md#insn-00849a20) · [`00849a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md#insn-00849a30) · [`00849a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a08.md#insn-00849a40)
- 新版 `00849a60`（命令位置の公開資料なし） · `00849a70`（命令位置の公開資料なし） · `00849a80`（命令位置の公開資料なし）

~~~diff
- 00849a20 ["INT_ADD", "register:40f0:8", ["const:849a20:8", "const:4:8"]]
- 00849a20 ["CALL", null, ["callee:005c179c:8"]]
+ 00849a60 ["INT_ADD", "register:40f0:8", ["const:849a60:8", "const:4:8"]]
+ 00849a60 ["CALL", null, ["callee:005c179c:8"]]
- 00849a20 bytes 4fdff597
+ 00849a60 bytes 4fdff597
- 00849a30 ["INT_ADD", "register:40f0:8", ["const:849a30:8", "const:4:8"]]
- 00849a30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849a70 ["INT_ADD", "register:40f0:8", ["const:849a70:8", "const:4:8"]]
+ 00849a70 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849a30 bytes 20381094
+ 00849a70 bytes 10391094
- 00849a40 ["INT_ADD", "register:40f0:8", ["const:849a40:8", "const:4:8"]]
- 00849a40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849a80 ["INT_ADD", "register:40f0:8", ["const:849a80:8", "const:4:8"]]
+ 00849a80 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849a40 bytes 1c381094
+ 00849a80 bytes 0c391094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3464639693d5c81f2e3e4107d0f2687b"></a>

### [`00849a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a64.md) → [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) FUN_00849aa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0086a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a764.md) [`0086a7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a7f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a64.md#insn-00849a80) · [`00849a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849a64.md#insn-00849a8c)
- 新版 `00849ac0`（命令位置の公開資料なし） · `00849acc`（命令位置の公開資料なし）

~~~diff
- 00849a80 ["INT_ADD", "register:40f0:8", ["const:849a80:8", "const:4:8"]]
- 00849a80 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849ac0 ["INT_ADD", "register:40f0:8", ["const:849ac0:8", "const:4:8"]]
+ 00849ac0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849a80 bytes 0c381094
+ 00849ac0 bytes fc381094
- 00849a8c ["INT_ADD", "register:40f0:8", ["const:849a8c:8", "const:4:8"]]
- 00849a8c ["CALL", null, ["callee:0086a7a4:8"]]
+ 00849acc ["INT_ADD", "register:40f0:8", ["const:849acc:8", "const:4:8"]]
+ 00849acc ["CALL", null, ["callee:0086a7a4:8"]]
- 00849a8c bytes 36830094
+ 00849acc bytes 36830094
~~~


<a id="compare-f683dbda113ed5a82d9f29de45547039"></a>

### [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) → [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) FUN_00849ae4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`0086a848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a848.md) [`0086a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a898.md) [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md#insn-00849abc) · [`00849ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md#insn-00849ac8) · [`00849ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md#insn-00849ad4)
- 新版 `00849afc`（命令位置の公開資料なし） · `00849b08`（命令位置の公開資料なし） · `00849b14`（命令位置の公開資料なし）

~~~diff
- 00849abc ["INT_ADD", "register:40f0:8", ["const:849abc:8", "const:4:8"]]
- 00849abc ["CALL", null, ["callee:0086a888:8"]]
+ 00849afc ["INT_ADD", "register:40f0:8", ["const:849afc:8", "const:4:8"]]
+ 00849afc ["CALL", null, ["callee:0086a888:8"]]
- 00849abc bytes 63830094
+ 00849afc bytes 63830094
- 00849ac8 ["INT_ADD", "register:40f0:8", ["const:849ac8:8", "const:4:8"]]
- 00849ac8 ["CALL", null, ["callee:0086bb54:8"]]
+ 00849b08 ["INT_ADD", "register:40f0:8", ["const:849b08:8", "const:4:8"]]
+ 00849b08 ["CALL", null, ["callee:0086bb54:8"]]
- 00849ac8 bytes 13880094
+ 00849b08 bytes 13880094
- 00849ad4 ["INT_ADD", "register:40f0:8", ["const:849ad4:8", "const:4:8"]]
- 00849ad4 ["CALL", null, ["callee:005c179c:8"]]
+ 00849b14 ["INT_ADD", "register:40f0:8", ["const:849b14:8", "const:4:8"]]
+ 00849b14 ["CALL", null, ["callee:005c179c:8"]]
- 00849ad4 bytes 22dff597
+ 00849b14 bytes 22dff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1edddac214170aff578c9fb057a20168"></a>

### [`00849b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b18.md) → [`00849b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md) FUN_00849b58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`0086a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a8dc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b18.md#insn-00849b30) · [`00849b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849b18.md#insn-00849b40)
- 新版 `00849b70`（命令位置の公開資料なし） · `00849b80`（命令位置の公開資料なし）

~~~diff
- 00849b30 ["INT_ADD", "register:40f0:8", ["const:849b30:8", "const:4:8"]]
- 00849b30 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00849b70 ["INT_ADD", "register:40f0:8", ["const:849b70:8", "const:4:8"]]
+ 00849b70 ["CALL", null, ["callee:005c3e7c:8"]]
- 00849b30 bytes c3e8f597
+ 00849b70 bytes c3e8f597
- 00849b40 ["INT_ADD", "register:40f0:8", ["const:849b40:8", "const:4:8"]]
- 00849b40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00849b80 ["INT_ADD", "register:40f0:8", ["const:849b80:8", "const:4:8"]]
+ 00849b80 ["CALL", null, ["callee:00c57eb0:8"]]
- 00849b40 bytes dc371094
+ 00849b80 bytes cc381094
~~~


