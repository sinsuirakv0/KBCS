# v15.7.2 → v15.7.3 · 要調査の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-c113b9e3c33fdca1daf9e0c5c73d0f85"></a>

### [`00b00fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md) → [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) FUN_00b010a8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00b001dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b001dc.md) [`00b080b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md) [`00b59a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59a5c.md) [`00b59c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b59/00b59c20.md) [`00b5a9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a9a0.md) · 呼出先 1件 [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 6件 [`00b002a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002a4.md) [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) [`00b59b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59b24.md) [`00b59ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59ce8.md) [`00b5aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md#insn-00b00fe8)
- 新版 `00b010b0`（命令位置の公開資料なし）

~~~diff
- 00b00fe8 ["INT_ADD", "register:40f0:8", ["const:b00fe8:8", "const:4:8"]]
- 00b00fe8 ["CALL", null, ["callee:00bde270:8"]]
+ 00b010b0 ["INT_ADD", "register:40f0:8", ["const:b010b0:8", "const:4:8"]]
+ 00b010b0 ["CALL", null, ["callee:00bde270:8"]]
- 00b00fe8 bytes 76740394
+ 00b010b0 bytes 70740394
~~~


<a id="compare-9669421e3754a8eb5ccdf35c00d3089a"></a>

### [`00b011d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b011d4.md) → [`00b0129c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md) FUN_00b0129c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00afea18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md) · 呼出先 4件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md) · 呼出先 4件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b011e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b011d4.md#insn-00b011e8) · [`00b01200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b011d4.md#insn-00b01200) · [`00b01214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b011d4.md#insn-00b01214)
- 新版 `00b012b0`（命令位置の公開資料なし） · `00b012c8`（命令位置の公開資料なし） · `00b012dc`（命令位置の公開資料なし）

~~~diff
- 00b011e8 ["INT_ADD", "register:40f0:8", ["const:b011e8:8", "const:4:8"]]
- 00b011e8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b012b0 ["INT_ADD", "register:40f0:8", ["const:b012b0:8", "const:4:8"]]
+ 00b012b0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b011e8 bytes 4e720394
+ 00b012b0 bytes 48720394
- 00b01200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b01200 ["INT_ADD", "register:40f0:8", ["const:b01200:8", "const:4:8"]]
- 00b01200 ["CALLIND", null, ["register:0:8"]]
+ 00b012c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b012c8 ["INT_ADD", "register:40f0:8", ["const:b012c8:8", "const:4:8"]]
+ 00b012c8 ["CALLIND", null, ["register:0:8"]]
- 00b01200 bytes 00013fd6
+ 00b012c8 bytes 00013fd6
- 00b01214 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b01214 ["INT_ADD", "register:40f0:8", ["const:b01214:8", "const:4:8"]]
- 00b01214 ["CALLIND", null, ["register:0:8"]]
+ 00b012dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b012dc ["INT_ADD", "register:40f0:8", ["const:b012dc:8", "const:4:8"]]
+ 00b012dc ["CALLIND", null, ["register:0:8"]]
- 00b01214 bytes 00013fd6
+ 00b012dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f141d9af4f7057a74e42f5c20f7d1c1"></a>

### [`00b017e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b017e4.md) → [`00b018ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b018ac.md) _ZN8firebase17ModuleInitializer20InitializeLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b017e4.md#insn-00b01804) · [`00b01810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b017e4.md#insn-00b01810) · [`00b0181c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b017e4.md#insn-00b0181c)
- 新版 `00b018cc`（命令位置の公開資料なし） · `00b018d8`（命令位置の公開資料なし） · `00b018e4`（命令位置の公開資料なし）

~~~diff
- 00b01804 ["INT_ADD", "register:40f0:8", ["const:b01804:8", "const:4:8"]]
- 00b01804 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b018cc ["INT_ADD", "register:40f0:8", ["const:b018cc:8", "const:4:8"]]
+ 00b018cc ["CALL", null, ["callee:00bddbd0:8"]]
- 00b01804 bytes c7700394
+ 00b018cc bytes c1700394
- 00b01810 ["INT_ADD", "register:40f0:8", ["const:b01810:8", "const:4:8"]]
- 00b01810 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b018d8 ["INT_ADD", "register:40f0:8", ["const:b018d8:8", "const:4:8"]]
+ 00b018d8 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b01810 bytes c8700394
+ 00b018d8 bytes c2700394
- 00b0181c ["INT_ADD", "register:40f0:8", ["const:b0181c:8", "const:4:8"]]
- 00b0181c ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b018e4 ["INT_ADD", "register:40f0:8", ["const:b018e4:8", "const:4:8"]]
+ 00b018e4 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b0181c bytes 3d710394
+ 00b018e4 bytes 37710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41984aff4515a5a02cec3399c344580d"></a>

### [`00b02404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02404.md) → [`00b024cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b024cc.md) _ZN8firebase16StaticFutureData13CreateNewDataEPKvi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddce0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02404.md#insn-00b02418) · [`00b02424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02404.md#insn-00b02424)
- 新版 `00b024e0`（命令位置の公開資料なし） · `00b024ec`（命令位置の公開資料なし）

~~~diff
- 00b02418 ["INT_ADD", "register:40f0:8", ["const:b02418:8", "const:4:8"]]
- 00b02418 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b024e0 ["INT_ADD", "register:40f0:8", ["const:b024e0:8", "const:4:8"]]
+ 00b024e0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b02418 bytes ca620394
+ 00b024e0 bytes c4620394
- 00b02424 ["INT_ADD", "register:40f0:8", ["const:b02424:8", "const:4:8"]]
- 00b02424 ["CALL", null, ["callee:00bddd90:8"]]
+ 00b024ec ["INT_ADD", "register:40f0:8", ["const:b024ec:8", "const:4:8"]]
+ 00b024ec ["CALL", null, ["callee:00bddd90:8"]]
- 00b02424 bytes 2f6e0394
+ 00b024ec bytes 296e0394
~~~


<a id="compare-73656ba0a0453f12f82489858bad3c5b"></a>

### [`00b028d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b028d0.md) → [`00b02998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02998.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee00.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdeeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeeb0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b028d0.md#insn-00b02934) · [`00b02940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b028d0.md#insn-00b02940) · [`00b0296c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b028d0.md#insn-00b0296c)
- 新版 `00b029fc`（命令位置の公開資料なし） · `00b02a08`（命令位置の公開資料なし） · `00b02a34`（命令位置の公開資料なし）

~~~diff
- 00b02934 ["INT_ADD", "register:40f0:8", ["const:b02934:8", "const:4:8"]]
- 00b02934 ["CALL", null, ["callee:00bde270:8"]]
+ 00b029fc ["INT_ADD", "register:40f0:8", ["const:b029fc:8", "const:4:8"]]
+ 00b029fc ["CALL", null, ["callee:00bde270:8"]]
- 00b02934 bytes 236e0394
+ 00b029fc bytes 1d6e0394
- 00b02940 ["INT_ADD", "register:40f0:8", ["const:b02940:8", "const:4:8"]]
- 00b02940 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b02a08 ["INT_ADD", "register:40f0:8", ["const:b02a08:8", "const:4:8"]]
+ 00b02a08 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b02940 bytes 80610394
+ 00b02a08 bytes 7a610394
- 00b0296c ["INT_ADD", "register:40f0:8", ["const:b0296c:8", "const:4:8"]]
- 00b0296c ["CALL", null, ["callee:00bdb160:8"]]
+ 00b02a34 ["INT_ADD", "register:40f0:8", ["const:b02a34:8", "const:4:8"]]
+ 00b02a34 ["CALL", null, ["callee:00bdb160:8"]]
- 00b0296c bytes d1610394
+ 00b02a34 bytes cb610394
~~~


<a id="compare-6015b9eb4182de44c0bbc1c6595b535f"></a>

