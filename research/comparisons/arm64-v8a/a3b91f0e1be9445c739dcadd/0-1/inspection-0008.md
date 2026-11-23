# v15.7.2 → v15.7.3 · 要調査の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-ef361b7c8eaaaf431a016b0492b9cefb"></a>

### [`00bd56c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md) → [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) FUN_00bd5790

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bd4efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md) [`00bd50e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd50e4.md) [`00bd54dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd54dc.md) · 呼出先 2件 [`00bd5714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5714.md) [`00be1e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e10.md)
- 新版 呼出元 3件 [`00bd4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md) [`00bd51ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md) [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 2件 [`00bd57dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md) [`00be1ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd56f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md#insn-00bd56f0) · [`00bd5700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md#insn-00bd5700)
- 新版 [`00bd57b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md#insn-00bd57b8) · [`00bd57c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md#insn-00bd57c8)

~~~diff
- 00bd56f0 ["INT_ADD", "register:40f0:8", ["const:bd56f0:8", "const:4:8"]]
- 00bd56f0 ["CALL", null, ["callee:00be1ec0:8"]]
+ 00bd57b8 ["INT_ADD", "register:40f0:8", ["const:bd57b8:8", "const:4:8"]]
+ 00bd57b8 ["CALL", null, ["callee:00be1ec0:8"]]
- 00bd56f0 bytes c8310094
+ 00bd57b8 bytes c2310094
- 00bd5700 ["INT_ADD", "register:40f0:8", ["const:bd5700:8", "const:4:8"]]
- 00bd5700 ["CALL", null, ["callee:00bd57dc:8"]]
+ 00bd57c8 ["INT_ADD", "register:40f0:8", ["const:bd57c8:8", "const:4:8"]]
+ 00bd57c8 ["CALL", null, ["callee:00bd57dc:8"]]
- 00bd5700 bytes 05000094
+ 00bd57c8 bytes 05000094
~~~


<a id="compare-7020ea917f906e290430adea3c7a2b2d"></a>

### [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) → [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) __gxx_personality_v0

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bd4ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ecc.md) [`00bd6184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6184.md) [`00bd632c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md) [`00bd7164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7164.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md#insn-00bd5a4c) · [`00bd5a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md#insn-00bd5a5c) · [`00bd5a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md#insn-00bd5a68)
- 新版 [`00bd5b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b14) · [`00bd5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b24) · [`00bd5b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md#insn-00bd5b30)

~~~diff
- 00bd5a4c ["INT_ADD", "register:40f0:8", ["const:bd5a4c:8", "const:4:8"]]
- 00bd5a4c ["CALL", null, ["callee:00bd72a8:8"]]
+ 00bd5b14 ["INT_ADD", "register:40f0:8", ["const:bd5b14:8", "const:4:8"]]
+ 00bd5b14 ["CALL", null, ["callee:00bd72a8:8"]]
- 00bd5a4c bytes e7050094
+ 00bd5b14 bytes e5050094
- 00bd5a5c ["INT_ADD", "register:40f0:8", ["const:bd5a5c:8", "const:4:8"]]
- 00bd5a5c ["CALL", null, ["callee:00bd72a8:8"]]
+ 00bd5b24 ["INT_ADD", "register:40f0:8", ["const:bd5b24:8", "const:4:8"]]
+ 00bd5b24 ["CALL", null, ["callee:00bd72a8:8"]]
- 00bd5a5c bytes e3050094
+ 00bd5b24 bytes e1050094
- 00bd5a68 ["INT_ADD", "register:40f0:8", ["const:bd5a68:8", "const:4:8"]]
- 00bd5a68 ["CALL", null, ["callee:00bd72e0:8"]]
+ 00bd5b30 ["INT_ADD", "register:40f0:8", ["const:bd5b30:8", "const:4:8"]]
+ 00bd5b30 ["CALL", null, ["callee:00bd72e0:8"]]
- 00bd5a68 bytes ee050094
+ 00bd5b30 bytes ec050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e58f1aaf28fa4d86075b15363e7f4f"></a>

### [`00bd6184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6184.md) → [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) FUN_00bd624c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) [`00bd5f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md) [`00bd632c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md) · 呼出先 1件 [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 3件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd6324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6184.md#insn-00bd6324) · [`00bd6328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6184.md#insn-00bd6328)
- 新版 [`00bd63ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md#insn-00bd63ec) · [`00bd63f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md#insn-00bd63f0)

~~~diff
- 00bd6324 ["INT_ADD", "register:40f0:8", ["const:bd6324:8", "const:4:8"]]
- 00bd6324 ["CALL", null, ["callee:00bde270:8"]]
+ 00bd63ec ["INT_ADD", "register:40f0:8", ["const:bd63ec:8", "const:4:8"]]
+ 00bd63ec ["CALL", null, ["callee:00bde270:8"]]
- 00bd6324 bytes a71f0094
+ 00bd63ec bytes a11f0094
- 00bd6328 ["INT_ADD", "register:40f0:8", ["const:bd6328:8", "const:4:8"]]
- 00bd6328 ["CALL", null, ["callee:00bde270:8"]]
+ 00bd63f0 ["INT_ADD", "register:40f0:8", ["const:bd63f0:8", "const:4:8"]]
+ 00bd63f0 ["CALL", null, ["callee:00bde270:8"]]
- 00bd6328 bytes a61f0094
+ 00bd63f0 bytes a01f0094
~~~


<a id="compare-9de906f32630fdb6cb223c42015f2a12"></a>

### [`00bd632c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md) → [`00bd63f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md) FUN_00bd63f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) [`00bd5f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md) · 呼出先 4件 [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bd6184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6184.md) [`00bdb0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 2件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) · 呼出先 4件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd624c.md) [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd63d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md#insn-00bd63d8) · [`00bd63f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md#insn-00bd63f0) · [`00bd6434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd632c.md#insn-00bd6434)
- 新版 [`00bd64a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64a0) · [`00bd64b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64b8) · [`00bd64fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd63f4.md#insn-00bd64fc)

~~~diff
- 00bd63d8 ["INT_ADD", "register:40f0:8", ["const:bd63d8:8", "const:4:8"]]
- 00bd63d8 ["CALL", null, ["callee:00bd624c:8"]]
+ 00bd64a0 ["INT_ADD", "register:40f0:8", ["const:bd64a0:8", "const:4:8"]]
+ 00bd64a0 ["CALL", null, ["callee:00bd624c:8"]]
- 00bd63d8 bytes 6bffff97
+ 00bd64a0 bytes 6bffff97
- 00bd63f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd63f0 ["INT_ADD", "register:40f0:8", ["const:bd63f0:8", "const:4:8"]]
- 00bd63f0 ["CALLIND", null, ["register:0:8"]]
+ 00bd64b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd64b8 ["INT_ADD", "register:40f0:8", ["const:bd64b8:8", "const:4:8"]]
+ 00bd64b8 ["CALLIND", null, ["register:0:8"]]
- 00bd63f0 bytes 00013fd6
+ 00bd64b8 bytes 00013fd6
- 00bd6434 ["INT_ADD", "register:40f0:8", ["const:bd6434:8", "const:4:8"]]
- 00bd6434 ["CALL", null, ["callee:00bdb170:8"]]
+ 00bd64fc ["INT_ADD", "register:40f0:8", ["const:bd64fc:8", "const:4:8"]]
+ 00bd64fc ["CALL", null, ["callee:00bdb170:8"]]
- 00bd6434 bytes 23130094
+ 00bd64fc bytes 1d130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ff4c2c0612bf369f2093da3ee03830a"></a>

### [`00bd7164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7164.md) → [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md) FUN_00bd7224

採用 · 移動量 `+0xc0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) · 呼出先 1件 [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md)
- 新版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7164.md#insn-00bd7178)
- 新版 [`00bd7238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md#insn-00bd7238)

~~~diff
- 00bd7178 ["INT_ADD", "register:40f0:8", ["const:bd7178:8", "const:4:8"]]
- 00bd7178 ["CALL", null, ["callee:00bd7528:8"]]
+ 00bd7238 ["INT_ADD", "register:40f0:8", ["const:bd7238:8", "const:4:8"]]
+ 00bd7238 ["CALL", null, ["callee:00bd7528:8"]]
- 00bd7178 bytes bc000094
+ 00bd7238 bytes bc000094
~~~


<a id="compare-a07d9a156df7d2acaecc6adf2568b1ae"></a>

### [`00bd7198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7198.md) → [`00bd7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md) FUN_00bd7258

採用 · 移動量 `+0xc0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) · 呼出先 1件 [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md)
- 新版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd71ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7198.md#insn-00bd71ac)
- 新版 [`00bd726c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md#insn-00bd726c)

~~~diff
- 00bd71ac ["INT_ADD", "register:40f0:8", ["const:bd71ac:8", "const:4:8"]]
- 00bd71ac ["CALL", null, ["callee:00bd7528:8"]]
+ 00bd726c ["INT_ADD", "register:40f0:8", ["const:bd726c:8", "const:4:8"]]
+ 00bd726c ["CALL", null, ["callee:00bd7528:8"]]
- 00bd71ac bytes af000094
+ 00bd726c bytes af000094
~~~


<a id="compare-1ddd1d5fa988b038821cef8ff6243c68"></a>

### [`00bd71f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd71f0.md) → [`00bd72b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md) FUN_00bd72b0

採用 · 移動量 `+0xc0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd59cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd59cc.md) · 呼出先 1件 [`00bd72d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md)
- 新版 呼出元 1件 [`00bd5a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5a94.md) · 呼出先 1件 [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd71f0.md#insn-00bd7208)
- 新版 [`00bd72c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md#insn-00bd72c8)

~~~diff
- 00bd7208 ["INT_ADD", "register:40f0:8", ["const:bd7208:8", "const:4:8"]]
- 00bd7208 ["CALL", null, ["callee:00bd7398:8"]]
+ 00bd72c8 ["INT_ADD", "register:40f0:8", ["const:bd72c8:8", "const:4:8"]]
+ 00bd72c8 ["CALL", null, ["callee:00bd7398:8"]]
- 00bd7208 bytes 34000094
+ 00bd72c8 bytes 34000094
~~~


<a id="compare-518f1e6b34f163b2fda8b57f4ddbaa2b"></a>

### [`00bd72d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md) → [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) FUN_00bd7398

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd71f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd71f0.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd72b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md#insn-00bd7300) · [`00bd7318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md#insn-00bd7318)
- 新版 [`00bd73c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md#insn-00bd73c0) · [`00bd73d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md#insn-00bd73d8)

~~~diff
- 00bd7300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7300 ["INT_ADD", "register:40f0:8", ["const:bd7300:8", "const:4:8"]]
- 00bd7300 ["CALLIND", null, ["register:0:8"]]
+ 00bd73c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd73c0 ["INT_ADD", "register:40f0:8", ["const:bd73c0:8", "const:4:8"]]
+ 00bd73c0 ["CALLIND", null, ["register:0:8"]]
- 00bd7300 bytes 00013fd6
+ 00bd73c0 bytes 00013fd6
- 00bd7318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7318 ["INT_ADD", "register:40f0:8", ["const:bd7318:8", "const:4:8"]]
- 00bd7318 ["CALLIND", null, ["register:0:8"]]
+ 00bd73d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd73d8 ["INT_ADD", "register:40f0:8", ["const:bd73d8:8", "const:4:8"]]
+ 00bd73d8 ["CALLIND", null, ["register:0:8"]]
- 00bd7318 bytes 00013fd6
+ 00bd73d8 bytes 00013fd6
~~~


<a id="compare-1768d3255ca227db7537ce673d1bab4b"></a>

### [`00bd7354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7354.md) → [`00bd7414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md) FUN_00bd7414

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd71e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd71e8.md) [`00bd7220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7220.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00bd72a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72a8.md) [`00bd72e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7354.md#insn-00bd7380) · [`00bd739c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7354.md#insn-00bd739c) · [`00bd73b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7354.md#insn-00bd73b8)
- 新版 [`00bd7440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd7440) · [`00bd745c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd745c) · [`00bd7478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7414.md#insn-00bd7478)

~~~diff
- 00bd7380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7380 ["INT_ADD", "register:40f0:8", ["const:bd7380:8", "const:4:8"]]
- 00bd7380 ["CALLIND", null, ["register:0:8"]]
+ 00bd7440 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7440 ["INT_ADD", "register:40f0:8", ["const:bd7440:8", "const:4:8"]]
+ 00bd7440 ["CALLIND", null, ["register:0:8"]]
- 00bd7380 bytes 00013fd6
+ 00bd7440 bytes 00013fd6
- 00bd739c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd739c ["INT_ADD", "register:40f0:8", ["const:bd739c:8", "const:4:8"]]
- 00bd739c ["CALLIND", null, ["register:0:8"]]
+ 00bd745c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd745c ["INT_ADD", "register:40f0:8", ["const:bd745c:8", "const:4:8"]]
+ 00bd745c ["CALLIND", null, ["register:0:8"]]
- 00bd739c bytes 00013fd6
+ 00bd745c bytes 00013fd6
- 00bd73b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd73b8 ["INT_ADD", "register:40f0:8", ["const:bd73b8:8", "const:4:8"]]
- 00bd73b8 ["CALLIND", null, ["register:0:8"]]
+ 00bd7478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7478 ["INT_ADD", "register:40f0:8", ["const:bd7478:8", "const:4:8"]]
+ 00bd7478 ["CALLIND", null, ["register:0:8"]]
- 00bd73b8 bytes 00013fd6
+ 00bd7478 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0f4122fd9bb8bd7eceafbc87d8969d5"></a>

### [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md) → [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) FUN_00bd7528

採用 · 移動量 `+0xc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd7070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md) [`00bd7164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7164.md) [`00bd7198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7198.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) [`00bd7224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7224.md) [`00bd7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7258.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md#insn-00bd7484)
- 新版 [`00bd7544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md#insn-00bd7544)

~~~diff
- 00bd7484 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7484 ["INT_ADD", "register:40f0:8", ["const:bd7484:8", "const:4:8"]]
- 00bd7484 ["CALLIND", null, ["register:0:8"]]
+ 00bd7544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7544 ["INT_ADD", "register:40f0:8", ["const:bd7544:8", "const:4:8"]]
+ 00bd7544 ["CALLIND", null, ["register:0:8"]]
- 00bd7484 bytes 00013fd6
+ 00bd7544 bytes 00013fd6
~~~


<a id="compare-5297134d8637b63b7b266d9e606f89c5"></a>

### [`00bd74a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74a8.md) → [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md) FUN_00bd7568

採用 · 移動量 `+0xc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd7070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd74bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74a8.md#insn-00bd74bc)
- 新版 [`00bd757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md#insn-00bd757c)

~~~diff
- 00bd74bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd74bc ["INT_ADD", "register:40f0:8", ["const:bd74bc:8", "const:4:8"]]
- 00bd74bc ["CALLIND", null, ["register:0:8"]]
+ 00bd757c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd757c ["INT_ADD", "register:40f0:8", ["const:bd757c:8", "const:4:8"]]
+ 00bd757c ["CALLIND", null, ["register:0:8"]]
- 00bd74bc bytes 00013fd6
+ 00bd757c bytes 00013fd6
~~~


