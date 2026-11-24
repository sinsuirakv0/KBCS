# v16.0.2 → v16.0.3 · 要調査の変更候補 (42)

[一覧の目次](README.md)

<a id="compare-c7a96d0d85ae01fd73662ecfb632c478"></a>

### [`00c39578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md) → [`00c3a56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a56c.md) FUN_00c3a56c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c395bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md#insn-00c395bc) · [`00c395d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39578.md#insn-00c395d8)
- 新版 [`00c3a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a56c.md#insn-00c3a5b0) · [`00c3a5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a56c.md#insn-00c3a5cc)

~~~diff
- 00c395bc ["INT_ADD", "register:40f0:8", ["const:c395bc:8", "const:4:8"]]
- 00c395bc ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a5b0 ["INT_ADD", "register:40f0:8", ["const:c3a5b0:8", "const:4:8"]]
+ 00c3a5b0 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c395bc bytes d9880094
+ 00c3a5b0 bytes d0880094
- 00c395d8 ["INT_ADD", "register:40f0:8", ["const:c395d8:8", "const:4:8"]]
- 00c395d8 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a5cc ["INT_ADD", "register:40f0:8", ["const:c3a5cc:8", "const:4:8"]]
+ 00c3a5cc ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c395d8 bytes d2880094
+ 00c3a5cc bytes c9880094
~~~


<a id="compare-2bf707ddc865541cd49cc160acddc371"></a>

### [`00c398d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c398d4.md) → [`00c3a8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a8c8.md) FUN_00c3a8c8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c398d4.md#insn-00c39924)
- 新版 [`00c3a918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3a8c8.md#insn-00c3a918)

~~~diff
- 00c39924 ["INT_ADD", "register:40f0:8", ["const:c39924:8", "const:4:8"]]
- 00c39924 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3a918 ["INT_ADD", "register:40f0:8", ["const:c3a918:8", "const:4:8"]]
+ 00c3a918 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39924 bytes ff870094
+ 00c3a918 bytes f6870094
~~~


<a id="compare-e07943c11566171b0c72afebd4775b11"></a>

### [`00c39a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39a18.md) → [`00c3aa0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3aa0c.md) FUN_00c3aa0c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c39a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39a18.md#insn-00c39a5c)
- 新版 [`00c3aa50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3aa0c.md#insn-00c3aa50)

~~~diff
- 00c39a5c ["INT_ADD", "register:40f0:8", ["const:c39a5c:8", "const:4:8"]]
- 00c39a5c ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c3aa50 ["INT_ADD", "register:40f0:8", ["const:c3aa50:8", "const:4:8"]]
+ 00c3aa50 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c39a5c bytes b1870094
+ 00c3aa50 bytes a8870094
~~~


<a id="compare-eef623cf6bc45c7db71db7b4c60fbd77"></a>

### [`00c3a0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md) → [`00c3b0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b0d8.md) FUN_00c3b0d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a108) · [`00c3a144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a144) · [`00c3a158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a0e4.md#insn-00c3a158)
- 新版 [`00c3b0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b0d8.md#insn-00c3b0fc) · [`00c3b138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b0d8.md#insn-00c3b138) · [`00c3b14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b0d8.md#insn-00c3b14c)

~~~diff
- 00c3a108 ["INT_ADD", "register:40f0:8", ["const:c3a108:8", "const:4:8"]]
- 00c3a108 ["CALL", null, ["callee:00c59700:8"]]
+ 00c3b0fc ["INT_ADD", "register:40f0:8", ["const:c3b0fc:8", "const:4:8"]]
+ 00c3b0fc ["CALL", null, ["callee:00c59700:8"]]
- 00c3a108 bytes 8a790094
+ 00c3b0fc bytes 81790094
- 00c3a144 ["INT_ADD", "register:40f0:8", ["const:c3a144:8", "const:4:8"]]
- 00c3a144 ["CALL", null, ["callee:00c59700:8"]]
+ 00c3b138 ["INT_ADD", "register:40f0:8", ["const:c3b138:8", "const:4:8"]]
+ 00c3b138 ["CALL", null, ["callee:00c59700:8"]]
- 00c3a144 bytes 7b790094
+ 00c3b138 bytes 72790094
- 00c3a158 ["INT_ADD", "register:40f0:8", ["const:c3a158:8", "const:4:8"]]
- 00c3a158 ["CALL", null, ["callee:00c59700:8"]]
+ 00c3b14c ["INT_ADD", "register:40f0:8", ["const:c3b14c:8", "const:4:8"]]
+ 00c3b14c ["CALL", null, ["callee:00c59700:8"]]
- 00c3a158 bytes 76790094
+ 00c3b14c bytes 6d790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483ed54761865f485ac8d925e69e4e26"></a>

### [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) → [`00c3b1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md) FUN_00c3b1a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3a1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md#insn-00c3a1e4)
- 新版 [`00c3b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md#insn-00c3b1d8)

~~~diff
- 00c3a1e4 ["INT_ADD", "register:40f0:8", ["const:c3a1e4:8", "const:4:8"]]
- 00c3a1e4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00c3b1d8 ["INT_ADD", "register:40f0:8", ["const:c3b1d8:8", "const:4:8"]]
+ 00c3b1d8 ["CALL", null, ["callee:00c590f0:8"]]
- 00c3a1e4 bytes cf770094
+ 00c3b1d8 bytes c6770094
~~~


<a id="compare-6daa3570c09c943830f66e2adef020ab"></a>

### [`00c3c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md) → [`00c3d0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d0f4.md) FUN_00c3d0f4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 2件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3c19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c19c) · [`00c3c218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c218) · [`00c3c238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md#insn-00c3c238)
- 新版 [`00c3d190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d0f4.md#insn-00c3d190) · [`00c3d20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d0f4.md#insn-00c3d20c) · [`00c3d22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d0f4.md#insn-00c3d22c)

~~~diff
- 00c3c19c ["INT_ADD", "register:40f0:8", ["const:c3c19c:8", "const:4:8"]]
- 00c3c19c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c3d190 ["INT_ADD", "register:40f0:8", ["const:c3d190:8", "const:4:8"]]
+ 00c3d190 ["CALL", null, ["callee:00c58fe0:8"]]
- 00c3c19c bytes 9d6f0094
+ 00c3d190 bytes 946f0094
- 00c3c218 ["INT_ADD", "register:40f0:8", ["const:c3c218:8", "const:4:8"]]
- 00c3c218 ["CALL", null, ["callee:00c59700:8"]]
+ 00c3d20c ["INT_ADD", "register:40f0:8", ["const:c3d20c:8", "const:4:8"]]
+ 00c3d20c ["CALL", null, ["callee:00c59700:8"]]
- 00c3c218 bytes 46710094
+ 00c3d20c bytes 3d710094
- 00c3c238 ["INT_ADD", "register:40f0:8", ["const:c3c238:8", "const:4:8"]]
- 00c3c238 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c3d22c ["INT_ADD", "register:40f0:8", ["const:c3d22c:8", "const:4:8"]]
+ 00c3d22c ["CALL", null, ["callee:00c58fe0:8"]]
- 00c3c238 bytes 766f0094
+ 00c3d22c bytes 6d6f0094
~~~


<a id="compare-afaccd7ff277b7dd2781519593844390"></a>

### [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md) → [`00c3dcf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md) FUN_00c3dcf8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 4件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3cd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd4c) · [`00c3cd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd60) · [`00c3cd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md#insn-00c3cd68)
- 新版 [`00c3dd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md#insn-00c3dd40) · [`00c3dd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md#insn-00c3dd54) · [`00c3dd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md#insn-00c3dd5c)

~~~diff
- 00c3cd4c ["INT_ADD", "register:40f0:8", ["const:c3cd4c:8", "const:4:8"]]
- 00c3cd4c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3dd40 ["INT_ADD", "register:40f0:8", ["const:c3dd40:8", "const:4:8"]]
+ 00c3dd40 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3cd4c bytes 09750094
+ 00c3dd40 bytes 00750094
- 00c3cd60 ["INT_ADD", "register:40f0:8", ["const:c3cd60:8", "const:4:8"]]
- 00c3cd60 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c3dd54 ["INT_ADD", "register:40f0:8", ["const:c3dd54:8", "const:4:8"]]
+ 00c3dd54 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c3cd60 bytes 2c790094
+ 00c3dd54 bytes 23790094
- 00c3cd68 ["INT_ADD", "register:40f0:8", ["const:c3cd68:8", "const:4:8"]]
- 00c3cd68 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3dd5c ["INT_ADD", "register:40f0:8", ["const:c3dd5c:8", "const:4:8"]]
+ 00c3dd5c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3cd68 bytes e2740094
+ 00c3dd5c bytes d9740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d28b58b8e1afa4a7190675f363f06be"></a>

### [`00c3d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md) → [`00c3e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e0c0.md) FUN_00c3e0c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 2件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d140) · [`00c3d168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d168) · [`00c3d1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md#insn-00c3d1fc)
- 新版 [`00c3e134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e0c0.md#insn-00c3e134) · [`00c3e15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e0c0.md#insn-00c3e15c) · [`00c3e1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e0c0.md#insn-00c3e1f0)

~~~diff
- 00c3d140 ["INT_ADD", "register:40f0:8", ["const:c3d140:8", "const:4:8"]]
- 00c3d140 ["CALL", null, ["callee:00c59700:8"]]
+ 00c3e134 ["INT_ADD", "register:40f0:8", ["const:c3e134:8", "const:4:8"]]
+ 00c3e134 ["CALL", null, ["callee:00c59700:8"]]
- 00c3d140 bytes 7c6d0094
+ 00c3e134 bytes 736d0094
- 00c3d168 ["INT_ADD", "register:40f0:8", ["const:c3d168:8", "const:4:8"]]
- 00c3d168 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c3e15c ["INT_ADD", "register:40f0:8", ["const:c3e15c:8", "const:4:8"]]
+ 00c3e15c ["CALL", null, ["callee:00c58fe0:8"]]
- 00c3d168 bytes aa6b0094
+ 00c3e15c bytes a16b0094
- 00c3d1fc ["INT_ADD", "register:40f0:8", ["const:c3d1fc:8", "const:4:8"]]
- 00c3d1fc ["CALL", null, ["callee:00c59700:8"]]
+ 00c3e1f0 ["INT_ADD", "register:40f0:8", ["const:c3e1f0:8", "const:4:8"]]
+ 00c3e1f0 ["CALL", null, ["callee:00c59700:8"]]
- 00c3d1fc bytes 4d6d0094
+ 00c3e1f0 bytes 446d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c400c304327d586a547016df9a5592e9"></a>

### [`00c3ddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md) → [`00c3edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3edc0.md) FUN_00c3edc0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3de1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de1c) · [`00c3de38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de38) · [`00c3de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3ddcc.md#insn-00c3de5c)
- 新版 [`00c3ee10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3edc0.md#insn-00c3ee10) · [`00c3ee2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3edc0.md#insn-00c3ee2c) · [`00c3ee50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3edc0.md#insn-00c3ee50)

~~~diff
- 00c3de1c ["INT_ADD", "register:40f0:8", ["const:c3de1c:8", "const:4:8"]]
- 00c3de1c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3ee10 ["INT_ADD", "register:40f0:8", ["const:c3ee10:8", "const:4:8"]]
+ 00c3ee10 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3de1c bytes d5700094
+ 00c3ee10 bytes cc700094
- 00c3de38 ["INT_ADD", "register:40f0:8", ["const:c3de38:8", "const:4:8"]]
- 00c3de38 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c3ee2c ["INT_ADD", "register:40f0:8", ["const:c3ee2c:8", "const:4:8"]]
+ 00c3ee2c ["CALL", null, ["callee:00c590a0:8"]]
- 00c3de38 bytes a6680094
+ 00c3ee2c bytes 9d680094
- 00c3de5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3de5c ["INT_ADD", "register:40f0:8", ["const:c3de5c:8", "const:4:8"]]
- 00c3de5c ["CALLIND", null, ["register:0:8"]]
+ 00c3ee50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3ee50 ["INT_ADD", "register:40f0:8", ["const:c3ee50:8", "const:4:8"]]
+ 00c3ee50 ["CALLIND", null, ["register:0:8"]]
- 00c3de5c bytes 00013fd6
+ 00c3ee50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0848681f108f64da1172881dbaaf36d"></a>

### [`00c3e318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md) → [`00c3f30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f30c.md) FUN_00c3f30c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3e368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e368) · [`00c3e384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e384) · [`00c3e3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e318.md#insn-00c3e3a8)
- 新版 [`00c3f35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f30c.md#insn-00c3f35c) · [`00c3f378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f30c.md#insn-00c3f378) · [`00c3f39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f30c.md#insn-00c3f39c)

~~~diff
- 00c3e368 ["INT_ADD", "register:40f0:8", ["const:c3e368:8", "const:4:8"]]
- 00c3e368 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3f35c ["INT_ADD", "register:40f0:8", ["const:c3f35c:8", "const:4:8"]]
+ 00c3f35c ["CALL", null, ["callee:00c5b140:8"]]
- 00c3e368 bytes 826f0094
+ 00c3f35c bytes 796f0094
- 00c3e384 ["INT_ADD", "register:40f0:8", ["const:c3e384:8", "const:4:8"]]
- 00c3e384 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c3f378 ["INT_ADD", "register:40f0:8", ["const:c3f378:8", "const:4:8"]]
+ 00c3f378 ["CALL", null, ["callee:00c590a0:8"]]
- 00c3e384 bytes 53670094
+ 00c3f378 bytes 4a670094
- 00c3e3a8 ["INT_ADD", "register:40f0:8", ["const:c3e3a8:8", "const:4:8"]]
- 00c3e3a8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c3f39c ["INT_ADD", "register:40f0:8", ["const:c3f39c:8", "const:4:8"]]
+ 00c3f39c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c3e3a8 bytes 9a730094
+ 00c3f39c bytes 91730094
~~~


<a id="compare-fe2ed9d7049c7e5e714a72e9836ee85a"></a>

### [`00c3e3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md) → [`00c3f3b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f3b8.md) FUN_00c3f3b8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3e3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e3f8) · [`00c3e41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e41c) · [`00c3e468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e3c4.md#insn-00c3e468)
- 新版 [`00c3f3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f3b8.md#insn-00c3f3ec) · [`00c3f410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f3b8.md#insn-00c3f410) · [`00c3f45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f3b8.md#insn-00c3f45c)

~~~diff
- 00c3e3f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3e3f8 ["INT_ADD", "register:40f0:8", ["const:c3e3f8:8", "const:4:8"]]
- 00c3e3f8 ["CALLIND", null, ["register:0:8"]]
+ 00c3f3ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3f3ec ["INT_ADD", "register:40f0:8", ["const:c3f3ec:8", "const:4:8"]]
+ 00c3f3ec ["CALLIND", null, ["register:0:8"]]
- 00c3e3f8 bytes 00013fd6
+ 00c3f3ec bytes 00013fd6
- 00c3e41c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3e41c ["INT_ADD", "register:40f0:8", ["const:c3e41c:8", "const:4:8"]]
- 00c3e41c ["CALLIND", null, ["register:0:8"]]
+ 00c3f410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3f410 ["INT_ADD", "register:40f0:8", ["const:c3f410:8", "const:4:8"]]
+ 00c3f410 ["CALLIND", null, ["register:0:8"]]
- 00c3e41c bytes 00013fd6
+ 00c3f410 bytes 00013fd6
- 00c3e468 ["INT_ADD", "register:40f0:8", ["const:c3e468:8", "const:4:8"]]
- 00c3e468 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3f45c ["INT_ADD", "register:40f0:8", ["const:c3f45c:8", "const:4:8"]]
+ 00c3f45c ["CALL", null, ["callee:00c5b140:8"]]
- 00c3e468 bytes 426f0094
+ 00c3f45c bytes 396f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e57070c9f6886155a0ab94be170a19f"></a>

### [`00c3fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) → [`00c40a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md) FUN_00c40a00

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 4件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c3fbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) · 呼出先 4件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa54) · [`00c3fa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa68) · [`00c3fa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md#insn-00c3fa70)
- 新版 [`00c40a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md#insn-00c40a48) · [`00c40a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md#insn-00c40a5c) · [`00c40a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md#insn-00c40a64)

~~~diff
- 00c3fa54 ["INT_ADD", "register:40f0:8", ["const:c3fa54:8", "const:4:8"]]
- 00c3fa54 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c40a48 ["INT_ADD", "register:40f0:8", ["const:c40a48:8", "const:4:8"]]
+ 00c40a48 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3fa54 bytes c7690094
+ 00c40a48 bytes be690094
- 00c3fa68 ["INT_ADD", "register:40f0:8", ["const:c3fa68:8", "const:4:8"]]
- 00c3fa68 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c40a5c ["INT_ADD", "register:40f0:8", ["const:c40a5c:8", "const:4:8"]]
+ 00c40a5c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c3fa68 bytes ea6d0094
+ 00c40a5c bytes e16d0094
- 00c3fa70 ["INT_ADD", "register:40f0:8", ["const:c3fa70:8", "const:4:8"]]
- 00c3fa70 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c40a64 ["INT_ADD", "register:40f0:8", ["const:c40a64:8", "const:4:8"]]
+ 00c40a64 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3fa70 bytes a0690094
+ 00c40a64 bytes 97690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4abefba8ac6ff16561c1531f5993dc72"></a>

### [`00c3fb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fb90.md) → [`00c40b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40b84.md) FUN_00c40b84

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fb90.md#insn-00c3fbdc)
- 新版 [`00c40bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40b84.md#insn-00c40bd0)

~~~diff
- 00c3fbdc ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fbdc ["INT_ADD", "register:40f0:8", ["const:c3fbdc:8", "const:4:8"]]
- 00c3fbdc ["CALLIND", null, ["register:0:8"]]
+ 00c40bd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c40bd0 ["INT_ADD", "register:40f0:8", ["const:c40bd0:8", "const:4:8"]]
+ 00c40bd0 ["CALLIND", null, ["register:0:8"]]
- 00c3fbdc bytes 20013fd6
+ 00c40bd0 bytes 20013fd6
~~~


<a id="compare-0bbf6de403f4e679d83670b227f040b4"></a>

### [`00c3fc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc14.md) → [`00c40c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40c08.md) FUN_00c40c08

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc14.md#insn-00c3fc60)
- 新版 [`00c40c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40c08.md#insn-00c40c54)

~~~diff
- 00c3fc60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fc60 ["INT_ADD", "register:40f0:8", ["const:c3fc60:8", "const:4:8"]]
- 00c3fc60 ["CALLIND", null, ["register:0:8"]]
+ 00c40c54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c40c54 ["INT_ADD", "register:40f0:8", ["const:c40c54:8", "const:4:8"]]
+ 00c40c54 ["CALLIND", null, ["register:0:8"]]
- 00c3fc60 bytes 20013fd6
+ 00c40c54 bytes 20013fd6
~~~


<a id="compare-bc541a35bb30172b17d08cdfdd1961b8"></a>

### [`00c3fc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc98.md) → [`00c40c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40c8c.md) FUN_00c40c8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fc98.md#insn-00c3fce4)
- 新版 [`00c40cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40c8c.md#insn-00c40cd8)

~~~diff
- 00c3fce4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fce4 ["INT_ADD", "register:40f0:8", ["const:c3fce4:8", "const:4:8"]]
- 00c3fce4 ["CALLIND", null, ["register:0:8"]]
+ 00c40cd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c40cd8 ["INT_ADD", "register:40f0:8", ["const:c40cd8:8", "const:4:8"]]
+ 00c40cd8 ["CALLIND", null, ["register:0:8"]]
- 00c3fce4 bytes 20013fd6
+ 00c40cd8 bytes 20013fd6
~~~


<a id="compare-a88320d6c5028223ad9019be0c604604"></a>

### [`00c3fd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd1c.md) → [`00c40d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40d10.md) FUN_00c40d10

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd1c.md#insn-00c3fd50)
- 新版 [`00c40d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40d10.md#insn-00c40d44)

~~~diff
- 00c3fd50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c3fd50 ["INT_ADD", "register:40f0:8", ["const:c3fd50:8", "const:4:8"]]
- 00c3fd50 ["CALLIND", null, ["register:0:8"]]
+ 00c40d44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c40d44 ["INT_ADD", "register:40f0:8", ["const:c40d44:8", "const:4:8"]]
+ 00c40d44 ["CALLIND", null, ["register:0:8"]]
- 00c3fd50 bytes 20013fd6
+ 00c40d44 bytes 20013fd6
~~~


<a id="compare-d23553f2f7f71524f8947bd9d288be8d"></a>

### [`00c3fd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd70.md) → [`00c40d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40d64.md) FUN_00c40d64

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fd70.md#insn-00c3fda0)
- 新版 [`00c40d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40d64.md#insn-00c40d94)

~~~diff
- 00c3fda0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3fda0 ["INT_ADD", "register:40f0:8", ["const:c3fda0:8", "const:4:8"]]
- 00c3fda0 ["CALLIND", null, ["register:0:8"]]
+ 00c40d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c40d94 ["INT_ADD", "register:40f0:8", ["const:c40d94:8", "const:4:8"]]
+ 00c40d94 ["CALLIND", null, ["register:0:8"]]
- 00c3fda0 bytes 00013fd6
+ 00c40d94 bytes 00013fd6
~~~


<a id="compare-fcc6008e06f3773034b1438a5b7eabcf"></a>

### [`00c3fdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fdc0.md) → [`00c40db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40db4.md) FUN_00c40db4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3fdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fdc0.md#insn-00c3fdf0)
- 新版 [`00c40de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40db4.md#insn-00c40de4)

~~~diff
- 00c3fdf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3fdf0 ["INT_ADD", "register:40f0:8", ["const:c3fdf0:8", "const:4:8"]]
- 00c3fdf0 ["CALLIND", null, ["register:0:8"]]
+ 00c40de4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c40de4 ["INT_ADD", "register:40f0:8", ["const:c40de4:8", "const:4:8"]]
+ 00c40de4 ["CALLIND", null, ["register:0:8"]]
- 00c3fdf0 bytes 00013fd6
+ 00c40de4 bytes 00013fd6
~~~


<a id="compare-6570ca539814bb4030dd1abd668c16ef"></a>

### [`00c43e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md) → [`00c44e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44e3c.md) FUN_00c44e3c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c43ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43ebc) · [`00c43ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43ee0) · [`00c43f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43e48.md#insn-00c43f1c)
- 新版 [`00c44eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44e3c.md#insn-00c44eb0) · [`00c44ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44e3c.md#insn-00c44ed4) · [`00c44f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44e3c.md#insn-00c44f10)

~~~diff
- 00c43ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c43ebc ["INT_ADD", "register:40f0:8", ["const:c43ebc:8", "const:4:8"]]
- 00c43ebc ["CALLIND", null, ["register:0:8"]]
+ 00c44eb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44eb0 ["INT_ADD", "register:40f0:8", ["const:c44eb0:8", "const:4:8"]]
+ 00c44eb0 ["CALLIND", null, ["register:0:8"]]
- 00c43ebc bytes 00013fd6
+ 00c44eb0 bytes 00013fd6
- 00c43ee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c43ee0 ["INT_ADD", "register:40f0:8", ["const:c43ee0:8", "const:4:8"]]
- 00c43ee0 ["CALLIND", null, ["register:0:8"]]
+ 00c44ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c44ed4 ["INT_ADD", "register:40f0:8", ["const:c44ed4:8", "const:4:8"]]
+ 00c44ed4 ["CALLIND", null, ["register:0:8"]]
- 00c43ee0 bytes 00013fd6
+ 00c44ed4 bytes 00013fd6
- 00c43f1c ["INT_ADD", "register:40f0:8", ["const:c43f1c:8", "const:4:8"]]
- 00c43f1c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c44f10 ["INT_ADD", "register:40f0:8", ["const:c44f10:8", "const:4:8"]]
+ 00c44f10 ["CALL", null, ["callee:00c5b140:8"]]
- 00c43f1c bytes 95580094
+ 00c44f10 bytes 8c580094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b3ab16f253c8e1661eeb9cca46bdc20"></a>

### [`00c4441c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md) → [`00c45410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45410.md) FUN_00c45410

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4446c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c4446c) · [`00c44488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c44488) · [`00c444c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4441c.md#insn-00c444c4)
- 新版 [`00c45460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45410.md#insn-00c45460) · [`00c4547c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45410.md#insn-00c4547c) · [`00c454b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45410.md#insn-00c454b8)

~~~diff
- 00c4446c ["INT_ADD", "register:40f0:8", ["const:c4446c:8", "const:4:8"]]
- 00c4446c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45460 ["INT_ADD", "register:40f0:8", ["const:c45460:8", "const:4:8"]]
+ 00c45460 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4446c bytes 41570094
+ 00c45460 bytes 38570094
- 00c44488 ["INT_ADD", "register:40f0:8", ["const:c44488:8", "const:4:8"]]
- 00c44488 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c4547c ["INT_ADD", "register:40f0:8", ["const:c4547c:8", "const:4:8"]]
+ 00c4547c ["CALL", null, ["callee:00c590a0:8"]]
- 00c44488 bytes 124f0094
+ 00c4547c bytes 094f0094
- 00c444c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c444c4 ["INT_ADD", "register:40f0:8", ["const:c444c4:8", "const:4:8"]]
- 00c444c4 ["CALLIND", null, ["register:0:8"]]
+ 00c454b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c454b8 ["INT_ADD", "register:40f0:8", ["const:c454b8:8", "const:4:8"]]
+ 00c454b8 ["CALLIND", null, ["register:0:8"]]
- 00c444c4 bytes 00013fd6
+ 00c454b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d220c6d93e882aa3a35d88d7abd54dc7"></a>

### [`00c44604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md) → [`00c455f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c455f8.md) FUN_00c455f8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c44650) · [`00c44674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c44674) · [`00c446b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44604.md#insn-00c446b8)
- 新版 [`00c45644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c455f8.md#insn-00c45644) · [`00c45668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c455f8.md#insn-00c45668) · [`00c456ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c455f8.md#insn-00c456ac)

~~~diff
- 00c44650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44650 ["INT_ADD", "register:40f0:8", ["const:c44650:8", "const:4:8"]]
- 00c44650 ["CALLIND", null, ["register:0:8"]]
+ 00c45644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45644 ["INT_ADD", "register:40f0:8", ["const:c45644:8", "const:4:8"]]
+ 00c45644 ["CALLIND", null, ["register:0:8"]]
- 00c44650 bytes 00013fd6
+ 00c45644 bytes 00013fd6
- 00c44674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44674 ["INT_ADD", "register:40f0:8", ["const:c44674:8", "const:4:8"]]
- 00c44674 ["CALLIND", null, ["register:0:8"]]
+ 00c45668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45668 ["INT_ADD", "register:40f0:8", ["const:c45668:8", "const:4:8"]]
+ 00c45668 ["CALLIND", null, ["register:0:8"]]
- 00c44674 bytes 00013fd6
+ 00c45668 bytes 00013fd6
- 00c446b8 ["INT_ADD", "register:40f0:8", ["const:c446b8:8", "const:4:8"]]
- 00c446b8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c456ac ["INT_ADD", "register:40f0:8", ["const:c456ac:8", "const:4:8"]]
+ 00c456ac ["CALL", null, ["callee:00c5b140:8"]]
- 00c446b8 bytes ae560094
+ 00c456ac bytes a5560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf0048472a9cf287ed7be903cb88d5f"></a>

### [`00c447ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md) → [`00c457e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c457e0.md) FUN_00c457e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44834) · [`00c44858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44858) · [`00c44894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c447ec.md#insn-00c44894)
- 新版 [`00c45828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c457e0.md#insn-00c45828) · [`00c4584c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c457e0.md#insn-00c4584c) · [`00c45888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c457e0.md#insn-00c45888)

~~~diff
- 00c44834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44834 ["INT_ADD", "register:40f0:8", ["const:c44834:8", "const:4:8"]]
- 00c44834 ["CALLIND", null, ["register:0:8"]]
+ 00c45828 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45828 ["INT_ADD", "register:40f0:8", ["const:c45828:8", "const:4:8"]]
+ 00c45828 ["CALLIND", null, ["register:0:8"]]
- 00c44834 bytes 00013fd6
+ 00c45828 bytes 00013fd6
- 00c44858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44858 ["INT_ADD", "register:40f0:8", ["const:c44858:8", "const:4:8"]]
- 00c44858 ["CALLIND", null, ["register:0:8"]]
+ 00c4584c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4584c ["INT_ADD", "register:40f0:8", ["const:c4584c:8", "const:4:8"]]
+ 00c4584c ["CALLIND", null, ["register:0:8"]]
- 00c44858 bytes 00013fd6
+ 00c4584c bytes 00013fd6
- 00c44894 ["INT_ADD", "register:40f0:8", ["const:c44894:8", "const:4:8"]]
- 00c44894 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45888 ["INT_ADD", "register:40f0:8", ["const:c45888:8", "const:4:8"]]
+ 00c45888 ["CALL", null, ["callee:00c5b140:8"]]
- 00c44894 bytes 37560094
+ 00c45888 bytes 2e560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055a2321561d018bfca3da2702932a74"></a>

### [`00c44b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md) → [`00c45b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45b40.md) FUN_00c45b40

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44b98) · [`00c44bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44bbc) · [`00c44c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44b4c.md#insn-00c44c00)
- 新版 [`00c45b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45b40.md#insn-00c45b8c) · [`00c45bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45b40.md#insn-00c45bb0) · [`00c45bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45b40.md#insn-00c45bf4)

~~~diff
- 00c44b98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44b98 ["INT_ADD", "register:40f0:8", ["const:c44b98:8", "const:4:8"]]
- 00c44b98 ["CALLIND", null, ["register:0:8"]]
+ 00c45b8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45b8c ["INT_ADD", "register:40f0:8", ["const:c45b8c:8", "const:4:8"]]
+ 00c45b8c ["CALLIND", null, ["register:0:8"]]
- 00c44b98 bytes 00013fd6
+ 00c45b8c bytes 00013fd6
- 00c44bbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c44bbc ["INT_ADD", "register:40f0:8", ["const:c44bbc:8", "const:4:8"]]
- 00c44bbc ["CALLIND", null, ["register:0:8"]]
+ 00c45bb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c45bb0 ["INT_ADD", "register:40f0:8", ["const:c45bb0:8", "const:4:8"]]
+ 00c45bb0 ["CALLIND", null, ["register:0:8"]]
- 00c44bbc bytes 00013fd6
+ 00c45bb0 bytes 00013fd6
- 00c44c00 ["INT_ADD", "register:40f0:8", ["const:c44c00:8", "const:4:8"]]
- 00c44c00 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45bf4 ["INT_ADD", "register:40f0:8", ["const:c45bf4:8", "const:4:8"]]
+ 00c45bf4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c44c00 bytes 5c550094
+ 00c45bf4 bytes 53550094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5860e11ef53db129bea55e65d483c98"></a>

### [`00c44e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md) → [`00c45e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45e74.md) FUN_00c45e74

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c44ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44ed0) · [`00c44f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44f1c) · [`00c44f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md#insn-00c44f7c)
- 新版 [`00c45ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45e74.md#insn-00c45ec4) · [`00c45f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45e74.md#insn-00c45f10) · [`00c45f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45e74.md#insn-00c45f70)

~~~diff
- 00c44ed0 ["INT_ADD", "register:40f0:8", ["const:c44ed0:8", "const:4:8"]]
- 00c44ed0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45ec4 ["INT_ADD", "register:40f0:8", ["const:c45ec4:8", "const:4:8"]]
+ 00c45ec4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c44ed0 bytes a8540094
+ 00c45ec4 bytes 9f540094
- 00c44f1c ["INT_ADD", "register:40f0:8", ["const:c44f1c:8", "const:4:8"]]
- 00c44f1c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45f10 ["INT_ADD", "register:40f0:8", ["const:c45f10:8", "const:4:8"]]
+ 00c45f10 ["CALL", null, ["callee:00c5b140:8"]]
- 00c44f1c bytes 95540094
+ 00c45f10 bytes 8c540094
- 00c44f7c ["INT_ADD", "register:40f0:8", ["const:c44f7c:8", "const:4:8"]]
- 00c44f7c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c45f70 ["INT_ADD", "register:40f0:8", ["const:c45f70:8", "const:4:8"]]
+ 00c45f70 ["CALL", null, ["callee:00c5b140:8"]]
- 00c44f7c bytes 7d540094
+ 00c45f70 bytes 74540094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ff2b41375949f5609fa433adfc9d88"></a>

### [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) → [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) FUN_00c461d4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00c44e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c44e80.md) [`00c455e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md) [`00c45714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md) [`00c48b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 15件 [`00c45e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45e74.md) [`00c465dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c465dc.md) [`00c46708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46708.md) [`00c49b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md) [`00c49f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49f50.md) · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c45270) · [`00c452c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c452c0) · [`00c452e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md#insn-00c452e4)
- 新版 [`00c46264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md#insn-00c46264) · [`00c462b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md#insn-00c462b4) · [`00c462d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md#insn-00c462d8)

~~~diff
- 00c45270 ["INT_ADD", "register:40f0:8", ["const:c45270:8", "const:4:8"]]
- 00c45270 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46264 ["INT_ADD", "register:40f0:8", ["const:c46264:8", "const:4:8"]]
+ 00c46264 ["CALL", null, ["callee:00c5b140:8"]]
- 00c45270 bytes c0530094
+ 00c46264 bytes b7530094
- 00c452c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c452c0 ["INT_ADD", "register:40f0:8", ["const:c452c0:8", "const:4:8"]]
- 00c452c0 ["CALLIND", null, ["register:0:8"]]
+ 00c462b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c462b4 ["INT_ADD", "register:40f0:8", ["const:c462b4:8", "const:4:8"]]
+ 00c462b4 ["CALLIND", null, ["register:0:8"]]
- 00c452c0 bytes 00013fd6
+ 00c462b4 bytes 00013fd6
- 00c452e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c452e4 ["INT_ADD", "register:40f0:8", ["const:c452e4:8", "const:4:8"]]
- 00c452e4 ["CALLIND", null, ["register:0:8"]]
+ 00c462d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c462d8 ["INT_ADD", "register:40f0:8", ["const:c462d8:8", "const:4:8"]]
+ 00c462d8 ["CALLIND", null, ["register:0:8"]]
- 00c452e4 bytes 00013fd6
+ 00c462d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a566afa6ec7f7c022e5c93297f444b03"></a>

### [`00c45410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md) → [`00c46404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46404.md) FUN_00c46404

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c4545c) · [`00c454a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c454a8) · [`00c4550c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45410.md#insn-00c4550c)
- 新版 [`00c46450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46404.md#insn-00c46450) · [`00c4649c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46404.md#insn-00c4649c) · [`00c46500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46404.md#insn-00c46500)

~~~diff
- 00c4545c ["INT_ADD", "register:40f0:8", ["const:c4545c:8", "const:4:8"]]
- 00c4545c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46450 ["INT_ADD", "register:40f0:8", ["const:c46450:8", "const:4:8"]]
+ 00c46450 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4545c bytes 45530094
+ 00c46450 bytes 3c530094
- 00c454a8 ["INT_ADD", "register:40f0:8", ["const:c454a8:8", "const:4:8"]]
- 00c454a8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4649c ["INT_ADD", "register:40f0:8", ["const:c4649c:8", "const:4:8"]]
+ 00c4649c ["CALL", null, ["callee:00c5b140:8"]]
- 00c454a8 bytes 32530094
+ 00c4649c bytes 29530094
- 00c4550c ["INT_ADD", "register:40f0:8", ["const:c4550c:8", "const:4:8"]]
- 00c4550c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46500 ["INT_ADD", "register:40f0:8", ["const:c46500:8", "const:4:8"]]
+ 00c46500 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4550c bytes 19530094
+ 00c46500 bytes 10530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0adc48451247e8d92e47011f7ea59424"></a>

### [`00c455e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md) → [`00c465dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c465dc.md) FUN_00c465dc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45614) · [`00c45638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45638) · [`00c45670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c455e8.md#insn-00c45670)
- 新版 [`00c46608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c465dc.md#insn-00c46608) · [`00c4662c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c465dc.md#insn-00c4662c) · [`00c46664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c465dc.md#insn-00c46664)

~~~diff
- 00c45614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45614 ["INT_ADD", "register:40f0:8", ["const:c45614:8", "const:4:8"]]
- 00c45614 ["CALLIND", null, ["register:0:8"]]
+ 00c46608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c46608 ["INT_ADD", "register:40f0:8", ["const:c46608:8", "const:4:8"]]
+ 00c46608 ["CALLIND", null, ["register:0:8"]]
- 00c45614 bytes 00013fd6
+ 00c46608 bytes 00013fd6
- 00c45638 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45638 ["INT_ADD", "register:40f0:8", ["const:c45638:8", "const:4:8"]]
- 00c45638 ["CALLIND", null, ["register:0:8"]]
+ 00c4662c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4662c ["INT_ADD", "register:40f0:8", ["const:c4662c:8", "const:4:8"]]
+ 00c4662c ["CALLIND", null, ["register:0:8"]]
- 00c45638 bytes 00013fd6
+ 00c4662c bytes 00013fd6
- 00c45670 ["INT_ADD", "register:40f0:8", ["const:c45670:8", "const:4:8"]]
- 00c45670 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46664 ["INT_ADD", "register:40f0:8", ["const:c46664:8", "const:4:8"]]
+ 00c46664 ["CALL", null, ["callee:00c5b140:8"]]
- 00c45670 bytes c0520094
+ 00c46664 bytes b7520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96009f4b29b9c6c4e13ac9c4623bdbe0"></a>

### [`00c45714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md) → [`00c46708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46708.md) FUN_00c46708

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c45764) · [`00c45798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c45798) · [`00c457bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45714.md#insn-00c457bc)
- 新版 [`00c46758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46708.md#insn-00c46758) · [`00c4678c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46708.md#insn-00c4678c) · [`00c467b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46708.md#insn-00c467b0)

~~~diff
- 00c45764 ["INT_ADD", "register:40f0:8", ["const:c45764:8", "const:4:8"]]
- 00c45764 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46758 ["INT_ADD", "register:40f0:8", ["const:c46758:8", "const:4:8"]]
+ 00c46758 ["CALL", null, ["callee:00c5b140:8"]]
- 00c45764 bytes 83520094
+ 00c46758 bytes 7a520094
- 00c45798 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45798 ["INT_ADD", "register:40f0:8", ["const:c45798:8", "const:4:8"]]
- 00c45798 ["CALLIND", null, ["register:0:8"]]
+ 00c4678c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4678c ["INT_ADD", "register:40f0:8", ["const:c4678c:8", "const:4:8"]]
+ 00c4678c ["CALLIND", null, ["register:0:8"]]
- 00c45798 bytes 00013fd6
+ 00c4678c bytes 00013fd6
- 00c457bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c457bc ["INT_ADD", "register:40f0:8", ["const:c457bc:8", "const:4:8"]]
- 00c457bc ["CALLIND", null, ["register:0:8"]]
+ 00c467b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c467b0 ["INT_ADD", "register:40f0:8", ["const:c467b0:8", "const:4:8"]]
+ 00c467b0 ["CALLIND", null, ["register:0:8"]]
- 00c457bc bytes 00013fd6
+ 00c467b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff3a7f5cd7894860ba82d3caeed6a1e"></a>

### [`00c458f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md) → [`00c468e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c468e8.md) FUN_00c468e8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4593c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c4593c) · [`00c45960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c45960) · [`00c4599c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c458f4.md#insn-00c4599c)
- 新版 [`00c46930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c468e8.md#insn-00c46930) · [`00c46954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c468e8.md#insn-00c46954) · [`00c46990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c468e8.md#insn-00c46990)

~~~diff
- 00c4593c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4593c ["INT_ADD", "register:40f0:8", ["const:c4593c:8", "const:4:8"]]
- 00c4593c ["CALLIND", null, ["register:0:8"]]
+ 00c46930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c46930 ["INT_ADD", "register:40f0:8", ["const:c46930:8", "const:4:8"]]
+ 00c46930 ["CALLIND", null, ["register:0:8"]]
- 00c4593c bytes 00013fd6
+ 00c46930 bytes 00013fd6
- 00c45960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c45960 ["INT_ADD", "register:40f0:8", ["const:c45960:8", "const:4:8"]]
- 00c45960 ["CALLIND", null, ["register:0:8"]]
+ 00c46954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c46954 ["INT_ADD", "register:40f0:8", ["const:c46954:8", "const:4:8"]]
+ 00c46954 ["CALLIND", null, ["register:0:8"]]
- 00c45960 bytes 00013fd6
+ 00c46954 bytes 00013fd6
- 00c4599c ["INT_ADD", "register:40f0:8", ["const:c4599c:8", "const:4:8"]]
- 00c4599c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46990 ["INT_ADD", "register:40f0:8", ["const:c46990:8", "const:4:8"]]
+ 00c46990 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4599c bytes f5510094
+ 00c46990 bytes ec510094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f1678a39e6f82253d2074da8e93acf"></a>

### [`00c45da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md) → [`00c46d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46d94.md) FUN_00c46d94

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c45df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45df4) · [`00c45e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45e10) · [`00c45e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c45da0.md#insn-00c45e50)
- 新版 [`00c46de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46d94.md#insn-00c46de8) · [`00c46e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46d94.md#insn-00c46e04) · [`00c46e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c46d94.md#insn-00c46e44)

~~~diff
- 00c45df4 ["INT_ADD", "register:40f0:8", ["const:c45df4:8", "const:4:8"]]
- 00c45df4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46de8 ["INT_ADD", "register:40f0:8", ["const:c46de8:8", "const:4:8"]]
+ 00c46de8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c45df4 bytes df500094
+ 00c46de8 bytes d6500094
- 00c45e10 ["INT_ADD", "register:40f0:8", ["const:c45e10:8", "const:4:8"]]
- 00c45e10 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c46e04 ["INT_ADD", "register:40f0:8", ["const:c46e04:8", "const:4:8"]]
+ 00c46e04 ["CALL", null, ["callee:00c590a0:8"]]
- 00c45e10 bytes b0480094
+ 00c46e04 bytes a7480094
- 00c45e50 ["INT_ADD", "register:40f0:8", ["const:c45e50:8", "const:4:8"]]
- 00c45e50 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c46e44 ["INT_ADD", "register:40f0:8", ["const:c46e44:8", "const:4:8"]]
+ 00c46e44 ["CALL", null, ["callee:00c5b140:8"]]
- 00c45e50 bytes c8500094
+ 00c46e44 bytes bf500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0337dfa5611da955fbfae7a52c863d05"></a>

### [`00c460e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md) → [`00c470d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c470d8.md) FUN_00c470d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c46138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46138) · [`00c46154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46154) · [`00c46198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c460e4.md#insn-00c46198)
- 新版 [`00c4712c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c470d8.md#insn-00c4712c) · [`00c47148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c470d8.md#insn-00c47148) · [`00c4718c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c470d8.md#insn-00c4718c)

~~~diff
- 00c46138 ["INT_ADD", "register:40f0:8", ["const:c46138:8", "const:4:8"]]
- 00c46138 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4712c ["INT_ADD", "register:40f0:8", ["const:c4712c:8", "const:4:8"]]
+ 00c4712c ["CALL", null, ["callee:00c5b140:8"]]
- 00c46138 bytes 0e500094
+ 00c4712c bytes 05500094
- 00c46154 ["INT_ADD", "register:40f0:8", ["const:c46154:8", "const:4:8"]]
- 00c46154 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c47148 ["INT_ADD", "register:40f0:8", ["const:c47148:8", "const:4:8"]]
+ 00c47148 ["CALL", null, ["callee:00c590a0:8"]]
- 00c46154 bytes df470094
+ 00c47148 bytes d6470094
- 00c46198 ["INT_ADD", "register:40f0:8", ["const:c46198:8", "const:4:8"]]
- 00c46198 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4718c ["INT_ADD", "register:40f0:8", ["const:c4718c:8", "const:4:8"]]
+ 00c4718c ["CALL", null, ["callee:00c5b140:8"]]
- 00c46198 bytes f64f0094
+ 00c4718c bytes ed4f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f3415e6c362b5556588888051ae0f1"></a>

### [`00c46e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md) → [`00c47e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47e7c.md) FUN_00c47e7c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c46ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46ee8) · [`00c46f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46f40) · [`00c46f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46e88.md#insn-00c46f5c)
- 新版 [`00c47edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47e7c.md#insn-00c47edc) · [`00c47f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47e7c.md#insn-00c47f34) · [`00c47f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47e7c.md#insn-00c47f50)

~~~diff
- 00c46ee8 ["INT_ADD", "register:40f0:8", ["const:c46ee8:8", "const:4:8"]]
- 00c46ee8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c47edc ["INT_ADD", "register:40f0:8", ["const:c47edc:8", "const:4:8"]]
+ 00c47edc ["CALL", null, ["callee:00c5b140:8"]]
- 00c46ee8 bytes a24c0094
+ 00c47edc bytes 994c0094
- 00c46f40 ["INT_ADD", "register:40f0:8", ["const:c46f40:8", "const:4:8"]]
- 00c46f40 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c47f34 ["INT_ADD", "register:40f0:8", ["const:c47f34:8", "const:4:8"]]
+ 00c47f34 ["CALL", null, ["callee:00c5b140:8"]]
- 00c46f40 bytes 8c4c0094
+ 00c47f34 bytes 834c0094
- 00c46f5c ["INT_ADD", "register:40f0:8", ["const:c46f5c:8", "const:4:8"]]
- 00c46f5c ["CALL", null, ["callee:00c590a0:8"]]
+ 00c47f50 ["INT_ADD", "register:40f0:8", ["const:c47f50:8", "const:4:8"]]
+ 00c47f50 ["CALL", null, ["callee:00c590a0:8"]]
- 00c46f5c bytes 5d440094
+ 00c47f50 bytes 54440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650702321e3ae145f5524ee73eb3f1bf"></a>

### [`00c477bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md) → [`00c487b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c487b0.md) FUN_00c487b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c47800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c47800) · [`00c4783c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c4783c) · [`00c47860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c477bc.md#insn-00c47860)
- 新版 [`00c487f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c487b0.md#insn-00c487f4) · [`00c48830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c487b0.md#insn-00c48830) · [`00c48854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c487b0.md#insn-00c48854)

~~~diff
- 00c47800 ["INT_ADD", "register:40f0:8", ["const:c47800:8", "const:4:8"]]
- 00c47800 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c487f4 ["INT_ADD", "register:40f0:8", ["const:c487f4:8", "const:4:8"]]
+ 00c487f4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c47800 bytes 5c4a0094
+ 00c487f4 bytes 534a0094
- 00c4783c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4783c ["INT_ADD", "register:40f0:8", ["const:c4783c:8", "const:4:8"]]
- 00c4783c ["CALLIND", null, ["register:0:8"]]
+ 00c48830 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48830 ["INT_ADD", "register:40f0:8", ["const:c48830:8", "const:4:8"]]
+ 00c48830 ["CALLIND", null, ["register:0:8"]]
- 00c4783c bytes 00013fd6
+ 00c48830 bytes 00013fd6
- 00c47860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c47860 ["INT_ADD", "register:40f0:8", ["const:c47860:8", "const:4:8"]]
- 00c47860 ["CALLIND", null, ["register:0:8"]]
+ 00c48854 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48854 ["INT_ADD", "register:40f0:8", ["const:c48854:8", "const:4:8"]]
+ 00c48854 ["CALLIND", null, ["register:0:8"]]
- 00c47860 bytes 00013fd6
+ 00c48854 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c2951e4320b77d4306ee51f557f467"></a>

### [`00c48398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md) → [`00c4938c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4938c.md) FUN_00c4938c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c483e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c483e0) · [`00c48448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c48448) · [`00c48464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48398.md#insn-00c48464)
- 新版 [`00c493d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4938c.md#insn-00c493d4) · [`00c4943c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4938c.md#insn-00c4943c) · [`00c49458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4938c.md#insn-00c49458)

~~~diff
- 00c483e0 ["INT_ADD", "register:40f0:8", ["const:c483e0:8", "const:4:8"]]
- 00c483e0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c493d4 ["INT_ADD", "register:40f0:8", ["const:c493d4:8", "const:4:8"]]
+ 00c493d4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c483e0 bytes 64470094
+ 00c493d4 bytes 5b470094
- 00c48448 ["INT_ADD", "register:40f0:8", ["const:c48448:8", "const:4:8"]]
- 00c48448 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4943c ["INT_ADD", "register:40f0:8", ["const:c4943c:8", "const:4:8"]]
+ 00c4943c ["CALL", null, ["callee:00c5b140:8"]]
- 00c48448 bytes 4a470094
+ 00c4943c bytes 41470094
- 00c48464 ["INT_ADD", "register:40f0:8", ["const:c48464:8", "const:4:8"]]
- 00c48464 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c49458 ["INT_ADD", "register:40f0:8", ["const:c49458:8", "const:4:8"]]
+ 00c49458 ["CALL", null, ["callee:00c590a0:8"]]
- 00c48464 bytes 1b3f0094
+ 00c49458 bytes 123f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35f65e32a5b02519e14a50ba542478f4"></a>

### [`00c48588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md) → [`00c4957c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4957c.md) FUN_00c4957c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c485f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c485f4) · [`00c4864c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c4864c) · [`00c486ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48588.md#insn-00c486ac)
- 新版 [`00c495e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4957c.md#insn-00c495e8) · [`00c49640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4957c.md#insn-00c49640) · [`00c496a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c4957c.md#insn-00c496a0)

~~~diff
- 00c485f4 ["INT_ADD", "register:40f0:8", ["const:c485f4:8", "const:4:8"]]
- 00c485f4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c495e8 ["INT_ADD", "register:40f0:8", ["const:c495e8:8", "const:4:8"]]
+ 00c495e8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c485f4 bytes df460094
+ 00c495e8 bytes d6460094
- 00c4864c ["INT_ADD", "register:40f0:8", ["const:c4864c:8", "const:4:8"]]
- 00c4864c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49640 ["INT_ADD", "register:40f0:8", ["const:c49640:8", "const:4:8"]]
+ 00c49640 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4864c bytes c9460094
+ 00c49640 bytes c0460094
- 00c486ac ["INT_ADD", "register:40f0:8", ["const:c486ac:8", "const:4:8"]]
- 00c486ac ["CALL", null, ["callee:00c5b140:8"]]
+ 00c496a0 ["INT_ADD", "register:40f0:8", ["const:c496a0:8", "const:4:8"]]
+ 00c496a0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c486ac bytes b1460094
+ 00c496a0 bytes a8460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35782ea424ec046c49168b8cacaea507"></a>

### [`00c48844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48844.md) → [`00c49838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49838.md) FUN_00c49838

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48844.md#insn-00c48868)
- 新版 [`00c4985c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49838.md#insn-00c4985c)

~~~diff
- 00c48868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48868 ["INT_ADD", "register:40f0:8", ["const:c48868:8", "const:4:8"]]
- 00c48868 ["CALLIND", null, ["register:0:8"]]
+ 00c4985c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4985c ["INT_ADD", "register:40f0:8", ["const:c4985c:8", "const:4:8"]]
+ 00c4985c ["CALLIND", null, ["register:0:8"]]
- 00c48868 bytes 00013fd6
+ 00c4985c bytes 00013fd6
~~~


<a id="compare-ee5b61b588f336be16bfa30d520c4c7e"></a>

### [`00c488b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md) → [`00c498a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c498a8.md) FUN_00c498a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c488d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c488d8) · [`00c488fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c488fc) · [`00c48928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c488b4.md#insn-00c48928)
- 新版 [`00c498cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c498a8.md#insn-00c498cc) · [`00c498f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c498a8.md#insn-00c498f0) · [`00c4991c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c498a8.md#insn-00c4991c)

~~~diff
- 00c488d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c488d8 ["INT_ADD", "register:40f0:8", ["const:c488d8:8", "const:4:8"]]
- 00c488d8 ["CALLIND", null, ["register:0:8"]]
+ 00c498cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c498cc ["INT_ADD", "register:40f0:8", ["const:c498cc:8", "const:4:8"]]
+ 00c498cc ["CALLIND", null, ["register:0:8"]]
- 00c488d8 bytes 00013fd6
+ 00c498cc bytes 00013fd6
- 00c488fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c488fc ["INT_ADD", "register:40f0:8", ["const:c488fc:8", "const:4:8"]]
- 00c488fc ["CALLIND", null, ["register:0:8"]]
+ 00c498f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c498f0 ["INT_ADD", "register:40f0:8", ["const:c498f0:8", "const:4:8"]]
+ 00c498f0 ["CALLIND", null, ["register:0:8"]]
- 00c488fc bytes 00013fd6
+ 00c498f0 bytes 00013fd6
- 00c48928 ["INT_ADD", "register:40f0:8", ["const:c48928:8", "const:4:8"]]
- 00c48928 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4991c ["INT_ADD", "register:40f0:8", ["const:c4991c:8", "const:4:8"]]
+ 00c4991c ["CALL", null, ["callee:00c5b140:8"]]
- 00c48928 bytes 12460094
+ 00c4991c bytes 09460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c1ad174e82eeca814a2743cb1bb7b97"></a>

### [`00c489d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md) → [`00c499c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c499c4.md) FUN_00c499c4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c489f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c489f4) · [`00c48a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c48a18) · [`00c48a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c489d0.md#insn-00c48a54)
- 新版 [`00c499e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c499c4.md#insn-00c499e8) · [`00c49a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c499c4.md#insn-00c49a0c) · [`00c49a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c499c4.md#insn-00c49a48)

~~~diff
- 00c489f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c489f4 ["INT_ADD", "register:40f0:8", ["const:c489f4:8", "const:4:8"]]
- 00c489f4 ["CALLIND", null, ["register:0:8"]]
+ 00c499e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c499e8 ["INT_ADD", "register:40f0:8", ["const:c499e8:8", "const:4:8"]]
+ 00c499e8 ["CALLIND", null, ["register:0:8"]]
- 00c489f4 bytes 00013fd6
+ 00c499e8 bytes 00013fd6
- 00c48a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48a18 ["INT_ADD", "register:40f0:8", ["const:c48a18:8", "const:4:8"]]
- 00c48a18 ["CALLIND", null, ["register:0:8"]]
+ 00c49a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49a0c ["INT_ADD", "register:40f0:8", ["const:c49a0c:8", "const:4:8"]]
+ 00c49a0c ["CALLIND", null, ["register:0:8"]]
- 00c48a18 bytes 00013fd6
+ 00c49a0c bytes 00013fd6
- 00c48a54 ["INT_ADD", "register:40f0:8", ["const:c48a54:8", "const:4:8"]]
- 00c48a54 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49a48 ["INT_ADD", "register:40f0:8", ["const:c49a48:8", "const:4:8"]]
+ 00c49a48 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48a54 bytes c7450094
+ 00c49a48 bytes be450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9accc69bb7eb466814b952c5c0ec6f60"></a>

### [`00c48a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md) → [`00c49a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49a80.md) FUN_00c49a80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md#insn-00c48ab8) · [`00c48adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48a8c.md#insn-00c48adc)
- 新版 [`00c49aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49a80.md#insn-00c49aac) · [`00c49ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49a80.md#insn-00c49ad0)

~~~diff
- 00c48ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48ab8 ["INT_ADD", "register:40f0:8", ["const:c48ab8:8", "const:4:8"]]
- 00c48ab8 ["CALLIND", null, ["register:0:8"]]
+ 00c49aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49aac ["INT_ADD", "register:40f0:8", ["const:c49aac:8", "const:4:8"]]
+ 00c49aac ["CALLIND", null, ["register:0:8"]]
- 00c48ab8 bytes 00013fd6
+ 00c49aac bytes 00013fd6
- 00c48adc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48adc ["INT_ADD", "register:40f0:8", ["const:c48adc:8", "const:4:8"]]
- 00c48adc ["CALLIND", null, ["register:0:8"]]
+ 00c49ad0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49ad0 ["INT_ADD", "register:40f0:8", ["const:c49ad0:8", "const:4:8"]]
+ 00c49ad0 ["CALLIND", null, ["register:0:8"]]
- 00c48adc bytes 00013fd6
+ 00c49ad0 bytes 00013fd6
~~~


<a id="compare-2e9ee7f65e9aa144cb02ec523fad8900"></a>

### [`00c48d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md) → [`00c49d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49d44.md) FUN_00c49d44

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48d70) · [`00c48d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48d9c) · [`00c48ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48d50.md#insn-00c48ddc)
- 新版 [`00c49d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49d44.md#insn-00c49d64) · [`00c49d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49d44.md#insn-00c49d90) · [`00c49dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49d44.md#insn-00c49dd0)

~~~diff
- 00c48d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48d70 ["INT_ADD", "register:40f0:8", ["const:c48d70:8", "const:4:8"]]
- 00c48d70 ["CALLIND", null, ["register:0:8"]]
+ 00c49d64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49d64 ["INT_ADD", "register:40f0:8", ["const:c49d64:8", "const:4:8"]]
+ 00c49d64 ["CALLIND", null, ["register:0:8"]]
- 00c48d70 bytes 00013fd6
+ 00c49d64 bytes 00013fd6
- 00c48d9c ["INT_ADD", "register:40f0:8", ["const:c48d9c:8", "const:4:8"]]
- 00c48d9c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49d90 ["INT_ADD", "register:40f0:8", ["const:c49d90:8", "const:4:8"]]
+ 00c49d90 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48d9c bytes f5440094
+ 00c49d90 bytes ec440094
- 00c48ddc ["INT_ADD", "register:40f0:8", ["const:c48ddc:8", "const:4:8"]]
- 00c48ddc ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c49dd0 ["INT_ADD", "register:40f0:8", ["const:c49dd0:8", "const:4:8"]]
+ 00c49dd0 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c48ddc bytes 0d490094
+ 00c49dd0 bytes 04490094
~~~


<a id="compare-f00e16fd8ea47ff561d359e8580d4469"></a>

### [`00c48dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md) → [`00c49df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49df0.md) FUN_00c49df0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c49f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c48e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48e44) · [`00c48eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48eb4) · [`00c48ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48dfc.md#insn-00c48ed0)
- 新版 [`00c49e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49df0.md#insn-00c49e38) · [`00c49ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49df0.md#insn-00c49ea8) · [`00c49ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49df0.md#insn-00c49ec4)

~~~diff
- 00c48e44 ["INT_ADD", "register:40f0:8", ["const:c48e44:8", "const:4:8"]]
- 00c48e44 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49e38 ["INT_ADD", "register:40f0:8", ["const:c49e38:8", "const:4:8"]]
+ 00c49e38 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48e44 bytes cb440094
+ 00c49e38 bytes c2440094
- 00c48eb4 ["INT_ADD", "register:40f0:8", ["const:c48eb4:8", "const:4:8"]]
- 00c48eb4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49ea8 ["INT_ADD", "register:40f0:8", ["const:c49ea8:8", "const:4:8"]]
+ 00c49ea8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48eb4 bytes af440094
+ 00c49ea8 bytes a6440094
- 00c48ed0 ["INT_ADD", "register:40f0:8", ["const:c48ed0:8", "const:4:8"]]
- 00c48ed0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c49ec4 ["INT_ADD", "register:40f0:8", ["const:c49ec4:8", "const:4:8"]]
+ 00c49ec4 ["CALL", null, ["callee:00c590a0:8"]]
- 00c48ed0 bytes 803c0094
+ 00c49ec4 bytes 773c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-030566fd9cf6913c061967aa90109092"></a>

### [`00c492bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md) → [`00c4a2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a2b0.md) FUN_00c4a2b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c48f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48f5c.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c49f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49f50.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c49300) · [`00c4933c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c4933c) · [`00c4936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c492bc.md#insn-00c4936c)
- 新版 [`00c4a2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a2b0.md#insn-00c4a2f4) · [`00c4a330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a2b0.md#insn-00c4a330) · [`00c4a360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a2b0.md#insn-00c4a360)

~~~diff
- 00c49300 ["INT_ADD", "register:40f0:8", ["const:c49300:8", "const:4:8"]]
- 00c49300 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a2f4 ["INT_ADD", "register:40f0:8", ["const:c4a2f4:8", "const:4:8"]]
+ 00c4a2f4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c49300 bytes 9c430094
+ 00c4a2f4 bytes 93430094
- 00c4933c ["INT_ADD", "register:40f0:8", ["const:c4933c:8", "const:4:8"]]
- 00c4933c ["CALL", null, ["callee:00c49f50:8"]]
+ 00c4a330 ["INT_ADD", "register:40f0:8", ["const:c4a330:8", "const:4:8"]]
+ 00c4a330 ["CALL", null, ["callee:00c49f50:8"]]
- 00c4933c bytes 08ffff97
+ 00c4a330 bytes 08ffff97
- 00c4936c ["INT_ADD", "register:40f0:8", ["const:c4936c:8", "const:4:8"]]
- 00c4936c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a360 ["INT_ADD", "register:40f0:8", ["const:c4a360:8", "const:4:8"]]
+ 00c4a360 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4936c bytes 81430094
+ 00c4a360 bytes 78430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c6f3e548907cfaf65e463e632cd7e1"></a>

### [`00c493c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md) → [`00c4a3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a3b4.md) FUN_00c4a3b4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49410) · [`00c49444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49444) · [`00c49468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c493c0.md#insn-00c49468)
- 新版 [`00c4a404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a3b4.md#insn-00c4a404) · [`00c4a438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a3b4.md#insn-00c4a438) · [`00c4a45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a3b4.md#insn-00c4a45c)

~~~diff
- 00c49410 ["INT_ADD", "register:40f0:8", ["const:c49410:8", "const:4:8"]]
- 00c49410 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a404 ["INT_ADD", "register:40f0:8", ["const:c4a404:8", "const:4:8"]]
+ 00c4a404 ["CALL", null, ["callee:00c5b140:8"]]
- 00c49410 bytes 58430094
+ 00c4a404 bytes 4f430094
- 00c49444 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49444 ["INT_ADD", "register:40f0:8", ["const:c49444:8", "const:4:8"]]
- 00c49444 ["CALLIND", null, ["register:0:8"]]
+ 00c4a438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a438 ["INT_ADD", "register:40f0:8", ["const:c4a438:8", "const:4:8"]]
+ 00c4a438 ["CALLIND", null, ["register:0:8"]]
- 00c49444 bytes 00013fd6
+ 00c4a438 bytes 00013fd6
- 00c49468 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49468 ["INT_ADD", "register:40f0:8", ["const:c49468:8", "const:4:8"]]
- 00c49468 ["CALLIND", null, ["register:0:8"]]
+ 00c4a45c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a45c ["INT_ADD", "register:40f0:8", ["const:c4a45c:8", "const:4:8"]]
+ 00c4a45c ["CALLIND", null, ["register:0:8"]]
- 00c49468 bytes 00013fd6
+ 00c4a45c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-931d8302f8e95a700bede2fc837170fd"></a>

### [`00c49698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md) → [`00c4a68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a68c.md) FUN_00c4a68c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c496e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c496e0) · [`00c4973c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c4973c) · [`00c49758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49698.md#insn-00c49758)
- 新版 [`00c4a6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a68c.md#insn-00c4a6d4) · [`00c4a730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a68c.md#insn-00c4a730) · [`00c4a74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a68c.md#insn-00c4a74c)

~~~diff
- 00c496e0 ["INT_ADD", "register:40f0:8", ["const:c496e0:8", "const:4:8"]]
- 00c496e0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a6d4 ["INT_ADD", "register:40f0:8", ["const:c4a6d4:8", "const:4:8"]]
+ 00c4a6d4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c496e0 bytes a4420094
+ 00c4a6d4 bytes 9b420094
- 00c4973c ["INT_ADD", "register:40f0:8", ["const:c4973c:8", "const:4:8"]]
- 00c4973c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a730 ["INT_ADD", "register:40f0:8", ["const:c4a730:8", "const:4:8"]]
+ 00c4a730 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4973c bytes 8d420094
+ 00c4a730 bytes 84420094
- 00c49758 ["INT_ADD", "register:40f0:8", ["const:c49758:8", "const:4:8"]]
- 00c49758 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c4a74c ["INT_ADD", "register:40f0:8", ["const:c4a74c:8", "const:4:8"]]
+ 00c4a74c ["CALL", null, ["callee:00c590a0:8"]]
- 00c49758 bytes 5e3a0094
+ 00c4a74c bytes 553a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-909d05d7df6bccc409cf24e57e8c9e9c"></a>

### [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) → [`00c4af04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md) FUN_00c4af04

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c4978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) [`00c4b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 2件 [`00c4a780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md) [`00c4c444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md) · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c49f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49f54) · [`00c49f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49f78) · [`00c49fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md#insn-00c49fd4)
- 新版 [`00c4af48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md#insn-00c4af48) · [`00c4af6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md#insn-00c4af6c) · [`00c4afc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md#insn-00c4afc8)

~~~diff
- 00c49f54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49f54 ["INT_ADD", "register:40f0:8", ["const:c49f54:8", "const:4:8"]]
- 00c49f54 ["CALLIND", null, ["register:0:8"]]
+ 00c4af48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4af48 ["INT_ADD", "register:40f0:8", ["const:c4af48:8", "const:4:8"]]
+ 00c4af48 ["CALLIND", null, ["register:0:8"]]
- 00c49f54 bytes 00013fd6
+ 00c4af48 bytes 00013fd6
- 00c49f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c49f78 ["INT_ADD", "register:40f0:8", ["const:c49f78:8", "const:4:8"]]
- 00c49f78 ["CALLIND", null, ["register:0:8"]]
+ 00c4af6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4af6c ["INT_ADD", "register:40f0:8", ["const:c4af6c:8", "const:4:8"]]
+ 00c4af6c ["CALLIND", null, ["register:0:8"]]
- 00c49f78 bytes 00013fd6
+ 00c4af6c bytes 00013fd6
- 00c49fd4 ["INT_ADD", "register:40f0:8", ["const:c49fd4:8", "const:4:8"]]
- 00c49fd4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4afc8 ["INT_ADD", "register:40f0:8", ["const:c4afc8:8", "const:4:8"]]
+ 00c4afc8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c49fd4 bytes 67400094
+ 00c4afc8 bytes 5e400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232dbd9485cf18b17b36806c90922796"></a>

### [`00c4a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md) → [`00c4b0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b0c4.md) FUN_00c4b0c4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a11c) · [`00c4a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a150) · [`00c4a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a0d0.md#insn-00c4a174)
- 新版 [`00c4b110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b0c4.md#insn-00c4b110) · [`00c4b144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b0c4.md#insn-00c4b144) · [`00c4b168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b0c4.md#insn-00c4b168)

~~~diff
- 00c4a11c ["INT_ADD", "register:40f0:8", ["const:c4a11c:8", "const:4:8"]]
- 00c4a11c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b110 ["INT_ADD", "register:40f0:8", ["const:c4b110:8", "const:4:8"]]
+ 00c4b110 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a11c bytes 15400094
+ 00c4b110 bytes 0c400094
- 00c4a150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a150 ["INT_ADD", "register:40f0:8", ["const:c4a150:8", "const:4:8"]]
- 00c4a150 ["CALLIND", null, ["register:0:8"]]
+ 00c4b144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b144 ["INT_ADD", "register:40f0:8", ["const:c4b144:8", "const:4:8"]]
+ 00c4b144 ["CALLIND", null, ["register:0:8"]]
- 00c4a150 bytes 00013fd6
+ 00c4b144 bytes 00013fd6
- 00c4a174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a174 ["INT_ADD", "register:40f0:8", ["const:c4a174:8", "const:4:8"]]
- 00c4a174 ["CALLIND", null, ["register:0:8"]]
+ 00c4b168 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b168 ["INT_ADD", "register:40f0:8", ["const:c4b168:8", "const:4:8"]]
+ 00c4b168 ["CALLIND", null, ["register:0:8"]]
- 00c4a174 bytes 00013fd6
+ 00c4b168 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3d95c140f658818cb5693b9d27fcf26"></a>

### [`00c4a31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md) → [`00c4b310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b310.md) FUN_00c4b310

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a364) · [`00c4a39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a39c) · [`00c4a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a31c.md#insn-00c4a3c0)
- 新版 [`00c4b358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b310.md#insn-00c4b358) · [`00c4b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b310.md#insn-00c4b390) · [`00c4b3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b310.md#insn-00c4b3b4)

~~~diff
- 00c4a364 ["INT_ADD", "register:40f0:8", ["const:c4a364:8", "const:4:8"]]
- 00c4a364 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b358 ["INT_ADD", "register:40f0:8", ["const:c4b358:8", "const:4:8"]]
+ 00c4b358 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a364 bytes 833f0094
+ 00c4b358 bytes 7a3f0094
- 00c4a39c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a39c ["INT_ADD", "register:40f0:8", ["const:c4a39c:8", "const:4:8"]]
- 00c4a39c ["CALLIND", null, ["register:0:8"]]
+ 00c4b390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b390 ["INT_ADD", "register:40f0:8", ["const:c4b390:8", "const:4:8"]]
+ 00c4b390 ["CALLIND", null, ["register:0:8"]]
- 00c4a39c bytes 00013fd6
+ 00c4b390 bytes 00013fd6
- 00c4a3c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a3c0 ["INT_ADD", "register:40f0:8", ["const:c4a3c0:8", "const:4:8"]]
- 00c4a3c0 ["CALLIND", null, ["register:0:8"]]
+ 00c4b3b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b3b4 ["INT_ADD", "register:40f0:8", ["const:c4b3b4:8", "const:4:8"]]
+ 00c4b3b4 ["CALLIND", null, ["register:0:8"]]
- 00c4a3c0 bytes 00013fd6
+ 00c4b3b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdfc5735cbcd5dc410ef0eab37236daf"></a>

### [`00c4a588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md) → [`00c4b57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b57c.md) FUN_00c4b57c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a5bc) · [`00c4a5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a5e0) · [`00c4a60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a588.md#insn-00c4a60c)
- 新版 [`00c4b5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b57c.md#insn-00c4b5b0) · [`00c4b5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b57c.md#insn-00c4b5d4) · [`00c4b600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b57c.md#insn-00c4b600)

~~~diff
- 00c4a5bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a5bc ["INT_ADD", "register:40f0:8", ["const:c4a5bc:8", "const:4:8"]]
- 00c4a5bc ["CALLIND", null, ["register:0:8"]]
+ 00c4b5b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b5b0 ["INT_ADD", "register:40f0:8", ["const:c4b5b0:8", "const:4:8"]]
+ 00c4b5b0 ["CALLIND", null, ["register:0:8"]]
- 00c4a5bc bytes 00013fd6
+ 00c4b5b0 bytes 00013fd6
- 00c4a5e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a5e0 ["INT_ADD", "register:40f0:8", ["const:c4a5e0:8", "const:4:8"]]
- 00c4a5e0 ["CALLIND", null, ["register:0:8"]]
+ 00c4b5d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b5d4 ["INT_ADD", "register:40f0:8", ["const:c4b5d4:8", "const:4:8"]]
+ 00c4b5d4 ["CALLIND", null, ["register:0:8"]]
- 00c4a5e0 bytes 00013fd6
+ 00c4b5d4 bytes 00013fd6
- 00c4a60c ["INT_ADD", "register:40f0:8", ["const:c4a60c:8", "const:4:8"]]
- 00c4a60c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b600 ["INT_ADD", "register:40f0:8", ["const:c4b600:8", "const:4:8"]]
+ 00c4b600 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a60c bytes d93e0094
+ 00c4b600 bytes d03e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa7eca7c79bc5b3521bd6f97ba631429"></a>

### [`00c4a6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md) → [`00c4b698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b698.md) FUN_00c4b698

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4a6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a6f4) · [`00c4a728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a728) · [`00c4a74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a6a4.md#insn-00c4a74c)
- 新版 [`00c4b6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b698.md#insn-00c4b6e8) · [`00c4b71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b698.md#insn-00c4b71c) · [`00c4b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b698.md#insn-00c4b740)

~~~diff
- 00c4a6f4 ["INT_ADD", "register:40f0:8", ["const:c4a6f4:8", "const:4:8"]]
- 00c4a6f4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b6e8 ["INT_ADD", "register:40f0:8", ["const:c4b6e8:8", "const:4:8"]]
+ 00c4b6e8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a6f4 bytes 9f3e0094
+ 00c4b6e8 bytes 963e0094
- 00c4a728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a728 ["INT_ADD", "register:40f0:8", ["const:c4a728:8", "const:4:8"]]
- 00c4a728 ["CALLIND", null, ["register:0:8"]]
+ 00c4b71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b71c ["INT_ADD", "register:40f0:8", ["const:c4b71c:8", "const:4:8"]]
+ 00c4b71c ["CALLIND", null, ["register:0:8"]]
- 00c4a728 bytes 00013fd6
+ 00c4b71c bytes 00013fd6
- 00c4a74c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a74c ["INT_ADD", "register:40f0:8", ["const:c4a74c:8", "const:4:8"]]
- 00c4a74c ["CALLIND", null, ["register:0:8"]]
+ 00c4b740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b740 ["INT_ADD", "register:40f0:8", ["const:c4b740:8", "const:4:8"]]
+ 00c4b740 ["CALLIND", null, ["register:0:8"]]
- 00c4a74c bytes 00013fd6
+ 00c4b740 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e804ec03021290d2874bbdefc905901c"></a>

### [`00c4ade8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md) → [`00c4bddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bddc.md) FUN_00c4bddc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ae30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4ae30) · [`00c4ae94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4ae94) · [`00c4aee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md#insn-00c4aee8)
- 新版 [`00c4be24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bddc.md#insn-00c4be24) · [`00c4be88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bddc.md#insn-00c4be88) · [`00c4bedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bddc.md#insn-00c4bedc)

~~~diff
- 00c4ae30 ["INT_ADD", "register:40f0:8", ["const:c4ae30:8", "const:4:8"]]
- 00c4ae30 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4be24 ["INT_ADD", "register:40f0:8", ["const:c4be24:8", "const:4:8"]]
+ 00c4be24 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ae30 bytes d03c0094
+ 00c4be24 bytes c73c0094
- 00c4ae94 ["INT_ADD", "register:40f0:8", ["const:c4ae94:8", "const:4:8"]]
- 00c4ae94 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4be88 ["INT_ADD", "register:40f0:8", ["const:c4be88:8", "const:4:8"]]
+ 00c4be88 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ae94 bytes b73c0094
+ 00c4be88 bytes ae3c0094
- 00c4aee8 ["INT_ADD", "register:40f0:8", ["const:c4aee8:8", "const:4:8"]]
- 00c4aee8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4bedc ["INT_ADD", "register:40f0:8", ["const:c4bedc:8", "const:4:8"]]
+ 00c4bedc ["CALL", null, ["callee:00c5b140:8"]]
- 00c4aee8 bytes a23c0094
+ 00c4bedc bytes 993c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8564339ce1d29cd0033553a811d2606e"></a>

### [`00c4b5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md) → [`00c4c5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c5d8.md) FUN_00c4c5d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b628) · [`00c4b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b674) · [`00c4b6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b5e4.md#insn-00c4b6b8)
- 新版 [`00c4c61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c5d8.md#insn-00c4c61c) · [`00c4c668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c5d8.md#insn-00c4c668) · [`00c4c6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c5d8.md#insn-00c4c6ac)

~~~diff
- 00c4b628 ["INT_ADD", "register:40f0:8", ["const:c4b628:8", "const:4:8"]]
- 00c4b628 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c61c ["INT_ADD", "register:40f0:8", ["const:c4c61c:8", "const:4:8"]]
+ 00c4c61c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b628 bytes d23a0094
+ 00c4c61c bytes c93a0094
- 00c4b674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b674 ["INT_ADD", "register:40f0:8", ["const:c4b674:8", "const:4:8"]]
- 00c4b674 ["CALLIND", null, ["register:0:8"]]
+ 00c4c668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c668 ["INT_ADD", "register:40f0:8", ["const:c4c668:8", "const:4:8"]]
+ 00c4c668 ["CALLIND", null, ["register:0:8"]]
- 00c4b674 bytes 00013fd6
+ 00c4c668 bytes 00013fd6
- 00c4b6b8 ["INT_ADD", "register:40f0:8", ["const:c4b6b8:8", "const:4:8"]]
- 00c4b6b8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c4c6ac ["INT_ADD", "register:40f0:8", ["const:c4c6ac:8", "const:4:8"]]
+ 00c4c6ac ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4b6b8 bytes d63e0094
+ 00c4c6ac bytes cd3e0094
~~~


<a id="compare-e51d717c49d9428db81d9925afda26e4"></a>

### [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) → [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) FUN_00c4c6b8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 8件 [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) [`00c4c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) · 呼出先 8件 [`00c3fbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) [`00c3ff90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md) [`00c400c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b700) · [`00c4b734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b734) · [`00c4b744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md#insn-00c4b744)
- 新版 [`00c4c6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md#insn-00c4c6f4) · [`00c4c728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md#insn-00c4c728) · [`00c4c738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md#insn-00c4c738)

~~~diff
- 00c4b700 ["INT_ADD", "register:40f0:8", ["const:c4b700:8", "const:4:8"]]
- 00c4b700 ["CALL", null, ["callee:00c3fbcc:8"]]
+ 00c4c6f4 ["INT_ADD", "register:40f0:8", ["const:c4c6f4:8", "const:4:8"]]
+ 00c4c6f4 ["CALL", null, ["callee:00c3fbcc:8"]]
- 00c4b700 bytes 36cdff97
+ 00c4c6f4 bytes 36cdff97
- 00c4b734 ["INT_ADD", "register:40f0:8", ["const:c4b734:8", "const:4:8"]]
- 00c4b734 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c728 ["INT_ADD", "register:40f0:8", ["const:c4c728:8", "const:4:8"]]
+ 00c4c728 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b734 bytes 8f3a0094
+ 00c4c728 bytes 863a0094
- 00c4b744 ["INT_ADD", "register:40f0:8", ["const:c4b744:8", "const:4:8"]]
- 00c4b744 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c4c738 ["INT_ADD", "register:40f0:8", ["const:c4c738:8", "const:4:8"]]
+ 00c4c738 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4b744 bytes b33e0094
+ 00c4c738 bytes aa3e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d280d831599fb3a7c8d4dc0a08a0448"></a>

### [`00c4bad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md) → [`00c4cacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cacc.md) FUN_00c4cacc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4bb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb04) · [`00c4bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb28) · [`00c4bb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md#insn-00c4bb54)
- 新版 [`00c4caf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cacc.md#insn-00c4caf8) · [`00c4cb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cacc.md#insn-00c4cb1c) · [`00c4cb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cacc.md#insn-00c4cb48)

~~~diff
- 00c4bb04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4bb04 ["INT_ADD", "register:40f0:8", ["const:c4bb04:8", "const:4:8"]]
- 00c4bb04 ["CALLIND", null, ["register:0:8"]]
+ 00c4caf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4caf8 ["INT_ADD", "register:40f0:8", ["const:c4caf8:8", "const:4:8"]]
+ 00c4caf8 ["CALLIND", null, ["register:0:8"]]
- 00c4bb04 bytes 00013fd6
+ 00c4caf8 bytes 00013fd6
- 00c4bb28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4bb28 ["INT_ADD", "register:40f0:8", ["const:c4bb28:8", "const:4:8"]]
- 00c4bb28 ["CALLIND", null, ["register:0:8"]]
+ 00c4cb1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4cb1c ["INT_ADD", "register:40f0:8", ["const:c4cb1c:8", "const:4:8"]]
+ 00c4cb1c ["CALLIND", null, ["register:0:8"]]
- 00c4bb28 bytes 00013fd6
+ 00c4cb1c bytes 00013fd6
- 00c4bb54 ["INT_ADD", "register:40f0:8", ["const:c4bb54:8", "const:4:8"]]
- 00c4bb54 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4cb48 ["INT_ADD", "register:40f0:8", ["const:c4cb48:8", "const:4:8"]]
+ 00c4cb48 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4bb54 bytes 87390094
+ 00c4cb48 bytes 7e390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab69ea233d6a1f6cd59f8c313e0e8be"></a>

### [`00c4bf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md) → [`00c4cf6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cf6c.md) FUN_00c4cf6c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4bfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md#insn-00c4bfc0) · [`00c4c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md#insn-00c4c008)
- 新版 [`00c4cfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cf6c.md#insn-00c4cfb4) · [`00c4cffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cf6c.md#insn-00c4cffc)

~~~diff
- 00c4bfc0 ["INT_ADD", "register:40f0:8", ["const:c4bfc0:8", "const:4:8"]]
- 00c4bfc0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4cfb4 ["INT_ADD", "register:40f0:8", ["const:c4cfb4:8", "const:4:8"]]
+ 00c4cfb4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4bfc0 bytes 6c380094
+ 00c4cfb4 bytes 63380094
- 00c4c008 ["INT_ADD", "register:40f0:8", ["const:c4c008:8", "const:4:8"]]
- 00c4c008 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c4cffc ["INT_ADD", "register:40f0:8", ["const:c4cffc:8", "const:4:8"]]
+ 00c4cffc ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4c008 bytes 823c0094
+ 00c4cffc bytes 793c0094
~~~


<a id="compare-1abeedf7acaf23c4dcb31e16951d4d64"></a>

### [`00c4c1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md) → [`00c4d1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d1d4.md) FUN_00c4d1d4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c224) · [`00c4c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c260) · [`00c4c2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c1e0.md#insn-00c4c2a4)
- 新版 [`00c4d218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d1d4.md#insn-00c4d218) · [`00c4d254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d1d4.md#insn-00c4d254) · [`00c4d298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d1d4.md#insn-00c4d298)

~~~diff
- 00c4c224 ["INT_ADD", "register:40f0:8", ["const:c4c224:8", "const:4:8"]]
- 00c4c224 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d218 ["INT_ADD", "register:40f0:8", ["const:c4d218:8", "const:4:8"]]
+ 00c4d218 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c224 bytes d3370094
+ 00c4d218 bytes ca370094
- 00c4c260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c260 ["INT_ADD", "register:40f0:8", ["const:c4c260:8", "const:4:8"]]
- 00c4c260 ["CALLIND", null, ["register:0:8"]]
+ 00c4d254 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d254 ["INT_ADD", "register:40f0:8", ["const:c4d254:8", "const:4:8"]]
+ 00c4d254 ["CALLIND", null, ["register:0:8"]]
- 00c4c260 bytes 00013fd6
+ 00c4d254 bytes 00013fd6
- 00c4c2a4 ["INT_ADD", "register:40f0:8", ["const:c4c2a4:8", "const:4:8"]]
- 00c4c2a4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c4d298 ["INT_ADD", "register:40f0:8", ["const:c4d298:8", "const:4:8"]]
+ 00c4d298 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4c2a4 bytes db3b0094
+ 00c4d298 bytes d23b0094
~~~


<a id="compare-d6d32289f880775f8ec3799d4b4376d3"></a>

### [`00c4c8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8dc.md) → [`00c4d8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8d0.md) FUN_00c4d8d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c4c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) · 呼出先 1件 [`00c3e1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e1f8.md)
- 新版 呼出元 1件 [`00c4d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d2b8.md) · 呼出先 1件 [`00c3f1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f1ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8dc.md#insn-00c4c8f8)
- 新版 [`00c4d8ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8d0.md#insn-00c4d8ec)

~~~diff
- 00c4c8f8 ["INT_ADD", "register:40f0:8", ["const:c4c8f8:8", "const:4:8"]]
- 00c4c8f8 ["CALL", null, ["callee:00c3f1ec:8"]]
+ 00c4d8ec ["INT_ADD", "register:40f0:8", ["const:c4d8ec:8", "const:4:8"]]
+ 00c4d8ec ["CALL", null, ["callee:00c3f1ec:8"]]
- 00c4c8f8 bytes 40c6ff97
+ 00c4d8ec bytes 40c6ff97
~~~


<a id="compare-3318da12be7924755f3ffd47156ea5e4"></a>

### [`00c4c944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md) → [`00c4d938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d938.md) FUN_00c4d938

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4c96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4c96c) · [`00c4c998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4c998) · [`00c4ca00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c944.md#insn-00c4ca00)
- 新版 [`00c4d960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d938.md#insn-00c4d960) · [`00c4d98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d938.md#insn-00c4d98c) · [`00c4d9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d938.md#insn-00c4d9f4)

~~~diff
- 00c4c96c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c96c ["INT_ADD", "register:40f0:8", ["const:c4c96c:8", "const:4:8"]]
- 00c4c96c ["CALLIND", null, ["register:0:8"]]
+ 00c4d960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d960 ["INT_ADD", "register:40f0:8", ["const:c4d960:8", "const:4:8"]]
+ 00c4d960 ["CALLIND", null, ["register:0:8"]]
- 00c4c96c bytes 00013fd6
+ 00c4d960 bytes 00013fd6
- 00c4c998 ["INT_ADD", "register:40f0:8", ["const:c4c998:8", "const:4:8"]]
- 00c4c998 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d98c ["INT_ADD", "register:40f0:8", ["const:c4d98c:8", "const:4:8"]]
+ 00c4d98c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c998 bytes f6350094
+ 00c4d98c bytes ed350094
- 00c4ca00 ["INT_ADD", "register:40f0:8", ["const:c4ca00:8", "const:4:8"]]
- 00c4ca00 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d9f4 ["INT_ADD", "register:40f0:8", ["const:c4d9f4:8", "const:4:8"]]
+ 00c4d9f4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ca00 bytes dc350094
+ 00c4d9f4 bytes d3350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634fca6aca29b35cd9aece8c6d79895c"></a>

### [`00c4cab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md) → [`00c4daa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4daa8.md) FUN_00c4daa8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb00) · [`00c4cb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb28) · [`00c4cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cab4.md#insn-00c4cb60)
- 新版 [`00c4daf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4daa8.md#insn-00c4daf4) · [`00c4db1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4daa8.md#insn-00c4db1c) · [`00c4db54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4daa8.md#insn-00c4db54)

~~~diff
- 00c4cb00 ["INT_ADD", "register:40f0:8", ["const:c4cb00:8", "const:4:8"]]
- 00c4cb00 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4daf4 ["INT_ADD", "register:40f0:8", ["const:c4daf4:8", "const:4:8"]]
+ 00c4daf4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4cb00 bytes 9c350094
+ 00c4daf4 bytes 93350094
- 00c4cb28 ["INT_ADD", "register:40f0:8", ["const:c4cb28:8", "const:4:8"]]
- 00c4cb28 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c4db1c ["INT_ADD", "register:40f0:8", ["const:c4db1c:8", "const:4:8"]]
+ 00c4db1c ["CALL", null, ["callee:00c461d4:8"]]
- 00c4cb28 bytes aee1ff97
+ 00c4db1c bytes aee1ff97
- 00c4cb60 ["INT_ADD", "register:40f0:8", ["const:c4cb60:8", "const:4:8"]]
- 00c4cb60 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4db54 ["INT_ADD", "register:40f0:8", ["const:c4db54:8", "const:4:8"]]
+ 00c4db54 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4cb60 bytes 84350094
+ 00c4db54 bytes 7b350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf1be92cc67ee9338ee0703bdc933527"></a>

### [`00c4cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md) → [`00c4dc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dc54.md) FUN_00c4dc54

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4ccb0) · [`00c4cce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4cce4) · [`00c4cd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cc60.md#insn-00c4cd1c)
- 新版 [`00c4dca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dc54.md#insn-00c4dca4) · [`00c4dcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dc54.md#insn-00c4dcd8) · [`00c4dd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dc54.md#insn-00c4dd10)

~~~diff
- 00c4ccb0 ["INT_ADD", "register:40f0:8", ["const:c4ccb0:8", "const:4:8"]]
- 00c4ccb0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4dca4 ["INT_ADD", "register:40f0:8", ["const:c4dca4:8", "const:4:8"]]
+ 00c4dca4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ccb0 bytes 30350094
+ 00c4dca4 bytes 27350094
- 00c4cce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cce4 ["INT_ADD", "register:40f0:8", ["const:c4cce4:8", "const:4:8"]]
- 00c4cce4 ["CALLIND", null, ["register:0:8"]]
+ 00c4dcd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4dcd8 ["INT_ADD", "register:40f0:8", ["const:c4dcd8:8", "const:4:8"]]
+ 00c4dcd8 ["CALLIND", null, ["register:0:8"]]
- 00c4cce4 bytes 00013fd6
+ 00c4dcd8 bytes 00013fd6
- 00c4cd1c ["INT_ADD", "register:40f0:8", ["const:c4cd1c:8", "const:4:8"]]
- 00c4cd1c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4dd10 ["INT_ADD", "register:40f0:8", ["const:c4dd10:8", "const:4:8"]]
+ 00c4dd10 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4cd1c bytes 15350094
+ 00c4dd10 bytes 0c350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754a13a856c577fc2ae004f316f8d61e"></a>

### [`00c4cd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md) → [`00c4dd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dd60.md) FUN_00c4dd60

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cd98) · [`00c4cdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cdbc) · [`00c4cde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cd6c.md#insn-00c4cde8)
- 新版 [`00c4dd8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dd60.md#insn-00c4dd8c) · [`00c4ddb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dd60.md#insn-00c4ddb0) · [`00c4dddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dd60.md#insn-00c4dddc)

~~~diff
- 00c4cd98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cd98 ["INT_ADD", "register:40f0:8", ["const:c4cd98:8", "const:4:8"]]
- 00c4cd98 ["CALLIND", null, ["register:0:8"]]
+ 00c4dd8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4dd8c ["INT_ADD", "register:40f0:8", ["const:c4dd8c:8", "const:4:8"]]
+ 00c4dd8c ["CALLIND", null, ["register:0:8"]]
- 00c4cd98 bytes 00013fd6
+ 00c4dd8c bytes 00013fd6
- 00c4cdbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cdbc ["INT_ADD", "register:40f0:8", ["const:c4cdbc:8", "const:4:8"]]
- 00c4cdbc ["CALLIND", null, ["register:0:8"]]
+ 00c4ddb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ddb0 ["INT_ADD", "register:40f0:8", ["const:c4ddb0:8", "const:4:8"]]
+ 00c4ddb0 ["CALLIND", null, ["register:0:8"]]
- 00c4cdbc bytes 00013fd6
+ 00c4ddb0 bytes 00013fd6
- 00c4cde8 ["INT_ADD", "register:40f0:8", ["const:c4cde8:8", "const:4:8"]]
- 00c4cde8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4dddc ["INT_ADD", "register:40f0:8", ["const:c4dddc:8", "const:4:8"]]
+ 00c4dddc ["CALL", null, ["callee:00c5b140:8"]]
- 00c4cde8 bytes e2340094
+ 00c4dddc bytes d9340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d40ff7c3a353d194e53d52630354e5"></a>

### [`00c4cfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md) → [`00c4dfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dfb0.md) FUN_00c4dfb0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4cfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4cfe8) · [`00c4d00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4d00c) · [`00c4d038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cfbc.md#insn-00c4d038)
- 新版 [`00c4dfdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dfb0.md#insn-00c4dfdc) · [`00c4e000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dfb0.md#insn-00c4e000) · [`00c4e02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dfb0.md#insn-00c4e02c)

~~~diff
- 00c4cfe8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4cfe8 ["INT_ADD", "register:40f0:8", ["const:c4cfe8:8", "const:4:8"]]
- 00c4cfe8 ["CALLIND", null, ["register:0:8"]]
+ 00c4dfdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4dfdc ["INT_ADD", "register:40f0:8", ["const:c4dfdc:8", "const:4:8"]]
+ 00c4dfdc ["CALLIND", null, ["register:0:8"]]
- 00c4cfe8 bytes 00013fd6
+ 00c4dfdc bytes 00013fd6
- 00c4d00c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d00c ["INT_ADD", "register:40f0:8", ["const:c4d00c:8", "const:4:8"]]
- 00c4d00c ["CALLIND", null, ["register:0:8"]]
+ 00c4e000 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e000 ["INT_ADD", "register:40f0:8", ["const:c4e000:8", "const:4:8"]]
+ 00c4e000 ["CALLIND", null, ["register:0:8"]]
- 00c4d00c bytes 00013fd6
+ 00c4e000 bytes 00013fd6
- 00c4d038 ["INT_ADD", "register:40f0:8", ["const:c4d038:8", "const:4:8"]]
- 00c4d038 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e02c ["INT_ADD", "register:40f0:8", ["const:c4e02c:8", "const:4:8"]]
+ 00c4e02c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d038 bytes 4e340094
+ 00c4e02c bytes 45340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bcc993e0e091cf4f38d22d5cefc3b41"></a>

### [`00c4d2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md) → [`00c4e2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e2d4.md) FUN_00c4e2d4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d30c) · [`00c4d330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d330) · [`00c4d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d2e0.md#insn-00c4d35c)
- 新版 [`00c4e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e2d4.md#insn-00c4e300) · [`00c4e324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e2d4.md#insn-00c4e324) · [`00c4e350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e2d4.md#insn-00c4e350)

~~~diff
- 00c4d30c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d30c ["INT_ADD", "register:40f0:8", ["const:c4d30c:8", "const:4:8"]]
- 00c4d30c ["CALLIND", null, ["register:0:8"]]
+ 00c4e300 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e300 ["INT_ADD", "register:40f0:8", ["const:c4e300:8", "const:4:8"]]
+ 00c4e300 ["CALLIND", null, ["register:0:8"]]
- 00c4d30c bytes 00013fd6
+ 00c4e300 bytes 00013fd6
- 00c4d330 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d330 ["INT_ADD", "register:40f0:8", ["const:c4d330:8", "const:4:8"]]
- 00c4d330 ["CALLIND", null, ["register:0:8"]]
+ 00c4e324 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e324 ["INT_ADD", "register:40f0:8", ["const:c4e324:8", "const:4:8"]]
+ 00c4e324 ["CALLIND", null, ["register:0:8"]]
- 00c4d330 bytes 00013fd6
+ 00c4e324 bytes 00013fd6
- 00c4d35c ["INT_ADD", "register:40f0:8", ["const:c4d35c:8", "const:4:8"]]
- 00c4d35c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e350 ["INT_ADD", "register:40f0:8", ["const:c4e350:8", "const:4:8"]]
+ 00c4e350 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d35c bytes 85330094
+ 00c4e350 bytes 7c330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde5754fa08c064e40925be3285acb37"></a>

### [`00c4d61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md) → [`00c4e610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e610.md) FUN_00c4e610

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d668) · [`00c4d694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d694) · [`00c4d6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d61c.md#insn-00c4d6c0)
- 新版 [`00c4e65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e610.md#insn-00c4e65c) · [`00c4e688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e610.md#insn-00c4e688) · [`00c4e6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e610.md#insn-00c4e6b4)

~~~diff
- 00c4d668 ["INT_ADD", "register:40f0:8", ["const:c4d668:8", "const:4:8"]]
- 00c4d668 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e65c ["INT_ADD", "register:40f0:8", ["const:c4e65c:8", "const:4:8"]]
+ 00c4e65c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d668 bytes c2320094
+ 00c4e65c bytes b9320094
- 00c4d694 ["INT_ADD", "register:40f0:8", ["const:c4d694:8", "const:4:8"]]
- 00c4d694 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c4e688 ["INT_ADD", "register:40f0:8", ["const:c4e688:8", "const:4:8"]]
+ 00c4e688 ["CALL", null, ["callee:00c461d4:8"]]
- 00c4d694 bytes d3deff97
+ 00c4e688 bytes d3deff97
- 00c4d6c0 ["INT_ADD", "register:40f0:8", ["const:c4d6c0:8", "const:4:8"]]
- 00c4d6c0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e6b4 ["INT_ADD", "register:40f0:8", ["const:c4e6b4:8", "const:4:8"]]
+ 00c4e6b4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d6c0 bytes ac320094
+ 00c4e6b4 bytes a3320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80d223a88ed1d954bd767843835bd3ed"></a>

### [`00c4d714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md) → [`00c4e708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e708.md) FUN_00c4e708

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d740) · [`00c4d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d764) · [`00c4d77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d714.md#insn-00c4d77c)
- 新版 [`00c4e734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e708.md#insn-00c4e734) · [`00c4e758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e708.md#insn-00c4e758) · [`00c4e770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e708.md#insn-00c4e770)

~~~diff
- 00c4d740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d740 ["INT_ADD", "register:40f0:8", ["const:c4d740:8", "const:4:8"]]
- 00c4d740 ["CALLIND", null, ["register:0:8"]]
+ 00c4e734 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e734 ["INT_ADD", "register:40f0:8", ["const:c4e734:8", "const:4:8"]]
+ 00c4e734 ["CALLIND", null, ["register:0:8"]]
- 00c4d740 bytes 00013fd6
+ 00c4e734 bytes 00013fd6
- 00c4d764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d764 ["INT_ADD", "register:40f0:8", ["const:c4d764:8", "const:4:8"]]
- 00c4d764 ["CALLIND", null, ["register:0:8"]]
+ 00c4e758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e758 ["INT_ADD", "register:40f0:8", ["const:c4e758:8", "const:4:8"]]
+ 00c4e758 ["CALLIND", null, ["register:0:8"]]
- 00c4d764 bytes 00013fd6
+ 00c4e758 bytes 00013fd6
- 00c4d77c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d77c ["INT_ADD", "register:40f0:8", ["const:c4d77c:8", "const:4:8"]]
- 00c4d77c ["CALLIND", null, ["register:0:8"]]
+ 00c4e770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e770 ["INT_ADD", "register:40f0:8", ["const:c4e770:8", "const:4:8"]]
+ 00c4e770 ["CALLIND", null, ["register:0:8"]]
- 00c4d77c bytes 00013fd6
+ 00c4e770 bytes 00013fd6
~~~


<a id="compare-c3f07e801f29b959b40d0ad15a4b3065"></a>

### [`00c4d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md) → [`00c4e954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e954.md) FUN_00c4e954

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4d9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4d9a4) · [`00c4d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4d9f0) · [`00c4da34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d960.md#insn-00c4da34)
- 新版 [`00c4e998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e954.md#insn-00c4e998) · [`00c4e9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e954.md#insn-00c4e9e4) · [`00c4ea28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e954.md#insn-00c4ea28)

~~~diff
- 00c4d9a4 ["INT_ADD", "register:40f0:8", ["const:c4d9a4:8", "const:4:8"]]
- 00c4d9a4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e998 ["INT_ADD", "register:40f0:8", ["const:c4e998:8", "const:4:8"]]
+ 00c4e998 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d9a4 bytes f3310094
+ 00c4e998 bytes ea310094
- 00c4d9f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4d9f0 ["INT_ADD", "register:40f0:8", ["const:c4d9f0:8", "const:4:8"]]
- 00c4d9f0 ["CALLIND", null, ["register:0:8"]]
+ 00c4e9e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4e9e4 ["INT_ADD", "register:40f0:8", ["const:c4e9e4:8", "const:4:8"]]
+ 00c4e9e4 ["CALLIND", null, ["register:0:8"]]
- 00c4d9f0 bytes 00013fd6
+ 00c4e9e4 bytes 00013fd6
- 00c4da34 ["INT_ADD", "register:40f0:8", ["const:c4da34:8", "const:4:8"]]
- 00c4da34 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c4ea28 ["INT_ADD", "register:40f0:8", ["const:c4ea28:8", "const:4:8"]]
+ 00c4ea28 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4da34 bytes f7350094
+ 00c4ea28 bytes ee350094
~~~


<a id="compare-7611371b646198b0c80f7669b73fcad4"></a>

### [`00c4da58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md) → [`00c4ea4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ea4c.md) FUN_00c4ea4c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4da84) · [`00c4daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4daa8) · [`00c4dae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4da58.md#insn-00c4dae4)
- 新版 [`00c4ea78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ea4c.md#insn-00c4ea78) · [`00c4ea9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ea4c.md#insn-00c4ea9c) · [`00c4ead8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ea4c.md#insn-00c4ead8)

~~~diff
- 00c4da84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4da84 ["INT_ADD", "register:40f0:8", ["const:c4da84:8", "const:4:8"]]
- 00c4da84 ["CALLIND", null, ["register:0:8"]]
+ 00c4ea78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ea78 ["INT_ADD", "register:40f0:8", ["const:c4ea78:8", "const:4:8"]]
+ 00c4ea78 ["CALLIND", null, ["register:0:8"]]
- 00c4da84 bytes 00013fd6
+ 00c4ea78 bytes 00013fd6
- 00c4daa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4daa8 ["INT_ADD", "register:40f0:8", ["const:c4daa8:8", "const:4:8"]]
- 00c4daa8 ["CALLIND", null, ["register:0:8"]]
+ 00c4ea9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ea9c ["INT_ADD", "register:40f0:8", ["const:c4ea9c:8", "const:4:8"]]
+ 00c4ea9c ["CALLIND", null, ["register:0:8"]]
- 00c4daa8 bytes 00013fd6
+ 00c4ea9c bytes 00013fd6
- 00c4dae4 ["INT_ADD", "register:40f0:8", ["const:c4dae4:8", "const:4:8"]]
- 00c4dae4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4ead8 ["INT_ADD", "register:40f0:8", ["const:c4ead8:8", "const:4:8"]]
+ 00c4ead8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4dae4 bytes a3310094
+ 00c4ead8 bytes 9a310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1aae2ee4a50a47cd3797396a4a3df5c"></a>

### [`00c4df68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md) → [`00c4ef5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ef5c.md) FUN_00c4ef5c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4df94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4df94) · [`00c4dfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4dfb8) · [`00c4dfe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md#insn-00c4dfe4)
- 新版 [`00c4ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ef5c.md#insn-00c4ef88) · [`00c4efac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ef5c.md#insn-00c4efac) · [`00c4efd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4ef5c.md#insn-00c4efd8)

~~~diff
- 00c4df94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4df94 ["INT_ADD", "register:40f0:8", ["const:c4df94:8", "const:4:8"]]
- 00c4df94 ["CALLIND", null, ["register:0:8"]]
+ 00c4ef88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ef88 ["INT_ADD", "register:40f0:8", ["const:c4ef88:8", "const:4:8"]]
+ 00c4ef88 ["CALLIND", null, ["register:0:8"]]
- 00c4df94 bytes 00013fd6
+ 00c4ef88 bytes 00013fd6
- 00c4dfb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4dfb8 ["INT_ADD", "register:40f0:8", ["const:c4dfb8:8", "const:4:8"]]
- 00c4dfb8 ["CALLIND", null, ["register:0:8"]]
+ 00c4efac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4efac ["INT_ADD", "register:40f0:8", ["const:c4efac:8", "const:4:8"]]
+ 00c4efac ["CALLIND", null, ["register:0:8"]]
- 00c4dfb8 bytes 00013fd6
+ 00c4efac bytes 00013fd6
- 00c4dfe4 ["INT_ADD", "register:40f0:8", ["const:c4dfe4:8", "const:4:8"]]
- 00c4dfe4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4efd8 ["INT_ADD", "register:40f0:8", ["const:c4efd8:8", "const:4:8"]]
+ 00c4efd8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4dfe4 bytes 63300094
+ 00c4efd8 bytes 5a300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b759f629c871c66d3c3c01c0cd82864"></a>

### [`00c4f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md) → [`00c505cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c505cc.md) FUN_00c505cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f61c) · [`00c4f680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f680) · [`00c4f6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f5d8.md#insn-00c4f6c4)
- 新版 [`00c50610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c505cc.md#insn-00c50610) · [`00c50674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c505cc.md#insn-00c50674) · [`00c506b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c505cc.md#insn-00c506b8)

~~~diff
- 00c4f61c ["INT_ADD", "register:40f0:8", ["const:c4f61c:8", "const:4:8"]]
- 00c4f61c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50610 ["INT_ADD", "register:40f0:8", ["const:c50610:8", "const:4:8"]]
+ 00c50610 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4f61c bytes d52a0094
+ 00c50610 bytes cc2a0094
- 00c4f680 ["INT_ADD", "register:40f0:8", ["const:c4f680:8", "const:4:8"]]
- 00c4f680 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50674 ["INT_ADD", "register:40f0:8", ["const:c50674:8", "const:4:8"]]
+ 00c50674 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4f680 bytes bc2a0094
+ 00c50674 bytes b32a0094
- 00c4f6c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f6c4 ["INT_ADD", "register:40f0:8", ["const:c4f6c4:8", "const:4:8"]]
- 00c4f6c4 ["CALLIND", null, ["register:0:8"]]
+ 00c506b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c506b8 ["INT_ADD", "register:40f0:8", ["const:c506b8:8", "const:4:8"]]
+ 00c506b8 ["CALLIND", null, ["register:0:8"]]
- 00c4f6c4 bytes 00013fd6
+ 00c506b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e5e395ce8307131dfc602a22233bd6"></a>

### [`00c4f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md) → [`00c50844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50844.md) FUN_00c50844

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f894) · [`00c4f8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f8fc) · [`00c4f924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f850.md#insn-00c4f924)
- 新版 [`00c50888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50844.md#insn-00c50888) · [`00c508f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50844.md#insn-00c508f0) · [`00c50918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50844.md#insn-00c50918)

~~~diff
- 00c4f894 ["INT_ADD", "register:40f0:8", ["const:c4f894:8", "const:4:8"]]
- 00c4f894 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50888 ["INT_ADD", "register:40f0:8", ["const:c50888:8", "const:4:8"]]
+ 00c50888 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4f894 bytes 372a0094
+ 00c50888 bytes 2e2a0094
- 00c4f8fc ["INT_ADD", "register:40f0:8", ["const:c4f8fc:8", "const:4:8"]]
- 00c4f8fc ["CALL", null, ["callee:00c5b140:8"]]
+ 00c508f0 ["INT_ADD", "register:40f0:8", ["const:c508f0:8", "const:4:8"]]
+ 00c508f0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4f8fc bytes 1d2a0094
+ 00c508f0 bytes 142a0094
- 00c4f924 ["INT_ADD", "register:40f0:8", ["const:c4f924:8", "const:4:8"]]
- 00c4f924 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c50918 ["INT_ADD", "register:40f0:8", ["const:c50918:8", "const:4:8"]]
+ 00c50918 ["CALL", null, ["callee:00c461d4:8"]]
- 00c4f924 bytes 2fd6ff97
+ 00c50918 bytes 2fd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c78a6f0babaa76b4e41b9d414e745f3c"></a>

### [`00c4f9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md) → [`00c509ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c509ac.md) FUN_00c509ac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4f9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4f9d8) · [`00c4fa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4fa04) · [`00c4fa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f9b8.md#insn-00c4fa38)
- 新版 [`00c509cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c509ac.md#insn-00c509cc) · [`00c509f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c509ac.md#insn-00c509f8) · [`00c50a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c509ac.md#insn-00c50a2c)

~~~diff
- 00c4f9d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4f9d8 ["INT_ADD", "register:40f0:8", ["const:c4f9d8:8", "const:4:8"]]
- 00c4f9d8 ["CALLIND", null, ["register:0:8"]]
+ 00c509cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c509cc ["INT_ADD", "register:40f0:8", ["const:c509cc:8", "const:4:8"]]
+ 00c509cc ["CALLIND", null, ["register:0:8"]]
- 00c4f9d8 bytes 00013fd6
+ 00c509cc bytes 00013fd6
- 00c4fa04 ["INT_ADD", "register:40f0:8", ["const:c4fa04:8", "const:4:8"]]
- 00c4fa04 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c509f8 ["INT_ADD", "register:40f0:8", ["const:c509f8:8", "const:4:8"]]
+ 00c509f8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4fa04 bytes db290094
+ 00c509f8 bytes d2290094
- 00c4fa38 ["INT_ADD", "register:40f0:8", ["const:c4fa38:8", "const:4:8"]]
- 00c4fa38 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c50a2c ["INT_ADD", "register:40f0:8", ["const:c50a2c:8", "const:4:8"]]
+ 00c50a2c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c4fa38 bytes f62d0094
+ 00c50a2c bytes ed2d0094
~~~


<a id="compare-6ca2dcdd0b0f43c7a1604415920d31f2"></a>

### [`00c4fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md) → [`00c50dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50dcc.md) FUN_00c50dcc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4fe04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe04) · [`00c4fe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe28) · [`00c4fe54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fdd8.md#insn-00c4fe54)
- 新版 [`00c50df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50dcc.md#insn-00c50df8) · [`00c50e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50dcc.md#insn-00c50e1c) · [`00c50e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50dcc.md#insn-00c50e48)

~~~diff
- 00c4fe04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fe04 ["INT_ADD", "register:40f0:8", ["const:c4fe04:8", "const:4:8"]]
- 00c4fe04 ["CALLIND", null, ["register:0:8"]]
+ 00c50df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50df8 ["INT_ADD", "register:40f0:8", ["const:c50df8:8", "const:4:8"]]
+ 00c50df8 ["CALLIND", null, ["register:0:8"]]
- 00c4fe04 bytes 00013fd6
+ 00c50df8 bytes 00013fd6
- 00c4fe28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fe28 ["INT_ADD", "register:40f0:8", ["const:c4fe28:8", "const:4:8"]]
- 00c4fe28 ["CALLIND", null, ["register:0:8"]]
+ 00c50e1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50e1c ["INT_ADD", "register:40f0:8", ["const:c50e1c:8", "const:4:8"]]
+ 00c50e1c ["CALLIND", null, ["register:0:8"]]
- 00c4fe28 bytes 00013fd6
+ 00c50e1c bytes 00013fd6
- 00c4fe54 ["INT_ADD", "register:40f0:8", ["const:c4fe54:8", "const:4:8"]]
- 00c4fe54 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50e48 ["INT_ADD", "register:40f0:8", ["const:c50e48:8", "const:4:8"]]
+ 00c50e48 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4fe54 bytes c7280094
+ 00c50e48 bytes be280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337abfc68e82cbd1784b18d60734f2c4"></a>

### [`00c4ff4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md) → [`00c50f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50f40.md) FUN_00c50f40

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c4ff78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ff78) · [`00c4ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ff9c) · [`00c4ffc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4ff4c.md#insn-00c4ffc8)
- 新版 [`00c50f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50f40.md#insn-00c50f6c) · [`00c50f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50f40.md#insn-00c50f90) · [`00c50fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50f40.md#insn-00c50fbc)

~~~diff
- 00c4ff78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ff78 ["INT_ADD", "register:40f0:8", ["const:c4ff78:8", "const:4:8"]]
- 00c4ff78 ["CALLIND", null, ["register:0:8"]]
+ 00c50f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50f6c ["INT_ADD", "register:40f0:8", ["const:c50f6c:8", "const:4:8"]]
+ 00c50f6c ["CALLIND", null, ["register:0:8"]]
- 00c4ff78 bytes 00013fd6
+ 00c50f6c bytes 00013fd6
- 00c4ff9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ff9c ["INT_ADD", "register:40f0:8", ["const:c4ff9c:8", "const:4:8"]]
- 00c4ff9c ["CALLIND", null, ["register:0:8"]]
+ 00c50f90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50f90 ["INT_ADD", "register:40f0:8", ["const:c50f90:8", "const:4:8"]]
+ 00c50f90 ["CALLIND", null, ["register:0:8"]]
- 00c4ff9c bytes 00013fd6
+ 00c50f90 bytes 00013fd6
- 00c4ffc8 ["INT_ADD", "register:40f0:8", ["const:c4ffc8:8", "const:4:8"]]
- 00c4ffc8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50fbc ["INT_ADD", "register:40f0:8", ["const:c50fbc:8", "const:4:8"]]
+ 00c50fbc ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ffc8 bytes 6a280094
+ 00c50fbc bytes 61280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53231bcdf13d4176ade3ee5db57e7cd"></a>

### [`00c502e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md) → [`00c512d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c512d8.md) FUN_00c512d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c50338) · [`00c50354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c50354) · [`00c5038c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c502e4.md#insn-00c5038c)
- 新版 [`00c5132c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c512d8.md#insn-00c5132c) · [`00c51348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c512d8.md#insn-00c51348) · [`00c51380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c512d8.md#insn-00c51380)

~~~diff
- 00c50338 ["INT_ADD", "register:40f0:8", ["const:c50338:8", "const:4:8"]]
- 00c50338 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c5132c ["INT_ADD", "register:40f0:8", ["const:c5132c:8", "const:4:8"]]
+ 00c5132c ["CALL", null, ["callee:00c5b140:8"]]
- 00c50338 bytes 8e270094
+ 00c5132c bytes 85270094
- 00c50354 ["INT_ADD", "register:40f0:8", ["const:c50354:8", "const:4:8"]]
- 00c50354 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c51348 ["INT_ADD", "register:40f0:8", ["const:c51348:8", "const:4:8"]]
+ 00c51348 ["CALL", null, ["callee:00c590a0:8"]]
- 00c50354 bytes 5f1f0094
+ 00c51348 bytes 561f0094
- 00c5038c ["INT_ADD", "register:40f0:8", ["const:c5038c:8", "const:4:8"]]
- 00c5038c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51380 ["INT_ADD", "register:40f0:8", ["const:c51380:8", "const:4:8"]]
+ 00c51380 ["CALL", null, ["callee:00c5b140:8"]]
- 00c5038c bytes 79270094
+ 00c51380 bytes 70270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b9b7f005e977c1d88ab7e554d47f3fb"></a>

### [`00c50458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md) → [`00c5144c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5144c.md) FUN_00c5144c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5049c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c5049c) · [`00c504e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c504e8) · [`00c5052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50458.md#insn-00c5052c)
- 新版 [`00c51490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5144c.md#insn-00c51490) · [`00c514dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5144c.md#insn-00c514dc) · [`00c51520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5144c.md#insn-00c51520)

~~~diff
- 00c5049c ["INT_ADD", "register:40f0:8", ["const:c5049c:8", "const:4:8"]]
- 00c5049c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51490 ["INT_ADD", "register:40f0:8", ["const:c51490:8", "const:4:8"]]
+ 00c51490 ["CALL", null, ["callee:00c5b140:8"]]
- 00c5049c bytes 35270094
+ 00c51490 bytes 2c270094
- 00c504e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c504e8 ["INT_ADD", "register:40f0:8", ["const:c504e8:8", "const:4:8"]]
- 00c504e8 ["CALLIND", null, ["register:0:8"]]
+ 00c514dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c514dc ["INT_ADD", "register:40f0:8", ["const:c514dc:8", "const:4:8"]]
+ 00c514dc ["CALLIND", null, ["register:0:8"]]
- 00c504e8 bytes 00013fd6
+ 00c514dc bytes 00013fd6
- 00c5052c ["INT_ADD", "register:40f0:8", ["const:c5052c:8", "const:4:8"]]
- 00c5052c ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c51520 ["INT_ADD", "register:40f0:8", ["const:c51520:8", "const:4:8"]]
+ 00c51520 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c5052c bytes 392b0094
+ 00c51520 bytes 302b0094
~~~


<a id="compare-9c82d21a6e1590b7f6f2d9bc94e28ba3"></a>

### [`00c50820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md) → [`00c51814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51814.md) FUN_00c51814

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c50848) · [`00c50880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c50880) · [`00c5089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50820.md#insn-00c5089c)
- 新版 [`00c5183c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51814.md#insn-00c5183c) · [`00c51874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51814.md#insn-00c51874) · [`00c51890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51814.md#insn-00c51890)

~~~diff
- 00c50848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50848 ["INT_ADD", "register:40f0:8", ["const:c50848:8", "const:4:8"]]
- 00c50848 ["CALLIND", null, ["register:0:8"]]
+ 00c5183c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5183c ["INT_ADD", "register:40f0:8", ["const:c5183c:8", "const:4:8"]]
+ 00c5183c ["CALLIND", null, ["register:0:8"]]
- 00c50848 bytes 00013fd6
+ 00c5183c bytes 00013fd6
- 00c50880 ["INT_ADD", "register:40f0:8", ["const:c50880:8", "const:4:8"]]
- 00c50880 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51874 ["INT_ADD", "register:40f0:8", ["const:c51874:8", "const:4:8"]]
+ 00c51874 ["CALL", null, ["callee:00c5b140:8"]]
- 00c50880 bytes 3c260094
+ 00c51874 bytes 33260094
- 00c5089c ["INT_ADD", "register:40f0:8", ["const:c5089c:8", "const:4:8"]]
- 00c5089c ["CALL", null, ["callee:00c590a0:8"]]
+ 00c51890 ["INT_ADD", "register:40f0:8", ["const:c51890:8", "const:4:8"]]
+ 00c51890 ["CALL", null, ["callee:00c590a0:8"]]
- 00c5089c bytes 0d1e0094
+ 00c51890 bytes 041e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60dab87b3ac7f0eb1869dadb30d07ad6"></a>

### [`00c50b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md) → [`00c51b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51b30.md) FUN_00c51b30

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c50b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50b68) · [`00c50b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50b8c) · [`00c50bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50b3c.md#insn-00c50bb8)
- 新版 [`00c51b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51b30.md#insn-00c51b5c) · [`00c51b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51b30.md#insn-00c51b80) · [`00c51bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51b30.md#insn-00c51bac)

~~~diff
- 00c50b68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50b68 ["INT_ADD", "register:40f0:8", ["const:c50b68:8", "const:4:8"]]
- 00c50b68 ["CALLIND", null, ["register:0:8"]]
+ 00c51b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51b5c ["INT_ADD", "register:40f0:8", ["const:c51b5c:8", "const:4:8"]]
+ 00c51b5c ["CALLIND", null, ["register:0:8"]]
- 00c50b68 bytes 00013fd6
+ 00c51b5c bytes 00013fd6
- 00c50b8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50b8c ["INT_ADD", "register:40f0:8", ["const:c50b8c:8", "const:4:8"]]
- 00c50b8c ["CALLIND", null, ["register:0:8"]]
+ 00c51b80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51b80 ["INT_ADD", "register:40f0:8", ["const:c51b80:8", "const:4:8"]]
+ 00c51b80 ["CALLIND", null, ["register:0:8"]]
- 00c50b8c bytes 00013fd6
+ 00c51b80 bytes 00013fd6
- 00c50bb8 ["INT_ADD", "register:40f0:8", ["const:c50bb8:8", "const:4:8"]]
- 00c50bb8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51bac ["INT_ADD", "register:40f0:8", ["const:c51bac:8", "const:4:8"]]
+ 00c51bac ["CALL", null, ["callee:00c5b140:8"]]
- 00c50bb8 bytes 6e250094
+ 00c51bac bytes 65250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a924c0bffa5629f8b183df4c68313ca"></a>

### [`00c50ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md) → [`00c51fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51fec.md) FUN_00c51fec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5101c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c5101c) · [`00c51044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c51044) · [`00c51074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50ff8.md#insn-00c51074)
- 新版 [`00c52010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51fec.md#insn-00c52010) · [`00c52038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51fec.md#insn-00c52038) · [`00c52068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51fec.md#insn-00c52068)

~~~diff
- 00c5101c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5101c ["INT_ADD", "register:40f0:8", ["const:c5101c:8", "const:4:8"]]
- 00c5101c ["CALLIND", null, ["register:0:8"]]
+ 00c52010 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52010 ["INT_ADD", "register:40f0:8", ["const:c52010:8", "const:4:8"]]
+ 00c52010 ["CALLIND", null, ["register:0:8"]]
- 00c5101c bytes 00013fd6
+ 00c52010 bytes 00013fd6
- 00c51044 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51044 ["INT_ADD", "register:40f0:8", ["const:c51044:8", "const:4:8"]]
- 00c51044 ["CALLIND", null, ["register:0:8"]]
+ 00c52038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52038 ["INT_ADD", "register:40f0:8", ["const:c52038:8", "const:4:8"]]
+ 00c52038 ["CALLIND", null, ["register:0:8"]]
- 00c51044 bytes 00013fd6
+ 00c52038 bytes 00013fd6
- 00c51074 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51074 ["INT_ADD", "register:40f0:8", ["const:c51074:8", "const:4:8"]]
- 00c51074 ["CALLIND", null, ["register:0:8"]]
+ 00c52068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52068 ["INT_ADD", "register:40f0:8", ["const:c52068:8", "const:4:8"]]
+ 00c52068 ["CALLIND", null, ["register:0:8"]]
- 00c51074 bytes 00013fd6
+ 00c52068 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823c24b396de55b6fea36d6c687c9ccf"></a>

### [`00c511b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md) → [`00c521ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c521ac.md) FUN_00c521ac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c511f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c511f4) · [`00c51224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c51224) · [`00c51254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c511b8.md#insn-00c51254)
- 新版 [`00c521e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c521ac.md#insn-00c521e8) · [`00c52218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c521ac.md#insn-00c52218) · [`00c52248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c521ac.md#insn-00c52248)

~~~diff
- 00c511f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c511f4 ["INT_ADD", "register:40f0:8", ["const:c511f4:8", "const:4:8"]]
- 00c511f4 ["CALLIND", null, ["register:0:8"]]
+ 00c521e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c521e8 ["INT_ADD", "register:40f0:8", ["const:c521e8:8", "const:4:8"]]
+ 00c521e8 ["CALLIND", null, ["register:0:8"]]
- 00c511f4 bytes 00013fd6
+ 00c521e8 bytes 00013fd6
- 00c51224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51224 ["INT_ADD", "register:40f0:8", ["const:c51224:8", "const:4:8"]]
- 00c51224 ["CALLIND", null, ["register:0:8"]]
+ 00c52218 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52218 ["INT_ADD", "register:40f0:8", ["const:c52218:8", "const:4:8"]]
+ 00c52218 ["CALLIND", null, ["register:0:8"]]
- 00c51224 bytes 00013fd6
+ 00c52218 bytes 00013fd6
- 00c51254 ["INT_ADD", "register:40f0:8", ["const:c51254:8", "const:4:8"]]
- 00c51254 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c52248 ["INT_ADD", "register:40f0:8", ["const:c52248:8", "const:4:8"]]
+ 00c52248 ["CALL", null, ["callee:00c5b140:8"]]
- 00c51254 bytes c7230094
+ 00c52248 bytes be230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e3eb4c88ffdbbe3acbbc747bb288557"></a>

### [`00c512a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md) → [`00c52298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52298.md) FUN_00c52298

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c512f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c512f8) · [`00c51314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c51314) · [`00c5134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c512a4.md#insn-00c5134c)
- 新版 [`00c522ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52298.md#insn-00c522ec) · [`00c52308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52298.md#insn-00c52308) · [`00c52340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52298.md#insn-00c52340)

~~~diff
- 00c512f8 ["INT_ADD", "register:40f0:8", ["const:c512f8:8", "const:4:8"]]
- 00c512f8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c522ec ["INT_ADD", "register:40f0:8", ["const:c522ec:8", "const:4:8"]]
+ 00c522ec ["CALL", null, ["callee:00c5b140:8"]]
- 00c512f8 bytes 9e230094
+ 00c522ec bytes 95230094
- 00c51314 ["INT_ADD", "register:40f0:8", ["const:c51314:8", "const:4:8"]]
- 00c51314 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c52308 ["INT_ADD", "register:40f0:8", ["const:c52308:8", "const:4:8"]]
+ 00c52308 ["CALL", null, ["callee:00c590a0:8"]]
- 00c51314 bytes 6f1b0094
+ 00c52308 bytes 661b0094
- 00c5134c ["INT_ADD", "register:40f0:8", ["const:c5134c:8", "const:4:8"]]
- 00c5134c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c52340 ["INT_ADD", "register:40f0:8", ["const:c52340:8", "const:4:8"]]
+ 00c52340 ["CALL", null, ["callee:00c5b140:8"]]
- 00c5134c bytes 89230094
+ 00c52340 bytes 80230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc2942fabb8aa0b4e958692312f8f2b9"></a>

### [`00c5140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md) → [`00c52400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52400.md) FUN_00c52400

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c51498) · [`00c514c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c514c0) · [`00c514f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5140c.md#insn-00c514f0)
- 新版 [`00c5248c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52400.md#insn-00c5248c) · [`00c524b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52400.md#insn-00c524b4) · [`00c524e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52400.md#insn-00c524e4)

~~~diff
- 00c51498 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51498 ["INT_ADD", "register:40f0:8", ["const:c51498:8", "const:4:8"]]
- 00c51498 ["CALLIND", null, ["register:0:8"]]
+ 00c5248c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5248c ["INT_ADD", "register:40f0:8", ["const:c5248c:8", "const:4:8"]]
+ 00c5248c ["CALLIND", null, ["register:0:8"]]
- 00c51498 bytes 00013fd6
+ 00c5248c bytes 00013fd6
- 00c514c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c514c0 ["INT_ADD", "register:40f0:8", ["const:c514c0:8", "const:4:8"]]
- 00c514c0 ["CALLIND", null, ["register:0:8"]]
+ 00c524b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c524b4 ["INT_ADD", "register:40f0:8", ["const:c524b4:8", "const:4:8"]]
+ 00c524b4 ["CALLIND", null, ["register:0:8"]]
- 00c514c0 bytes 00013fd6
+ 00c524b4 bytes 00013fd6
- 00c514f0 ["INT_ADD", "register:40f0:8", ["const:c514f0:8", "const:4:8"]]
- 00c514f0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c524e4 ["INT_ADD", "register:40f0:8", ["const:c524e4:8", "const:4:8"]]
+ 00c524e4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c514f0 bytes 20230094
+ 00c524e4 bytes 17230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-551c9ee1ac6c51d94dcdba93f9d18aff"></a>

### [`00c5174c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md) → [`00c52740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52740.md) FUN_00c52740

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c517e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c517e8) · [`00c51818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c51818) · [`00c51848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c5174c.md#insn-00c51848)
- 新版 [`00c527dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52740.md#insn-00c527dc) · [`00c5280c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52740.md#insn-00c5280c) · [`00c5283c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52740.md#insn-00c5283c)

~~~diff
- 00c517e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c517e8 ["INT_ADD", "register:40f0:8", ["const:c517e8:8", "const:4:8"]]
- 00c517e8 ["CALLIND", null, ["register:0:8"]]
+ 00c527dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c527dc ["INT_ADD", "register:40f0:8", ["const:c527dc:8", "const:4:8"]]
+ 00c527dc ["CALLIND", null, ["register:0:8"]]
- 00c517e8 bytes 00013fd6
+ 00c527dc bytes 00013fd6
- 00c51818 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51818 ["INT_ADD", "register:40f0:8", ["const:c51818:8", "const:4:8"]]
- 00c51818 ["CALLIND", null, ["register:0:8"]]
+ 00c5280c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5280c ["INT_ADD", "register:40f0:8", ["const:c5280c:8", "const:4:8"]]
+ 00c5280c ["CALLIND", null, ["register:0:8"]]
- 00c51818 bytes 00013fd6
+ 00c5280c bytes 00013fd6
- 00c51848 ["INT_ADD", "register:40f0:8", ["const:c51848:8", "const:4:8"]]
- 00c51848 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c5283c ["INT_ADD", "register:40f0:8", ["const:c5283c:8", "const:4:8"]]
+ 00c5283c ["CALL", null, ["callee:00c5b140:8"]]
- 00c51848 bytes 4a220094
+ 00c5283c bytes 41220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcff89b556eb6d46368c4752a581eb73"></a>

### [`00c51ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md) → [`00c52adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52adc.md) FUN_00c52adc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c52c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b14) · [`00c51b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b44) · [`00c51b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md#insn-00c51b74)
- 新版 [`00c52b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52adc.md#insn-00c52b08) · [`00c52b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52adc.md#insn-00c52b38) · [`00c52b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52adc.md#insn-00c52b68)

~~~diff
- 00c51b14 ["INT_ADD", "register:40f0:8", ["const:c51b14:8", "const:4:8"]]
- 00c51b14 ["CALL", null, ["callee:00c52c04:8"]]
+ 00c52b08 ["INT_ADD", "register:40f0:8", ["const:c52b08:8", "const:4:8"]]
+ 00c52b08 ["CALL", null, ["callee:00c52c04:8"]]
- 00c51b14 bytes 3f000094
+ 00c52b08 bytes 3f000094
- 00c51b44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51b44 ["INT_ADD", "register:40f0:8", ["const:c51b44:8", "const:4:8"]]
- 00c51b44 ["CALLIND", null, ["register:0:8"]]
+ 00c52b38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52b38 ["INT_ADD", "register:40f0:8", ["const:c52b38:8", "const:4:8"]]
+ 00c52b38 ["CALLIND", null, ["register:0:8"]]
- 00c51b44 bytes 00013fd6
+ 00c52b38 bytes 00013fd6
- 00c51b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51b74 ["INT_ADD", "register:40f0:8", ["const:c51b74:8", "const:4:8"]]
- 00c51b74 ["CALLIND", null, ["register:0:8"]]
+ 00c52b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52b68 ["INT_ADD", "register:40f0:8", ["const:c52b68:8", "const:4:8"]]
+ 00c52b68 ["CALLIND", null, ["register:0:8"]]
- 00c51b74 bytes 00013fd6
+ 00c52b68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9eebf62f6a1dffedab4f1cffb2a9a2d"></a>

### [`00c51dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dbc.md) → [`00c52db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52db0.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a920.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8f0.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dbc.md#insn-00c51dc8)
- 新版 [`00c52dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52db0.md#insn-00c52dbc)

~~~diff
- 00c51dc8 ["INT_ADD", "register:40f0:8", ["const:c51dc8:8", "const:4:8"]]
- 00c51dc8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c52dbc ["INT_ADD", "register:40f0:8", ["const:c52dbc:8", "const:4:8"]]
+ 00c52dbc ["CALL", null, ["callee:00c58f30:8"]]
- 00c51dc8 bytes 66180094
+ 00c52dbc bytes 5d180094
~~~


<a id="compare-8d3779c1539075ce179f50e6ab2dead3"></a>

### [`00c51dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dec.md) → [`00c52de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52de0.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51dec.md#insn-00c51df8)
- 新版 [`00c52dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52de0.md#insn-00c52dec)

~~~diff
- 00c51df8 ["INT_ADD", "register:40f0:8", ["const:c51df8:8", "const:4:8"]]
- 00c51df8 ["CALL", null, ["callee:00c5cef0:8"]]
+ 00c52dec ["INT_ADD", "register:40f0:8", ["const:c52dec:8", "const:4:8"]]
+ 00c52dec ["CALL", null, ["callee:00c5cef0:8"]]
- 00c51df8 bytes 4a280094
+ 00c52dec bytes 41280094
~~~


<a id="compare-0a8e90876c02d0fd236dec333d2f9eda"></a>

### [`00c51e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e4c.md) → [`00c52e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52e40.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ff60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e4c.md#insn-00c51e58)
- 新版 [`00c52e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52e40.md#insn-00c52e4c)

~~~diff
- 00c51e58 ["INT_ADD", "register:40f0:8", ["const:c51e58:8", "const:4:8"]]
- 00c51e58 ["CALL", null, ["callee:00c5ff60:8"]]
+ 00c52e4c ["INT_ADD", "register:40f0:8", ["const:c52e4c:8", "const:4:8"]]
+ 00c52e4c ["CALL", null, ["callee:00c5ff60:8"]]
- 00c51e58 bytes 4e340094
+ 00c52e4c bytes 45340094
~~~


<a id="compare-96ed1699d8cbd78d5be6976fbfe79295"></a>

### [`00c51e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e7c.md) → [`00c52e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52e70.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5efb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ff80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51e7c.md#insn-00c51e88)
- 新版 [`00c52e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52e70.md#insn-00c52e7c)

~~~diff
- 00c51e88 ["INT_ADD", "register:40f0:8", ["const:c51e88:8", "const:4:8"]]
- 00c51e88 ["CALL", null, ["callee:00c5ff80:8"]]
+ 00c52e7c ["INT_ADD", "register:40f0:8", ["const:c52e7c:8", "const:4:8"]]
+ 00c52e7c ["CALL", null, ["callee:00c5ff80:8"]]
- 00c51e88 bytes 4a340094
+ 00c52e7c bytes 41340094
~~~


<a id="compare-48299886dd18fdce0542dbcc057298c3"></a>

### [`00c51f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md) → [`00c52f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f08.md) __cxa_allocate_exception

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) · 呼出先 3件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) · 呼出先 3件 [`00c536d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f2c) · [`00c51f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f44) · [`00c51f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md#insn-00c51f5c)
- 新版 [`00c52f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f08.md#insn-00c52f20) · [`00c52f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f08.md#insn-00c52f38) · [`00c52f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f08.md#insn-00c52f50)

~~~diff
- 00c51f2c ["INT_ADD", "register:40f0:8", ["const:c51f2c:8", "const:4:8"]]
- 00c51f2c ["CALL", null, ["callee:00c536d4:8"]]
+ 00c52f20 ["INT_ADD", "register:40f0:8", ["const:c52f20:8", "const:4:8"]]
+ 00c52f20 ["CALL", null, ["callee:00c536d4:8"]]
- 00c51f2c bytes ed010094
+ 00c52f20 bytes ed010094
- 00c51f44 ["INT_ADD", "register:40f0:8", ["const:c51f44:8", "const:4:8"]]
- 00c51f44 ["CALL", null, ["callee:00c59130:8"]]
+ 00c52f38 ["INT_ADD", "register:40f0:8", ["const:c52f38:8", "const:4:8"]]
+ 00c52f38 ["CALL", null, ["callee:00c59130:8"]]
- 00c51f44 bytes 87180094
+ 00c52f38 bytes 7e180094
- 00c51f5c ["INT_ADD", "register:40f0:8", ["const:c51f5c:8", "const:4:8"]]
- 00c51f5c ["CALL", null, ["callee:00c590c0:8"]]
+ 00c52f50 ["INT_ADD", "register:40f0:8", ["const:c52f50:8", "const:4:8"]]
+ 00c52f50 ["CALL", null, ["callee:00c590c0:8"]]
- 00c51f5c bytes 65180094
+ 00c52f50 bytes 5c180094
~~~


<a id="compare-bc8413689307695a1c5c8a53ac60f45b"></a>

### [`00c51f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md) → [`00c52f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f58.md) __cxa_begin_catch

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580e0.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)
- 新版 呼出元 1件 [`00c590b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590b0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5fe30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c51f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md#insn-00c51f78) · [`00c51ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f64.md#insn-00c51ff8)
- 新版 [`00c52f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f58.md#insn-00c52f6c) · [`00c52fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f58.md#insn-00c52fec)

~~~diff
- 00c51f78 ["INT_ADD", "register:40f0:8", ["const:c51f78:8", "const:4:8"]]
- 00c51f78 ["CALL", null, ["callee:00c5fe30:8"]]
+ 00c52f6c ["INT_ADD", "register:40f0:8", ["const:c52f6c:8", "const:4:8"]]
+ 00c52f6c ["CALL", null, ["callee:00c5fe30:8"]]
- 00c51f78 bytes ba330094
+ 00c52f6c bytes b1330094
- 00c51ff8 ["INT_ADD", "register:40f0:8", ["const:c51ff8:8", "const:4:8"]]
- 00c51ff8 ["CALL", null, ["callee:00c590c0:8"]]
+ 00c52fec ["INT_ADD", "register:40f0:8", ["const:c52fec:8", "const:4:8"]]
+ 00c52fec ["CALL", null, ["callee:00c590c0:8"]]
- 00c51ff8 bytes 3e180094
+ 00c52fec bytes 35180094
~~~


<a id="compare-4045d2cdaddde6e82301262714a36490"></a>

### [`00c520fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md) → [`00c530f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c530f0.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c536d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md#insn-00c5210c) · [`00c52134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md#insn-00c52134)
- 新版 [`00c53100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c530f0.md#insn-00c53100) · [`00c53128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c530f0.md#insn-00c53128)

~~~diff
- 00c5210c ["INT_ADD", "register:40f0:8", ["const:c5210c:8", "const:4:8"]]
- 00c5210c ["CALL", null, ["callee:00c536d4:8"]]
+ 00c53100 ["INT_ADD", "register:40f0:8", ["const:c53100:8", "const:4:8"]]
+ 00c53100 ["CALL", null, ["callee:00c536d4:8"]]
- 00c5210c bytes 75010094
+ 00c53100 bytes 75010094
- 00c52134 ["INT_ADD", "register:40f0:8", ["const:c52134:8", "const:4:8"]]
- 00c52134 ["CALL", null, ["callee:00c590c0:8"]]
+ 00c53128 ["INT_ADD", "register:40f0:8", ["const:c53128:8", "const:4:8"]]
+ 00c53128 ["CALL", null, ["callee:00c590c0:8"]]
- 00c52134 bytes ef170094
+ 00c53128 bytes e6170094
~~~


<a id="compare-ba533800f6be895f0171ba45e8ceff98"></a>

### [`00c52140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md) → [`00c53134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md) __cxa_throw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) · 呼出先 4件 [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c58400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58400.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)
- 新版 呼出元 1件 [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) · 呼出先 4件 [`00c53190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53190.md) [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c593d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593d0.md) [`00c5fe30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c52160) · [`00c5217c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c5217c) · [`00c52190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md#insn-00c52190)
- 新版 [`00c53154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md#insn-00c53154) · [`00c53170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md#insn-00c53170) · [`00c53184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md#insn-00c53184)

~~~diff
- 00c52160 ["INT_ADD", "register:40f0:8", ["const:c52160:8", "const:4:8"]]
- 00c52160 ["CALL", null, ["callee:00c5fe30:8"]]
+ 00c53154 ["INT_ADD", "register:40f0:8", ["const:c53154:8", "const:4:8"]]
+ 00c53154 ["CALL", null, ["callee:00c5fe30:8"]]
- 00c52160 bytes 40330094
+ 00c53154 bytes 37330094
- 00c5217c ["INT_ADD", "register:40f0:8", ["const:c5217c:8", "const:4:8"]]
- 00c5217c ["CALL", null, ["callee:00c593d0:8"]]
+ 00c53170 ["INT_ADD", "register:40f0:8", ["const:c53170:8", "const:4:8"]]
+ 00c53170 ["CALL", null, ["callee:00c593d0:8"]]
- 00c5217c bytes a1180094
+ 00c53170 bytes 98180094
- 00c52190 ["INT_ADD", "register:40f0:8", ["const:c52190:8", "const:4:8"]]
- 00c52190 ["CALL", null, ["callee:00c54dc0:8"]]
+ 00c53184 ["INT_ADD", "register:40f0:8", ["const:c53184:8", "const:4:8"]]
+ 00c53184 ["CALL", null, ["callee:00c54dc0:8"]]
- 00c52190 bytes 10070094
+ 00c53184 bytes 0f070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e43afc6d5d645a4f3ffe1caf6a6fddb"></a>

### [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) → [`00c53190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53190.md) FUN_00c53190

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c52140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md) · 呼出先 2件 [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c580e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580e0.md)
- 新版 呼出元 1件 [`00c53134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md) · 呼出先 2件 [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c590b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c521b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md#insn-00c521b4) · [`00c521bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md#insn-00c521bc)
- 新版 [`00c531a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53190.md#insn-00c531a8) · [`00c531b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53190.md#insn-00c531b0)

~~~diff
- 00c521b4 ["INT_ADD", "register:40f0:8", ["const:c521b4:8", "const:4:8"]]
- 00c521b4 ["CALL", null, ["callee:00c590b0:8"]]
+ 00c531a8 ["INT_ADD", "register:40f0:8", ["const:c531a8:8", "const:4:8"]]
+ 00c531a8 ["CALL", null, ["callee:00c590b0:8"]]
- 00c521b4 bytes cb170094
+ 00c531a8 bytes c2170094
- 00c521bc ["INT_ADD", "register:40f0:8", ["const:c521bc:8", "const:4:8"]]
- 00c521bc ["CALL", null, ["callee:00c38970:8"]]
+ 00c531b0 ["INT_ADD", "register:40f0:8", ["const:c531b0:8", "const:4:8"]]
+ 00c531b0 ["CALL", null, ["callee:00c38970:8"]]
- 00c521bc bytes f095ff97
+ 00c531b0 bytes f095ff97
~~~


<a id="compare-39f3a0adae44b2ffadd842e8d315a320"></a>

### [`00c52314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52314.md) → [`00c53308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53308.md) __cxa_current_exception_type

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52314.md#insn-00c52320)
- 新版 [`00c53314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53308.md#insn-00c53314)

~~~diff
- 00c52320 ["INT_ADD", "register:40f0:8", ["const:c52320:8", "const:4:8"]]
- 00c52320 ["CALL", null, ["callee:00c5fe40:8"]]
+ 00c53314 ["INT_ADD", "register:40f0:8", ["const:c53314:8", "const:4:8"]]
+ 00c53314 ["CALL", null, ["callee:00c5fe40:8"]]
- 00c52320 bytes d4320094
+ 00c53314 bytes cb320094
~~~


<a id="compare-7d312537c2a7db433ac27787adacb75f"></a>

### [`00c52364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md) → [`00c53358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md) __cxa_rethrow

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585d0.md) · 呼出先 5件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee60.md)
- 新版 呼出元 1件 [`00c595a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c595a0.md) · 呼出先 5件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5fe30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c52378) · [`00c52384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c52384) · [`00c523d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md#insn-00c523d0)
- 新版 [`00c5336c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md#insn-00c5336c) · [`00c53378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md#insn-00c53378) · [`00c533c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md#insn-00c533c4)

~~~diff
- 00c52378 ["INT_ADD", "register:40f0:8", ["const:c52378:8", "const:4:8"]]
- 00c52378 ["CALL", null, ["callee:00c5fe30:8"]]
+ 00c5336c ["INT_ADD", "register:40f0:8", ["const:c5336c:8", "const:4:8"]]
+ 00c5336c ["CALL", null, ["callee:00c5fe30:8"]]
- 00c52378 bytes ba320094
+ 00c5336c bytes b1320094
- 00c52384 ["INT_ADD", "register:40f0:8", ["const:c52384:8", "const:4:8"]]
- 00c52384 ["CALL", null, ["callee:00c590c0:8"]]
+ 00c53378 ["INT_ADD", "register:40f0:8", ["const:c53378:8", "const:4:8"]]
+ 00c53378 ["CALL", null, ["callee:00c590c0:8"]]
- 00c52384 bytes 5b170094
+ 00c53378 bytes 52170094
- 00c523d0 ["INT_ADD", "register:40f0:8", ["const:c523d0:8", "const:4:8"]]
- 00c523d0 ["CALL", null, ["callee:00c54dc0:8"]]
+ 00c533c4 ["INT_ADD", "register:40f0:8", ["const:c533c4:8", "const:4:8"]]
+ 00c533c4 ["CALL", null, ["callee:00c54dc0:8"]]
- 00c523d0 bytes 80060094
+ 00c533c4 bytes 7f060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f5b80bd3f8dac01bbd20c06e1f362f"></a>

### [`00c52448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52448.md) → [`00c5343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c5343c.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dff0.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efc0.md) · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52448.md#insn-00c52464)
- 新版 [`00c53458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c5343c.md#insn-00c53458)

~~~diff
- 00c52464 ["INT_ADD", "register:40f0:8", ["const:c52464:8", "const:4:8"]]
- 00c52464 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c53458 ["INT_ADD", "register:40f0:8", ["const:c53458:8", "const:4:8"]]
+ 00c53458 ["CALL", null, ["callee:00c54d90:8"]]
- 00c52464 bytes 4f060094
+ 00c53458 bytes 4e060094
~~~


<a id="compare-50eafb6fb8c8680c6e77ee68f735c4c3"></a>

### [`00c52474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md) → [`00c53468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53468.md) __cxa_current_primary_exception

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 1件 [`00c5efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efe0.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md#insn-00c52484) · [`00c524d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52474.md#insn-00c524d0)
- 新版 [`00c53478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53468.md#insn-00c53478) · [`00c534c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53468.md#insn-00c534c4)

~~~diff
- 00c52484 ["INT_ADD", "register:40f0:8", ["const:c52484:8", "const:4:8"]]
- 00c52484 ["CALL", null, ["callee:00c5fe40:8"]]
+ 00c53478 ["INT_ADD", "register:40f0:8", ["const:c53478:8", "const:4:8"]]
+ 00c53478 ["CALL", null, ["callee:00c5fe40:8"]]
- 00c52484 bytes 7b320094
+ 00c53478 bytes 72320094
- 00c524d0 ["INT_ADD", "register:40f0:8", ["const:c524d0:8", "const:4:8"]]
- 00c524d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c534c4 ["INT_ADD", "register:40f0:8", ["const:c534c4:8", "const:4:8"]]
+ 00c534c4 ["CALL", null, ["callee:00c54d90:8"]]
- 00c524d0 bytes 34060094
+ 00c534c4 bytes 33060094
~~~


<a id="compare-ef0e0e6042959849cff1c8336f86fa31"></a>

### [`00c52688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52688.md) → [`00c5367c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c5367c.md) __cxa_uncaught_exception

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52688.md#insn-00c52694)
- 新版 [`00c53688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c5367c.md#insn-00c53688)

~~~diff
- 00c52694 ["INT_ADD", "register:40f0:8", ["const:c52694:8", "const:4:8"]]
- 00c52694 ["CALL", null, ["callee:00c5fe40:8"]]
+ 00c53688 ["INT_ADD", "register:40f0:8", ["const:c53688:8", "const:4:8"]]
+ 00c53688 ["CALL", null, ["callee:00c5fe40:8"]]
- 00c52694 bytes f7310094
+ 00c53688 bytes ee310094
~~~


<a id="compare-315b3c3cb911a2dfc0810d99b72a4dfc"></a>

### [`00c526b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526b8.md) → [`00c536ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536ac.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfd0.md) · 呼出先 1件 [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 1件 [`00c5efa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efa0.md) · 呼出先 1件 [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c526c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526b8.md#insn-00c526c4)
- 新版 [`00c536b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536ac.md#insn-00c536b8)

~~~diff
- 00c526c4 ["INT_ADD", "register:40f0:8", ["const:c526c4:8", "const:4:8"]]
- 00c526c4 ["CALL", null, ["callee:00c5fe40:8"]]
+ 00c536b8 ["INT_ADD", "register:40f0:8", ["const:c536b8:8", "const:4:8"]]
+ 00c536b8 ["CALL", null, ["callee:00c5fe40:8"]]
- 00c526c4 bytes eb310094
+ 00c536b8 bytes e2310094
~~~


<a id="compare-bfb8828fa1fb1bbe67c5f69de05d7736"></a>

### [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) → [`00c536d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md) FUN_00c536d4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c51f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51f14.md) [`00c520fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c520fc.md) [`00c524f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c524f4.md) · 呼出先 2件 [`00c5272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md) [`00c5efa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efa0.md)
- 新版 呼出元 3件 [`00c52f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52f08.md) [`00c530f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c530f0.md) [`00c534e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c534e8.md) · 呼出先 2件 [`00c53720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53720.md) [`00c5ff70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c52708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md#insn-00c52708) · [`00c52718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md#insn-00c52718)
- 新版 [`00c536fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md#insn-00c536fc) · [`00c5370c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md#insn-00c5370c)

~~~diff
- 00c52708 ["INT_ADD", "register:40f0:8", ["const:c52708:8", "const:4:8"]]
- 00c52708 ["CALL", null, ["callee:00c5ff70:8"]]
+ 00c536fc ["INT_ADD", "register:40f0:8", ["const:c536fc:8", "const:4:8"]]
+ 00c536fc ["CALL", null, ["callee:00c5ff70:8"]]
- 00c52708 bytes 26320094
+ 00c536fc bytes 1d320094
- 00c52718 ["INT_ADD", "register:40f0:8", ["const:c52718:8", "const:4:8"]]
- 00c52718 ["CALL", null, ["callee:00c53720:8"]]
+ 00c5370c ["INT_ADD", "register:40f0:8", ["const:c5370c:8", "const:4:8"]]
+ 00c5370c ["CALL", null, ["callee:00c53720:8"]]
- 00c52718 bytes 05000094
+ 00c5370c bytes 05000094
~~~


<a id="compare-e43f722459a9674d79765c07d2f40b44"></a>

### [`00c5319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md) → [`00c54190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54190.md) FUN_00c54190

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) [`00c53344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53344.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 3件 [`00c539d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md) [`00c53f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md) [`00c54338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54338.md) · 呼出先 1件 [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c5333c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md#insn-00c5333c) · [`00c53340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md#insn-00c53340)
- 新版 [`00c54330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54190.md#insn-00c54330) · [`00c54334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54190.md#insn-00c54334)

~~~diff
- 00c5333c ["INT_ADD", "register:40f0:8", ["const:c5333c:8", "const:4:8"]]
- 00c5333c ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c54330 ["INT_ADD", "register:40f0:8", ["const:c54330:8", "const:4:8"]]
+ 00c54330 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c5333c bytes b51f0094
+ 00c54330 bytes ac1f0094
- 00c53340 ["INT_ADD", "register:40f0:8", ["const:c53340:8", "const:4:8"]]
- 00c53340 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c54334 ["INT_ADD", "register:40f0:8", ["const:c54334:8", "const:4:8"]]
+ 00c54334 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c53340 bytes b41f0094
+ 00c54334 bytes ab1f0094
~~~


<a id="compare-f42611f72af0bff0a6bd4a5d6e0b554c"></a>

### [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) → [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) FUN_00c54dc0

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c52140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52140.md) [`00c52364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md) [`00c524f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c524f4.md) · 呼出先 6件 [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) [`00c542e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md) [`00c54450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54450.md) [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md)
- 新版 呼出元 3件 [`00c53134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53134.md) [`00c53358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md) [`00c534e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c534e8.md) · 呼出先 6件 [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c55230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md) [`00c552d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md) [`00c55440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55440.md) [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c53dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md#insn-00c53dec) · [`00c53dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md#insn-00c53dfc) · [`00c53e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md#insn-00c53e04)
- 新版 [`00c54ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md#insn-00c54ddc) · [`00c54dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md#insn-00c54dec) · [`00c54df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md#insn-00c54df4)

~~~diff
- 00c53dec ["INT_ADD", "register:40f0:8", ["const:c53dec:8", "const:4:8"]]
- 00c53dec ["CALL", null, ["callee:00c58cd8:8"]]
+ 00c54ddc ["INT_ADD", "register:40f0:8", ["const:c54ddc:8", "const:4:8"]]
+ 00c54ddc ["CALL", null, ["callee:00c58cd8:8"]]
- 00c53dec bytes bf0f0094
+ 00c54ddc bytes bf0f0094
- 00c53dfc ["INT_ADD", "register:40f0:8", ["const:c53dfc:8", "const:4:8"]]
- 00c53dfc ["CALL", null, ["callee:00c55230:8"]]
+ 00c54dec ["INT_ADD", "register:40f0:8", ["const:c54dec:8", "const:4:8"]]
+ 00c54dec ["CALL", null, ["callee:00c55230:8"]]
- 00c53dfc bytes 11010094
+ 00c54dec bytes 11010094
- 00c53e04 ["INT_ADD", "register:40f0:8", ["const:c53e04:8", "const:4:8"]]
- 00c53e04 ["CALL", null, ["callee:00c55440:8"]]
+ 00c54df4 ["INT_ADD", "register:40f0:8", ["const:c54df4:8", "const:4:8"]]
+ 00c54df4 ["CALL", null, ["callee:00c55440:8"]]
- 00c53e04 bytes 93010094
+ 00c54df4 bytes 93010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