### [`00b029b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b029b8.md) → [`00b02a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02a80.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdedd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdedd0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdedd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdedd0.md)
- 新版 呼出元 1件 [`00bdee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b029d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b029b8.md#insn-00b029d4) · [`00b029e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b029b8.md#insn-00b029e0) · [`00b029f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b029b8.md#insn-00b029f0)
- 新版 `00b02a9c`（命令位置の公開資料なし） · `00b02aa8`（命令位置の公開資料なし） · `00b02ab8`（命令位置の公開資料なし）

~~~diff
- 00b029d4 ["INT_ADD", "register:40f0:8", ["const:b029d4:8", "const:4:8"]]
- 00b029d4 ["CALL", null, ["callee:00bdee80:8"]]
+ 00b02a9c ["INT_ADD", "register:40f0:8", ["const:b02a9c:8", "const:4:8"]]
+ 00b02a9c ["CALL", null, ["callee:00bdee80:8"]]
- 00b029d4 bytes ff700394
+ 00b02a9c bytes f9700394
- 00b029e0 ["INT_ADD", "register:40f0:8", ["const:b029e0:8", "const:4:8"]]
- 00b029e0 ["CALL", null, ["callee:00bdee80:8"]]
+ 00b02aa8 ["INT_ADD", "register:40f0:8", ["const:b02aa8:8", "const:4:8"]]
+ 00b02aa8 ["CALL", null, ["callee:00bdee80:8"]]
- 00b029e0 bytes fc700394
+ 00b02aa8 bytes f6700394
- 00b029f0 ["INT_ADD", "register:40f0:8", ["const:b029f0:8", "const:4:8"]]
- 00b029f0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b02ab8 ["INT_ADD", "register:40f0:8", ["const:b02ab8:8", "const:4:8"]]
+ 00b02ab8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b029f0 bytes 5c610394
+ 00b02ab8 bytes 56610394
~~~


<a id="compare-590d46aa211f42b09dade2f94de2ec8f"></a>

### [`00b02a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02a08.md) → [`00b02ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02ad0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdedc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdedc0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdee70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee70.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02a08.md#insn-00b02aa4) · [`00b02ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02a08.md#insn-00b02ae4)
- 新版 `00b02b6c`（命令位置の公開資料なし） · `00b02bac`（命令位置の公開資料なし）

~~~diff
- 00b02aa4 ["INT_ADD", "register:40f0:8", ["const:b02aa4:8", "const:4:8"]]
- 00b02aa4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02b6c ["INT_ADD", "register:40f0:8", ["const:b02b6c:8", "const:4:8"]]
+ 00b02b6c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02aa4 bytes 97610394
+ 00b02b6c bytes 91610394
- 00b02ae4 ["INT_ADD", "register:40f0:8", ["const:b02ae4:8", "const:4:8"]]
- 00b02ae4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02bac ["INT_ADD", "register:40f0:8", ["const:b02bac:8", "const:4:8"]]
+ 00b02bac ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02ae4 bytes 87610394
+ 00b02bac bytes 81610394
~~~


<a id="compare-0fde03a16a7768072d0e8d56958b2e52"></a>

### [`00b02b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02b28.md) → [`00b02bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02bf0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdedf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdedf0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdeea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeea0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02b28.md#insn-00b02bc0) · [`00b02c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02b28.md#insn-00b02c08)
- 新版 `00b02c88`（命令位置の公開資料なし） · `00b02cd0`（命令位置の公開資料なし）

~~~diff
- 00b02bc0 ["INT_ADD", "register:40f0:8", ["const:b02bc0:8", "const:4:8"]]
- 00b02bc0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02c88 ["INT_ADD", "register:40f0:8", ["const:b02c88:8", "const:4:8"]]
+ 00b02c88 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02bc0 bytes 50610394
+ 00b02c88 bytes 4a610394
- 00b02c08 ["INT_ADD", "register:40f0:8", ["const:b02c08:8", "const:4:8"]]
- 00b02c08 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02cd0 ["INT_ADD", "register:40f0:8", ["const:b02cd0:8", "const:4:8"]]
+ 00b02cd0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02c08 bytes 3e610394
+ 00b02cd0 bytes 38610394
~~~


<a id="compare-d6571b2d74e96215280178da46623976"></a>

### [`00b02c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02c3c.md) → [`00b02d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02d04.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdede0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdede0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdee90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02c3c.md#insn-00b02cd8) · [`00b02d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02c3c.md#insn-00b02d18)
- 新版 `00b02da0`（命令位置の公開資料なし） · `00b02de0`（命令位置の公開資料なし）

~~~diff
- 00b02cd8 ["INT_ADD", "register:40f0:8", ["const:b02cd8:8", "const:4:8"]]
- 00b02cd8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02da0 ["INT_ADD", "register:40f0:8", ["const:b02da0:8", "const:4:8"]]
+ 00b02da0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02cd8 bytes 0a610394
+ 00b02da0 bytes 04610394
- 00b02d18 ["INT_ADD", "register:40f0:8", ["const:b02d18:8", "const:4:8"]]
- 00b02d18 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b02de0 ["INT_ADD", "register:40f0:8", ["const:b02de0:8", "const:4:8"]]
+ 00b02de0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02d18 bytes fa600394
+ 00b02de0 bytes f4600394
~~~


<a id="compare-a478ba3206820080ee283ea0366ad7dc"></a>

### [`00b04768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04768.md) → [`00b04830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md) FUN_00b04830

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b045c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b045c4.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1d0.md)
- 新版 呼出元 1件 [`00b0468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b047d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04768.md#insn-00b047d8) · [`00b047fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04768.md#insn-00b047fc)
- 新版 `00b048a0`（命令位置の公開資料なし） · `00b048c4`（命令位置の公開資料なし）

~~~diff
- 00b047d8 ["INT_ADD", "register:40f0:8", ["const:b047d8:8", "const:4:8"]]
- 00b047d8 ["CALL", null, ["callee:00bde280:8"]]
+ 00b048a0 ["INT_ADD", "register:40f0:8", ["const:b048a0:8", "const:4:8"]]
+ 00b048a0 ["CALL", null, ["callee:00bde280:8"]]
- 00b047d8 bytes 7e660394
+ 00b048a0 bytes 78660394
- 00b047fc ["INT_ADD", "register:40f0:8", ["const:b047fc:8", "const:4:8"]]
- 00b047fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b048c4 ["INT_ADD", "register:40f0:8", ["const:b048c4:8", "const:4:8"]]
+ 00b048c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b047fc bytes e5590394
+ 00b048c4 bytes df590394
~~~


<a id="compare-42e510113b7f842d7d7e375923f2cdb9"></a>

### [`00b05190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05190.md) → [`00b05258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05258.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md)
- 新版 呼出元 1件 [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b051ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05190.md#insn-00b051ac) · [`00b051b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05190.md#insn-00b051b8) · [`00b051c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05190.md#insn-00b051c8)
- 新版 `00b05274`（命令位置の公開資料なし） · `00b05280`（命令位置の公開資料なし） · `00b05290`（命令位置の公開資料なし）

~~~diff
- 00b051ac ["INT_ADD", "register:40f0:8", ["const:b051ac:8", "const:4:8"]]
- 00b051ac ["CALL", null, ["callee:00bdef20:8"]]
+ 00b05274 ["INT_ADD", "register:40f0:8", ["const:b05274:8", "const:4:8"]]
+ 00b05274 ["CALL", null, ["callee:00bdef20:8"]]
- 00b051ac bytes 31670394
+ 00b05274 bytes 2b670394
- 00b051b8 ["INT_ADD", "register:40f0:8", ["const:b051b8:8", "const:4:8"]]
- 00b051b8 ["CALL", null, ["callee:00bdef20:8"]]
+ 00b05280 ["INT_ADD", "register:40f0:8", ["const:b05280:8", "const:4:8"]]
+ 00b05280 ["CALL", null, ["callee:00bdef20:8"]]
- 00b051b8 bytes 2e670394
+ 00b05280 bytes 28670394
- 00b051c8 ["INT_ADD", "register:40f0:8", ["const:b051c8:8", "const:4:8"]]
- 00b051c8 ["CALL", null, ["callee:00bdd990:8"]]
+ 00b05290 ["INT_ADD", "register:40f0:8", ["const:b05290:8", "const:4:8"]]
+ 00b05290 ["CALL", null, ["callee:00bdd990:8"]]
- 00b051c8 bytes c6610394
+ 00b05290 bytes c0610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbd7ab9a2cad8be64db17205cd1af7d2"></a>

### [`00b051ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b051ec.md) → [`00b052b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b052b4.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE15__emp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdee60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee60.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9a0.md) [`00bde620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde620.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md)
- 新版 呼出元 1件 [`00bdef10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef10.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b051ec.md#insn-00b05208) · [`00b05220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b051ec.md#insn-00b05220) · [`00b05230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b051ec.md#insn-00b05230)
- 新版 `00b052d0`（命令位置の公開資料なし） · `00b052e8`（命令位置の公開資料なし） · `00b052f8`（命令位置の公開資料なし）

~~~diff
- 00b05208 ["INT_ADD", "register:40f0:8", ["const:b05208:8", "const:4:8"]]
- 00b05208 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b052d0 ["INT_ADD", "register:40f0:8", ["const:b052d0:8", "const:4:8"]]
+ 00b052d0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b05208 bytes 4e570394
+ 00b052d0 bytes 48570394
- 00b05220 ["INT_ADD", "register:40f0:8", ["const:b05220:8", "const:4:8"]]
- 00b05220 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b052e8 ["INT_ADD", "register:40f0:8", ["const:b052e8:8", "const:4:8"]]
+ 00b052e8 ["CALL", null, ["callee:00bdda50:8"]]
- 00b05220 bytes e0610394
+ 00b052e8 bytes da610394
- 00b05230 ["INT_ADD", "register:40f0:8", ["const:b05230:8", "const:4:8"]]
- 00b05230 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b052f8 ["INT_ADD", "register:40f0:8", ["const:b052f8:8", "const:4:8"]]
+ 00b052f8 ["CALL", null, ["callee:00bdda50:8"]]
- 00b05230 bytes dc610394
+ 00b052f8 bytes d6610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11cd121036891892544e7f35902fab89"></a>

### [`00b06a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06a6c.md) → [`00b06b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde840.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00847/0084795c.md) [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde240.md) [`00bde440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde440.md)
- 新版 呼出元 1件 [`00bde8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8f0.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2f0.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06a6c.md#insn-00b06a80) · [`00b06a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06a6c.md#insn-00b06a8c) · [`00b06aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06a6c.md#insn-00b06aa0)
- 新版 `00b06b48`（命令位置の公開資料なし） · `00b06b54`（命令位置の公開資料なし） · `00b06b68`（命令位置の公開資料なし）

~~~diff
- 00b06a80 ["INT_ADD", "register:40f0:8", ["const:b06a80:8", "const:4:8"]]
- 00b06a80 ["CALL", null, ["callee:00bde890:8"]]
+ 00b06b48 ["INT_ADD", "register:40f0:8", ["const:b06b48:8", "const:4:8"]]
+ 00b06b48 ["CALL", null, ["callee:00bde890:8"]]
- 00b06a80 bytes 585f0394
+ 00b06b48 bytes 525f0394
- 00b06a8c ["INT_ADD", "register:40f0:8", ["const:b06a8c:8", "const:4:8"]]
- 00b06a8c ["CALL", null, ["callee:00bde4f0:8"]]
+ 00b06b54 ["INT_ADD", "register:40f0:8", ["const:b06b54:8", "const:4:8"]]
+ 00b06b54 ["CALL", null, ["callee:00bde4f0:8"]]
- 00b06a8c bytes 6d5e0394
+ 00b06b54 bytes 675e0394
- 00b06aa0 ["INT_ADD", "register:40f0:8", ["const:b06aa0:8", "const:4:8"]]
- 00b06aa0 ["CALL", null, ["callee:00bde2f0:8"]]
+ 00b06b68 ["INT_ADD", "register:40f0:8", ["const:b06b68:8", "const:4:8"]]
+ 00b06b68 ["CALL", null, ["callee:00bde2f0:8"]]
- 00b06aa0 bytes e85d0394
+ 00b06b68 bytes e25d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3314527f72c46c60429d1b583c672622"></a>

### [`00b080b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md) → [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b00fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md) [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md) [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b080c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md#insn-00b080c8) · [`00b080e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md#insn-00b080e0) · [`00b08100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md#insn-00b08100)
- 新版 `00b08190`（命令位置の公開資料なし） · `00b081a8`（命令位置の公開資料なし） · `00b081c8`（命令位置の公開資料なし）

~~~diff
- 00b080c8 ["INT_ADD", "register:40f0:8", ["const:b080c8:8", "const:4:8"]]
- 00b080c8 ["CALL", null, ["callee:00b06390:8"]]
+ 00b08190 ["INT_ADD", "register:40f0:8", ["const:b08190:8", "const:4:8"]]
+ 00b08190 ["CALL", null, ["callee:00b06390:8"]]
- 00b080c8 bytes 80f8ff97
+ 00b08190 bytes 80f8ff97
- 00b080e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b080e0 ["INT_ADD", "register:40f0:8", ["const:b080e0:8", "const:4:8"]]
- 00b080e0 ["CALLIND", null, ["register:0:8"]]
+ 00b081a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b081a8 ["INT_ADD", "register:40f0:8", ["const:b081a8:8", "const:4:8"]]
+ 00b081a8 ["CALLIND", null, ["register:0:8"]]
- 00b080e0 bytes 00013fd6
+ 00b081a8 bytes 00013fd6
- 00b08100 ["INT_ADD", "register:40f0:8", ["const:b08100:8", "const:4:8"]]
- 00b08100 ["CALL", null, ["callee:00b010a8:8"]]
+ 00b081c8 ["INT_ADD", "register:40f0:8", ["const:b081c8:8", "const:4:8"]]
+ 00b081c8 ["CALL", null, ["callee:00b010a8:8"]]
- 00b08100 bytes b8e3ff97
+ 00b081c8 bytes b8e3ff97
~~~


<a id="compare-29e670da72a88890e003cbcab97d5eba"></a>

### [`00b0aadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0aadc.md) → [`00b0aba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde900.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md)
- 新版 呼出元 1件 [`00bde9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9b0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ab0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0aadc.md#insn-00b0ab0c) · [`00b0ab18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0aadc.md#insn-00b0ab18) · [`00b0ab2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0aadc.md#insn-00b0ab2c)
- 新版 `00b0abd4`（命令位置の公開資料なし） · `00b0abe0`（命令位置の公開資料なし） · `00b0abf4`（命令位置の公開資料なし）

~~~diff
- 00b0ab0c ["INT_ADD", "register:40f0:8", ["const:b0ab0c:8", "const:4:8"]]
- 00b0ab0c ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b0abd4 ["INT_ADD", "register:40f0:8", ["const:b0abd4:8", "const:4:8"]]
+ 00b0abd4 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b0ab0c bytes c94e0394
+ 00b0abd4 bytes c34e0394
- 00b0ab18 ["INT_ADD", "register:40f0:8", ["const:b0ab18:8", "const:4:8"]]
- 00b0ab18 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b0abe0 ["INT_ADD", "register:40f0:8", ["const:b0abe0:8", "const:4:8"]]
+ 00b0abe0 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b0ab18 bytes c64e0394
+ 00b0abe0 bytes c04e0394
- 00b0ab2c ["INT_ADD", "register:40f0:8", ["const:b0ab2c:8", "const:4:8"]]
- 00b0ab2c ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b0abf4 ["INT_ADD", "register:40f0:8", ["const:b0abf4:8", "const:4:8"]]
+ 00b0abf4 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b0ab2c bytes c14e0394
+ 00b0abf4 bytes bb4e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41438a4e309629561cfea0266cec2a12"></a>

### [`00b0ac78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0ac78.md) → [`00b0ad40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0ad40.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb20.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebd0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0acdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0ac78.md#insn-00b0acdc) · [`00b0ace8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0ac78.md#insn-00b0ace8) · [`00b0ad14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0ac78.md#insn-00b0ad14)
- 新版 `00b0ada4`（命令位置の公開資料なし） · `00b0adb0`（命令位置の公開資料なし） · `00b0addc`（命令位置の公開資料なし）

~~~diff
- 00b0acdc ["INT_ADD", "register:40f0:8", ["const:b0acdc:8", "const:4:8"]]
- 00b0acdc ["CALL", null, ["callee:00bde270:8"]]
+ 00b0ada4 ["INT_ADD", "register:40f0:8", ["const:b0ada4:8", "const:4:8"]]
+ 00b0ada4 ["CALL", null, ["callee:00bde270:8"]]
- 00b0acdc bytes 394d0394
+ 00b0ada4 bytes 334d0394
- 00b0ace8 ["INT_ADD", "register:40f0:8", ["const:b0ace8:8", "const:4:8"]]
- 00b0ace8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b0adb0 ["INT_ADD", "register:40f0:8", ["const:b0adb0:8", "const:4:8"]]
+ 00b0adb0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b0ace8 bytes 96400394
+ 00b0adb0 bytes 90400394
- 00b0ad14 ["INT_ADD", "register:40f0:8", ["const:b0ad14:8", "const:4:8"]]
- 00b0ad14 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b0addc ["INT_ADD", "register:40f0:8", ["const:b0addc:8", "const:4:8"]]
+ 00b0addc ["CALL", null, ["callee:00bdb160:8"]]
- 00b0ad14 bytes e7400394
+ 00b0addc bytes e1400394
~~~


<a id="compare-67ac2def3fd5b16bfdf84fa0ef26fbfb"></a>

### [`00b0d054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d054.md) → [`00b0d11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d11c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea70.md) · 呼出先 3件 [`0051d9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d9f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdea70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea70.md)
- 新版 呼出元 1件 [`00bdeb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb20.md) · 呼出先 3件 [`0051d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d054.md#insn-00b0d070) · [`00b0d07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d054.md#insn-00b0d07c) · [`00b0d088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d054.md#insn-00b0d088)
- 新版 `00b0d138`（命令位置の公開資料なし） · `00b0d144`（命令位置の公開資料なし） · `00b0d150`（命令位置の公開資料なし）

~~~diff
- 00b0d070 ["INT_ADD", "register:40f0:8", ["const:b0d070:8", "const:4:8"]]
- 00b0d070 ["CALL", null, ["callee:00bdeb20:8"]]
+ 00b0d138 ["INT_ADD", "register:40f0:8", ["const:b0d138:8", "const:4:8"]]
+ 00b0d138 ["CALL", null, ["callee:00bdeb20:8"]]
- 00b0d070 bytes 80460394
+ 00b0d138 bytes 7a460394
- 00b0d07c ["INT_ADD", "register:40f0:8", ["const:b0d07c:8", "const:4:8"]]
- 00b0d07c ["CALL", null, ["callee:00bdeb20:8"]]
+ 00b0d144 ["INT_ADD", "register:40f0:8", ["const:b0d144:8", "const:4:8"]]
+ 00b0d144 ["CALL", null, ["callee:00bdeb20:8"]]
- 00b0d07c bytes 7d460394
+ 00b0d144 bytes 77460394
- 00b0d088 ["INT_ADD", "register:40f0:8", ["const:b0d088:8", "const:4:8"]]
- 00b0d088 ["CALL", null, ["callee:0051d9f8:8"]]
+ 00b0d150 ["INT_ADD", "register:40f0:8", ["const:b0d150:8", "const:4:8"]]
+ 00b0d150 ["CALL", null, ["callee:0051d9f8:8"]]
- 00b0d088 bytes 5c42e897
+ 00b0d150 bytes 2a42e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09aee377a99c02b1f0bdce8b7e119af7"></a>

### [`00b0d0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0b0.md) → [`00b0d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d178.md) _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb00.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb00.md)
- 新版 呼出元 1件 [`00bdebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebb0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdebb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0b0.md#insn-00b0d0cc) · [`00b0d0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0b0.md#insn-00b0d0d8)
- 新版 `00b0d194`（命令位置の公開資料なし） · `00b0d1a0`（命令位置の公開資料なし）

~~~diff
- 00b0d0cc ["INT_ADD", "register:40f0:8", ["const:b0d0cc:8", "const:4:8"]]
- 00b0d0cc ["CALL", null, ["callee:00bdebb0:8"]]
+ 00b0d194 ["INT_ADD", "register:40f0:8", ["const:b0d194:8", "const:4:8"]]
+ 00b0d194 ["CALL", null, ["callee:00bdebb0:8"]]
- 00b0d0cc bytes 8d460394
+ 00b0d194 bytes 87460394
- 00b0d0d8 ["INT_ADD", "register:40f0:8", ["const:b0d0d8:8", "const:4:8"]]
- 00b0d0d8 ["CALL", null, ["callee:00bdebb0:8"]]
+ 00b0d1a0 ["INT_ADD", "register:40f0:8", ["const:b0d1a0:8", "const:4:8"]]
+ 00b0d1a0 ["CALL", null, ["callee:00bdebb0:8"]]
- 00b0d0d8 bytes 8a460394
+ 00b0d1a0 bytes 84460394
~~~


<a id="compare-6008db069603b1d4b82fa732912e2e99"></a>

### [`00b0d0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0f0.md) → [`00b0d1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1b8.md) _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb10.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb10.md)
- 新版 呼出元 1件 [`00bdebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebc0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdebc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0f0.md#insn-00b0d10c) · [`00b0d118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d0f0.md#insn-00b0d118)
- 新版 `00b0d1d4`（命令位置の公開資料なし） · `00b0d1e0`（命令位置の公開資料なし）

~~~diff
- 00b0d10c ["INT_ADD", "register:40f0:8", ["const:b0d10c:8", "const:4:8"]]
- 00b0d10c ["CALL", null, ["callee:00bdebc0:8"]]
+ 00b0d1d4 ["INT_ADD", "register:40f0:8", ["const:b0d1d4:8", "const:4:8"]]
+ 00b0d1d4 ["CALL", null, ["callee:00bdebc0:8"]]
- 00b0d10c bytes 81460394
+ 00b0d1d4 bytes 7b460394
- 00b0d118 ["INT_ADD", "register:40f0:8", ["const:b0d118:8", "const:4:8"]]
- 00b0d118 ["CALL", null, ["callee:00bdebc0:8"]]
+ 00b0d1e0 ["INT_ADD", "register:40f0:8", ["const:b0d1e0:8", "const:4:8"]]
+ 00b0d1e0 ["CALL", null, ["callee:00bdebc0:8"]]
- 00b0d118 bytes 7e460394
+ 00b0d1e0 bytes 78460394
~~~


<a id="compare-72d384f389dc5674d45b1ae17de57cc1"></a>

### [`00b0d130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d130.md) → [`00b0d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d1f8.md) _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_17FlatBufferBuilder19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea60.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdea60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea60.md)
- 新版 呼出元 1件 [`00bdeb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb10.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d130.md#insn-00b0d14c) · [`00b0d158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d130.md#insn-00b0d158)
- 新版 `00b0d214`（命令位置の公開資料なし） · `00b0d220`（命令位置の公開資料なし）

~~~diff
- 00b0d14c ["INT_ADD", "register:40f0:8", ["const:b0d14c:8", "const:4:8"]]
- 00b0d14c ["CALL", null, ["callee:00bdeb10:8"]]
+ 00b0d214 ["INT_ADD", "register:40f0:8", ["const:b0d214:8", "const:4:8"]]
+ 00b0d214 ["CALL", null, ["callee:00bdeb10:8"]]
- 00b0d14c bytes 45460394
+ 00b0d214 bytes 3f460394
- 00b0d158 ["INT_ADD", "register:40f0:8", ["const:b0d158:8", "const:4:8"]]
- 00b0d158 ["CALL", null, ["callee:00bdeb10:8"]]
+ 00b0d220 ["INT_ADD", "register:40f0:8", ["const:b0d220:8", "const:4:8"]]
+ 00b0d220 ["CALL", null, ["callee:00bdeb10:8"]]
- 00b0d158 bytes 42460394
+ 00b0d220 bytes 3c460394
~~~


<a id="compare-51208a2d6601cb2204696fc812f8f3c6"></a>

### [`00b0d284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d284.md) → [`00b0d34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d34c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdead0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdead0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdead0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdead0.md)
- 新版 呼出元 1件 [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d284.md#insn-00b0d2a0) · [`00b0d2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d284.md#insn-00b0d2ac) · [`00b0d2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d284.md#insn-00b0d2bc)
- 新版 `00b0d368`（命令位置の公開資料なし） · `00b0d374`（命令位置の公開資料なし） · `00b0d384`（命令位置の公開資料なし）

~~~diff
- 00b0d2a0 ["INT_ADD", "register:40f0:8", ["const:b0d2a0:8", "const:4:8"]]
- 00b0d2a0 ["CALL", null, ["callee:00bdeb80:8"]]
+ 00b0d368 ["INT_ADD", "register:40f0:8", ["const:b0d368:8", "const:4:8"]]
+ 00b0d368 ["CALL", null, ["callee:00bdeb80:8"]]
- 00b0d2a0 bytes 0c460394
+ 00b0d368 bytes 06460394
- 00b0d2ac ["INT_ADD", "register:40f0:8", ["const:b0d2ac:8", "const:4:8"]]
- 00b0d2ac ["CALL", null, ["callee:00bdeb80:8"]]
+ 00b0d374 ["INT_ADD", "register:40f0:8", ["const:b0d374:8", "const:4:8"]]
+ 00b0d374 ["CALL", null, ["callee:00bdeb80:8"]]
- 00b0d2ac bytes 09460394
+ 00b0d374 bytes 03460394
- 00b0d2bc ["INT_ADD", "register:40f0:8", ["const:b0d2bc:8", "const:4:8"]]
- 00b0d2bc ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d384 ["INT_ADD", "register:40f0:8", ["const:b0d384:8", "const:4:8"]]
+ 00b0d384 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d2bc bytes 29370394
+ 00b0d384 bytes 23370394
~~~


<a id="compare-21c04a825ce992b8a66b5a50e41c1821"></a>

### [`00b0d324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d324.md) → [`00b0d3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d3ec.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdea80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea80.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdea80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea80.md)
- 新版 呼出元 1件 [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d324.md#insn-00b0d340) · [`00b0d34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d324.md#insn-00b0d34c) · [`00b0d35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d324.md#insn-00b0d35c)
- 新版 `00b0d408`（命令位置の公開資料なし） · `00b0d414`（命令位置の公開資料なし） · `00b0d424`（命令位置の公開資料なし）

~~~diff
- 00b0d340 ["INT_ADD", "register:40f0:8", ["const:b0d340:8", "const:4:8"]]
- 00b0d340 ["CALL", null, ["callee:00bdeb30:8"]]
+ 00b0d408 ["INT_ADD", "register:40f0:8", ["const:b0d408:8", "const:4:8"]]
+ 00b0d408 ["CALL", null, ["callee:00bdeb30:8"]]
- 00b0d340 bytes d0450394
+ 00b0d408 bytes ca450394
- 00b0d34c ["INT_ADD", "register:40f0:8", ["const:b0d34c:8", "const:4:8"]]
- 00b0d34c ["CALL", null, ["callee:00bdeb30:8"]]
+ 00b0d414 ["INT_ADD", "register:40f0:8", ["const:b0d414:8", "const:4:8"]]
+ 00b0d414 ["CALL", null, ["callee:00bdeb30:8"]]
- 00b0d34c bytes cd450394
+ 00b0d414 bytes c7450394
- 00b0d35c ["INT_ADD", "register:40f0:8", ["const:b0d35c:8", "const:4:8"]]
- 00b0d35c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d424 ["INT_ADD", "register:40f0:8", ["const:b0d424:8", "const:4:8"]]
+ 00b0d424 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d35c bytes 01370394
+ 00b0d424 bytes fb360394
~~~


<a id="compare-e92af5a7037ea6e3c6b5935824ff1fe5"></a>

### [`00b0d458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d458.md) → [`00b0d520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d520.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeac0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeac0.md)
- 新版 呼出元 1件 [`00bdeb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb70.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d458.md#insn-00b0d474) · [`00b0d480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d458.md#insn-00b0d480) · [`00b0d490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d458.md#insn-00b0d490)
- 新版 `00b0d53c`（命令位置の公開資料なし） · `00b0d548`（命令位置の公開資料なし） · `00b0d558`（命令位置の公開資料なし）

~~~diff
- 00b0d474 ["INT_ADD", "register:40f0:8", ["const:b0d474:8", "const:4:8"]]
- 00b0d474 ["CALL", null, ["callee:00bdeb70:8"]]
+ 00b0d53c ["INT_ADD", "register:40f0:8", ["const:b0d53c:8", "const:4:8"]]
+ 00b0d53c ["CALL", null, ["callee:00bdeb70:8"]]
- 00b0d474 bytes 93450394
+ 00b0d53c bytes 8d450394
- 00b0d480 ["INT_ADD", "register:40f0:8", ["const:b0d480:8", "const:4:8"]]
- 00b0d480 ["CALL", null, ["callee:00bdeb70:8"]]
+ 00b0d548 ["INT_ADD", "register:40f0:8", ["const:b0d548:8", "const:4:8"]]
+ 00b0d548 ["CALL", null, ["callee:00bdeb70:8"]]
- 00b0d480 bytes 90450394
+ 00b0d548 bytes 8a450394
- 00b0d490 ["INT_ADD", "register:40f0:8", ["const:b0d490:8", "const:4:8"]]
- 00b0d490 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d558 ["INT_ADD", "register:40f0:8", ["const:b0d558:8", "const:4:8"]]
+ 00b0d558 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d490 bytes b4360394
+ 00b0d558 bytes ae360394
~~~


<a id="compare-016be8211a8037f175525c8560b06c54"></a>

### [`00b0d4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4a8.md) → [`00b0d570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d570.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeab0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeab0.md)
- 新版 呼出元 1件 [`00bdeb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb60.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4a8.md#insn-00b0d4c4) · [`00b0d4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4a8.md#insn-00b0d4d0) · [`00b0d4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4a8.md#insn-00b0d4e0)
- 新版 `00b0d58c`（命令位置の公開資料なし） · `00b0d598`（命令位置の公開資料なし） · `00b0d5a8`（命令位置の公開資料なし）

~~~diff
- 00b0d4c4 ["INT_ADD", "register:40f0:8", ["const:b0d4c4:8", "const:4:8"]]
- 00b0d4c4 ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b0d58c ["INT_ADD", "register:40f0:8", ["const:b0d58c:8", "const:4:8"]]
+ 00b0d58c ["CALL", null, ["callee:00bdeb60:8"]]
- 00b0d4c4 bytes 7b450394
+ 00b0d58c bytes 75450394
- 00b0d4d0 ["INT_ADD", "register:40f0:8", ["const:b0d4d0:8", "const:4:8"]]
- 00b0d4d0 ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b0d598 ["INT_ADD", "register:40f0:8", ["const:b0d598:8", "const:4:8"]]
+ 00b0d598 ["CALL", null, ["callee:00bdeb60:8"]]
- 00b0d4d0 bytes 78450394
+ 00b0d598 bytes 72450394
- 00b0d4e0 ["INT_ADD", "register:40f0:8", ["const:b0d4e0:8", "const:4:8"]]
- 00b0d4e0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d5a8 ["INT_ADD", "register:40f0:8", ["const:b0d5a8:8", "const:4:8"]]
+ 00b0d5a8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d4e0 bytes a0360394
+ 00b0d5a8 bytes 9a360394
~~~


<a id="compare-e0a078ad371547c30b2e4a0eed9f241d"></a>

### [`00b0d588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d588.md) → [`00b0d650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d650.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeae0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeae0.md)
- 新版 呼出元 1件 [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d588.md#insn-00b0d5a4) · [`00b0d5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d588.md#insn-00b0d5b0) · [`00b0d5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d588.md#insn-00b0d5c0)
- 新版 `00b0d66c`（命令位置の公開資料なし） · `00b0d678`（命令位置の公開資料なし） · `00b0d688`（命令位置の公開資料なし）

~~~diff
- 00b0d5a4 ["INT_ADD", "register:40f0:8", ["const:b0d5a4:8", "const:4:8"]]
- 00b0d5a4 ["CALL", null, ["callee:00bdeb90:8"]]
+ 00b0d66c ["INT_ADD", "register:40f0:8", ["const:b0d66c:8", "const:4:8"]]
+ 00b0d66c ["CALL", null, ["callee:00bdeb90:8"]]
- 00b0d5a4 bytes 4f450394
+ 00b0d66c bytes 49450394
- 00b0d5b0 ["INT_ADD", "register:40f0:8", ["const:b0d5b0:8", "const:4:8"]]
- 00b0d5b0 ["CALL", null, ["callee:00bdeb90:8"]]
+ 00b0d678 ["INT_ADD", "register:40f0:8", ["const:b0d678:8", "const:4:8"]]
+ 00b0d678 ["CALL", null, ["callee:00bdeb90:8"]]
- 00b0d5b0 bytes 4c450394
+ 00b0d678 bytes 46450394
- 00b0d5c0 ["INT_ADD", "register:40f0:8", ["const:b0d5c0:8", "const:4:8"]]
- 00b0d5c0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d688 ["INT_ADD", "register:40f0:8", ["const:b0d688:8", "const:4:8"]]
+ 00b0d688 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d5c0 bytes 68360394
+ 00b0d688 bytes 62360394
~~~


<a id="compare-275219afdc7d1078979ad51bc4447060"></a>

### [`00b0d5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d5d8.md) → [`00b0d6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6a0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdeaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeaf0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeaf0.md)
- 新版 呼出元 1件 [`00bdeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeba0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d5d8.md#insn-00b0d5f4) · [`00b0d600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d5d8.md#insn-00b0d600) · [`00b0d610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d5d8.md#insn-00b0d610)
- 新版 `00b0d6bc`（命令位置の公開資料なし） · `00b0d6c8`（命令位置の公開資料なし） · `00b0d6d8`（命令位置の公開資料なし）

~~~diff
- 00b0d5f4 ["INT_ADD", "register:40f0:8", ["const:b0d5f4:8", "const:4:8"]]
- 00b0d5f4 ["CALL", null, ["callee:00bdeba0:8"]]
+ 00b0d6bc ["INT_ADD", "register:40f0:8", ["const:b0d6bc:8", "const:4:8"]]
+ 00b0d6bc ["CALL", null, ["callee:00bdeba0:8"]]
- 00b0d5f4 bytes 3f450394
+ 00b0d6bc bytes 39450394
- 00b0d600 ["INT_ADD", "register:40f0:8", ["const:b0d600:8", "const:4:8"]]
- 00b0d600 ["CALL", null, ["callee:00bdeba0:8"]]
+ 00b0d6c8 ["INT_ADD", "register:40f0:8", ["const:b0d6c8:8", "const:4:8"]]
+ 00b0d6c8 ["CALL", null, ["callee:00bdeba0:8"]]
- 00b0d600 bytes 3c450394
+ 00b0d6c8 bytes 36450394
- 00b0d610 ["INT_ADD", "register:40f0:8", ["const:b0d610:8", "const:4:8"]]
- 00b0d610 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d6d8 ["INT_ADD", "register:40f0:8", ["const:b0d6d8:8", "const:4:8"]]
+ 00b0d6d8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d610 bytes 54360394
+ 00b0d6d8 bytes 4e360394
~~~


<a id="compare-37f725e33b34c8b8babab22021e9aa1e"></a>

### [`00b0ddcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0ddcc.md) → [`00b0de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0de94.md) _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdef90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef90.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdf040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf040.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0de40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0ddcc.md#insn-00b0de40) · [`00b0de64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0ddcc.md#insn-00b0de64)
- 新版 `00b0df08`（命令位置の公開資料なし） · `00b0df2c`（命令位置の公開資料なし）

~~~diff
- 00b0de40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0de40 ["INT_ADD", "register:40f0:8", ["const:b0de40:8", "const:4:8"]]
- 00b0de40 ["CALLIND", null, ["register:0:8"]]
+ 00b0df08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0df08 ["INT_ADD", "register:40f0:8", ["const:b0df08:8", "const:4:8"]]
+ 00b0df08 ["CALLIND", null, ["register:0:8"]]
- 00b0de40 bytes 00013fd6
+ 00b0df08 bytes 00013fd6
- 00b0de64 ["INT_ADD", "register:40f0:8", ["const:b0de64:8", "const:4:8"]]
- 00b0de64 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0df2c ["INT_ADD", "register:40f0:8", ["const:b0df2c:8", "const:4:8"]]
+ 00b0df2c ["CALL", null, ["callee:00bdb040:8"]]
- 00b0de64 bytes 4b340394
+ 00b0df2c bytes 45340394
~~~


<a id="compare-4448a6eb0f8898531230cb1953b0277a"></a>

### [`00b0edbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0edbc.md) → [`00b0ee84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdf8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0ede8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0edbc.md#insn-00b0ede8) · [`00b0edf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0edbc.md#insn-00b0edf4) · [`00b0ee04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0edbc.md#insn-00b0ee04)
- 新版 `00b0eeb0`（命令位置の公開資料なし） · `00b0eebc`（命令位置の公開資料なし） · `00b0eecc`（命令位置の公開資料なし）

~~~diff
- 00b0ede8 ["INT_ADD", "register:40f0:8", ["const:b0ede8:8", "const:4:8"]]
- 00b0ede8 ["CALL", null, ["callee:00bdb210:8"]]
+ 00b0eeb0 ["INT_ADD", "register:40f0:8", ["const:b0eeb0:8", "const:4:8"]]
+ 00b0eeb0 ["CALL", null, ["callee:00bdb210:8"]]
- 00b0ede8 bytes de300394
+ 00b0eeb0 bytes d8300394
- 00b0edf4 ["INT_ADD", "register:40f0:8", ["const:b0edf4:8", "const:4:8"]]
- 00b0edf4 ["CALL", null, ["callee:00bdf980:8"]]
+ 00b0eebc ["INT_ADD", "register:40f0:8", ["const:b0eebc:8", "const:4:8"]]
+ 00b0eebc ["CALL", null, ["callee:00bdf980:8"]]
- 00b0edf4 bytes b7420394
+ 00b0eebc bytes b1420394
- 00b0ee04 ["INT_ADD", "register:40f0:8", ["const:b0ee04:8", "const:4:8"]]
- 00b0ee04 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0eecc ["INT_ADD", "register:40f0:8", ["const:b0eecc:8", "const:4:8"]]
+ 00b0eecc ["CALL", null, ["callee:00bdb010:8"]]
- 00b0ee04 bytes 57300394
+ 00b0eecc bytes 51300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ccbb61ef3b86ae803d2fec0670abad"></a>

### [`00b10b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10b00.md) → [`00b10bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10bc8.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf950.md) · 呼出先 1件 [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`00bdfa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa00.md) · 呼出先 1件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b10bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10b00.md#insn-00b10bec) · [`00b10cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10b00.md#insn-00b10cb8)
- 新版 `00b10cb4`（命令位置の公開資料なし） · `00b10d80`（命令位置の公開資料なし）

~~~diff
- 00b10bec ["INT_ADD", "register:40f0:8", ["const:b10bec:8", "const:4:8"]]
- 00b10bec ["CALL", null, ["callee:00bdda40:8"]]
+ 00b10cb4 ["INT_ADD", "register:40f0:8", ["const:b10cb4:8", "const:4:8"]]
+ 00b10cb4 ["CALL", null, ["callee:00bdda40:8"]]
- 00b10bec bytes 69330394
+ 00b10cb4 bytes 63330394
- 00b10cb8 ["INT_ADD", "register:40f0:8", ["const:b10cb8:8", "const:4:8"]]
- 00b10cb8 ["CALL", null, ["callee:00bdda40:8"]]
+ 00b10d80 ["INT_ADD", "register:40f0:8", ["const:b10d80:8", "const:4:8"]]
+ 00b10d80 ["CALL", null, ["callee:00bdda40:8"]]
- 00b10cb8 bytes 36330394
+ 00b10d80 bytes 30330394
~~~


<a id="compare-b868efc3a3af254ceac2413f93b54c6b"></a>

### [`00b10d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10d0c.md) → [`00b10dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10dd4.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b10d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10d0c.md#insn-00b10d30) · [`00b10d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10d0c.md#insn-00b10d74) · [`00b10d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10d0c.md#insn-00b10d9c)
- 新版 `00b10df8`（命令位置の公開資料なし） · `00b10e3c`（命令位置の公開資料なし） · `00b10e64`（命令位置の公開資料なし）

~~~diff
- 00b10d30 ["INT_ADD", "register:40f0:8", ["const:b10d30:8", "const:4:8"]]
- 00b10d30 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b10df8 ["INT_ADD", "register:40f0:8", ["const:b10df8:8", "const:4:8"]]
+ 00b10df8 ["CALL", null, ["callee:00bdb140:8"]]
- 00b10d30 bytes d8280394
+ 00b10df8 bytes d2280394
- 00b10d74 ["INT_ADD", "register:40f0:8", ["const:b10d74:8", "const:4:8"]]
- 00b10d74 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b10e3c ["INT_ADD", "register:40f0:8", ["const:b10e3c:8", "const:4:8"]]
+ 00b10e3c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b10d74 bytes e3280394
+ 00b10e3c bytes dd280394
- 00b10d9c ["INT_ADD", "register:40f0:8", ["const:b10d9c:8", "const:4:8"]]
- 00b10d9c ["CALL", null, ["callee:00bde270:8"]]
+ 00b10e64 ["INT_ADD", "register:40f0:8", ["const:b10e64:8", "const:4:8"]]
+ 00b10e64 ["CALL", null, ["callee:00bde270:8"]]
- 00b10d9c bytes 09350394
+ 00b10e64 bytes 03350394
~~~


<a id="compare-68294413682a0f75d17027eb78557d5a"></a>

### [`00b11260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11260.md) → [`00b11328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11328.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdfb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb70.md) [`00bdfba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfba0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md) [`00bdfc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b112c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11260.md#insn-00b112c8) · [`00b112d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11260.md#insn-00b112d4) · [`00b112f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11260.md#insn-00b112f0)
- 新版 `00b11390`（命令位置の公開資料なし） · `00b1139c`（命令位置の公開資料なし） · `00b113b8`（命令位置の公開資料なし）

~~~diff
- 00b112c8 ["INT_ADD", "register:40f0:8", ["const:b112c8:8", "const:4:8"]]
- 00b112c8 ["CALL", null, ["callee:00bdfc20:8"]]
+ 00b11390 ["INT_ADD", "register:40f0:8", ["const:b11390:8", "const:4:8"]]
+ 00b11390 ["CALL", null, ["callee:00bdfc20:8"]]
- 00b112c8 bytes 2a3a0394
+ 00b11390 bytes 243a0394
- 00b112d4 ["INT_ADD", "register:40f0:8", ["const:b112d4:8", "const:4:8"]]
- 00b112d4 ["CALL", null, ["callee:00bdfc50:8"]]
+ 00b1139c ["INT_ADD", "register:40f0:8", ["const:b1139c:8", "const:4:8"]]
+ 00b1139c ["CALL", null, ["callee:00bdfc50:8"]]
- 00b112d4 bytes 333a0394
+ 00b1139c bytes 2d3a0394
- 00b112f0 ["INT_ADD", "register:40f0:8", ["const:b112f0:8", "const:4:8"]]
- 00b112f0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b113b8 ["INT_ADD", "register:40f0:8", ["const:b113b8:8", "const:4:8"]]
+ 00b113b8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b112f0 bytes 1c270394
+ 00b113b8 bytes 16270394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe650a37f1fb3874c85fdcf3133d5a9"></a>

### [`00b11350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11350.md) → [`00b11418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11418.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdfbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b11364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11350.md#insn-00b11364)
- 新版 `00b1142c`（命令位置の公開資料なし）

~~~diff
- 00b11364 ["INT_ADD", "register:40f0:8", ["const:b11364:8", "const:4:8"]]
- 00b11364 ["CALL", null, ["callee:00bdfc80:8"]]
+ 00b1142c ["INT_ADD", "register:40f0:8", ["const:b1142c:8", "const:4:8"]]
+ 00b1142c ["CALL", null, ["callee:00bdfc80:8"]]
- 00b11364 bytes 1b3a0394
+ 00b1142c bytes 153a0394
~~~


<a id="compare-92a100cb2c9127befeaa35e7d02c2101"></a>

### [`00b1139c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b1139c.md) → [`00b11464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11464.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf770.md) · 呼出先 10件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf820.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b11434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b1139c.md#insn-00b11434) · [`00b11454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b1139c.md#insn-00b11454) · [`00b11468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b1139c.md#insn-00b11468)
- 新版 `00b114fc`（命令位置の公開資料なし） · `00b1151c`（命令位置の公開資料なし） · `00b11530`（命令位置の公開資料なし）

~~~diff
- 00b11434 ["INT_ADD", "register:40f0:8", ["const:b11434:8", "const:4:8"]]
- 00b11434 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b114fc ["INT_ADD", "register:40f0:8", ["const:b114fc:8", "const:4:8"]]
+ 00b114fc ["CALL", null, ["callee:00bdaff0:8"]]
- 00b11434 bytes c3260394
+ 00b114fc bytes bd260394
- 00b11454 ["INT_ADD", "register:40f0:8", ["const:b11454:8", "const:4:8"]]
- 00b11454 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b1151c ["INT_ADD", "register:40f0:8", ["const:b1151c:8", "const:4:8"]]
+ 00b1151c ["CALL", null, ["callee:00bdb160:8"]]
- 00b11454 bytes 17270394
+ 00b1151c bytes 11270394
- 00b11468 ["INT_ADD", "register:40f0:8", ["const:b11468:8", "const:4:8"]]
- 00b11468 ["CALL", null, ["callee:00bdf960:8"]]
+ 00b11530 ["INT_ADD", "register:40f0:8", ["const:b11530:8", "const:4:8"]]
+ 00b11530 ["CALL", null, ["callee:00bdf960:8"]]
- 00b11468 bytes 12390394
+ 00b11530 bytes 0c390394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78bcdd6b94603ae0d5414013142ef41d"></a>

### [`00b19fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19fdc.md) → [`00b1a0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a0a4.md) _ZN11flatbuffers6Parser15SerializeStructERNS_17FlatBufferBuilderERKNS_9StructDefERKNS_5ValueE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf790.md) · 呼出先 2件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf840.md) · 呼出先 2件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19fdc.md#insn-00b1a040) · [`00b1a0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19fdc.md#insn-00b1a0c4) · [`00b1a0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19fdc.md#insn-00b1a0dc)
- 新版 `00b1a108`（命令位置の公開資料なし） · `00b1a18c`（命令位置の公開資料なし） · `00b1a1a4`（命令位置の公開資料なし）

~~~diff
- 00b1a040 ["INT_ADD", "register:40f0:8", ["const:b1a040:8", "const:4:8"]]
- 00b1a040 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a108 ["INT_ADD", "register:40f0:8", ["const:b1a108:8", "const:4:8"]]
+ 00b1a108 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a040 bytes 94140394
+ 00b1a108 bytes 8e140394
- 00b1a0c4 ["INT_ADD", "register:40f0:8", ["const:b1a0c4:8", "const:4:8"]]
- 00b1a0c4 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a18c ["INT_ADD", "register:40f0:8", ["const:b1a18c:8", "const:4:8"]]
+ 00b1a18c ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a0c4 bytes 73140394
+ 00b1a18c bytes 6d140394
- 00b1a0dc ["INT_ADD", "register:40f0:8", ["const:b1a0dc:8", "const:4:8"]]
- 00b1a0dc ["CALL", null, ["callee:00bdb160:8"]]
+ 00b1a1a4 ["INT_ADD", "register:40f0:8", ["const:b1a1a4:8", "const:4:8"]]
+ 00b1a1a4 ["CALL", null, ["callee:00bdb160:8"]]
- 00b1a0dc bytes f5030394
+ 00b1a1a4 bytes ef030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3c8205cc28cb3361d35210e0cd7c75f"></a>

### [`00b1a154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a154.md) → [`00b1a21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a21c.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementIhEEvtT_S2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2b0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf360.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a154.md#insn-00b1a1a8) · [`00b1a1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a154.md#insn-00b1a1e0)
- 新版 `00b1a270`（命令位置の公開資料なし） · `00b1a2a8`（命令位置の公開資料なし）

~~~diff
- 00b1a1a8 ["INT_ADD", "register:40f0:8", ["const:b1a1a8:8", "const:4:8"]]
- 00b1a1a8 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a270 ["INT_ADD", "register:40f0:8", ["const:b1a270:8", "const:4:8"]]
+ 00b1a270 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a1a8 bytes 3a140394
+ 00b1a270 bytes 34140394
- 00b1a1e0 ["INT_ADD", "register:40f0:8", ["const:b1a1e0:8", "const:4:8"]]
- 00b1a1e0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a2a8 ["INT_ADD", "register:40f0:8", ["const:b1a2a8:8", "const:4:8"]]
+ 00b1a2a8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a1e0 bytes 2c140394
+ 00b1a2a8 bytes 26140394
~~~


<a id="compare-5519e0296ba9e173e9c7ba70230663e3"></a>

### [`00b1a694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a694.md) → [`00b1a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a75c.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementIaEEvtT_S2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2a0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf350.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1a6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a694.md#insn-00b1a6e8) · [`00b1a720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a694.md#insn-00b1a720)
- 新版 `00b1a7b0`（命令位置の公開資料なし） · `00b1a7e8`（命令位置の公開資料なし）

~~~diff
- 00b1a6e8 ["INT_ADD", "register:40f0:8", ["const:b1a6e8:8", "const:4:8"]]
- 00b1a6e8 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a7b0 ["INT_ADD", "register:40f0:8", ["const:b1a7b0:8", "const:4:8"]]
+ 00b1a7b0 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a6e8 bytes ea120394
+ 00b1a7b0 bytes e4120394
- 00b1a720 ["INT_ADD", "register:40f0:8", ["const:b1a720:8", "const:4:8"]]
- 00b1a720 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1a7e8 ["INT_ADD", "register:40f0:8", ["const:b1a7e8:8", "const:4:8"]]
+ 00b1a7e8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1a720 bytes dc120394
+ 00b1a7e8 bytes d6120394
~~~


<a id="compare-ba9a076bee4afe3879759681d786a2e4"></a>

### [`00b1b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b028.md) → [`00b1b0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementItEEvtT_S2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf370.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1b098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b028.md#insn-00b1b098) · [`00b1b0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b028.md#insn-00b1b0d4) · [`00b1b108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b028.md#insn-00b1b108)
- 新版 `00b1b160`（命令位置の公開資料なし） · `00b1b19c`（命令位置の公開資料なし） · `00b1b1d0`（命令位置の公開資料なし）

~~~diff
- 00b1b098 ["INT_ADD", "register:40f0:8", ["const:b1b098:8", "const:4:8"]]
- 00b1b098 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1b160 ["INT_ADD", "register:40f0:8", ["const:b1b160:8", "const:4:8"]]
+ 00b1b160 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1b098 bytes 7e100394
+ 00b1b160 bytes 78100394
- 00b1b0d4 ["INT_ADD", "register:40f0:8", ["const:b1b0d4:8", "const:4:8"]]
- 00b1b0d4 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1b19c ["INT_ADD", "register:40f0:8", ["const:b1b19c:8", "const:4:8"]]
+ 00b1b19c ["CALL", null, ["callee:00bdf340:8"]]
- 00b1b0d4 bytes 6f100394
+ 00b1b19c bytes 69100394
- 00b1b108 ["INT_ADD", "register:40f0:8", ["const:b1b108:8", "const:4:8"]]
- 00b1b108 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1b1d0 ["INT_ADD", "register:40f0:8", ["const:b1b1d0:8", "const:4:8"]]
+ 00b1b1d0 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1b108 bytes 62100394
+ 00b1b1d0 bytes 5c100394
~~~


<a id="compare-04d53c91060f641fc5582cb6d3a4d270"></a>

### [`00b1bb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bb74.md) → [`00b1bc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIlEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1bbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bb74.md#insn-00b1bbd0) · [`00b1bc2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bb74.md#insn-00b1bc2c)
- 新版 `00b1bc98`（命令位置の公開資料なし） · `00b1bcf4`（命令位置の公開資料なし）

~~~diff
- 00b1bbd0 ["INT_ADD", "register:40f0:8", ["const:b1bbd0:8", "const:4:8"]]
- 00b1bbd0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1bc98 ["INT_ADD", "register:40f0:8", ["const:b1bc98:8", "const:4:8"]]
+ 00b1bc98 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1bbd0 bytes b00d0394
+ 00b1bc98 bytes aa0d0394
- 00b1bc2c ["INT_ADD", "register:40f0:8", ["const:b1bc2c:8", "const:4:8"]]
- 00b1bc2c ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1bcf4 ["INT_ADD", "register:40f0:8", ["const:b1bcf4:8", "const:4:8"]]
+ 00b1bcf4 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1bc2c bytes 990d0394
+ 00b1bcf4 bytes 930d0394
~~~


<a id="compare-eda95d708e0fc14984e10218c05546b3"></a>

### [`00b1c090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c090.md) → [`00b1c158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c158.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementImEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3a0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c090.md#insn-00b1c0ec) · [`00b1c148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c090.md#insn-00b1c148)
- 新版 `00b1c1b4`（命令位置の公開資料なし） · `00b1c210`（命令位置の公開資料なし）

~~~diff
- 00b1c0ec ["INT_ADD", "register:40f0:8", ["const:b1c0ec:8", "const:4:8"]]
- 00b1c0ec ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c1b4 ["INT_ADD", "register:40f0:8", ["const:b1c1b4:8", "const:4:8"]]
+ 00b1c1b4 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c0ec bytes 690c0394
+ 00b1c1b4 bytes 630c0394
- 00b1c148 ["INT_ADD", "register:40f0:8", ["const:b1c148:8", "const:4:8"]]
- 00b1c148 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c210 ["INT_ADD", "register:40f0:8", ["const:b1c210:8", "const:4:8"]]
+ 00b1c210 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c148 bytes 520c0394
+ 00b1c210 bytes 4c0c0394
~~~


<a id="compare-2532d6f5713d0a1321fead9f818cd420"></a>

### [`00b1c364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c364.md) → [`00b1c42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c42c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIfEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf360.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf410.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c364.md#insn-00b1c3c0) · [`00b1c41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c364.md#insn-00b1c41c)
- 新版 `00b1c488`（命令位置の公開資料なし） · `00b1c4e4`（命令位置の公開資料なし）

~~~diff
- 00b1c3c0 ["INT_ADD", "register:40f0:8", ["const:b1c3c0:8", "const:4:8"]]
- 00b1c3c0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c488 ["INT_ADD", "register:40f0:8", ["const:b1c488:8", "const:4:8"]]
+ 00b1c488 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c3c0 bytes b40b0394
+ 00b1c488 bytes ae0b0394
- 00b1c41c ["INT_ADD", "register:40f0:8", ["const:b1c41c:8", "const:4:8"]]
- 00b1c41c ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c4e4 ["INT_ADD", "register:40f0:8", ["const:b1c4e4:8", "const:4:8"]]
+ 00b1c4e4 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c41c bytes 9d0b0394
+ 00b1c4e4 bytes 970b0394
~~~


<a id="compare-f36bbeecd12e668f036f404735dde75a"></a>

### [`00b1c634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c634.md) → [`00b1c6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c6fc.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIdEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf350.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf400.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c634.md#insn-00b1c690) · [`00b1c6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c634.md#insn-00b1c6ec)
- 新版 `00b1c758`（命令位置の公開資料なし） · `00b1c7b4`（命令位置の公開資料なし）

~~~diff
- 00b1c690 ["INT_ADD", "register:40f0:8", ["const:b1c690:8", "const:4:8"]]
- 00b1c690 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c758 ["INT_ADD", "register:40f0:8", ["const:b1c758:8", "const:4:8"]]
+ 00b1c758 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c690 bytes 000b0394
+ 00b1c758 bytes fa0a0394
- 00b1c6ec ["INT_ADD", "register:40f0:8", ["const:b1c6ec:8", "const:4:8"]]
- 00b1c6ec ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c7b4 ["INT_ADD", "register:40f0:8", ["const:b1c7b4:8", "const:4:8"]]
+ 00b1c7b4 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c6ec bytes e90a0394
+ 00b1c7b4 bytes e30a0394
~~~


<a id="compare-533173d0e4b849086a4427afad1bfd0d"></a>

### [`00b1c720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c720.md) → [`00b1c7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetIvEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4d0.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf580.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c720.md#insn-00b1c784) · [`00b1c7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c720.md#insn-00b1c7f4) · [`00b1c814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c720.md#insn-00b1c814)
- 新版 `00b1c84c`（命令位置の公開資料なし） · `00b1c8bc`（命令位置の公開資料なし） · `00b1c8dc`（命令位置の公開資料なし）

~~~diff
- 00b1c784 ["INT_ADD", "register:40f0:8", ["const:b1c784:8", "const:4:8"]]
- 00b1c784 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c84c ["INT_ADD", "register:40f0:8", ["const:b1c84c:8", "const:4:8"]]
+ 00b1c84c ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c784 bytes c30a0394
+ 00b1c84c bytes bd0a0394
- 00b1c7f4 ["INT_ADD", "register:40f0:8", ["const:b1c7f4:8", "const:4:8"]]
- 00b1c7f4 ["CALL", null, ["callee:00bdf430:8"]]
+ 00b1c8bc ["INT_ADD", "register:40f0:8", ["const:b1c8bc:8", "const:4:8"]]
+ 00b1c8bc ["CALL", null, ["callee:00bdf430:8"]]
- 00b1c7f4 bytes e30a0394
+ 00b1c8bc bytes dd0a0394
- 00b1c814 ["INT_ADD", "register:40f0:8", ["const:b1c814:8", "const:4:8"]]
- 00b1c814 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c8dc ["INT_ADD", "register:40f0:8", ["const:b1c8dc:8", "const:4:8"]]
+ 00b1c8dc ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c814 bytes 9f0a0394
+ 00b1c8dc bytes 990a0394
~~~


<a id="compare-6ce2a36895a75c946be211ad2b156562"></a>

### [`00b1c864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c864.md) → [`00b1c92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md) _ZN11flatbuffers17FlatBufferBuilder8EndTableEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf410.md) · 呼出先 4件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf370.md)
- 新版 呼出元 1件 [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md) · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1c890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c864.md#insn-00b1c890) · [`00b1c8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c864.md#insn-00b1c8d0) · [`00b1c8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c864.md#insn-00b1c8e8)
- 新版 `00b1c958`（命令位置の公開資料なし） · `00b1c998`（命令位置の公開資料なし） · `00b1c9b0`（命令位置の公開資料なし）

~~~diff
- 00b1c890 ["INT_ADD", "register:40f0:8", ["const:b1c890:8", "const:4:8"]]
- 00b1c890 ["CALL", null, ["callee:00bdf420:8"]]
+ 00b1c958 ["INT_ADD", "register:40f0:8", ["const:b1c958:8", "const:4:8"]]
+ 00b1c958 ["CALL", null, ["callee:00bdf420:8"]]
- 00b1c890 bytes b80a0394
+ 00b1c958 bytes b20a0394
- 00b1c8d0 ["INT_ADD", "register:40f0:8", ["const:b1c8d0:8", "const:4:8"]]
- 00b1c8d0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1c998 ["INT_ADD", "register:40f0:8", ["const:b1c998:8", "const:4:8"]]
+ 00b1c998 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1c8d0 bytes 700a0394
+ 00b1c998 bytes 6a0a0394
- 00b1c8e8 ["INT_ADD", "register:40f0:8", ["const:b1c8e8:8", "const:4:8"]]
- 00b1c8e8 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00b1c9b0 ["INT_ADD", "register:40f0:8", ["const:b1c9b0:8", "const:4:8"]]
+ 00b1c9b0 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00b1c8e8 bytes 16fa0294
+ 00b1c9b0 bytes 10fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ffac08696aa72ca115537bceead09a"></a>

### [`00b1ca2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1ca2c.md) → [`00b1caf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1caf4.md) _ZN11flatbuffers17FlatBufferBuilder11StartVectorEmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3c0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf470.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1ca98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1ca2c.md#insn-00b1ca98) · [`00b1cb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1ca2c.md#insn-00b1cb24)
- 新版 `00b1cb60`（命令位置の公開資料なし） · `00b1cbec`（命令位置の公開資料なし）

~~~diff
- 00b1ca98 ["INT_ADD", "register:40f0:8", ["const:b1ca98:8", "const:4:8"]]
- 00b1ca98 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1cb60 ["INT_ADD", "register:40f0:8", ["const:b1cb60:8", "const:4:8"]]
+ 00b1cb60 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1ca98 bytes fe090394
+ 00b1cb60 bytes f8090394
- 00b1cb24 ["INT_ADD", "register:40f0:8", ["const:b1cb24:8", "const:4:8"]]
- 00b1cb24 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1cbec ["INT_ADD", "register:40f0:8", ["const:b1cbec:8", "const:4:8"]]
+ 00b1cbec ["CALL", null, ["callee:00bdf340:8"]]
- 00b1cb24 bytes db090394
+ 00b1cbec bytes d5090394
~~~


<a id="compare-d4dd178ab1809e244ff5e61e26e84432"></a>

### [`00b1cb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cb78.md) → [`00b1cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIvEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1cbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cb78.md#insn-00b1cbd4)
- 新版 `00b1cc9c`（命令位置の公開資料なし）

~~~diff
- 00b1cbd4 ["INT_ADD", "register:40f0:8", ["const:b1cbd4:8", "const:4:8"]]
- 00b1cbd4 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1cc9c ["INT_ADD", "register:40f0:8", ["const:b1cc9c:8", "const:4:8"]]
+ 00b1cc9c ["CALL", null, ["callee:00bdf340:8"]]
- 00b1cbd4 bytes af090394
+ 00b1cc9c bytes a9090394
~~~


<a id="compare-4178edbe66694e820e87daaebbf7c2ba"></a>

### [`00b1d3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d3fc.md) → [`00b1d4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d4c4.md) _ZN11flatbuffers10IDLOptionsaSERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf060.md) · 呼出先 2件 [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdff90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff90.md)
- 新版 呼出元 1件 [`00bdf110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf110.md) · 呼出先 2件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1d448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d3fc.md#insn-00b1d448) · [`00b1d46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d3fc.md#insn-00b1d46c) · [`00b1d498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d3fc.md#insn-00b1d498)
- 新版 `00b1d510`（命令位置の公開資料なし） · `00b1d534`（命令位置の公開資料なし） · `00b1d560`（命令位置の公開資料なし）

~~~diff
- 00b1d448 ["INT_ADD", "register:40f0:8", ["const:b1d448:8", "const:4:8"]]
- 00b1d448 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b1d510 ["INT_ADD", "register:40f0:8", ["const:b1d510:8", "const:4:8"]]
+ 00b1d510 ["CALL", null, ["callee:00bde1e0:8"]]
- 00b1d448 bytes 3a030394
+ 00b1d510 bytes 34030394
- 00b1d46c ["INT_ADD", "register:40f0:8", ["const:b1d46c:8", "const:4:8"]]
- 00b1d46c ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b1d534 ["INT_ADD", "register:40f0:8", ["const:b1d534:8", "const:4:8"]]
+ 00b1d534 ["CALL", null, ["callee:00bde1e0:8"]]
- 00b1d46c bytes 31030394
+ 00b1d534 bytes 2b030394
- 00b1d498 ["INT_ADD", "register:40f0:8", ["const:b1d498:8", "const:4:8"]]
- 00b1d498 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b1d560 ["INT_ADD", "register:40f0:8", ["const:b1d560:8", "const:4:8"]]
+ 00b1d560 ["CALL", null, ["callee:00bde1e0:8"]]
- 00b1d498 bytes 26030394
+ 00b1d560 bytes 20030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9633a15e6a971e88f4deef46437a7a9d"></a>

### [`00b1d688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d688.md) → [`00b1d750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d750.md) _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdef60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef60.md) · 呼出先 5件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdf780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf780.md) [`00bdf840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf840.md) [`00bdf920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf920.md) [`00bdfa30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa30.md)
- 新版 呼出元 1件 [`00bdf010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf010.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf830.md) [`00bdf8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8f0.md) [`00bdf9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9d0.md) [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1d6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d688.md#insn-00b1d6c0) · [`00b1d6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d688.md#insn-00b1d6e4) · [`00b1d700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d688.md#insn-00b1d700)
- 新版 `00b1d788`（命令位置の公開資料なし） · `00b1d7ac`（命令位置の公開資料なし） · `00b1d7c8`（命令位置の公開資料なし）

~~~diff
- 00b1d6c0 ["INT_ADD", "register:40f0:8", ["const:b1d6c0:8", "const:4:8"]]
- 00b1d6c0 ["CALL", null, ["callee:00bdf830:8"]]
+ 00b1d788 ["INT_ADD", "register:40f0:8", ["const:b1d788:8", "const:4:8"]]
+ 00b1d788 ["CALL", null, ["callee:00bdf830:8"]]
- 00b1d6c0 bytes 30080394
+ 00b1d788 bytes 2a080394
- 00b1d6e4 ["INT_ADD", "register:40f0:8", ["const:b1d6e4:8", "const:4:8"]]
- 00b1d6e4 ["CALL", null, ["callee:00bdf8f0:8"]]
+ 00b1d7ac ["INT_ADD", "register:40f0:8", ["const:b1d7ac:8", "const:4:8"]]
+ 00b1d7ac ["CALL", null, ["callee:00bdf8f0:8"]]
- 00b1d6e4 bytes 57080394
+ 00b1d7ac bytes 51080394
- 00b1d700 ["INT_ADD", "register:40f0:8", ["const:b1d700:8", "const:4:8"]]
- 00b1d700 ["CALL", null, ["callee:00bdf9d0:8"]]
+ 00b1d7c8 ["INT_ADD", "register:40f0:8", ["const:b1d7c8:8", "const:4:8"]]
+ 00b1d7c8 ["CALL", null, ["callee:00bdf9d0:8"]]
- 00b1d700 bytes 88080394
+ 00b1d7c8 bytes 82080394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc5d227f6df2481d923bb825ae646194"></a>

### [`00b1f594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f594.md) → [`00b1f65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f65c.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf970.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdfa20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa20.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b1f640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f594.md#insn-00b1f640) · [`00b1f6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f594.md#insn-00b1f6cc) · [`00b1f6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f594.md#insn-00b1f6dc)
- 新版 `00b1f708`（命令位置の公開資料なし） · `00b1f794`（命令位置の公開資料なし） · `00b1f7a4`（命令位置の公開資料なし）

~~~diff
- 00b1f640 ["INT_ADD", "register:40f0:8", ["const:b1f640:8", "const:4:8"]]
- 00b1f640 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1f708 ["INT_ADD", "register:40f0:8", ["const:b1f708:8", "const:4:8"]]
+ 00b1f708 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1f640 bytes 48ee0294
+ 00b1f708 bytes 42ee0294
- 00b1f6cc ["INT_ADD", "register:40f0:8", ["const:b1f6cc:8", "const:4:8"]]
- 00b1f6cc ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1f794 ["INT_ADD", "register:40f0:8", ["const:b1f794:8", "const:4:8"]]
+ 00b1f794 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1f6cc bytes 25ee0294
+ 00b1f794 bytes 1fee0294
- 00b1f6dc ["INT_ADD", "register:40f0:8", ["const:b1f6dc:8", "const:4:8"]]
- 00b1f6dc ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1f7a4 ["INT_ADD", "register:40f0:8", ["const:b1f7a4:8", "const:4:8"]]
+ 00b1f7a4 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1f6dc bytes 21ee0294
+ 00b1f7a4 bytes 1bee0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22df53337f504bb4c198451409772cf"></a>

### [`00b209f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b209f4.md) → [`00b20abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20abc.md) _ZN11flatbuffers6Parser16ParseProtoOptionEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf7e0.md) · 呼出先 3件 [`00bdf730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf730.md) [`00bdf870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf870.md) [`00bdf8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8b0.md)
- 新版 呼出元 1件 [`00bdf890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf890.md) · 呼出先 3件 [`00bdf7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7e0.md) [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b209f4.md#insn-00b20a0c) · [`00b20a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b209f4.md#insn-00b20a28) · [`00b20a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b209f4.md#insn-00b20a44)
- 新版 `00b20ad4`（命令位置の公開資料なし） · `00b20af0`（命令位置の公開資料なし） · `00b20b0c`（命令位置の公開資料なし）

~~~diff
- 00b20a0c ["INT_ADD", "register:40f0:8", ["const:b20a0c:8", "const:4:8"]]
- 00b20a0c ["CALL", null, ["callee:00bdf920:8"]]
+ 00b20ad4 ["INT_ADD", "register:40f0:8", ["const:b20ad4:8", "const:4:8"]]
+ 00b20ad4 ["CALL", null, ["callee:00bdf920:8"]]
- 00b20a0c bytes 99fb0294
+ 00b20ad4 bytes 93fb0294
- 00b20a28 ["INT_ADD", "register:40f0:8", ["const:b20a28:8", "const:4:8"]]
- 00b20a28 ["CALL", null, ["callee:00bdf7e0:8"]]
+ 00b20af0 ["INT_ADD", "register:40f0:8", ["const:b20af0:8", "const:4:8"]]
+ 00b20af0 ["CALL", null, ["callee:00bdf7e0:8"]]
- 00b20a28 bytes 42fb0294
+ 00b20af0 bytes 3cfb0294
- 00b20a44 ["INT_ADD", "register:40f0:8", ["const:b20a44:8", "const:4:8"]]
- 00b20a44 ["CALL", null, ["callee:00bdf960:8"]]
+ 00b20b0c ["INT_ADD", "register:40f0:8", ["const:b20b0c:8", "const:4:8"]]
+ 00b20b0c ["CALL", null, ["callee:00bdf960:8"]]
- 00b20a44 bytes 9bfb0294
+ 00b20b0c bytes 95fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3094fe3e063f6caf76128259de7f8e07"></a>

### [`00b20d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20d88.md) → [`00b20e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20e50.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf110.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1c0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20d88.md#insn-00b20e18) · [`00b20e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20d88.md#insn-00b20e24) · [`00b20e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20d88.md#insn-00b20e4c)
- 新版 `00b20ee0`（命令位置の公開資料なし） · `00b20eec`（命令位置の公開資料なし） · `00b20f14`（命令位置の公開資料なし）

~~~diff
- 00b20e18 ["INT_ADD", "register:40f0:8", ["const:b20e18:8", "const:4:8"]]
- 00b20e18 ["CALL", null, ["callee:00bde270:8"]]
+ 00b20ee0 ["INT_ADD", "register:40f0:8", ["const:b20ee0:8", "const:4:8"]]
+ 00b20ee0 ["CALL", null, ["callee:00bde270:8"]]
- 00b20e18 bytes eaf40294
+ 00b20ee0 bytes e4f40294
- 00b20e24 ["INT_ADD", "register:40f0:8", ["const:b20e24:8", "const:4:8"]]
- 00b20e24 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b20eec ["INT_ADD", "register:40f0:8", ["const:b20eec:8", "const:4:8"]]
+ 00b20eec ["CALL", null, ["callee:00bdaff0:8"]]
- 00b20e24 bytes 47e80294
+ 00b20eec bytes 41e80294
- 00b20e4c ["INT_ADD", "register:40f0:8", ["const:b20e4c:8", "const:4:8"]]
- 00b20e4c ["CALL", null, ["callee:00bdb160:8"]]
+ 00b20f14 ["INT_ADD", "register:40f0:8", ["const:b20f14:8", "const:4:8"]]
+ 00b20f14 ["CALL", null, ["callee:00bdb160:8"]]
- 00b20e4c bytes 99e80294
+ 00b20f14 bytes 93e80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94871d1d0a095ad8914a1e72c7a22d4"></a>

### [`00b20f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20f40.md) → [`00b21008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b21008.md) _ZN11flatbuffers6Parser11StartStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPNS_9StructDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf6d0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdf820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf820.md)
- 新版 呼出元 1件 [`00bdf780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf780.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdf8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b20f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20f40.md#insn-00b20f7c) · [`00b20fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20f40.md#insn-00b20fb4) · [`00b20fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20f40.md#insn-00b20fe4)
- 新版 `00b21044`（命令位置の公開資料なし） · `00b2107c`（命令位置の公開資料なし） · `00b210ac`（命令位置の公開資料なし）

~~~diff
- 00b20f7c ["INT_ADD", "register:40f0:8", ["const:b20f7c:8", "const:4:8"]]
- 00b20f7c ["CALL", null, ["callee:00bdf8d0:8"]]
+ 00b21044 ["INT_ADD", "register:40f0:8", ["const:b21044:8", "const:4:8"]]
+ 00b21044 ["CALL", null, ["callee:00bdf8d0:8"]]
- 00b20f7c bytes 29fa0294
+ 00b21044 bytes 23fa0294
- 00b20fb4 ["INT_ADD", "register:40f0:8", ["const:b20fb4:8", "const:4:8"]]
- 00b20fb4 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b2107c ["INT_ADD", "register:40f0:8", ["const:b2107c:8", "const:4:8"]]
+ 00b2107c ["CALL", null, ["callee:00bde1e0:8"]]
- 00b20fb4 bytes 5ff40294
+ 00b2107c bytes 59f40294
- 00b20fe4 ["INT_ADD", "register:40f0:8", ["const:b20fe4:8", "const:4:8"]]
- 00b20fe4 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b210ac ["INT_ADD", "register:40f0:8", ["const:b210ac:8", "const:4:8"]]
+ 00b210ac ["CALL", null, ["callee:00bde1e0:8"]]
- 00b20fe4 bytes 53f40294
+ 00b210ac bytes 4df40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8464b7074755951ae09ca07e7727d6fb"></a>

### [`00b213c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b213c4.md) → [`00b2148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2148c.md) _ZN11flatbuffers6Parser15UniqueNamespaceEPNS_9NamespaceE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf7a0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf850.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b214c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b213c4.md#insn-00b214c8) · [`00b2152c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b213c4.md#insn-00b2152c) · [`00b21570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b213c4.md#insn-00b21570)
- 新版 `00b21590`（命令位置の公開資料なし） · `00b215f4`（命令位置の公開資料なし） · `00b21638`（命令位置の公開資料なし）

~~~diff
- 00b214c8 ["INT_ADD", "register:40f0:8", ["const:b214c8:8", "const:4:8"]]
- 00b214c8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b21590 ["INT_ADD", "register:40f0:8", ["const:b21590:8", "const:4:8"]]
+ 00b21590 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b214c8 bytes 0ee70294
+ 00b21590 bytes 08e70294
- 00b2152c ["INT_ADD", "register:40f0:8", ["const:b2152c:8", "const:4:8"]]
- 00b2152c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b215f4 ["INT_ADD", "register:40f0:8", ["const:b215f4:8", "const:4:8"]]
+ 00b215f4 ["CALL", null, ["callee:00bdb010:8"]]
- 00b2152c bytes 8de60294
+ 00b215f4 bytes 87e60294
- 00b21570 ["INT_ADD", "register:40f0:8", ["const:b21570:8", "const:4:8"]]
- 00b21570 ["CALL", null, ["callee:00bde270:8"]]
+ 00b21638 ["INT_ADD", "register:40f0:8", ["const:b21638:8", "const:4:8"]]
+ 00b21638 ["CALL", null, ["callee:00bde270:8"]]
- 00b21570 bytes 14f30294
+ 00b21638 bytes 0ef30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d15dbdea5724554f4185088f81f1e374"></a>

### [`00b21614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b21614.md) → [`00b216dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b216dc.md) _ZN11flatbuffers6Parser15UnqualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf7b0.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bde6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6d0.md)
- 新版 呼出元 1件 [`00bdf860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf860.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2164c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b21614.md#insn-00b2164c) · [`00b21680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b21614.md#insn-00b21680) · [`00b216b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b21614.md#insn-00b216b0)
- 新版 `00b21714`（命令位置の公開資料なし） · `00b21748`（命令位置の公開資料なし） · `00b21778`（命令位置の公開資料なし）

~~~diff
- 00b2164c ["INT_ADD", "register:40f0:8", ["const:b2164c:8", "const:4:8"]]
- 00b2164c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b21714 ["INT_ADD", "register:40f0:8", ["const:b21714:8", "const:4:8"]]
+ 00b21714 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b2164c bytes 3de60294
+ 00b21714 bytes 37e60294
- 00b21680 ["INT_ADD", "register:40f0:8", ["const:b21680:8", "const:4:8"]]
- 00b21680 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b21748 ["INT_ADD", "register:40f0:8", ["const:b21748:8", "const:4:8"]]
+ 00b21748 ["CALL", null, ["callee:00bdb130:8"]]
- 00b21680 bytes 80e60294
+ 00b21748 bytes 7ae60294
- 00b216b0 ["INT_ADD", "register:40f0:8", ["const:b216b0:8", "const:4:8"]]
- 00b216b0 ["CALL", null, ["callee:00bde920:8"]]
+ 00b21778 ["INT_ADD", "register:40f0:8", ["const:b21778:8", "const:4:8"]]
+ 00b21778 ["CALL", null, ["callee:00bde920:8"]]
- 00b216b0 bytes 70f40294
+ 00b21778 bytes 6af40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19dc07d6dc26fe9234fada1674a34dd5"></a>

### [`00b22214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22214.md) → [`00b222dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md) FUN_00b222dc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b217a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b217a4.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9e0.md) [`00bdfb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb90.md)
- 新版 呼出元 1件 [`00b2186c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdda90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda90.md) [`00bdfc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22214.md#insn-00b22260) · [`00b22294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22214.md#insn-00b22294) · [`00b222a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22214.md#insn-00b222a8)
- 新版 `00b22328`（命令位置の公開資料なし） · `00b2235c`（命令位置の公開資料なし） · `00b22370`（命令位置の公開資料なし）

~~~diff
- 00b22260 ["INT_ADD", "register:40f0:8", ["const:b22260:8", "const:4:8"]]
- 00b22260 ["CALL", null, ["callee:00bdfc40:8"]]
+ 00b22328 ["INT_ADD", "register:40f0:8", ["const:b22328:8", "const:4:8"]]
+ 00b22328 ["CALL", null, ["callee:00bdfc40:8"]]
- 00b22260 bytes 4cf60294
+ 00b22328 bytes 46f60294
- 00b22294 ["INT_ADD", "register:40f0:8", ["const:b22294:8", "const:4:8"]]
- 00b22294 ["CALL", null, ["callee:00bdda90:8"]]
+ 00b2235c ["INT_ADD", "register:40f0:8", ["const:b2235c:8", "const:4:8"]]
+ 00b2235c ["CALL", null, ["callee:00bdda90:8"]]
- 00b22294 bytes d3ed0294
+ 00b2235c bytes cded0294
- 00b222a8 ["INT_ADD", "register:40f0:8", ["const:b222a8:8", "const:4:8"]]
- 00b222a8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b22370 ["INT_ADD", "register:40f0:8", ["const:b22370:8", "const:4:8"]]
+ 00b22370 ["CALL", null, ["callee:00bdb010:8"]]
- 00b222a8 bytes 2ee30294
+ 00b22370 bytes 28e30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d721af642c357df353ac12156690fc3"></a>

### [`00b22bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22bb0.md) → [`00b22c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22c78.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf100.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1b0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22bb0.md#insn-00b22c40) · [`00b22c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22bb0.md#insn-00b22c4c) · [`00b22c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22bb0.md#insn-00b22c74)
- 新版 `00b22d08`（命令位置の公開資料なし） · `00b22d14`（命令位置の公開資料なし） · `00b22d3c`（命令位置の公開資料なし）

~~~diff
- 00b22c40 ["INT_ADD", "register:40f0:8", ["const:b22c40:8", "const:4:8"]]
- 00b22c40 ["CALL", null, ["callee:00bde270:8"]]
+ 00b22d08 ["INT_ADD", "register:40f0:8", ["const:b22d08:8", "const:4:8"]]
+ 00b22d08 ["CALL", null, ["callee:00bde270:8"]]
- 00b22c40 bytes 60ed0294
+ 00b22d08 bytes 5aed0294
- 00b22c4c ["INT_ADD", "register:40f0:8", ["const:b22c4c:8", "const:4:8"]]
- 00b22c4c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b22d14 ["INT_ADD", "register:40f0:8", ["const:b22d14:8", "const:4:8"]]
+ 00b22d14 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b22c4c bytes bde00294
+ 00b22d14 bytes b7e00294
- 00b22c74 ["INT_ADD", "register:40f0:8", ["const:b22c74:8", "const:4:8"]]
- 00b22c74 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b22d3c ["INT_ADD", "register:40f0:8", ["const:b22d3c:8", "const:4:8"]]
+ 00b22d3c ["CALL", null, ["callee:00bdb160:8"]]
- 00b22c74 bytes 0fe10294
+ 00b22d3c bytes 09e10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e66b206933e9a159bfebefd4d4f89aaa"></a>

### [`00b22d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22d68.md) → [`00b22e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf150.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b22df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22d68.md#insn-00b22df8) · [`00b22e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22d68.md#insn-00b22e04) · [`00b22e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22d68.md#insn-00b22e2c)
- 新版 `00b22ec0`（命令位置の公開資料なし） · `00b22ecc`（命令位置の公開資料なし） · `00b22ef4`（命令位置の公開資料なし）

~~~diff
- 00b22df8 ["INT_ADD", "register:40f0:8", ["const:b22df8:8", "const:4:8"]]
- 00b22df8 ["CALL", null, ["callee:00bde270:8"]]
+ 00b22ec0 ["INT_ADD", "register:40f0:8", ["const:b22ec0:8", "const:4:8"]]
+ 00b22ec0 ["CALL", null, ["callee:00bde270:8"]]
- 00b22df8 bytes f2ec0294
+ 00b22ec0 bytes ecec0294
- 00b22e04 ["INT_ADD", "register:40f0:8", ["const:b22e04:8", "const:4:8"]]
- 00b22e04 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b22ecc ["INT_ADD", "register:40f0:8", ["const:b22ecc:8", "const:4:8"]]
+ 00b22ecc ["CALL", null, ["callee:00bdaff0:8"]]
- 00b22e04 bytes 4fe00294
+ 00b22ecc bytes 49e00294
- 00b22e2c ["INT_ADD", "register:40f0:8", ["const:b22e2c:8", "const:4:8"]]
- 00b22e2c ["CALL", null, ["callee:00bdb160:8"]]
+ 00b22ef4 ["INT_ADD", "register:40f0:8", ["const:b22ef4:8", "const:4:8"]]
+ 00b22ef4 ["CALL", null, ["callee:00bdb160:8"]]
- 00b22e2c bytes a1e00294
+ 00b22ef4 bytes 9be00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-843269f34b3d0d5e4bc1ea22f242e4e3"></a>

### [`00b253d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b253d0.md) → [`00b25498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25498.md) _ZN11flatbuffers6Parser13ParseProtoKeyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf730.md) · 呼出先 2件 [`00bdf870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf870.md) [`00bdf8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8b0.md)
- 新版 呼出元 1件 [`00bdf7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7e0.md) · 呼出先 2件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b253fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b253d0.md#insn-00b253fc) · [`00b2541c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b253d0.md#insn-00b2541c) · [`00b2544c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b253d0.md#insn-00b2544c)
- 新版 `00b254c4`（命令位置の公開資料なし） · `00b254e4`（命令位置の公開資料なし） · `00b25514`（命令位置の公開資料なし）

~~~diff
- 00b253fc ["INT_ADD", "register:40f0:8", ["const:b253fc:8", "const:4:8"]]
- 00b253fc ["CALL", null, ["callee:00bdf920:8"]]
+ 00b254c4 ["INT_ADD", "register:40f0:8", ["const:b254c4:8", "const:4:8"]]
+ 00b254c4 ["CALL", null, ["callee:00bdf920:8"]]
- 00b253fc bytes 1de90294
+ 00b254c4 bytes 17e90294
- 00b2541c ["INT_ADD", "register:40f0:8", ["const:b2541c:8", "const:4:8"]]
- 00b2541c ["CALL", null, ["callee:00bdf920:8"]]
+ 00b254e4 ["INT_ADD", "register:40f0:8", ["const:b254e4:8", "const:4:8"]]
+ 00b254e4 ["CALL", null, ["callee:00bdf920:8"]]
- 00b2541c bytes 15e90294
+ 00b254e4 bytes 0fe90294
- 00b2544c ["INT_ADD", "register:40f0:8", ["const:b2544c:8", "const:4:8"]]
- 00b2544c ["CALL", null, ["callee:00bdf960:8"]]
+ 00b25514 ["INT_ADD", "register:40f0:8", ["const:b25514:8", "const:4:8"]]
+ 00b25514 ["CALL", null, ["callee:00bdf960:8"]]
- 00b2544c bytes 19e90294
+ 00b25514 bytes 13e90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4da190cca4e5dc3a33dc5a620487c163"></a>

### [`00b25c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25c7c.md) → [`00b25d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25d44.md) _ZN11flexbuffers7Builder6EndMapEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa20.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdfad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfad0.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25c7c.md#insn-00b25cf4) · [`00b25d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25c7c.md#insn-00b25d14) · [`00b25d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25c7c.md#insn-00b25d38)
- 新版 `00b25dbc`（命令位置の公開資料なし） · `00b25ddc`（命令位置の公開資料なし） · `00b25e00`（命令位置の公開資料なし）

~~~diff
- 00b25cf4 ["INT_ADD", "register:40f0:8", ["const:b25cf4:8", "const:4:8"]]
- 00b25cf4 ["CALL", null, ["callee:00bdfe80:8"]]
+ 00b25dbc ["INT_ADD", "register:40f0:8", ["const:b25dbc:8", "const:4:8"]]
+ 00b25dbc ["CALL", null, ["callee:00bdfe80:8"]]
- 00b25cf4 bytes 37e80294
+ 00b25dbc bytes 31e80294
- 00b25d14 ["INT_ADD", "register:40f0:8", ["const:b25d14:8", "const:4:8"]]
- 00b25d14 ["CALL", null, ["callee:00bdfab0:8"]]
+ 00b25ddc ["INT_ADD", "register:40f0:8", ["const:b25ddc:8", "const:4:8"]]
+ 00b25ddc ["CALL", null, ["callee:00bdfab0:8"]]
- 00b25d14 bytes 3be70294
+ 00b25ddc bytes 35e70294
- 00b25d38 ["INT_ADD", "register:40f0:8", ["const:b25d38:8", "const:4:8"]]
- 00b25d38 ["CALL", null, ["callee:00bdfab0:8"]]
+ 00b25e00 ["INT_ADD", "register:40f0:8", ["const:b25e00:8", "const:4:8"]]
+ 00b25e00 ["CALL", null, ["callee:00bdfab0:8"]]
- 00b25d38 bytes 32e70294
+ 00b25e00 bytes 2ce70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871529180336610c95362f67835922ef"></a>

### [`00b25e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25e60.md) → [`00b25f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25f28.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa60.md) · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00bdfa00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa00.md)
- 新版 呼出元 1件 [`00bdfb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb10.md) · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bdfab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25e60.md#insn-00b25eac) · [`00b25ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25e60.md#insn-00b25ed8) · [`00b25f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25e60.md#insn-00b25f48)
- 新版 `00b25f74`（命令位置の公開資料なし） · `00b25fa0`（命令位置の公開資料なし） · `00b26010`（命令位置の公開資料なし）

~~~diff
- 00b25eac ["INT_ADD", "register:40f0:8", ["const:b25eac:8", "const:4:8"]]
- 00b25eac ["CALL", null, ["callee:00bdfab0:8"]]
+ 00b25f74 ["INT_ADD", "register:40f0:8", ["const:b25f74:8", "const:4:8"]]
+ 00b25f74 ["CALL", null, ["callee:00bdfab0:8"]]
- 00b25eac bytes d5e60294
+ 00b25f74 bytes cfe60294
- 00b25ed8 ["INT_ADD", "register:40f0:8", ["const:b25ed8:8", "const:4:8"]]
- 00b25ed8 ["CALL", null, ["callee:00be0020:8"]]
+ 00b25fa0 ["INT_ADD", "register:40f0:8", ["const:b25fa0:8", "const:4:8"]]
+ 00b25fa0 ["CALL", null, ["callee:00be0020:8"]]
- 00b25ed8 bytes 26e80294
+ 00b25fa0 bytes 20e80294
- 00b25f48 ["INT_ADD", "register:40f0:8", ["const:b25f48:8", "const:4:8"]]
- 00b25f48 ["CALL", null, ["callee:00bde270:8"]]
+ 00b26010 ["INT_ADD", "register:40f0:8", ["const:b26010:8", "const:4:8"]]
+ 00b26010 ["CALL", null, ["callee:00bde270:8"]]
- 00b25f48 bytes 9ee00294
+ 00b26010 bytes 98e00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8164a2d27a5376f23769a123676d5dc6"></a>

### [`00b25fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25fbc.md) → [`00b26084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26084.md) _ZN11flatbuffers6Parser15ParseFlexBufferEPKcS2_PN11flexbuffers7BuilderE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdf780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf780.md) [`00bdf840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf840.md) [`00bdfa30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf830.md) [`00bdf8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8f0.md) [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b25fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25fbc.md#insn-00b25fe8) · [`00b26008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25fbc.md#insn-00b26008) · [`00b26040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25fbc.md#insn-00b26040)
- 新版 `00b260b0`（命令位置の公開資料なし） · `00b260d0`（命令位置の公開資料なし） · `00b26108`（命令位置の公開資料なし）

~~~diff
- 00b25fe8 ["INT_ADD", "register:40f0:8", ["const:b25fe8:8", "const:4:8"]]
- 00b25fe8 ["CALL", null, ["callee:00bdf830:8"]]
+ 00b260b0 ["INT_ADD", "register:40f0:8", ["const:b260b0:8", "const:4:8"]]
+ 00b260b0 ["CALL", null, ["callee:00bdf830:8"]]
- 00b25fe8 bytes e6e50294
+ 00b260b0 bytes e0e50294
- 00b26008 ["INT_ADD", "register:40f0:8", ["const:b26008:8", "const:4:8"]]
- 00b26008 ["CALL", null, ["callee:00bdf8f0:8"]]
+ 00b260d0 ["INT_ADD", "register:40f0:8", ["const:b260d0:8", "const:4:8"]]
+ 00b260d0 ["CALL", null, ["callee:00bdf8f0:8"]]
- 00b26008 bytes 0ee60294
+ 00b260d0 bytes 08e60294
- 00b26040 ["INT_ADD", "register:40f0:8", ["const:b26040:8", "const:4:8"]]
- 00b26040 ["CALL", null, ["callee:00bdfae0:8"]]
+ 00b26108 ["INT_ADD", "register:40f0:8", ["const:b26108:8", "const:4:8"]]
+ 00b26108 ["CALL", null, ["callee:00bdfae0:8"]]
- 00b26040 bytes 7ce60294
+ 00b26108 bytes 76e60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e743248811bc886d14c59d0a7fed7a34"></a>

### [`00b2af9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2af9c.md) → [`00b2b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b064.md) _ZNK11flatbuffers4Type9SerializeEPNS_17FlatBufferBuilderE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdefa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2afc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2af9c.md#insn-00b2afc8)
- 新版 `00b2b090`（命令位置の公開資料なし）

~~~diff
- 00b2afc8 ["INT_ADD", "register:40f0:8", ["const:b2afc8:8", "const:4:8"]]
- 00b2afc8 ["CALL", null, ["callee:00bdf050:8"]]
+ 00b2b090 ["INT_ADD", "register:40f0:8", ["const:b2b090:8", "const:4:8"]]
+ 00b2b090 ["CALL", null, ["callee:00bdf050:8"]]
- 00b2afc8 bytes f6cf0294
+ 00b2b090 bytes f0cf0294
~~~


<a id="compare-73b13c75807e4373e7307002e0af75ec"></a>

### [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) → [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) _ZN10reflection11CreateFieldERN11flatbuffers17FlatBufferBuilderENS0_6OffsetINS0_6StringEEENS3_INS_4TypeEEEttldbbbNS3_INS0_6VectorINS3_INS_8K

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefb0.md) · 呼出先 13件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdf000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf000.md) [`00bdf010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md) [`00bdf020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf020.md) [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf060.md) · 呼出先 13件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0b0.md) [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) [`00bdf0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0d0.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2b060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md#insn-00b2b060) · [`00b2b080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md#insn-00b2b080) · [`00b2b0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md#insn-00b2b0e0)
- 新版 `00b2b128`（命令位置の公開資料なし） · `00b2b148`（命令位置の公開資料なし） · `00b2b1a8`（命令位置の公開資料なし）

~~~diff
- 00b2b060 ["INT_ADD", "register:40f0:8", ["const:b2b060:8", "const:4:8"]]
- 00b2b060 ["CALL", null, ["callee:00bdf400:8"]]
+ 00b2b128 ["INT_ADD", "register:40f0:8", ["const:b2b128:8", "const:4:8"]]
+ 00b2b128 ["CALL", null, ["callee:00bdf400:8"]]
- 00b2b060 bytes bcd00294
+ 00b2b128 bytes b6d00294
- 00b2b080 ["INT_ADD", "register:40f0:8", ["const:b2b080:8", "const:4:8"]]
- 00b2b080 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b2b148 ["INT_ADD", "register:40f0:8", ["const:b2b148:8", "const:4:8"]]
+ 00b2b148 ["CALL", null, ["callee:00bdf340:8"]]
- 00b2b080 bytes 84d00294
+ 00b2b148 bytes 7ed00294
- 00b2b0e0 ["INT_ADD", "register:40f0:8", ["const:b2b0e0:8", "const:4:8"]]
- 00b2b0e0 ["CALL", null, ["callee:00bdf440:8"]]
+ 00b2b1a8 ["INT_ADD", "register:40f0:8", ["const:b2b1a8:8", "const:4:8"]]
+ 00b2b1a8 ["CALL", null, ["callee:00bdf440:8"]]
- 00b2b0e0 bytes acd00294
+ 00b2b1a8 bytes a6d00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016f8b4a0194245354ac24b42453c356"></a>

### [`00b2bd18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bd18.md) → [`00b2bde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2bde0.md) _ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb40.md) · 呼出先 4件 [`00bdefa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefa0.md) [`00bdf030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf030.md) [`00bdf3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3d0.md) [`00bdf3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3f0.md)
- 新版 呼出元 1件 [`00bdfbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfbf0.md) · 呼出先 4件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md) [`00bdf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0e0.md) [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md) [`00bdf4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4a0.md)

変更の種類 constant, local_def_use, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b2be98",
      "incomplete_value": true,
      "site": "00b2bea0",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:ffffffff:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b2bd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bd18.md#insn-00b2bd50) · [`00b2bd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bd18.md#insn-00b2bd78) · [`00b2bd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bd18.md#insn-00b2bd90)
- 新版 `00b2be18`（命令位置の公開資料なし） · `00b2be40`（命令位置の公開資料なし） · `00b2be58`（命令位置の公開資料なし）

~~~diff
- 00b2bd50 ["INT_ADD", "register:40f0:8", ["const:b2bd50:8", "const:4:8"]]
- 00b2bd50 ["CALL", null, ["callee:00bdf480:8"]]
+ 00b2be18 ["INT_ADD", "register:40f0:8", ["const:b2be18:8", "const:4:8"]]
+ 00b2be18 ["CALL", null, ["callee:00bdf480:8"]]
- 00b2bd50 bytes a0cd0294
+ 00b2be18 bytes 9acd0294
- 00b2bd78 ["INT_ADD", "register:40f0:8", ["const:b2bd78:8", "const:4:8"]]
- 00b2bd78 ["CALL", null, ["callee:00bdf050:8"]]
+ 00b2be40 ["INT_ADD", "register:40f0:8", ["const:b2be40:8", "const:4:8"]]
+ 00b2be40 ["CALL", null, ["callee:00bdf050:8"]]
- 00b2bd78 bytes 8acc0294
+ 00b2be40 bytes 84cc0294
- 00b2bd90 ["INT_ADD", "register:40f0:8", ["const:b2bd90:8", "const:4:8"]]
- 00b2bd90 ["CALL", null, ["callee:00bdf4a0:8"]]
+ 00b2be58 ["INT_ADD", "register:40f0:8", ["const:b2be58:8", "const:4:8"]]
+ 00b2be58 ["CALL", null, ["callee:00bdf4a0:8"]]
- 00b2bd90 bytes 98cd0294
+ 00b2be58 bytes 92cd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96cb76df5c17b62361949f322878658c"></a>

### [`00b2c5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c5c0.md) → [`00b2c688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md) _ZN10reflection10CreateTypeERN11flatbuffers17FlatBufferBuilderENS_8BaseTypeES3_it

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefa0.md) · 呼出先 7件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdefd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefd0.md) [`00bdefe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefe0.md) [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md)
- 新版 呼出元 1件 [`00bdf050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf050.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf080.md) [`00bdf090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf090.md) [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2c630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c5c0.md#insn-00b2c630) · [`00b2c650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c5c0.md#insn-00b2c650) · [`00b2c6a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c5c0.md#insn-00b2c6a4)
- 新版 `00b2c6f8`（命令位置の公開資料なし） · `00b2c718`（命令位置の公開資料なし） · `00b2c76c`（命令位置の公開資料なし）

~~~diff
- 00b2c630 ["INT_ADD", "register:40f0:8", ["const:b2c630:8", "const:4:8"]]
- 00b2c630 ["CALL", null, ["callee:00bdf420:8"]]
+ 00b2c6f8 ["INT_ADD", "register:40f0:8", ["const:b2c6f8:8", "const:4:8"]]
+ 00b2c6f8 ["CALL", null, ["callee:00bdf420:8"]]
- 00b2c630 bytes 50cb0294
+ 00b2c6f8 bytes 4acb0294
- 00b2c650 ["INT_ADD", "register:40f0:8", ["const:b2c650:8", "const:4:8"]]
- 00b2c650 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b2c718 ["INT_ADD", "register:40f0:8", ["const:b2c718:8", "const:4:8"]]
+ 00b2c718 ["CALL", null, ["callee:00bdf340:8"]]
- 00b2c650 bytes 10cb0294
+ 00b2c718 bytes 0acb0294
- 00b2c6a4 ["INT_ADD", "register:40f0:8", ["const:b2c6a4:8", "const:4:8"]]
- 00b2c6a4 ["CALL", null, ["callee:00bdf370:8"]]
+ 00b2c76c ["INT_ADD", "register:40f0:8", ["const:b2c76c:8", "const:4:8"]]
+ 00b2c76c ["CALL", null, ["callee:00bdf370:8"]]
- 00b2c6a4 bytes 07cb0294
+ 00b2c76c bytes 01cb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61dec9c9b0d77838d367e60121730fe6"></a>

### [`00b31814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31814.md) → [`00b318dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b318dc.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31814.md#insn-00b31894) · [`00b318a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31814.md#insn-00b318a8)
- 新版 `00b3195c`（命令位置の公開資料なし） · `00b31970`（命令位置の公開資料なし）

~~~diff
- 00b31894 ["INT_ADD", "register:40f0:8", ["const:b31894:8", "const:4:8"]]
- 00b31894 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b3195c ["INT_ADD", "register:40f0:8", ["const:b3195c:8", "const:4:8"]]
+ 00b3195c ["CALL", null, ["callee:00bdb160:8"]]
- 00b31894 bytes 07a60294
+ 00b3195c bytes 01a60294
- 00b318a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b318a8 ["INT_ADD", "register:40f0:8", ["const:b318a8:8", "const:4:8"]]
- 00b318a8 ["CALLIND", null, ["register:0:8"]]
+ 00b31970 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31970 ["INT_ADD", "register:40f0:8", ["const:b31970:8", "const:4:8"]]
+ 00b31970 ["CALLIND", null, ["register:0:8"]]
- 00b318a8 bytes 00013fd6
+ 00b31970 bytes 00013fd6
~~~


<a id="compare-8546d6bdc6d48f2d239e91dad6c2c8f5"></a>

### [`00b3192c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b3192c.md) → [`00b319f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b319f4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5uflowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b3192c.md#insn-00b31944)
- 新版 `00b31a0c`（命令位置の公開資料なし）

~~~diff
- 00b31944 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31944 ["INT_ADD", "register:40f0:8", ["const:b31944:8", "const:4:8"]]
- 00b31944 ["CALLIND", null, ["register:0:8"]]
+ 00b31a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31a0c ["INT_ADD", "register:40f0:8", ["const:b31a0c:8", "const:4:8"]]
+ 00b31a0c ["CALLIND", null, ["register:0:8"]]
- 00b31944 bytes 00013fd6
+ 00b31a0c bytes 00013fd6
~~~


<a id="compare-958209bb5b0c10a10e61c05b42d753ef"></a>

### [`00b319dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b319dc.md) → [`00b31aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31aa4.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b319dc.md#insn-00b31a50) · [`00b31a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b319dc.md#insn-00b31a68)
- 新版 `00b31b18`（命令位置の公開資料なし） · `00b31b30`（命令位置の公開資料なし）

~~~diff
- 00b31a50 ["INT_ADD", "register:40f0:8", ["const:b31a50:8", "const:4:8"]]
- 00b31a50 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b31b18 ["INT_ADD", "register:40f0:8", ["const:b31b18:8", "const:4:8"]]
+ 00b31b18 ["CALL", null, ["callee:00bdb160:8"]]
- 00b31a50 bytes 98a50294
+ 00b31b18 bytes 92a50294
- 00b31a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31a68 ["INT_ADD", "register:40f0:8", ["const:b31a68:8", "const:4:8"]]
- 00b31a68 ["CALLIND", null, ["register:0:8"]]
+ 00b31b30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b31b30 ["INT_ADD", "register:40f0:8", ["const:b31b30:8", "const:4:8"]]
+ 00b31b30 ["CALLIND", null, ["register:0:8"]]
- 00b31a68 bytes 00013fd6
+ 00b31b30 bytes 00013fd6
~~~


<a id="compare-5d992eec726e9cfdf50e2a36cafbc983"></a>

### [`00b34930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34930.md) → [`00b349f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b349f8.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection5FieldEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf460.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf510.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34930.md#insn-00b34994) · [`00b34a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34930.md#insn-00b34a04) · [`00b34a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34930.md#insn-00b34a24)
- 新版 `00b34a5c`（命令位置の公開資料なし） · `00b34acc`（命令位置の公開資料なし） · `00b34aec`（命令位置の公開資料なし）

~~~diff
- 00b34994 ["INT_ADD", "register:40f0:8", ["const:b34994:8", "const:4:8"]]
- 00b34994 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b34a5c ["INT_ADD", "register:40f0:8", ["const:b34a5c:8", "const:4:8"]]
+ 00b34a5c ["CALL", null, ["callee:00bdf340:8"]]
- 00b34994 bytes 3faa0294
+ 00b34a5c bytes 39aa0294
- 00b34a04 ["INT_ADD", "register:40f0:8", ["const:b34a04:8", "const:4:8"]]
- 00b34a04 ["CALL", null, ["callee:00bdf430:8"]]
+ 00b34acc ["INT_ADD", "register:40f0:8", ["const:b34acc:8", "const:4:8"]]
+ 00b34acc ["CALL", null, ["callee:00bdf430:8"]]
- 00b34a04 bytes 5faa0294
+ 00b34acc bytes 59aa0294
- 00b34a24 ["INT_ADD", "register:40f0:8", ["const:b34a24:8", "const:4:8"]]
- 00b34a24 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b34aec ["INT_ADD", "register:40f0:8", ["const:b34aec:8", "const:4:8"]]
+ 00b34aec ["CALL", null, ["callee:00bdf340:8"]]
- 00b34a24 bytes 1baa0294
+ 00b34aec bytes 15aa0294
~~~


<a id="compare-9a5561348e026e37799841f1afdaf389"></a>

### [`00b34a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34a74.md) → [`00b34b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34b3c.md) _ZN10reflection12FieldBuilder7add_keyEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf020.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0d0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34a74.md#insn-00b34ab8) · [`00b34af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34a74.md#insn-00b34af0)
- 新版 `00b34b80`（命令位置の公開資料なし） · `00b34bb8`（命令位置の公開資料なし）

~~~diff
- 00b34ab8 ["INT_ADD", "register:40f0:8", ["const:b34ab8:8", "const:4:8"]]
- 00b34ab8 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b34b80 ["INT_ADD", "register:40f0:8", ["const:b34b80:8", "const:4:8"]]
+ 00b34b80 ["CALL", null, ["callee:00bdf340:8"]]
- 00b34ab8 bytes f6a90294
+ 00b34b80 bytes f0a90294
- 00b34af0 ["INT_ADD", "register:40f0:8", ["const:b34af0:8", "const:4:8"]]
- 00b34af0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b34bb8 ["INT_ADD", "register:40f0:8", ["const:b34bb8:8", "const:4:8"]]
+ 00b34bb8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b34af0 bytes e8a90294
+ 00b34bb8 bytes e2a90294
~~~


<a id="compare-48acb756d33791b2b860174cab1958b1"></a>

### [`00b34f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34f54.md) → [`00b3501c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b3501c.md) _ZN10reflection11EnumBuilder12add_is_unionEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefc0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf070.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34f54.md#insn-00b34f98) · [`00b34fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34f54.md#insn-00b34fd0)
- 新版 `00b35060`（命令位置の公開資料なし） · `00b35098`（命令位置の公開資料なし）

~~~diff
- 00b34f98 ["INT_ADD", "register:40f0:8", ["const:b34f98:8", "const:4:8"]]
- 00b34f98 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b35060 ["INT_ADD", "register:40f0:8", ["const:b35060:8", "const:4:8"]]
+ 00b35060 ["CALL", null, ["callee:00bdf340:8"]]
- 00b34f98 bytes bea80294
+ 00b35060 bytes b8a80294
- 00b34fd0 ["INT_ADD", "register:40f0:8", ["const:b34fd0:8", "const:4:8"]]
- 00b34fd0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b35098 ["INT_ADD", "register:40f0:8", ["const:b35098:8", "const:4:8"]]
+ 00b35098 ["CALL", null, ["callee:00bdf340:8"]]
- 00b34fd0 bytes b0a80294
+ 00b35098 bytes aaa80294
~~~


<a id="compare-8e8d218bd23ab0cf89ffeef8e3a1a836"></a>

### [`00b3501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3501c.md) → [`00b350e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b350e4.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7EnumValEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf480.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf530.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3501c.md#insn-00b35080) · [`00b350f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3501c.md#insn-00b350f0) · [`00b35110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3501c.md#insn-00b35110)
- 新版 `00b35148`（命令位置の公開資料なし） · `00b351b8`（命令位置の公開資料なし） · `00b351d8`（命令位置の公開資料なし）

~~~diff
- 00b35080 ["INT_ADD", "register:40f0:8", ["const:b35080:8", "const:4:8"]]
- 00b35080 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b35148 ["INT_ADD", "register:40f0:8", ["const:b35148:8", "const:4:8"]]
+ 00b35148 ["CALL", null, ["callee:00bdf340:8"]]
- 00b35080 bytes 84a80294
+ 00b35148 bytes 7ea80294
- 00b350f0 ["INT_ADD", "register:40f0:8", ["const:b350f0:8", "const:4:8"]]
- 00b350f0 ["CALL", null, ["callee:00bdf430:8"]]
+ 00b351b8 ["INT_ADD", "register:40f0:8", ["const:b351b8:8", "const:4:8"]]
+ 00b351b8 ["CALL", null, ["callee:00bdf430:8"]]
- 00b350f0 bytes a4a80294
+ 00b351b8 bytes 9ea80294
- 00b35110 ["INT_ADD", "register:40f0:8", ["const:b35110:8", "const:4:8"]]
- 00b35110 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b351d8 ["INT_ADD", "register:40f0:8", ["const:b351d8:8", "const:4:8"]]
+ 00b351d8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b35110 bytes 60a80294
+ 00b351d8 bytes 5aa80294
~~~


<a id="compare-00edf20cb4ab6701f2be3400bbaf008e"></a>

### [`00b35160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b35160.md) → [`00b35228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35228.md) _ZN10reflection11TypeBuilder11add_elementENS_8BaseTypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefd0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf080.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b351a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b35160.md#insn-00b351a8) · [`00b351e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b35160.md#insn-00b351e0)
- 新版 `00b35270`（命令位置の公開資料なし） · `00b352a8`（命令位置の公開資料なし）

~~~diff
- 00b351a8 ["INT_ADD", "register:40f0:8", ["const:b351a8:8", "const:4:8"]]
- 00b351a8 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b35270 ["INT_ADD", "register:40f0:8", ["const:b35270:8", "const:4:8"]]
+ 00b35270 ["CALL", null, ["callee:00bdf340:8"]]
- 00b351a8 bytes 3aa80294
+ 00b35270 bytes 34a80294
- 00b351e0 ["INT_ADD", "register:40f0:8", ["const:b351e0:8", "const:4:8"]]
- 00b351e0 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b352a8 ["INT_ADD", "register:40f0:8", ["const:b352a8:8", "const:4:8"]]
+ 00b352a8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b351e0 bytes 2ca80294
+ 00b352a8 bytes 26a80294
~~~


<a id="compare-7b459b3905088b04375aa6a5ea004e45"></a>

### [`00b3522c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3522c.md) → [`00b352f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b352f4.md) _ZN10reflection11TypeBuilder13add_base_typeENS_8BaseTypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdefe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdefe0.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf090.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3522c.md#insn-00b35274) · [`00b352ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b3522c.md#insn-00b352ac)
- 新版 `00b3533c`（命令位置の公開資料なし） · `00b35374`（命令位置の公開資料なし）

~~~diff
- 00b35274 ["INT_ADD", "register:40f0:8", ["const:b35274:8", "const:4:8"]]
- 00b35274 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3533c ["INT_ADD", "register:40f0:8", ["const:b3533c:8", "const:4:8"]]
+ 00b3533c ["CALL", null, ["callee:00bdf340:8"]]
- 00b35274 bytes 07a80294
+ 00b3533c bytes 01a80294
- 00b352ac ["INT_ADD", "register:40f0:8", ["const:b352ac:8", "const:4:8"]]
- 00b352ac ["CALL", null, ["callee:00bdf340:8"]]
+ 00b35374 ["INT_ADD", "register:40f0:8", ["const:b35374:8", "const:4:8"]]
+ 00b35374 ["CALL", null, ["callee:00bdf340:8"]]
- 00b352ac bytes f9a70294
+ 00b35374 bytes f3a70294
~~~


<a id="compare-bcf25ec6d651fd4cdae19e90fe13f643"></a>

### [`00b352f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b352f8.md) → [`00b353c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b353c0.md) _ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfab0.md) · 呼出先 3件 [`00bdfa70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa70.md) [`00bdfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaa0.md) [`00bdfae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfae0.md)
- 新版 呼出元 1件 [`00bdfb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) · 呼出先 3件 [`00bdfb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb20.md) [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) [`00bdfb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b354d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b352f8.md#insn-00b354d8) · [`00b35608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b352f8.md#insn-00b35608) · [`00b3589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b352f8.md#insn-00b3589c)
- 新版 `00b355a0`（命令位置の公開資料なし） · `00b356d0`（命令位置の公開資料なし） · `00b35964`（命令位置の公開資料なし）

~~~diff
- 00b354d8 ["INT_ADD", "register:40f0:8", ["const:b354d8:8", "const:4:8"]]
- 00b354d8 ["CALL", null, ["callee:00bdfb50:8"]]
+ 00b355a0 ["INT_ADD", "register:40f0:8", ["const:b355a0:8", "const:4:8"]]
+ 00b355a0 ["CALL", null, ["callee:00bdfb50:8"]]
- 00b354d8 bytes 72a90294
+ 00b355a0 bytes 6ca90294
- 00b35608 ["INT_ADD", "register:40f0:8", ["const:b35608:8", "const:4:8"]]
- 00b35608 ["CALL", null, ["callee:00bdfb20:8"]]
+ 00b356d0 ["INT_ADD", "register:40f0:8", ["const:b356d0:8", "const:4:8"]]
+ 00b356d0 ["CALL", null, ["callee:00bdfb20:8"]]
- 00b35608 bytes 1aa90294
+ 00b356d0 bytes 14a90294
- 00b3589c ["INT_ADD", "register:40f0:8", ["const:b3589c:8", "const:4:8"]]
- 00b3589c ["CALL", null, ["callee:00bdfb50:8"]]
+ 00b35964 ["INT_ADD", "register:40f0:8", ["const:b35964:8", "const:4:8"]]
+ 00b35964 ["CALL", null, ["callee:00bdfb50:8"]]
- 00b3589c bytes 81a80294
+ 00b35964 bytes 7ba80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc96d5e32fa6519ebc85aa080ff6a0c"></a>

### [`00b359f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b359f8.md) → [`00b35ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b35/00b35ac0.md) _ZNK10reflection6Object6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaa0.md) · 呼出先 2件 [`00bdfa90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa90.md) [`00bdfaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaf0.md)
- 新版 呼出元 1件 [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) · 呼出先 2件 [`00bdfb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb40.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b359f8.md#insn-00b35cb8) · [`00b35ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b35/00b359f8.md#insn-00b35ea0)
- 新版 `00b35d80`（命令位置の公開資料なし） · `00b35f68`（命令位置の公開資料なし）

~~~diff
- 00b35cb8 ["INT_ADD", "register:40f0:8", ["const:b35cb8:8", "const:4:8"]]
- 00b35cb8 ["CALL", null, ["callee:00bdfb40:8"]]
+ 00b35d80 ["INT_ADD", "register:40f0:8", ["const:b35d80:8", "const:4:8"]]
+ 00b35d80 ["CALL", null, ["callee:00bdfb40:8"]]
- 00b35cb8 bytes 76a70294
+ 00b35d80 bytes 70a70294
- 00b35ea0 ["INT_ADD", "register:40f0:8", ["const:b35ea0:8", "const:4:8"]]
- 00b35ea0 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b35f68 ["INT_ADD", "register:40f0:8", ["const:b35f68:8", "const:4:8"]]
+ 00b35f68 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b35ea0 bytes 14a70294
+ 00b35f68 bytes 0ea70294
~~~


<a id="compare-e979963867d340a1607bafd9bf3349de"></a>

### [`00b36068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36068.md) → [`00b36130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36130.md) _ZNK10reflection5Field6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa90.md) · 呼出先 2件 [`00bdfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa80.md) [`00bdfaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaf0.md)
- 新版 呼出元 1件 [`00bdfb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb40.md) · 呼出先 2件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36068.md#insn-00b36298) · [`00b36554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36068.md#insn-00b36554)
- 新版 `00b36360`（命令位置の公開資料なし） · `00b3661c`（命令位置の公開資料なし）

~~~diff
- 00b36298 ["INT_ADD", "register:40f0:8", ["const:b36298:8", "const:4:8"]]
- 00b36298 ["CALL", null, ["callee:00bdfb30:8"]]
+ 00b36360 ["INT_ADD", "register:40f0:8", ["const:b36360:8", "const:4:8"]]
+ 00b36360 ["CALL", null, ["callee:00bdfb30:8"]]
- 00b36298 bytes faa50294
+ 00b36360 bytes f4a50294
- 00b36554 ["INT_ADD", "register:40f0:8", ["const:b36554:8", "const:4:8"]]
- 00b36554 ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b3661c ["INT_ADD", "register:40f0:8", ["const:b3661c:8", "const:4:8"]]
+ 00b3661c ["CALL", null, ["callee:00bdfba0:8"]]
- 00b36554 bytes 67a50294
+ 00b3661c bytes 61a50294
~~~


<a id="compare-e6d53819175ef00e1a524d52e27cc3e9"></a>

### [`00b36b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36b18.md) → [`00b36be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b36/00b36be0.md) _ZNK10reflection4Enum6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfa70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa70.md) · 呼出先 3件 [`00bdfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa80.md) [`00bdfac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfac0.md) [`00bdfaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaf0.md)
- 新版 呼出元 1件 [`00bdfb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb20.md) · 呼出先 3件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb70.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36b18.md#insn-00b36dd8) · [`00b36ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36b18.md#insn-00b36ec0) · [`00b36fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b36/00b36b18.md#insn-00b36fec)
- 新版 `00b36ea0`（命令位置の公開資料なし） · `00b36f88`（命令位置の公開資料なし） · `00b370b4`（命令位置の公開資料なし）

~~~diff
- 00b36dd8 ["INT_ADD", "register:40f0:8", ["const:b36dd8:8", "const:4:8"]]
- 00b36dd8 ["CALL", null, ["callee:00bdfb70:8"]]
+ 00b36ea0 ["INT_ADD", "register:40f0:8", ["const:b36ea0:8", "const:4:8"]]
+ 00b36ea0 ["CALL", null, ["callee:00bdfb70:8"]]
- 00b36dd8 bytes 3aa30294
+ 00b36ea0 bytes 34a30294
- 00b36ec0 ["INT_ADD", "register:40f0:8", ["const:b36ec0:8", "const:4:8"]]
- 00b36ec0 ["CALL", null, ["callee:00bdfb30:8"]]
+ 00b36f88 ["INT_ADD", "register:40f0:8", ["const:b36f88:8", "const:4:8"]]
+ 00b36f88 ["CALL", null, ["callee:00bdfb30:8"]]
- 00b36ec0 bytes f0a20294
+ 00b36f88 bytes eaa20294
- 00b36fec ["INT_ADD", "register:40f0:8", ["const:b36fec:8", "const:4:8"]]
- 00b36fec ["CALL", null, ["callee:00bdfba0:8"]]
+ 00b370b4 ["INT_ADD", "register:40f0:8", ["const:b370b4:8", "const:4:8"]]
+ 00b370b4 ["CALL", null, ["callee:00bdfba0:8"]]
- 00b36fec bytes c1a20294
+ 00b370b4 bytes bba20294
~~~


<a id="compare-2516adc819bcc20d662d6728893b0b7c"></a>

### [`00b397c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b397c8.md) → [`00b39890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39890.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS5_EEEEvT0_SB_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc70.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0030.md)
- 新版 呼出元 1件 [`00bdfd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd20.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b397c8.md#insn-00b39804) · [`00b398a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b397c8.md#insn-00b398a0) · [`00b3991c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b397c8.md#insn-00b3991c)
- 新版 `00b398cc`（命令位置の公開資料なし） · `00b39968`（命令位置の公開資料なし） · `00b399e4`（命令位置の公開資料なし）

~~~diff
- 00b39804 ["INT_ADD", "register:40f0:8", ["const:b39804:8", "const:4:8"]]
- 00b39804 ["CALL", null, ["callee:00be00e0:8"]]
+ 00b398cc ["INT_ADD", "register:40f0:8", ["const:b398cc:8", "const:4:8"]]
+ 00b398cc ["CALL", null, ["callee:00be00e0:8"]]
- 00b39804 bytes 0b9a0294
+ 00b398cc bytes 059a0294
- 00b398a0 ["INT_ADD", "register:40f0:8", ["const:b398a0:8", "const:4:8"]]
- 00b398a0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b39968 ["INT_ADD", "register:40f0:8", ["const:b39968:8", "const:4:8"]]
+ 00b39968 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b398a0 bytes 18860294
+ 00b39968 bytes 12860294
- 00b3991c ["INT_ADD", "register:40f0:8", ["const:b3991c:8", "const:4:8"]]
- 00b3991c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b399e4 ["INT_ADD", "register:40f0:8", ["const:b399e4:8", "const:4:8"]]
+ 00b399e4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3991c bytes f9850294
+ 00b399e4 bytes f3850294
~~~


<a id="compare-9d17d2fd590ef82a4e856f432555d076"></a>

### [`00b3aaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3aaf0.md) → [`00b3abb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc40.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md)
- 新版 呼出元 1件 [`00bdfcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfcf0.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ab2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3aaf0.md#insn-00b3ab2c) · [`00b3abc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3aaf0.md#insn-00b3abc8) · [`00b3ac44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3aaf0.md#insn-00b3ac44)
- 新版 `00b3abf4`（命令位置の公開資料なし） · `00b3ac90`（命令位置の公開資料なし） · `00b3ad0c`（命令位置の公開資料なし）

~~~diff
- 00b3ab2c ["INT_ADD", "register:40f0:8", ["const:b3ab2c:8", "const:4:8"]]
- 00b3ab2c ["CALL", null, ["callee:00be00b0:8"]]
+ 00b3abf4 ["INT_ADD", "register:40f0:8", ["const:b3abf4:8", "const:4:8"]]
+ 00b3abf4 ["CALL", null, ["callee:00be00b0:8"]]
- 00b3ab2c bytes 35950294
+ 00b3abf4 bytes 2f950294
- 00b3abc8 ["INT_ADD", "register:40f0:8", ["const:b3abc8:8", "const:4:8"]]
- 00b3abc8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3ac90 ["INT_ADD", "register:40f0:8", ["const:b3ac90:8", "const:4:8"]]
+ 00b3ac90 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3abc8 bytes 4e810294
+ 00b3ac90 bytes 48810294
- 00b3ac44 ["INT_ADD", "register:40f0:8", ["const:b3ac44:8", "const:4:8"]]
- 00b3ac44 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3ad0c ["INT_ADD", "register:40f0:8", ["const:b3ad0c:8", "const:4:8"]]
+ 00b3ad0c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3ac44 bytes 2f810294
+ 00b3ad0c bytes 29810294
~~~


<a id="compare-6f9922270e559d27b3a89cf3211d05d0"></a>

### [`00b3af5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3af5c.md) → [`00b3b024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b024.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection5FieldEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2e0.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf390.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3afb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3af5c.md#insn-00b3afb8)
- 新版 `00b3b080`（命令位置の公開資料なし）

~~~diff
- 00b3afb8 ["INT_ADD", "register:40f0:8", ["const:b3afb8:8", "const:4:8"]]
- 00b3afb8 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3b080 ["INT_ADD", "register:40f0:8", ["const:b3b080:8", "const:4:8"]]
+ 00b3b080 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3afb8 bytes b6900294
+ 00b3b080 bytes b0900294
~~~


<a id="compare-6529ab2b6bead0bfb1689abb2b5e91c3"></a>

### [`00b3b9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b9bc.md) → [`00b3ba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0070.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0010.md)
- 新版 呼出元 1件 [`00be0120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0120.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b9bc.md#insn-00b3b9f0) · [`00b3ba54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b9bc.md#insn-00b3ba54) · [`00b3bacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b9bc.md#insn-00b3bacc)
- 新版 `00b3bab8`（命令位置の公開資料なし） · `00b3bb1c`（命令位置の公開資料なし） · `00b3bb94`（命令位置の公開資料なし）

~~~diff
- 00b3b9f0 ["INT_ADD", "register:40f0:8", ["const:b3b9f0:8", "const:4:8"]]
- 00b3b9f0 ["CALL", null, ["callee:00be00c0:8"]]
+ 00b3bab8 ["INT_ADD", "register:40f0:8", ["const:b3bab8:8", "const:4:8"]]
+ 00b3bab8 ["CALL", null, ["callee:00be00c0:8"]]
- 00b3b9f0 bytes 88910294
+ 00b3bab8 bytes 82910294
- 00b3ba54 ["INT_ADD", "register:40f0:8", ["const:b3ba54:8", "const:4:8"]]
- 00b3ba54 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3bb1c ["INT_ADD", "register:40f0:8", ["const:b3bb1c:8", "const:4:8"]]
+ 00b3bb1c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3ba54 bytes ab7d0294
+ 00b3bb1c bytes a57d0294
- 00b3bacc ["INT_ADD", "register:40f0:8", ["const:b3bacc:8", "const:4:8"]]
- 00b3bacc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3bb94 ["INT_ADD", "register:40f0:8", ["const:b3bb94:8", "const:4:8"]]
+ 00b3bb94 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3bacc bytes 8d7d0294
+ 00b3bb94 bytes 877d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a617ded86002062728153540f9605c69"></a>

### [`00b3cec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cec8.md) → [`00b3cf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md) FUN_00b3cf90

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b3c354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c354.md) [`00b3d2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0050.md)
- 新版 呼出元 2件 [`00b3c41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c41c.md) [`00b3d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3cf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cec8.md#insn-00b3cf04) · [`00b3cf68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cec8.md#insn-00b3cf68) · [`00b3cfe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cec8.md#insn-00b3cfe8)
- 新版 `00b3cfcc`（命令位置の公開資料なし） · `00b3d030`（命令位置の公開資料なし） · `00b3d0b0`（命令位置の公開資料なし）

~~~diff
- 00b3cf04 ["INT_ADD", "register:40f0:8", ["const:b3cf04:8", "const:4:8"]]
- 00b3cf04 ["CALL", null, ["callee:00be0100:8"]]
+ 00b3cfcc ["INT_ADD", "register:40f0:8", ["const:b3cfcc:8", "const:4:8"]]
+ 00b3cfcc ["CALL", null, ["callee:00be0100:8"]]
- 00b3cf04 bytes 538c0294
+ 00b3cfcc bytes 4d8c0294
- 00b3cf68 ["INT_ADD", "register:40f0:8", ["const:b3cf68:8", "const:4:8"]]
- 00b3cf68 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3d030 ["INT_ADD", "register:40f0:8", ["const:b3d030:8", "const:4:8"]]
+ 00b3d030 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3cf68 bytes 66780294
+ 00b3d030 bytes 60780294
- 00b3cfe8 ["INT_ADD", "register:40f0:8", ["const:b3cfe8:8", "const:4:8"]]
- 00b3cfe8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3d0b0 ["INT_ADD", "register:40f0:8", ["const:b3d0b0:8", "const:4:8"]]
+ 00b3d0b0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3cfe8 bytes 46780294
+ 00b3d0b0 bytes 40780294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0cfcfbaad1fbb2785076fdedded7c0b"></a>

### [`00b3d5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d5ac.md) → [`00b3d674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d674.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection4EnumEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2d0.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3d608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d5ac.md#insn-00b3d608)
- 新版 `00b3d6d0`（命令位置の公開資料なし）

~~~diff
- 00b3d608 ["INT_ADD", "register:40f0:8", ["const:b3d608:8", "const:4:8"]]
- 00b3d608 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3d6d0 ["INT_ADD", "register:40f0:8", ["const:b3d6d0:8", "const:4:8"]]
+ 00b3d6d0 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3d608 bytes 22870294
+ 00b3d6d0 bytes 1c870294
~~~


<a id="compare-8b878fc33fa366d0bdaf506434ad21e3"></a>

### [`00b3e8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e8d4.md) → [`00b3e99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e99c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection7ServiceEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf320.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3d0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e8d4.md#insn-00b3e930)
- 新版 `00b3e9f8`（命令位置の公開資料なし）

~~~diff
- 00b3e930 ["INT_ADD", "register:40f0:8", ["const:b3e930:8", "const:4:8"]]
- 00b3e930 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3e9f8 ["INT_ADD", "register:40f0:8", ["const:b3e9f8:8", "const:4:8"]]
+ 00b3e9f8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3e930 bytes 58820294
+ 00b3e9f8 bytes 52820294
~~~


<a id="compare-8c8ed4bb43cf54882f2428b148dcfd97"></a>

### [`00b3e9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e9a4.md) → [`00b3ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ea6c.md) _ZN11flatbuffers17FlatBufferBuilder6FinishEjPKcb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdf400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf400.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4b0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ea20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e9a4.md#insn-00b3ea20) · [`00b3ea80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e9a4.md#insn-00b3ea80) · [`00b3eadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e9a4.md#insn-00b3eadc)
- 新版 `00b3eae8`（命令位置の公開資料なし） · `00b3eb48`（命令位置の公開資料なし） · `00b3eba4`（命令位置の公開資料なし）

~~~diff
- 00b3ea20 ["INT_ADD", "register:40f0:8", ["const:b3ea20:8", "const:4:8"]]
- 00b3ea20 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3eae8 ["INT_ADD", "register:40f0:8", ["const:b3eae8:8", "const:4:8"]]
+ 00b3eae8 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3ea20 bytes 1c820294
+ 00b3eae8 bytes 16820294
- 00b3ea80 ["INT_ADD", "register:40f0:8", ["const:b3ea80:8", "const:4:8"]]
- 00b3ea80 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3eb48 ["INT_ADD", "register:40f0:8", ["const:b3eb48:8", "const:4:8"]]
+ 00b3eb48 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3ea80 bytes 04820294
+ 00b3eb48 bytes fe810294
- 00b3eadc ["INT_ADD", "register:40f0:8", ["const:b3eadc:8", "const:4:8"]]
- 00b3eadc ["CALL", null, ["callee:00bdf340:8"]]
+ 00b3eba4 ["INT_ADD", "register:40f0:8", ["const:b3eba4:8", "const:4:8"]]
+ 00b3eba4 ["CALL", null, ["callee:00bdf340:8"]]
- 00b3eadc bytes ed810294
+ 00b3eba4 bytes e7810294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7793db0fa47c457192997844c8ff6f1e"></a>

### [`00b3eb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eb80.md) → [`00b3ec48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ec48.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ebb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eb80.md#insn-00b3ebb8) · [`00b3ec0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eb80.md#insn-00b3ec0c) · [`00b3ec54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eb80.md#insn-00b3ec54)
- 新版 `00b3ec80`（命令位置の公開資料なし） · `00b3ecd4`（命令位置の公開資料なし） · `00b3ed1c`（命令位置の公開資料なし）

~~~diff
- 00b3ebb8 ["INT_ADD", "register:40f0:8", ["const:b3ebb8:8", "const:4:8"]]
- 00b3ebb8 ["CALL", null, ["callee:00bde270:8"]]
+ 00b3ec80 ["INT_ADD", "register:40f0:8", ["const:b3ec80:8", "const:4:8"]]
+ 00b3ec80 ["CALL", null, ["callee:00bde270:8"]]
- 00b3ebb8 bytes 827d0294
+ 00b3ec80 bytes 7c7d0294
- 00b3ec0c ["INT_ADD", "register:40f0:8", ["const:b3ec0c:8", "const:4:8"]]
- 00b3ec0c ["CALL", null, ["callee:00bde1d0:8"]]
+ 00b3ecd4 ["INT_ADD", "register:40f0:8", ["const:b3ecd4:8", "const:4:8"]]
+ 00b3ecd4 ["CALL", null, ["callee:00bde1d0:8"]]
- 00b3ec0c bytes 457d0294
+ 00b3ecd4 bytes 3f7d0294
- 00b3ec54 ["INT_ADD", "register:40f0:8", ["const:b3ec54:8", "const:4:8"]]
- 00b3ec54 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b3ed1c ["INT_ADD", "register:40f0:8", ["const:b3ed1c:8", "const:4:8"]]
+ 00b3ed1c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b3ec54 bytes e7700294
+ 00b3ed1c bytes e1700294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2274b27a33605c4460519fd85839baa5"></a>

### [`00b3faac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3faac.md) → [`00b3fb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fb74.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdfbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbc0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc70.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3fb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3faac.md#insn-00b3fb44) · [`00b3fb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3faac.md#insn-00b3fb8c)
- 新版 `00b3fc0c`（命令位置の公開資料なし） · `00b3fc54`（命令位置の公開資料なし）

~~~diff
- 00b3fb44 ["INT_ADD", "register:40f0:8", ["const:b3fb44:8", "const:4:8"]]
- 00b3fb44 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3fc0c ["INT_ADD", "register:40f0:8", ["const:b3fc0c:8", "const:4:8"]]
+ 00b3fc0c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3fb44 bytes 6f6d0294
+ 00b3fc0c bytes 696d0294
- 00b3fb8c ["INT_ADD", "register:40f0:8", ["const:b3fb8c:8", "const:4:8"]]
- 00b3fb8c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3fc54 ["INT_ADD", "register:40f0:8", ["const:b3fc54:8", "const:4:8"]]
+ 00b3fc54 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3fb8c bytes 5d6d0294
+ 00b3fc54 bytes 576d0294
~~~


<a id="compare-9df2259fb73ff37296e53ce76fa82446"></a>

### [`00b47b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47b2c.md) → [`00b47bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47bf4.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be01a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b47b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47b2c.md#insn-00b47b3c)
- 新版 `00b47c04`（命令位置の公開資料なし）

~~~diff
- 00b47b3c ["INT_ADD", "register:40f0:8", ["const:b47b3c:8", "const:4:8"]]
- 00b47b3c ["CALL", null, ["callee:00be0250:8"]]
+ 00b47c04 ["INT_ADD", "register:40f0:8", ["const:b47c04:8", "const:4:8"]]
+ 00b47c04 ["CALL", null, ["callee:00be0250:8"]]
- 00b47b3c bytes 99610294
+ 00b47c04 bytes 93610294
~~~


<a id="compare-6a2498832120db158c60c2458b50deb7"></a>

### [`00b4856c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b4856c.md) → [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) FUN_00b48634

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00b47d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md) [`00b47e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47e68.md) [`00b48058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48058.md) [`00b48334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48334.md) · 呼出先 1件 [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 4件 [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md) [`00b48120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48120.md) [`00b483fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md) · 呼出先 1件 [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b4856c.md#insn-00b48574)
- 新版 `00b4863c`（命令位置の公開資料なし）

~~~diff
- 00b48574 ["INT_ADD", "register:40f0:8", ["const:b48574:8", "const:4:8"]]
- 00b48574 ["CALL", null, ["callee:00bde270:8"]]
+ 00b4863c ["INT_ADD", "register:40f0:8", ["const:b4863c:8", "const:4:8"]]
+ 00b4863c ["CALL", null, ["callee:00bde270:8"]]
- 00b48574 bytes 13570294
+ 00b4863c bytes 0d570294
~~~


<a id="compare-28b861ca90a3808a30d031579e4a0b23"></a>

### [`00b48fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48fac.md) → [`00b49074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49074.md) _ZN8firebase9messaging16PollableListenerD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0280.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b48fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48fac.md#insn-00b48fbc)
- 新版 `00b49084`（命令位置の公開資料なし）

~~~diff
- 00b48fbc ["INT_ADD", "register:40f0:8", ["const:b48fbc:8", "const:4:8"]]
- 00b48fbc ["CALL", null, ["callee:00be0330:8"]]
+ 00b49084 ["INT_ADD", "register:40f0:8", ["const:b49084:8", "const:4:8"]]
+ 00b49084 ["CALL", null, ["callee:00be0330:8"]]
- 00b48fbc bytes b15c0294
+ 00b49084 bytes ab5c0294
~~~


<a id="compare-17f657ffc9d7af3f0fe3343fc1a52b37"></a>

### [`00b49400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49400.md) → [`00b494c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md) FUN_00b494c8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b48afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48afc.md) · 呼出先 3件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00be0340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0340.md) [`00be0370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md)
- 新版 呼出元 1件 [`00b48bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md) · 呼出先 3件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00be03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03f0.md) [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b49410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49400.md#insn-00b49410) · [`00b49414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49400.md#insn-00b49414)
- 新版 `00b494d8`（命令位置の公開資料なし） · `00b494dc`（命令位置の公開資料なし）

~~~diff
- 00b49410 ["INT_ADD", "register:40f0:8", ["const:b49410:8", "const:4:8"]]
- 00b49410 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b494d8 ["INT_ADD", "register:40f0:8", ["const:b494d8:8", "const:4:8"]]
+ 00b494d8 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b49410 bytes 4c520294
+ 00b494d8 bytes 46520294
- 00b49414 ["INT_ADD", "register:40f0:8", ["const:b49414:8", "const:4:8"]]
- 00b49414 ["CALL", null, ["callee:00be03f0:8"]]
+ 00b494dc ["INT_ADD", "register:40f0:8", ["const:b494dc:8", "const:4:8"]]
+ 00b494dc ["CALL", null, ["callee:00be03f0:8"]]
- 00b49414 bytes cb5b0294
+ 00b494dc bytes c55b0294
~~~


<a id="compare-e5ff1a780193fb0fd79744732af02cb8"></a>

### [`00b4b3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b3e0.md) → [`00b4b4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b4a8.md) _ZN8firebase9messaging10FileLockerC2EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be04a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4b400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b3e0.md#insn-00b4b400)
- 新版 `00b4b4c8`（命令位置の公開資料なし）

~~~diff
- 00b4b400 ["INT_ADD", "register:40f0:8", ["const:b4b400:8", "const:4:8"]]
- 00b4b400 ["CALL", null, ["callee:00be0550:8"]]
+ 00b4b4c8 ["INT_ADD", "register:40f0:8", ["const:b4b4c8:8", "const:4:8"]]
+ 00b4b4c8 ["CALL", null, ["callee:00be0550:8"]]
- 00b4b400 bytes 28540294
+ 00b4b4c8 bytes 22540294
~~~


<a id="compare-bccaa9b3f878586fa56452086e0fcfeb"></a>

### [`00b5220c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5220c.md) → [`00b522d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b522d4.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0470.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0520.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b522a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5220c.md#insn-00b522a8) · [`00b52394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5220c.md#insn-00b52394) · [`00b523d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5220c.md#insn-00b523d0)
- 新版 `00b52370`（命令位置の公開資料なし） · `00b5245c`（命令位置の公開資料なし） · `00b52498`（命令位置の公開資料なし）

~~~diff
- 00b522a8 ["INT_ADD", "register:40f0:8", ["const:b522a8:8", "const:4:8"]]
- 00b522a8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b52370 ["INT_ADD", "register:40f0:8", ["const:b52370:8", "const:4:8"]]
+ 00b52370 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b522a8 bytes 26230294
+ 00b52370 bytes 20230294
- 00b52394 ["INT_ADD", "register:40f0:8", ["const:b52394:8", "const:4:8"]]
- 00b52394 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b5245c ["INT_ADD", "register:40f0:8", ["const:b5245c:8", "const:4:8"]]
+ 00b5245c ["CALL", null, ["callee:00bdb010:8"]]
- 00b52394 bytes f3220294
+ 00b5245c bytes ed220294
- 00b523d0 ["INT_ADD", "register:40f0:8", ["const:b523d0:8", "const:4:8"]]
- 00b523d0 ["CALL", null, ["callee:00bdde60:8"]]
+ 00b52498 ["INT_ADD", "register:40f0:8", ["const:b52498:8", "const:4:8"]]
+ 00b52498 ["CALL", null, ["callee:00bdde60:8"]]
- 00b523d0 bytes 782e0294
+ 00b52498 bytes 722e0294
~~~


<a id="compare-6239ae3764d08d381c48220e1b97b775"></a>

### [`00b52bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bf0.md) → [`00b52cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cb8.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_13remote_config12RemoteConfigEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be07b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07b0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be07b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07b0.md)
- 新版 呼出元 1件 [`00be0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0860.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bf0.md#insn-00b52c0c) · [`00b52c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bf0.md#insn-00b52c18)
- 新版 `00b52cd4`（命令位置の公開資料なし） · `00b52ce0`（命令位置の公開資料なし）

~~~diff
- 00b52c0c ["INT_ADD", "register:40f0:8", ["const:b52c0c:8", "const:4:8"]]
- 00b52c0c ["CALL", null, ["callee:00be0860:8"]]
+ 00b52cd4 ["INT_ADD", "register:40f0:8", ["const:b52cd4:8", "const:4:8"]]
+ 00b52cd4 ["CALL", null, ["callee:00be0860:8"]]
- 00b52c0c bytes e9360294
+ 00b52cd4 bytes e3360294
- 00b52c18 ["INT_ADD", "register:40f0:8", ["const:b52c18:8", "const:4:8"]]
- 00b52c18 ["CALL", null, ["callee:00be0860:8"]]
+ 00b52ce0 ["INT_ADD", "register:40f0:8", ["const:b52ce0:8", "const:4:8"]]
+ 00b52ce0 ["CALL", null, ["callee:00be0860:8"]]
- 00b52c18 bytes e6360294
+ 00b52ce0 bytes e0360294
~~~


<a id="compare-8276833e4329964984ce01c4bab9d5de"></a>

### [`00b55564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55564.md) → [`00b5562c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b5562c.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0870.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0920.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b555b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55564.md#insn-00b555b4) · [`00b555f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55564.md#insn-00b555f0) · [`00b55614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55564.md#insn-00b55614)
- 新版 `00b5567c`（命令位置の公開資料なし） · `00b556b8`（命令位置の公開資料なし） · `00b556dc`（命令位置の公開資料なし）

~~~diff
- 00b555b4 ["INT_ADD", "register:40f0:8", ["const:b555b4:8", "const:4:8"]]
- 00b555b4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b5567c ["INT_ADD", "register:40f0:8", ["const:b5567c:8", "const:4:8"]]
+ 00b5567c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b555b4 bytes 63160294
+ 00b5567c bytes 5d160294
- 00b555f0 ["INT_ADD", "register:40f0:8", ["const:b555f0:8", "const:4:8"]]
- 00b555f0 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b556b8 ["INT_ADD", "register:40f0:8", ["const:b556b8:8", "const:4:8"]]
+ 00b556b8 ["CALL", null, ["callee:00bdb160:8"]]
- 00b555f0 bytes b0160294
+ 00b556b8 bytes aa160294
- 00b55614 ["INT_ADD", "register:40f0:8", ["const:b55614:8", "const:4:8"]]
- 00b55614 ["CALL", null, ["callee:00bdde60:8"]]
+ 00b556dc ["INT_ADD", "register:40f0:8", ["const:b556dc:8", "const:4:8"]]
+ 00b556dc ["CALL", null, ["callee:00bdde60:8"]]
- 00b55614 bytes e7210294
+ 00b556dc bytes e1210294
~~~


<a id="compare-0e5e407ae08b86973c575a6de5a853ee"></a>

### [`00b560ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md) → [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b57094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57094.md) [`00b5732c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b5732c.md) [`00b57a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57a40.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00be07c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07c0.md)
- 新版 呼出元 3件 [`00b5715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md) [`00b573f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md) [`00b57b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be0870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0870.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md#insn-00b56128) · [`00b56174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md#insn-00b56174) · [`00b56180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b560ec.md#insn-00b56180)
- 新版 `00b561f0`（命令位置の公開資料なし） · `00b5623c`（命令位置の公開資料なし） · `00b56248`（命令位置の公開資料なし）

~~~diff
- 00b56128 ["INT_ADD", "register:40f0:8", ["const:b56128:8", "const:4:8"]]
- 00b56128 ["CALL", null, ["callee:00be0870:8"]]
+ 00b561f0 ["INT_ADD", "register:40f0:8", ["const:b561f0:8", "const:4:8"]]
+ 00b561f0 ["CALL", null, ["callee:00be0870:8"]]
- 00b56128 bytes a6290294
+ 00b561f0 bytes a0290294
- 00b56174 ["INT_ADD", "register:40f0:8", ["const:b56174:8", "const:4:8"]]
- 00b56174 ["CALL", null, ["callee:00be0930:8"]]
+ 00b5623c ["INT_ADD", "register:40f0:8", ["const:b5623c:8", "const:4:8"]]
+ 00b5623c ["CALL", null, ["callee:00be0930:8"]]
- 00b56174 bytes c3290294
+ 00b5623c bytes bd290294
- 00b56180 ["INT_ADD", "register:40f0:8", ["const:b56180:8", "const:4:8"]]
- 00b56180 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b56248 ["INT_ADD", "register:40f0:8", ["const:b56248:8", "const:4:8"]]
+ 00b56248 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b56180 bytes 681e0294
+ 00b56248 bytes 621e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f7f30c1a84dfff399f7ff8491aa929d"></a>

### [`00b562c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b562c4.md) → [`00b5638c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5638c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0880.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md) [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md)
- 新版 呼出元 1件 [`00be0930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0930.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b56314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b562c4.md#insn-00b56314) · [`00b56340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b562c4.md#insn-00b56340) · [`00b5636c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b562c4.md#insn-00b5636c)
- 新版 `00b563dc`（命令位置の公開資料なし） · `00b56408`（命令位置の公開資料なし） · `00b56434`（命令位置の公開資料なし）

~~~diff
- 00b56314 ["INT_ADD", "register:40f0:8", ["const:b56314:8", "const:4:8"]]
- 00b56314 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b563dc ["INT_ADD", "register:40f0:8", ["const:b563dc:8", "const:4:8"]]
+ 00b563dc ["CALL", null, ["callee:00bdaff0:8"]]
- 00b56314 bytes 0b130294
+ 00b563dc bytes 05130294
- 00b56340 ["INT_ADD", "register:40f0:8", ["const:b56340:8", "const:4:8"]]
- 00b56340 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b56408 ["INT_ADD", "register:40f0:8", ["const:b56408:8", "const:4:8"]]
+ 00b56408 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b56340 bytes bc200294
+ 00b56408 bytes b6200294
- 00b5636c ["INT_ADD", "register:40f0:8", ["const:b5636c:8", "const:4:8"]]
- 00b5636c ["CALL", null, ["callee:00bdde60:8"]]
+ 00b56434 ["INT_ADD", "register:40f0:8", ["const:b56434:8", "const:4:8"]]
+ 00b56434 ["CALL", null, ["callee:00bdde60:8"]]
- 00b5636c bytes 911e0294
+ 00b56434 bytes 8b1e0294
~~~


<a id="compare-f4a2166550554de2d2996f0a0e657333"></a>

### [`00b57f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57f6c.md) → [`00b58034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58034.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0690.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be0740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0740.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57f6c.md#insn-00b57f8c) · [`00b57f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57f6c.md#insn-00b57f98) · [`00b57fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b57/00b57f6c.md#insn-00b57fa4)
- 新版 `00b58054`（命令位置の公開資料なし） · `00b58060`（命令位置の公開資料なし） · `00b5806c`（命令位置の公開資料なし）

~~~diff
- 00b57f8c ["INT_ADD", "register:40f0:8", ["const:b57f8c:8", "const:4:8"]]
- 00b57f8c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b58054 ["INT_ADD", "register:40f0:8", ["const:b58054:8", "const:4:8"]]
+ 00b58054 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b57f8c bytes e5160294
+ 00b58054 bytes df160294
- 00b57f98 ["INT_ADD", "register:40f0:8", ["const:b57f98:8", "const:4:8"]]
- 00b57f98 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b58060 ["INT_ADD", "register:40f0:8", ["const:b58060:8", "const:4:8"]]
+ 00b58060 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b57f98 bytes e6160294
+ 00b58060 bytes e0160294
- 00b57fa4 ["INT_ADD", "register:40f0:8", ["const:b57fa4:8", "const:4:8"]]
- 00b57fa4 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5806c ["INT_ADD", "register:40f0:8", ["const:b5806c:8", "const:4:8"]]
+ 00b5806c ["CALL", null, ["callee:00bdddc0:8"]]
- 00b57fa4 bytes 5b170294
+ 00b5806c bytes 55170294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c445cf466d6e80a93b94cf7209d47f6"></a>

### [`00b583c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b583c0.md) → [`00b58488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58488.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be06d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06d0.md) · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00be0780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0780.md) · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b583e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b583c0.md#insn-00b583e0) · [`00b583ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b583c0.md#insn-00b583ec) · [`00b583f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b583c0.md#insn-00b583f8)
- 新版 `00b584a8`（命令位置の公開資料なし） · `00b584b4`（命令位置の公開資料なし） · `00b584c0`（命令位置の公開資料なし）

~~~diff
- 00b583e0 ["INT_ADD", "register:40f0:8", ["const:b583e0:8", "const:4:8"]]
- 00b583e0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b584a8 ["INT_ADD", "register:40f0:8", ["const:b584a8:8", "const:4:8"]]
+ 00b584a8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b583e0 bytes d0150294
+ 00b584a8 bytes ca150294
- 00b583ec ["INT_ADD", "register:40f0:8", ["const:b583ec:8", "const:4:8"]]
- 00b583ec ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b584b4 ["INT_ADD", "register:40f0:8", ["const:b584b4:8", "const:4:8"]]
+ 00b584b4 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b583ec bytes d1150294
+ 00b584b4 bytes cb150294
- 00b583f8 ["INT_ADD", "register:40f0:8", ["const:b583f8:8", "const:4:8"]]
- 00b583f8 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b584c0 ["INT_ADD", "register:40f0:8", ["const:b584c0:8", "const:4:8"]]
+ 00b584c0 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b583f8 bytes 46160294
+ 00b584c0 bytes 40160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0650006f6a07ff673b3869519b30be3c"></a>

### [`00b58f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58f80.md) → [`00b59048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59048.md) _ZN8firebase9MutexLockD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0840.md) · 呼出先 1件 [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00be08f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08f0.md) · 呼出先 1件 [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58f80.md#insn-00b58f8c)
- 新版 `00b59054`（命令位置の公開資料なし）

~~~diff
- 00b58f8c ["INT_ADD", "register:40f0:8", ["const:b58f8c:8", "const:4:8"]]
- 00b58f8c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b59054 ["INT_ADD", "register:40f0:8", ["const:b59054:8", "const:4:8"]]
+ 00b59054 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b58f8c bytes e9120294
+ 00b59054 bytes e3120294
~~~


