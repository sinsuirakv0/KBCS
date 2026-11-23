# v15.7.2 → v15.7.3 · 要調査の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-7e1790e4527c0478e953d78863aed7d3"></a>

### [`00b59c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59c20.md) → [`00b59ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md) _ZN8firebase13remote_config8internal37JniConfigUpdateListener_nativeOnErrorEP7_JNIEnvP8_jobjectli

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b00fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59c20.md#insn-00b59c70) · [`00b59cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59c20.md#insn-00b59cac) · [`00b59cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59c20.md#insn-00b59cc4)
- 新版 [`00b59d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d38) · [`00b59d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d74) · [`00b59d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md#insn-00b59d8c)

~~~diff
- 00b59c70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59c70 ["INT_ADD", "register:40f0:8", ["const:b59c70:8", "const:4:8"]]
- 00b59c70 ["CALLIND", null, ["register:0:8"]]
+ 00b59d38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59d38 ["INT_ADD", "register:40f0:8", ["const:b59d38:8", "const:4:8"]]
+ 00b59d38 ["CALLIND", null, ["register:0:8"]]
- 00b59c70 bytes 00013fd6
+ 00b59d38 bytes 00013fd6
- 00b59cac ["INT_ADD", "register:40f0:8", ["const:b59cac:8", "const:4:8"]]
- 00b59cac ["CALL", null, ["callee:00bdb010:8"]]
+ 00b59d74 ["INT_ADD", "register:40f0:8", ["const:b59d74:8", "const:4:8"]]
+ 00b59d74 ["CALL", null, ["callee:00bdb010:8"]]
- 00b59cac bytes ad040294
+ 00b59d74 bytes a7040294
- 00b59cc4 ["INT_ADD", "register:40f0:8", ["const:b59cc4:8", "const:4:8"]]
- 00b59cc4 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b59d8c ["INT_ADD", "register:40f0:8", ["const:b59d8c:8", "const:4:8"]]
+ 00b59d8c ["CALL", null, ["callee:00bdb010:8"]]
- 00b59cc4 bytes a7040294
+ 00b59d8c bytes a1040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2fb34101530750e3626834f8d6f56e"></a>

### [`00b59d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59d54.md) → [`00b59e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase7VariantEEENS_19__map_value_compar

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0860.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md) [`00be0850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0850.md)
- 新版 呼出元 1件 [`00be0910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0910.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00be0900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0900.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59d54.md#insn-00b59d88) · [`00b59da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59d54.md#insn-00b59da4) · [`00b59dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59d54.md#insn-00b59dcc)
- 新版 [`00b59e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e50) · [`00b59e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e6c) · [`00b59e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59e1c.md#insn-00b59e94)

~~~diff
- 00b59d88 ["INT_ADD", "register:40f0:8", ["const:b59d88:8", "const:4:8"]]
- 00b59d88 ["CALL", null, ["callee:00be0900:8"]]
+ 00b59e50 ["INT_ADD", "register:40f0:8", ["const:b59e50:8", "const:4:8"]]
+ 00b59e50 ["CALL", null, ["callee:00be0900:8"]]
- 00b59d88 bytes b21a0294
+ 00b59e50 bytes ac1a0294
- 00b59da4 ["INT_ADD", "register:40f0:8", ["const:b59da4:8", "const:4:8"]]
- 00b59da4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b59e6c ["INT_ADD", "register:40f0:8", ["const:b59e6c:8", "const:4:8"]]
+ 00b59e6c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b59da4 bytes 67040294
+ 00b59e6c bytes 61040294
- 00b59dcc ["INT_ADD", "register:40f0:8", ["const:b59dcc:8", "const:4:8"]]
- 00b59dcc ["CALL", null, ["callee:00bdd9a0:8"]]
+ 00b59e94 ["INT_ADD", "register:40f0:8", ["const:b59e94:8", "const:4:8"]]
+ 00b59e94 ["CALL", null, ["callee:00bdd9a0:8"]]
- 00b59dcc bytes c90e0294
+ 00b59e94 bytes c30e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd1fb6f26b146dc7d054d606208aec2"></a>

### [`00b59f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f64.md) → [`00b5a02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md) FUN_00b5a02c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b597c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b597c0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be05b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05b0.md)
- 新版 呼出元 1件 [`00b59888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59f64.md#insn-00b59f78)
- 新版 [`00b5a040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md#insn-00b5a040)

~~~diff
- 00b59f78 ["INT_ADD", "register:40f0:8", ["const:b59f78:8", "const:4:8"]]
- 00b59f78 ["CALL", null, ["callee:00be0660:8"]]
+ 00b5a040 ["INT_ADD", "register:40f0:8", ["const:b5a040:8", "const:4:8"]]
+ 00b5a040 ["CALL", null, ["callee:00be0660:8"]]
- 00b59f78 bytes 8e190294
+ 00b5a040 bytes 88190294
~~~


<a id="compare-05a70d2a97fcb8daa0a6c3a2de4eb557"></a>

### [`00b5b264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b264.md) → [`00b5b32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be09b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09b0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddae0.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) [`00be08a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08a0.md)
- 新版 呼出元 1件 [`00be0a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a60.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00be0950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b264.md#insn-00b5b274) · [`00b5b290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b264.md#insn-00b5b290) · [`00b5b2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b264.md#insn-00b5b2a0)
- 新版 [`00b5b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b33c) · [`00b5b358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b358) · [`00b5b368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b32c.md#insn-00b5b368)

~~~diff
- 00b5b274 ["INT_ADD", "register:40f0:8", ["const:b5b274:8", "const:4:8"]]
- 00b5b274 ["CALL", null, ["callee:00be0950:8"]]
+ 00b5b33c ["INT_ADD", "register:40f0:8", ["const:b5b33c:8", "const:4:8"]]
+ 00b5b33c ["CALL", null, ["callee:00be0950:8"]]
- 00b5b274 bytes 8b150294
+ 00b5b33c bytes 85150294
- 00b5b290 ["INT_ADD", "register:40f0:8", ["const:b5b290:8", "const:4:8"]]
- 00b5b290 ["CALL", null, ["callee:00be0a20:8"]]
+ 00b5b358 ["INT_ADD", "register:40f0:8", ["const:b5b358:8", "const:4:8"]]
+ 00b5b358 ["CALL", null, ["callee:00be0a20:8"]]
- 00b5b290 bytes b8150294
+ 00b5b358 bytes b2150294
- 00b5b2a0 ["INT_ADD", "register:40f0:8", ["const:b5b2a0:8", "const:4:8"]]
- 00b5b2a0 ["CALL", null, ["callee:00be0a10:8"]]
+ 00b5b368 ["INT_ADD", "register:40f0:8", ["const:b5b368:8", "const:4:8"]]
+ 00b5b368 ["CALL", null, ["callee:00be0a10:8"]]
- 00b5b2a0 bytes b0150294
+ 00b5b368 bytes aa150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7812c4d673ef3baa6f3f3133ca2bf86c"></a>

### [`00b5b3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b3b0.md) → [`00b5b478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b478.md) _ZN8firebase4auth4AuthD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be09e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b3b0.md#insn-00b5b3b8)
- 新版 [`00b5b480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b478.md#insn-00b5b480)

~~~diff
- 00b5b3b8 ["INT_ADD", "register:40f0:8", ["const:b5b3b8:8", "const:4:8"]]
- 00b5b3b8 ["CALL", null, ["callee:00be09e0:8"]]
+ 00b5b480 ["INT_ADD", "register:40f0:8", ["const:b5b480:8", "const:4:8"]]
+ 00b5b480 ["CALL", null, ["callee:00be09e0:8"]]
- 00b5b3b8 bytes 5e150294
+ 00b5b480 bytes 58150294
~~~


<a id="compare-b9527025e5fa66106092d4796cebc5e7"></a>

### [`00b5c3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3b0.md) → [`00b5c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be09c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09c0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be09c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09c0.md)
- 新版 呼出元 1件 [`00be0a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a70.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3b0.md#insn-00b5c3cc) · [`00b5c3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3b0.md#insn-00b5c3d8)
- 新版 [`00b5c494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md#insn-00b5c494) · [`00b5c4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c478.md#insn-00b5c4a0)

~~~diff
- 00b5c3cc ["INT_ADD", "register:40f0:8", ["const:b5c3cc:8", "const:4:8"]]
- 00b5c3cc ["CALL", null, ["callee:00be0a70:8"]]
+ 00b5c494 ["INT_ADD", "register:40f0:8", ["const:b5c494:8", "const:4:8"]]
+ 00b5c494 ["CALL", null, ["callee:00be0a70:8"]]
- 00b5c3cc bytes 7d110294
+ 00b5c494 bytes 77110294
- 00b5c3d8 ["INT_ADD", "register:40f0:8", ["const:b5c3d8:8", "const:4:8"]]
- 00b5c3d8 ["CALL", null, ["callee:00be0a70:8"]]
+ 00b5c4a0 ["INT_ADD", "register:40f0:8", ["const:b5c4a0:8", "const:4:8"]]
+ 00b5c4a0 ["CALL", null, ["callee:00be0a70:8"]]
- 00b5c3d8 bytes 7a110294
+ 00b5c4a0 bytes 74110294
~~~


<a id="compare-debca8fcd107ee264a8a0e95defb8381"></a>

### [`00b5c8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8a4.md) → [`00b5c96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md) _ZNK8firebase4auth4UserneERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bddba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8a4.md#insn-00b5c8b4) · [`00b5c8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8a4.md#insn-00b5c8c0)
- 新版 [`00b5c97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md#insn-00b5c97c) · [`00b5c988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c96c.md#insn-00b5c988)

~~~diff
- 00b5c8b4 ["INT_ADD", "register:40f0:8", ["const:b5c8b4:8", "const:4:8"]]
- 00b5c8b4 ["CALL", null, ["callee:00bddba0:8"]]
+ 00b5c97c ["INT_ADD", "register:40f0:8", ["const:b5c97c:8", "const:4:8"]]
+ 00b5c97c ["CALL", null, ["callee:00bddba0:8"]]
- 00b5c8b4 bytes 8f040294
+ 00b5c97c bytes 89040294
- 00b5c8c0 ["INT_ADD", "register:40f0:8", ["const:b5c8c0:8", "const:4:8"]]
- 00b5c8c0 ["CALL", null, ["callee:00bddba0:8"]]
+ 00b5c988 ["INT_ADD", "register:40f0:8", ["const:b5c988:8", "const:4:8"]]
+ 00b5c988 ["CALL", null, ["callee:00bddba0:8"]]
- 00b5c8c0 bytes 8c040294
+ 00b5c988 bytes 86040294
~~~


<a id="compare-d87301e07abeda9a69bdfbefed972824"></a>

### [`00b5e110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e110.md) → [`00b5e1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e1d8.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0910.md) [`00be0b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be09c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09c0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e110.md#insn-00b5e124)
- 新版 [`00b5e1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e1d8.md#insn-00b5e1ec)

~~~diff
- 00b5e124 ["INT_ADD", "register:40f0:8", ["const:b5e124:8", "const:4:8"]]
- 00b5e124 ["CALL", null, ["callee:00be0be0:8"]]
+ 00b5e1ec ["INT_ADD", "register:40f0:8", ["const:b5e1ec:8", "const:4:8"]]
+ 00b5e1ec ["CALL", null, ["callee:00be0be0:8"]]
- 00b5e124 bytes 830a0294
+ 00b5e1ec bytes 7d0a0294
~~~


<a id="compare-721d9e3b91a9d2a4091bca9f8686b876"></a>

### [`00b5e138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e138.md) → [`00b5e200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00be08f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08f0.md) [`00be0b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be09a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09a0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e138.md#insn-00b5e150) · [`00b5e15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e138.md#insn-00b5e15c) · [`00b5e164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e138.md#insn-00b5e164)
- 新版 [`00b5e218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e218) · [`00b5e224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e224) · [`00b5e22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e200.md#insn-00b5e22c)

~~~diff
- 00b5e150 ["INT_ADD", "register:40f0:8", ["const:b5e150:8", "const:4:8"]]
- 00b5e150 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5e218 ["INT_ADD", "register:40f0:8", ["const:b5e218:8", "const:4:8"]]
+ 00b5e218 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5e150 bytes 74fe0194
+ 00b5e218 bytes 6efe0194
- 00b5e15c ["INT_ADD", "register:40f0:8", ["const:b5e15c:8", "const:4:8"]]
- 00b5e15c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b5e224 ["INT_ADD", "register:40f0:8", ["const:b5e224:8", "const:4:8"]]
+ 00b5e224 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b5e15c bytes 75fe0194
+ 00b5e224 bytes 6ffe0194
- 00b5e164 ["INT_ADD", "register:40f0:8", ["const:b5e164:8", "const:4:8"]]
- 00b5e164 ["CALL", null, ["callee:00be0be0:8"]]
+ 00b5e22c ["INT_ADD", "register:40f0:8", ["const:b5e22c:8", "const:4:8"]]
+ 00b5e22c ["CALL", null, ["callee:00be0be0:8"]]
- 00b5e164 bytes 730a0294
+ 00b5e22c bytes 6d0a0294
~~~


<a id="compare-957957edee0eec8756c8794a8b8a1501"></a>

### [`00b5fe6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fe6c.md) → [`00b5ff34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b5e17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5febc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fe6c.md#insn-00b5febc) · [`00b5fed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fe6c.md#insn-00b5fed8)
- 新版 [`00b5ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md#insn-00b5ff84) · [`00b5ffa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md#insn-00b5ffa0)

~~~diff
- 00b5febc ["INT_ADD", "register:40f0:8", ["const:b5febc:8", "const:4:8"]]
- 00b5febc ["CALL", null, ["callee:00bdb010:8"]]
+ 00b5ff84 ["INT_ADD", "register:40f0:8", ["const:b5ff84:8", "const:4:8"]]
+ 00b5ff84 ["CALL", null, ["callee:00bdb010:8"]]
- 00b5febc bytes 29ec0194
+ 00b5ff84 bytes 23ec0194
- 00b5fed8 ["INT_ADD", "register:40f0:8", ["const:b5fed8:8", "const:4:8"]]
- 00b5fed8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b5ffa0 ["INT_ADD", "register:40f0:8", ["const:b5ffa0:8", "const:4:8"]]
+ 00b5ffa0 ["CALL", null, ["callee:00bdb010:8"]]
- 00b5fed8 bytes 22ec0194
+ 00b5ffa0 bytes 1cec0194
~~~


<a id="compare-e5cee56a26731f2aae77633280607c85"></a>

### [`00b5fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fff8.md) → [`00b600c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md) _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b5e17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0aa0.md)
- 新版 呼出元 1件 [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fff8.md#insn-00b60030) · [`00b60048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fff8.md#insn-00b60048) · [`00b60070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fff8.md#insn-00b60070)
- 新版 [`00b600f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b600f8) · [`00b60110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b60110) · [`00b60138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md#insn-00b60138)

~~~diff
- 00b60030 ["INT_ADD", "register:40f0:8", ["const:b60030:8", "const:4:8"]]
- 00b60030 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b600f8 ["INT_ADD", "register:40f0:8", ["const:b600f8:8", "const:4:8"]]
+ 00b600f8 ["CALL", null, ["callee:00be0cd0:8"]]
- 00b60030 bytes fc020294
+ 00b600f8 bytes f6020294
- 00b60048 ["INT_ADD", "register:40f0:8", ["const:b60048:8", "const:4:8"]]
- 00b60048 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b60110 ["INT_ADD", "register:40f0:8", ["const:b60110:8", "const:4:8"]]
+ 00b60110 ["CALL", null, ["callee:00bddf30:8"]]
- 00b60048 bytes 8ef70194
+ 00b60110 bytes 88f70194
- 00b60070 ["INT_ADD", "register:40f0:8", ["const:b60070:8", "const:4:8"]]
- 00b60070 ["CALL", null, ["callee:00be0b50:8"]]
+ 00b60138 ["INT_ADD", "register:40f0:8", ["const:b60138:8", "const:4:8"]]
+ 00b60138 ["CALL", null, ["callee:00be0b50:8"]]
- 00b60070 bytes 8c020294
+ 00b60138 bytes 86020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ed64b28ac488cd2b7e410cbcfcd1f4"></a>

### [`00b60204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60204.md) → [`00b602cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c40.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cf0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60204.md#insn-00b60224) · [`00b60238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60204.md#insn-00b60238) · [`00b6024c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60204.md#insn-00b6024c)
- 新版 [`00b602ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b602ec) · [`00b60300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b60300) · [`00b60314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b602cc.md#insn-00b60314)

~~~diff
- 00b60224 ["INT_ADD", "register:40f0:8", ["const:b60224:8", "const:4:8"]]
- 00b60224 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b602ec ["INT_ADD", "register:40f0:8", ["const:b602ec:8", "const:4:8"]]
+ 00b602ec ["CALL", null, ["callee:00bdddc0:8"]]
- 00b60224 bytes bbf60194
+ 00b602ec bytes b5f60194
- 00b60238 ["INT_ADD", "register:40f0:8", ["const:b60238:8", "const:4:8"]]
- 00b60238 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b60300 ["INT_ADD", "register:40f0:8", ["const:b60300:8", "const:4:8"]]
+ 00b60300 ["CALL", null, ["callee:00bddf30:8"]]
- 00b60238 bytes 12f70194
+ 00b60300 bytes 0cf70194
- 00b6024c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6024c ["INT_ADD", "register:40f0:8", ["const:b6024c:8", "const:4:8"]]
- 00b6024c ["CALLIND", null, ["register:0:8"]]
+ 00b60314 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60314 ["INT_ADD", "register:40f0:8", ["const:b60314:8", "const:4:8"]]
+ 00b60314 ["CALLIND", null, ["register:0:8"]]
- 00b6024c bytes 00013fd6
+ 00b60314 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14b75eee0561779a5aa0cee708dda286"></a>

### [`00b602a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b602a4.md) → [`00b6036c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b5e858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e858.md) [`00b6c138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c138.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaa0.md) [`00bddae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddae0.md) [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md)
- 新版 呼出元 2件 [`00b5e920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e920.md) [`00b6c200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c200.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b602bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b602a4.md#insn-00b602bc) · [`00b602c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b602a4.md#insn-00b602c4) · [`00b602cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b602a4.md#insn-00b602cc)
- 新版 [`00b60384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b60384) · [`00b6038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b6038c) · [`00b60394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md#insn-00b60394)

~~~diff
- 00b602bc ["INT_ADD", "register:40f0:8", ["const:b602bc:8", "const:4:8"]]
- 00b602bc ["CALL", null, ["callee:00bddb90:8"]]
+ 00b60384 ["INT_ADD", "register:40f0:8", ["const:b60384:8", "const:4:8"]]
+ 00b60384 ["CALL", null, ["callee:00bddb90:8"]]
- 00b602bc bytes 09f60194
+ 00b60384 bytes 03f60194
- 00b602c4 ["INT_ADD", "register:40f0:8", ["const:b602c4:8", "const:4:8"]]
- 00b602c4 ["CALL", null, ["callee:00bddb50:8"]]
+ 00b6038c ["INT_ADD", "register:40f0:8", ["const:b6038c:8", "const:4:8"]]
+ 00b6038c ["CALL", null, ["callee:00bddb50:8"]]
- 00b602c4 bytes f7f50194
+ 00b6038c bytes f1f50194
- 00b602cc ["INT_ADD", "register:40f0:8", ["const:b602cc:8", "const:4:8"]]
- 00b602cc ["CALL", null, ["callee:00bddb50:8"]]
+ 00b60394 ["INT_ADD", "register:40f0:8", ["const:b60394:8", "const:4:8"]]
+ 00b60394 ["CALL", null, ["callee:00bddb50:8"]]
- 00b602cc bytes f5f50194
+ 00b60394 bytes eff50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4e7fc5d9c02491924b321b3a91693b"></a>

### [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) → [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b5e694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md) [`00b5ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md) [`00b5f0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md) [`00b5f258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md) [`00b5f4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a90.md)
- 新版 呼出元 8件 [`00b5e75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e75c.md) [`00b5ef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ef24.md) [`00b5f194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f194.md) [`00b5f320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f320.md) [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md#insn-00b60348) · [`00b60360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md#insn-00b60360) · [`00b60388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md#insn-00b60388)
- 新版 [`00b60410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60410) · [`00b60428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60428) · [`00b60450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md#insn-00b60450)

~~~diff
- 00b60348 ["INT_ADD", "register:40f0:8", ["const:b60348:8", "const:4:8"]]
- 00b60348 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b60410 ["INT_ADD", "register:40f0:8", ["const:b60410:8", "const:4:8"]]
+ 00b60410 ["CALL", null, ["callee:00be0cd0:8"]]
- 00b60348 bytes 36020294
+ 00b60410 bytes 30020294
- 00b60360 ["INT_ADD", "register:40f0:8", ["const:b60360:8", "const:4:8"]]
- 00b60360 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b60428 ["INT_ADD", "register:40f0:8", ["const:b60428:8", "const:4:8"]]
+ 00b60428 ["CALL", null, ["callee:00bddf30:8"]]
- 00b60360 bytes c8f60194
+ 00b60428 bytes c2f60194
- 00b60388 ["INT_ADD", "register:40f0:8", ["const:b60388:8", "const:4:8"]]
- 00b60388 ["CALL", null, ["callee:00be0b40:8"]]
+ 00b60450 ["INT_ADD", "register:40f0:8", ["const:b60450:8", "const:4:8"]]
+ 00b60450 ["CALL", null, ["callee:00be0b40:8"]]
- 00b60388 bytes c2010294
+ 00b60450 bytes bc010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f2e0574825c57bdf2c8b8b76148660"></a>

### [`00b606d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md) → [`00b607a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md) _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b5eaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md) [`00b707d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ab0.md)
- 新版 呼出元 2件 [`00b5eb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5eb70.md) [`00b70898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md#insn-00b60710) · [`00b60728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md#insn-00b60728) · [`00b60750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md#insn-00b60750)
- 新版 [`00b607d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b607d8) · [`00b607f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b607f0) · [`00b60818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md#insn-00b60818)

~~~diff
- 00b60710 ["INT_ADD", "register:40f0:8", ["const:b60710:8", "const:4:8"]]
- 00b60710 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b607d8 ["INT_ADD", "register:40f0:8", ["const:b607d8:8", "const:4:8"]]
+ 00b607d8 ["CALL", null, ["callee:00be0cd0:8"]]
- 00b60710 bytes 44010294
+ 00b607d8 bytes 3e010294
- 00b60728 ["INT_ADD", "register:40f0:8", ["const:b60728:8", "const:4:8"]]
- 00b60728 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b607f0 ["INT_ADD", "register:40f0:8", ["const:b607f0:8", "const:4:8"]]
+ 00b607f0 ["CALL", null, ["callee:00bddf30:8"]]
- 00b60728 bytes d6f50194
+ 00b607f0 bytes d0f50194
- 00b60750 ["INT_ADD", "register:40f0:8", ["const:b60750:8", "const:4:8"]]
- 00b60750 ["CALL", null, ["callee:00be0b60:8"]]
+ 00b60818 ["INT_ADD", "register:40f0:8", ["const:b60818:8", "const:4:8"]]
+ 00b60818 ["CALL", null, ["callee:00be0b60:8"]]
- 00b60750 bytes d8000294
+ 00b60818 bytes d2000294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733f02b731ee309d4e91364e60f46ef4"></a>

### [`00b64d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d7c.md) → [`00b64e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md) _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c30.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d7c.md#insn-00b64dac) · [`00b64dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d7c.md#insn-00b64dc8) · [`00b64de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d7c.md#insn-00b64de0)
- 新版 [`00b64e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64e74) · [`00b64e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64e90) · [`00b64ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e44.md#insn-00b64ea8)

~~~diff
- 00b64dac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64dac ["INT_ADD", "register:40f0:8", ["const:b64dac:8", "const:4:8"]]
- 00b64dac ["CALLIND", null, ["register:0:8"]]
+ 00b64e74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64e74 ["INT_ADD", "register:40f0:8", ["const:b64e74:8", "const:4:8"]]
+ 00b64e74 ["CALLIND", null, ["register:0:8"]]
- 00b64dac bytes 00013fd6
+ 00b64e74 bytes 00013fd6
- 00b64dc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64dc8 ["INT_ADD", "register:40f0:8", ["const:b64dc8:8", "const:4:8"]]
- 00b64dc8 ["CALLIND", null, ["register:0:8"]]
+ 00b64e90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64e90 ["INT_ADD", "register:40f0:8", ["const:b64e90:8", "const:4:8"]]
+ 00b64e90 ["CALLIND", null, ["register:0:8"]]
- 00b64dc8 bytes 00013fd6
+ 00b64e90 bytes 00013fd6
- 00b64de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64de0 ["INT_ADD", "register:40f0:8", ["const:b64de0:8", "const:4:8"]]
- 00b64de0 ["CALLIND", null, ["register:0:8"]]
+ 00b64ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b64ea8 ["INT_ADD", "register:40f0:8", ["const:b64ea8:8", "const:4:8"]]
+ 00b64ea8 ["CALLIND", null, ["register:0:8"]]
- 00b64de0 bytes 00013fd6
+ 00b64ea8 bytes 00013fd6
~~~


<a id="compare-c63b5a9f696732f2c3612eafe7fe2889"></a>

### [`00b69ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69ce0.md) → [`00b69da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md) _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d30.md) · 呼出先 2件 [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md)
- 新版 呼出元 1件 [`00be0de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0de0.md) · 呼出先 2件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b69cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69ce0.md#insn-00b69cf4) · [`00b69d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69ce0.md#insn-00b69d20)
- 新版 [`00b69dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md#insn-00b69dbc) · [`00b69de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69da8.md#insn-00b69de8)

~~~diff
- 00b69cf4 ["INT_ADD", "register:40f0:8", ["const:b69cf4:8", "const:4:8"]]
- 00b69cf4 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b69dbc ["INT_ADD", "register:40f0:8", ["const:b69dbc:8", "const:4:8"]]
+ 00b69dbc ["CALL", null, ["callee:00be0d10:8"]]
- 00b69cf4 bytes dbdb0194
+ 00b69dbc bytes d5db0194
- 00b69d20 ["INT_ADD", "register:40f0:8", ["const:b69d20:8", "const:4:8"]]
- 00b69d20 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b69de8 ["INT_ADD", "register:40f0:8", ["const:b69de8:8", "const:4:8"]]
+ 00b69de8 ["CALL", null, ["callee:00bde1e0:8"]]
- 00b69d20 bytes 04d10194
+ 00b69de8 bytes fed00194
~~~


<a id="compare-5c6964ec6eb4a440b37541b8b072864a"></a>

### [`00b6ac44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac44.md) → [`00b6ad0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad0c.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ac58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac44.md#insn-00b6ac58)
- 新版 [`00b6ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad0c.md#insn-00b6ad20)

~~~diff
- 00b6ac58 ["INT_ADD", "register:40f0:8", ["const:b6ac58:8", "const:4:8"]]
- 00b6ac58 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b6ad20 ["INT_ADD", "register:40f0:8", ["const:b6ad20:8", "const:4:8"]]
+ 00b6ad20 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b6ac58 bytes bac00194
+ 00b6ad20 bytes b4c00194
~~~


<a id="compare-d95d75d48e6f7d043a5845033984916e"></a>

### [`00b6acdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6acdc.md) → [`00b6ada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ada4.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00be0d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6acf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6acdc.md#insn-00b6acf4)
- 新版 [`00b6adbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ada4.md#insn-00b6adbc)

~~~diff
- 00b6acf4 ["INT_ADD", "register:40f0:8", ["const:b6acf4:8", "const:4:8"]]
- 00b6acf4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b6adbc ["INT_ADD", "register:40f0:8", ["const:b6adbc:8", "const:4:8"]]
+ 00b6adbc ["CALL", null, ["callee:00bdaff0:8"]]
- 00b6acf4 bytes 93c00194
+ 00b6adbc bytes 8dc00194
~~~


<a id="compare-f18a21765d7ec5bf23f97150c2894fe6"></a>

### [`00b6adb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6adb8.md) → [`00b6ae80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ae80.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6add4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6adb8.md#insn-00b6add4)
- 新版 [`00b6ae9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ae80.md#insn-00b6ae9c)

~~~diff
- 00b6add4 ["INT_ADD", "register:40f0:8", ["const:b6add4:8", "const:4:8"]]
- 00b6add4 ["CALL", null, ["callee:00be0df0:8"]]
+ 00b6ae9c ["INT_ADD", "register:40f0:8", ["const:b6ae9c:8", "const:4:8"]]
+ 00b6ae9c ["CALL", null, ["callee:00be0df0:8"]]
- 00b6add4 bytes dbd70194
+ 00b6ae9c bytes d5d70194
~~~


<a id="compare-8bd8aa4818a3ffde7c60f8d042f390f5"></a>

### [`00b6c9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c9f4.md) → [`00b6cabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b6a9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a9dc.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d00.md)
- 新版 呼出元 1件 [`00b6aaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0db0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c9f4.md#insn-00b6ca08)
- 新版 [`00b6cad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md#insn-00b6cad0)

~~~diff
- 00b6ca08 ["INT_ADD", "register:40f0:8", ["const:b6ca08:8", "const:4:8"]]
- 00b6ca08 ["CALL", null, ["callee:00be0db0:8"]]
+ 00b6cad0 ["INT_ADD", "register:40f0:8", ["const:b6cad0:8", "const:4:8"]]
+ 00b6cad0 ["CALL", null, ["callee:00be0db0:8"]]
- 00b6ca08 bytes bed00194
+ 00b6cad0 bytes b8d00194
~~~


<a id="compare-52fe232b7c49bfda7b7558668e16ed2a"></a>

### [`00b6cb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cb28.md) → [`00b6cbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md) _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d50.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cb28.md#insn-00b6cb48) · [`00b6cb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cb28.md#insn-00b6cb5c) · [`00b6cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cb28.md#insn-00b6cb70)
- 新版 [`00b6cc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc10) · [`00b6cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc24) · [`00b6cc38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cbf0.md#insn-00b6cc38)

~~~diff
- 00b6cb48 ["INT_ADD", "register:40f0:8", ["const:b6cb48:8", "const:4:8"]]
- 00b6cb48 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b6cc10 ["INT_ADD", "register:40f0:8", ["const:b6cc10:8", "const:4:8"]]
+ 00b6cc10 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b6cb48 bytes 72c40194
+ 00b6cc10 bytes 6cc40194
- 00b6cb5c ["INT_ADD", "register:40f0:8", ["const:b6cb5c:8", "const:4:8"]]
- 00b6cb5c ["CALL", null, ["callee:00bddf30:8"]]
+ 00b6cc24 ["INT_ADD", "register:40f0:8", ["const:b6cc24:8", "const:4:8"]]
+ 00b6cc24 ["CALL", null, ["callee:00bddf30:8"]]
- 00b6cb5c bytes c9c40194
+ 00b6cc24 bytes c3c40194
- 00b6cb70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6cb70 ["INT_ADD", "register:40f0:8", ["const:b6cb70:8", "const:4:8"]]
- 00b6cb70 ["CALLIND", null, ["register:0:8"]]
+ 00b6cc38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6cc38 ["INT_ADD", "register:40f0:8", ["const:b6cc38:8", "const:4:8"]]
+ 00b6cc38 ["CALLIND", null, ["register:0:8"]]
- 00b6cb70 bytes 00013fd6
+ 00b6cc38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa7e9847546fe02ad82567ba9b35367"></a>

### [`00b6cbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cbc8.md) → [`00b6cc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0cf0.md) · 呼出先 3件 [`00bddad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddad0.md) [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md) [`00be0d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d20.md)
- 新版 呼出元 1件 [`00be0da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0da0.md) · 呼出先 3件 [`00bddb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb80.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) [`00be0dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cbc8.md#insn-00b6cbe0) · [`00b6cc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cbc8.md#insn-00b6cc04) · [`00b6cc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cbc8.md#insn-00b6cc10)
- 新版 [`00b6cca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6cca8) · [`00b6cccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6cccc) · [`00b6ccd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cc90.md#insn-00b6ccd8)

~~~diff
- 00b6cbe0 ["INT_ADD", "register:40f0:8", ["const:b6cbe0:8", "const:4:8"]]
- 00b6cbe0 ["CALL", null, ["callee:00be0dd0:8"]]
+ 00b6cca8 ["INT_ADD", "register:40f0:8", ["const:b6cca8:8", "const:4:8"]]
+ 00b6cca8 ["CALL", null, ["callee:00be0dd0:8"]]
- 00b6cbe0 bytes 50d00194
+ 00b6cca8 bytes 4ad00194
- 00b6cc04 ["INT_ADD", "register:40f0:8", ["const:b6cc04:8", "const:4:8"]]
- 00b6cc04 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b6cccc ["INT_ADD", "register:40f0:8", ["const:b6cccc:8", "const:4:8"]]
+ 00b6cccc ["CALL", null, ["callee:00be0d10:8"]]
- 00b6cc04 bytes 17d00194
+ 00b6cccc bytes 11d00194
- 00b6cc10 ["INT_ADD", "register:40f0:8", ["const:b6cc10:8", "const:4:8"]]
- 00b6cc10 ["CALL", null, ["callee:00bddb80:8"]]
+ 00b6ccd8 ["INT_ADD", "register:40f0:8", ["const:b6ccd8:8", "const:4:8"]]
+ 00b6ccd8 ["CALL", null, ["callee:00bddb80:8"]]
- 00b6cc10 bytes b0c30194
+ 00b6ccd8 bytes aac30194
~~~


<a id="compare-b5029a68fde9be882a668d8000ddf75d"></a>

### [`00b6cc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cc98.md) → [`00b6cd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d20.md) · 呼出先 3件 [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md) [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md) [`00be0d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d70.md)
- 新版 呼出元 1件 [`00be0dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0dd0.md) · 呼出先 3件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) [`00be0e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ccb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cc98.md#insn-00b6ccb8) · [`00b6ccc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cc98.md#insn-00b6ccc8) · [`00b6cd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cc98.md#insn-00b6cd10)
- 新版 [`00b6cd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cd80) · [`00b6cd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cd90) · [`00b6cdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cd60.md#insn-00b6cdd8)

~~~diff
- 00b6ccb8 ["INT_ADD", "register:40f0:8", ["const:b6ccb8:8", "const:4:8"]]
- 00b6ccb8 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b6cd80 ["INT_ADD", "register:40f0:8", ["const:b6cd80:8", "const:4:8"]]
+ 00b6cd80 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b6ccb8 bytes 5ec60194
+ 00b6cd80 bytes 58c60194
- 00b6ccc8 ["INT_ADD", "register:40f0:8", ["const:b6ccc8:8", "const:4:8"]]
- 00b6ccc8 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b6cd90 ["INT_ADD", "register:40f0:8", ["const:b6cd90:8", "const:4:8"]]
+ 00b6cd90 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b6ccc8 bytes 5ac60194
+ 00b6cd90 bytes 54c60194
- 00b6cd10 ["INT_ADD", "register:40f0:8", ["const:b6cd10:8", "const:4:8"]]
- 00b6cd10 ["CALL", null, ["callee:00be0e20:8"]]
+ 00b6cdd8 ["INT_ADD", "register:40f0:8", ["const:b6cdd8:8", "const:4:8"]]
+ 00b6cdd8 ["CALL", null, ["callee:00be0e20:8"]]
- 00b6cd10 bytes 18d00194
+ 00b6cdd8 bytes 12d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d96e076b5749737ce91977d5e09385a"></a>

### [`00b6d38c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d38c.md) → [`00b6d454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d454.md) _ZN8firebase4auth19PhoneAuthCredentialC1ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0de0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6d3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d38c.md#insn-00b6d3b0)
- 新版 [`00b6d478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d454.md#insn-00b6d478)

~~~diff
- 00b6d3b0 ["INT_ADD", "register:40f0:8", ["const:b6d3b0:8", "const:4:8"]]
- 00b6d3b0 ["CALL", null, ["callee:00be0de0:8"]]
+ 00b6d478 ["INT_ADD", "register:40f0:8", ["const:b6d478:8", "const:4:8"]]
+ 00b6d478 ["CALL", null, ["callee:00be0de0:8"]]
- 00b6d3b0 bytes 60ce0194
+ 00b6d478 bytes 5ace0194
~~~


<a id="compare-ff5304c2a31f13da851163435c27b0ff"></a>

### [`00b71ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71ea4.md) → [`00b71f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71ea4.md#insn-00b71ec4) · [`00b71ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71ea4.md#insn-00b71ed0) · [`00b71edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71ea4.md#insn-00b71edc)
- 新版 [`00b71f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71f8c) · [`00b71f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71f98) · [`00b71fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71f6c.md#insn-00b71fa4)

~~~diff
- 00b71ec4 ["INT_ADD", "register:40f0:8", ["const:b71ec4:8", "const:4:8"]]
- 00b71ec4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b71f8c ["INT_ADD", "register:40f0:8", ["const:b71f8c:8", "const:4:8"]]
+ 00b71f8c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b71ec4 bytes 17af0194
+ 00b71f8c bytes 11af0194
- 00b71ed0 ["INT_ADD", "register:40f0:8", ["const:b71ed0:8", "const:4:8"]]
- 00b71ed0 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b71f98 ["INT_ADD", "register:40f0:8", ["const:b71f98:8", "const:4:8"]]
+ 00b71f98 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b71ed0 bytes 18af0194
+ 00b71f98 bytes 12af0194
- 00b71edc ["INT_ADD", "register:40f0:8", ["const:b71edc:8", "const:4:8"]]
- 00b71edc ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b71fa4 ["INT_ADD", "register:40f0:8", ["const:b71fa4:8", "const:4:8"]]
+ 00b71fa4 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b71edc bytes 8daf0194
+ 00b71fa4 bytes 87af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdf531041a3ca4aa58120c1dea5613cd"></a>

### [`00b71f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71f34.md) → [`00b71ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b71f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71f34.md#insn-00b71f54) · [`00b71f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71f34.md#insn-00b71f60) · [`00b71f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71f34.md#insn-00b71f6c)
- 新版 [`00b7201c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b7201c) · [`00b72028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b72028) · [`00b72034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71ffc.md#insn-00b72034)

~~~diff
- 00b71f54 ["INT_ADD", "register:40f0:8", ["const:b71f54:8", "const:4:8"]]
- 00b71f54 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7201c ["INT_ADD", "register:40f0:8", ["const:b7201c:8", "const:4:8"]]
+ 00b7201c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b71f54 bytes f3ae0194
+ 00b7201c bytes edae0194
- 00b71f60 ["INT_ADD", "register:40f0:8", ["const:b71f60:8", "const:4:8"]]
- 00b71f60 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b72028 ["INT_ADD", "register:40f0:8", ["const:b72028:8", "const:4:8"]]
+ 00b72028 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b71f60 bytes f4ae0194
+ 00b72028 bytes eeae0194
- 00b71f6c ["INT_ADD", "register:40f0:8", ["const:b71f6c:8", "const:4:8"]]
- 00b71f6c ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b72034 ["INT_ADD", "register:40f0:8", ["const:b72034:8", "const:4:8"]]
+ 00b72034 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b71f6c bytes 69af0194
+ 00b72034 bytes 63af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bec6f721c2b98042d6cbd8b5b2e2043"></a>

### [`00b72054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72054.md) → [`00b7211c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md) _ZNK8firebase4auth4User24ReauthenticateLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72054.md#insn-00b72074) · [`00b72080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72054.md#insn-00b72080) · [`00b7208c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72054.md#insn-00b7208c)
- 新版 [`00b7213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b7213c) · [`00b72148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b72148) · [`00b72154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7211c.md#insn-00b72154)

~~~diff
- 00b72074 ["INT_ADD", "register:40f0:8", ["const:b72074:8", "const:4:8"]]
- 00b72074 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7213c ["INT_ADD", "register:40f0:8", ["const:b7213c:8", "const:4:8"]]
+ 00b7213c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b72074 bytes abae0194
+ 00b7213c bytes a5ae0194
- 00b72080 ["INT_ADD", "register:40f0:8", ["const:b72080:8", "const:4:8"]]
- 00b72080 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b72148 ["INT_ADD", "register:40f0:8", ["const:b72148:8", "const:4:8"]]
+ 00b72148 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b72080 bytes acae0194
+ 00b72148 bytes a6ae0194
- 00b7208c ["INT_ADD", "register:40f0:8", ["const:b7208c:8", "const:4:8"]]
- 00b7208c ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b72154 ["INT_ADD", "register:40f0:8", ["const:b72154:8", "const:4:8"]]
+ 00b72154 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b7208c bytes 21af0194
+ 00b72154 bytes 1baf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c87af2246b1f113863d3c1f69d97b69"></a>

### [`00b72204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72204.md) → [`00b722cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md) _ZNK8firebase4auth4User50SendEmailVerificationBeforeUpdatingEmailLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b722fc",
      "incomplete_value": true,
      "site": "00b72304",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72300",
      "incomplete_value": false,
      "site": "00b72304",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b72250",
      "incomplete_value": true,
      "site": "00b72258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7223c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72204.md#insn-00b7223c) · [`00b72258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72204.md#insn-00b72258) · [`00b72224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72204.md#insn-00b72224)
- 新版 [`00b72304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b72304) · [`00b72320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b72320) · [`00b722ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b722cc.md#insn-00b722ec)

~~~diff
- 00b7223c ["INT_ADD", "register:40f0:8", ["const:b7223c:8", "const:4:8"]]
- 00b7223c ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b72304 ["INT_ADD", "register:40f0:8", ["const:b72304:8", "const:4:8"]]
+ 00b72304 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b7223c bytes b5ae0194
+ 00b72304 bytes afae0194
- 00b72258 ["INT_ADD", "register:40f0:8", ["const:b72258:8", "const:4:8"]]
- 00b72258 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b72320 ["INT_ADD", "register:40f0:8", ["const:b72320:8", "const:4:8"]]
+ 00b72320 ["CALL", null, ["callee:00bddea0:8"]]
- 00b72258 bytes e6ae0194
+ 00b72320 bytes e0ae0194
- 00b72224 ["INT_ADD", "register:40f0:8", ["const:b72224:8", "const:4:8"]]
- 00b72224 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b722ec ["INT_ADD", "register:40f0:8", ["const:b722ec:8", "const:4:8"]]
+ 00b722ec ["CALL", null, ["callee:00bddbd0:8"]]
- 00b72224 bytes 3fae0194
+ 00b722ec bytes 39ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-566115bf1862faa80c9daacf8c55cc54"></a>

### [`00b72294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72294.md) → [`00b7235c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md) _ZNK8firebase4auth4User16UnlinkLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b722bc",
      "incomplete_value": true,
      "site": "00b722c0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b722c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72294.md#insn-00b722c0) · [`00b722b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72294.md#insn-00b722b4) · [`00b722cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72294.md#insn-00b722cc)
- 新版 [`00b72388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b72388) · [`00b7237c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b7237c) · [`00b72394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7235c.md#insn-00b72394)

~~~diff
- 00b722c0 ["INT_ADD", "register:40f0:8", ["const:b722c0:8", "const:4:8"]]
- 00b722c0 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b72388 ["INT_ADD", "register:40f0:8", ["const:b72388:8", "const:4:8"]]
+ 00b72388 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b722c0 bytes 1cae0194
+ 00b72388 bytes 16ae0194
- 00b722b4 ["INT_ADD", "register:40f0:8", ["const:b722b4:8", "const:4:8"]]
- 00b722b4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7237c ["INT_ADD", "register:40f0:8", ["const:b7237c:8", "const:4:8"]]
+ 00b7237c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b722b4 bytes 1bae0194
+ 00b7237c bytes 15ae0194
- 00b722cc ["INT_ADD", "register:40f0:8", ["const:b722cc:8", "const:4:8"]]
- 00b722cc ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b72394 ["INT_ADD", "register:40f0:8", ["const:b72394:8", "const:4:8"]]
+ 00b72394 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b722cc bytes 91ae0194
+ 00b72394 bytes 8bae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233120cfbd5281ebb1c13c922035bb57"></a>

### [`00b727ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b727ac.md) → [`00b72874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72874.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b727bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b727ac.md#insn-00b727bc)
- 新版 [`00b72884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72874.md#insn-00b72884)

~~~diff
- 00b727bc ["INT_ADD", "register:40f0:8", ["const:b727bc:8", "const:4:8"]]
- 00b727bc ["CALL", null, ["callee:00be0b30:8"]]
+ 00b72884 ["INT_ADD", "register:40f0:8", ["const:b72884:8", "const:4:8"]]
+ 00b72884 ["CALL", null, ["callee:00be0b30:8"]]
- 00b727bc bytes b1b80194
+ 00b72884 bytes abb80194
~~~


<a id="compare-b838af09a3d96a2dd91244c2c2bcd15d"></a>

### [`00b72974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72974.md) → [`00b72a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e30.md) · 呼出先 2件 [`00be0e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e10.md) [`00be0e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e20.md)
- 新版 呼出元 1件 [`00be0ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ee0.md) · 呼出先 2件 [`00be0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ec0.md) [`00be0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7299c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72974.md#insn-00b7299c) · [`00b729a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72974.md#insn-00b729a4)
- 新版 [`00b72a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md#insn-00b72a64) · [`00b72a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md#insn-00b72a6c)

~~~diff
- 00b7299c ["INT_ADD", "register:40f0:8", ["const:b7299c:8", "const:4:8"]]
- 00b7299c ["CALL", null, ["callee:00be0ed0:8"]]
+ 00b72a64 ["INT_ADD", "register:40f0:8", ["const:b72a64:8", "const:4:8"]]
+ 00b72a64 ["CALL", null, ["callee:00be0ed0:8"]]
- 00b7299c bytes 21b90194
+ 00b72a64 bytes 1bb90194
- 00b729a4 ["INT_ADD", "register:40f0:8", ["const:b729a4:8", "const:4:8"]]
- 00b729a4 ["CALL", null, ["callee:00be0ec0:8"]]
+ 00b72a6c ["INT_ADD", "register:40f0:8", ["const:b72a6c:8", "const:4:8"]]
+ 00b72a6c ["CALL", null, ["callee:00be0ec0:8"]]
- 00b729a4 bytes 1bb90194
+ 00b72a6c bytes 15b90194
~~~


<a id="compare-6e1c779f34ced505d1d0e63db8397c08"></a>

### [`00b72ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72ad4.md) → [`00b72b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb570.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00be0e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e60.md)
- 新版 呼出元 1件 [`00bdb620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb620.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be0f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72ad4.md#insn-00b72ae4) · [`00b72ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72ad4.md#insn-00b72ae8)
- 新版 [`00b72bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md#insn-00b72bac) · [`00b72bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md#insn-00b72bb0)

~~~diff
- 00b72ae4 ["INT_ADD", "register:40f0:8", ["const:b72ae4:8", "const:4:8"]]
- 00b72ae4 ["CALL", null, ["callee:00be0f10:8"]]
+ 00b72bac ["INT_ADD", "register:40f0:8", ["const:b72bac:8", "const:4:8"]]
+ 00b72bac ["CALL", null, ["callee:00be0f10:8"]]
- 00b72ae4 bytes dfb80194
+ 00b72bac bytes d9b80194
- 00b72ae8 ["INT_ADD", "register:40f0:8", ["const:b72ae8:8", "const:4:8"]]
- 00b72ae8 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b72bb0 ["INT_ADD", "register:40f0:8", ["const:b72bb0:8", "const:4:8"]]
+ 00b72bb0 ["CALL", null, ["callee:00bdb180:8"]]
- 00b72ae8 bytes 7aa10194
+ 00b72bb0 bytes 74a10194
~~~


<a id="compare-01a101a8e050066b99631ea969b66c6e"></a>

### [`00b732a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732a0.md) → [`00b73368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73368.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd840.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b732b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732a0.md#insn-00b732b4)
- 新版 [`00b7337c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73368.md#insn-00b7337c)

~~~diff
- 00b732b4 ["INT_ADD", "register:40f0:8", ["const:b732b4:8", "const:4:8"]]
- 00b732b4 ["CALL", null, ["callee:00bdd8f0:8"]]
+ 00b7337c ["INT_ADD", "register:40f0:8", ["const:b7337c:8", "const:4:8"]]
+ 00b7337c ["CALL", null, ["callee:00bdd8f0:8"]]
- 00b732b4 bytes 63a90194
+ 00b7337c bytes 5da90194
~~~


<a id="compare-e33611c86cbd01f4f89fc0c1310ac72e"></a>

### [`00b732f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732f4.md) → [`00b733bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733bc.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732f4.md#insn-00b73308)
- 新版 [`00b733d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733bc.md#insn-00b733d0)

~~~diff
- 00b73308 ["INT_ADD", "register:40f0:8", ["const:b73308:8", "const:4:8"]]
- 00b73308 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00b733d0 ["INT_ADD", "register:40f0:8", ["const:b733d0:8", "const:4:8"]]
+ 00b733d0 ["CALL", null, ["callee:00bd6e20:8"]]
- 00b73308 bytes 968e0194
+ 00b733d0 bytes 948e0194
~~~


<a id="compare-47f9432dda6e275822ee83339585b5b8"></a>

### [`00b73318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73318.md) → [`00b733e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md) _ZNSt6__ndk114__shared_count16__release_sharedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73318.md#insn-00b73334) · [`00b7334c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73318.md#insn-00b7334c)
- 新版 [`00b733fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md#insn-00b733fc) · [`00b73414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md#insn-00b73414)

~~~diff
- 00b73334 ["INT_ADD", "register:40f0:8", ["const:b73334:8", "const:4:8"]]
- 00b73334 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b733fc ["INT_ADD", "register:40f0:8", ["const:b733fc:8", "const:4:8"]]
+ 00b733fc ["CALL", null, ["callee:00bd6e50:8"]]
- 00b73334 bytes 978e0194
+ 00b733fc bytes 958e0194
- 00b7334c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7334c ["INT_ADD", "register:40f0:8", ["const:b7334c:8", "const:4:8"]]
- 00b7334c ["CALLIND", null, ["register:0:8"]]
+ 00b73414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b73414 ["INT_ADD", "register:40f0:8", ["const:b73414:8", "const:4:8"]]
+ 00b73414 ["CALLIND", null, ["register:0:8"]]
- 00b7334c bytes 00013fd6
+ 00b73414 bytes 00013fd6
~~~


<a id="compare-04e33e8c014e0aa6ade18f516a878e92"></a>

### [`00b73368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73368.md) → [`00b73430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73430.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7337c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73368.md#insn-00b7337c)
- 新版 [`00b73444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73430.md#insn-00b73444)

~~~diff
- 00b7337c ["INT_ADD", "register:40f0:8", ["const:b7337c:8", "const:4:8"]]
- 00b7337c ["CALL", null, ["callee:00bd6e20:8"]]
+ 00b73444 ["INT_ADD", "register:40f0:8", ["const:b73444:8", "const:4:8"]]
+ 00b73444 ["CALL", null, ["callee:00bd6e20:8"]]
- 00b7337c bytes 798e0194
+ 00b73444 bytes 778e0194
~~~


<a id="compare-7fe48d1e8fe5d68b5dd7a5c439349767"></a>

### [`00b7338c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7338c.md) → [`00b73454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73454.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b733a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7338c.md#insn-00b733a0)
- 新版 [`00b73468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73454.md#insn-00b73468)

~~~diff
- 00b733a0 ["INT_ADD", "register:40f0:8", ["const:b733a0:8", "const:4:8"]]
- 00b733a0 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00b73468 ["INT_ADD", "register:40f0:8", ["const:b73468:8", "const:4:8"]]
+ 00b73468 ["CALL", null, ["callee:00bd6e20:8"]]
- 00b733a0 bytes 708e0194
+ 00b73468 bytes 6e8e0194
~~~


<a id="compare-b73e2d19210191071aec10899df38b1c"></a>

### [`00b733b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b733b0.md) → [`00b73478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b733cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b733b0.md#insn-00b733cc) · [`00b733f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b733b0.md#insn-00b733f4) · [`00b73408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b733b0.md#insn-00b73408)
- 新版 [`00b73494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b73494) · [`00b734bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b734bc) · [`00b734d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b734d0)

~~~diff
- 00b733cc ["INT_ADD", "register:40f0:8", ["const:b733cc:8", "const:4:8"]]
- 00b733cc ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b73494 ["INT_ADD", "register:40f0:8", ["const:b73494:8", "const:4:8"]]
+ 00b73494 ["CALL", null, ["callee:00bd6e50:8"]]
- 00b733cc bytes 718e0194
+ 00b73494 bytes 6f8e0194
- 00b733f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b733f4 ["INT_ADD", "register:40f0:8", ["const:b733f4:8", "const:4:8"]]
- 00b733f4 ["CALLIND", null, ["register:0:8"]]
+ 00b734bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b734bc ["INT_ADD", "register:40f0:8", ["const:b734bc:8", "const:4:8"]]
+ 00b734bc ["CALLIND", null, ["register:0:8"]]
- 00b733f4 bytes 00013fd6
+ 00b734bc bytes 00013fd6
- 00b73408 ["INT_ADD", "register:40f0:8", ["const:b73408:8", "const:4:8"]]
- 00b73408 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b734d0 ["INT_ADD", "register:40f0:8", ["const:b734d0:8", "const:4:8"]]
+ 00b734d0 ["CALL", null, ["callee:00bd6e50:8"]]
- 00b73408 bytes 628e0194
+ 00b734d0 bytes 608e0194
~~~


<a id="compare-69a5e12ad859a4cfd2937dbb4390527e"></a>

### [`00b73484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73484.md) → [`00b7354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5a0.md) · 呼出先 1件 [`00bd6c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6c90.md)
- 新版 呼出元 1件 [`00bdb650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb650.md) · 呼出先 1件 [`00bd6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b734b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73484.md#insn-00b734b4)
- 新版 [`00b7357c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md#insn-00b7357c)

~~~diff
- 00b734b4 ["INT_ADD", "register:40f0:8", ["const:b734b4:8", "const:4:8"]]
- 00b734b4 ["CALL", null, ["callee:00bd6d50:8"]]
+ 00b7357c ["INT_ADD", "register:40f0:8", ["const:b7357c:8", "const:4:8"]]
+ 00b7357c ["CALL", null, ["callee:00bd6d50:8"]]
- 00b734b4 bytes f78d0194
+ 00b7357c bytes f58d0194
~~~


<a id="compare-d4a89dabb3b70d7c6c6745ac3d1999e3"></a>

### [`00b734f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b734f0.md) → [`00b735b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735b8.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b734f0.md#insn-00b73500)
- 新版 [`00b735c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735b8.md#insn-00b735c8)

~~~diff
- 00b73500 ["INT_ADD", "register:40f0:8", ["const:b73500:8", "const:4:8"]]
- 00b73500 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b735c8 ["INT_ADD", "register:40f0:8", ["const:b735c8:8", "const:4:8"]]
+ 00b735c8 ["CALL", null, ["callee:00bde7d0:8"]]
- 00b73500 bytes 88ac0194
+ 00b735c8 bytes 82ac0194
~~~


<a id="compare-9942f79573920303c82339930c10dacc"></a>

### [`00b73514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73514.md) → [`00b735dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735dc.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73514.md#insn-00b73524)
- 新版 [`00b735ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735dc.md#insn-00b735ec)

~~~diff
- 00b73524 ["INT_ADD", "register:40f0:8", ["const:b73524:8", "const:4:8"]]
- 00b73524 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b735ec ["INT_ADD", "register:40f0:8", ["const:b735ec:8", "const:4:8"]]
+ 00b735ec ["CALL", null, ["callee:00bde7e0:8"]]
- 00b73524 bytes 83ac0194
+ 00b735ec bytes 7dac0194
~~~


<a id="compare-9e5446ce83051659d97d4543db030fc4"></a>

### [`00b73538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73538.md) → [`00b73600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73600.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b7364c",
      "incomplete_value": true,
      "site": "00b73650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c247b8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73584",
      "incomplete_value": true,
      "site": "00b73588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24708:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b73578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73538.md#insn-00b73578)
- 新版 [`00b73640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73600.md#insn-00b73640)

~~~diff
- 00b73578 ["COPY", "register:4048:8", ["const:c24708:8"]]
+ 00b73640 ["COPY", "register:4048:8", ["const:c247b8:8"]]
- 00b73578 bytes 898c5810
+ 00b73640 bytes c98b5810
~~~


<a id="compare-af4cfc656697ca62a2e906d6be7127b2"></a>

### [`00b73918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73918.md) → [`00b739e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md) _ZNSt13runtime_erroraSERKS_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73918.md#insn-00b73940) · [`00b7394c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73918.md#insn-00b7394c) · [`00b7395c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73918.md#insn-00b7395c)
- 新版 [`00b73a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a08) · [`00b73a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a14) · [`00b73a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a24)

~~~diff
- 00b73940 ["INT_ADD", "register:40f0:8", ["const:b73940:8", "const:4:8"]]
- 00b73940 ["CALL", null, ["callee:00bd6df0:8"]]
+ 00b73a08 ["INT_ADD", "register:40f0:8", ["const:b73a08:8", "const:4:8"]]
+ 00b73a08 ["CALL", null, ["callee:00bd6df0:8"]]
- 00b73940 bytes fc8c0194
+ 00b73a08 bytes fa8c0194
- 00b7394c ["INT_ADD", "register:40f0:8", ["const:b7394c:8", "const:4:8"]]
- 00b7394c ["CALL", null, ["callee:00bd6df0:8"]]
+ 00b73a14 ["INT_ADD", "register:40f0:8", ["const:b73a14:8", "const:4:8"]]
+ 00b73a14 ["CALL", null, ["callee:00bd6df0:8"]]
- 00b7394c bytes f98c0194
+ 00b73a14 bytes f78c0194
- 00b7395c ["INT_ADD", "register:40f0:8", ["const:b7395c:8", "const:4:8"]]
- 00b7395c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b73a24 ["INT_ADD", "register:40f0:8", ["const:b73a24:8", "const:4:8"]]
+ 00b73a24 ["CALL", null, ["callee:00bdb010:8"]]
- 00b7395c bytes 819d0194
+ 00b73a24 bytes 7b9d0194
~~~


<a id="compare-cfd26af06773d604b8316fd708d9864b"></a>

### [`00b73c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73c54.md) → [`00b73d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73c54.md#insn-00b73cb0) · [`00b73cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73c54.md#insn-00b73cd4) · [`00b73cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73c54.md#insn-00b73cf4)
- 新版 [`00b73d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73d78) · [`00b73d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73d9c) · [`00b73dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73dbc)

~~~diff
- 00b73cb0 ["INT_ADD", "register:40f0:8", ["const:b73cb0:8", "const:4:8"]]
- 00b73cb0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b73d78 ["INT_ADD", "register:40f0:8", ["const:b73d78:8", "const:4:8"]]
+ 00b73d78 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b73cb0 bytes a49c0194
+ 00b73d78 bytes 9e9c0194
- 00b73cd4 ["INT_ADD", "register:40f0:8", ["const:b73cd4:8", "const:4:8"]]
- 00b73cd4 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b73d9c ["INT_ADD", "register:40f0:8", ["const:b73d9c:8", "const:4:8"]]
+ 00b73d9c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b73cd4 bytes c79c0194
+ 00b73d9c bytes c19c0194
- 00b73cf4 ["INT_ADD", "register:40f0:8", ["const:b73cf4:8", "const:4:8"]]
- 00b73cf4 ["CALL", null, ["callee:00418c24:8"]]
+ 00b73dbc ["INT_ADD", "register:40f0:8", ["const:b73dbc:8", "const:4:8"]]
+ 00b73dbc ["CALL", null, ["callee:00418c24:8"]]
- 00b73cf4 bytes cc93e297
+ 00b73dbc bytes 9a93e297
~~~


<a id="compare-d49f703087aeda7f9340eebe1ee9fd2a"></a>

### [`00b73d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73d24.md) → [`00b73dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73dec.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb130.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00bdb1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1e0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73d24.md#insn-00b73d4c)
- 新版 [`00b73e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73dec.md#insn-00b73e14)

~~~diff
- 00b73d4c ["INT_ADD", "register:40f0:8", ["const:b73d4c:8", "const:4:8"]]
- 00b73d4c ["CALL", null, ["callee:00bdb140:8"]]
+ 00b73e14 ["INT_ADD", "register:40f0:8", ["const:b73e14:8", "const:4:8"]]
+ 00b73e14 ["CALL", null, ["callee:00bdb140:8"]]
- 00b73d4c bytes d19c0194
+ 00b73e14 bytes cb9c0194
~~~


<a id="compare-0e363a2de5b5fbef2de2978e5ce1bb92"></a>

### [`00b74290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74290.md) → [`00b74358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74358.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b742d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74290.md#insn-00b742d0)
- 新版 [`00b74398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74358.md#insn-00b74398)

~~~diff
- 00b742d0 ["INT_ADD", "register:40f0:8", ["const:b742d0:8", "const:4:8"]]
- 00b742d0 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74398 ["INT_ADD", "register:40f0:8", ["const:b74398:8", "const:4:8"]]
+ 00b74398 ["CALL", null, ["callee:0041fddc:8"]]
- 00b742d0 bytes c3aee297
+ 00b74398 bytes 91aee297
~~~


<a id="compare-ed6700ed83cc463f7a79fcf24811d830"></a>

### [`00b74350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74350.md) → [`00b74418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00b74088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74088.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b74150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b743e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74350.md#insn-00b743e8) · [`00b74420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74350.md#insn-00b74420) · [`00b74434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74350.md#insn-00b74434)
- 新版 [`00b744b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744b0) · [`00b744e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744e8) · [`00b744fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744fc)

~~~diff
- 00b743e8 ["INT_ADD", "register:40f0:8", ["const:b743e8:8", "const:4:8"]]
- 00b743e8 ["CALL", null, ["callee:00b74150:8"]]
+ 00b744b0 ["INT_ADD", "register:40f0:8", ["const:b744b0:8", "const:4:8"]]
+ 00b744b0 ["CALL", null, ["callee:00b74150:8"]]
- 00b743e8 bytes 28ffff97
+ 00b744b0 bytes 28ffff97
- 00b74420 ["INT_ADD", "register:40f0:8", ["const:b74420:8", "const:4:8"]]
- 00b74420 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b744e8 ["INT_ADD", "register:40f0:8", ["const:b744e8:8", "const:4:8"]]
+ 00b744e8 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b74420 bytes f49a0194
+ 00b744e8 bytes ee9a0194
- 00b74434 ["INT_ADD", "register:40f0:8", ["const:b74434:8", "const:4:8"]]
- 00b74434 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00b744fc ["INT_ADD", "register:40f0:8", ["const:b744fc:8", "const:4:8"]]
+ 00b744fc ["CALL", null, ["callee:00bdb1f0:8"]]
- 00b74434 bytes 439b0194
+ 00b744fc bytes 3d9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27879e62e539561a68df17e2ef77e95"></a>

### [`00b747dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b747dc.md) → [`00b748a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b747dc.md#insn-00b74838) · [`00b74858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b747dc.md#insn-00b74858) · [`00b74878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b747dc.md#insn-00b74878)
- 新版 [`00b74900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74900) · [`00b74920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74920) · [`00b74940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74940)

~~~diff
- 00b74838 ["INT_ADD", "register:40f0:8", ["const:b74838:8", "const:4:8"]]
- 00b74838 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b74900 ["INT_ADD", "register:40f0:8", ["const:b74900:8", "const:4:8"]]
+ 00b74900 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b74838 bytes c2990194
+ 00b74900 bytes bc990194
- 00b74858 ["INT_ADD", "register:40f0:8", ["const:b74858:8", "const:4:8"]]
- 00b74858 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00b74920 ["INT_ADD", "register:40f0:8", ["const:b74920:8", "const:4:8"]]
+ 00b74920 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00b74858 bytes 3a9a0194
+ 00b74920 bytes 349a0194
- 00b74878 ["INT_ADD", "register:40f0:8", ["const:b74878:8", "const:4:8"]]
- 00b74878 ["CALL", null, ["callee:00418c24:8"]]
+ 00b74940 ["INT_ADD", "register:40f0:8", ["const:b74940:8", "const:4:8"]]
+ 00b74940 ["CALL", null, ["callee:00418c24:8"]]
- 00b74878 bytes eb90e297
+ 00b74940 bytes b990e297
~~~


<a id="compare-1fd339c309e08c01b7177238da0fe49b"></a>

### [`00b7487c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b7487c.md) → [`00b74944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74944.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md)
- 新版 呼出元 1件 [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b748a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b7487c.md#insn-00b748a0)
- 新版 [`00b74968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74944.md#insn-00b74968)

~~~diff
- 00b748a0 ["INT_ADD", "register:40f0:8", ["const:b748a0:8", "const:4:8"]]
- 00b748a0 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b74968 ["INT_ADD", "register:40f0:8", ["const:b74968:8", "const:4:8"]]
+ 00b74968 ["CALL", null, ["callee:00bdb140:8"]]
- 00b748a0 bytes fc990194
+ 00b74968 bytes f6990194
~~~


<a id="compare-a0723cecd6039e5b8eb0cc755f5e19e4"></a>

### [`00b748c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b748c8.md) → [`00b74990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74990.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b748c8.md#insn-00b74924)
- 新版 [`00b749ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74990.md#insn-00b749ec)

~~~diff
- 00b74924 ["INT_ADD", "register:40f0:8", ["const:b74924:8", "const:4:8"]]
- 00b74924 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b749ec ["INT_ADD", "register:40f0:8", ["const:b749ec:8", "const:4:8"]]
+ 00b749ec ["CALL", null, ["callee:00bdb130:8"]]
- 00b74924 bytes d7990194
+ 00b749ec bytes d1990194
~~~


<a id="compare-f2128865c3594c468b7231fedc4bfe75"></a>

### [`00b74950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74950.md) → [`00b74a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74950.md#insn-00b74a1c) · [`00b74a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74950.md#insn-00b74a2c) · [`00b74a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74950.md#insn-00b74a3c)
- 新版 [`00b74ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74ae4) · [`00b74af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74af4) · [`00b74b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74b04)

~~~diff
- 00b74a1c ["INT_ADD", "register:40f0:8", ["const:b74a1c:8", "const:4:8"]]
- 00b74a1c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b74ae4 ["INT_ADD", "register:40f0:8", ["const:b74ae4:8", "const:4:8"]]
+ 00b74ae4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b74a1c bytes 49990194
+ 00b74ae4 bytes 43990194
- 00b74a2c ["INT_ADD", "register:40f0:8", ["const:b74a2c:8", "const:4:8"]]
- 00b74a2c ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b74af4 ["INT_ADD", "register:40f0:8", ["const:b74af4:8", "const:4:8"]]
+ 00b74af4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b74a2c bytes 71990194
+ 00b74af4 bytes 6b990194
- 00b74a3c ["INT_ADD", "register:40f0:8", ["const:b74a3c:8", "const:4:8"]]
- 00b74a3c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b74b04 ["INT_ADD", "register:40f0:8", ["const:b74b04:8", "const:4:8"]]
+ 00b74b04 ["CALL", null, ["callee:00bdb010:8"]]
- 00b74a3c bytes 49990194
+ 00b74b04 bytes 43990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dddab125814c366bd33138ddd1cf5f2"></a>

### [`00b74ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74ad4.md) → [`00b74b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd790.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdd840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd840.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74ad4.md#insn-00b74bb0) · [`00b74bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74ad4.md#insn-00b74bc0) · [`00b74bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74ad4.md#insn-00b74bdc)
- 新版 [`00b74c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74c78) · [`00b74c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74c88) · [`00b74ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74ca4)

~~~diff
- 00b74bb0 ["INT_ADD", "register:40f0:8", ["const:b74bb0:8", "const:4:8"]]
- 00b74bb0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b74c78 ["INT_ADD", "register:40f0:8", ["const:b74c78:8", "const:4:8"]]
+ 00b74c78 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b74bb0 bytes e4980194
+ 00b74c78 bytes de980194
- 00b74bc0 ["INT_ADD", "register:40f0:8", ["const:b74bc0:8", "const:4:8"]]
- 00b74bc0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b74c88 ["INT_ADD", "register:40f0:8", ["const:b74c88:8", "const:4:8"]]
+ 00b74c88 ["CALL", null, ["callee:00bdb010:8"]]
- 00b74bc0 bytes e8980194
+ 00b74c88 bytes e2980194
- 00b74bdc ["INT_ADD", "register:40f0:8", ["const:b74bdc:8", "const:4:8"]]
- 00b74bdc ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00b74ca4 ["INT_ADD", "register:40f0:8", ["const:b74ca4:8", "const:4:8"]]
+ 00b74ca4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00b74bdc bytes 59990194
+ 00b74ca4 bytes 53990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f9c72b064e817557b3f3a2e16934d3"></a>

### [`00b74d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74d24.md) → [`00b74dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74d24.md#insn-00b74dc0) · [`00b74de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74d24.md#insn-00b74de8) · [`00b74e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74d24.md#insn-00b74e28)
- 新版 [`00b74e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74e88) · [`00b74eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74eb0) · [`00b74ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74ef0)

~~~diff
- 00b74dc0 ["INT_ADD", "register:40f0:8", ["const:b74dc0:8", "const:4:8"]]
- 00b74dc0 ["CALL", null, ["callee:00bde1d0:8"]]
+ 00b74e88 ["INT_ADD", "register:40f0:8", ["const:b74e88:8", "const:4:8"]]
+ 00b74e88 ["CALL", null, ["callee:00bde1d0:8"]]
- 00b74dc0 bytes d8a40194
+ 00b74e88 bytes d2a40194
- 00b74de8 ["INT_ADD", "register:40f0:8", ["const:b74de8:8", "const:4:8"]]
- 00b74de8 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b74eb0 ["INT_ADD", "register:40f0:8", ["const:b74eb0:8", "const:4:8"]]
+ 00b74eb0 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b74de8 bytes 82980194
+ 00b74eb0 bytes 7c980194
- 00b74e28 ["INT_ADD", "register:40f0:8", ["const:b74e28:8", "const:4:8"]]
- 00b74e28 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74ef0 ["INT_ADD", "register:40f0:8", ["const:b74ef0:8", "const:4:8"]]
+ 00b74ef0 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74e28 bytes edabe297
+ 00b74ef0 bytes bbabe297
~~~


<a id="compare-da0b7f89263369cf4dc65a822d929281"></a>

### [`00b74e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74e2c.md) → [`00b74ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74e2c.md#insn-00b74e48) · [`00b74e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74e2c.md#insn-00b74e84) · [`00b74ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74e2c.md#insn-00b74ea4)
- 新版 [`00b74f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f10) · [`00b74f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f4c) · [`00b74f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f6c)

~~~diff
- 00b74e48 ["INT_ADD", "register:40f0:8", ["const:b74e48:8", "const:4:8"]]
- 00b74e48 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b74f10 ["INT_ADD", "register:40f0:8", ["const:b74f10:8", "const:4:8"]]
+ 00b74f10 ["CALL", null, ["callee:00bdb140:8"]]
- 00b74e48 bytes 92980194
+ 00b74f10 bytes 8c980194
- 00b74e84 ["INT_ADD", "register:40f0:8", ["const:b74e84:8", "const:4:8"]]
- 00b74e84 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b74f4c ["INT_ADD", "register:40f0:8", ["const:b74f4c:8", "const:4:8"]]
+ 00b74f4c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b74e84 bytes 9f980194
+ 00b74f4c bytes 99980194
- 00b74ea4 ["INT_ADD", "register:40f0:8", ["const:b74ea4:8", "const:4:8"]]
- 00b74ea4 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74f6c ["INT_ADD", "register:40f0:8", ["const:b74f6c:8", "const:4:8"]]
+ 00b74f6c ["CALL", null, ["callee:0041fddc:8"]]
- 00b74ea4 bytes ceabe297
+ 00b74f6c bytes 9cabe297
~~~


<a id="compare-865fa9e8e290385b1a83d4517cff5084"></a>

### [`00b74eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74eac.md) → [`00b74f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74eac.md#insn-00b74f0c) · [`00b74f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74eac.md#insn-00b74f28)
- 新版 [`00b74fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md#insn-00b74fd4) · [`00b74ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md#insn-00b74ff0)

~~~diff
- 00b74f0c ["INT_ADD", "register:40f0:8", ["const:b74f0c:8", "const:4:8"]]
- 00b74f0c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b74fd4 ["INT_ADD", "register:40f0:8", ["const:b74fd4:8", "const:4:8"]]
+ 00b74fd4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b74f0c bytes 7d980194
+ 00b74fd4 bytes 77980194
- 00b74f28 ["INT_ADD", "register:40f0:8", ["const:b74f28:8", "const:4:8"]]
- 00b74f28 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74ff0 ["INT_ADD", "register:40f0:8", ["const:b74ff0:8", "const:4:8"]]
+ 00b74ff0 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74f28 bytes adabe297
+ 00b74ff0 bytes 7babe297
~~~


<a id="compare-4f2f08b79bb233887008fcc0120da73e"></a>

### [`00b760a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760a0.md) → [`00b76168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76168.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b760e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760a0.md#insn-00b760e4)
- 新版 [`00b761ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76168.md#insn-00b761ac)

~~~diff
- 00b760e4 ["INT_ADD", "register:40f0:8", ["const:b760e4:8", "const:4:8"]]
- 00b760e4 ["CALL", null, ["callee:00b75a24:8"]]
+ 00b761ac ["INT_ADD", "register:40f0:8", ["const:b761ac:8", "const:4:8"]]
+ 00b761ac ["CALL", null, ["callee:00b75a24:8"]]
- 00b760e4 bytes 1efeff97
+ 00b761ac bytes 1efeff97
~~~


<a id="compare-e289a7ff104c71edcc844249ab7c5ee9"></a>

### [`00b76424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76424.md) → [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md) FUN_00b764ec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00b7641c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b7641c.md) [`00b767a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767a4.md) [`00b77478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77478.md) [`00bb0018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0018.md) [`00bb0aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0aac.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 5件 [`00b764e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764e4.md) [`00b7686c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md) [`00b77540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md) [`00bb00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb00e0.md) [`00bb0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0b74.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7648c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76424.md#insn-00b7648c) · [`00b764b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76424.md#insn-00b764b4)
- 新版 [`00b76554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md#insn-00b76554) · [`00b7657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md#insn-00b7657c)

~~~diff
- 00b7648c ["INT_ADD", "register:40f0:8", ["const:b7648c:8", "const:4:8"]]
- 00b7648c ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b76554 ["INT_ADD", "register:40f0:8", ["const:b76554:8", "const:4:8"]]
+ 00b76554 ["CALL", null, ["callee:00be0fb0:8"]]
- 00b7648c bytes 9daa0194
+ 00b76554 bytes 97aa0194
- 00b764b4 ["INT_ADD", "register:40f0:8", ["const:b764b4:8", "const:4:8"]]
- 00b764b4 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b7657c ["INT_ADD", "register:40f0:8", ["const:b7657c:8", "const:4:8"]]
+ 00b7657c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b764b4 bytes cf920194
+ 00b7657c bytes c9920194
~~~


<a id="compare-cddad7c7fcfc25d43ee8ec8824fc2460"></a>

### [`00b764ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b764ec.md) → [`00b765b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b76588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76588.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b76650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b764ec.md#insn-00b76584)
- 新版 [`00b7664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md#insn-00b7664c)

~~~diff
- 00b76584 ["INT_ADD", "register:40f0:8", ["const:b76584:8", "const:4:8"]]
- 00b76584 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b7664c ["INT_ADD", "register:40f0:8", ["const:b7664c:8", "const:4:8"]]
+ 00b7664c ["CALL", null, ["callee:006ad8a4:8"]]
- 00b76584 bytes c8dcec97
+ 00b7664c bytes 96dcec97
~~~


<a id="compare-6e64dda760dc19fc4da40cfc4a532a29"></a>

### [`00b767a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767a4.md) → [`00b7686c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignERKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00b76424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76424.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b767f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767a4.md#insn-00b767f4)
- 新版 [`00b768bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md#insn-00b768bc)

~~~diff
- 00b767f4 ["INT_ADD", "register:40f0:8", ["const:b767f4:8", "const:4:8"]]
- 00b767f4 ["CALL", null, ["callee:00b75a24:8"]]
+ 00b768bc ["INT_ADD", "register:40f0:8", ["const:b768bc:8", "const:4:8"]]
+ 00b768bc ["CALL", null, ["callee:00b75a24:8"]]
- 00b767f4 bytes 5afcff97
+ 00b768bc bytes 5afcff97
~~~


<a id="compare-bda237c4d10c904db92393d84f910d40"></a>

### [`00b767f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767f8.md) → [`00b768c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767f8.md#insn-00b76850) · [`00b76868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b767f8.md#insn-00b76868)
- 新版 [`00b76918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md#insn-00b76918) · [`00b76930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md#insn-00b76930)

~~~diff
- 00b76850 ["INT_ADD", "register:40f0:8", ["const:b76850:8", "const:4:8"]]
- 00b76850 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b76918 ["INT_ADD", "register:40f0:8", ["const:b76918:8", "const:4:8"]]
+ 00b76918 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b76850 bytes e8910194
+ 00b76918 bytes e2910194
- 00b76868 ["INT_ADD", "register:40f0:8", ["const:b76868:8", "const:4:8"]]
- 00b76868 ["CALL", null, ["callee:00b75a24:8"]]
+ 00b76930 ["INT_ADD", "register:40f0:8", ["const:b76930:8", "const:4:8"]]
+ 00b76930 ["CALL", null, ["callee:00b75a24:8"]]
- 00b76868 bytes 3dfcff97
+ 00b76930 bytes 3dfcff97
~~~


<a id="compare-bb8cc050ecf8a5506c6d726f3027262c"></a>

### [`00b7686c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b7686c.md) → [`00b76934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9c0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdda70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda70.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7690c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b7686c.md#insn-00b7690c) · [`00b7692c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b7686c.md#insn-00b7692c) · [`00b76950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b7686c.md#insn-00b76950)
- 新版 [`00b769d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b769d4) · [`00b769f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b769f4) · [`00b76a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b76a18)

~~~diff
- 00b7690c ["INT_ADD", "register:40f0:8", ["const:b7690c:8", "const:4:8"]]
- 00b7690c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b769d4 ["INT_ADD", "register:40f0:8", ["const:b769d4:8", "const:4:8"]]
+ 00b769d4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7690c bytes 8d910194
+ 00b769d4 bytes 87910194
- 00b7692c ["INT_ADD", "register:40f0:8", ["const:b7692c:8", "const:4:8"]]
- 00b7692c ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b769f4 ["INT_ADD", "register:40f0:8", ["const:b769f4:8", "const:4:8"]]
+ 00b769f4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b7692c bytes b1910194
+ 00b769f4 bytes ab910194
- 00b76950 ["INT_ADD", "register:40f0:8", ["const:b76950:8", "const:4:8"]]
- 00b76950 ["CALL", null, ["callee:00b75a24:8"]]
+ 00b76a18 ["INT_ADD", "register:40f0:8", ["const:b76a18:8", "const:4:8"]]
+ 00b76a18 ["CALL", null, ["callee:00b75a24:8"]]
- 00b76950 bytes 03fcff97
+ 00b76a18 bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f3fa3061db0204412726a2afe747fcc"></a>

### [`00b76ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ac4.md) → [`00b76b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76b8c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md) [`00be0f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ac4.md#insn-00b76ae8)
- 新版 [`00b76bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76b8c.md#insn-00b76bb0)

~~~diff
- 00b76ae8 ["INT_ADD", "register:40f0:8", ["const:b76ae8:8", "const:4:8"]]
- 00b76ae8 ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b76bb0 ["INT_ADD", "register:40f0:8", ["const:b76bb0:8", "const:4:8"]]
+ 00b76bb0 ["CALL", null, ["callee:00be0fc0:8"]]
- 00b76ae8 bytes 0aa90194
+ 00b76bb0 bytes 04a90194
~~~


<a id="compare-4317008728923a6b6b57db1fb9041538"></a>

### [`00b77428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77428.md) → [`00b774f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b774f0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7746c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77428.md#insn-00b7746c)
- 新版 [`00b77534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b774f0.md#insn-00b77534)

~~~diff
- 00b7746c ["INT_ADD", "register:40f0:8", ["const:b7746c:8", "const:4:8"]]
- 00b7746c ["CALL", null, ["callee:00b75a24:8"]]
+ 00b77534 ["INT_ADD", "register:40f0:8", ["const:b77534:8", "const:4:8"]]
+ 00b77534 ["CALL", null, ["callee:00b75a24:8"]]
- 00b7746c bytes 3cf9ff97
+ 00b77534 bytes 3cf9ff97
~~~


<a id="compare-ae8514abc42b39239cf3f4fa13f7f162"></a>

### [`00b77478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77478.md) → [`00b77540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md) FUN_00b77540

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b77470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77470.md) · 呼出先 2件 [`00b76424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76424.md) [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md)
- 新版 呼出元 1件 [`00b77538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77538.md) · 呼出先 2件 [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77478.md#insn-00b77494)
- 新版 [`00b7755c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md#insn-00b7755c)

~~~diff
- 00b77494 ["INT_ADD", "register:40f0:8", ["const:b77494:8", "const:4:8"]]
- 00b77494 ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b7755c ["INT_ADD", "register:40f0:8", ["const:b7755c:8", "const:4:8"]]
+ 00b7755c ["CALL", null, ["callee:00be0fc0:8"]]
- 00b77494 bytes 9fa60194
+ 00b7755c bytes 99a60194
~~~


<a id="compare-249808e748616343960858ef0d8f5bae"></a>

### [`00b77778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77778.md) → [`00b77840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md) FUN_00b77840

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b7764c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7764c.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 1件 [`00b77714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77714.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b777c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77778.md#insn-00b777c0) · [`00b777ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77778.md#insn-00b777ec)
- 新版 [`00b77888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md#insn-00b77888) · [`00b778b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md#insn-00b778b4)

~~~diff
- 00b777c0 ["INT_ADD", "register:40f0:8", ["const:b777c0:8", "const:4:8"]]
- 00b777c0 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b77888 ["INT_ADD", "register:40f0:8", ["const:b77888:8", "const:4:8"]]
+ 00b77888 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b777c0 bytes 0c8e0194
+ 00b77888 bytes 068e0194
- 00b777ec ["INT_ADD", "register:40f0:8", ["const:b777ec:8", "const:4:8"]]
- 00b777ec ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b778b4 ["INT_ADD", "register:40f0:8", ["const:b778b4:8", "const:4:8"]]
+ 00b778b4 ["CALL", null, ["callee:00be0fb0:8"]]
- 00b777ec bytes c5a50194
+ 00b778b4 bytes bfa50194
~~~


<a id="compare-1399a1d19f477143d69b24e40db87cb5"></a>

### [`00b778f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b778f0.md) → [`00b779b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b779b8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00be0ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ef0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7793c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b778f0.md#insn-00b7793c)
- 新版 [`00b77a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b779b8.md#insn-00b77a04)

~~~diff
- 00b7793c ["INT_ADD", "register:40f0:8", ["const:b7793c:8", "const:4:8"]]
- 00b7793c ["CALL", null, ["callee:00b75a24:8"]]
+ 00b77a04 ["INT_ADD", "register:40f0:8", ["const:b77a04:8", "const:4:8"]]
+ 00b77a04 ["CALL", null, ["callee:00b75a24:8"]]
- 00b7793c bytes 08f8ff97
+ 00b77a04 bytes 08f8ff97
~~~


<a id="compare-d59647775486976fa9003701ca2bcb9a"></a>

### [`00b77940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77940.md) → [`00b77a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b779c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77940.md#insn-00b779c0) · [`00b779f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77940.md#insn-00b779f0)
- 新版 [`00b77a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md#insn-00b77a88) · [`00b77ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md#insn-00b77ab8)

~~~diff
- 00b779c0 ["INT_ADD", "register:40f0:8", ["const:b779c0:8", "const:4:8"]]
- 00b779c0 ["CALL", null, ["callee:00bdda00:8"]]
+ 00b77a88 ["INT_ADD", "register:40f0:8", ["const:b77a88:8", "const:4:8"]]
+ 00b77a88 ["CALL", null, ["callee:00bdda00:8"]]
- 00b779c0 bytes e4970194
+ 00b77a88 bytes de970194
- 00b779f0 ["INT_ADD", "register:40f0:8", ["const:b779f0:8", "const:4:8"]]
- 00b779f0 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b77ab8 ["INT_ADD", "register:40f0:8", ["const:b77ab8:8", "const:4:8"]]
+ 00b77ab8 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b779f0 bytes 808d0194
+ 00b77ab8 bytes 7a8d0194
~~~


<a id="compare-b9f7c438cfa0193c32a4eac3fa41b001"></a>

### [`00b77a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77a44.md) → [`00b77b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77b0c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd940.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77a44.md#insn-00b77ac8)
- 新版 [`00b77b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77b0c.md#insn-00b77b90)

~~~diff
- 00b77ac8 ["INT_ADD", "register:40f0:8", ["const:b77ac8:8", "const:4:8"]]
- 00b77ac8 ["CALL", null, ["callee:00bdda00:8"]]
+ 00b77b90 ["INT_ADD", "register:40f0:8", ["const:b77b90:8", "const:4:8"]]
+ 00b77b90 ["CALL", null, ["callee:00bdda00:8"]]
- 00b77ac8 bytes a2970194
+ 00b77b90 bytes 9c970194
~~~


<a id="compare-09f349a69c6d3b4448e064fcc5d2d2a7"></a>

### [`00b77ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77ba4.md) → [`00b77c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77c6c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00be0f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77ba4.md#insn-00b77bf0)
- 新版 [`00b77cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77c6c.md#insn-00b77cb8)

~~~diff
- 00b77bf0 ["INT_ADD", "register:40f0:8", ["const:b77bf0:8", "const:4:8"]]
- 00b77bf0 ["CALL", null, ["callee:00b75a24:8"]]
+ 00b77cb8 ["INT_ADD", "register:40f0:8", ["const:b77cb8:8", "const:4:8"]]
+ 00b77cb8 ["CALL", null, ["callee:00b75a24:8"]]
- 00b77bf0 bytes 5bf7ff97
+ 00b77cb8 bytes 5bf7ff97
~~~


<a id="compare-b6763b5834baf07a0ef4510e9cf28101"></a>

### [`00b7974c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md) → [`00b79814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md#insn-00b79774) · [`00b797b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md#insn-00b797b8) · [`00b797e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md#insn-00b797e4)
- 新版 [`00b7983c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b7983c) · [`00b79880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b79880) · [`00b798ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md#insn-00b798ac)

~~~diff
- 00b79774 ["INT_ADD", "register:40f0:8", ["const:b79774:8", "const:4:8"]]
- 00b79774 ["CALL", null, ["callee:00b7b3a4:8"]]
+ 00b7983c ["INT_ADD", "register:40f0:8", ["const:b7983c:8", "const:4:8"]]
+ 00b7983c ["CALL", null, ["callee:00b7b3a4:8"]]
- 00b79774 bytes da060094
+ 00b7983c bytes da060094
- 00b797b8 ["INT_ADD", "register:40f0:8", ["const:b797b8:8", "const:4:8"]]
- 00b797b8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b79880 ["INT_ADD", "register:40f0:8", ["const:b79880:8", "const:4:8"]]
+ 00b79880 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b797b8 bytes e2850194
+ 00b79880 bytes dc850194
- 00b797e4 ["INT_ADD", "register:40f0:8", ["const:b797e4:8", "const:4:8"]]
- 00b797e4 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b798ac ["INT_ADD", "register:40f0:8", ["const:b798ac:8", "const:4:8"]]
+ 00b798ac ["CALL", null, ["callee:00bdb160:8"]]
- 00b797e4 bytes 33860194
+ 00b798ac bytes 2d860194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629e902d765b99e76c534121522ebf5a"></a>

### [`00b7ab10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ab10.md) → [`00b7abd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md) _ZNSt6__ndk19to_stringEd

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd810.md) · 呼出先 3件 [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md) [`00be1000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1000.md)
- 新版 呼出元 1件 [`00bdd8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8c0.md) · 呼出先 3件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ab50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ab10.md#insn-00b7ab50) · [`00b7ab84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ab10.md#insn-00b7ab84) · [`00b7aba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ab10.md#insn-00b7aba4)
- 新版 [`00b7ac18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac18) · [`00b7ac4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac4c) · [`00b7ac6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7abd8.md#insn-00b7ac6c)

~~~diff
- 00b7ab50 ["INT_ADD", "register:40f0:8", ["const:b7ab50:8", "const:4:8"]]
- 00b7ab50 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b7ac18 ["INT_ADD", "register:40f0:8", ["const:b7ac18:8", "const:4:8"]]
+ 00b7ac18 ["CALL", null, ["callee:00bdef70:8"]]
- 00b7ab50 bytes dc900194
+ 00b7ac18 bytes d6900194
- 00b7ab84 ["INT_ADD", "register:40f0:8", ["const:b7ab84:8", "const:4:8"]]
- 00b7ab84 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b7ac4c ["INT_ADD", "register:40f0:8", ["const:b7ac4c:8", "const:4:8"]]
+ 00b7ac4c ["CALL", null, ["callee:00bdef70:8"]]
- 00b7ab84 bytes cf900194
+ 00b7ac4c bytes c9900194
- 00b7aba4 ["INT_ADD", "register:40f0:8", ["const:b7aba4:8", "const:4:8"]]
- 00b7aba4 ["CALL", null, ["callee:00be10b0:8"]]
+ 00b7ac6c ["INT_ADD", "register:40f0:8", ["const:b7ac6c:8", "const:4:8"]]
+ 00b7ac6c ["CALL", null, ["callee:00be10b0:8"]]
- 00b7aba4 bytes 17990194
+ 00b7ac6c bytes 11990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33763f97117ab82dc0ca07bd850ab81f"></a>

### [`00b7ae38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ae38.md) → [`00b7af00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md) _ZNSt6__ndk110to_wstringEf

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd940.md) [`00be1010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1010.md) [`00be1020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ae64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ae38.md#insn-00b7ae64) · [`00b7ae9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ae38.md#insn-00b7ae9c) · [`00b7aee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7ae38.md#insn-00b7aee0)
- 新版 [`00b7af2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7af2c) · [`00b7af64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7af64) · [`00b7afa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7af00.md#insn-00b7afa8)

~~~diff
- 00b7ae64 ["INT_ADD", "register:40f0:8", ["const:b7ae64:8", "const:4:8"]]
- 00b7ae64 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7af2c ["INT_ADD", "register:40f0:8", ["const:b7af2c:8", "const:4:8"]]
+ 00b7af2c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7ae64 bytes 37800194
+ 00b7af2c bytes 31800194
- 00b7ae9c ["INT_ADD", "register:40f0:8", ["const:b7ae9c:8", "const:4:8"]]
- 00b7ae9c ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00b7af64 ["INT_ADD", "register:40f0:8", ["const:b7af64:8", "const:4:8"]]
+ 00b7af64 ["CALL", null, ["callee:00bdd9f0:8"]]
- 00b7ae9c bytes a98a0194
+ 00b7af64 bytes a38a0194
- 00b7aee0 ["INT_ADD", "register:40f0:8", ["const:b7aee0:8", "const:4:8"]]
- 00b7aee0 ["CALL", null, ["callee:00be10c0:8"]]
+ 00b7afa8 ["INT_ADD", "register:40f0:8", ["const:b7afa8:8", "const:4:8"]]
+ 00b7afa8 ["CALL", null, ["callee:00be10c0:8"]]
- 00b7aee0 bytes 4c980194
+ 00b7afa8 bytes 46980194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858c7326f76259668124c24f6d57e986"></a>

### [`00b7af80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7af80.md) → [`00b7b048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md) _ZNSt6__ndk110to_wstringEd

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd940.md) [`00be1010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1010.md) [`00be1020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7afac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7af80.md#insn-00b7afac) · [`00b7afe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7af80.md#insn-00b7afe4) · [`00b7b024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7af80.md#insn-00b7b024)
- 新版 [`00b7b074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b074) · [`00b7b0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b0ac) · [`00b7b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b048.md#insn-00b7b0ec)

~~~diff
- 00b7afac ["INT_ADD", "register:40f0:8", ["const:b7afac:8", "const:4:8"]]
- 00b7afac ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7b074 ["INT_ADD", "register:40f0:8", ["const:b7b074:8", "const:4:8"]]
+ 00b7b074 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7afac bytes e57f0194
+ 00b7b074 bytes df7f0194
- 00b7afe4 ["INT_ADD", "register:40f0:8", ["const:b7afe4:8", "const:4:8"]]
- 00b7afe4 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00b7b0ac ["INT_ADD", "register:40f0:8", ["const:b7b0ac:8", "const:4:8"]]
+ 00b7b0ac ["CALL", null, ["callee:00bdd9f0:8"]]
- 00b7afe4 bytes 578a0194
+ 00b7b0ac bytes 518a0194
- 00b7b024 ["INT_ADD", "register:40f0:8", ["const:b7b024:8", "const:4:8"]]
- 00b7b024 ["CALL", null, ["callee:00be10c0:8"]]
+ 00b7b0ec ["INT_ADD", "register:40f0:8", ["const:b7b0ec:8", "const:4:8"]]
+ 00b7b0ec ["CALL", null, ["callee:00be10c0:8"]]
- 00b7b024 bytes fb970194
+ 00b7b0ec bytes f5970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ead202cf64ddfbb842d47f5001f258"></a>

### [`00b7b0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b0c4.md) → [`00b7b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md) _ZNSt6__ndk110to_wstringEe

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd940.md) [`00be1010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1010.md) [`00be1020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) [`00be10c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7b0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b0c4.md#insn-00b7b0ec) · [`00b7b124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b0c4.md#insn-00b7b124) · [`00b7b164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b0c4.md#insn-00b7b164)
- 新版 [`00b7b1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b1b4) · [`00b7b1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b1ec) · [`00b7b22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b18c.md#insn-00b7b22c)

~~~diff
- 00b7b0ec ["INT_ADD", "register:40f0:8", ["const:b7b0ec:8", "const:4:8"]]
- 00b7b0ec ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7b1b4 ["INT_ADD", "register:40f0:8", ["const:b7b1b4:8", "const:4:8"]]
+ 00b7b1b4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7b0ec bytes 957f0194
+ 00b7b1b4 bytes 8f7f0194
- 00b7b124 ["INT_ADD", "register:40f0:8", ["const:b7b124:8", "const:4:8"]]
- 00b7b124 ["CALL", null, ["callee:00bdd9f0:8"]]
+ 00b7b1ec ["INT_ADD", "register:40f0:8", ["const:b7b1ec:8", "const:4:8"]]
+ 00b7b1ec ["CALL", null, ["callee:00bdd9f0:8"]]
- 00b7b124 bytes 078a0194
+ 00b7b1ec bytes 018a0194
- 00b7b164 ["INT_ADD", "register:40f0:8", ["const:b7b164:8", "const:4:8"]]
- 00b7b164 ["CALL", null, ["callee:00be10c0:8"]]
+ 00b7b22c ["INT_ADD", "register:40f0:8", ["const:b7b22c:8", "const:4:8"]]
+ 00b7b22c ["CALL", null, ["callee:00be10c0:8"]]
- 00b7b164 bytes ab970194
+ 00b7b22c bytes a5970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e7ec69e8670d36fee14e63c01361d1"></a>

### [`00b7b890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b890.md) → [`00b7b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md) FUN_00b7b958

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7b8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b890.md#insn-00b7b8b4)
- 新版 [`00b7b97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md#insn-00b7b97c)

~~~diff
- 00b7b8b4 ["INT_ADD", "register:40f0:8", ["const:b7b8b4:8", "const:4:8"]]
- 00b7b8b4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7b97c ["INT_ADD", "register:40f0:8", ["const:b7b97c:8", "const:4:8"]]
+ 00b7b97c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7b8b4 bytes a37d0194
+ 00b7b97c bytes 9d7d0194
~~~


<a id="compare-c97819bbb51faae0a5555458ae0f0d3d"></a>

### [`00b7c0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c0c0.md) → [`00b7c188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c188.md) _ZNSt6__ndk112system_errorD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c0c0.md#insn-00b7c0d4)
- 新版 [`00b7c19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c188.md#insn-00b7c19c)

~~~diff
- 00b7c0d4 ["INT_ADD", "register:40f0:8", ["const:b7c0d4:8", "const:4:8"]]
- 00b7c0d4 ["CALL", null, ["callee:00be1130:8"]]
+ 00b7c19c ["INT_ADD", "register:40f0:8", ["const:b7c19c:8", "const:4:8"]]
+ 00b7c19c ["CALL", null, ["callee:00be1130:8"]]
- 00b7c0d4 bytes eb930194
+ 00b7c19c bytes e5930194
~~~


<a id="compare-16e1b8ba0fdca3f994a6194505f1110c"></a>

### [`00b7c174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c174.md) → [`00b7c23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c23c.md) FUN_00b7c23c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c174.md#insn-00b7c188)
- 新版 [`00b7c250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c23c.md#insn-00b7c250)

~~~diff
- 00b7c188 ["INT_ADD", "register:40f0:8", ["const:b7c188:8", "const:4:8"]]
- 00b7c188 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b7c250 ["INT_ADD", "register:40f0:8", ["const:b7c250:8", "const:4:8"]]
+ 00b7c250 ["CALL", null, ["callee:00be0ea0:8"]]
- 00b7c188 bytes 1a930194
+ 00b7c250 bytes 14930194
~~~


<a id="compare-02557cc8f855a1a859ab1d9e279d8cbb"></a>

### [`00b7c1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c1a0.md) → [`00b7c268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c268.md) FUN_00b7c268

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c1a0.md#insn-00b7c1b4)
- 新版 [`00b7c27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c268.md#insn-00b7c27c)

~~~diff
- 00b7c1b4 ["INT_ADD", "register:40f0:8", ["const:b7c1b4:8", "const:4:8"]]
- 00b7c1b4 ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b7c27c ["INT_ADD", "register:40f0:8", ["const:b7c27c:8", "const:4:8"]]
+ 00b7c27c ["CALL", null, ["callee:00be0ea0:8"]]
- 00b7c1b4 bytes 0f930194
+ 00b7c27c bytes 09930194
~~~


<a id="compare-e968df1b07d006675ee2057c757c4e6c"></a>

### [`00b7c208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c208.md) → [`00b7c2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c2d0.md) _ZNKSt6__ndk114error_category10equivalentEiRKNS_15error_conditionE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c208.md#insn-00b7c224)
- 新版 [`00b7c2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c2d0.md#insn-00b7c2ec)

~~~diff
- 00b7c224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7c224 ["INT_ADD", "register:40f0:8", ["const:b7c224:8", "const:4:8"]]
- 00b7c224 ["CALLIND", null, ["register:0:8"]]
+ 00b7c2ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7c2ec ["INT_ADD", "register:40f0:8", ["const:b7c2ec:8", "const:4:8"]]
+ 00b7c2ec ["CALLIND", null, ["register:0:8"]]
- 00b7c224 bytes 00013fd6
+ 00b7c2ec bytes 00013fd6
~~~


<a id="compare-40106116cb0e4c28cb6a3c5f80dabf8d"></a>

### [`00b7c268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c268.md) → [`00b7c330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c330.md) _ZNSt6__ndk118condition_variableD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) · 呼出先 1件 [`00be0540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0540.md)
- 新版 呼出元 1件 [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) · 呼出先 1件 [`00be05f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c268.md#insn-00b7c274)
- 新版 [`00b7c33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c330.md#insn-00b7c33c)

~~~diff
- 00b7c274 ["INT_ADD", "register:40f0:8", ["const:b7c274:8", "const:4:8"]]
- 00b7c274 ["CALL", null, ["callee:00be05f0:8"]]
+ 00b7c33c ["INT_ADD", "register:40f0:8", ["const:b7c33c:8", "const:4:8"]]
+ 00b7c33c ["CALL", null, ["callee:00be05f0:8"]]
- 00b7c274 bytes b3900194
+ 00b7c33c bytes ad900194
~~~


<a id="compare-af2967bef2d08f4ac60cec318e61a0a1"></a>

### [`00b7c288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c288.md) → [`00b7c350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c350.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md) · 呼出先 1件 [`00be0550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0550.md)
- 新版 呼出元 1件 [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) · 呼出先 1件 [`00be0600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c288.md#insn-00b7c294)
- 新版 [`00b7c35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c350.md#insn-00b7c35c)

~~~diff
- 00b7c294 ["INT_ADD", "register:40f0:8", ["const:b7c294:8", "const:4:8"]]
- 00b7c294 ["CALL", null, ["callee:00be0600:8"]]
+ 00b7c35c ["INT_ADD", "register:40f0:8", ["const:b7c35c:8", "const:4:8"]]
+ 00b7c35c ["CALL", null, ["callee:00be0600:8"]]
- 00b7c294 bytes af900194
+ 00b7c35c bytes a9900194
~~~


<a id="compare-161a2ecab9bac2accdf0d5fb6ac2f0e1"></a>

### [`00b7c2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c2a8.md) → [`00b7c370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c370.md) _ZNSt6__ndk118condition_variable10notify_allEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb430.md) · 呼出先 1件 [`00be10c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10c0.md)
- 新版 呼出元 1件 [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md) · 呼出先 1件 [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c2a8.md#insn-00b7c2b4)
- 新版 [`00b7c37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c370.md#insn-00b7c37c)

~~~diff
- 00b7c2b4 ["INT_ADD", "register:40f0:8", ["const:b7c2b4:8", "const:4:8"]]
- 00b7c2b4 ["CALL", null, ["callee:00be1170:8"]]
+ 00b7c37c ["INT_ADD", "register:40f0:8", ["const:b7c37c:8", "const:4:8"]]
+ 00b7c37c ["CALL", null, ["callee:00be1170:8"]]
- 00b7c2b4 bytes 83930194
+ 00b7c37c bytes 7d930194
~~~


<a id="compare-98e59c7e7fe89490cc557bfadbed24c5"></a>

### [`00b7c3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c3b4.md) → [`00b7c47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md) _ZNSt6__ndk125notify_all_at_thread_exitERNS_18condition_variableENS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md) [`00bdb1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1e0.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00be10f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00be11a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c3b4.md#insn-00b7c3d0) · [`00b7c3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c3b4.md#insn-00b7c3dc) · [`00b7c3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c3b4.md#insn-00b7c3e8)
- 新版 [`00b7c498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c498) · [`00b7c4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c4a4) · [`00b7c4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c47c.md#insn-00b7c4b0)

~~~diff
- 00b7c3d0 ["INT_ADD", "register:40f0:8", ["const:b7c3d0:8", "const:4:8"]]
- 00b7c3d0 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c498 ["INT_ADD", "register:40f0:8", ["const:b7c498:8", "const:4:8"]]
+ 00b7c498 ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c3d0 bytes 847b0194
+ 00b7c498 bytes 7e7b0194
- 00b7c3dc ["INT_ADD", "register:40f0:8", ["const:b7c3dc:8", "const:4:8"]]
- 00b7c3dc ["CALL", null, ["callee:00be11a0:8"]]
+ 00b7c4a4 ["INT_ADD", "register:40f0:8", ["const:b7c4a4:8", "const:4:8"]]
+ 00b7c4a4 ["CALL", null, ["callee:00be11a0:8"]]
- 00b7c3dc bytes 45930194
+ 00b7c4a4 bytes 3f930194
- 00b7c3e8 ["INT_ADD", "register:40f0:8", ["const:b7c3e8:8", "const:4:8"]]
- 00b7c3e8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7c4b0 ["INT_ADD", "register:40f0:8", ["const:b7c4b0:8", "const:4:8"]]
+ 00b7c4b0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7c3e8 bytes d67a0194
+ 00b7c4b0 bytes d07a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e76027643bc7ab258a6ae2f9a2db1a87"></a>

### [`00b7c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c6c4.md) → [`00b7c78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c78c.md) _ZNSt6__ndk112future_errorD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c6c4.md#insn-00b7c6d8)
- 新版 [`00b7c7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c78c.md#insn-00b7c7a0)

~~~diff
- 00b7c6d8 ["INT_ADD", "register:40f0:8", ["const:b7c6d8:8", "const:4:8"]]
- 00b7c6d8 ["CALL", null, ["callee:00bdb4d0:8"]]
+ 00b7c7a0 ["INT_ADD", "register:40f0:8", ["const:b7c7a0:8", "const:4:8"]]
+ 00b7c7a0 ["CALL", null, ["callee:00bdb4d0:8"]]
- 00b7c6d8 bytes 527b0194
+ 00b7c7a0 bytes 4c7b0194
~~~


<a id="compare-06ce6125f5e5983cd2ec77d171cfe498"></a>

### [`00b7c700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c700.md) → [`00b7c7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb600.md) · 呼出先 5件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb430.md)
- 新版 呼出元 1件 [`00bdb6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6b0.md) · 呼出先 5件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c700.md#insn-00b7c71c) · [`00b7c734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c700.md#insn-00b7c734) · [`00b7c750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c700.md#insn-00b7c750)
- 新版 [`00b7c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c7e4) · [`00b7c7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c7fc) · [`00b7c818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c7c8.md#insn-00b7c818)

~~~diff
- 00b7c71c ["INT_ADD", "register:40f0:8", ["const:b7c71c:8", "const:4:8"]]
- 00b7c71c ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7c7e4 ["INT_ADD", "register:40f0:8", ["const:b7c7e4:8", "const:4:8"]]
+ 00b7c7e4 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c71c bytes 9d7a0194
+ 00b7c7e4 bytes 977a0194
- 00b7c734 ["INT_ADD", "register:40f0:8", ["const:b7c734:8", "const:4:8"]]
- 00b7c734 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b7c7fc ["INT_ADD", "register:40f0:8", ["const:b7c7fc:8", "const:4:8"]]
+ 00b7c7fc ["CALL", null, ["callee:00bdb450:8"]]
- 00b7c734 bytes 1b7b0194
+ 00b7c7fc bytes 157b0194
- 00b7c750 ["INT_ADD", "register:40f0:8", ["const:b7c750:8", "const:4:8"]]
- 00b7c750 ["CALL", null, ["callee:00bdb4e0:8"]]
+ 00b7c818 ["INT_ADD", "register:40f0:8", ["const:b7c818:8", "const:4:8"]]
+ 00b7c818 ["CALL", null, ["callee:00bdb4e0:8"]]
- 00b7c750 bytes 387b0194
+ 00b7c818 bytes 327b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4e3ef794b7b6e035b78140615e3ebe"></a>

### [`00b7c78c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c78c.md) → [`00b7c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1120.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1e0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`00be11d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11d0.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c78c.md#insn-00b7c7a8) · [`00b7c7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c78c.md#insn-00b7c7c0) · [`00b7c7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c78c.md#insn-00b7c7d4)
- 新版 [`00b7c870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c870) · [`00b7c888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c888) · [`00b7c89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c854.md#insn-00b7c89c)

~~~diff
- 00b7c7a8 ["INT_ADD", "register:40f0:8", ["const:b7c7a8:8", "const:4:8"]]
- 00b7c7a8 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7c870 ["INT_ADD", "register:40f0:8", ["const:b7c870:8", "const:4:8"]]
+ 00b7c870 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c7a8 bytes 7a7a0194
+ 00b7c870 bytes 747a0194
- 00b7c7c0 ["INT_ADD", "register:40f0:8", ["const:b7c7c0:8", "const:4:8"]]
- 00b7c7c0 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b7c888 ["INT_ADD", "register:40f0:8", ["const:b7c888:8", "const:4:8"]]
+ 00b7c888 ["CALL", null, ["callee:00bdb450:8"]]
- 00b7c7c0 bytes f87a0194
+ 00b7c888 bytes f27a0194
- 00b7c7d4 ["INT_ADD", "register:40f0:8", ["const:b7c7d4:8", "const:4:8"]]
- 00b7c7d4 ["CALL", null, ["callee:00bdb290:8"]]
+ 00b7c89c ["INT_ADD", "register:40f0:8", ["const:b7c89c:8", "const:4:8"]]
+ 00b7c89c ["CALL", null, ["callee:00bdb290:8"]]
- 00b7c7d4 bytes 837a0194
+ 00b7c89c bytes 7d7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f81006bc64f1adaf15462689b7b0781"></a>

### [`00b7c820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c820.md) → [`00b7c8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb410.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb430.md)
- 新版 呼出元 1件 [`00bdb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4c0.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c820.md#insn-00b7c844) · [`00b7c860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c820.md#insn-00b7c860) · [`00b7c870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c820.md#insn-00b7c870)
- 新版 [`00b7c90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c90c) · [`00b7c928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c928) · [`00b7c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c8e8.md#insn-00b7c938)

~~~diff
- 00b7c844 ["INT_ADD", "register:40f0:8", ["const:b7c844:8", "const:4:8"]]
- 00b7c844 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7c90c ["INT_ADD", "register:40f0:8", ["const:b7c90c:8", "const:4:8"]]
+ 00b7c90c ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c844 bytes 537a0194
+ 00b7c90c bytes 4d7a0194
- 00b7c860 ["INT_ADD", "register:40f0:8", ["const:b7c860:8", "const:4:8"]]
- 00b7c860 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b7c928 ["INT_ADD", "register:40f0:8", ["const:b7c928:8", "const:4:8"]]
+ 00b7c928 ["CALL", null, ["callee:00bdb450:8"]]
- 00b7c860 bytes d07a0194
+ 00b7c928 bytes ca7a0194
- 00b7c870 ["INT_ADD", "register:40f0:8", ["const:b7c870:8", "const:4:8"]]
- 00b7c870 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b7c938 ["INT_ADD", "register:40f0:8", ["const:b7c938:8", "const:4:8"]]
+ 00b7c938 ["CALL", null, ["callee:00be0ee0:8"]]
- 00b7c870 bytes 70910194
+ 00b7c938 bytes 6a910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f71f84772d1d48d75c832bc19615011"></a>

### [`00b7c8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c8c4.md) → [`00b7c98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1140.md) · 呼出先 8件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1e0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`00be11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11f0.md) · 呼出先 8件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c8c4.md#insn-00b7c8e8) · [`00b7c904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c8c4.md#insn-00b7c904) · [`00b7c914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c8c4.md#insn-00b7c914)
- 新版 [`00b7c9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9b0) · [`00b7c9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9cc) · [`00b7c9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c98c.md#insn-00b7c9dc)

~~~diff
- 00b7c8e8 ["INT_ADD", "register:40f0:8", ["const:b7c8e8:8", "const:4:8"]]
- 00b7c8e8 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7c9b0 ["INT_ADD", "register:40f0:8", ["const:b7c9b0:8", "const:4:8"]]
+ 00b7c9b0 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c8e8 bytes 2a7a0194
+ 00b7c9b0 bytes 247a0194
- 00b7c904 ["INT_ADD", "register:40f0:8", ["const:b7c904:8", "const:4:8"]]
- 00b7c904 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b7c9cc ["INT_ADD", "register:40f0:8", ["const:b7c9cc:8", "const:4:8"]]
+ 00b7c9cc ["CALL", null, ["callee:00bdb450:8"]]
- 00b7c904 bytes a77a0194
+ 00b7c9cc bytes a17a0194
- 00b7c914 ["INT_ADD", "register:40f0:8", ["const:b7c914:8", "const:4:8"]]
- 00b7c914 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00b7c9dc ["INT_ADD", "register:40f0:8", ["const:b7c9dc:8", "const:4:8"]]
+ 00b7c9dc ["CALL", null, ["callee:00be0ee0:8"]]
- 00b7c914 bytes 47910194
+ 00b7c9dc bytes 41910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68934072bd348b8c0a446faa412c8844"></a>

### [`00b7c968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c968.md) → [`00b7ca30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md) _ZNSt6__ndk117__assoc_sub_state12__make_readyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1150.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb430.md)
- 新版 呼出元 1件 [`00be1200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1200.md) · 呼出先 3件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c968.md#insn-00b7c980) · [`00b7c994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c968.md#insn-00b7c994)
- 新版 [`00b7ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md#insn-00b7ca48) · [`00b7ca5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca30.md#insn-00b7ca5c)

~~~diff
- 00b7c980 ["INT_ADD", "register:40f0:8", ["const:b7c980:8", "const:4:8"]]
- 00b7c980 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7ca48 ["INT_ADD", "register:40f0:8", ["const:b7ca48:8", "const:4:8"]]
+ 00b7ca48 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c980 bytes 047a0194
+ 00b7ca48 bytes fe790194
- 00b7c994 ["INT_ADD", "register:40f0:8", ["const:b7c994:8", "const:4:8"]]
- 00b7c994 ["CALL", null, ["callee:00bdb4e0:8"]]
+ 00b7ca5c ["INT_ADD", "register:40f0:8", ["const:b7ca5c:8", "const:4:8"]]
+ 00b7ca5c ["CALL", null, ["callee:00bdb4e0:8"]]
- 00b7c994 bytes a77a0194
+ 00b7ca5c bytes a17a0194
~~~


<a id="compare-b48637080d624913c35fc484e51bbe59"></a>

### [`00b7c9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c9ac.md) → [`00b7ca74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1160.md) · 呼出先 7件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00be1210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1210.md) · 呼出先 7件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7c9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c9ac.md#insn-00b7c9d8) · [`00b7c9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c9ac.md#insn-00b7c9f0) · [`00b7ca0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c9ac.md#insn-00b7ca0c)
- 新版 [`00b7caa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7caa0) · [`00b7cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7cab8) · [`00b7cad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md#insn-00b7cad4)

~~~diff
- 00b7c9d8 ["INT_ADD", "register:40f0:8", ["const:b7c9d8:8", "const:4:8"]]
- 00b7c9d8 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7caa0 ["INT_ADD", "register:40f0:8", ["const:b7caa0:8", "const:4:8"]]
+ 00b7caa0 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7c9d8 bytes ee790194
+ 00b7caa0 bytes e8790194
- 00b7c9f0 ["INT_ADD", "register:40f0:8", ["const:b7c9f0:8", "const:4:8"]]
- 00b7c9f0 ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00b7cab8 ["INT_ADD", "register:40f0:8", ["const:b7cab8:8", "const:4:8"]]
+ 00b7cab8 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00b7c9f0 bytes d07a0194
+ 00b7cab8 bytes ca7a0194
- 00b7ca0c ["INT_ADD", "register:40f0:8", ["const:b7ca0c:8", "const:4:8"]]
- 00b7ca0c ["CALL", null, ["callee:00bdb250:8"]]
+ 00b7cad4 ["INT_ADD", "register:40f0:8", ["const:b7cad4:8", "const:4:8"]]
+ 00b7cad4 ["CALL", null, ["callee:00bdb250:8"]]
- 00b7ca0c bytes e5790194
+ 00b7cad4 bytes df790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fab1088ccd838a91b1cde9a2219c39b"></a>

### [`00b7cb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md) → [`00b7cbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5e0.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00bdb690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb690.md) · 呼出先 3件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md#insn-00b7cb50) · [`00b7cb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md#insn-00b7cb68) · [`00b7cb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md#insn-00b7cb80)
- 新版 [`00b7cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc18) · [`00b7cc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc30) · [`00b7cc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md#insn-00b7cc48)

~~~diff
- 00b7cb50 ["INT_ADD", "register:40f0:8", ["const:b7cb50:8", "const:4:8"]]
- 00b7cb50 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7cc18 ["INT_ADD", "register:40f0:8", ["const:b7cc18:8", "const:4:8"]]
+ 00b7cc18 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7cb50 bytes 90790194
+ 00b7cc18 bytes 8a790194
- 00b7cb68 ["INT_ADD", "register:40f0:8", ["const:b7cb68:8", "const:4:8"]]
- 00b7cb68 ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00b7cc30 ["INT_ADD", "register:40f0:8", ["const:b7cc30:8", "const:4:8"]]
+ 00b7cc30 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00b7cb68 bytes 727a0194
+ 00b7cc30 bytes 6c7a0194
- 00b7cb80 ["INT_ADD", "register:40f0:8", ["const:b7cb80:8", "const:4:8"]]
- 00b7cb80 ["CALL", null, ["callee:00bdb250:8"]]
+ 00b7cc48 ["INT_ADD", "register:40f0:8", ["const:b7cc48:8", "const:4:8"]]
+ 00b7cc48 ["CALL", null, ["callee:00bdb250:8"]]
- 00b7cb80 bytes 88790194
+ 00b7cc48 bytes 82790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4038f83d9b2b6e5325f6a0fe10a0c8e"></a>

### [`00b7cbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbc8.md) → [`00b7cc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cc90.md) _ZNSt6__ndk117__assoc_sub_state9__executeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cbd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbc8.md#insn-00b7cbd8)
- 新版 [`00b7cca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cc90.md#insn-00b7cca0)

~~~diff
- 00b7cbd8 ["INT_ADD", "register:40f0:8", ["const:b7cbd8:8", "const:4:8"]]
- 00b7cbd8 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7cca0 ["INT_ADD", "register:40f0:8", ["const:b7cca0:8", "const:4:8"]]
+ 00b7cca0 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cbd8 bytes 09ebe297
+ 00b7cca0 bytes d7eae297
~~~


<a id="compare-ed15b6283ada351f3f19be1423b55667"></a>

### [`00b7cbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbdc.md) → [`00b7cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md) _ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md) · 呼出先 4件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md)
- 新版 呼出元 1件 [`00bdb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb680.md) · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cbf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbdc.md#insn-00b7cbf8) · [`00b7cc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbdc.md#insn-00b7cc0c) · [`00b7cc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbdc.md#insn-00b7cc30)
- 新版 [`00b7ccc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccc0) · [`00b7ccd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccd4) · [`00b7ccf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md#insn-00b7ccf8)

~~~diff
- 00b7cbf8 ["INT_ADD", "register:40f0:8", ["const:b7cbf8:8", "const:4:8"]]
- 00b7cbf8 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7ccc0 ["INT_ADD", "register:40f0:8", ["const:b7ccc0:8", "const:4:8"]]
+ 00b7ccc0 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7cbf8 bytes 66790194
+ 00b7ccc0 bytes 60790194
- 00b7cc0c ["INT_ADD", "register:40f0:8", ["const:b7cc0c:8", "const:4:8"]]
- 00b7cc0c ["CALL", null, ["callee:00bd6e20:8"]]
+ 00b7ccd4 ["INT_ADD", "register:40f0:8", ["const:b7ccd4:8", "const:4:8"]]
+ 00b7ccd4 ["CALL", null, ["callee:00bd6e20:8"]]
- 00b7cc0c bytes 55680194
+ 00b7ccd4 bytes 53680194
- 00b7cc30 ["INT_ADD", "register:40f0:8", ["const:b7cc30:8", "const:4:8"]]
- 00b7cc30 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7ccf8 ["INT_ADD", "register:40f0:8", ["const:b7ccf8:8", "const:4:8"]]
+ 00b7ccf8 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cc30 bytes f3eae297
+ 00b7ccf8 bytes c1eae297
~~~


<a id="compare-28167cfa7a1d9e7e216aa76362252891"></a>

### [`00b7cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc48.md) → [`00b7cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd10.md) _ZNSt6__ndk16futureIvED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb590.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cc68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc48.md#insn-00b7cc68)
- 新版 [`00b7cd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd10.md#insn-00b7cd30)

~~~diff
- 00b7cc68 ["INT_ADD", "register:40f0:8", ["const:b7cc68:8", "const:4:8"]]
- 00b7cc68 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b7cd30 ["INT_ADD", "register:40f0:8", ["const:b7cd30:8", "const:4:8"]]
+ 00b7cd30 ["CALL", null, ["callee:00bd6e50:8"]]
- 00b7cc68 bytes 4a680194
+ 00b7cd30 bytes 48680194
~~~


<a id="compare-fc29746f8e3af00b2a12b48909feb75c"></a>

### [`00b7cc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc9c.md) → [`00b7cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md) _ZNSt6__ndk16futureIvE3getEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be1160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1160.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be1210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7ccb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc9c.md#insn-00b7ccb8) · [`00b7ccc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc9c.md#insn-00b7ccc4)
- 新版 [`00b7cd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md#insn-00b7cd80) · [`00b7cd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cd64.md#insn-00b7cd8c)

~~~diff
- 00b7ccb8 ["INT_ADD", "register:40f0:8", ["const:b7ccb8:8", "const:4:8"]]
- 00b7ccb8 ["CALL", null, ["callee:00be1210:8"]]
+ 00b7cd80 ["INT_ADD", "register:40f0:8", ["const:b7cd80:8", "const:4:8"]]
+ 00b7cd80 ["CALL", null, ["callee:00be1210:8"]]
- 00b7ccb8 bytes 2a910194
+ 00b7cd80 bytes 24910194
- 00b7ccc4 ["INT_ADD", "register:40f0:8", ["const:b7ccc4:8", "const:4:8"]]
- 00b7ccc4 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b7cd8c ["INT_ADD", "register:40f0:8", ["const:b7cd8c:8", "const:4:8"]]
+ 00b7cd8c ["CALL", null, ["callee:00bd6e50:8"]]
- 00b7ccc4 bytes 33680194
+ 00b7cd8c bytes 31680194
~~~


<a id="compare-2670a53609745ff0c122947b19751a14"></a>

### [`00b7cf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf10.md) → [`00b7cfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cfd8.md) _ZNSt6__ndk17promiseIvE10get_futureEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cf34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf10.md#insn-00b7cf34)
- 新版 [`00b7cffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cfd8.md#insn-00b7cffc)

~~~diff
- 00b7cf34 ["INT_ADD", "register:40f0:8", ["const:b7cf34:8", "const:4:8"]]
- 00b7cf34 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7cffc ["INT_ADD", "register:40f0:8", ["const:b7cffc:8", "const:4:8"]]
+ 00b7cffc ["CALL", null, ["callee:004377fc:8"]]
- 00b7cf34 bytes 32eae297
+ 00b7cffc bytes 00eae297
~~~


<a id="compare-d324486508c4098d14d93e1e7bfc759d"></a>

### [`00b7cf38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf38.md) → [`00b7d000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d000.md) _ZNSt6__ndk17promiseIvE9set_valueEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb600.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cf58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf38.md#insn-00b7cf58)
- 新版 [`00b7d020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d000.md#insn-00b7d020)

~~~diff
- 00b7cf58 ["INT_ADD", "register:40f0:8", ["const:b7cf58:8", "const:4:8"]]
- 00b7cf58 ["CALL", null, ["callee:004377fc:8"]]
+ 00b7d020 ["INT_ADD", "register:40f0:8", ["const:b7d020:8", "const:4:8"]]
+ 00b7d020 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cf58 bytes 29eae297
+ 00b7d020 bytes f7e9e297
~~~


<a id="compare-693eea7a613675d9a4aed5277bea20d4"></a>

### [`00b7cfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfe0.md) → [`00b7d0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md) [`00be1140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md) [`00be11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfe0.md#insn-00b7cffc) · [`00b7d008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfe0.md#insn-00b7d008) · [`00b7d010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfe0.md#insn-00b7d010)
- 新版 [`00b7d0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0c4) · [`00b7d0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0d0) · [`00b7d0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d0a8.md#insn-00b7d0d8)

~~~diff
- 00b7cffc ["INT_ADD", "register:40f0:8", ["const:b7cffc:8", "const:4:8"]]
- 00b7cffc ["CALL", null, ["callee:00bdb610:8"]]
+ 00b7d0c4 ["INT_ADD", "register:40f0:8", ["const:b7d0c4:8", "const:4:8"]]
+ 00b7d0c4 ["CALL", null, ["callee:00bdb610:8"]]
- 00b7cffc bytes 59790194
+ 00b7d0c4 bytes 53790194
- 00b7d008 ["INT_ADD", "register:40f0:8", ["const:b7d008:8", "const:4:8"]]
- 00b7d008 ["CALL", null, ["callee:00be11f0:8"]]
+ 00b7d0d0 ["INT_ADD", "register:40f0:8", ["const:b7d0d0:8", "const:4:8"]]
+ 00b7d0d0 ["CALL", null, ["callee:00be11f0:8"]]
- 00b7d008 bytes 4e900194
+ 00b7d0d0 bytes 48900194
- 00b7d010 ["INT_ADD", "register:40f0:8", ["const:b7d010:8", "const:4:8"]]
- 00b7d010 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b7d0d8 ["INT_ADD", "register:40f0:8", ["const:b7d0d8:8", "const:4:8"]]
+ 00b7d0d8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b7d010 bytes e4780194
+ 00b7d0d8 bytes de780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fa9a4cc667b5f123b7aaea54951a90"></a>

### [`00b7d040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d040.md) → [`00b7d108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d108.md) _ZNSt6__ndk113shared_futureIvED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d040.md#insn-00b7d060)
- 新版 [`00b7d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d108.md#insn-00b7d128)

~~~diff
- 00b7d060 ["INT_ADD", "register:40f0:8", ["const:b7d060:8", "const:4:8"]]
- 00b7d060 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b7d128 ["INT_ADD", "register:40f0:8", ["const:b7d128:8", "const:4:8"]]
+ 00b7d128 ["CALL", null, ["callee:00bd6e50:8"]]
- 00b7d060 bytes 4c670194
+ 00b7d128 bytes 4a670194
~~~


