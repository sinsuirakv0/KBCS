# v16.0.1 → v16.0.2 · 要調査の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-6eab45131ee2aa7c7a6c9b01f5203157"></a>

### [`00763c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md) → [`00763ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md) FUN_00763ce8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 5件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0066d094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d094.md) [`00b357e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) · 呼出先 5件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0066d0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d0d4.md) [`00b35884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35884.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00763cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md#insn-00763cb4) · [`00763cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md#insn-00763cc8) · [`00763cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763c90.md#insn-00763cd8)
- 新版 [`00763d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d0c) · [`00763d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d20) · [`00763d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d30)

~~~diff
- 00763cb4 ["INT_ADD", "register:40f0:8", ["const:763cb4:8", "const:4:8"]]
- 00763cb4 ["CALL", null, ["callee:0066d0d4:8"]]
+ 00763d0c ["INT_ADD", "register:40f0:8", ["const:763d0c:8", "const:4:8"]]
+ 00763d0c ["CALL", null, ["callee:0066d0d4:8"]]
- 00763cb4 bytes f824fc97
+ 00763d0c bytes f224fc97
- 00763cc8 ["INT_ADD", "register:40f0:8", ["const:763cc8:8", "const:4:8"]]
- 00763cc8 ["CALL", null, ["callee:00447f34:8"]]
+ 00763d20 ["INT_ADD", "register:40f0:8", ["const:763d20:8", "const:4:8"]]
+ 00763d20 ["CALL", null, ["callee:00447f34:8"]]
- 00763cc8 bytes 8b90f397
+ 00763d20 bytes 8590f397
- 00763cd8 ["INT_ADD", "register:40f0:8", ["const:763cd8:8", "const:4:8"]]
- 00763cd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00763d30 ["INT_ADD", "register:40f0:8", ["const:763d30:8", "const:4:8"]]
+ 00763d30 ["CALL", null, ["callee:00c57f80:8"]]
- 00763cd8 bytes 76d01394
+ 00763d30 bytes 94d01394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eaa353d969516beb693934424534b24"></a>

### [`00769720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769720.md) → [`00769778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md) FUN_00769778

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00769774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769720.md#insn-00769774)
- 新版 [`007697cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769778.md#insn-007697cc)

~~~diff
- 00769774 ["INT_ADD", "register:40f0:8", ["const:769774:8", "const:4:8"]]
- 00769774 ["CALL", null, ["callee:00c57f80:8"]]
+ 007697cc ["INT_ADD", "register:40f0:8", ["const:7697cc:8", "const:4:8"]]
+ 007697cc ["CALL", null, ["callee:00c57f80:8"]]
- 00769774 bytes cfb91394
+ 007697cc bytes edb91394
~~~


<a id="compare-23cd516475d64e794cc38347670852bd"></a>

### [`007737ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/007737ac.md) → [`00773804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md) FUN_00773804

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00773814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/007737ac.md#insn-00773814) · [`0077386c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/007737ac.md#insn-0077386c)
- 新版 [`0077386c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md#insn-0077386c) · [`007738c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/00773804.md#insn-007738c4)

~~~diff
- 00773814 ["INT_ADD", "register:40f0:8", ["const:773814:8", "const:4:8"]]
- 00773814 ["CALL", null, ["callee:00c57f60:8"]]
+ 0077386c ["INT_ADD", "register:40f0:8", ["const:77386c:8", "const:4:8"]]
+ 0077386c ["CALL", null, ["callee:00c57f60:8"]]
- 00773814 bytes 9f911394
+ 0077386c bytes bd911394
- 0077386c ["INT_ADD", "register:40f0:8", ["const:77386c:8", "const:4:8"]]
- 0077386c ["CALL", null, ["callee:0043bbe4:8"]]
+ 007738c4 ["INT_ADD", "register:40f0:8", ["const:7738c4:8", "const:4:8"]]
+ 007738c4 ["CALL", null, ["callee:0043bbe4:8"]]
- 0077386c bytes ce20f397
+ 007738c4 bytes c820f397
~~~


<a id="compare-2112d035928fab6d8d921687675f5a60"></a>

### [`0077b258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b258.md) → [`0077b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md) FUN_0077b2b0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077b290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b258.md#insn-0077b290) · [`0077b29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b258.md#insn-0077b29c)
- 新版 [`0077b2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md#insn-0077b2e8) · [`0077b2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md#insn-0077b2f4)

~~~diff
- 0077b290 ["INT_ADD", "register:40f0:8", ["const:77b290:8", "const:4:8"]]
- 0077b290 ["CALL", null, ["callee:005c17dc:8"]]
+ 0077b2e8 ["INT_ADD", "register:40f0:8", ["const:77b2e8:8", "const:4:8"]]
+ 0077b2e8 ["CALL", null, ["callee:005c17dc:8"]]
- 0077b290 bytes 4319f997
+ 0077b2e8 bytes 3d19f997
- 0077b29c ["INT_ADD", "register:40f0:8", ["const:77b29c:8", "const:4:8"]]
- 0077b29c ["CALL", null, ["callee:005c17dc:8"]]
+ 0077b2f4 ["INT_ADD", "register:40f0:8", ["const:77b2f4:8", "const:4:8"]]
+ 0077b2f4 ["CALL", null, ["callee:005c17dc:8"]]
- 0077b29c bytes 4019f997
+ 0077b2f4 bytes 3a19f997
~~~


<a id="compare-65cbc63afaf396ef906bf96fb3a1c9ad"></a>

### [`0077c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c034.md) → [`0077c08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c08c.md) FUN_0077c08c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0077bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077bbc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0077bc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c034.md#insn-0077c044)
- 新版 [`0077c09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c08c.md#insn-0077c09c)

~~~diff
- 0077c044 ["INT_ADD", "register:40f0:8", ["const:77c044:8", "const:4:8"]]
- 0077c044 ["CALL", null, ["callee:0077bc18:8"]]
+ 0077c09c ["INT_ADD", "register:40f0:8", ["const:77c09c:8", "const:4:8"]]
+ 0077c09c ["CALL", null, ["callee:0077bc18:8"]]
- 0077c044 bytes dffeff97
+ 0077c09c bytes dffeff97
~~~


<a id="compare-46ccd9c4b7b2c2f395298f5747677b4d"></a>

### [`0077c55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md) → [`0077c5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md) FUN_0077c5b4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0077c190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) · 呼出先 5件 [`00726260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0077c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md) · 呼出先 5件 [`007262b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007262b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md#insn-0077c5b0) · [`0077c614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md#insn-0077c614) · [`0077c63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md#insn-0077c63c)
- 新版 [`0077c608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c608) · [`0077c66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c66c) · [`0077c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c694)

~~~diff
- 0077c5b0 ["INT_ADD", "register:40f0:8", ["const:77c5b0:8", "const:4:8"]]
- 0077c5b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0077c608 ["INT_ADD", "register:40f0:8", ["const:77c608:8", "const:4:8"]]
+ 0077c608 ["CALL", null, ["callee:00c57f80:8"]]
- 0077c5b0 bytes 406e1394
+ 0077c608 bytes 5e6e1394
- 0077c614 ["INT_ADD", "register:40f0:8", ["const:77c614:8", "const:4:8"]]
- 0077c614 ["CALL", null, ["callee:00c57f60:8"]]
+ 0077c66c ["INT_ADD", "register:40f0:8", ["const:77c66c:8", "const:4:8"]]
+ 0077c66c ["CALL", null, ["callee:00c57f60:8"]]
- 0077c614 bytes 1f6e1394
+ 0077c66c bytes 3d6e1394
- 0077c63c ["INT_ADD", "register:40f0:8", ["const:77c63c:8", "const:4:8"]]
- 0077c63c ["CALL", null, ["callee:00c580d0:8"]]
+ 0077c694 ["INT_ADD", "register:40f0:8", ["const:77c694:8", "const:4:8"]]
+ 0077c694 ["CALL", null, ["callee:00c580d0:8"]]
- 0077c63c bytes 716e1394
+ 0077c694 bytes 8f6e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00a5bbca53c2ba5a141869b12c9799ab"></a>

### [`0077c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c6c0.md) → [`0077c718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md) FUN_0077c718

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) · 呼出先 5件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) · 呼出先 5件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c6c0.md#insn-0077c704) · [`0077c73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c6c0.md#insn-0077c73c) · [`0077c764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c6c0.md#insn-0077c764)
- 新版 [`0077c75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c75c) · [`0077c794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c794) · [`0077c7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c7bc)

~~~diff
- 0077c704 ["INT_ADD", "register:40f0:8", ["const:77c704:8", "const:4:8"]]
- 0077c704 ["CALL", null, ["callee:00c57f80:8"]]
+ 0077c75c ["INT_ADD", "register:40f0:8", ["const:77c75c:8", "const:4:8"]]
+ 0077c75c ["CALL", null, ["callee:00c57f80:8"]]
- 0077c704 bytes eb6d1394
+ 0077c75c bytes 096e1394
- 0077c73c ["INT_ADD", "register:40f0:8", ["const:77c73c:8", "const:4:8"]]
- 0077c73c ["CALL", null, ["callee:00c57f60:8"]]
+ 0077c794 ["INT_ADD", "register:40f0:8", ["const:77c794:8", "const:4:8"]]
+ 0077c794 ["CALL", null, ["callee:00c57f60:8"]]
- 0077c73c bytes d56d1394
+ 0077c794 bytes f36d1394
- 0077c764 ["INT_ADD", "register:40f0:8", ["const:77c764:8", "const:4:8"]]
- 0077c764 ["CALL", null, ["callee:00c580d0:8"]]
+ 0077c7bc ["INT_ADD", "register:40f0:8", ["const:77c7bc:8", "const:4:8"]]
+ 0077c7bc ["CALL", null, ["callee:00c580d0:8"]]
- 0077c764 bytes 276e1394
+ 0077c7bc bytes 456e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d601f7ee5f2780a3f898d300ce92e0"></a>

### [`0077c860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c860.md) → [`0077c8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md) FUN_0077c8b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b924.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0075b97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b97c.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c860.md#insn-0077c8c4) · [`0077c8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c860.md#insn-0077c8d4) · [`0077c8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c860.md#insn-0077c8e4)
- 新版 [`0077c91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c91c) · [`0077c92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c92c) · [`0077c93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c93c)

~~~diff
- 0077c8c4 ["INT_ADD", "register:40f0:8", ["const:77c8c4:8", "const:4:8"]]
- 0077c8c4 ["CALL", null, ["callee:00494650:8"]]
+ 0077c91c ["INT_ADD", "register:40f0:8", ["const:77c91c:8", "const:4:8"]]
+ 0077c91c ["CALL", null, ["callee:00494650:8"]]
- 0077c8c4 bytes 535ff497
+ 0077c91c bytes 4d5ff497
- 0077c8d4 ["INT_ADD", "register:40f0:8", ["const:77c8d4:8", "const:4:8"]]
- 0077c8d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0077c92c ["INT_ADD", "register:40f0:8", ["const:77c92c:8", "const:4:8"]]
+ 0077c92c ["CALL", null, ["callee:00c57f80:8"]]
- 0077c8d4 bytes 776d1394
+ 0077c92c bytes 956d1394
- 0077c8e4 ["INT_ADD", "register:40f0:8", ["const:77c8e4:8", "const:4:8"]]
- 0077c8e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0077c93c ["INT_ADD", "register:40f0:8", ["const:77c93c:8", "const:4:8"]]
+ 0077c93c ["CALL", null, ["callee:00c57f80:8"]]
- 0077c8e4 bytes 736d1394
+ 0077c93c bytes 916d1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c09c100b3f0fd7bb73327987cb5c37f"></a>

### [`00782b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b20.md) → [`00782b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md) FUN_00782b78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00782b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b20.md#insn-00782b3c) · [`00782b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b20.md#insn-00782b5c)
- 新版 [`00782b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md#insn-00782b94) · [`00782bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md#insn-00782bb4)

~~~diff
- 00782b3c ["INT_ADD", "register:40f0:8", ["const:782b3c:8", "const:4:8"]]
- 00782b3c ["CALL", null, ["callee:00c53da0:8"]]
+ 00782b94 ["INT_ADD", "register:40f0:8", ["const:782b94:8", "const:4:8"]]
+ 00782b94 ["CALL", null, ["callee:00c53da0:8"]]
- 00782b3c bytes 71441394
+ 00782b94 bytes 83441394
- 00782b5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00782b5c ["INT_ADD", "register:40f0:8", ["const:782b5c:8", "const:4:8"]]
- 00782b5c ["CALLIND", null, ["register:0:8"]]
+ 00782bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00782bb4 ["INT_ADD", "register:40f0:8", ["const:782bb4:8", "const:4:8"]]
+ 00782bb4 ["CALLIND", null, ["register:0:8"]]
- 00782b5c bytes 00013fd6
+ 00782bb4 bytes 00013fd6
~~~


<a id="compare-2f26765cf84a7a75480f01f739ab8f27"></a>

### [`007839b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007839b4.md) → [`00783a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783a0c.md) FUN_00783a0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007839d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007839b4.md#insn-007839d4)
- 新版 [`00783a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783a0c.md#insn-00783a2c)

~~~diff
- 007839d4 ["INT_ADD", "register:40f0:8", ["const:7839d4:8", "const:4:8"]]
- 007839d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00783a2c ["INT_ADD", "register:40f0:8", ["const:783a2c:8", "const:4:8"]]
+ 00783a2c ["CALL", null, ["callee:00c57f80:8"]]
- 007839d4 bytes 37511394
+ 00783a2c bytes 55511394
~~~


<a id="compare-0e593ee45da276931a22f463449f1e71"></a>

### [`0078bc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bc3c.md) → [`0078bc94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078b/0078bc94.md) FUN_0078bc94

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006d5fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d5/006d5fc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006d6020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6020.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078bc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bc3c.md#insn-0078bc88) · [`0078bcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bc3c.md#insn-0078bcb8) · [`0078bccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bc3c.md#insn-0078bccc)
- 新版 [`0078bce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078b/0078bc94.md#insn-0078bce0) · [`0078bd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078b/0078bc94.md#insn-0078bd10) · [`0078bd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078b/0078bc94.md#insn-0078bd24)

~~~diff
- 0078bc88 ["INT_ADD", "register:40f0:8", ["const:78bc88:8", "const:4:8"]]
- 0078bc88 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0078bce0 ["INT_ADD", "register:40f0:8", ["const:78bce0:8", "const:4:8"]]
+ 0078bce0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0078bc88 bytes c7bff297
+ 0078bce0 bytes c1bff297
- 0078bcb8 ["INT_ADD", "register:40f0:8", ["const:78bcb8:8", "const:4:8"]]
- 0078bcb8 ["CALL", null, ["callee:006d6020:8"]]
+ 0078bd10 ["INT_ADD", "register:40f0:8", ["const:78bd10:8", "const:4:8"]]
+ 0078bd10 ["CALL", null, ["callee:006d6020:8"]]
- 0078bcb8 bytes c428fd97
+ 0078bd10 bytes c428fd97
- 0078bccc ["INT_ADD", "register:40f0:8", ["const:78bccc:8", "const:4:8"]]
- 0078bccc ["CALL", null, ["callee:00c57f60:8"]]
+ 0078bd24 ["INT_ADD", "register:40f0:8", ["const:78bd24:8", "const:4:8"]]
+ 0078bd24 ["CALL", null, ["callee:00c57f60:8"]]
- 0078bccc bytes 71301394
+ 0078bd24 bytes 8f301394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d83b1871c1bdd44d9de741dbef6fc1"></a>

### [`0078db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md) → [`0078dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md) FUN_0078dbb4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) [`0078de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078de54.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) [`0078deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078deac.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078db7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md#insn-0078db7c) · [`0078db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md#insn-0078db90) · [`0078db98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md#insn-0078db98)
- 新版 [`0078dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbd4) · [`0078dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbe8) · [`0078dbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbf0)

~~~diff
- 0078db7c ["INT_ADD", "register:40f0:8", ["const:78db7c:8", "const:4:8"]]
- 0078db7c ["CALL", null, ["callee:00c53da0:8"]]
+ 0078dbd4 ["INT_ADD", "register:40f0:8", ["const:78dbd4:8", "const:4:8"]]
+ 0078dbd4 ["CALL", null, ["callee:00c53da0:8"]]
- 0078db7c bytes 61181394
+ 0078dbd4 bytes 73181394
- 0078db90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078db90 ["INT_ADD", "register:40f0:8", ["const:78db90:8", "const:4:8"]]
- 0078db90 ["CALLIND", null, ["register:0:8"]]
+ 0078dbe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0078dbe8 ["INT_ADD", "register:40f0:8", ["const:78dbe8:8", "const:4:8"]]
+ 0078dbe8 ["CALLIND", null, ["register:0:8"]]
- 0078db90 bytes 00013fd6
+ 0078dbe8 bytes 00013fd6
- 0078db98 ["INT_ADD", "register:40f0:8", ["const:78db98:8", "const:4:8"]]
- 0078db98 ["CALL", null, ["callee:00c57f50:8"]]
+ 0078dbf0 ["INT_ADD", "register:40f0:8", ["const:78dbf0:8", "const:4:8"]]
+ 0078dbf0 ["CALL", null, ["callee:00c57f50:8"]]
- 0078db98 bytes ba281394
+ 0078dbf0 bytes d8281394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e473c28f812f0995a135a8a9df45dde4"></a>

### [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) → [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) FUN_0078dd04

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) [`0078de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078de54.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008468cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008468cc.md) [`00846fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846fa4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 10件 [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) [`0078deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078deac.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00846924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md) [`00846ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078dccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md#insn-0078dccc) · [`0078dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md#insn-0078dce0) · [`0078dce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md#insn-0078dce8)
- 新版 [`0078dd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md#insn-0078dd24) · [`0078dd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md#insn-0078dd38) · [`0078dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md#insn-0078dd40)

~~~diff
- 0078dccc ["INT_ADD", "register:40f0:8", ["const:78dccc:8", "const:4:8"]]
- 0078dccc ["CALL", null, ["callee:00c53da0:8"]]
+ 0078dd24 ["INT_ADD", "register:40f0:8", ["const:78dd24:8", "const:4:8"]]
+ 0078dd24 ["CALL", null, ["callee:00c53da0:8"]]
- 0078dccc bytes 0d181394
+ 0078dd24 bytes 1f181394
- 0078dce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078dce0 ["INT_ADD", "register:40f0:8", ["const:78dce0:8", "const:4:8"]]
- 0078dce0 ["CALLIND", null, ["register:0:8"]]
+ 0078dd38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0078dd38 ["INT_ADD", "register:40f0:8", ["const:78dd38:8", "const:4:8"]]
+ 0078dd38 ["CALLIND", null, ["register:0:8"]]
- 0078dce0 bytes 00013fd6
+ 0078dd38 bytes 00013fd6
- 0078dce8 ["INT_ADD", "register:40f0:8", ["const:78dce8:8", "const:4:8"]]
- 0078dce8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0078dd40 ["INT_ADD", "register:40f0:8", ["const:78dd40:8", "const:4:8"]]
+ 0078dd40 ["CALL", null, ["callee:00c57f50:8"]]
- 0078dce8 bytes 66281394
+ 0078dd40 bytes 84281394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c4ad8d0fc77ed0d1516d12df92b77f"></a>

### [`0078e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e4a0.md) → [`0078e4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4f8.md) FUN_0078e4f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078e4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e4a0.md#insn-0078e4bc) · [`0078e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e4a0.md#insn-0078e4c4) · [`0078e4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e4a0.md#insn-0078e4d0)
- 新版 [`0078e514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4f8.md#insn-0078e514) · [`0078e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4f8.md#insn-0078e51c) · [`0078e528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4f8.md#insn-0078e528)

~~~diff
- 0078e4bc ["INT_ADD", "register:40f0:8", ["const:78e4bc:8", "const:4:8"]]
- 0078e4bc ["CALL", null, ["callee:008b7a20:8"]]
+ 0078e514 ["INT_ADD", "register:40f0:8", ["const:78e514:8", "const:4:8"]]
+ 0078e514 ["CALL", null, ["callee:008b7a20:8"]]
- 0078e4bc bytes 43a50494
+ 0078e514 bytes 43a50494
- 0078e4c4 ["INT_ADD", "register:40f0:8", ["const:78e4c4:8", "const:4:8"]]
- 0078e4c4 ["CALL", null, ["callee:008b6f70:8"]]
+ 0078e51c ["INT_ADD", "register:40f0:8", ["const:78e51c:8", "const:4:8"]]
+ 0078e51c ["CALL", null, ["callee:008b6f70:8"]]
- 0078e4c4 bytes 95a20494
+ 0078e51c bytes 95a20494
- 0078e4d0 ["INT_ADD", "register:40f0:8", ["const:78e4d0:8", "const:4:8"]]
- 0078e4d0 ["CALL", null, ["callee:008b7a20:8"]]
+ 0078e528 ["INT_ADD", "register:40f0:8", ["const:78e528:8", "const:4:8"]]
+ 0078e528 ["CALL", null, ["callee:008b7a20:8"]]
- 0078e4d0 bytes 3ea50494
+ 0078e528 bytes 3ea50494
~~~


<a id="compare-258477aa62d2dee301cae24a30850713"></a>

### [`0078e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e5e8.md) → [`0078e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e640.md) FUN_0078e640

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e5e8.md#insn-0078e624)
- 新版 [`0078e67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e640.md#insn-0078e67c)

~~~diff
- 0078e624 ["INT_ADD", "register:40f0:8", ["const:78e624:8", "const:4:8"]]
- 0078e624 ["CALL", null, ["callee:0049f430:8"]]
+ 0078e67c ["INT_ADD", "register:40f0:8", ["const:78e67c:8", "const:4:8"]]
+ 0078e67c ["CALL", null, ["callee:0049f430:8"]]
- 0078e624 bytes 7343f497
+ 0078e67c bytes 6d43f497
~~~


<a id="compare-3fcaa600add4e9374e27aed175eee0a3"></a>

### [`0078f1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f1a4.md) → [`0078f1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md) FUN_0078f1fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847c24.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 5件 [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847c7c.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 5件 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f1a4.md#insn-0078f1c4) · [`0078f1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f1a4.md#insn-0078f1d0) · [`0078f1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f1a4.md#insn-0078f1dc)
- 新版 [`0078f21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f21c) · [`0078f228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f228) · [`0078f234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f234)

~~~diff
- 0078f1c4 ["INT_ADD", "register:40f0:8", ["const:78f1c4:8", "const:4:8"]]
- 0078f1c4 ["CALL", null, ["callee:00676aa0:8"]]
+ 0078f21c ["INT_ADD", "register:40f0:8", ["const:78f21c:8", "const:4:8"]]
+ 0078f21c ["CALL", null, ["callee:00676aa0:8"]]
- 0078f1c4 bytes 279efb97
+ 0078f21c bytes 219efb97
- 0078f1d0 ["INT_ADD", "register:40f0:8", ["const:78f1d0:8", "const:4:8"]]
- 0078f1d0 ["CALL", null, ["callee:00676aa0:8"]]
+ 0078f228 ["INT_ADD", "register:40f0:8", ["const:78f228:8", "const:4:8"]]
+ 0078f228 ["CALL", null, ["callee:00676aa0:8"]]
- 0078f1d0 bytes 249efb97
+ 0078f228 bytes 1e9efb97
- 0078f1dc ["INT_ADD", "register:40f0:8", ["const:78f1dc:8", "const:4:8"]]
- 0078f1dc ["CALL", null, ["callee:005c1c30:8"]]
+ 0078f234 ["INT_ADD", "register:40f0:8", ["const:78f234:8", "const:4:8"]]
+ 0078f234 ["CALL", null, ["callee:005c1c30:8"]]
- 0078f1dc bytes 85caf897
+ 0078f234 bytes 7fcaf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8c60daaba856d09587e7ba34d837a9"></a>

### [`0078f480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f480.md) → [`0078f4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md) FUN_0078f4d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f480.md#insn-0078f4a4) · [`0078f4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f480.md#insn-0078f4e0) · [`0078f4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f480.md#insn-0078f4ec)
- 新版 [`0078f4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f4fc) · [`0078f538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f538) · [`0078f544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f544)

~~~diff
- 0078f4a4 ["INT_ADD", "register:40f0:8", ["const:78f4a4:8", "const:4:8"]]
- 0078f4a4 ["CALL", null, ["callee:00480bd0:8"]]
+ 0078f4fc ["INT_ADD", "register:40f0:8", ["const:78f4fc:8", "const:4:8"]]
+ 0078f4fc ["CALL", null, ["callee:00480bd0:8"]]
- 0078f4a4 bytes bbc5f397
+ 0078f4fc bytes b5c5f397
- 0078f4e0 ["INT_ADD", "register:40f0:8", ["const:78f4e0:8", "const:4:8"]]
- 0078f4e0 ["CALL", null, ["callee:00480bd0:8"]]
+ 0078f538 ["INT_ADD", "register:40f0:8", ["const:78f538:8", "const:4:8"]]
+ 0078f538 ["CALL", null, ["callee:00480bd0:8"]]
- 0078f4e0 bytes acc5f397
+ 0078f538 bytes a6c5f397
- 0078f4ec ["INT_ADD", "register:40f0:8", ["const:78f4ec:8", "const:4:8"]]
- 0078f4ec ["CALL", null, ["callee:00480d88:8"]]
+ 0078f544 ["INT_ADD", "register:40f0:8", ["const:78f544:8", "const:4:8"]]
+ 0078f544 ["CALL", null, ["callee:00480d88:8"]]
- 0078f4ec bytes 17c6f397
+ 0078f544 bytes 11c6f397
~~~


<a id="compare-dcfd80ae7a9909366393cb92e409c8d8"></a>

### [`0078f520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f520.md) → [`0078f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md) FUN_0078f578

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f520.md#insn-0078f558) · [`0078f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f520.md#insn-0078f568) · [`0078f588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f520.md#insn-0078f588)
- 新版 [`0078f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f5b0) · [`0078f5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f5c0) · [`0078f5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f5e0)

~~~diff
- 0078f558 ["INT_ADD", "register:40f0:8", ["const:78f558:8", "const:4:8"]]
- 0078f558 ["CALL", null, ["callee:00676aa0:8"]]
+ 0078f5b0 ["INT_ADD", "register:40f0:8", ["const:78f5b0:8", "const:4:8"]]
+ 0078f5b0 ["CALL", null, ["callee:00676aa0:8"]]
- 0078f558 bytes 429dfb97
+ 0078f5b0 bytes 3c9dfb97
- 0078f568 ["INT_ADD", "register:40f0:8", ["const:78f568:8", "const:4:8"]]
- 0078f568 ["CALL", null, ["callee:004801b8:8"]]
+ 0078f5c0 ["INT_ADD", "register:40f0:8", ["const:78f5c0:8", "const:4:8"]]
+ 0078f5c0 ["CALL", null, ["callee:004801b8:8"]]
- 0078f568 bytes 04c3f397
+ 0078f5c0 bytes fec2f397
- 0078f588 ["INT_ADD", "register:40f0:8", ["const:78f588:8", "const:4:8"]]
- 0078f588 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0078f5e0 ["INT_ADD", "register:40f0:8", ["const:78f5e0:8", "const:4:8"]]
+ 0078f5e0 ["CALL", null, ["callee:0043bbe4:8"]]
- 0078f588 bytes 87b1f297
+ 0078f5e0 bytes 81b1f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e7f45bb36f7b3877eb573d8aae0c47f"></a>

### [`0078f668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f668.md) → [`0078f6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md) FUN_0078f6c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f668.md#insn-0078f690) · [`0078f6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f668.md#insn-0078f6d0) · [`0078f6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f668.md#insn-0078f6dc)
- 新版 [`0078f6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md#insn-0078f6e8) · [`0078f728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md#insn-0078f728) · [`0078f734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md#insn-0078f734)

~~~diff
- 0078f690 ["INT_ADD", "register:40f0:8", ["const:78f690:8", "const:4:8"]]
- 0078f690 ["CALL", null, ["callee:00480b78:8"]]
+ 0078f6e8 ["INT_ADD", "register:40f0:8", ["const:78f6e8:8", "const:4:8"]]
+ 0078f6e8 ["CALL", null, ["callee:00480b78:8"]]
- 0078f690 bytes 2ac5f397
+ 0078f6e8 bytes 24c5f397
- 0078f6d0 ["INT_ADD", "register:40f0:8", ["const:78f6d0:8", "const:4:8"]]
- 0078f6d0 ["CALL", null, ["callee:00480c28:8"]]
+ 0078f728 ["INT_ADD", "register:40f0:8", ["const:78f728:8", "const:4:8"]]
+ 0078f728 ["CALL", null, ["callee:00480c28:8"]]
- 0078f6d0 bytes 46c5f397
+ 0078f728 bytes 40c5f397
- 0078f6dc ["INT_ADD", "register:40f0:8", ["const:78f6dc:8", "const:4:8"]]
- 0078f6dc ["CALL", null, ["callee:004810d8:8"]]
+ 0078f734 ["INT_ADD", "register:40f0:8", ["const:78f734:8", "const:4:8"]]
+ 0078f734 ["CALL", null, ["callee:004810d8:8"]]
- 0078f6dc bytes 6fc6f397
+ 0078f734 bytes 69c6f397
~~~


<a id="compare-d422e84e0bb79ab445bfe2d46debcbc5"></a>

### [`0078f710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f710.md) → [`0078f768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md) FUN_0078f768

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f710.md#insn-0078f748) · [`0078f758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f710.md#insn-0078f758) · [`0078f774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f710.md#insn-0078f774)
- 新版 [`0078f7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f7a0) · [`0078f7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f7b0) · [`0078f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f7cc)

~~~diff
- 0078f748 ["INT_ADD", "register:40f0:8", ["const:78f748:8", "const:4:8"]]
- 0078f748 ["CALL", null, ["callee:005c1c30:8"]]
+ 0078f7a0 ["INT_ADD", "register:40f0:8", ["const:78f7a0:8", "const:4:8"]]
+ 0078f7a0 ["CALL", null, ["callee:005c1c30:8"]]
- 0078f748 bytes 2ac9f897
+ 0078f7a0 bytes 24c9f897
- 0078f758 ["INT_ADD", "register:40f0:8", ["const:78f758:8", "const:4:8"]]
- 0078f758 ["CALL", null, ["callee:00480158:8"]]
+ 0078f7b0 ["INT_ADD", "register:40f0:8", ["const:78f7b0:8", "const:4:8"]]
+ 0078f7b0 ["CALL", null, ["callee:00480158:8"]]
- 0078f758 bytes 70c2f397
+ 0078f7b0 bytes 6ac2f397
- 0078f774 ["INT_ADD", "register:40f0:8", ["const:78f774:8", "const:4:8"]]
- 0078f774 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0078f7cc ["INT_ADD", "register:40f0:8", ["const:78f7cc:8", "const:4:8"]]
+ 0078f7cc ["CALL", null, ["callee:0043bbe4:8"]]
- 0078f774 bytes 0cb1f297
+ 0078f7cc bytes 06b1f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57685e803eb570085ef6be4a10b67871"></a>

### [`0078f850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f850.md) → [`0078f8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md) FUN_0078f8a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f850.md#insn-0078f878) · [`0078f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f850.md#insn-0078f894) · [`0078f8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f850.md#insn-0078f8d4)
- 新版 [`0078f8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f8d0) · [`0078f8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f8ec) · [`0078f92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f92c)

~~~diff
- 0078f878 ["INT_ADD", "register:40f0:8", ["const:78f878:8", "const:4:8"]]
- 0078f878 ["CALL", null, ["callee:00480e68:8"]]
+ 0078f8d0 ["INT_ADD", "register:40f0:8", ["const:78f8d0:8", "const:4:8"]]
+ 0078f8d0 ["CALL", null, ["callee:00480e68:8"]]
- 0078f878 bytes 6cc5f397
+ 0078f8d0 bytes 66c5f397
- 0078f894 ["INT_ADD", "register:40f0:8", ["const:78f894:8", "const:4:8"]]
- 0078f894 ["CALL", null, ["callee:00480e68:8"]]
+ 0078f8ec ["INT_ADD", "register:40f0:8", ["const:78f8ec:8", "const:4:8"]]
+ 0078f8ec ["CALL", null, ["callee:00480e68:8"]]
- 0078f894 bytes 65c5f397
+ 0078f8ec bytes 5fc5f397
- 0078f8d4 ["INT_ADD", "register:40f0:8", ["const:78f8d4:8", "const:4:8"]]
- 0078f8d4 ["CALL", null, ["callee:00480e68:8"]]
+ 0078f92c ["INT_ADD", "register:40f0:8", ["const:78f92c:8", "const:4:8"]]
+ 0078f92c ["CALL", null, ["callee:00480e68:8"]]
- 0078f8d4 bytes 55c5f397
+ 0078f92c bytes 4fc5f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67538ca88d68155cf23c0bf7259e2744"></a>

### [`0078f96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f96c.md) → [`0078f9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md) FUN_0078f9c4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078f9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f96c.md#insn-0078f9a4) · [`0078f9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f96c.md#insn-0078f9b4) · [`0078f9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078f96c.md#insn-0078f9d0)
- 新版 [`0078f9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078f9fc) · [`0078fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078fa0c) · [`0078fa28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078fa28)

~~~diff
- 0078f9a4 ["INT_ADD", "register:40f0:8", ["const:78f9a4:8", "const:4:8"]]
- 0078f9a4 ["CALL", null, ["callee:005c1c30:8"]]
+ 0078f9fc ["INT_ADD", "register:40f0:8", ["const:78f9fc:8", "const:4:8"]]
+ 0078f9fc ["CALL", null, ["callee:005c1c30:8"]]
- 0078f9a4 bytes 93c8f897
+ 0078f9fc bytes 8dc8f897
- 0078f9b4 ["INT_ADD", "register:40f0:8", ["const:78f9b4:8", "const:4:8"]]
- 0078f9b4 ["CALL", null, ["callee:00480430:8"]]
+ 0078fa0c ["INT_ADD", "register:40f0:8", ["const:78fa0c:8", "const:4:8"]]
+ 0078fa0c ["CALL", null, ["callee:00480430:8"]]
- 0078f9b4 bytes 8fc2f397
+ 0078fa0c bytes 89c2f397
- 0078f9d0 ["INT_ADD", "register:40f0:8", ["const:78f9d0:8", "const:4:8"]]
- 0078f9d0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0078fa28 ["INT_ADD", "register:40f0:8", ["const:78fa28:8", "const:4:8"]]
+ 0078fa28 ["CALL", null, ["callee:0043bbe4:8"]]
- 0078f9d0 bytes 75b0f297
+ 0078fa28 bytes 6fb0f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f31ca8497df1a79859dfd6bfcb3b03c9"></a>

### [`0078fbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fbac.md) → [`0078fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md) FUN_0078fc04

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 3件 [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0078fc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc74.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 3件 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078fbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fbac.md#insn-0078fbcc) · [`0078fbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fbac.md#insn-0078fbe8) · [`0078fc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fbac.md#insn-0078fc04)
- 新版 [`0078fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc24) · [`0078fc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc40) · [`0078fc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc5c)

~~~diff
- 0078fbcc ["INT_ADD", "register:40f0:8", ["const:78fbcc:8", "const:4:8"]]
- 0078fbcc ["CALL", null, ["callee:005c1c30:8"]]
+ 0078fc24 ["INT_ADD", "register:40f0:8", ["const:78fc24:8", "const:4:8"]]
+ 0078fc24 ["CALL", null, ["callee:005c1c30:8"]]
- 0078fbcc bytes 09c8f897
+ 0078fc24 bytes 03c8f897
- 0078fbe8 ["INT_ADD", "register:40f0:8", ["const:78fbe8:8", "const:4:8"]]
- 0078fbe8 ["CALL", null, ["callee:005c1c30:8"]]
+ 0078fc40 ["INT_ADD", "register:40f0:8", ["const:78fc40:8", "const:4:8"]]
+ 0078fc40 ["CALL", null, ["callee:005c1c30:8"]]
- 0078fbe8 bytes 02c8f897
+ 0078fc40 bytes fcc7f897
- 0078fc04 ["INT_ADD", "register:40f0:8", ["const:78fc04:8", "const:4:8"]]
- 0078fc04 ["CALL", null, ["callee:00676aa0:8"]]
+ 0078fc5c ["INT_ADD", "register:40f0:8", ["const:78fc5c:8", "const:4:8"]]
+ 0078fc5c ["CALL", null, ["callee:00676aa0:8"]]
- 0078fc04 bytes 979bfb97
+ 0078fc5c bytes 919bfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-849b9ec27380a4623212026579cbfef8"></a>

### [`0078fc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc44.md) → [`0078fc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc9c.md) FUN_0078fc9c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 1件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)
- 新版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 1件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078fc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc44.md#insn-0078fc5c)
- 新版 [`0078fcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc9c.md#insn-0078fcb4)

~~~diff
- 0078fc5c ["INT_ADD", "register:40f0:8", ["const:78fc5c:8", "const:4:8"]]
- 0078fc5c ["CALL", null, ["callee:00676aa0:8"]]
+ 0078fcb4 ["INT_ADD", "register:40f0:8", ["const:78fcb4:8", "const:4:8"]]
+ 0078fcb4 ["CALL", null, ["callee:00676aa0:8"]]
- 0078fc5c bytes 819bfb97
+ 0078fcb4 bytes 7b9bfb97
~~~


<a id="compare-f1d28efdc0420a46c2a4edbbf074d9d5"></a>

### [`0078fc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc74.md) → [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md) FUN_0078fccc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078fbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fbac.md) [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0078fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md) [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc74.md#insn-0078fd0c) · [`0078fd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc74.md#insn-0078fd54) · [`0078fd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fc74.md#insn-0078fd68)
- 新版 [`0078fd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fd64) · [`0078fdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fdac) · [`0078fdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fdc0)

~~~diff
- 0078fd0c ["INT_ADD", "register:40f0:8", ["const:78fd0c:8", "const:4:8"]]
- 0078fd0c ["CALL", null, ["callee:00c57f80:8"]]
+ 0078fd64 ["INT_ADD", "register:40f0:8", ["const:78fd64:8", "const:4:8"]]
+ 0078fd64 ["CALL", null, ["callee:00c57f80:8"]]
- 0078fd0c bytes 69201394
+ 0078fd64 bytes 87201394
- 0078fd54 ["INT_ADD", "register:40f0:8", ["const:78fd54:8", "const:4:8"]]
- 0078fd54 ["CALL", null, ["callee:00c53da0:8"]]
+ 0078fdac ["INT_ADD", "register:40f0:8", ["const:78fdac:8", "const:4:8"]]
+ 0078fdac ["CALL", null, ["callee:00c53da0:8"]]
- 0078fd54 bytes eb0f1394
+ 0078fdac bytes fd0f1394
- 0078fd68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078fd68 ["INT_ADD", "register:40f0:8", ["const:78fd68:8", "const:4:8"]]
- 0078fd68 ["CALLIND", null, ["register:0:8"]]
+ 0078fdc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0078fdc0 ["INT_ADD", "register:40f0:8", ["const:78fdc0:8", "const:4:8"]]
+ 0078fdc0 ["CALLIND", null, ["register:0:8"]]
- 0078fd68 bytes 00013fd6
+ 0078fdc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b816ad99d80b6a2b76349cf8bd8d5d"></a>

### [`00791224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md) → [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md) FUN_0079127c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md)
- 新版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00791270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md#insn-00791270) · [`007912b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md#insn-007912b8) · [`007912d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md#insn-007912d0)
- 新版 [`007912c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-007912c8) · [`00791310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-00791310) · [`00791328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-00791328)

~~~diff
- 00791270 ["INT_ADD", "register:40f0:8", ["const:791270:8", "const:4:8"]]
- 00791270 ["CALL", null, ["callee:0048cec4:8"]]
+ 007912c8 ["INT_ADD", "register:40f0:8", ["const:7912c8:8", "const:4:8"]]
+ 007912c8 ["CALL", null, ["callee:0048cec4:8"]]
- 00791270 bytes 05eff397
+ 007912c8 bytes ffeef397
- 007912b8 ["INT_ADD", "register:40f0:8", ["const:7912b8:8", "const:4:8"]]
- 007912b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00791310 ["INT_ADD", "register:40f0:8", ["const:791310:8", "const:4:8"]]
+ 00791310 ["CALL", null, ["callee:00c57f60:8"]]
- 007912b8 bytes f61a1394
+ 00791310 bytes 141b1394
- 007912d0 ["INT_ADD", "register:40f0:8", ["const:7912d0:8", "const:4:8"]]
- 007912d0 ["CALL", null, ["callee:00c580d0:8"]]
+ 00791328 ["INT_ADD", "register:40f0:8", ["const:791328:8", "const:4:8"]]
+ 00791328 ["CALL", null, ["callee:00c580d0:8"]]
- 007912d0 bytes 4c1b1394
+ 00791328 bytes 6a1b1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639d92f017c832a2ad7b733096fa270c"></a>

### [`00791850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791850.md) → [`007918a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md) FUN_007918a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00791890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791850.md#insn-00791890) · [`007918d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791850.md#insn-007918d8)
- 新版 [`007918e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md#insn-007918e8) · [`00791930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md#insn-00791930)

~~~diff
- 00791890 ["INT_ADD", "register:40f0:8", ["const:791890:8", "const:4:8"]]
- 00791890 ["CALL", null, ["callee:00c57f80:8"]]
+ 007918e8 ["INT_ADD", "register:40f0:8", ["const:7918e8:8", "const:4:8"]]
+ 007918e8 ["CALL", null, ["callee:00c57f80:8"]]
- 00791890 bytes 88191394
+ 007918e8 bytes a6191394
- 007918d8 ["INT_ADD", "register:40f0:8", ["const:7918d8:8", "const:4:8"]]
- 007918d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00791930 ["INT_ADD", "register:40f0:8", ["const:791930:8", "const:4:8"]]
+ 00791930 ["CALL", null, ["callee:00c57f80:8"]]
- 007918d8 bytes 76191394
+ 00791930 bytes 94191394
~~~


<a id="compare-845787c44c490b5d99ee7460b1a31bbc"></a>

### [`00791910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md) → [`00791968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md) FUN_00791968

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0072b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b144.md) [`007941d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007941d4.md)
- 新版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0072b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072b/0072b19c.md) [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00791990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md#insn-00791990) · [`007919a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md#insn-007919a8) · [`007919c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md#insn-007919c4)
- 新版 [`007919e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-007919e8) · [`00791a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-00791a00) · [`00791a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-00791a1c)

~~~diff
- 00791990 ["INT_ADD", "register:40f0:8", ["const:791990:8", "const:4:8"]]
- 00791990 ["CALL", null, ["callee:00c57f60:8"]]
+ 007919e8 ["INT_ADD", "register:40f0:8", ["const:7919e8:8", "const:4:8"]]
+ 007919e8 ["CALL", null, ["callee:00c57f60:8"]]
- 00791990 bytes 40191394
+ 007919e8 bytes 5e191394
- 007919a8 ["INT_ADD", "register:40f0:8", ["const:7919a8:8", "const:4:8"]]
- 007919a8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00791a00 ["INT_ADD", "register:40f0:8", ["const:791a00:8", "const:4:8"]]
+ 00791a00 ["CALL", null, ["callee:00c580d0:8"]]
- 007919a8 bytes 96191394
+ 00791a00 bytes b4191394
- 007919c4 ["INT_ADD", "register:40f0:8", ["const:7919c4:8", "const:4:8"]]
- 007919c4 ["CALL", null, ["callee:0072b19c:8"]]
+ 00791a1c ["INT_ADD", "register:40f0:8", ["const:791a1c:8", "const:4:8"]]
+ 00791a1c ["CALL", null, ["callee:0072b19c:8"]]
- 007919c4 bytes e065fe97
+ 00791a1c bytes e065fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1cd4274061d4527a73eb8f77d0c71e"></a>

### [`00791e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md) → [`00791eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md) FUN_00791eb8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md)
- 新版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00791eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md#insn-00791eac) · [`00791ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md#insn-00791ef4) · [`00791f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md#insn-00791f0c)
- 新版 [`00791f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-00791f04) · [`00791f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-00791f4c) · [`00791f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-00791f64)

~~~diff
- 00791eac ["INT_ADD", "register:40f0:8", ["const:791eac:8", "const:4:8"]]
- 00791eac ["CALL", null, ["callee:0048cec4:8"]]
+ 00791f04 ["INT_ADD", "register:40f0:8", ["const:791f04:8", "const:4:8"]]
+ 00791f04 ["CALL", null, ["callee:0048cec4:8"]]
- 00791eac bytes f6ebf397
+ 00791f04 bytes f0ebf397
- 00791ef4 ["INT_ADD", "register:40f0:8", ["const:791ef4:8", "const:4:8"]]
- 00791ef4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00791f4c ["INT_ADD", "register:40f0:8", ["const:791f4c:8", "const:4:8"]]
+ 00791f4c ["CALL", null, ["callee:00c57f60:8"]]
- 00791ef4 bytes e7171394
+ 00791f4c bytes 05181394
- 00791f0c ["INT_ADD", "register:40f0:8", ["const:791f0c:8", "const:4:8"]]
- 00791f0c ["CALL", null, ["callee:00c580d0:8"]]
+ 00791f64 ["INT_ADD", "register:40f0:8", ["const:791f64:8", "const:4:8"]]
+ 00791f64 ["CALL", null, ["callee:00c580d0:8"]]
- 00791f0c bytes 3d181394
+ 00791f64 bytes 5b181394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-947014d1502cafb2651adbae1f5a9b2e"></a>

### [`00792484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md) → [`007924dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md) FUN_007924dc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0072ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ade0.md) [`007941d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007941d4.md)
- 新版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0072ae38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072a/0072ae38.md) [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00792500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md#insn-00792500) · [`00792518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md#insn-00792518) · [`0079252c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md#insn-0079252c)
- 新版 [`00792558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792558) · [`00792570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792570) · [`00792584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792584)

~~~diff
- 00792500 ["INT_ADD", "register:40f0:8", ["const:792500:8", "const:4:8"]]
- 00792500 ["CALL", null, ["callee:00c57f60:8"]]
+ 00792558 ["INT_ADD", "register:40f0:8", ["const:792558:8", "const:4:8"]]
+ 00792558 ["CALL", null, ["callee:00c57f60:8"]]
- 00792500 bytes 64161394
+ 00792558 bytes 82161394
- 00792518 ["INT_ADD", "register:40f0:8", ["const:792518:8", "const:4:8"]]
- 00792518 ["CALL", null, ["callee:00c580d0:8"]]
+ 00792570 ["INT_ADD", "register:40f0:8", ["const:792570:8", "const:4:8"]]
+ 00792570 ["CALL", null, ["callee:00c580d0:8"]]
- 00792518 bytes ba161394
+ 00792570 bytes d8161394
- 0079252c ["INT_ADD", "register:40f0:8", ["const:79252c:8", "const:4:8"]]
- 0079252c ["CALL", null, ["callee:0072ae38:8"]]
+ 00792584 ["INT_ADD", "register:40f0:8", ["const:792584:8", "const:4:8"]]
+ 00792584 ["CALL", null, ["callee:0072ae38:8"]]
- 0079252c bytes 2d62fe97
+ 00792584 bytes 2d62fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7be456b29f8305269a746e0a2d31d72a"></a>

### [`00792cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792cd4.md) → [`00792d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md) FUN_00792d2c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 3件 [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 3件 [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00792cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792cd4.md#insn-00792cfc) · [`00792d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792cd4.md#insn-00792d0c) · [`00792d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792cd4.md#insn-00792d18)
- 新版 [`00792d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d54) · [`00792d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d64) · [`00792d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d70)

~~~diff
- 00792cfc ["INT_ADD", "register:40f0:8", ["const:792cfc:8", "const:4:8"]]
- 00792cfc ["CALL", null, ["callee:008b7a20:8"]]
+ 00792d54 ["INT_ADD", "register:40f0:8", ["const:792d54:8", "const:4:8"]]
+ 00792d54 ["CALL", null, ["callee:008b7a20:8"]]
- 00792cfc bytes 33930494
+ 00792d54 bytes 33930494
- 00792d0c ["INT_ADD", "register:40f0:8", ["const:792d0c:8", "const:4:8"]]
- 00792d0c ["CALL", null, ["callee:008b6f68:8"]]
+ 00792d64 ["INT_ADD", "register:40f0:8", ["const:792d64:8", "const:4:8"]]
+ 00792d64 ["CALL", null, ["callee:008b6f68:8"]]
- 00792d0c bytes 81900494
+ 00792d64 bytes 81900494
- 00792d18 ["INT_ADD", "register:40f0:8", ["const:792d18:8", "const:4:8"]]
- 00792d18 ["CALL", null, ["callee:008b6f70:8"]]
+ 00792d70 ["INT_ADD", "register:40f0:8", ["const:792d70:8", "const:4:8"]]
+ 00792d70 ["CALL", null, ["callee:008b6f70:8"]]
- 00792d18 bytes 80900494
+ 00792d70 bytes 80900494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d770acd52392ea16810a7e9176f75d"></a>

### [`00794140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794140.md) → [`00794198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794198.md) FUN_00794198

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079415c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794140.md#insn-0079415c)
- 新版 [`007941b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794198.md#insn-007941b4)

~~~diff
- 0079415c ["INT_ADD", "register:40f0:8", ["const:79415c:8", "const:4:8"]]
- 0079415c ["CALL", null, ["callee:008b79a0:8"]]
+ 007941b4 ["INT_ADD", "register:40f0:8", ["const:7941b4:8", "const:4:8"]]
+ 007941b4 ["CALL", null, ["callee:008b79a0:8"]]
- 0079415c bytes fb8d0494
+ 007941b4 bytes fb8d0494
~~~


<a id="compare-6f44de2ff0fd262925a246e794039f60"></a>

### [`00794708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794708.md) → [`00794760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md) FUN_00794760

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794708.md#insn-00794754) · [`00794768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794708.md#insn-00794768) · [`00794770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794708.md#insn-00794770)
- 新版 [`007947ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947ac) · [`007947c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947c0) · [`007947c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947c8)

~~~diff
- 00794754 ["INT_ADD", "register:40f0:8", ["const:794754:8", "const:4:8"]]
- 00794754 ["CALL", null, ["callee:00c53da0:8"]]
+ 007947ac ["INT_ADD", "register:40f0:8", ["const:7947ac:8", "const:4:8"]]
+ 007947ac ["CALL", null, ["callee:00c53da0:8"]]
- 00794754 bytes 6bfd1294
+ 007947ac bytes 7dfd1294
- 00794768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00794768 ["INT_ADD", "register:40f0:8", ["const:794768:8", "const:4:8"]]
- 00794768 ["CALLIND", null, ["register:0:8"]]
+ 007947c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007947c0 ["INT_ADD", "register:40f0:8", ["const:7947c0:8", "const:4:8"]]
+ 007947c0 ["CALLIND", null, ["register:0:8"]]
- 00794768 bytes 00013fd6
+ 007947c0 bytes 00013fd6
- 00794770 ["INT_ADD", "register:40f0:8", ["const:794770:8", "const:4:8"]]
- 00794770 ["CALL", null, ["callee:00c57f50:8"]]
+ 007947c8 ["INT_ADD", "register:40f0:8", ["const:7947c8:8", "const:4:8"]]
+ 007947c8 ["CALL", null, ["callee:00c57f50:8"]]
- 00794770 bytes c40d1394
+ 007947c8 bytes e20d1394
~~~


<a id="compare-d55ca481090582b50e7346b3cb026714"></a>

### [`007947a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007947a0.md) → [`007947f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md) FUN_007947f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00929498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929498.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0092918c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/0092918c.md)
- 新版 呼出元 1件 [`009294ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/009294ec.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009291e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/009291e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007947b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007947a0.md#insn-007947b0) · [`007947bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007947a0.md#insn-007947bc)
- 新版 [`00794808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md#insn-00794808) · [`00794814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md#insn-00794814)

~~~diff
- 007947b0 ["INT_ADD", "register:40f0:8", ["const:7947b0:8", "const:4:8"]]
- 007947b0 ["CALL", null, ["callee:00851550:8"]]
+ 00794808 ["INT_ADD", "register:40f0:8", ["const:794808:8", "const:4:8"]]
+ 00794808 ["CALL", null, ["callee:00851550:8"]]
- 007947b0 bytes 52f30294
+ 00794808 bytes 52f30294
- 007947bc ["INT_ADD", "register:40f0:8", ["const:7947bc:8", "const:4:8"]]
- 007947bc ["CALL", null, ["callee:009291e0:8"]]
+ 00794814 ["INT_ADD", "register:40f0:8", ["const:794814:8", "const:4:8"]]
+ 00794814 ["CALL", null, ["callee:009291e0:8"]]
- 007947bc bytes 74520694
+ 00794814 bytes 73520694
~~~


<a id="compare-79df67aff237ffd4986a786b7fc48948"></a>

### [`0079493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md) → [`00794994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md) FUN_00794994

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) [`00791224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md) [`00791910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md) [`00791e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md) [`00792484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md) · 呼出先 6件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00794a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794a90.md) [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 5件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md) [`00791968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md) [`00791eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md) [`007924dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md) · 呼出先 6件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00794ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md) [`00794bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md#insn-00794998) · [`007949f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md#insn-007949f4) · [`00794a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md#insn-00794a50)
- 新版 [`007949f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-007949f0) · [`00794a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-00794a4c) · [`00794aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-00794aa8)

~~~diff
- 00794998 ["INT_ADD", "register:40f0:8", ["const:794998:8", "const:4:8"]]
- 00794998 ["CALL", null, ["callee:00c57f60:8"]]
+ 007949f0 ["INT_ADD", "register:40f0:8", ["const:7949f0:8", "const:4:8"]]
+ 007949f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00794998 bytes 3e0d1394
+ 007949f0 bytes 5c0d1394
- 007949f4 ["INT_ADD", "register:40f0:8", ["const:7949f4:8", "const:4:8"]]
- 007949f4 ["CALL", null, ["callee:0054079c:8"]]
+ 00794a4c ["INT_ADD", "register:40f0:8", ["const:794a4c:8", "const:4:8"]]
+ 00794a4c ["CALL", null, ["callee:0054079c:8"]]
- 007949f4 bytes 5aaff697
+ 00794a4c bytes 54aff697
- 00794a50 ["INT_ADD", "register:40f0:8", ["const:794a50:8", "const:4:8"]]
- 00794a50 ["CALL", null, ["callee:00794bc4:8"]]
+ 00794aa8 ["INT_ADD", "register:40f0:8", ["const:794aa8:8", "const:4:8"]]
+ 00794aa8 ["CALL", null, ["callee:00794bc4:8"]]
- 00794a50 bytes 47000094
+ 00794aa8 bytes 47000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b67688fd3400c741924346cadaad89e"></a>

### [`00794a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794a90.md) → [`00794ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md) FUN_00794ae8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00794994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794a90.md#insn-00794af8) · [`00794b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794a90.md#insn-00794b40)
- 新版 [`00794b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md#insn-00794b50) · [`00794b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md#insn-00794b98)

~~~diff
- 00794af8 ["INT_ADD", "register:40f0:8", ["const:794af8:8", "const:4:8"]]
- 00794af8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00794b50 ["INT_ADD", "register:40f0:8", ["const:794b50:8", "const:4:8"]]
+ 00794b50 ["CALL", null, ["callee:00c57f80:8"]]
- 00794af8 bytes ee0c1394
+ 00794b50 bytes 0c0d1394
- 00794b40 ["INT_ADD", "register:40f0:8", ["const:794b40:8", "const:4:8"]]
- 00794b40 ["CALL", null, ["callee:00c57f80:8"]]
+ 00794b98 ["INT_ADD", "register:40f0:8", ["const:794b98:8", "const:4:8"]]
+ 00794b98 ["CALL", null, ["callee:00c57f80:8"]]
- 00794b40 bytes dc0c1394
+ 00794b98 bytes fa0c1394
~~~


<a id="compare-f186503e3dff80f99fc9a380887a8b1e"></a>

### [`00794b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b80.md) → [`00794bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md) FUN_00794bd8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b80.md#insn-00794bc4) · [`00794c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b80.md#insn-00794c0c)
- 新版 [`00794c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md#insn-00794c1c) · [`00794c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md#insn-00794c64)

~~~diff
- 00794bc4 ["INT_ADD", "register:40f0:8", ["const:794bc4:8", "const:4:8"]]
- 00794bc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00794c1c ["INT_ADD", "register:40f0:8", ["const:794c1c:8", "const:4:8"]]
+ 00794c1c ["CALL", null, ["callee:00c57f80:8"]]
- 00794bc4 bytes bb0c1394
+ 00794c1c bytes d90c1394
- 00794c0c ["INT_ADD", "register:40f0:8", ["const:794c0c:8", "const:4:8"]]
- 00794c0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00794c64 ["INT_ADD", "register:40f0:8", ["const:794c64:8", "const:4:8"]]
+ 00794c64 ["CALL", null, ["callee:00c57f80:8"]]
- 00794c0c bytes a90c1394
+ 00794c64 bytes c70c1394
~~~


<a id="compare-58ddc6ebff58d78022980d38aa1b86a1"></a>

### [`00794c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794c28.md) → [`00794c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md) FUN_00794c80

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007929c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/007929c8.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00794d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794d4c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00792a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00794da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794c28.md#insn-00794c84) · [`00794ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794c28.md#insn-00794ca4) · [`00794ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794c28.md#insn-00794ce0)
- 新版 [`00794cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md#insn-00794cdc) · [`00794cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md#insn-00794cfc) · [`00794d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md#insn-00794d38)

~~~diff
- 00794c84 ["INT_ADD", "register:40f0:8", ["const:794c84:8", "const:4:8"]]
- 00794c84 ["CALL", null, ["callee:00794da4:8"]]
+ 00794cdc ["INT_ADD", "register:40f0:8", ["const:794cdc:8", "const:4:8"]]
+ 00794cdc ["CALL", null, ["callee:00794da4:8"]]
- 00794c84 bytes 32000094
+ 00794cdc bytes 32000094
- 00794ca4 ["INT_ADD", "register:40f0:8", ["const:794ca4:8", "const:4:8"]]
- 00794ca4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00794cfc ["INT_ADD", "register:40f0:8", ["const:794cfc:8", "const:4:8"]]
+ 00794cfc ["CALL", null, ["callee:00c57f60:8"]]
- 00794ca4 bytes 7b0c1394
+ 00794cfc bytes 990c1394
- 00794ce0 ["INT_ADD", "register:40f0:8", ["const:794ce0:8", "const:4:8"]]
- 00794ce0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00794d38 ["INT_ADD", "register:40f0:8", ["const:794d38:8", "const:4:8"]]
+ 00794d38 ["CALL", null, ["callee:0043bbe4:8"]]
- 00794ce0 bytes b19bf297
+ 00794d38 bytes ab9bf297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b6dbd54bf4da15f2e5e7242f838ab4"></a>

### [`00794ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794ef4.md) → [`00794f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md) FUN_00794f4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00792eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792eb4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00792f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794ef4.md#insn-00794f64) · [`00794f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794ef4.md#insn-00794f78) · [`00794f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794ef4.md#insn-00794f80)
- 新版 [`00794fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fbc) · [`00794fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fd0) · [`00794fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fd8)

~~~diff
- 00794f64 ["INT_ADD", "register:40f0:8", ["const:794f64:8", "const:4:8"]]
- 00794f64 ["CALL", null, ["callee:00c53da0:8"]]
+ 00794fbc ["INT_ADD", "register:40f0:8", ["const:794fbc:8", "const:4:8"]]
+ 00794fbc ["CALL", null, ["callee:00c53da0:8"]]
- 00794f64 bytes 67fb1294
+ 00794fbc bytes 79fb1294
- 00794f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00794f78 ["INT_ADD", "register:40f0:8", ["const:794f78:8", "const:4:8"]]
- 00794f78 ["CALLIND", null, ["register:0:8"]]
+ 00794fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00794fd0 ["INT_ADD", "register:40f0:8", ["const:794fd0:8", "const:4:8"]]
+ 00794fd0 ["CALLIND", null, ["register:0:8"]]
- 00794f78 bytes 00013fd6
+ 00794fd0 bytes 00013fd6
- 00794f80 ["INT_ADD", "register:40f0:8", ["const:794f80:8", "const:4:8"]]
- 00794f80 ["CALL", null, ["callee:00c57f50:8"]]
+ 00794fd8 ["INT_ADD", "register:40f0:8", ["const:794fd8:8", "const:4:8"]]
+ 00794fd8 ["CALL", null, ["callee:00c57f50:8"]]
- 00794f80 bytes c00b1394
+ 00794fd8 bytes de0b1394
~~~


<a id="compare-dfb3546865a117d7681782c667ab660e"></a>

### [`0079517c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/0079517c.md) → [`007951d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md) FUN_007951d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00790204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/00790204.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007951b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/0079517c.md#insn-007951b8)
- 新版 [`00795210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md#insn-00795210)

~~~diff
- 007951b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007951b8 ["INT_ADD", "register:40f0:8", ["const:7951b8:8", "const:4:8"]]
- 007951b8 ["CALLIND", null, ["register:0:8"]]
+ 00795210 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795210 ["INT_ADD", "register:40f0:8", ["const:795210:8", "const:4:8"]]
+ 00795210 ["CALLIND", null, ["register:0:8"]]
- 007951b8 bytes 00013fd6
+ 00795210 bytes 00013fd6
~~~


<a id="compare-d4ecc8fc0593ac58f8b372abee217379"></a>

### [`00795258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md) → [`007952b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md) FUN_007952b0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007941d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007941d4.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00795454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795454.md) [`00795674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795674.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007954ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md) [`007956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007952dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md#insn-007952dc) · [`00795324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md#insn-00795324) · [`00795388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md#insn-00795388)
- 新版 [`00795334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-00795334) · [`0079537c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-0079537c) · [`007953e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-007953e0)

~~~diff
- 007952dc ["INT_ADD", "register:40f0:8", ["const:7952dc:8", "const:4:8"]]
- 007952dc ["CALL", null, ["callee:00c57f60:8"]]
+ 00795334 ["INT_ADD", "register:40f0:8", ["const:795334:8", "const:4:8"]]
+ 00795334 ["CALL", null, ["callee:00c57f60:8"]]
- 007952dc bytes ed0a1394
+ 00795334 bytes 0b0b1394
- 00795324 ["INT_ADD", "register:40f0:8", ["const:795324:8", "const:4:8"]]
- 00795324 ["CALL", null, ["callee:007954ac:8"]]
+ 0079537c ["INT_ADD", "register:40f0:8", ["const:79537c:8", "const:4:8"]]
+ 0079537c ["CALL", null, ["callee:007954ac:8"]]
- 00795324 bytes 4c000094
+ 0079537c bytes 4c000094
- 00795388 ["INT_ADD", "register:40f0:8", ["const:795388:8", "const:4:8"]]
- 00795388 ["CALL", null, ["callee:00c53da0:8"]]
+ 007953e0 ["INT_ADD", "register:40f0:8", ["const:7953e0:8", "const:4:8"]]
+ 007953e0 ["CALL", null, ["callee:00c53da0:8"]]
- 00795388 bytes 5efa1294
+ 007953e0 bytes 70fa1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e241a7a760e85c5840914050f7aa514f"></a>

### [`00795454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795454.md) → [`007954ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md) FUN_007954ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00795258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007952b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007954d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795454.md#insn-007954d8) · [`00795520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795454.md#insn-00795520) · [`00795534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795454.md#insn-00795534)
- 新版 [`00795530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-00795530) · [`00795578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-00795578) · [`0079558c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-0079558c)

~~~diff
- 007954d8 ["INT_ADD", "register:40f0:8", ["const:7954d8:8", "const:4:8"]]
- 007954d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00795530 ["INT_ADD", "register:40f0:8", ["const:795530:8", "const:4:8"]]
+ 00795530 ["CALL", null, ["callee:00c57f80:8"]]
- 007954d8 bytes 760a1394
+ 00795530 bytes 940a1394
- 00795520 ["INT_ADD", "register:40f0:8", ["const:795520:8", "const:4:8"]]
- 00795520 ["CALL", null, ["callee:00c53da0:8"]]
+ 00795578 ["INT_ADD", "register:40f0:8", ["const:795578:8", "const:4:8"]]
+ 00795578 ["CALL", null, ["callee:00c53da0:8"]]
- 00795520 bytes f8f91294
+ 00795578 bytes 0afa1294
- 00795534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00795534 ["INT_ADD", "register:40f0:8", ["const:795534:8", "const:4:8"]]
- 00795534 ["CALLIND", null, ["register:0:8"]]
+ 0079558c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079558c ["INT_ADD", "register:40f0:8", ["const:79558c:8", "const:4:8"]]
+ 0079558c ["CALLIND", null, ["register:0:8"]]
- 00795534 bytes 00013fd6
+ 0079558c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed9ffe3067bb7b066c19869e790e8a0"></a>

### [`00795594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795594.md) → [`007955ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md) FUN_007955ec

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00795608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795594.md#insn-00795608) · [`0079561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795594.md#insn-0079561c) · [`00795624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795594.md#insn-00795624)
- 新版 [`00795660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-00795660) · [`00795674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-00795674) · [`0079567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-0079567c)

~~~diff
- 00795608 ["INT_ADD", "register:40f0:8", ["const:795608:8", "const:4:8"]]
- 00795608 ["CALL", null, ["callee:00c53da0:8"]]
+ 00795660 ["INT_ADD", "register:40f0:8", ["const:795660:8", "const:4:8"]]
+ 00795660 ["CALL", null, ["callee:00c53da0:8"]]
- 00795608 bytes bef91294
+ 00795660 bytes d0f91294
- 0079561c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079561c ["INT_ADD", "register:40f0:8", ["const:79561c:8", "const:4:8"]]
- 0079561c ["CALLIND", null, ["register:0:8"]]
+ 00795674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795674 ["INT_ADD", "register:40f0:8", ["const:795674:8", "const:4:8"]]
+ 00795674 ["CALLIND", null, ["register:0:8"]]
- 0079561c bytes 00013fd6
+ 00795674 bytes 00013fd6
- 00795624 ["INT_ADD", "register:40f0:8", ["const:795624:8", "const:4:8"]]
- 00795624 ["CALL", null, ["callee:00c57f50:8"]]
+ 0079567c ["INT_ADD", "register:40f0:8", ["const:79567c:8", "const:4:8"]]
+ 0079567c ["CALL", null, ["callee:00c57f50:8"]]
- 00795624 bytes 170a1394
+ 0079567c bytes 350a1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f3d33f20e7a299390c06eb4652418d"></a>

### [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md) → [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md) FUN_00795eb4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 18件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 2件 [`00796104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 18件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) · 呼出先 2件 [`0079615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00795e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md#insn-00795e9c) · [`00795eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md#insn-00795eb4)
- 新版 [`00795ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md#insn-00795ef4) · [`00795f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md#insn-00795f0c)

~~~diff
- 00795e9c ["INT_ADD", "register:40f0:8", ["const:795e9c:8", "const:4:8"]]
- 00795e9c ["CALL", null, ["callee:00c53d70:8"]]
+ 00795ef4 ["INT_ADD", "register:40f0:8", ["const:795ef4:8", "const:4:8"]]
+ 00795ef4 ["CALL", null, ["callee:00c53d70:8"]]
- 00795e9c bytes 8df71294
+ 00795ef4 bytes 9ff71294
- 00795eb4 ["INT_ADD", "register:40f0:8", ["const:795eb4:8", "const:4:8"]]
- 00795eb4 ["CALL", null, ["callee:0079615c:8"]]
+ 00795f0c ["INT_ADD", "register:40f0:8", ["const:795f0c:8", "const:4:8"]]
+ 00795f0c ["CALL", null, ["callee:0079615c:8"]]
- 00795eb4 bytes 94000094
+ 00795f0c bytes 94000094
~~~


<a id="compare-554188b249e515514d392217c9c9f8ba"></a>

### [`00795edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795edc.md) → [`00795f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md) FUN_00795f34

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 3件 [`00795fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795fe4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 4件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 3件 [`0079603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00795fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795edc.md#insn-00795fa0) · [`00795fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795edc.md#insn-00795fb4) · [`00795fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795edc.md#insn-00795fbc)
- 新版 [`00795ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-00795ff8) · [`0079600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-0079600c) · [`00796014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-00796014)

~~~diff
- 00795fa0 ["INT_ADD", "register:40f0:8", ["const:795fa0:8", "const:4:8"]]
- 00795fa0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00795ff8 ["INT_ADD", "register:40f0:8", ["const:795ff8:8", "const:4:8"]]
+ 00795ff8 ["CALL", null, ["callee:00c53da0:8"]]
- 00795fa0 bytes 58f71294
+ 00795ff8 bytes 6af71294
- 00795fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00795fb4 ["INT_ADD", "register:40f0:8", ["const:795fb4:8", "const:4:8"]]
- 00795fb4 ["CALLIND", null, ["register:0:8"]]
+ 0079600c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079600c ["INT_ADD", "register:40f0:8", ["const:79600c:8", "const:4:8"]]
+ 0079600c ["CALLIND", null, ["register:0:8"]]
- 00795fb4 bytes 00013fd6
+ 0079600c bytes 00013fd6
- 00795fbc ["INT_ADD", "register:40f0:8", ["const:795fbc:8", "const:4:8"]]
- 00795fbc ["CALL", null, ["callee:00c57f50:8"]]
+ 00796014 ["INT_ADD", "register:40f0:8", ["const:796014:8", "const:4:8"]]
+ 00796014 ["CALL", null, ["callee:00c57f50:8"]]
- 00795fbc bytes b1071394
+ 00796014 bytes cf071394
~~~


<a id="compare-6ec6f3e285a6066b93c740faed0a1d83"></a>

### [`00795fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795fe4.md) → [`0079603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md) FUN_0079603c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00795edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795edc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00795f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079606c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795fe4.md#insn-0079606c) · [`00796080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795fe4.md#insn-00796080) · [`00796088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795fe4.md#insn-00796088)
- 新版 [`007960c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md#insn-007960c4) · [`007960d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md#insn-007960d8) · [`007960e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md#insn-007960e0)

~~~diff
- 0079606c ["INT_ADD", "register:40f0:8", ["const:79606c:8", "const:4:8"]]
- 0079606c ["CALL", null, ["callee:00c53da0:8"]]
+ 007960c4 ["INT_ADD", "register:40f0:8", ["const:7960c4:8", "const:4:8"]]
+ 007960c4 ["CALL", null, ["callee:00c53da0:8"]]
- 0079606c bytes 25f71294
+ 007960c4 bytes 37f71294
- 00796080 ["COPY", "register:0:8", ["register:4040:8"]]
- 00796080 ["INT_ADD", "register:40f0:8", ["const:796080:8", "const:4:8"]]
- 00796080 ["CALLIND", null, ["register:0:8"]]
+ 007960d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007960d8 ["INT_ADD", "register:40f0:8", ["const:7960d8:8", "const:4:8"]]
+ 007960d8 ["CALLIND", null, ["register:0:8"]]
- 00796080 bytes 00013fd6
+ 007960d8 bytes 00013fd6
- 00796088 ["INT_ADD", "register:40f0:8", ["const:796088:8", "const:4:8"]]
- 00796088 ["CALL", null, ["callee:00c57f50:8"]]
+ 007960e0 ["INT_ADD", "register:40f0:8", ["const:7960e0:8", "const:4:8"]]
+ 007960e0 ["CALL", null, ["callee:00c57f50:8"]]
- 00796088 bytes 7e071394
+ 007960e0 bytes 9c071394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5fe0ae596377a34a76b734009d55bda"></a>

### [`00796104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md) → [`0079615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md) FUN_0079615c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00796260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796260.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007962b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00796170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md#insn-00796170) · [`0079619c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md#insn-0079619c) · [`007961fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md#insn-007961fc)
- 新版 [`007961c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-007961c8) · [`007961f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-007961f4) · [`00796254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-00796254)

~~~diff
- 00796170 ["INT_ADD", "register:40f0:8", ["const:796170:8", "const:4:8"]]
- 00796170 ["CALL", null, ["callee:00c57f60:8"]]
+ 007961c8 ["INT_ADD", "register:40f0:8", ["const:7961c8:8", "const:4:8"]]
+ 007961c8 ["CALL", null, ["callee:00c57f60:8"]]
- 00796170 bytes 48071394
+ 007961c8 bytes 66071394
- 0079619c ["INT_ADD", "register:40f0:8", ["const:79619c:8", "const:4:8"]]
- 0079619c ["CALL", null, ["callee:00c53d70:8"]]
+ 007961f4 ["INT_ADD", "register:40f0:8", ["const:7961f4:8", "const:4:8"]]
+ 007961f4 ["CALL", null, ["callee:00c53d70:8"]]
- 0079619c bytes cdf61294
+ 007961f4 bytes dff61294
- 007961fc ["INT_ADD", "register:40f0:8", ["const:7961fc:8", "const:4:8"]]
- 007961fc ["CALL", null, ["callee:00c53da0:8"]]
+ 00796254 ["INT_ADD", "register:40f0:8", ["const:796254:8", "const:4:8"]]
+ 00796254 ["CALL", null, ["callee:00c53da0:8"]]
- 007961fc bytes c1f61294
+ 00796254 bytes d3f61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d974bfb5d0ed06dda7d8cdd0ab6b610c"></a>

### [`00796604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796604.md) → [`0079665c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md) FUN_0079665c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) · 呼出先 2件 [`00796634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796634.md) [`00796af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796af8.md)
- 新版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 2件 [`0079668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md) [`00796b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079661c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796604.md#insn-0079661c)
- 新版 [`00796674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md#insn-00796674)

~~~diff
- 0079661c ["INT_ADD", "register:40f0:8", ["const:79661c:8", "const:4:8"]]
- 0079661c ["CALL", null, ["callee:0079668c:8"]]
+ 00796674 ["INT_ADD", "register:40f0:8", ["const:796674:8", "const:4:8"]]
+ 00796674 ["CALL", null, ["callee:0079668c:8"]]
- 0079661c bytes 06000094
+ 00796674 bytes 06000094
~~~


<a id="compare-1945871991a841c684e4dd8b3daf38d3"></a>

### [`00797a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797a30.md) → [`00797a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md) FUN_00797a88

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 2件 [`0079fe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 2件 [`0079fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fe88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00797a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797a30.md#insn-00797a78) · [`00797a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797a30.md#insn-00797a80)
- 新版 [`00797ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md#insn-00797ad0) · [`00797ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md#insn-00797ad8)

~~~diff
- 00797a78 ["INT_ADD", "register:40f0:8", ["const:797a78:8", "const:4:8"]]
- 00797a78 ["CALL", null, ["callee:00c57f60:8"]]
+ 00797ad0 ["INT_ADD", "register:40f0:8", ["const:797ad0:8", "const:4:8"]]
+ 00797ad0 ["CALL", null, ["callee:00c57f60:8"]]
- 00797a78 bytes 06011394
+ 00797ad0 bytes 24011394
- 00797a80 ["INT_ADD", "register:40f0:8", ["const:797a80:8", "const:4:8"]]
- 00797a80 ["CALL", null, ["callee:0079fe88:8"]]
+ 00797ad8 ["INT_ADD", "register:40f0:8", ["const:797ad8:8", "const:4:8"]]
+ 00797ad8 ["CALL", null, ["callee:0079fe88:8"]]
- 00797a80 bytes ec200094
+ 00797ad8 bytes ec200094
~~~


<a id="compare-615e2865081f02ee2a736442c7266a3f"></a>

### [`00797ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md) → [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) FUN_00797b30

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008485b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008485b0.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 4件 [`0079d0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md) [`0079d178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md) [`0079d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848608.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 4件 [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00797b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md#insn-00797b20) · [`00797b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md#insn-00797b30) · [`00797b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md#insn-00797b44)
- 新版 [`00797b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md#insn-00797b78) · [`00797b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md#insn-00797b88) · [`00797b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md#insn-00797b9c)

~~~diff
- 00797b20 ["INT_ADD", "register:40f0:8", ["const:797b20:8", "const:4:8"]]
- 00797b20 ["CALL", null, ["callee:00c57f80:8"]]
+ 00797b78 ["INT_ADD", "register:40f0:8", ["const:797b78:8", "const:4:8"]]
+ 00797b78 ["CALL", null, ["callee:00c57f80:8"]]
- 00797b20 bytes e4001394
+ 00797b78 bytes 02011394
- 00797b30 ["INT_ADD", "register:40f0:8", ["const:797b30:8", "const:4:8"]]
- 00797b30 ["CALL", null, ["callee:00c57f80:8"]]
+ 00797b88 ["INT_ADD", "register:40f0:8", ["const:797b88:8", "const:4:8"]]
+ 00797b88 ["CALL", null, ["callee:00c57f80:8"]]
- 00797b30 bytes e0001394
+ 00797b88 bytes fe001394
- 00797b44 ["INT_ADD", "register:40f0:8", ["const:797b44:8", "const:4:8"]]
- 00797b44 ["CALL", null, ["callee:0079d130:8"]]
+ 00797b9c ["INT_ADD", "register:40f0:8", ["const:797b9c:8", "const:4:8"]]
+ 00797b9c ["CALL", null, ["callee:0079d130:8"]]
- 00797b44 bytes 65150094
+ 00797b9c bytes 65150094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae13027c21fb37ea8f28bc3f64bfee0e"></a>

### [`00797b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b84.md) → [`00797bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md) FUN_00797bdc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0079d258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d258.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0079d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00797c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b84.md#insn-00797c60) · [`00797c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b84.md#insn-00797c90) · [`00797c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b84.md#insn-00797c98)
- 新版 [`00797cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797cb8) · [`00797ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797ce8) · [`00797cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797cf0)

~~~diff
- 00797c60 ["INT_ADD", "register:40f0:8", ["const:797c60:8", "const:4:8"]]
- 00797c60 ["CALL", null, ["callee:00494650:8"]]
+ 00797cb8 ["INT_ADD", "register:40f0:8", ["const:797cb8:8", "const:4:8"]]
+ 00797cb8 ["CALL", null, ["callee:00494650:8"]]
- 00797c60 bytes 6cf2f397
+ 00797cb8 bytes 66f2f397
- 00797c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00797c90 ["INT_ADD", "register:40f0:8", ["const:797c90:8", "const:4:8"]]
- 00797c90 ["CALLIND", null, ["register:0:8"]]
+ 00797ce8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00797ce8 ["INT_ADD", "register:40f0:8", ["const:797ce8:8", "const:4:8"]]
+ 00797ce8 ["CALLIND", null, ["register:0:8"]]
- 00797c90 bytes 00013fd6
+ 00797ce8 bytes 00013fd6
- 00797c98 ["INT_ADD", "register:40f0:8", ["const:797c98:8", "const:4:8"]]
- 00797c98 ["CALL", null, ["callee:00c57f80:8"]]
+ 00797cf0 ["INT_ADD", "register:40f0:8", ["const:797cf0:8", "const:4:8"]]
+ 00797cf0 ["CALL", null, ["callee:00c57f80:8"]]
- 00797c98 bytes 86001394
+ 00797cf0 bytes a4001394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78ea8b87c73c45ef0d822c94fe6c5c22"></a>

### [`00797ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ddc.md) → [`00797e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md) FUN_00797e34

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00797eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ddc.md#insn-00797eb8) · [`00797ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ddc.md#insn-00797ee8) · [`00797ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ddc.md#insn-00797ef0)
- 新版 [`00797f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797f10) · [`00797f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797f40) · [`00797f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797f48)

~~~diff
- 00797eb8 ["INT_ADD", "register:40f0:8", ["const:797eb8:8", "const:4:8"]]
- 00797eb8 ["CALL", null, ["callee:00494650:8"]]
+ 00797f10 ["INT_ADD", "register:40f0:8", ["const:797f10:8", "const:4:8"]]
+ 00797f10 ["CALL", null, ["callee:00494650:8"]]
- 00797eb8 bytes d6f1f397
+ 00797f10 bytes d0f1f397
- 00797ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00797ee8 ["INT_ADD", "register:40f0:8", ["const:797ee8:8", "const:4:8"]]
- 00797ee8 ["CALLIND", null, ["register:0:8"]]
+ 00797f40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00797f40 ["INT_ADD", "register:40f0:8", ["const:797f40:8", "const:4:8"]]
+ 00797f40 ["CALLIND", null, ["register:0:8"]]
- 00797ee8 bytes 00013fd6
+ 00797f40 bytes 00013fd6
- 00797ef0 ["INT_ADD", "register:40f0:8", ["const:797ef0:8", "const:4:8"]]
- 00797ef0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00797f48 ["INT_ADD", "register:40f0:8", ["const:797f48:8", "const:4:8"]]
+ 00797f48 ["CALL", null, ["callee:00c57f80:8"]]
- 00797ef0 bytes f0ff1294
+ 00797f48 bytes 0e001394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3891d80e287c780f8edd28e7ce2eb8d7"></a>

### [`00798dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798dd4.md) → [`00798e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e2c.md) FUN_00798e2c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00798e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798dd4.md#insn-00798e08)
- 新版 [`00798e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e2c.md#insn-00798e60)

~~~diff
- 00798e08 ["INT_ADD", "register:40f0:8", ["const:798e08:8", "const:4:8"]]
- 00798e08 ["CALL", null, ["callee:00c57f80:8"]]
+ 00798e60 ["INT_ADD", "register:40f0:8", ["const:798e60:8", "const:4:8"]]
+ 00798e60 ["CALL", null, ["callee:00c57f80:8"]]
- 00798e08 bytes 2afc1294
+ 00798e60 bytes 48fc1294
~~~


<a id="compare-5ad97499ad04bf7810368ab571842d90"></a>

### [`00798e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798e24.md) → [`00798e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md) FUN_00798e7c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) · 呼出先 4件 [`0079d0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md) [`0079fe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 4件 [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) [`0079fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fe88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00798e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798e24.md#insn-00798e48) · [`00798e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798e24.md#insn-00798e50) · [`00798e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798e24.md#insn-00798e64)
- 新版 [`00798ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ea0) · [`00798ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ea8) · [`00798ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ebc)

~~~diff
- 00798e48 ["INT_ADD", "register:40f0:8", ["const:798e48:8", "const:4:8"]]
- 00798e48 ["CALL", null, ["callee:00c57f60:8"]]
+ 00798ea0 ["INT_ADD", "register:40f0:8", ["const:798ea0:8", "const:4:8"]]
+ 00798ea0 ["CALL", null, ["callee:00c57f60:8"]]
- 00798e48 bytes 12fc1294
+ 00798ea0 bytes 30fc1294
- 00798e50 ["INT_ADD", "register:40f0:8", ["const:798e50:8", "const:4:8"]]
- 00798e50 ["CALL", null, ["callee:0079fe88:8"]]
+ 00798ea8 ["INT_ADD", "register:40f0:8", ["const:798ea8:8", "const:4:8"]]
+ 00798ea8 ["CALL", null, ["callee:0079fe88:8"]]
- 00798e50 bytes f81b0094
+ 00798ea8 bytes f81b0094
- 00798e64 ["INT_ADD", "register:40f0:8", ["const:798e64:8", "const:4:8"]]
- 00798e64 ["CALL", null, ["callee:0079d130:8"]]
+ 00798ebc ["INT_ADD", "register:40f0:8", ["const:798ebc:8", "const:4:8"]]
+ 00798ebc ["CALL", null, ["callee:0079d130:8"]]
- 00798e64 bytes 9d100094
+ 00798ebc bytes 9d100094
~~~


<a id="compare-51b550701344e992723866bab8ef3f10"></a>

### [`00799c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c0c.md) → [`00799c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md) FUN_00799c64

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00799c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c0c.md#insn-00799c54) · [`00799c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c0c.md#insn-00799c64)
- 新版 [`00799cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md#insn-00799cac) · [`00799cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md#insn-00799cbc)

~~~diff
- 00799c54 ["INT_ADD", "register:40f0:8", ["const:799c54:8", "const:4:8"]]
- 00799c54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00799cac ["INT_ADD", "register:40f0:8", ["const:799cac:8", "const:4:8"]]
+ 00799cac ["CALL", null, ["callee:00c57f80:8"]]
- 00799c54 bytes 97f81294
+ 00799cac bytes b5f81294
- 00799c64 ["INT_ADD", "register:40f0:8", ["const:799c64:8", "const:4:8"]]
- 00799c64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00799cbc ["INT_ADD", "register:40f0:8", ["const:799cbc:8", "const:4:8"]]
+ 00799cbc ["CALL", null, ["callee:00c57f80:8"]]
- 00799c64 bytes 93f81294
+ 00799cbc bytes b1f81294
~~~


<a id="compare-01e076f65e98b4e17481bb4fed5856a9"></a>

### [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) → [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) FUN_0079a660

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) · 呼出先 6件 [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`0079d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 6件 [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`0079d624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079a668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md#insn-0079a668) · [`0079a6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md#insn-0079a6ac) · [`0079a6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md#insn-0079a6b8)
- 新版 [`0079a6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a6c0) · [`0079a704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a704) · [`0079a710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a710)

~~~diff
- 0079a668 ["INT_ADD", "register:40f0:8", ["const:79a668:8", "const:4:8"]]
- 0079a668 ["CALL", null, ["callee:005a4124:8"]]
+ 0079a6c0 ["INT_ADD", "register:40f0:8", ["const:79a6c0:8", "const:4:8"]]
+ 0079a6c0 ["CALL", null, ["callee:005a4124:8"]]
- 0079a668 bytes 9f26f897
+ 0079a6c0 bytes 9926f897
- 0079a6ac ["INT_ADD", "register:40f0:8", ["const:79a6ac:8", "const:4:8"]]
- 0079a6ac ["CALL", null, ["callee:005a42e0:8"]]
+ 0079a704 ["INT_ADD", "register:40f0:8", ["const:79a704:8", "const:4:8"]]
+ 0079a704 ["CALL", null, ["callee:005a42e0:8"]]
- 0079a6ac bytes fd26f897
+ 0079a704 bytes f726f897
- 0079a6b8 ["INT_ADD", "register:40f0:8", ["const:79a6b8:8", "const:4:8"]]
- 0079a6b8 ["CALL", null, ["callee:004939d8:8"]]
+ 0079a710 ["INT_ADD", "register:40f0:8", ["const:79a710:8", "const:4:8"]]
+ 0079a710 ["CALL", null, ["callee:004939d8:8"]]
- 0079a6b8 bytes b8e4f397
+ 0079a710 bytes b2e4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f25149f35bcb8f68da7f802cc9b724e"></a>

### [`0079af88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079af88.md) → [`0079afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md) FUN_0079afe0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079d864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d864.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0079d8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8bc.md) · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0079b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079af88.md#insn-0079b040) · [`0079b07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079af88.md#insn-0079b07c) · [`0079b08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079af88.md#insn-0079b08c)
- 新版 [`0079b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079b098) · [`0079b0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079b0d4) · [`0079b0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079b0e4)

~~~diff
- 0079b040 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079b040 ["INT_ADD", "register:40f0:8", ["const:79b040:8", "const:4:8"]]
- 0079b040 ["CALLIND", null, ["register:0:8"]]
+ 0079b098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079b098 ["INT_ADD", "register:40f0:8", ["const:79b098:8", "const:4:8"]]
+ 0079b098 ["CALLIND", null, ["register:0:8"]]
- 0079b040 bytes 00013fd6
+ 0079b098 bytes 00013fd6
- 0079b07c ["INT_ADD", "register:40f0:8", ["const:79b07c:8", "const:4:8"]]
- 0079b07c ["CALL", null, ["callee:00c57f80:8"]]
+ 0079b0d4 ["INT_ADD", "register:40f0:8", ["const:79b0d4:8", "const:4:8"]]
+ 0079b0d4 ["CALL", null, ["callee:00c57f80:8"]]
- 0079b07c bytes 8df31294
+ 0079b0d4 bytes abf31294
- 0079b08c ["INT_ADD", "register:40f0:8", ["const:79b08c:8", "const:4:8"]]
- 0079b08c ["CALL", null, ["callee:00c57f80:8"]]
+ 0079b0e4 ["INT_ADD", "register:40f0:8", ["const:79b0e4:8", "const:4:8"]]
+ 0079b0e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0079b08c bytes 89f31294
+ 0079b0e4 bytes a7f31294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56483070b0ef316bdf4834783b7eb365"></a>

### [`0079b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md) → [`0079ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md) FUN_0079ba1c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079db14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db14.md) · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) [`0079bcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0079db6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db6c.md) · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) [`0079bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079b9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md#insn-0079b9fc) · [`0079ba14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md#insn-0079ba14) · [`0079ba8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md#insn-0079ba8c)
- 新版 [`0079ba54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079ba54) · [`0079ba6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079ba6c) · [`0079bae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079bae4)

~~~diff
- 0079b9fc ["INT_ADD", "register:40f0:8", ["const:79b9fc:8", "const:4:8"]]
- 0079b9fc ["CALL", null, ["callee:00799cec:8"]]
+ 0079ba54 ["INT_ADD", "register:40f0:8", ["const:79ba54:8", "const:4:8"]]
+ 0079ba54 ["CALL", null, ["callee:00799cec:8"]]
- 0079b9fc bytes a6f8ff97
+ 0079ba54 bytes a6f8ff97
- 0079ba14 ["INT_ADD", "register:40f0:8", ["const:79ba14:8", "const:4:8"]]
- 0079ba14 ["CALL", null, ["callee:0079bd14:8"]]
+ 0079ba6c ["INT_ADD", "register:40f0:8", ["const:79ba6c:8", "const:4:8"]]
+ 0079ba6c ["CALL", null, ["callee:0079bd14:8"]]
- 0079ba14 bytes aa000094
+ 0079ba6c bytes aa000094
- 0079ba8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ba8c ["INT_ADD", "register:40f0:8", ["const:79ba8c:8", "const:4:8"]]
- 0079ba8c ["CALLIND", null, ["register:0:8"]]
+ 0079bae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079bae4 ["INT_ADD", "register:40f0:8", ["const:79bae4:8", "const:4:8"]]
+ 0079bae4 ["CALLIND", null, ["register:0:8"]]
- 0079ba8c bytes 00013fd6
+ 0079bae4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b58fabe3c397b5a897c1896bd7dc7d7"></a>

### [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) → [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) FUN_0079c3f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079dc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc90.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md)
- 新版 呼出元 1件 [`0079dce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dce8.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079c408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md#insn-0079c408) · [`0079c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md#insn-0079c40c) · [`0079c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md#insn-0079c44c)
- 新版 [`0079c460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c460) · [`0079c464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c464) · [`0079c4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c4a4)

~~~diff
- 0079c408 ["INT_ADD", "register:40f0:8", ["const:79c408:8", "const:4:8"]]
- 0079c408 ["CALL", null, ["callee:005a4124:8"]]
+ 0079c460 ["INT_ADD", "register:40f0:8", ["const:79c460:8", "const:4:8"]]
+ 0079c460 ["CALL", null, ["callee:005a4124:8"]]
- 0079c408 bytes 371ff897
+ 0079c460 bytes 311ff897
- 0079c40c ["INT_ADD", "register:40f0:8", ["const:79c40c:8", "const:4:8"]]
- 0079c40c ["CALL", null, ["callee:00851550:8"]]
+ 0079c464 ["INT_ADD", "register:40f0:8", ["const:79c464:8", "const:4:8"]]
+ 0079c464 ["CALL", null, ["callee:00851550:8"]]
- 0079c40c bytes 3bd40294
+ 0079c464 bytes 3bd40294
- 0079c44c ["INT_ADD", "register:40f0:8", ["const:79c44c:8", "const:4:8"]]
- 0079c44c ["CALL", null, ["callee:004939d8:8"]]
+ 0079c4a4 ["INT_ADD", "register:40f0:8", ["const:79c4a4:8", "const:4:8"]]
+ 0079c4a4 ["CALL", null, ["callee:004939d8:8"]]
- 0079c44c bytes 53ddf397
+ 0079c4a4 bytes 4dddf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab7550c172222e0feb5696e76dd65f7"></a>

### [`0079c86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md) → [`0079c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md) FUN_0079c8c4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) · 呼出先 5件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`005a13cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a13cc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 5件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`005a140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a140c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079c898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md#insn-0079c898) · [`0079c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md#insn-0079c8c4) · [`0079c8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md#insn-0079c8d0)
- 新版 [`0079c8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md#insn-0079c8f0) · [`0079c91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md#insn-0079c91c) · [`0079c928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md#insn-0079c928)

~~~diff
- 0079c898 ["INT_ADD", "register:40f0:8", ["const:79c898:8", "const:4:8"]]
- 0079c898 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079c8f0 ["INT_ADD", "register:40f0:8", ["const:79c8f0:8", "const:4:8"]]
+ 0079c8f0 ["CALL", null, ["callee:00c57f60:8"]]
- 0079c898 bytes 7eed1294
+ 0079c8f0 bytes 9ced1294
- 0079c8c4 ["INT_ADD", "register:40f0:8", ["const:79c8c4:8", "const:4:8"]]
- 0079c8c4 ["CALL", null, ["callee:0054079c:8"]]
+ 0079c91c ["INT_ADD", "register:40f0:8", ["const:79c91c:8", "const:4:8"]]
+ 0079c91c ["CALL", null, ["callee:0054079c:8"]]
- 0079c8c4 bytes a68ff697
+ 0079c91c bytes a08ff697
- 0079c8d0 ["INT_ADD", "register:40f0:8", ["const:79c8d0:8", "const:4:8"]]
- 0079c8d0 ["CALL", null, ["callee:005a140c:8"]]
+ 0079c928 ["INT_ADD", "register:40f0:8", ["const:79c928:8", "const:4:8"]]
+ 0079c928 ["CALL", null, ["callee:005a140c:8"]]
- 0079c8d0 bytes bf12f897
+ 0079c928 bytes b912f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25ac501ec8ab3b9bf48b96f347a1b8c1"></a>

### [`0079c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c980.md) → [`0079c9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md) FUN_0079c9d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a1768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1768.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079c99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c980.md#insn-0079c99c)
- 新版 [`0079c9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md#insn-0079c9f4)

~~~diff
- 0079c99c ["INT_ADD", "register:40f0:8", ["const:79c99c:8", "const:4:8"]]
- 0079c99c ["CALL", null, ["callee:005a1768:8"]]
+ 0079c9f4 ["INT_ADD", "register:40f0:8", ["const:79c9f4:8", "const:4:8"]]
+ 0079c9f4 ["CALL", null, ["callee:005a1768:8"]]
- 0079c99c bytes 6313f897
+ 0079c9f4 bytes 5d13f897
~~~


<a id="compare-681b24bc4e6ffb1f94639b83fd877714"></a>

### [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) → [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) FUN_0079cc68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) · 呼出先 10件 [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) [`005a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4280.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`0079cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md)
- 新版 呼出元 1件 [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) · 呼出先 10件 [`005a42ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42ac.md) [`005a42c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42c0.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079cc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md#insn-0079cc7c) · [`0079cc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md#insn-0079cc84) · [`0079cce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md#insn-0079cce8)
- 新版 [`0079ccd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079ccd4) · [`0079ccdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079ccdc) · [`0079cd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079cd40)

~~~diff
- 0079cc7c ["INT_ADD", "register:40f0:8", ["const:79cc7c:8", "const:4:8"]]
- 0079cc7c ["CALL", null, ["callee:005a4548:8"]]
+ 0079ccd4 ["INT_ADD", "register:40f0:8", ["const:79ccd4:8", "const:4:8"]]
+ 0079ccd4 ["CALL", null, ["callee:005a4548:8"]]
- 0079cc7c bytes 231ef897
+ 0079ccd4 bytes 1d1ef897
- 0079cc84 ["INT_ADD", "register:40f0:8", ["const:79cc84:8", "const:4:8"]]
- 0079cc84 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079ccdc ["INT_ADD", "register:40f0:8", ["const:79ccdc:8", "const:4:8"]]
+ 0079ccdc ["CALL", null, ["callee:00c57f80:8"]]
- 0079cc84 bytes 8bec1294
+ 0079ccdc bytes a9ec1294
- 0079cce8 ["INT_ADD", "register:40f0:8", ["const:79cce8:8", "const:4:8"]]
- 0079cce8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079cd40 ["INT_ADD", "register:40f0:8", ["const:79cd40:8", "const:4:8"]]
+ 0079cd40 ["CALL", null, ["callee:00c57f60:8"]]
- 0079cce8 bytes 6aec1294
+ 0079cd40 bytes 88ec1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32334b2e6ad55f04607d700f8852ca04"></a>

### [`0079cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md) → [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md) FUN_0079cfcc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) · 呼出先 5件 [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) · 呼出先 5件 [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079cfc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md#insn-0079cfc8) · [`0079d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md#insn-0079d02c) · [`0079d054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md#insn-0079d054)
- 新版 [`0079d020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d020) · [`0079d084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d084) · [`0079d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d0ac)

~~~diff
- 0079cfc8 ["INT_ADD", "register:40f0:8", ["const:79cfc8:8", "const:4:8"]]
- 0079cfc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d020 ["INT_ADD", "register:40f0:8", ["const:79d020:8", "const:4:8"]]
+ 0079d020 ["CALL", null, ["callee:00c57f80:8"]]
- 0079cfc8 bytes baeb1294
+ 0079d020 bytes d8eb1294
- 0079d02c ["INT_ADD", "register:40f0:8", ["const:79d02c:8", "const:4:8"]]
- 0079d02c ["CALL", null, ["callee:00c57f60:8"]]
+ 0079d084 ["INT_ADD", "register:40f0:8", ["const:79d084:8", "const:4:8"]]
+ 0079d084 ["CALL", null, ["callee:00c57f60:8"]]
- 0079d02c bytes 99eb1294
+ 0079d084 bytes b7eb1294
- 0079d054 ["INT_ADD", "register:40f0:8", ["const:79d054:8", "const:4:8"]]
- 0079d054 ["CALL", null, ["callee:00c580d0:8"]]
+ 0079d0ac ["INT_ADD", "register:40f0:8", ["const:79d0ac:8", "const:4:8"]]
+ 0079d0ac ["CALL", null, ["callee:00c580d0:8"]]
- 0079d054 bytes ebeb1294
+ 0079d0ac bytes 09ec1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd404639da1a58592d3047e2940f0d36"></a>

### [`0079d0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md) → [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) FUN_0079d130

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00797ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md) [`00798e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798e24.md) · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`00798e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md) · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md#insn-0079d120) · [`0079d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md#insn-0079d130) · [`0079d140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d0d8.md#insn-0079d140)
- 新版 [`0079d178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d178) · [`0079d188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d188) · [`0079d198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d198)

~~~diff
- 0079d120 ["INT_ADD", "register:40f0:8", ["const:79d120:8", "const:4:8"]]
- 0079d120 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d178 ["INT_ADD", "register:40f0:8", ["const:79d178:8", "const:4:8"]]
+ 0079d178 ["CALL", null, ["callee:00c57f80:8"]]
- 0079d120 bytes 64eb1294
+ 0079d178 bytes 82eb1294
- 0079d130 ["INT_ADD", "register:40f0:8", ["const:79d130:8", "const:4:8"]]
- 0079d130 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d188 ["INT_ADD", "register:40f0:8", ["const:79d188:8", "const:4:8"]]
+ 0079d188 ["CALL", null, ["callee:00c57f80:8"]]
- 0079d130 bytes 60eb1294
+ 0079d188 bytes 7eeb1294
- 0079d140 ["INT_ADD", "register:40f0:8", ["const:79d140:8", "const:4:8"]]
- 0079d140 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d198 ["INT_ADD", "register:40f0:8", ["const:79d198:8", "const:4:8"]]
+ 0079d198 ["CALL", null, ["callee:00c57f80:8"]]
- 0079d140 bytes 5ceb1294
+ 0079d198 bytes 7aeb1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd8c6622578f3f35996fc1c4114de4b8"></a>

### [`0079d178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md) → [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) FUN_0079d1d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00797ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md) [`0079d178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md) · 呼出先 2件 [`0079d178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) · 呼出先 2件 [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md#insn-0079d194) · [`0079d1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md#insn-0079d1a0) · [`0079d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d178.md#insn-0079d1d4)
- 新版 [`0079d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d1ec) · [`0079d1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d1f8) · [`0079d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d22c)

~~~diff
- 0079d194 ["INT_ADD", "register:40f0:8", ["const:79d194:8", "const:4:8"]]
- 0079d194 ["CALL", null, ["local:b0:8"]]
+ 0079d1ec ["INT_ADD", "register:40f0:8", ["const:79d1ec:8", "const:4:8"]]
+ 0079d1ec ["CALL", null, ["local:b0:8"]]
- 0079d194 bytes f9ffff97
+ 0079d1ec bytes f9ffff97
- 0079d1a0 ["INT_ADD", "register:40f0:8", ["const:79d1a0:8", "const:4:8"]]
- 0079d1a0 ["CALL", null, ["local:b0:8"]]
+ 0079d1f8 ["INT_ADD", "register:40f0:8", ["const:79d1f8:8", "const:4:8"]]
+ 0079d1f8 ["CALL", null, ["local:b0:8"]]
- 0079d1a0 bytes f6ffff97
+ 0079d1f8 bytes f6ffff97
- 0079d1d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d1d4 ["INT_ADD", "register:40f0:8", ["const:79d1d4:8", "const:4:8"]]
- 0079d1d4 ["CALLIND", null, ["register:0:8"]]
+ 0079d22c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d22c ["INT_ADD", "register:40f0:8", ["const:79d22c:8", "const:4:8"]]
+ 0079d22c ["CALLIND", null, ["register:0:8"]]
- 0079d1d4 bytes 00013fd6
+ 0079d22c bytes 00013fd6
~~~


<a id="compare-c621a31a72a950a4f568bd9162047c4e"></a>

### [`0079d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md) → [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) FUN_0079d240

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00797ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797ad8.md) [`0079d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md) · 呼出先 2件 [`0079d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) · 呼出先 2件 [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md#insn-0079d204) · [`0079d210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md#insn-0079d210) · [`0079d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d1e8.md#insn-0079d244)
- 新版 [`0079d25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d25c) · [`0079d268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d268) · [`0079d29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d29c)

~~~diff
- 0079d204 ["INT_ADD", "register:40f0:8", ["const:79d204:8", "const:4:8"]]
- 0079d204 ["CALL", null, ["local:b0:8"]]
+ 0079d25c ["INT_ADD", "register:40f0:8", ["const:79d25c:8", "const:4:8"]]
+ 0079d25c ["CALL", null, ["local:b0:8"]]
- 0079d204 bytes f9ffff97
+ 0079d25c bytes f9ffff97
- 0079d210 ["INT_ADD", "register:40f0:8", ["const:79d210:8", "const:4:8"]]
- 0079d210 ["CALL", null, ["local:b0:8"]]
+ 0079d268 ["INT_ADD", "register:40f0:8", ["const:79d268:8", "const:4:8"]]
+ 0079d268 ["CALL", null, ["local:b0:8"]]
- 0079d210 bytes f6ffff97
+ 0079d268 bytes f6ffff97
- 0079d244 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d244 ["INT_ADD", "register:40f0:8", ["const:79d244:8", "const:4:8"]]
- 0079d244 ["CALLIND", null, ["register:0:8"]]
+ 0079d29c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d29c ["INT_ADD", "register:40f0:8", ["const:79d29c:8", "const:4:8"]]
+ 0079d29c ["CALLIND", null, ["register:0:8"]]
- 0079d244 bytes 00013fd6
+ 0079d29c bytes 00013fd6
~~~


<a id="compare-3293beb594d3d8f84c2e430d1e301f66"></a>

### [`0079d258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d258.md) → [`0079d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md) FUN_0079d2b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00797b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b84.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00797bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d258.md#insn-0079d2c4) · [`0079d2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d258.md#insn-0079d2d4) · [`0079d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d258.md#insn-0079d2f4)
- 新版 [`0079d31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d31c) · [`0079d32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d32c) · [`0079d34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d34c)

~~~diff
- 0079d2c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d2c4 ["INT_ADD", "register:40f0:8", ["const:79d2c4:8", "const:4:8"]]
- 0079d2c4 ["CALLIND", null, ["register:0:8"]]
+ 0079d31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d31c ["INT_ADD", "register:40f0:8", ["const:79d31c:8", "const:4:8"]]
+ 0079d31c ["CALLIND", null, ["register:0:8"]]
- 0079d2c4 bytes 00013fd6
+ 0079d31c bytes 00013fd6
- 0079d2d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d2d4 ["INT_ADD", "register:40f0:8", ["const:79d2d4:8", "const:4:8"]]
- 0079d2d4 ["CALLIND", null, ["register:0:8"]]
+ 0079d32c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d32c ["INT_ADD", "register:40f0:8", ["const:79d32c:8", "const:4:8"]]
+ 0079d32c ["CALLIND", null, ["register:0:8"]]
- 0079d2d4 bytes 00013fd6
+ 0079d32c bytes 00013fd6
- 0079d2f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d2f4 ["INT_ADD", "register:40f0:8", ["const:79d2f4:8", "const:4:8"]]
- 0079d2f4 ["CALLIND", null, ["register:0:8"]]
+ 0079d34c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d34c ["INT_ADD", "register:40f0:8", ["const:79d34c:8", "const:4:8"]]
+ 0079d34c ["CALLIND", null, ["register:0:8"]]
- 0079d2f4 bytes 00013fd6
+ 0079d34c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b60f14ab87725632c667441658b2b9e"></a>

### [`0079d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d470.md) → [`0079d4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md) FUN_0079d4c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0079d5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0079d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d470.md#insn-0079d4d8) · [`0079d574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d470.md#insn-0079d574) · [`0079d590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d470.md#insn-0079d590)
- 新版 [`0079d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d530) · [`0079d5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d5cc) · [`0079d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d5e8)

~~~diff
- 0079d4d8 ["INT_ADD", "register:40f0:8", ["const:79d4d8:8", "const:4:8"]]
- 0079d4d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079d530 ["INT_ADD", "register:40f0:8", ["const:79d530:8", "const:4:8"]]
+ 0079d530 ["CALL", null, ["callee:00c57f60:8"]]
- 0079d4d8 bytes 6eea1294
+ 0079d530 bytes 8cea1294
- 0079d574 ["INT_ADD", "register:40f0:8", ["const:79d574:8", "const:4:8"]]
- 0079d574 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d5cc ["INT_ADD", "register:40f0:8", ["const:79d5cc:8", "const:4:8"]]
+ 0079d5cc ["CALL", null, ["callee:00c57f80:8"]]
- 0079d574 bytes 4fea1294
+ 0079d5cc bytes 6dea1294
- 0079d590 ["INT_ADD", "register:40f0:8", ["const:79d590:8", "const:4:8"]]
- 0079d590 ["CALL", null, ["callee:00c57f80:8"]]
+ 0079d5e8 ["INT_ADD", "register:40f0:8", ["const:79d5e8:8", "const:4:8"]]
+ 0079d5e8 ["CALL", null, ["callee:00c57f80:8"]]
- 0079d590 bytes 48ea1294
+ 0079d5e8 bytes 66ea1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3248938caf85b8df4497c9f08349bc94"></a>

### [`0079d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md) → [`0079d624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md) FUN_0079d624

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a608.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md#insn-0079d680) · [`0079d6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md#insn-0079d6bc) · [`0079d734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md#insn-0079d734)
- 新版 [`0079d6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d6d8) · [`0079d714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d714) · [`0079d78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d78c)

~~~diff
- 0079d680 ["INT_ADD", "register:40f0:8", ["const:79d680:8", "const:4:8"]]
- 0079d680 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079d6d8 ["INT_ADD", "register:40f0:8", ["const:79d6d8:8", "const:4:8"]]
+ 0079d6d8 ["CALL", null, ["callee:00c57f60:8"]]
- 0079d680 bytes 04ea1294
+ 0079d6d8 bytes 22ea1294
- 0079d6bc ["INT_ADD", "register:40f0:8", ["const:79d6bc:8", "const:4:8"]]
- 0079d6bc ["CALL", null, ["callee:00c58010:8"]]
+ 0079d714 ["INT_ADD", "register:40f0:8", ["const:79d714:8", "const:4:8"]]
+ 0079d714 ["CALL", null, ["callee:00c58010:8"]]
- 0079d6bc bytes 21ea1294
+ 0079d714 bytes 3fea1294
- 0079d734 ["INT_ADD", "register:40f0:8", ["const:79d734:8", "const:4:8"]]
- 0079d734 ["CALL", null, ["callee:00c58010:8"]]
+ 0079d78c ["INT_ADD", "register:40f0:8", ["const:79d78c:8", "const:4:8"]]
+ 0079d78c ["CALL", null, ["callee:00c58010:8"]]
- 0079d734 bytes 03ea1294
+ 0079d78c bytes 21ea1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da79ffe19f1a820d6c823b12144feda3"></a>

### [`0079d8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8ec.md) → [`0079d944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md) FUN_0079d944

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8ec.md#insn-0079d960)
- 新版 [`0079d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md#insn-0079d9b8)

~~~diff
- 0079d960 ["INT_ADD", "register:40f0:8", ["const:79d960:8", "const:4:8"]]
- 0079d960 ["CALL", null, ["callee:00459db4:8"]]
+ 0079d9b8 ["INT_ADD", "register:40f0:8", ["const:79d9b8:8", "const:4:8"]]
+ 0079d9b8 ["CALL", null, ["callee:00459db4:8"]]
- 0079d960 bytes 05f1f297
+ 0079d9b8 bytes fff0f297
~~~


<a id="compare-a2e44e0c1c350b558a5a729652518850"></a>

### [`0079db98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db98.md) → [`0079dbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbf0.md) FUN_0079dbf0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079dc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db98.md#insn-0079dc0c)
- 新版 [`0079dc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbf0.md#insn-0079dc64)

~~~diff
- 0079dc0c ["INT_ADD", "register:40f0:8", ["const:79dc0c:8", "const:4:8"]]
- 0079dc0c ["CALL", null, ["callee:00459db4:8"]]
+ 0079dc64 ["INT_ADD", "register:40f0:8", ["const:79dc64:8", "const:4:8"]]
+ 0079dc64 ["CALL", null, ["callee:00459db4:8"]]
- 0079dc0c bytes 5af0f297
+ 0079dc64 bytes 54f0f297
~~~


<a id="compare-ea3287f03b9cfe570570dd08fce86c20"></a>

### [`0079dd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dd14.md) → [`0079dd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd6c.md) FUN_0079dd6c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079dd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dd14.md#insn-0079dd88)
- 新版 [`0079dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd6c.md#insn-0079dde0)

~~~diff
- 0079dd88 ["INT_ADD", "register:40f0:8", ["const:79dd88:8", "const:4:8"]]
- 0079dd88 ["CALL", null, ["callee:00459db4:8"]]
+ 0079dde0 ["INT_ADD", "register:40f0:8", ["const:79dde0:8", "const:4:8"]]
+ 0079dde0 ["CALL", null, ["callee:00459db4:8"]]
- 0079dd88 bytes fbeff297
+ 0079dde0 bytes f5eff297
~~~


<a id="compare-ad87743b945cfec290e369ffdd924b74"></a>

### [`0079e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e2e0.md) → [`0079e338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e338.md) FUN_0079e338

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e2e0.md#insn-0079e320) · [`0079e34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e2e0.md#insn-0079e34c)
- 新版 [`0079e378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e338.md#insn-0079e378) · [`0079e3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e338.md#insn-0079e3a4)

~~~diff
- 0079e320 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e320 ["INT_ADD", "register:40f0:8", ["const:79e320:8", "const:4:8"]]
- 0079e320 ["CALLIND", null, ["register:0:8"]]
+ 0079e378 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e378 ["INT_ADD", "register:40f0:8", ["const:79e378:8", "const:4:8"]]
+ 0079e378 ["CALLIND", null, ["register:0:8"]]
- 0079e320 bytes 00013fd6
+ 0079e378 bytes 00013fd6
- 0079e34c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e34c ["INT_ADD", "register:40f0:8", ["const:79e34c:8", "const:4:8"]]
- 0079e34c ["CALLIND", null, ["register:0:8"]]
+ 0079e3a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e3a4 ["INT_ADD", "register:40f0:8", ["const:79e3a4:8", "const:4:8"]]
+ 0079e3a4 ["CALLIND", null, ["register:0:8"]]
- 0079e34c bytes 00013fd6
+ 0079e3a4 bytes 00013fd6
~~~


<a id="compare-8a245e9a9c6d550919a53210832c629c"></a>

### [`0079e360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e360.md) → [`0079e3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md) FUN_0079e3b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e360.md#insn-0079e398) · [`0079e3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e360.md#insn-0079e3b4) · [`0079e3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e360.md#insn-0079e3cc)
- 新版 [`0079e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e3f0) · [`0079e40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e40c) · [`0079e424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e424)

~~~diff
- 0079e398 ["INT_ADD", "register:40f0:8", ["const:79e398:8", "const:4:8"]]
- 0079e398 ["CALL", null, ["callee:00c53d70:8"]]
+ 0079e3f0 ["INT_ADD", "register:40f0:8", ["const:79e3f0:8", "const:4:8"]]
+ 0079e3f0 ["CALL", null, ["callee:00c53d70:8"]]
- 0079e398 bytes 4ed61294
+ 0079e3f0 bytes 60d61294
- 0079e3b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e3b4 ["INT_ADD", "register:40f0:8", ["const:79e3b4:8", "const:4:8"]]
- 0079e3b4 ["CALLIND", null, ["register:0:8"]]
+ 0079e40c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e40c ["INT_ADD", "register:40f0:8", ["const:79e40c:8", "const:4:8"]]
+ 0079e40c ["CALLIND", null, ["register:0:8"]]
- 0079e3b4 bytes 00013fd6
+ 0079e40c bytes 00013fd6
- 0079e3cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e3cc ["INT_ADD", "register:40f0:8", ["const:79e3cc:8", "const:4:8"]]
- 0079e3cc ["CALLIND", null, ["register:0:8"]]
+ 0079e424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e424 ["INT_ADD", "register:40f0:8", ["const:79e424:8", "const:4:8"]]
+ 0079e424 ["CALLIND", null, ["register:0:8"]]
- 0079e3cc bytes 00013fd6
+ 0079e424 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faa580b5f06f231f97dde2abdd1e48d1"></a>

### [`0079e4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4a4.md) → [`0079e4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md) FUN_0079e4fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4a4.md#insn-0079e4c0) · [`0079e4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4a4.md#insn-0079e4e0)
- 新版 [`0079e518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md#insn-0079e518) · [`0079e538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md#insn-0079e538)

~~~diff
- 0079e4c0 ["INT_ADD", "register:40f0:8", ["const:79e4c0:8", "const:4:8"]]
- 0079e4c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0079e518 ["INT_ADD", "register:40f0:8", ["const:79e518:8", "const:4:8"]]
+ 0079e518 ["CALL", null, ["callee:00c53da0:8"]]
- 0079e4c0 bytes 10d61294
+ 0079e518 bytes 22d61294
- 0079e4e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e4e0 ["INT_ADD", "register:40f0:8", ["const:79e4e0:8", "const:4:8"]]
- 0079e4e0 ["CALLIND", null, ["register:0:8"]]
+ 0079e538 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e538 ["INT_ADD", "register:40f0:8", ["const:79e538:8", "const:4:8"]]
+ 0079e538 ["CALLIND", null, ["register:0:8"]]
- 0079e4e0 bytes 00013fd6
+ 0079e538 bytes 00013fd6
~~~


<a id="compare-354cace02520f10f3893988d5b2704ed"></a>

### [`0079e6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e6c8.md) → [`0079e720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e720.md) FUN_0079e720

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e6c8.md#insn-0079e704)
- 新版 [`0079e75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e720.md#insn-0079e75c)

~~~diff
- 0079e704 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e704 ["INT_ADD", "register:40f0:8", ["const:79e704:8", "const:4:8"]]
- 0079e704 ["CALLIND", null, ["register:0:8"]]
+ 0079e75c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e75c ["INT_ADD", "register:40f0:8", ["const:79e75c:8", "const:4:8"]]
+ 0079e75c ["CALLIND", null, ["register:0:8"]]
- 0079e704 bytes 00013fd6
+ 0079e75c bytes 00013fd6
~~~


<a id="compare-9853ddfcdae5ae9236ed4b72f71c2c1b"></a>

### [`0079e718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e718.md) → [`0079e770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e770.md) FUN_0079e770

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e718.md#insn-0079e734)
- 新版 [`0079e78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e770.md#insn-0079e78c)

~~~diff
- 0079e734 ["INT_ADD", "register:40f0:8", ["const:79e734:8", "const:4:8"]]
- 0079e734 ["CALL", null, ["callee:00459db4:8"]]
+ 0079e78c ["INT_ADD", "register:40f0:8", ["const:79e78c:8", "const:4:8"]]
+ 0079e78c ["CALL", null, ["callee:00459db4:8"]]
- 0079e734 bytes 90edf297
+ 0079e78c bytes 8aedf297
~~~


<a id="compare-9139de80f03f4722cc4d5a74f4c392fe"></a>

### [`0079ec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ec8c.md) → [`0079ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md) FUN_0079ece4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079eccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ec8c.md#insn-0079eccc) · [`0079ecf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ec8c.md#insn-0079ecf8)
- 新版 [`0079ed24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md#insn-0079ed24) · [`0079ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md#insn-0079ed50)

~~~diff
- 0079eccc ["COPY", "register:0:8", ["register:4040:8"]]
- 0079eccc ["INT_ADD", "register:40f0:8", ["const:79eccc:8", "const:4:8"]]
- 0079eccc ["CALLIND", null, ["register:0:8"]]
+ 0079ed24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ed24 ["INT_ADD", "register:40f0:8", ["const:79ed24:8", "const:4:8"]]
+ 0079ed24 ["CALLIND", null, ["register:0:8"]]
- 0079eccc bytes 00013fd6
+ 0079ed24 bytes 00013fd6
- 0079ecf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ecf8 ["INT_ADD", "register:40f0:8", ["const:79ecf8:8", "const:4:8"]]
- 0079ecf8 ["CALLIND", null, ["register:0:8"]]
+ 0079ed50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ed50 ["INT_ADD", "register:40f0:8", ["const:79ed50:8", "const:4:8"]]
+ 0079ed50 ["CALLIND", null, ["register:0:8"]]
- 0079ecf8 bytes 00013fd6
+ 0079ed50 bytes 00013fd6
~~~


<a id="compare-b3d906609443dbb19497ba0d12c06155"></a>

### [`0079ed0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ed0c.md) → [`0079ed64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md) FUN_0079ed64

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079ed44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ed0c.md#insn-0079ed44) · [`0079ed68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ed0c.md#insn-0079ed68) · [`0079ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ed0c.md#insn-0079ed80)
- 新版 [`0079ed9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079ed9c) · [`0079edc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079edc0) · [`0079edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079edd8)

~~~diff
- 0079ed44 ["INT_ADD", "register:40f0:8", ["const:79ed44:8", "const:4:8"]]
- 0079ed44 ["CALL", null, ["callee:00c53d70:8"]]
+ 0079ed9c ["INT_ADD", "register:40f0:8", ["const:79ed9c:8", "const:4:8"]]
+ 0079ed9c ["CALL", null, ["callee:00c53d70:8"]]
- 0079ed44 bytes e3d31294
+ 0079ed9c bytes f5d31294
- 0079ed68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ed68 ["INT_ADD", "register:40f0:8", ["const:79ed68:8", "const:4:8"]]
- 0079ed68 ["CALLIND", null, ["register:0:8"]]
+ 0079edc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079edc0 ["INT_ADD", "register:40f0:8", ["const:79edc0:8", "const:4:8"]]
+ 0079edc0 ["CALLIND", null, ["register:0:8"]]
- 0079ed68 bytes 00013fd6
+ 0079edc0 bytes 00013fd6
- 0079ed80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ed80 ["INT_ADD", "register:40f0:8", ["const:79ed80:8", "const:4:8"]]
- 0079ed80 ["CALLIND", null, ["register:0:8"]]
+ 0079edd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079edd8 ["INT_ADD", "register:40f0:8", ["const:79edd8:8", "const:4:8"]]
+ 0079edd8 ["CALLIND", null, ["register:0:8"]]
- 0079ed80 bytes 00013fd6
+ 0079edd8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a688ba9b2203ead38efbce93b9890f"></a>

### [`0079ee38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee38.md) → [`0079ee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md) FUN_0079ee90

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079ee54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee38.md#insn-0079ee54) · [`0079ee74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee38.md#insn-0079ee74)
- 新版 [`0079eeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md#insn-0079eeac) · [`0079eecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md#insn-0079eecc)

~~~diff
- 0079ee54 ["INT_ADD", "register:40f0:8", ["const:79ee54:8", "const:4:8"]]
- 0079ee54 ["CALL", null, ["callee:00c53da0:8"]]
+ 0079eeac ["INT_ADD", "register:40f0:8", ["const:79eeac:8", "const:4:8"]]
+ 0079eeac ["CALL", null, ["callee:00c53da0:8"]]
- 0079ee54 bytes abd31294
+ 0079eeac bytes bdd31294
- 0079ee74 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ee74 ["INT_ADD", "register:40f0:8", ["const:79ee74:8", "const:4:8"]]
- 0079ee74 ["CALLIND", null, ["register:0:8"]]
+ 0079eecc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079eecc ["INT_ADD", "register:40f0:8", ["const:79eecc:8", "const:4:8"]]
+ 0079eecc ["CALLIND", null, ["register:0:8"]]
- 0079ee74 bytes 00013fd6
+ 0079eecc bytes 00013fd6
~~~


<a id="compare-ab265d32e19ee77de4267d4c62e0c5c1"></a>

### [`0079f05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f05c.md) → [`0079f0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f0b4.md) FUN_0079f0b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f05c.md#insn-0079f098)
- 新版 [`0079f0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f0b4.md#insn-0079f0f0)

~~~diff
- 0079f098 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f098 ["INT_ADD", "register:40f0:8", ["const:79f098:8", "const:4:8"]]
- 0079f098 ["CALLIND", null, ["register:0:8"]]
+ 0079f0f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f0f0 ["INT_ADD", "register:40f0:8", ["const:79f0f0:8", "const:4:8"]]
+ 0079f0f0 ["CALLIND", null, ["register:0:8"]]
- 0079f098 bytes 00013fd6
+ 0079f0f0 bytes 00013fd6
~~~


<a id="compare-121d04bd9085cade1154497680c4cb76"></a>

### [`0079f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f0ac.md) → [`0079f104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f104.md) FUN_0079f104

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f0ac.md#insn-0079f0c8)
- 新版 [`0079f120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f104.md#insn-0079f120)

~~~diff
- 0079f0c8 ["INT_ADD", "register:40f0:8", ["const:79f0c8:8", "const:4:8"]]
- 0079f0c8 ["CALL", null, ["callee:00459db4:8"]]
+ 0079f120 ["INT_ADD", "register:40f0:8", ["const:79f120:8", "const:4:8"]]
+ 0079f120 ["CALL", null, ["callee:00459db4:8"]]
- 0079f0c8 bytes 2bebf297
+ 0079f120 bytes 25ebf297
~~~


<a id="compare-7084ec38a4f56f0318e482632c130c98"></a>

### [`0079f620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f620.md) → [`0079f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md) FUN_0079f678

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f620.md#insn-0079f660) · [`0079f68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f620.md#insn-0079f68c)
- 新版 [`0079f6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md#insn-0079f6b8) · [`0079f6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md#insn-0079f6e4)

~~~diff
- 0079f660 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f660 ["INT_ADD", "register:40f0:8", ["const:79f660:8", "const:4:8"]]
- 0079f660 ["CALLIND", null, ["register:0:8"]]
+ 0079f6b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f6b8 ["INT_ADD", "register:40f0:8", ["const:79f6b8:8", "const:4:8"]]
+ 0079f6b8 ["CALLIND", null, ["register:0:8"]]
- 0079f660 bytes 00013fd6
+ 0079f6b8 bytes 00013fd6
- 0079f68c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f68c ["INT_ADD", "register:40f0:8", ["const:79f68c:8", "const:4:8"]]
- 0079f68c ["CALLIND", null, ["register:0:8"]]
+ 0079f6e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f6e4 ["INT_ADD", "register:40f0:8", ["const:79f6e4:8", "const:4:8"]]
+ 0079f6e4 ["CALLIND", null, ["register:0:8"]]
- 0079f68c bytes 00013fd6
+ 0079f6e4 bytes 00013fd6
~~~


<a id="compare-90cfc234925b99c3bc2df8a627d8b54d"></a>

### [`0079f6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f6a0.md) → [`0079f6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md) FUN_0079f6f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f6a0.md#insn-0079f6d8) · [`0079f6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f6a0.md#insn-0079f6f4) · [`0079f70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f6a0.md#insn-0079f70c)
- 新版 [`0079f730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md#insn-0079f730) · [`0079f74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md#insn-0079f74c) · [`0079f764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md#insn-0079f764)

~~~diff
- 0079f6d8 ["INT_ADD", "register:40f0:8", ["const:79f6d8:8", "const:4:8"]]
- 0079f6d8 ["CALL", null, ["callee:00c53d70:8"]]
+ 0079f730 ["INT_ADD", "register:40f0:8", ["const:79f730:8", "const:4:8"]]
+ 0079f730 ["CALL", null, ["callee:00c53d70:8"]]
- 0079f6d8 bytes 7ed11294
+ 0079f730 bytes 90d11294
- 0079f6f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f6f4 ["INT_ADD", "register:40f0:8", ["const:79f6f4:8", "const:4:8"]]
- 0079f6f4 ["CALLIND", null, ["register:0:8"]]
+ 0079f74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f74c ["INT_ADD", "register:40f0:8", ["const:79f74c:8", "const:4:8"]]
+ 0079f74c ["CALLIND", null, ["register:0:8"]]
- 0079f6f4 bytes 00013fd6
+ 0079f74c bytes 00013fd6
- 0079f70c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f70c ["INT_ADD", "register:40f0:8", ["const:79f70c:8", "const:4:8"]]
- 0079f70c ["CALLIND", null, ["register:0:8"]]
+ 0079f764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f764 ["INT_ADD", "register:40f0:8", ["const:79f764:8", "const:4:8"]]
+ 0079f764 ["CALLIND", null, ["register:0:8"]]
- 0079f70c bytes 00013fd6
+ 0079f764 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85c4e91590c430e4698c577cef267a6"></a>

### [`0079f7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f7e4.md) → [`0079f83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md) FUN_0079f83c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f7e4.md#insn-0079f800) · [`0079f820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f7e4.md#insn-0079f820)
- 新版 [`0079f858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md#insn-0079f858) · [`0079f878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md#insn-0079f878)

~~~diff
- 0079f800 ["INT_ADD", "register:40f0:8", ["const:79f800:8", "const:4:8"]]
- 0079f800 ["CALL", null, ["callee:00c53da0:8"]]
+ 0079f858 ["INT_ADD", "register:40f0:8", ["const:79f858:8", "const:4:8"]]
+ 0079f858 ["CALL", null, ["callee:00c53da0:8"]]
- 0079f800 bytes 40d11294
+ 0079f858 bytes 52d11294
- 0079f820 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f820 ["INT_ADD", "register:40f0:8", ["const:79f820:8", "const:4:8"]]
- 0079f820 ["CALLIND", null, ["register:0:8"]]
+ 0079f878 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f878 ["INT_ADD", "register:40f0:8", ["const:79f878:8", "const:4:8"]]
+ 0079f878 ["CALLIND", null, ["register:0:8"]]
- 0079f820 bytes 00013fd6
+ 0079f878 bytes 00013fd6
~~~


<a id="compare-5fb50bd1d4dcbab6d9c42e08447b5f6f"></a>

### [`0079fa08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fa08.md) → [`0079fa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md) FUN_0079fa60

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079fa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fa08.md#insn-0079fa44)
- 新版 [`0079fa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md#insn-0079fa9c)

~~~diff
- 0079fa44 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079fa44 ["INT_ADD", "register:40f0:8", ["const:79fa44:8", "const:4:8"]]
- 0079fa44 ["CALLIND", null, ["register:0:8"]]
+ 0079fa9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079fa9c ["INT_ADD", "register:40f0:8", ["const:79fa9c:8", "const:4:8"]]
+ 0079fa9c ["CALLIND", null, ["register:0:8"]]
- 0079fa44 bytes 00013fd6
+ 0079fa9c bytes 00013fd6
~~~


<a id="compare-75050254b00862f24bad848a9311572f"></a>

### [`0079fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fa58.md) → [`0079fab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md) FUN_0079fab0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079fa74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fa58.md#insn-0079fa74)
- 新版 [`0079facc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md#insn-0079facc)

~~~diff
- 0079fa74 ["INT_ADD", "register:40f0:8", ["const:79fa74:8", "const:4:8"]]
- 0079fa74 ["CALL", null, ["callee:00459db4:8"]]
+ 0079facc ["INT_ADD", "register:40f0:8", ["const:79facc:8", "const:4:8"]]
+ 0079facc ["CALL", null, ["callee:00459db4:8"]]
- 0079fa74 bytes c0e8f297
+ 0079facc bytes bae8f297
~~~


<a id="compare-f1409ed22f018cc2a52c26ca5987a388"></a>

### [`0079fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md) → [`0079fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md) FUN_0079fea0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00797b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b74.md) · 呼出先 5件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md) [`00481240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md)
- 新版 呼出元 1件 [`00797bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bcc.md) · 呼出先 5件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`00481168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481168.md) [`00481280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md#insn-0079fe88) · [`0079feb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md#insn-0079feb8) · [`0079fec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md#insn-0079fec4)
- 新版 [`0079fee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md#insn-0079fee0) · [`0079ff10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md#insn-0079ff10) · [`0079ff1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md#insn-0079ff1c)

~~~diff
- 0079fe88 ["INT_ADD", "register:40f0:8", ["const:79fe88:8", "const:4:8"]]
- 0079fe88 ["CALL", null, ["callee:00480bd0:8"]]
+ 0079fee0 ["INT_ADD", "register:40f0:8", ["const:79fee0:8", "const:4:8"]]
+ 0079fee0 ["CALL", null, ["callee:00480bd0:8"]]
- 0079fe88 bytes 4283f397
+ 0079fee0 bytes 3c83f397
- 0079feb8 ["INT_ADD", "register:40f0:8", ["const:79feb8:8", "const:4:8"]]
- 0079feb8 ["CALL", null, ["callee:00481168:8"]]
+ 0079ff10 ["INT_ADD", "register:40f0:8", ["const:79ff10:8", "const:4:8"]]
+ 0079ff10 ["CALL", null, ["callee:00481168:8"]]
- 0079feb8 bytes 9c84f397
+ 0079ff10 bytes 9684f397
- 0079fec4 ["INT_ADD", "register:40f0:8", ["const:79fec4:8", "const:4:8"]]
- 0079fec4 ["CALL", null, ["callee:00480e68:8"]]
+ 0079ff1c ["INT_ADD", "register:40f0:8", ["const:79ff1c:8", "const:4:8"]]
+ 0079ff1c ["CALL", null, ["callee:00480e68:8"]]
- 0079fec4 bytes d983f397
+ 0079ff1c bytes d383f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28759137faaa904b934a950d74b3bc0a"></a>

### [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) → [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) FUN_007a008c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00797b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797b7c.md) · 呼出先 17件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`004807cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md)
- 新版 呼出元 1件 [`00797bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bd4.md) · 呼出先 17件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`0048080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/0048080c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md#insn-007a0074) · [`007a00a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md#insn-007a00a8) · [`007a00b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md#insn-007a00b8)
- 新版 [`007a00cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md#insn-007a00cc) · [`007a0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md#insn-007a0100) · [`007a0110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md#insn-007a0110)

~~~diff
- 007a0074 ["INT_ADD", "register:40f0:8", ["const:7a0074:8", "const:4:8"]]
- 007a0074 ["CALL", null, ["callee:005a4548:8"]]
+ 007a00cc ["INT_ADD", "register:40f0:8", ["const:7a00cc:8", "const:4:8"]]
+ 007a00cc ["CALL", null, ["callee:005a4548:8"]]
- 007a0074 bytes 2511f897
+ 007a00cc bytes 1f11f897
- 007a00a8 ["INT_ADD", "register:40f0:8", ["const:7a00a8:8", "const:4:8"]]
- 007a00a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a0100 ["INT_ADD", "register:40f0:8", ["const:7a0100:8", "const:4:8"]]
+ 007a0100 ["CALL", null, ["callee:00c57f80:8"]]
- 007a00a8 bytes 82df1294
+ 007a0100 bytes a0df1294
- 007a00b8 ["INT_ADD", "register:40f0:8", ["const:7a00b8:8", "const:4:8"]]
- 007a00b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a0110 ["INT_ADD", "register:40f0:8", ["const:7a0110:8", "const:4:8"]]
+ 007a0110 ["CALL", null, ["callee:00c57f80:8"]]
- 007a00b8 bytes 7edf1294
+ 007a0110 bytes 9cdf1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2881ef69a02bdbb6181b821706358483"></a>

### [`007a0708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md) → [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) FUN_007a0760

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`007a2004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a2/007a2004.md) [`007a3708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a3/007a3708.md) [`007a41dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a4/007a41dc.md) [`007a5240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a5/007a5240.md) [`007a6128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a6/007a6128.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 9件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a3760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a3760.md) [`007a4234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a4/007a4234.md) [`007a5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5298.md) [`007a6180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a6/007a6180.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0708.md#insn-007a0724)
- 新版 [`007a077c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md#insn-007a077c)

~~~diff
- 007a0724 ["INT_ADD", "register:40f0:8", ["const:7a0724:8", "const:4:8"]]
- 007a0724 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a077c ["INT_ADD", "register:40f0:8", ["const:7a077c:8", "const:4:8"]]
+ 007a077c ["CALL", null, ["callee:00c57f80:8"]]
- 007a0724 bytes e3dd1294
+ 007a077c bytes 01de1294
~~~


<a id="compare-64dd72b8a829d22221c59e56edd4fcb0"></a>

### [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md) → [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md) FUN_007a07dc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00798060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798060.md) [`00798214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798214.md) · 呼出先 10件 [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 2件 [`007980b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md) [`0079826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md) · 呼出先 10件 [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b0dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md#insn-007a0848) · [`007a0864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md#insn-007a0864) · [`007a0884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md#insn-007a0884)
- 新版 [`007a08a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08a0) · [`007a08bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08bc) · [`007a08dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08dc)

~~~diff
- 007a0848 ["INT_ADD", "register:40f0:8", ["const:7a0848:8", "const:4:8"]]
- 007a0848 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a08a0 ["INT_ADD", "register:40f0:8", ["const:7a08a0:8", "const:4:8"]]
+ 007a08a0 ["CALL", null, ["callee:00c57f60:8"]]
- 007a0848 bytes 92dd1294
+ 007a08a0 bytes b0dd1294
- 007a0864 ["INT_ADD", "register:40f0:8", ["const:7a0864:8", "const:4:8"]]
- 007a0864 ["CALL", null, ["callee:00c580d0:8"]]
+ 007a08bc ["INT_ADD", "register:40f0:8", ["const:7a08bc:8", "const:4:8"]]
+ 007a08bc ["CALL", null, ["callee:00c580d0:8"]]
- 007a0864 bytes e7dd1294
+ 007a08bc bytes 05de1294
- 007a0884 ["INT_ADD", "register:40f0:8", ["const:7a0884:8", "const:4:8"]]
- 007a0884 ["CALL", null, ["callee:007a0b08:8"]]
+ 007a08dc ["INT_ADD", "register:40f0:8", ["const:7a08dc:8", "const:4:8"]]
+ 007a08dc ["CALL", null, ["callee:007a0b08:8"]]
- 007a0884 bytes 8b000094
+ 007a08dc bytes 8b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5065f803c9b2b17fdad6ef296b5df77"></a>

### [`007a0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md) → [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) FUN_007a0b08

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md) [`007a0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00737c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737c74.md) [`007a0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00737ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00737/00737ccc.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md#insn-007a0b54) · [`007a0c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md#insn-007a0c20) · [`007a0c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0ab0.md#insn-007a0c54)
- 新版 [`007a0bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0bac) · [`007a0c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0c78) · [`007a0cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0cac)

~~~diff
- 007a0b54 ["INT_ADD", "register:40f0:8", ["const:7a0b54:8", "const:4:8"]]
- 007a0b54 ["CALL", null, ["callee:00737ccc:8"]]
+ 007a0bac ["INT_ADD", "register:40f0:8", ["const:7a0bac:8", "const:4:8"]]
+ 007a0bac ["CALL", null, ["callee:00737ccc:8"]]
- 007a0b54 bytes 485cfe97
+ 007a0bac bytes 485cfe97
- 007a0c20 ["INT_ADD", "register:40f0:8", ["const:7a0c20:8", "const:4:8"]]
- 007a0c20 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a0c78 ["INT_ADD", "register:40f0:8", ["const:7a0c78:8", "const:4:8"]]
+ 007a0c78 ["CALL", null, ["callee:00c57f60:8"]]
- 007a0c20 bytes 9cdc1294
+ 007a0c78 bytes badc1294
- 007a0c54 ["INT_ADD", "register:40f0:8", ["const:7a0c54:8", "const:4:8"]]
- 007a0c54 ["CALL", null, ["callee:00c580d0:8"]]
+ 007a0cac ["INT_ADD", "register:40f0:8", ["const:7a0cac:8", "const:4:8"]]
+ 007a0cac ["CALL", null, ["callee:00c580d0:8"]]
- 007a0c54 bytes ebdc1294
+ 007a0cac bytes 09dd1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e786f06db1678a0c9418d56ef0ced181"></a>

### [`007a0fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md) → [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) FUN_007a0ff8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c3a0.md) · 呼出先 8件 [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`0079cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md) [`007a1c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md) [`007a1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1e6c.md)
- 新版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 8件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md) [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md#insn-007a0fdc) · [`007a0ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md#insn-007a0ffc) · [`007a1020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0fa0.md#insn-007a1020)
- 新版 [`007a1034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1034) · [`007a1054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1054) · [`007a1078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1078)

~~~diff
- 007a0fdc ["INT_ADD", "register:40f0:8", ["const:7a0fdc:8", "const:4:8"]]
- 007a0fdc ["CALL", null, ["callee:0059769c:8"]]
+ 007a1034 ["INT_ADD", "register:40f0:8", ["const:7a1034:8", "const:4:8"]]
+ 007a1034 ["CALL", null, ["callee:0059769c:8"]]
- 007a0fdc bytes a0d9f797
+ 007a1034 bytes 9ad9f797
- 007a0ffc ["INT_ADD", "register:40f0:8", ["const:7a0ffc:8", "const:4:8"]]
- 007a0ffc ["CALL", null, ["callee:00597e88:8"]]
+ 007a1054 ["INT_ADD", "register:40f0:8", ["const:7a1054:8", "const:4:8"]]
+ 007a1054 ["CALL", null, ["callee:00597e88:8"]]
- 007a0ffc bytes 93dbf797
+ 007a1054 bytes 8ddbf797
- 007a1020 ["INT_ADD", "register:40f0:8", ["const:7a1020:8", "const:4:8"]]
- 007a1020 ["CALL", null, ["callee:00c58500:8"]]
+ 007a1078 ["INT_ADD", "register:40f0:8", ["const:7a1078:8", "const:4:8"]]
+ 007a1078 ["CALL", null, ["callee:00c58500:8"]]
- 007a1020 bytes 04dd1294
+ 007a1078 bytes 22dd1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40aa6892607c3714a4f76d452eb8873"></a>

### [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) → [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) FUN_007a1168

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`007a1610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1610.md)
- 新版 呼出元 1件 [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a1668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a114c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md#insn-007a114c) · [`007a1184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md#insn-007a1184) · [`007a120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md#insn-007a120c)
- 新版 [`007a11a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a11a4) · [`007a11dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a11dc) · [`007a1264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a1264)

~~~diff
- 007a114c ["INT_ADD", "register:40f0:8", ["const:7a114c:8", "const:4:8"]]
- 007a114c ["CALL", null, ["callee:00597e88:8"]]
+ 007a11a4 ["INT_ADD", "register:40f0:8", ["const:7a11a4:8", "const:4:8"]]
+ 007a11a4 ["CALL", null, ["callee:00597e88:8"]]
- 007a114c bytes 3fdbf797
+ 007a11a4 bytes 39dbf797
- 007a1184 ["INT_ADD", "register:40f0:8", ["const:7a1184:8", "const:4:8"]]
- 007a1184 ["CALL", null, ["callee:007a205c:8"]]
+ 007a11dc ["INT_ADD", "register:40f0:8", ["const:7a11dc:8", "const:4:8"]]
+ 007a11dc ["CALL", null, ["callee:007a205c:8"]]
- 007a1184 bytes a0030094
+ 007a11dc bytes a0030094
- 007a120c ["INT_ADD", "register:40f0:8", ["const:7a120c:8", "const:4:8"]]
- 007a120c ["CALL", null, ["callee:0043bb60:8"]]
+ 007a1264 ["INT_ADD", "register:40f0:8", ["const:7a1264:8", "const:4:8"]]
+ 007a1264 ["CALL", null, ["callee:0043bb60:8"]]
- 007a120c bytes 456af297
+ 007a1264 bytes 3f6af297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc7921ea8dd728b11790d6b92016bc38"></a>

### [`007a1610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1610.md) → [`007a1668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md) FUN_007a1668

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a16d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1610.md#insn-007a16d0) · [`007a16fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1610.md#insn-007a16fc) · [`007a1738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1610.md#insn-007a1738)
- 新版 [`007a1728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1728) · [`007a1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1754) · [`007a1790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1790)

~~~diff
- 007a16d0 ["INT_ADD", "register:40f0:8", ["const:7a16d0:8", "const:4:8"]]
- 007a16d0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1728 ["INT_ADD", "register:40f0:8", ["const:7a1728:8", "const:4:8"]]
+ 007a1728 ["CALL", null, ["callee:00c57f80:8"]]
- 007a16d0 bytes f8d91294
+ 007a1728 bytes 16da1294
- 007a16fc ["INT_ADD", "register:40f0:8", ["const:7a16fc:8", "const:4:8"]]
- 007a16fc ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1754 ["INT_ADD", "register:40f0:8", ["const:7a1754:8", "const:4:8"]]
+ 007a1754 ["CALL", null, ["callee:00c57f80:8"]]
- 007a16fc bytes edd91294
+ 007a1754 bytes 0bda1294
- 007a1738 ["INT_ADD", "register:40f0:8", ["const:7a1738:8", "const:4:8"]]
- 007a1738 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1790 ["INT_ADD", "register:40f0:8", ["const:7a1790:8", "const:4:8"]]
+ 007a1790 ["CALL", null, ["callee:00c57f80:8"]]
- 007a1738 bytes ded91294
+ 007a1790 bytes fcd91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc7f9242725c0dac63d72250f796d70a"></a>

### [`007a1774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1774.md) → [`007a17cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md) FUN_007a17cc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1774.md#insn-007a17d4) · [`007a1864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1774.md#insn-007a1864) · [`007a1874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1774.md#insn-007a1874)
- 新版 [`007a182c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a182c) · [`007a18bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a18bc) · [`007a18cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a18cc)

~~~diff
- 007a17d4 ["INT_ADD", "register:40f0:8", ["const:7a17d4:8", "const:4:8"]]
- 007a17d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007a182c ["INT_ADD", "register:40f0:8", ["const:7a182c:8", "const:4:8"]]
+ 007a182c ["CALL", null, ["callee:00c57f60:8"]]
- 007a17d4 bytes afd91294
+ 007a182c bytes cdd91294
- 007a1864 ["INT_ADD", "register:40f0:8", ["const:7a1864:8", "const:4:8"]]
- 007a1864 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a18bc ["INT_ADD", "register:40f0:8", ["const:7a18bc:8", "const:4:8"]]
+ 007a18bc ["CALL", null, ["callee:00c57f80:8"]]
- 007a1864 bytes 93d91294
+ 007a18bc bytes b1d91294
- 007a1874 ["INT_ADD", "register:40f0:8", ["const:7a1874:8", "const:4:8"]]
- 007a1874 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a18cc ["INT_ADD", "register:40f0:8", ["const:7a18cc:8", "const:4:8"]]
+ 007a18cc ["CALL", null, ["callee:00c57f80:8"]]
- 007a1874 bytes 8fd91294
+ 007a18cc bytes add91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a30cb8185a34c1a08552f6569e8552c2"></a>

### [`007a18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md) → [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) FUN_007a1928

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1110.md) · 呼出先 6件 [`007a1a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1a18.md) [`007a1ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md) [`007a1b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1b28.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 6件 [`007a1a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md) [`007a1b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md) [`007a1b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a192c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md#insn-007a192c) · [`007a1974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md#insn-007a1974) · [`007a19d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md#insn-007a19d8)
- 新版 [`007a1984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a1984) · [`007a19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a19cc) · [`007a1a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a1a30)

~~~diff
- 007a192c ["INT_ADD", "register:40f0:8", ["const:7a192c:8", "const:4:8"]]
- 007a192c ["CALL", null, ["callee:00c57f60:8"]]
+ 007a1984 ["INT_ADD", "register:40f0:8", ["const:7a1984:8", "const:4:8"]]
+ 007a1984 ["CALL", null, ["callee:00c57f60:8"]]
- 007a192c bytes 59d91294
+ 007a1984 bytes 77d91294
- 007a1974 ["INT_ADD", "register:40f0:8", ["const:7a1974:8", "const:4:8"]]
- 007a1974 ["CALL", null, ["callee:007a1b80:8"]]
+ 007a19cc ["INT_ADD", "register:40f0:8", ["const:7a19cc:8", "const:4:8"]]
+ 007a19cc ["CALL", null, ["callee:007a1b80:8"]]
- 007a1974 bytes 6d000094
+ 007a19cc bytes 6d000094
- 007a19d8 ["INT_ADD", "register:40f0:8", ["const:7a19d8:8", "const:4:8"]]
- 007a19d8 ["CALL", null, ["callee:007a1b08:8"]]
+ 007a1a30 ["INT_ADD", "register:40f0:8", ["const:7a1a30:8", "const:4:8"]]
+ 007a1a30 ["CALL", null, ["callee:007a1b08:8"]]
- 007a19d8 bytes 36000094
+ 007a1a30 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-070fae10e636f03e805500733310f42a"></a>

### [`007a1a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1a18.md) → [`007a1a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md) FUN_007a1a70

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1a18.md#insn-007a1a7c) · [`007a1a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1a18.md#insn-007a1a8c)
- 新版 [`007a1ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md#insn-007a1ad4) · [`007a1ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md#insn-007a1ae4)

~~~diff
- 007a1a7c ["INT_ADD", "register:40f0:8", ["const:7a1a7c:8", "const:4:8"]]
- 007a1a7c ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1ad4 ["INT_ADD", "register:40f0:8", ["const:7a1ad4:8", "const:4:8"]]
+ 007a1ad4 ["CALL", null, ["callee:00c57f80:8"]]
- 007a1a7c bytes 0dd91294
+ 007a1ad4 bytes 2bd91294
- 007a1a8c ["INT_ADD", "register:40f0:8", ["const:7a1a8c:8", "const:4:8"]]
- 007a1a8c ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1ae4 ["INT_ADD", "register:40f0:8", ["const:7a1ae4:8", "const:4:8"]]
+ 007a1ae4 ["CALL", null, ["callee:00c57f80:8"]]
- 007a1a8c bytes 09d91294
+ 007a1ae4 bytes 27d91294
~~~


<a id="compare-1b78b31b51f12e07e42fd12e8eaa0d0e"></a>

### [`007a1ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ac4.md) → [`007a1b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md) FUN_007a1b1c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ac4.md#insn-007a1b04) · [`007a1b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ac4.md#insn-007a1b14)
- 新版 [`007a1b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md#insn-007a1b5c) · [`007a1b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md#insn-007a1b6c)

~~~diff
- 007a1b04 ["INT_ADD", "register:40f0:8", ["const:7a1b04:8", "const:4:8"]]
- 007a1b04 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1b5c ["INT_ADD", "register:40f0:8", ["const:7a1b5c:8", "const:4:8"]]
+ 007a1b5c ["CALL", null, ["callee:00c57f80:8"]]
- 007a1b04 bytes ebd81294
+ 007a1b5c bytes 09d91294
- 007a1b14 ["INT_ADD", "register:40f0:8", ["const:7a1b14:8", "const:4:8"]]
- 007a1b14 ["CALL", null, ["callee:00c57f80:8"]]
+ 007a1b6c ["INT_ADD", "register:40f0:8", ["const:7a1b6c:8", "const:4:8"]]
+ 007a1b6c ["CALL", null, ["callee:00c57f80:8"]]
- 007a1b14 bytes e7d81294
+ 007a1b6c bytes 05d91294
~~~


<a id="compare-492ecf1b32230842d6e5649282344c3f"></a>

### [`007a1b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1b28.md) → [`007a1b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md) FUN_007a1b80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1b28.md#insn-007a1b88) · [`007a1bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1b28.md#insn-007a1bcc) · [`007a1be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1b28.md#insn-007a1be4)
- 新版 [`007a1be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1be0) · [`007a1c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1c24) · [`007a1c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1c3c)

~~~diff
- 007a1b88 ["INT_ADD", "register:40f0:8", ["const:7a1b88:8", "const:4:8"]]
- 007a1b88 ["CALL", null, ["callee:0043bb60:8"]]
+ 007a1be0 ["INT_ADD", "register:40f0:8", ["const:7a1be0:8", "const:4:8"]]
+ 007a1be0 ["CALL", null, ["callee:0043bb60:8"]]
- 007a1b88 bytes e667f297
+ 007a1be0 bytes e067f297
- 007a1bcc ["INT_ADD", "register:40f0:8", ["const:7a1bcc:8", "const:4:8"]]
- 007a1bcc ["CALL", null, ["callee:00c57f60:8"]]
+ 007a1c24 ["INT_ADD", "register:40f0:8", ["const:7a1c24:8", "const:4:8"]]
+ 007a1c24 ["CALL", null, ["callee:00c57f60:8"]]
- 007a1bcc bytes b1d81294
+ 007a1c24 bytes cfd81294
- 007a1be4 ["INT_ADD", "register:40f0:8", ["const:7a1be4:8", "const:4:8"]]
- 007a1be4 ["CALL", null, ["callee:00c580d0:8"]]
+ 007a1c3c ["INT_ADD", "register:40f0:8", ["const:7a1c3c:8", "const:4:8"]]
+ 007a1c3c ["CALL", null, ["callee:00c580d0:8"]]
- 007a1be4 bytes 07d91294
+ 007a1c3c bytes 25d91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

