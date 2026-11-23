# v15.7.2 → v15.7.3 · 最優先の変更候補 (69)

[一覧の目次](README.md)

<a id="compare-be3e67f2f67a3946951d401d8432f374"></a>

### [`00b5c000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c000.md) → [`00b5c0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c0c8.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c0f8",
      "incomplete_value": true,
      "site": "00b5c100",
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
      "definition_site": "00b5c0fc",
      "incomplete_value": false,
      "site": "00b5c100",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c000.md#insn-00b5c038) · [`00b5c020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c000.md#insn-00b5c020) · [`00b5c02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c000.md#insn-00b5c02c)
- 新版 `00b5c100`（命令位置の公開資料なし） · `00b5c0e8`（命令位置の公開資料なし） · `00b5c0f4`（命令位置の公開資料なし）

~~~diff
- 00b5c038 ["INT_ADD", "register:40f0:8", ["const:b5c038:8", "const:4:8"]]
- 00b5c038 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5c100 ["INT_ADD", "register:40f0:8", ["const:b5c100:8", "const:4:8"]]
+ 00b5c100 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5c038 bytes 36070294
+ 00b5c100 bytes 30070294
- 00b5c020 ["INT_ADD", "register:40f0:8", ["const:b5c020:8", "const:4:8"]]
- 00b5c020 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5c0e8 ["INT_ADD", "register:40f0:8", ["const:b5c0e8:8", "const:4:8"]]
+ 00b5c0e8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5c020 bytes c0060294
+ 00b5c0e8 bytes ba060294
- 00b5c02c ["INT_ADD", "register:40f0:8", ["const:b5c02c:8", "const:4:8"]]
- 00b5c02c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b5c0f4 ["INT_ADD", "register:40f0:8", ["const:b5c0f4:8", "const:4:8"]]
+ 00b5c0f4 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b5c02c bytes c1060294
+ 00b5c0f4 bytes bb060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df13e8ae6c8764056007d69b2e284ab"></a>

### [`00b5c090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c090.md) → [`00b5c158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c158.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c188",
      "incomplete_value": true,
      "site": "00b5c190",
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
      "definition_site": "00b5c18c",
      "incomplete_value": false,
      "site": "00b5c190",
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
      "definition_site": "00b5c0dc",
      "incomplete_value": true,
      "site": "00b5c0e4",
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
            "const:40:8"
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

- 旧版 [`00b5c0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c090.md#insn-00b5c0c8) · [`00b5c0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c090.md#insn-00b5c0e4) · [`00b5c0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c090.md#insn-00b5c0b0)
- 新版 `00b5c190`（命令位置の公開資料なし） · `00b5c1ac`（命令位置の公開資料なし） · `00b5c178`（命令位置の公開資料なし）

~~~diff
- 00b5c0c8 ["INT_ADD", "register:40f0:8", ["const:b5c0c8:8", "const:4:8"]]
- 00b5c0c8 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5c190 ["INT_ADD", "register:40f0:8", ["const:b5c190:8", "const:4:8"]]
+ 00b5c190 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5c0c8 bytes 12070294
+ 00b5c190 bytes 0c070294
- 00b5c0e4 ["INT_ADD", "register:40f0:8", ["const:b5c0e4:8", "const:4:8"]]
- 00b5c0e4 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b5c1ac ["INT_ADD", "register:40f0:8", ["const:b5c1ac:8", "const:4:8"]]
+ 00b5c1ac ["CALL", null, ["callee:00bddea0:8"]]
- 00b5c0e4 bytes 43070294
+ 00b5c1ac bytes 3d070294
- 00b5c0b0 ["INT_ADD", "register:40f0:8", ["const:b5c0b0:8", "const:4:8"]]
- 00b5c0b0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5c178 ["INT_ADD", "register:40f0:8", ["const:b5c178:8", "const:4:8"]]
+ 00b5c178 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5c0b0 bytes 9c060294
+ 00b5c178 bytes 96060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6de7b081116535100023ff5e051b4b"></a>

### [`00b5c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c120.md) → [`00b5c1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c1e8.md) _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c204",
      "incomplete_value": true,
      "site": "00b5c208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c13c",
      "incomplete_value": true,
      "site": "00b5c140",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c120.md#insn-00b5c140) · [`00b5c13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c120.md#insn-00b5c13c) · [`00b5c14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c120.md#insn-00b5c14c)
- 新版 `00b5c208`（命令位置の公開資料なし） · `00b5c214`（命令位置の公開資料なし）

~~~diff
- 00b5c140 ["INT_ADD", "register:40f0:8", ["const:b5c140:8", "const:4:8"]]
- 00b5c140 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5c208 ["INT_ADD", "register:40f0:8", ["const:b5c208:8", "const:4:8"]]
+ 00b5c208 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5c140 bytes 78060294
+ 00b5c208 bytes 72060294
- 00b5c13c ["COPY", "register:4000:8", ["register:40a0:8"]]
- 00b5c13c bytes e00314aa
- 00b5c14c ["INT_ADD", "register:40f0:8", ["const:b5c14c:8", "const:4:8"]]
- 00b5c14c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b5c214 ["INT_ADD", "register:40f0:8", ["const:b5c214:8", "const:4:8"]]
+ 00b5c214 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b5c14c bytes 79060294
+ 00b5c214 bytes 73060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d002723109cc3beb8c5cd743ccca2b08"></a>

### [`00b5c1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c1b0.md) → [`00b5c278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c278.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5c1e0",
      "incomplete_value": true,
      "site": "00b5c1e8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5c1e4",
      "incomplete_value": false,
      "site": "00b5c1e8",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c2bc",
      "incomplete_value": true,
      "site": "00b5c2c0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00b5c1f4",
      "incomplete_value": true,
      "site": "00b5c1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c1b0.md#insn-00b5c1e8) · [`00b5c1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c1b0.md#insn-00b5c1f8) · [`00b5c204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c1b0.md#insn-00b5c204)
- 新版 `00b5c2b0`（命令位置の公開資料なし） · `00b5c2c0`（命令位置の公開資料なし） · `00b5c2cc`（命令位置の公開資料なし）

~~~diff
- 00b5c1e8 ["INT_ADD", "register:40f0:8", ["const:b5c1e8:8", "const:4:8"]]
- 00b5c1e8 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5c2b0 ["INT_ADD", "register:40f0:8", ["const:b5c2b0:8", "const:4:8"]]
+ 00b5c2b0 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5c1e8 bytes ca060294
+ 00b5c2b0 bytes c4060294
- 00b5c1f8 ["INT_ADD", "register:40f0:8", ["const:b5c1f8:8", "const:4:8"]]
- 00b5c1f8 ["CALL", null, ["callee:00bddf40:8"]]
+ 00b5c2c0 ["INT_ADD", "register:40f0:8", ["const:b5c2c0:8", "const:4:8"]]
+ 00b5c2c0 ["CALL", null, ["callee:00bddf40:8"]]
- 00b5c1f8 bytes 26070294
+ 00b5c2c0 bytes 20070294
- 00b5c204 ["INT_ADD", "register:40f0:8", ["const:b5c204:8", "const:4:8"]]
- 00b5c204 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b5c2cc ["INT_ADD", "register:40f0:8", ["const:b5c2cc:8", "const:4:8"]]
+ 00b5c2cc ["CALL", null, ["callee:00bddea0:8"]]
- 00b5c204 bytes fb060294
+ 00b5c2cc bytes f5060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8efc59631b98ef8d91eaaffb6ab82c69"></a>

### [`00b5c240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c240.md) → [`00b5c308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c308.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c240.md#insn-00b5c260) · [`00b5c26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c240.md#insn-00b5c26c) · [`00b5c278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c240.md#insn-00b5c278)
- 新版 `00b5c328`（命令位置の公開資料なし） · `00b5c334`（命令位置の公開資料なし） · `00b5c340`（命令位置の公開資料なし）

~~~diff
- 00b5c260 ["INT_ADD", "register:40f0:8", ["const:b5c260:8", "const:4:8"]]
- 00b5c260 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5c328 ["INT_ADD", "register:40f0:8", ["const:b5c328:8", "const:4:8"]]
+ 00b5c328 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5c260 bytes 30060294
+ 00b5c328 bytes 2a060294
- 00b5c26c ["INT_ADD", "register:40f0:8", ["const:b5c26c:8", "const:4:8"]]
- 00b5c26c ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b5c334 ["INT_ADD", "register:40f0:8", ["const:b5c334:8", "const:4:8"]]
+ 00b5c334 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b5c26c bytes 31060294
+ 00b5c334 bytes 2b060294
- 00b5c278 ["INT_ADD", "register:40f0:8", ["const:b5c278:8", "const:4:8"]]
- 00b5c278 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b5c340 ["INT_ADD", "register:40f0:8", ["const:b5c340:8", "const:4:8"]]
+ 00b5c340 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b5c278 bytes a6060294
+ 00b5c340 bytes a0060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a6244a4ea6c623a83563c12840816ad"></a>

### [`00b5c2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c2d0.md) → [`00b5c398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c398.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c2d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c2d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5c398",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c39c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c3a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c2d0.md#insn-00b5c2d0) · [`00b5c2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c2d0.md#insn-00b5c2d4) · [`00b5c2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c2d0.md#insn-00b5c2d8)

~~~diff
- 00b5c2d0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c2d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c2d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c2d0 bytes f50f1df8
- 00b5c2d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c2d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c2d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c2d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c2d4 bytes f44f01a9
- 00b5c2d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c2d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c2d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c2d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c2d8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1238f6c42250adba7b71be1786a23b36"></a>

### [`00b5c378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c378.md) → [`00b5c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md) FUN_00b5c440

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b5ad5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5ad5c.md) · 呼出先 2件 [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00be0930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0930.md)
- 新版 呼出元 1件 [`00b5ae24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md) · 呼出先 2件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00be09e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c458",
      "incomplete_value": false,
      "site": "00b5c464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:306:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c390",
      "incomplete_value": false,
      "site": "00b5c39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:279:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c458",
      "PARAM",
      [
        "storage",
        "00294279",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5c458",
      "PARAM",
      [
        "storage",
        "00294306",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c378.md#insn-00b5c39c) · [`00b5c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c378.md#insn-00b5c390)
- 新版 `00b5c464`（命令位置の公開資料なし） · `00b5c458`（命令位置の公開資料なし）

~~~diff
- 00b5c39c ["INT_ADD", "register:40f0:8", ["const:b5c39c:8", "const:4:8"]]
- 00b5c39c ["CALL", null, ["callee:00bddf10:8"]]
+ 00b5c464 ["INT_ADD", "register:40f0:8", ["const:b5c464:8", "const:4:8"]]
+ 00b5c464 ["CALL", null, ["callee:00bddf10:8"]]
- 00b5c39c bytes b1060294
+ 00b5c464 bytes ab060294
- 00b5c390 ["COPY", "tmp:0:8", ["const:279:8"]]
- 00b5c390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c458 ["COPY", "tmp:0:8", ["const:306:8"]]
+ 00b5c458 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c458 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c458 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c390 bytes 00e40991
+ 00b5c458 bytes 00180c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad8b55077cd9b5a3042ded0f42519e25"></a>

### [`00b5c3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3f0.md) → [`00b5c4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c4b8.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be09f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09f0.md) · 呼出先 5件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0aa0.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c520",
      "incomplete_value": false,
      "site": "00b5c524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c458",
      "incomplete_value": false,
      "site": "00b5c45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c520",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5c520",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3f0.md#insn-00b5c45c) · [`00b5c458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3f0.md#insn-00b5c458) · [`00b5c468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c3f0.md#insn-00b5c468)
- 新版 `00b5c524`（命令位置の公開資料なし） · `00b5c520`（命令位置の公開資料なし） · `00b5c530`（命令位置の公開資料なし）

~~~diff
- 00b5c45c ["INT_ADD", "register:40f0:8", ["const:b5c45c:8", "const:4:8"]]
- 00b5c45c ["CALL", null, ["callee:00ae047c:8"]]
+ 00b5c524 ["INT_ADD", "register:40f0:8", ["const:b5c524:8", "const:4:8"]]
+ 00b5c524 ["CALL", null, ["callee:00ae047c:8"]]
- 00b5c45c bytes d60ffe97
+ 00b5c524 bytes d60ffe97
- 00b5c458 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00b5c458 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c520 ["COPY", "tmp:0:8", ["const:87d:8"]]
+ 00b5c520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 bytes 00c01f91
+ 00b5c520 bytes 00f42191
- 00b5c468 ["INT_ADD", "register:40f0:8", ["const:b5c468:8", "const:4:8"]]
- 00b5c468 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b5c530 ["INT_ADD", "register:40f0:8", ["const:b5c530:8", "const:4:8"]]
+ 00b5c530 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b5c468 bytes b6fa0194
+ 00b5c530 bytes b0fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7103183e9a73982d811b5117522822a2"></a>

### [`00b5c4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c4e8.md) → [`00b5c5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c5b0.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a10.md) · 呼出先 5件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ac0.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 87.50% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c518"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5c5e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c618",
      "incomplete_value": false,
      "site": "00b5c61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c550",
      "incomplete_value": false,
      "site": "00b5c554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c518",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c6a0"
      ]
    ],
    [
      "00b5c618",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5c5e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c6a0"
      ]
    ],
    [
      "00b5c618",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c4e8.md#insn-00b5c518) · [`00b5c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c4e8.md#insn-00b5c554)
- 新版 `00b5c61c`（命令位置の公開資料なし） · `00b5c5e0`（命令位置の公開資料なし）

~~~diff
- 00b5c518 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5c518 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b5c518 bytes 090600b5
- 00b5c554 ["INT_ADD", "register:40f0:8", ["const:b5c554:8", "const:4:8"]]
- 00b5c554 ["CALL", null, ["callee:00ae047c:8"]]
+ 00b5c61c ["INT_ADD", "register:40f0:8", ["const:b5c61c:8", "const:4:8"]]
+ 00b5c61c ["CALL", null, ["callee:00ae047c:8"]]
- 00b5c554 bytes 980ffe97
+ 00b5c61c bytes 980ffe97
+ 00b5c5e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5c5e0 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b5c5e0 bytes 090600b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b8236bf6a060cd410318230be418ca"></a>

### [`00b5c5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c5e0.md) → [`00b5c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c6a8.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be09d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09d0.md) · 呼出先 5件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a80.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 75.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5c738"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c710",
      "incomplete_value": false,
      "site": "00b5c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c648",
      "incomplete_value": false,
      "site": "00b5c64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c710",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5c710",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c5e0.md#insn-00b5c64c) · [`00b5c670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c5e0.md#insn-00b5c670)
- 新版 `00b5c714`（命令位置の公開資料なし） · `00b5c738`（命令位置の公開資料なし）

~~~diff
- 00b5c64c ["INT_ADD", "register:40f0:8", ["const:b5c64c:8", "const:4:8"]]
- 00b5c64c ["CALL", null, ["callee:00ae047c:8"]]
+ 00b5c714 ["INT_ADD", "register:40f0:8", ["const:b5c714:8", "const:4:8"]]
+ 00b5c714 ["CALL", null, ["callee:00ae047c:8"]]
- 00b5c64c bytes 5a0ffe97
+ 00b5c714 bytes 5a0ffe97
- 00b5c670 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5c670 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b5c670 ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:8:8"]]
- 00b5c670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5c670 bytes 088700f8
+ 00b5c738 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b5c738 ["COPY", "tmp:1:8", ["register:40c0:8"]]
+ 00b5c738 ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:8:8"]]
+ 00b5c738 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b5c738 bytes 088700f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-769530fcab120138fc21c2ae5787de60"></a>

### [`00b5c6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c6d8.md) → [`00b5c7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c7a0.md) _INIT_281

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aa9c.md) [`00b5aaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aaa4.md) [`00b5aaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aaa8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5ab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab64.md) [`00b5ab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab6c.md) [`00b5ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab70.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 64.86% / 新版 64.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c6f4",
      "PARAM",
      [
        "storage",
        "010a12e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5c704",
      "WRITE",
      [
        "storage",
        "010a12e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5c704",
      "DATA",
      [
        "storage",
        "002ab1a1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5c7bc",
      "PARAM",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c7cc",
      "WRITE",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c7cc",
      "DATA",
      [
        "storage",
        "002ab1a7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c6d8.md#insn-00b5c704) · [`00b5c708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c6d8.md#insn-00b5c708) · [`00b5c70c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c6d8.md#insn-00b5c70c)

~~~diff
- 00b5c704 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5c704 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b5c704 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00b5c704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c704 bytes 082400a9
- 00b5c708 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b5c708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b5c708 bytes 0a0800f9
- 00b5c70c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5c70c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5c70c ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00b5c70c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5c70c bytes 1f600039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c55aac76e56bc7fc9303e9248346918"></a>

### [`00b5c8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8d8.md) → [`00b5c9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9a0.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5c9cc",
      "incomplete_value": true,
      "site": "00b5c9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c904",
      "incomplete_value": true,
      "site": "00b5c904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5c9b4",
      "incomplete_value": true,
      "site": "00b5c9b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c8ec",
      "incomplete_value": true,
      "site": "00b5c8ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c9c0",
      "incomplete_value": false,
      "site": "00b5c9c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c8f8",
      "incomplete_value": false,
      "site": "00b5c8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c9b0",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9c0",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5c9cc",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c9b0",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9c0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5c9cc",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8d8.md#insn-00b5c8fc) · [`00b5c904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8d8.md#insn-00b5c904) · [`00b5c8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c8d8.md#insn-00b5c8e8)
- 新版 `00b5c9c4`（命令位置の公開資料なし） · `00b5c9cc`（命令位置の公開資料なし） · `00b5c9b0`（命令位置の公開資料なし）

~~~diff
- 00b5c8fc ["INT_ADD", "register:40f0:8", ["const:b5c8fc:8", "const:4:8"]]
- 00b5c8fc ["CALL", null, ["callee:00bde040:8"]]
+ 00b5c9c4 ["INT_ADD", "register:40f0:8", ["const:b5c9c4:8", "const:4:8"]]
+ 00b5c9c4 ["CALL", null, ["callee:00bde040:8"]]
- 00b5c8fc bytes a5050294
+ 00b5c9c4 bytes 9f050294
- 00b5c904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5c9cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5c9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5c904 bytes 609201f9
+ 00b5c9cc bytes 60f201f9
- 00b5c8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c8e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c9b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5c9b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c8e8 bytes 689241f9
+ 00b5c9b0 bytes 68f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b46d039f3fa06d0f1f813ac66785baa"></a>

### [`00b5c918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c918.md) → [`00b5c9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9e0.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ca0c",
      "incomplete_value": true,
      "site": "00b5ca0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c944",
      "incomplete_value": true,
      "site": "00b5c944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5c9f4",
      "incomplete_value": true,
      "site": "00b5c9f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c92c",
      "incomplete_value": true,
      "site": "00b5c92c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c9fc",
      "incomplete_value": false,
      "site": "00b5ca04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c934",
      "incomplete_value": false,
      "site": "00b5c93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c9f0",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9fc",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5ca0c",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c9f0",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9fc",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca0c",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c918.md#insn-00b5c93c) · [`00b5c944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c918.md#insn-00b5c944) · [`00b5c928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c918.md#insn-00b5c928)
- 新版 `00b5ca04`（命令位置の公開資料なし） · `00b5ca0c`（命令位置の公開資料なし） · `00b5c9f0`（命令位置の公開資料なし）

~~~diff
- 00b5c93c ["INT_ADD", "register:40f0:8", ["const:b5c93c:8", "const:4:8"]]
- 00b5c93c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5ca04 ["INT_ADD", "register:40f0:8", ["const:b5ca04:8", "const:4:8"]]
+ 00b5ca04 ["CALL", null, ["callee:00bde040:8"]]
- 00b5c93c bytes 95050294
+ 00b5ca04 bytes 8f050294
- 00b5c944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5ca0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5c944 bytes 609201f9
+ 00b5ca0c bytes 60f201f9
- 00b5c928 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c928 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c9f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5c9f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c928 bytes 689241f9
+ 00b5c9f0 bytes 68f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0b51b78bb1b18d6355be54f4ae82929"></a>

### [`00b5c958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c958.md) → [`00b5ca20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca20.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ca50",
      "incomplete_value": true,
      "site": "00b5ca50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c988",
      "incomplete_value": true,
      "site": "00b5c988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ca34",
      "incomplete_value": true,
      "site": "00b5ca34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c96c",
      "incomplete_value": true,
      "site": "00b5c96c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ca40",
      "incomplete_value": false,
      "site": "00b5ca48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c978",
      "incomplete_value": false,
      "site": "00b5c980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ca30",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca40",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5ca50",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ca30",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca40",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca50",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c958.md#insn-00b5c980) · [`00b5c988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c958.md#insn-00b5c988) · [`00b5c968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c958.md#insn-00b5c968)
- 新版 `00b5ca48`（命令位置の公開資料なし） · `00b5ca50`（命令位置の公開資料なし） · `00b5ca30`（命令位置の公開資料なし）

~~~diff
- 00b5c980 ["INT_ADD", "register:40f0:8", ["const:b5c980:8", "const:4:8"]]
- 00b5c980 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5ca48 ["INT_ADD", "register:40f0:8", ["const:b5ca48:8", "const:4:8"]]
+ 00b5ca48 ["CALL", null, ["callee:00bde040:8"]]
- 00b5c980 bytes 84050294
+ 00b5ca48 bytes 7e050294
- 00b5c988 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5ca50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5c988 bytes 609201f9
+ 00b5ca50 bytes 60f201f9
- 00b5c968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c968 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ca30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5ca30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c968 bytes 689241f9
+ 00b5ca30 bytes 68f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1580f317c5f3977a12e6c822a493f25d"></a>

### [`00b5c99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c99c.md) → [`00b5ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca64.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ca94",
      "incomplete_value": true,
      "site": "00b5ca94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9cc",
      "incomplete_value": true,
      "site": "00b5c9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ca78",
      "incomplete_value": true,
      "site": "00b5ca78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9b0",
      "incomplete_value": true,
      "site": "00b5c9b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ca80",
      "incomplete_value": false,
      "site": "00b5ca8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9b8",
      "incomplete_value": false,
      "site": "00b5c9c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ca74",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca80",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5ca94",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ca74",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca80",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca94",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c99c.md#insn-00b5c9c4) · [`00b5c9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c99c.md#insn-00b5c9cc) · [`00b5c9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c99c.md#insn-00b5c9ac)
- 新版 `00b5ca8c`（命令位置の公開資料なし） · `00b5ca94`（命令位置の公開資料なし） · `00b5ca74`（命令位置の公開資料なし）

~~~diff
- 00b5c9c4 ["INT_ADD", "register:40f0:8", ["const:b5c9c4:8", "const:4:8"]]
- 00b5c9c4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5ca8c ["INT_ADD", "register:40f0:8", ["const:b5ca8c:8", "const:4:8"]]
+ 00b5ca8c ["CALL", null, ["callee:00bde040:8"]]
- 00b5c9c4 bytes 73050294
+ 00b5ca8c bytes 6d050294
- 00b5c9cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5ca94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5c9cc bytes 609201f9
+ 00b5ca94 bytes 60f201f9
- 00b5c9ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:320:8"]]
- 00b5c9ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ca74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
+ 00b5ca74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c9ac bytes 689241f9
+ 00b5ca74 bytes 68f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a1eda372fb660d6df2259e576b90673"></a>

### [`00b5c9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c9ec.md) → [`00b5cab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cab4.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cb0c",
      "incomplete_value": true,
      "site": "00b5cb0c",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca44",
      "incomplete_value": true,
      "site": "00b5ca44",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cae8",
      "incomplete_value": true,
      "site": "00b5caf4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca20",
      "incomplete_value": true,
      "site": "00b5ca2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cac8",
      "READ",
      [
        "storage",
        "010a1328",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cae8",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb0c",
      "WRITE",
      [
        "storage",
        "010a1328",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5cac8",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cae8",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb0c",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c9ec.md#insn-00b5ca2c) · [`00b5ca44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c9ec.md#insn-00b5ca44) · [`00b5ca00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c9ec.md#insn-00b5ca00)
- 新版 `00b5caf4`（命令位置の公開資料なし） · `00b5cb0c`（命令位置の公開資料なし） · `00b5cac8`（命令位置の公開資料なし）

~~~diff
- 00b5ca2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ca2c ["INT_ADD", "register:40f0:8", ["const:b5ca2c:8", "const:4:8"]]
- 00b5ca2c ["CALLIND", null, ["register:0:8"]]
+ 00b5caf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5caf4 ["INT_ADD", "register:40f0:8", ["const:b5caf4:8", "const:4:8"]]
+ 00b5caf4 ["CALLIND", null, ["register:0:8"]]
- 00b5ca2c bytes 00013fd6
+ 00b5caf4 bytes 00013fd6
- 00b5ca44 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5ca44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:328:8"]]
- 00b5ca44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5cb0c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5cb0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3e8:8"]]
+ 00b5cb0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5ca44 bytes a0a20c39
+ 00b5cb0c bytes a0a20f39
- 00b5ca00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:328:8"]]
- 00b5ca00 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5ca00 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5cac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3e8:8"]]
+ 00b5cac8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cac8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5ca00 bytes a8a24c39
+ 00b5cac8 bytes a8a24f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ca67ef6a98feaf796756469540b0868"></a>

### [`00b5ca58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ca58.md) → [`00b5cb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb20.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cb5c",
      "incomplete_value": true,
      "site": "00b5cb5c",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca94",
      "incomplete_value": true,
      "site": "00b5ca94",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cb7c",
      "incomplete_value": true,
      "site": "00b5cb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cab4",
      "incomplete_value": true,
      "site": "00b5cab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cb38",
      "incomplete_value": true,
      "site": "00b5cb38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca70",
      "incomplete_value": true,
      "site": "00b5ca70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cb34",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb40",
      "READ",
      [
        "storage",
        "010a1328",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cb5c",
      "WRITE",
      [
        "storage",
        "010a1328",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5cb34",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb40",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cb5c",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ca58.md#insn-00b5ca94) · [`00b5cab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ca58.md#insn-00b5cab0) · [`00b5cab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ca58.md#insn-00b5cab4)
- 新版 `00b5cb5c`（命令位置の公開資料なし） · `00b5cb78`（命令位置の公開資料なし） · `00b5cb7c`（命令位置の公開資料なし）

~~~diff
- 00b5ca94 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5ca94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5ca94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:328:8"]]
- 00b5ca94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5cb5c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5cb5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5cb5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e8:8"]]
+ 00b5cb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5ca94 bytes bfa20c39
+ 00b5cb5c bytes bfa20f39
- 00b5cab0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cab0 ["INT_ADD", "register:40f0:8", ["const:b5cab0:8", "const:4:8"]]
- 00b5cab0 ["CALLIND", null, ["register:0:8"]]
+ 00b5cb78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cb78 ["INT_ADD", "register:40f0:8", ["const:b5cb78:8", "const:4:8"]]
+ 00b5cb78 ["CALLIND", null, ["register:0:8"]]
- 00b5cab0 bytes 00013fd6
+ 00b5cb78 bytes 00013fd6
- 00b5cab4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
- 00b5cab4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5cab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b5cb7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
+ 00b5cb7c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b5cb7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5cab4 bytes 9f9201f9
+ 00b5cb7c bytes 9ff201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4022c8fa556ed122a1de945518f0e40"></a>

### [`00b5cac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cac8.md) → [`00b5cb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb90.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cbd0",
      "incomplete_value": true,
      "site": "00b5cbd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb08",
      "incomplete_value": true,
      "site": "00b5cb08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cbac",
      "incomplete_value": true,
      "site": "00b5cbac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cae4",
      "incomplete_value": true,
      "site": "00b5cae4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cbb4",
      "incomplete_value": false,
      "site": "00b5cbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5caec",
      "incomplete_value": false,
      "site": "00b5cb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cba4",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbb4",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5cbd0",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cba4",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbb4",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5cbd0",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cac8.md#insn-00b5cb00) · [`00b5cb08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cac8.md#insn-00b5cb08) · [`00b5cadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cac8.md#insn-00b5cadc)
- 新版 `00b5cbc8`（命令位置の公開資料なし） · `00b5cbd0`（命令位置の公開資料なし） · `00b5cba4`（命令位置の公開資料なし）

~~~diff
- 00b5cb00 ["INT_ADD", "register:40f0:8", ["const:b5cb00:8", "const:4:8"]]
- 00b5cb00 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cbc8 ["INT_ADD", "register:40f0:8", ["const:b5cbc8:8", "const:4:8"]]
+ 00b5cbc8 ["CALL", null, ["callee:00bde040:8"]]
- 00b5cb00 bytes 24050294
+ 00b5cbc8 bytes 1e050294
- 00b5cb08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
- 00b5cb08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cbd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
+ 00b5cbd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cb08 bytes 809201f9
+ 00b5cbd0 bytes 80f201f9
- 00b5cadc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
- 00b5cadc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cba4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
+ 00b5cba4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cadc bytes 819241f9
+ 00b5cba4 bytes 81f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dac92fdb87c0151fa04ab238171faf7"></a>

### [`00b5cb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb38.md) → [`00b5cc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc00.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cc1c",
      "incomplete_value": false,
      "site": "00b5cc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb54",
      "incomplete_value": false,
      "site": "00b5cb58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5cc2c",
      "incomplete_value": true,
      "site": "00b5cc38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb64",
      "incomplete_value": true,
      "site": "00b5cb70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cc1c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5cc2c",
      "DATA",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc1c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5cc2c",
      "DATA",
      [
        "storage",
        "010a13f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb38.md#insn-00b5cb58) · [`00b5cb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb38.md#insn-00b5cb54) · [`00b5cb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb38.md#insn-00b5cb60)
- 新版 `00b5cc20`（命令位置の公開資料なし） · `00b5cc1c`（命令位置の公開資料なし） · `00b5cc28`（命令位置の公開資料なし）

~~~diff
- 00b5cb58 ["INT_ADD", "register:40f0:8", ["const:b5cb58:8", "const:4:8"]]
- 00b5cb58 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5cc20 ["INT_ADD", "register:40f0:8", ["const:b5cc20:8", "const:4:8"]]
+ 00b5cc20 ["CALL", null, ["callee:00bde130:8"]]
- 00b5cb58 bytes 4a050294
+ 00b5cc20 bytes 44050294
- 00b5cb54 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5cb54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cb54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cb54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc1c ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b5cc1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cb54 bytes 001c1591
+ 00b5cc1c bytes 00501791
- 00b5cb60 ["COPY", "tmp:0:8", ["const:330:8"]]
- 00b5cb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc28 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00b5cc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5cb60 bytes 08c10c91
+ 00b5cc28 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb88da7c1b9bc1d8ba81534575e33213"></a>

### [`00b5cb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb74.md) → [`00b5cc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc3c.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cc7c",
      "incomplete_value": true,
      "site": "00b5cc7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbb4",
      "incomplete_value": true,
      "site": "00b5cbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cc58",
      "incomplete_value": true,
      "site": "00b5cc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb90",
      "incomplete_value": true,
      "site": "00b5cb90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cc60",
      "incomplete_value": false,
      "site": "00b5cc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb98",
      "incomplete_value": false,
      "site": "00b5cbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f4b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cc50",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cc60",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5cc7c",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc50",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cc60",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5cc7c",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb74.md#insn-00b5cbac) · [`00b5cbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb74.md#insn-00b5cbb4) · [`00b5cb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cb74.md#insn-00b5cb88)
- 新版 `00b5cc74`（命令位置の公開資料なし） · `00b5cc7c`（命令位置の公開資料なし） · `00b5cc50`（命令位置の公開資料なし）

~~~diff
- 00b5cbac ["INT_ADD", "register:40f0:8", ["const:b5cbac:8", "const:4:8"]]
- 00b5cbac ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cc74 ["INT_ADD", "register:40f0:8", ["const:b5cc74:8", "const:4:8"]]
+ 00b5cc74 ["CALL", null, ["callee:00bde040:8"]]
- 00b5cbac bytes f9040294
+ 00b5cc74 bytes f3040294
- 00b5cbb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
- 00b5cbb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cc7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
+ 00b5cc7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cbb4 bytes 809201f9
+ 00b5cc7c bytes 80f201f9
- 00b5cb88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:320:8"]]
- 00b5cb88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cc50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
+ 00b5cc50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cb88 bytes 819241f9
+ 00b5cc50 bytes 81f241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d743907dc4ea7c776e8e91f527f8bf"></a>

### [`00b5cbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cbe4.md) → [`00b5ccac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ccac.md) _ZN8firebase4auth4auth10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ccc8",
      "incomplete_value": false,
      "site": "00b5cccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc00",
      "incomplete_value": false,
      "site": "00b5cc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5ccd8",
      "incomplete_value": true,
      "site": "00b5cce4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc10",
      "incomplete_value": true,
      "site": "00b5cc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ccc8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5ccd8",
      "DATA",
      [
        "storage",
        "010a13c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5ccc8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5ccd8",
      "DATA",
      [
        "storage",
        "010a1480",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cbe4.md#insn-00b5cc04) · [`00b5cc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cbe4.md#insn-00b5cc00) · [`00b5cc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cbe4.md#insn-00b5cc0c)
- 新版 `00b5cccc`（命令位置の公開資料なし） · `00b5ccc8`（命令位置の公開資料なし） · `00b5ccd4`（命令位置の公開資料なし）

~~~diff
- 00b5cc04 ["INT_ADD", "register:40f0:8", ["const:b5cc04:8", "const:4:8"]]
- 00b5cc04 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5cccc ["INT_ADD", "register:40f0:8", ["const:b5cccc:8", "const:4:8"]]
+ 00b5cccc ["CALL", null, ["callee:00bde130:8"]]
- 00b5cc04 bytes 1f050294
+ 00b5cccc bytes 19050294
- 00b5cc00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b5cc00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5ccc8 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5ccc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5ccc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5ccc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cc00 bytes 00c81791
+ 00b5ccc8 bytes 00fc1991
- 00b5cc0c ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00b5cc0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cc0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cc0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5ccd4 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00b5ccd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5ccd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5ccd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5cc0c bytes 08010f91
+ 00b5ccd4 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30896447b7e385c4a00e6a5e29d7f8be"></a>

### [`00b5cc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc20.md) → [`00b5cce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cce8.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cd14",
      "incomplete_value": true,
      "site": "00b5cd14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc4c",
      "incomplete_value": true,
      "site": "00b5cc4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ccfc",
      "incomplete_value": true,
      "site": "00b5ccfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc34",
      "incomplete_value": true,
      "site": "00b5cc34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cd08",
      "incomplete_value": false,
      "site": "00b5cd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc40",
      "incomplete_value": false,
      "site": "00b5cc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ccf8",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd08",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cd14",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ccf8",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd08",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cd14",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc20.md#insn-00b5cc44) · [`00b5cc4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc20.md#insn-00b5cc4c) · [`00b5cc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc20.md#insn-00b5cc30)
- 新版 `00b5cd0c`（命令位置の公開資料なし） · `00b5cd14`（命令位置の公開資料なし） · `00b5ccf8`（命令位置の公開資料なし）

~~~diff
- 00b5cc44 ["INT_ADD", "register:40f0:8", ["const:b5cc44:8", "const:4:8"]]
- 00b5cc44 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cd0c ["INT_ADD", "register:40f0:8", ["const:b5cd0c:8", "const:4:8"]]
+ 00b5cd0c ["CALL", null, ["callee:00bde040:8"]]
- 00b5cc44 bytes d3040294
+ 00b5cd0c bytes cd040294
- 00b5cc4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5cc4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cd14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cc4c bytes 60e601f9
+ 00b5cd14 bytes 604602f9
- 00b5cc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5cc30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ccf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5ccf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cc30 bytes 68e641f9
+ 00b5ccf8 bytes 684642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65ad99b63d356db116d2f84add4fe9e9"></a>

### [`00b5cc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc60.md) → [`00b5cd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd28.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cd54",
      "incomplete_value": true,
      "site": "00b5cd54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc8c",
      "incomplete_value": true,
      "site": "00b5cc8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cd3c",
      "incomplete_value": true,
      "site": "00b5cd3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc74",
      "incomplete_value": true,
      "site": "00b5cc74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cd44",
      "incomplete_value": false,
      "site": "00b5cd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc7c",
      "incomplete_value": false,
      "site": "00b5cc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cd38",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd44",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cd54",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cd38",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd44",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cd54",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc60.md#insn-00b5cc84) · [`00b5cc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc60.md#insn-00b5cc8c) · [`00b5cc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cc60.md#insn-00b5cc70)
- 新版 `00b5cd4c`（命令位置の公開資料なし） · `00b5cd54`（命令位置の公開資料なし） · `00b5cd38`（命令位置の公開資料なし）

~~~diff
- 00b5cc84 ["INT_ADD", "register:40f0:8", ["const:b5cc84:8", "const:4:8"]]
- 00b5cc84 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cd4c ["INT_ADD", "register:40f0:8", ["const:b5cd4c:8", "const:4:8"]]
+ 00b5cd4c ["CALL", null, ["callee:00bde040:8"]]
- 00b5cc84 bytes c3040294
+ 00b5cd4c bytes bd040294
- 00b5cc8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5cc8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cd54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cd54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cc8c bytes 60e601f9
+ 00b5cd54 bytes 604602f9
- 00b5cc70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5cc70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cd38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cd38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cc70 bytes 68e641f9
+ 00b5cd38 bytes 684642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c9aa8774915400411fe5bd47742c6c"></a>

### [`00b5cca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cca0.md) → [`00b5cd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cd98",
      "incomplete_value": true,
      "site": "00b5cd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ccd0",
      "incomplete_value": true,
      "site": "00b5ccd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cd7c",
      "incomplete_value": true,
      "site": "00b5cd7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ccb4",
      "incomplete_value": true,
      "site": "00b5ccb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cd88",
      "incomplete_value": false,
      "site": "00b5cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ccc0",
      "incomplete_value": false,
      "site": "00b5ccc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cd78",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd88",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cd98",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cd78",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd88",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cd98",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ccc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cca0.md#insn-00b5ccc8) · [`00b5ccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cca0.md#insn-00b5ccd0) · [`00b5ccb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cca0.md#insn-00b5ccb0)
- 新版 `00b5cd90`（命令位置の公開資料なし） · `00b5cd98`（命令位置の公開資料なし） · `00b5cd78`（命令位置の公開資料なし）

~~~diff
- 00b5ccc8 ["INT_ADD", "register:40f0:8", ["const:b5ccc8:8", "const:4:8"]]
- 00b5ccc8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cd90 ["INT_ADD", "register:40f0:8", ["const:b5cd90:8", "const:4:8"]]
+ 00b5cd90 ["CALL", null, ["callee:00bde040:8"]]
- 00b5ccc8 bytes b2040294
+ 00b5cd90 bytes ac040294
- 00b5ccd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5ccd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cd98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cd98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ccd0 bytes 60e601f9
+ 00b5cd98 bytes 604602f9
- 00b5ccb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5ccb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cd78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ccb0 bytes 68e641f9
+ 00b5cd78 bytes 684642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2a6334116c8a27e4c420800118b2e7e"></a>

### [`00b5cce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cce4.md) → [`00b5cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdac.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cddc",
      "incomplete_value": true,
      "site": "00b5cddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd14",
      "incomplete_value": true,
      "site": "00b5cd14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cdc0",
      "incomplete_value": true,
      "site": "00b5cdc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ccf8",
      "incomplete_value": true,
      "site": "00b5ccf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cdc8",
      "incomplete_value": false,
      "site": "00b5cdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd00",
      "incomplete_value": false,
      "site": "00b5cd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cdbc",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cdc8",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cddc",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cdbc",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cdc8",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cddc",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cce4.md#insn-00b5cd0c) · [`00b5cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cce4.md#insn-00b5cd14) · [`00b5ccf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cce4.md#insn-00b5ccf4)
- 新版 `00b5cdd4`（命令位置の公開資料なし） · `00b5cddc`（命令位置の公開資料なし） · `00b5cdbc`（命令位置の公開資料なし）

~~~diff
- 00b5cd0c ["INT_ADD", "register:40f0:8", ["const:b5cd0c:8", "const:4:8"]]
- 00b5cd0c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cdd4 ["INT_ADD", "register:40f0:8", ["const:b5cdd4:8", "const:4:8"]]
+ 00b5cdd4 ["CALL", null, ["callee:00bde040:8"]]
- 00b5cd0c bytes a1040294
+ 00b5cdd4 bytes 9b040294
- 00b5cd14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5cd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd14 bytes 60e601f9
+ 00b5cddc bytes 604602f9
- 00b5ccf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
- 00b5ccf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cdbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
+ 00b5cdbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ccf4 bytes 68e641f9
+ 00b5cdbc bytes 684642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cd166a5bf8e5c24b659e5b02a80b6c8"></a>

### [`00b5cd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cd34.md) → [`00b5cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdfc.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ce54",
      "incomplete_value": true,
      "site": "00b5ce54",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd8c",
      "incomplete_value": true,
      "site": "00b5cd8c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ce30",
      "incomplete_value": true,
      "site": "00b5ce3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd68",
      "incomplete_value": true,
      "site": "00b5cd74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ce10",
      "READ",
      [
        "storage",
        "010a13d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ce30",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce54",
      "WRITE",
      [
        "storage",
        "010a13d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5ce10",
      "READ",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ce30",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce54",
      "WRITE",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cd34.md#insn-00b5cd74) · [`00b5cd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cd34.md#insn-00b5cd8c) · [`00b5cd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cd34.md#insn-00b5cd48)
- 新版 `00b5ce3c`（命令位置の公開資料なし） · `00b5ce54`（命令位置の公開資料なし） · `00b5ce10`（命令位置の公開資料なし）

~~~diff
- 00b5cd74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cd74 ["INT_ADD", "register:40f0:8", ["const:b5cd74:8", "const:4:8"]]
- 00b5cd74 ["CALLIND", null, ["register:0:8"]]
+ 00b5ce3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ce3c ["INT_ADD", "register:40f0:8", ["const:b5ce3c:8", "const:4:8"]]
+ 00b5ce3c ["CALLIND", null, ["register:0:8"]]
- 00b5cd74 bytes 00013fd6
+ 00b5ce3c bytes 00013fd6
- 00b5cd8c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5cd8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3d0:8"]]
- 00b5cd8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5ce54 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5ce54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:490:8"]]
+ 00b5ce54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5cd8c bytes a0420f39
+ 00b5ce54 bytes a0421239
- 00b5cd48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d0:8"]]
- 00b5cd48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5cd48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5ce10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:490:8"]]
+ 00b5ce10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ce10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5cd48 bytes a8424f39
+ 00b5ce10 bytes a8425239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f578deb303df376742e5c30c6c020c1"></a>

### [`00b5cda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cda0.md) → [`00b5ce68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cea4",
      "incomplete_value": true,
      "site": "00b5cea4",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cddc",
      "incomplete_value": true,
      "site": "00b5cddc",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cec4",
      "incomplete_value": true,
      "site": "00b5cec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cdfc",
      "incomplete_value": true,
      "site": "00b5cdfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ce80",
      "incomplete_value": true,
      "site": "00b5ce80",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cdb8",
      "incomplete_value": true,
      "site": "00b5cdb8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ce7c",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce88",
      "READ",
      [
        "storage",
        "010a13d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cea4",
      "WRITE",
      [
        "storage",
        "010a13d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5ce7c",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce88",
      "READ",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cea4",
      "WRITE",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cda0.md#insn-00b5cddc) · [`00b5cdf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cda0.md#insn-00b5cdf8) · [`00b5cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cda0.md#insn-00b5cdfc)
- 新版 `00b5cea4`（命令位置の公開資料なし） · `00b5cec0`（命令位置の公開資料なし） · `00b5cec4`（命令位置の公開資料なし）

~~~diff
- 00b5cddc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5cddc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5cddc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3d0:8"]]
- 00b5cddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5cea4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5cea4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5cea4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:490:8"]]
+ 00b5cea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5cddc bytes bf420f39
+ 00b5cea4 bytes bf421239
- 00b5cdf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cdf8 ["INT_ADD", "register:40f0:8", ["const:b5cdf8:8", "const:4:8"]]
- 00b5cdf8 ["CALLIND", null, ["register:0:8"]]
+ 00b5cec0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cec0 ["INT_ADD", "register:40f0:8", ["const:b5cec0:8", "const:4:8"]]
+ 00b5cec0 ["CALLIND", null, ["register:0:8"]]
- 00b5cdf8 bytes 00013fd6
+ 00b5cec0 bytes 00013fd6
- 00b5cdfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b5cdfc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5cdfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b5cec4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
+ 00b5cec4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b5cec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5cdfc bytes 9fe601f9
+ 00b5cec4 bytes 9f4602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7d987cd7a52de7c369f04dbf477f86"></a>

### [`00b5ce10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce10.md) → [`00b5ced8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ced8.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cf18",
      "incomplete_value": true,
      "site": "00b5cf18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce50",
      "incomplete_value": true,
      "site": "00b5ce50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cef4",
      "incomplete_value": true,
      "site": "00b5cef4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce2c",
      "incomplete_value": true,
      "site": "00b5ce2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cefc",
      "incomplete_value": false,
      "site": "00b5cf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce34",
      "incomplete_value": false,
      "site": "00b5ce48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ceec",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cefc",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cf18",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ceec",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cefc",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cf18",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ce48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce10.md#insn-00b5ce48) · [`00b5ce50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce10.md#insn-00b5ce50) · [`00b5ce24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce10.md#insn-00b5ce24)
- 新版 `00b5cf10`（命令位置の公開資料なし） · `00b5cf18`（命令位置の公開資料なし） · `00b5ceec`（命令位置の公開資料なし）

~~~diff
- 00b5ce48 ["INT_ADD", "register:40f0:8", ["const:b5ce48:8", "const:4:8"]]
- 00b5ce48 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cf10 ["INT_ADD", "register:40f0:8", ["const:b5cf10:8", "const:4:8"]]
+ 00b5cf10 ["CALL", null, ["callee:00bde040:8"]]
- 00b5ce48 bytes 52040294
+ 00b5cf10 bytes 4c040294
- 00b5ce50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b5ce50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cf18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
+ 00b5cf18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ce50 bytes 80e601f9
+ 00b5cf18 bytes 804602f9
- 00b5ce24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b5ce24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ceec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
+ 00b5ceec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ce24 bytes 81e641f9
+ 00b5ceec bytes 814642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b452699c252fd4a8b07bb19d2906c3c"></a>

### [`00b5ce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce80.md) → [`00b5cf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf48.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cf64",
      "incomplete_value": false,
      "site": "00b5cf68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce9c",
      "incomplete_value": false,
      "site": "00b5cea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5cf74",
      "incomplete_value": true,
      "site": "00b5cf80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ceac",
      "incomplete_value": true,
      "site": "00b5ceb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cf64",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5cf74",
      "DATA",
      [
        "storage",
        "010a13d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cf64",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5cf74",
      "DATA",
      [
        "storage",
        "010a1498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce80.md#insn-00b5cea0) · [`00b5ce9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce80.md#insn-00b5ce9c) · [`00b5cea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5ce80.md#insn-00b5cea8)
- 新版 `00b5cf68`（命令位置の公開資料なし） · `00b5cf64`（命令位置の公開資料なし） · `00b5cf70`（命令位置の公開資料なし）

~~~diff
- 00b5cea0 ["INT_ADD", "register:40f0:8", ["const:b5cea0:8", "const:4:8"]]
- 00b5cea0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5cf68 ["INT_ADD", "register:40f0:8", ["const:b5cf68:8", "const:4:8"]]
+ 00b5cf68 ["CALL", null, ["callee:00bde130:8"]]
- 00b5cea0 bytes 78040294
+ 00b5cf68 bytes 72040294
- 00b5ce9c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5ce9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5ce9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5ce9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5cf64 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b5cf64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cf64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cf64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5ce9c bytes 001c1591
+ 00b5cf64 bytes 00501791
- 00b5cea8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00b5cea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5cf70 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00b5cf70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cf70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cf70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5cea8 bytes 08610f91
+ 00b5cf70 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-454cc4392e53ffbfc1c4ee898abee0ab"></a>

### [`00b5cebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cebc.md) → [`00b5cf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cfc4",
      "incomplete_value": true,
      "site": "00b5cfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cefc",
      "incomplete_value": true,
      "site": "00b5cefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cfa0",
      "incomplete_value": true,
      "site": "00b5cfa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ced8",
      "incomplete_value": true,
      "site": "00b5ced8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5cfa8",
      "incomplete_value": false,
      "site": "00b5cfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cee0",
      "incomplete_value": false,
      "site": "00b5cef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:40e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5cf98",
      "READ",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfa8",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cfc4",
      "WRITE",
      [
        "storage",
        "010a13c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cf98",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfa8",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cfc4",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cebc.md#insn-00b5cef4) · [`00b5cefc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cebc.md#insn-00b5cefc) · [`00b5ced0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cebc.md#insn-00b5ced0)
- 新版 `00b5cfbc`（命令位置の公開資料なし） · `00b5cfc4`（命令位置の公開資料なし） · `00b5cf98`（命令位置の公開資料なし）

~~~diff
- 00b5cef4 ["INT_ADD", "register:40f0:8", ["const:b5cef4:8", "const:4:8"]]
- 00b5cef4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5cfbc ["INT_ADD", "register:40f0:8", ["const:b5cfbc:8", "const:4:8"]]
+ 00b5cfbc ["CALL", null, ["callee:00bde040:8"]]
- 00b5cef4 bytes 27040294
+ 00b5cfbc bytes 21040294
- 00b5cefc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b5cefc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cfc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
+ 00b5cfc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cefc bytes 80e601f9
+ 00b5cfc4 bytes 804602f9
- 00b5ced0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b5ced0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cf98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
+ 00b5cf98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ced0 bytes 81e641f9
+ 00b5cf98 bytes 814642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1595ac31b47c104cfc750f44559aef32"></a>

### [`00b5cf68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf68.md) → [`00b5d030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d030.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d05c",
      "incomplete_value": true,
      "site": "00b5d05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf94",
      "incomplete_value": true,
      "site": "00b5cf94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d044",
      "incomplete_value": true,
      "site": "00b5d044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf7c",
      "incomplete_value": true,
      "site": "00b5cf7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d050",
      "incomplete_value": false,
      "site": "00b5d054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf88",
      "incomplete_value": false,
      "site": "00b5cf8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d040",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d050",
      "PARAM",
      [
        "storage",
        "002a50e8",
        null,
        "string"
      ]
    ],
    [
      "00b5d05c",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d040",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d050",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d05c",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cf8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf68.md#insn-00b5cf8c) · [`00b5cf94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf68.md#insn-00b5cf94) · [`00b5cf78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf68.md#insn-00b5cf78)
- 新版 `00b5d054`（命令位置の公開資料なし） · `00b5d05c`（命令位置の公開資料なし） · `00b5d040`（命令位置の公開資料なし）

~~~diff
- 00b5cf8c ["INT_ADD", "register:40f0:8", ["const:b5cf8c:8", "const:4:8"]]
- 00b5cf8c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d054 ["INT_ADD", "register:40f0:8", ["const:b5d054:8", "const:4:8"]]
+ 00b5d054 ["CALL", null, ["callee:00bde040:8"]]
- 00b5cf8c bytes 01040294
+ 00b5d054 bytes fb030294
- 00b5cf94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5cf94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cf94 bytes 60f601f9
+ 00b5d05c bytes 605602f9
- 00b5cf78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5cf78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d040 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cf78 bytes 68f641f9
+ 00b5d040 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a9a972f8e65448dc2372581c1796a8"></a>

### [`00b5cfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfa8.md) → [`00b5d070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d070.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d09c",
      "incomplete_value": true,
      "site": "00b5d09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfd4",
      "incomplete_value": true,
      "site": "00b5cfd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d084",
      "incomplete_value": true,
      "site": "00b5d084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfbc",
      "incomplete_value": true,
      "site": "00b5cfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d08c",
      "incomplete_value": false,
      "site": "00b5d094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfc4",
      "incomplete_value": false,
      "site": "00b5cfcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d080",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d08c",
      "PARAM",
      [
        "storage",
        "002a50e8",
        null,
        "string"
      ]
    ],
    [
      "00b5d09c",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d080",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d08c",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d09c",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cfcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfa8.md#insn-00b5cfcc) · [`00b5cfd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfa8.md#insn-00b5cfd4) · [`00b5cfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfa8.md#insn-00b5cfb8)
- 新版 `00b5d094`（命令位置の公開資料なし） · `00b5d09c`（命令位置の公開資料なし） · `00b5d080`（命令位置の公開資料なし）

~~~diff
- 00b5cfcc ["INT_ADD", "register:40f0:8", ["const:b5cfcc:8", "const:4:8"]]
- 00b5cfcc ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d094 ["INT_ADD", "register:40f0:8", ["const:b5d094:8", "const:4:8"]]
+ 00b5d094 ["CALL", null, ["callee:00bde040:8"]]
- 00b5cfcc bytes f1030294
+ 00b5d094 bytes eb030294
- 00b5cfd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5cfd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d09c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d09c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cfd4 bytes 60f601f9
+ 00b5d09c bytes 605602f9
- 00b5cfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5cfb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cfb8 bytes 68f641f9
+ 00b5d080 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aeda145dcf708b7c6f26b2e7ea7a6df"></a>

### [`00b5cfe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfe8.md) → [`00b5d0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0b0.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d018"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d0e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d0c4",
      "incomplete_value": true,
      "site": "00b5d0c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cffc",
      "incomplete_value": true,
      "site": "00b5cffc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d0c0",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d008",
      "PARAM",
      [
        "storage",
        "002a50e8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5d010",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b5d0c0",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d0d0",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d0d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfe8.md#insn-00b5cffc) · [`00b5d010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfe8.md#insn-00b5d010) · [`00b5d018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cfe8.md#insn-00b5d018)
- 新版 `00b5d0c4`（命令位置の公開資料なし）

~~~diff
- 00b5cffc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5cffc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5d0c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5d0c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5cffc bytes 080100b5
+ 00b5d0c4 bytes 080100b5
- 00b5d010 ["INT_ADD", "register:40f0:8", ["const:b5d010:8", "const:4:8"]]
- 00b5d010 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d010 bytes e0030294
- 00b5d018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5d018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d018 bytes 60f601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465156ed9dc951c4287be5ea1adc04fb"></a>

### [`00b5d02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d02c.md) → [`00b5d0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0f4.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d124",
      "incomplete_value": true,
      "site": "00b5d124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d05c",
      "incomplete_value": true,
      "site": "00b5d05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d108",
      "incomplete_value": true,
      "site": "00b5d108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d040",
      "incomplete_value": true,
      "site": "00b5d040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d110",
      "incomplete_value": false,
      "site": "00b5d11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d048",
      "incomplete_value": false,
      "site": "00b5d054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d104",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d110",
      "PARAM",
      [
        "storage",
        "002a50e8",
        null,
        "string"
      ]
    ],
    [
      "00b5d124",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d104",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d110",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d124",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d02c.md#insn-00b5d054) · [`00b5d05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d02c.md#insn-00b5d05c) · [`00b5d03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d02c.md#insn-00b5d03c)
- 新版 `00b5d11c`（命令位置の公開資料なし） · `00b5d124`（命令位置の公開資料なし） · `00b5d104`（命令位置の公開資料なし）

~~~diff
- 00b5d054 ["INT_ADD", "register:40f0:8", ["const:b5d054:8", "const:4:8"]]
- 00b5d054 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d11c ["INT_ADD", "register:40f0:8", ["const:b5d11c:8", "const:4:8"]]
+ 00b5d11c ["CALL", null, ["callee:00bde040:8"]]
- 00b5d054 bytes cf030294
+ 00b5d11c bytes c9030294
- 00b5d05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5d05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d05c bytes 60f601f9
+ 00b5d124 bytes 605602f9
- 00b5d03c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00b5d03c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00b5d104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d03c bytes 68f641f9
+ 00b5d104 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e7c5c69b8702edb9d17ff322996e07f"></a>

### [`00b5d07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d07c.md) → [`00b5d144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d144.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d19c",
      "incomplete_value": true,
      "site": "00b5d19c",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d0d4",
      "incomplete_value": true,
      "site": "00b5d0d4",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d178",
      "incomplete_value": true,
      "site": "00b5d184",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d0b0",
      "incomplete_value": true,
      "site": "00b5d0bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d158",
      "READ",
      [
        "storage",
        "010a13f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d178",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d19c",
      "WRITE",
      [
        "storage",
        "010a13f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d158",
      "READ",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d178",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d19c",
      "WRITE",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d07c.md#insn-00b5d0bc) · [`00b5d0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d07c.md#insn-00b5d0d4) · [`00b5d090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d07c.md#insn-00b5d090)
- 新版 `00b5d184`（命令位置の公開資料なし） · `00b5d19c`（命令位置の公開資料なし） · `00b5d158`（命令位置の公開資料なし）

~~~diff
- 00b5d0bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d0bc ["INT_ADD", "register:40f0:8", ["const:b5d0bc:8", "const:4:8"]]
- 00b5d0bc ["CALLIND", null, ["register:0:8"]]
+ 00b5d184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d184 ["INT_ADD", "register:40f0:8", ["const:b5d184:8", "const:4:8"]]
+ 00b5d184 ["CALLIND", null, ["register:0:8"]]
- 00b5d0bc bytes 00013fd6
+ 00b5d184 bytes 00013fd6
- 00b5d0d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5d0d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3f0:8"]]
- 00b5d0d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5d19c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5d19c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
+ 00b5d19c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5d0d4 bytes a0c20f39
+ 00b5d19c bytes a0c21239
- 00b5d090 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3f0:8"]]
- 00b5d090 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d090 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5d158 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
+ 00b5d158 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d158 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5d090 bytes a8c24f39
+ 00b5d158 bytes a8c25239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4247a613fbae2c434fecee2f606b897c"></a>

### [`00b5d0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d0e8.md) → [`00b5d1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d1b0.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d1ec",
      "incomplete_value": true,
      "site": "00b5d1ec",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d124",
      "incomplete_value": true,
      "site": "00b5d124",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d20c",
      "incomplete_value": true,
      "site": "00b5d20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d144",
      "incomplete_value": true,
      "site": "00b5d144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d1c8",
      "incomplete_value": true,
      "site": "00b5d1c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d100",
      "incomplete_value": true,
      "site": "00b5d100",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d1c4",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d1d0",
      "READ",
      [
        "storage",
        "010a13f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d1ec",
      "WRITE",
      [
        "storage",
        "010a13f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d1c4",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d1d0",
      "READ",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d1ec",
      "WRITE",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d0e8.md#insn-00b5d124) · [`00b5d140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d0e8.md#insn-00b5d140) · [`00b5d144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d0e8.md#insn-00b5d144)
- 新版 `00b5d1ec`（命令位置の公開資料なし） · `00b5d208`（命令位置の公開資料なし） · `00b5d20c`（命令位置の公開資料なし）

~~~diff
- 00b5d124 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d124 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d124 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3f0:8"]]
- 00b5d124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5d1ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5d1ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5d1ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
+ 00b5d1ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d124 bytes bfc20f39
+ 00b5d1ec bytes bfc21239
- 00b5d140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d140 ["INT_ADD", "register:40f0:8", ["const:b5d140:8", "const:4:8"]]
- 00b5d140 ["CALLIND", null, ["register:0:8"]]
+ 00b5d208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d208 ["INT_ADD", "register:40f0:8", ["const:b5d208:8", "const:4:8"]]
+ 00b5d208 ["CALLIND", null, ["register:0:8"]]
- 00b5d140 bytes 00013fd6
+ 00b5d208 bytes 00013fd6
- 00b5d144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e8:8"]]
- 00b5d144 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5d144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b5d20c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00b5d20c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b5d20c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5d144 bytes 9ff601f9
+ 00b5d20c bytes 9f5602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d03ee8b4a4b8ee09c01be64a903b6fd"></a>

### [`00b5d158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d158.md) → [`00b5d220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d220.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d260"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d174"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d16c",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d264"
      ]
    ],
    [
      "unmatched:00b5d17c",
      "PARAM",
      [
        "storage",
        "002a50e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5d234",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d23c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d264"
      ]
    ],
    [
      "00b5d244",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d158.md#insn-00b5d174) · [`00b5d190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d158.md#insn-00b5d190) · [`00b5d198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d158.md#insn-00b5d198)
- 新版 `00b5d258`（命令位置の公開資料なし）

~~~diff
- 00b5d174 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d174 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5d174 bytes 410100b5
- 00b5d190 ["INT_ADD", "register:40f0:8", ["const:b5d190:8", "const:4:8"]]
- 00b5d190 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d258 ["INT_ADD", "register:40f0:8", ["const:b5d258:8", "const:4:8"]]
+ 00b5d258 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d190 bytes 80030294
+ 00b5d258 bytes 7a030294
- 00b5d198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e8:8"]]
- 00b5d198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d198 bytes 80f601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7c5ef5e07154c49b1cbca1096251f6"></a>

### [`00b5d204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d204.md) → [`00b5d2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d2cc.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d208"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d204",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d208",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d218",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d2cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5d2d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5d2e0",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d204.md#insn-00b5d204) · [`00b5d208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d204.md#insn-00b5d208) · [`00b5d220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d204.md#insn-00b5d220)

~~~diff
- 00b5d204 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d204 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d204 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5d204 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d204 bytes f44fbea9
- 00b5d208 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d208 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d208 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d208 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d208 bytes fd7b01a9
- 00b5d220 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d220 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d220 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d7efc2170a94d27a4c58b61842c2daa"></a>

### [`00b5d274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d274.md) → [`00b5d33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d33c.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d358",
      "incomplete_value": false,
      "site": "00b5d35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d290",
      "incomplete_value": false,
      "site": "00b5d294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5d368",
      "incomplete_value": true,
      "site": "00b5d374",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d2a0",
      "incomplete_value": true,
      "site": "00b5d2ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d358",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5d368",
      "DATA",
      [
        "storage",
        "010a1408",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d358",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d368",
      "DATA",
      [
        "storage",
        "010a14c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d274.md#insn-00b5d294) · [`00b5d290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d274.md#insn-00b5d290) · [`00b5d29c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d274.md#insn-00b5d29c)
- 新版 `00b5d35c`（命令位置の公開資料なし） · `00b5d358`（命令位置の公開資料なし） · `00b5d364`（命令位置の公開資料なし）

~~~diff
- 00b5d294 ["INT_ADD", "register:40f0:8", ["const:b5d294:8", "const:4:8"]]
- 00b5d294 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5d35c ["INT_ADD", "register:40f0:8", ["const:b5d35c:8", "const:4:8"]]
+ 00b5d35c ["CALL", null, ["callee:00bde130:8"]]
- 00b5d294 bytes 7b030294
+ 00b5d35c bytes 75030294
- 00b5d290 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b5d290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d358 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5d358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d290 bytes 00c81791
+ 00b5d358 bytes 00fc1991
- 00b5d29c ["COPY", "tmp:0:8", ["const:408:8"]]
- 00b5d29c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d29c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d29c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d364 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00b5d364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d29c bytes 08211091
+ 00b5d364 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4393d9a57ec791170d8c2817678bbcce"></a>

### [`00b5d2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2b0.md) → [`00b5d378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d378.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d3a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d38c",
      "incomplete_value": true,
      "site": "00b5d38c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d2c4",
      "incomplete_value": true,
      "site": "00b5d2c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d388",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d2d0",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5d2d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b5d388",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d398",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d39c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2b0.md#insn-00b5d2d4) · [`00b5d2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2b0.md#insn-00b5d2dc)
- 新版 `00b5d39c`（命令位置の公開資料なし）

~~~diff
- 00b5d2d4 ["INT_ADD", "register:40f0:8", ["const:b5d2d4:8", "const:4:8"]]
- 00b5d2d4 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d2d4 bytes 2f030294
- 00b5d2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d2dc bytes 600a02f9
+ 00b5d39c ["INT_ADD", "register:40f0:8", ["const:b5d39c:8", "const:4:8"]]
+ 00b5d39c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d39c bytes 29030294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e596b103bf8f0874af5460bf96d84f89"></a>

### [`00b5d2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2f0.md) → [`00b5d3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3b8.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d3e4",
      "incomplete_value": true,
      "site": "00b5d3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d31c",
      "incomplete_value": true,
      "site": "00b5d31c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d3cc",
      "incomplete_value": true,
      "site": "00b5d3cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d304",
      "incomplete_value": true,
      "site": "00b5d304",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d3d4",
      "incomplete_value": false,
      "site": "00b5d3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d30c",
      "incomplete_value": false,
      "site": "00b5d314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:851:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d3c8",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d3d4",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ],
    [
      "00b5d3e4",
      "WRITE",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d3c8",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d3d4",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d3e4",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2f0.md#insn-00b5d314) · [`00b5d31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2f0.md#insn-00b5d31c) · [`00b5d300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d2f0.md#insn-00b5d300)
- 新版 `00b5d3dc`（命令位置の公開資料なし） · `00b5d3e4`（命令位置の公開資料なし） · `00b5d3c8`（命令位置の公開資料なし）

~~~diff
- 00b5d314 ["INT_ADD", "register:40f0:8", ["const:b5d314:8", "const:4:8"]]
- 00b5d314 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d3dc ["INT_ADD", "register:40f0:8", ["const:b5d3dc:8", "const:4:8"]]
+ 00b5d3dc ["CALL", null, ["callee:00bde040:8"]]
- 00b5d314 bytes 1f030294
+ 00b5d3dc bytes 19030294
- 00b5d31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d3e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
+ 00b5d3e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d31c bytes 600a02f9
+ 00b5d3e4 bytes 606a02f9
- 00b5d300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d3c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
+ 00b5d3c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d300 bytes 680a42f9
+ 00b5d3c8 bytes 686a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ff1f8217063fa246184ccc50ad610da"></a>

### [`00b5d330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d330.md) → [`00b5d3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3f8.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d428",
      "incomplete_value": true,
      "site": "00b5d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d360",
      "incomplete_value": true,
      "site": "00b5d360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d40c",
      "incomplete_value": true,
      "site": "00b5d40c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d344",
      "incomplete_value": true,
      "site": "00b5d344",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d418",
      "incomplete_value": false,
      "site": "00b5d420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d350",
      "incomplete_value": false,
      "site": "00b5d358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:851:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d408",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d418",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ],
    [
      "00b5d428",
      "WRITE",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d408",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d418",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d428",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d330.md#insn-00b5d358) · [`00b5d360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d330.md#insn-00b5d360) · [`00b5d340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d330.md#insn-00b5d340)
- 新版 `00b5d420`（命令位置の公開資料なし） · `00b5d428`（命令位置の公開資料なし） · `00b5d408`（命令位置の公開資料なし）

~~~diff
- 00b5d358 ["INT_ADD", "register:40f0:8", ["const:b5d358:8", "const:4:8"]]
- 00b5d358 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d420 ["INT_ADD", "register:40f0:8", ["const:b5d420:8", "const:4:8"]]
+ 00b5d420 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d358 bytes 0e030294
+ 00b5d420 bytes 08030294
- 00b5d360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d428 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
+ 00b5d428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d360 bytes 600a02f9
+ 00b5d428 bytes 606a02f9
- 00b5d340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
+ 00b5d408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d340 bytes 680a42f9
+ 00b5d408 bytes 686a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2548c55fbbaad26c4243a34191961d3e"></a>

### [`00b5d374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d374.md) → [`00b5d43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d43c.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d46c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d450",
      "incomplete_value": true,
      "site": "00b5d450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d388",
      "incomplete_value": true,
      "site": "00b5d388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d44c",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d390",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5d3a4",
      "WRITE",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d44c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d458",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d46c",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d374.md#insn-00b5d388) · [`00b5d39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d374.md#insn-00b5d39c) · [`00b5d3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d374.md#insn-00b5d3a4)
- 新版 `00b5d450`（命令位置の公開資料なし） · `00b5d464`（命令位置の公開資料なし）

~~~diff
- 00b5d388 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5d388 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5d450 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5d450 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d388 bytes 080100b5
+ 00b5d450 bytes 080100b5
- 00b5d39c ["INT_ADD", "register:40f0:8", ["const:b5d39c:8", "const:4:8"]]
- 00b5d39c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d464 ["INT_ADD", "register:40f0:8", ["const:b5d464:8", "const:4:8"]]
+ 00b5d464 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d39c bytes fd020294
+ 00b5d464 bytes f7020294
- 00b5d3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:410:8"]]
- 00b5d3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d3a4 bytes 600a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d326811595f818ee70ec9045e85cdf1"></a>

### [`00b5d3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d3c4.md) → [`00b5d48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d48c.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d4e4",
      "incomplete_value": true,
      "site": "00b5d4e4",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d41c",
      "incomplete_value": true,
      "site": "00b5d41c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d4c0",
      "incomplete_value": true,
      "site": "00b5d4cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:4d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d3f8",
      "incomplete_value": true,
      "site": "00b5d404",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d4a0",
      "READ",
      [
        "storage",
        "010a1418",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d4c0",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d4e4",
      "WRITE",
      [
        "storage",
        "010a1418",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d4a0",
      "READ",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d4c0",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d4e4",
      "WRITE",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d3c4.md#insn-00b5d404) · [`00b5d41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d3c4.md#insn-00b5d41c) · [`00b5d3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d3c4.md#insn-00b5d3d8)
- 新版 `00b5d4cc`（命令位置の公開資料なし） · `00b5d4e4`（命令位置の公開資料なし） · `00b5d4a0`（命令位置の公開資料なし）

~~~diff
- 00b5d404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d404 ["INT_ADD", "register:40f0:8", ["const:b5d404:8", "const:4:8"]]
- 00b5d404 ["CALLIND", null, ["register:0:8"]]
+ 00b5d4cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d4cc ["INT_ADD", "register:40f0:8", ["const:b5d4cc:8", "const:4:8"]]
+ 00b5d4cc ["CALLIND", null, ["register:0:8"]]
- 00b5d404 bytes 00013fd6
+ 00b5d4cc bytes 00013fd6
- 00b5d41c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5d41c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:418:8"]]
- 00b5d41c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5d4e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5d4e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d8:8"]]
+ 00b5d4e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5d41c bytes a0621039
+ 00b5d4e4 bytes a0621339
- 00b5d3d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:418:8"]]
- 00b5d3d8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d3d8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5d4a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d8:8"]]
+ 00b5d4a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d4a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5d3d8 bytes a8625039
+ 00b5d4a0 bytes a8625339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0310ba2352cf754754195aff27b06d"></a>

### [`00b5d430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d430.md) → [`00b5d4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d4f8.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d534",
      "incomplete_value": true,
      "site": "00b5d534",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d46c",
      "incomplete_value": true,
      "site": "00b5d46c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d554",
      "incomplete_value": true,
      "site": "00b5d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d48c",
      "incomplete_value": true,
      "site": "00b5d48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5d510",
      "incomplete_value": true,
      "site": "00b5d510",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d448",
      "incomplete_value": true,
      "site": "00b5d448",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d50c",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d518",
      "READ",
      [
        "storage",
        "010a1418",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d534",
      "WRITE",
      [
        "storage",
        "010a1418",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d50c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d518",
      "READ",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d534",
      "WRITE",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d430.md#insn-00b5d46c) · [`00b5d488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d430.md#insn-00b5d488) · [`00b5d48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d430.md#insn-00b5d48c)
- 新版 `00b5d534`（命令位置の公開資料なし） · `00b5d550`（命令位置の公開資料なし） · `00b5d554`（命令位置の公開資料なし）

~~~diff
- 00b5d46c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d46c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d46c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:418:8"]]
- 00b5d46c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5d534 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5d534 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5d534 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d8:8"]]
+ 00b5d534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d46c bytes bf621039
+ 00b5d534 bytes bf621339
- 00b5d488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d488 ["INT_ADD", "register:40f0:8", ["const:b5d488:8", "const:4:8"]]
- 00b5d488 ["CALLIND", null, ["register:0:8"]]
+ 00b5d550 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d550 ["INT_ADD", "register:40f0:8", ["const:b5d550:8", "const:4:8"]]
+ 00b5d550 ["CALLIND", null, ["register:0:8"]]
- 00b5d488 bytes 00013fd6
+ 00b5d550 bytes 00013fd6
- 00b5d48c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:410:8"]]
- 00b5d48c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5d48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b5d554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
+ 00b5d554 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b5d554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5d48c bytes 9f0a02f9
+ 00b5d554 bytes 9f6a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdb57e28df3495216b6fe3a212698911"></a>

### [`00b5d4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d4a0.md) → [`00b5d568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d568.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d5a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d4b4",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d5ac"
      ]
    ],
    [
      "unmatched:00b5d4c4",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5d57c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d5ac"
      ]
    ],
    [
      "00b5d58c",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d4bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d4a0.md#insn-00b5d4bc) · [`00b5d4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d4a0.md#insn-00b5d4d8) · [`00b5d4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d4a0.md#insn-00b5d4e0)
- 新版 `00b5d5a0`（命令位置の公開資料なし）

~~~diff
- 00b5d4bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d4bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d4bc bytes 410100b5
- 00b5d4d8 ["INT_ADD", "register:40f0:8", ["const:b5d4d8:8", "const:4:8"]]
- 00b5d4d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d5a0 ["INT_ADD", "register:40f0:8", ["const:b5d5a0:8", "const:4:8"]]
+ 00b5d5a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d4d8 bytes ae020294
+ 00b5d5a0 bytes a8020294
- 00b5d4e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:410:8"]]
- 00b5d4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d4e0 bytes 800a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e81ccdde97e058a31652e23320c810"></a>

### [`00b5d510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d510.md) → [`00b5d5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d5d8.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d5f4",
      "incomplete_value": false,
      "site": "00b5d5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d52c",
      "incomplete_value": false,
      "site": "00b5d530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5d604",
      "incomplete_value": true,
      "site": "00b5d610",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d53c",
      "incomplete_value": true,
      "site": "00b5d548",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d5f4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5d604",
      "DATA",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d5f4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5d604",
      "DATA",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d510.md#insn-00b5d530) · [`00b5d52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d510.md#insn-00b5d52c) · [`00b5d538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d510.md#insn-00b5d538)
- 新版 `00b5d5f8`（命令位置の公開資料なし） · `00b5d5f4`（命令位置の公開資料なし） · `00b5d600`（命令位置の公開資料なし）

~~~diff
- 00b5d530 ["INT_ADD", "register:40f0:8", ["const:b5d530:8", "const:4:8"]]
- 00b5d530 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5d5f8 ["INT_ADD", "register:40f0:8", ["const:b5d5f8:8", "const:4:8"]]
+ 00b5d5f8 ["CALL", null, ["callee:00bde130:8"]]
- 00b5d530 bytes d4020294
+ 00b5d5f8 bytes ce020294
- 00b5d52c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5d52c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d52c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d52c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d5f4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b5d5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d52c bytes 001c1591
+ 00b5d5f4 bytes 00501791
- 00b5d538 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00b5d538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d600 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00b5d600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d538 bytes 08811091
+ 00b5d600 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a6e9496532a666618b64305f57d88d"></a>

### [`00b5d54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d54c.md) → [`00b5d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d614.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d654"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d568"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d560",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d658"
      ]
    ],
    [
      "unmatched:00b5d570",
      "PARAM",
      [
        "storage",
        "0029a851",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5d628",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d658"
      ]
    ],
    [
      "00b5d638",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d54c.md#insn-00b5d568) · [`00b5d584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d54c.md#insn-00b5d584) · [`00b5d58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d54c.md#insn-00b5d58c)
- 新版 `00b5d64c`（命令位置の公開資料なし）

~~~diff
- 00b5d568 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d568 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5d568 bytes 410100b5
- 00b5d584 ["INT_ADD", "register:40f0:8", ["const:b5d584:8", "const:4:8"]]
- 00b5d584 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d64c ["INT_ADD", "register:40f0:8", ["const:b5d64c:8", "const:4:8"]]
+ 00b5d64c ["CALL", null, ["callee:00bde040:8"]]
- 00b5d584 bytes 83020294
+ 00b5d64c bytes 7d020294
- 00b5d58c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:410:8"]]
- 00b5d58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d58c bytes 800a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f897e03144264d0ecb7bad1830533ed"></a>

### [`00b5d5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5bc.md) → [`00b5d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d684.md) _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d6a0",
      "incomplete_value": false,
      "site": "00b5d6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d5d8",
      "incomplete_value": false,
      "site": "00b5d5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5d6b0",
      "incomplete_value": true,
      "site": "00b5d6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d5e8",
      "incomplete_value": true,
      "site": "00b5d5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d6a0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5d6b0",
      "DATA",
      [
        "storage",
        "010a1430",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d6a0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d6b0",
      "DATA",
      [
        "storage",
        "010a14f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5bc.md#insn-00b5d5dc) · [`00b5d5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5bc.md#insn-00b5d5d8) · [`00b5d5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5bc.md#insn-00b5d5e4)
- 新版 `00b5d6a4`（命令位置の公開資料なし） · `00b5d6a0`（命令位置の公開資料なし） · `00b5d6ac`（命令位置の公開資料なし）

~~~diff
- 00b5d5dc ["INT_ADD", "register:40f0:8", ["const:b5d5dc:8", "const:4:8"]]
- 00b5d5dc ["CALL", null, ["callee:00bde130:8"]]
+ 00b5d6a4 ["INT_ADD", "register:40f0:8", ["const:b5d6a4:8", "const:4:8"]]
+ 00b5d6a4 ["CALL", null, ["callee:00bde130:8"]]
- 00b5d5dc bytes a9020294
+ 00b5d6a4 bytes a3020294
- 00b5d5d8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b5d5d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d5d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d5d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6a0 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5d6a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d5d8 bytes 00c81791
+ 00b5d6a0 bytes 00fc1991
- 00b5d5e4 ["COPY", "tmp:0:8", ["const:430:8"]]
- 00b5d5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6ac ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 00b5d6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d5e4 bytes 08c11091
+ 00b5d6ac bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bc9948ad1c740a9a163daeb59d7e357"></a>

### [`00b5d5f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5f8.md) → [`00b5d6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d6c0.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b40.md) · 呼出先 3件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bf0.md) · 呼出先 3件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 18件, `call_target` 1件, `store_condition` 1件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d70c",
      "incomplete_value": true,
      "site": "00b5d70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d644",
      "incomplete_value": true,
      "site": "00b5d644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d764",
      "incomplete_value": true,
      "site": "00b5d764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d69c",
      "incomplete_value": true,
      "site": "00b5d69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d7bc",
      "incomplete_value": true,
      "site": "00b5d7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d6f4",
      "incomplete_value": true,
      "site": "00b5d6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d6dc",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d6f0",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b5d70c",
      "WRITE",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d6dc",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d6f0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5d70c",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5f8.md#insn-00b5d63c) · [`00b5d644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5f8.md#insn-00b5d644) · [`00b5d654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d5f8.md#insn-00b5d654)
- 新版 `00b5d704`（命令位置の公開資料なし） · `00b5d70c`（命令位置の公開資料なし） · `00b5d71c`（命令位置の公開資料なし）

~~~diff
- 00b5d63c ["INT_ADD", "register:40f0:8", ["const:b5d63c:8", "const:4:8"]]
- 00b5d63c ["CALL", null, ["callee:00bde040:8"]]
+ 00b5d704 ["INT_ADD", "register:40f0:8", ["const:b5d704:8", "const:4:8"]]
+ 00b5d704 ["CALL", null, ["callee:00bde040:8"]]
- 00b5d63c bytes 55020294
+ 00b5d704 bytes 4f020294
- 00b5d644 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:320:8"]]
- 00b5d644 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d70c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3e0:8"]]
+ 00b5d70c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d644 bytes c09201f9
+ 00b5d70c bytes c0f201f9
- 00b5d654 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00b5d654 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b5d654 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b5d654 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b5d71c ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00b5d71c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b5d71c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b5d71c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b5d654 bytes 42802b91
+ 00b5d71c bytes 42402e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b75e6fc43de8ab55b7309c9cb015936"></a>

### [`00b5d828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d828.md) → [`00b5d8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d8f0.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b60.md) · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c10.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 15.29% / 新版 15.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d8b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d904",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d888"
      ]
    ],
    [
      "unmatched:00b5d84c",
      "READ",
      [
        "storage",
        "010a1328",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d904",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d950"
      ]
    ],
    [
      "00b5d914",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d828.md#insn-00b5d850) · [`00b5d860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d828.md#insn-00b5d860) · [`00b5d864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d828.md#insn-00b5d864)

~~~diff
- 00b5d850 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b5d850 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5d850 bytes c8000034
- 00b5d860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d860 ["INT_ADD", "register:40f0:8", ["const:b5d860:8", "const:4:8"]]
- 00b5d860 ["CALLIND", null, ["register:0:8"]]
- 00b5d860 bytes 00013fd6
- 00b5d864 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d864 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d864 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:328:8"]]
- 00b5d864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d864 bytes bfa20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64c92eac792e8a846a21cf944108132"></a>

### [`00b5d97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d97c.md) → [`00b5da44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5da44.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b30.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5d994",
      "incomplete_value": true,
      "site": "00b5d998",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4000:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5da74",
      "incomplete_value": true,
      "site": "00b5da84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:1f8:8"
              ]
            ]
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
    "new": {
      "definition_site": "00b5da7c",
      "incomplete_value": true,
      "site": "00b5da84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5da7c",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d9f4",
      "PARAM",
      [
        "storage",
        "002a7fa1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5da7c",
      "READ",
      [
        "storage",
        "010a13f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5dabc",
      "PARAM",
      [
        "storage",
        "002a7f0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d97c.md#insn-00b5d998) · [`00b5d9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d97c.md#insn-00b5d9bc) · [`00b5d9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d97c.md#insn-00b5d9fc)
- 新版 `00b5da60`（命令位置の公開資料なし） · `00b5da84`（命令位置の公開資料なし） · `00b5dac4`（命令位置の公開資料なし）

~~~diff
- 00b5d998 ["INT_ADD", "register:40f0:8", ["const:b5d998:8", "const:4:8"]]
- 00b5d998 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b5da60 ["INT_ADD", "register:40f0:8", ["const:b5da60:8", "const:4:8"]]
+ 00b5da60 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5d998 bytes da010294
+ 00b5da60 bytes d4010294
- 00b5d9bc ["INT_ADD", "register:40f0:8", ["const:b5d9bc:8", "const:4:8"]]
- 00b5d9bc ["CALL", null, ["callee:0047495c:8"]]
+ 00b5da84 ["INT_ADD", "register:40f0:8", ["const:b5da84:8", "const:4:8"]]
+ 00b5da84 ["CALL", null, ["callee:0047495c:8"]]
- 00b5d9bc bytes e85be497
+ 00b5da84 bytes b65be497
- 00b5d9fc ["INT_ADD", "register:40f0:8", ["const:b5d9fc:8", "const:4:8"]]
- 00b5d9fc ["CALL", null, ["callee:00bde260:8"]]
+ 00b5dac4 ["INT_ADD", "register:40f0:8", ["const:b5dac4:8", "const:4:8"]]
+ 00b5dac4 ["CALL", null, ["callee:00bde260:8"]]
- 00b5d9fc bytes ed010294
+ 00b5dac4 bytes e7010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e354eb9aafc913455c78409f220e4aea"></a>

### [`00b5da38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5da38.md) → [`00b5db00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db00.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5db40",
      "incomplete_value": true,
      "site": "00b5db54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5da78",
      "incomplete_value": true,
      "site": "00b5da8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:380:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5db40",
      "READ",
      [
        "storage",
        "010a1380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5db40",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5da8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5da38.md#insn-00b5da8c) · [`00b5da58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5da38.md#insn-00b5da58) · [`00b5da6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5da38.md#insn-00b5da6c)
- 新版 `00b5db54`（命令位置の公開資料なし） · `00b5db20`（命令位置の公開資料なし） · `00b5db34`（命令位置の公開資料なし）

~~~diff
- 00b5da8c ["INT_ADD", "register:40f0:8", ["const:b5da8c:8", "const:4:8"]]
- 00b5da8c ["CALL", null, ["callee:00551e14:8"]]
+ 00b5db54 ["INT_ADD", "register:40f0:8", ["const:b5db54:8", "const:4:8"]]
+ 00b5db54 ["CALL", null, ["callee:00551e14:8"]]
- 00b5da8c bytes e2d0e797
+ 00b5db54 bytes b0d0e797
- 00b5da58 ["INT_ADD", "register:40f0:8", ["const:b5da58:8", "const:4:8"]]
- 00b5da58 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b5db20 ["INT_ADD", "register:40f0:8", ["const:b5db20:8", "const:4:8"]]
+ 00b5db20 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5da58 bytes aa010294
+ 00b5db20 bytes a4010294
- 00b5da6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5da6c ["INT_ADD", "register:40f0:8", ["const:b5da6c:8", "const:4:8"]]
- 00b5da6c ["CALLIND", null, ["register:0:8"]]
+ 00b5db34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5db34 ["INT_ADD", "register:40f0:8", ["const:b5db34:8", "const:4:8"]]
+ 00b5db34 ["CALLIND", null, ["register:0:8"]]
- 00b5da6c bytes 00013fd6
+ 00b5db34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5b6fd3c0b59317449cdcb2f3b372d85"></a>

### [`00b5dab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dab8.md) → [`00b5db80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db80.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b20.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb110.md) [`00bdc950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc950.md)
- 新版 呼出元 1件 [`00be0bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bd0.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1c0.md) [`00bdca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 16.67% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dac0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5dabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5dac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5dac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5db84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5db88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5db8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5dabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dab8.md#insn-00b5dabc) · [`00b5dac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dab8.md#insn-00b5dac0) · [`00b5dac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dab8.md#insn-00b5dac4)

~~~diff
- 00b5dabc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5dabc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5dabc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5dabc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dabc bytes f65702a9
- 00b5dac0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5dac0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5dac0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5dac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dac0 bytes f44f03a9
- 00b5dac4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5dac4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5dac4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5dac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dac4 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f523adb667336f59de1ab403b9e806a6"></a>

### [`00b5dc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dc20.md) → [`00b5dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dce8.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be08d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08d0.md) · 呼出先 21件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf20.md)
- 新版 呼出元 1件 [`00be0980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0980.md) · 呼出先 21件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.92% / 新版 86.92%

CFGの説明率　旧版 43.75% / 新版 45.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dc44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dc64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dcf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5dc44",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b5dd18",
      "READ",
      [
        "storage",
        "010a1438",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b5dc64",
      "WRITE",
      [
        "storage",
        "010a1438",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5dd0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b5dd18",
      "READ",
      [
        "storage",
        "010a14f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5dd2c",
      "WRITE",
      [
        "storage",
        "010a14f8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5dc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dc20.md#insn-00b5dc44) · [`00b5dc64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dc20.md#insn-00b5dc64) · [`00b5dc68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5dc20.md#insn-00b5dc68)

~~~diff
- 00b5dc44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b5dc44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5dc44 bytes e81f00f9
- 00b5dc64 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:438:8"]]
- 00b5dc64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b5dc64 bytes e83a04b9
- 00b5dc68 ["INT_ADD", "register:40f0:8", ["const:b5dc68:8", "const:4:8"]]
- 00b5dc68 ["CALL", null, ["callee:00bdeff0:8"]]
- 00b5dc68 bytes b6040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca672cb6cd6207201e0bcc18de604f49"></a>

### [`00b5de5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5de5c.md) → [`00b5df24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5df24.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0940.md) · 呼出先 6件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00be0b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b20.md) [`00be0b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b30.md)
- 新版 呼出元 1件 [`00be09f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09f0.md) · 呼出先 6件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bd0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5df48",
      "incomplete_value": true,
      "site": "00b5df58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5de80",
      "incomplete_value": true,
      "site": "00b5de90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5df4c",
      "incomplete_value": true,
      "site": "00b5df58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5de84",
      "incomplete_value": true,
      "site": "00b5de90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5df68",
      "incomplete_value": true,
      "site": "00b5df78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dea0",
      "incomplete_value": true,
      "site": "00b5deb0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:358:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5de80",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5de84",
      "READ",
      [
        "storage",
        "010a13f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5dea0",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5df48",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5df4c",
      "READ",
      [
        "storage",
        "010a14b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5df68",
      "READ",
      [
        "storage",
        "010a1418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5de5c.md#insn-00b5de90) · [`00b5deb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5de5c.md#insn-00b5deb0) · [`00b5dedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5de5c.md#insn-00b5dedc)
- 新版 `00b5df58`（命令位置の公開資料なし） · `00b5df78`（命令位置の公開資料なし） · `00b5dfa4`（命令位置の公開資料なし）

~~~diff
- 00b5de90 ["INT_ADD", "register:40f0:8", ["const:b5de90:8", "const:4:8"]]
- 00b5de90 ["CALL", null, ["callee:0056681c:8"]]
+ 00b5df58 ["INT_ADD", "register:40f0:8", ["const:b5df58:8", "const:4:8"]]
+ 00b5df58 ["CALL", null, ["callee:0056681c:8"]]
- 00b5de90 bytes 6322e897
+ 00b5df58 bytes 3122e897
- 00b5deb0 ["INT_ADD", "register:40f0:8", ["const:b5deb0:8", "const:4:8"]]
- 00b5deb0 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5df78 ["INT_ADD", "register:40f0:8", ["const:b5df78:8", "const:4:8"]]
+ 00b5df78 ["CALL", null, ["callee:00551e14:8"]]
- 00b5deb0 bytes d9cfe797
+ 00b5df78 bytes a7cfe797
- 00b5dedc ["INT_ADD", "register:40f0:8", ["const:b5dedc:8", "const:4:8"]]
- 00b5dedc ["CALL", null, ["callee:0056681c:8"]]
+ 00b5dfa4 ["INT_ADD", "register:40f0:8", ["const:b5dfa4:8", "const:4:8"]]
+ 00b5dfa4 ["CALL", null, ["callee:0056681c:8"]]
- 00b5dedc bytes 5022e897
+ 00b5dfa4 bytes 1e22e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5219fdbefb19679a8f83932ac5875c"></a>

### [`00b5df24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md) → [`00b5dfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dfec.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0950.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md) [`00bde050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde050.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00be0a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a00.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5e0f4",
      "incomplete_value": true,
      "site": "00b5e0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e02c",
      "incomplete_value": true,
      "site": "00b5e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5df74",
      "incomplete_value": true,
      "site": "00b5df7c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5df6c",
      "incomplete_value": true,
      "site": "00b5df7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e038",
      "READ",
      [
        "storage",
        "010a1400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5df8c",
      "READ",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e070",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5e038",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e054",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e070",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5df64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md#insn-00b5df64) · [`00b5df7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md#insn-00b5df7c) · [`00b5df9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md#insn-00b5df9c)
- 新版 `00b5e02c`（命令位置の公開資料なし） · `00b5e044`（命令位置の公開資料なし） · `00b5e064`（命令位置の公開資料なし）

~~~diff
- 00b5df64 ["INT_ADD", "register:40f0:8", ["const:b5df64:8", "const:4:8"]]
- 00b5df64 ["CALL", null, ["callee:00bde030:8"]]
+ 00b5e02c ["INT_ADD", "register:40f0:8", ["const:b5e02c:8", "const:4:8"]]
+ 00b5e02c ["CALL", null, ["callee:00bde030:8"]]
- 00b5df64 bytes 07000294
+ 00b5e02c bytes 01000294
- 00b5df7c ["INT_ADD", "register:40f0:8", ["const:b5df7c:8", "const:4:8"]]
- 00b5df7c ["CALL", null, ["callee:00551e14:8"]]
+ 00b5e044 ["INT_ADD", "register:40f0:8", ["const:b5e044:8", "const:4:8"]]
+ 00b5e044 ["CALL", null, ["callee:00551e14:8"]]
- 00b5df7c bytes a6cfe797
+ 00b5e044 bytes 74cfe797
- 00b5df9c ["INT_ADD", "register:40f0:8", ["const:b5df9c:8", "const:4:8"]]
- 00b5df9c ["CALL", null, ["callee:00551e14:8"]]
+ 00b5e064 ["INT_ADD", "register:40f0:8", ["const:b5e064:8", "const:4:8"]]
+ 00b5e064 ["CALL", null, ["callee:00551e14:8"]]
- 00b5df9c bytes 9ecfe797
+ 00b5e064 bytes 6ccfe797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aa6aec8ce467c7b32f65117535b98da"></a>

### [`00b5e080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e080.md) → [`00b5e148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e148.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0890.md) · 呼出先 5件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bdef40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef40.md) [`00be0980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0980.md)
- 新版 呼出元 1件 [`00be0940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0940.md) · 呼出先 5件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bdeff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeff0.md) [`00be0a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a30.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e180",
      "incomplete_value": true,
      "site": "00b5e194",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e0b8",
      "incomplete_value": true,
      "site": "00b5e0cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              [
                "leaf",
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e184",
      "incomplete_value": true,
      "site": "00b5e194",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e0bc",
      "incomplete_value": true,
      "site": "00b5e0cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e0b8",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5e0bc",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5e104",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5e180",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e184",
      "READ",
      [
        "storage",
        "010a13f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e1cc",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e080.md#insn-00b5e0cc) · [`00b5e09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e080.md#insn-00b5e09c) · [`00b5e0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e080.md#insn-00b5e0a8)
- 新版 `00b5e194`（命令位置の公開資料なし） · `00b5e164`（命令位置の公開資料なし） · `00b5e170`（命令位置の公開資料なし）

~~~diff
- 00b5e0cc ["INT_ADD", "register:40f0:8", ["const:b5e0cc:8", "const:4:8"]]
- 00b5e0cc ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b5e194 ["INT_ADD", "register:40f0:8", ["const:b5e194:8", "const:4:8"]]
+ 00b5e194 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b5e0cc bytes ddfe0194
+ 00b5e194 bytes d7fe0194
- 00b5e09c ["INT_ADD", "register:40f0:8", ["const:b5e09c:8", "const:4:8"]]
- 00b5e09c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b5e164 ["INT_ADD", "register:40f0:8", ["const:b5e164:8", "const:4:8"]]
+ 00b5e164 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5e09c bytes 19000294
+ 00b5e164 bytes 13000294
- 00b5e0a8 ["INT_ADD", "register:40f0:8", ["const:b5e0a8:8", "const:4:8"]]
- 00b5e0a8 ["CALL", null, ["callee:00be0a30:8"]]
+ 00b5e170 ["INT_ADD", "register:40f0:8", ["const:b5e170:8", "const:4:8"]]
+ 00b5e170 ["CALL", null, ["callee:00be0a30:8"]]
- 00b5e0a8 bytes 360a0294
+ 00b5e170 bytes 300a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5905d9415626c1f5f7f807a55b6afdb"></a>

### [`00b5e17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md) → [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b5e480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e480.md) [`00b5fe6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fe6c.md) [`00b5fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fff8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b5e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e548.md) [`00b5ff34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ff34.md) [`00b600c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b600c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 15.38% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5e364",
      "incomplete_value": false,
      "site": "00b5e364",
      "value": [
        "leaf",
        "const:b5e548:8"
      ]
    },
    "old": {
      "definition_site": "00b5e29c",
      "incomplete_value": false,
      "site": "00b5e29c",
      "value": [
        "leaf",
        "const:b5e480:8"
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e310"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5e3d8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e294",
      "READ",
      [
        "storage",
        "00c1bac0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e294",
      "PARAM",
      [
        "storage",
        "00b5fe6c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00b5e220",
      "READ",
      [
        "storage",
        "010a1388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5e294",
      "READ",
      [
        "storage",
        "00c1bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e294",
      "PARAM",
      [
        "storage",
        "00b5ff34",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      "00b5e2e8",
      "READ",
      [
        "storage",
        "010a1448",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md#insn-00b5e1e0) · [`00b5e234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md#insn-00b5e234) · [`00b5e24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md#insn-00b5e24c)
- 新版 `00b5e2a8`（命令位置の公開資料なし） · `00b5e2fc`（命令位置の公開資料なし）

~~~diff
- 00b5e1e0 ["INT_ADD", "register:40f0:8", ["const:b5e1e0:8", "const:4:8"]]
- 00b5e1e0 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b5e2a8 ["INT_ADD", "register:40f0:8", ["const:b5e2a8:8", "const:4:8"]]
+ 00b5e2a8 ["CALL", null, ["callee:00bddf70:8"]]
- 00b5e1e0 bytes 38ff0194
+ 00b5e2a8 bytes 32ff0194
- 00b5e234 ["INT_ADD", "register:40f0:8", ["const:b5e234:8", "const:4:8"]]
- 00b5e234 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5e2fc ["INT_ADD", "register:40f0:8", ["const:b5e2fc:8", "const:4:8"]]
+ 00b5e2fc ["CALL", null, ["callee:0047495c:8"]]
- 00b5e234 bytes ca59e497
+ 00b5e2fc bytes 9859e497
- 00b5e24c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5e24c ["INT_ADD", "register:40f0:8", ["const:b5e24c:8", "const:4:8"]]
- 00b5e24c ["CALLIND", null, ["register:0:8"]]
- 00b5e24c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b76474857ac6495b093b1bb3dcdb83"></a>

### [`00b5e480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e480.md) → [`00b5e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e548.md) FUN_00b5e548

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5e17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e17c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00b5e244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e244.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.41% / 新版 65.41%

CFGの説明率　旧版 5.88% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e488"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e484",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e488",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e48c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5e54c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5e550",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5e554",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e480.md#insn-00b5e484) · [`00b5e488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e480.md#insn-00b5e488) · [`00b5e48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e480.md#insn-00b5e48c)

~~~diff
- 00b5e484 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b5e484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b5e484 bytes fb1300f9
- 00b5e488 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5e488 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5e488 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5e488 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e488 bytes fa6703a9
- 00b5e48c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5e48c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5e48c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5e48c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e48c bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02ee87caafb050e3470f22a6e99ed49"></a>

### [`00b5e694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md) → [`00b5e75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e75c.md) _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e69c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e698",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5e760",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5e764",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5e768",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md#insn-00b5e698) · [`00b5e69c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md#insn-00b5e69c) · [`00b5e6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md#insn-00b5e6a0)

~~~diff
- 00b5e698 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5e698 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5e698 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5e698 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e698 bytes fa6703a9
- 00b5e69c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5e69c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5e69c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5e69c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e69c bytes f85f04a9
- 00b5e6a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5e6a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5e6a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5e6a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e6a0 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ee5ccbae23ff7e374e2049895ca9f32"></a>

### [`00b5e858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e858.md) → [`00b5e920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e920.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b00.md) · 呼出先 7件 [`00b602a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b602a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bb0.md) · 呼出先 7件 [`00b6036c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b6036c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e8c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e8c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e8cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e9ac",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e9ac",
      "PARAM",
      [
        "storage",
        "00b602a4",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5e9ac",
      "READ",
      [
        "storage",
        "00c1bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e9ac",
      "PARAM",
      [
        "storage",
        "00b6036c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e858.md#insn-00b5e8c8) · [`00b5e8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e858.md#insn-00b5e8cc) · [`00b5e8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e858.md#insn-00b5e8d0)

~~~diff
- 00b5e8c8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b5e8c8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5e8c8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b5e8c8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b5e8c8 bytes 7ffe08a9
- 00b5e8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:80:8"]]
- 00b5e8cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5e8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5e8cc bytes 7f4200f9
- 00b5e8d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
- 00b5e8d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b5e8d0 bytes 6082853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfbce25380bdb6a71d8c38930be6effc"></a>

### [`00b5e9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e9a4.md) → [`00b5ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ea6c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0bd0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ac0.md)
- 新版 呼出元 1件 [`00be0c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c80.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e9cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e9cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e9c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e9cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e9d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5ea90",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5ea94",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5ea98",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e9a4.md#insn-00b5e9c8) · [`00b5e9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e9a4.md#insn-00b5e9cc) · [`00b5e9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e9a4.md#insn-00b5e9d0)

~~~diff
- 00b5e9c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5e9c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b5e9c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5e9c8 bytes a8831df8
- 00b5e9cc ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b5e9cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5e9cc ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b5e9cc ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b5e9cc bytes ff7f02a9
- 00b5e9d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5e9d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5e9d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5e9d0 bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-372c76bfee39e81e56b296ef06b6591a"></a>

### [`00b5eaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md) → [`00b5eb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5eb70.md) _ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b606d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md) [`00b65208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b607a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md) [`00b652d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b652d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.52% / 新版 89.52%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ebb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ebb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5ec7c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ec18",
      "READ",
      [
        "storage",
        "010a1398",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5ebb0",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5ebb4",
      "DATA",
      [
        "storage",
        "00b65208",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5ec18",
      "READ",
      [
        "storage",
        "010a1458",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ec78",
      "READ",
      [
        "storage",
        "00c1bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5ec7c",
      "DATA",
      [
        "storage",
        "00b652d0",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5eaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md#insn-00b5eaf0) · [`00b5eb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md#insn-00b5eb28) · [`00b5eb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md#insn-00b5eb38)
- 新版 `00b5ebb8`（命令位置の公開資料なし） · `00b5ec00`（命令位置の公開資料なし）

~~~diff
- 00b5eaf0 ["INT_ADD", "register:40f0:8", ["const:b5eaf0:8", "const:4:8"]]
- 00b5eaf0 ["CALL", null, ["callee:00be0bc0:8"]]
+ 00b5ebb8 ["INT_ADD", "register:40f0:8", ["const:b5ebb8:8", "const:4:8"]]
+ 00b5ebb8 ["CALL", null, ["callee:00be0bc0:8"]]
- 00b5eaf0 bytes 08080294
+ 00b5ebb8 bytes 02080294
- 00b5eb28 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b5eb28 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b5eb28 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b5eb28 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b5eb28 bytes 4301899a
- 00b5eb38 ["INT_ADD", "register:40f0:8", ["const:b5eb38:8", "const:4:8"]]
- 00b5eb38 ["CALL", null, ["callee:00be0b90:8"]]
+ 00b5ec00 ["INT_ADD", "register:40f0:8", ["const:b5ec00:8", "const:4:8"]]
+ 00b5ec00 ["CALL", null, ["callee:00be0b90:8"]]
- 00b5eb38 bytes ea070294
+ 00b5ec00 bytes e4070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80eeb3e25e07539b82bce016af13e303"></a>

### [`00b5ed58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ed58.md) → [`00b5ee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ee20.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0bf0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ae0.md)
- 新版 呼出元 1件 [`00be0ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ca0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 63.64% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ed8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ed58.md#insn-00b5ed8c) · [`00b5eda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ed58.md#insn-00b5eda0) · [`00b5edcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ed58.md#insn-00b5edcc)
- 新版 `00b5ee54`（命令位置の公開資料なし） · `00b5ee68`（命令位置の公開資料なし） · `00b5ee94`（命令位置の公開資料なし）

~~~diff
- 00b5ed8c ["INT_ADD", "register:40f0:8", ["const:b5ed8c:8", "const:4:8"]]
- 00b5ed8c ["CALL", null, ["callee:00be0cc0:8"]]
+ 00b5ee54 ["INT_ADD", "register:40f0:8", ["const:b5ee54:8", "const:4:8"]]
+ 00b5ee54 ["CALL", null, ["callee:00be0cc0:8"]]
- 00b5ed8c bytes a1070294
+ 00b5ee54 bytes 9b070294
- 00b5eda0 ["INT_ADD", "register:40f0:8", ["const:b5eda0:8", "const:4:8"]]
- 00b5eda0 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b5ee68 ["INT_ADD", "register:40f0:8", ["const:b5ee68:8", "const:4:8"]]
+ 00b5ee68 ["CALL", null, ["callee:00bddf30:8"]]
- 00b5eda0 bytes 38fc0194
+ 00b5ee68 bytes 32fc0194
- 00b5edcc ["INT_ADD", "register:40f0:8", ["const:b5edcc:8", "const:4:8"]]
- 00b5edcc ["CALL", null, ["callee:00be0b90:8"]]
+ 00b5ee94 ["INT_ADD", "register:40f0:8", ["const:b5ee94:8", "const:4:8"]]
+ 00b5ee94 ["CALL", null, ["callee:00be0b90:8"]]
- 00b5edcc bytes 45070294
+ 00b5ee94 bytes 3f070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c86bcf61255f48c9ae2be68dd4faa224"></a>

### [`00b5ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md) → [`00b5ef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ef24.md) _ZN8firebase4auth4Auth35SignInAndRetrieveDataWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda90.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bddb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb40.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5f030",
      "incomplete_value": true,
      "site": "00b5f030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ef68",
      "incomplete_value": true,
      "site": "00b5ef68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5efcc",
      "incomplete_value": true,
      "site": "00b5efdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ef04",
      "incomplete_value": true,
      "site": "00b5ef14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5ef8c",
      "incomplete_value": true,
      "site": "00b5ef98",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5efcc",
      "READ",
      [
        "storage",
        "010a1398",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f02c",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f030",
      "DATA",
      [
        "storage",
        "00b64df8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5efcc",
      "READ",
      [
        "storage",
        "010a1458",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f02c",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f030",
      "DATA",
      [
        "storage",
        "00b64ec0",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ef14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md#insn-00b5ef14) · [`00b5ef98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md#insn-00b5ef98) · [`00b5efa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md#insn-00b5efa0)
- 新版 `00b5efdc`（命令位置の公開資料なし） · `00b5f060`（命令位置の公開資料なし） · `00b5f068`（命令位置の公開資料なし）

~~~diff
- 00b5ef14 ["INT_ADD", "register:40f0:8", ["const:b5ef14:8", "const:4:8"]]
- 00b5ef14 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5efdc ["INT_ADD", "register:40f0:8", ["const:b5efdc:8", "const:4:8"]]
+ 00b5efdc ["CALL", null, ["callee:0047495c:8"]]
- 00b5ef14 bytes 9256e497
+ 00b5efdc bytes 6056e497
- 00b5ef98 ["INT_ADD", "register:40f0:8", ["const:b5ef98:8", "const:4:8"]]
- 00b5ef98 ["CALL", null, ["callee:00bde070:8"]]
+ 00b5f060 ["INT_ADD", "register:40f0:8", ["const:b5f060:8", "const:4:8"]]
+ 00b5f060 ["CALL", null, ["callee:00bde070:8"]]
- 00b5ef98 bytes 0afc0194
+ 00b5f060 bytes 04fc0194
- 00b5efa0 ["INT_ADD", "register:40f0:8", ["const:b5efa0:8", "const:4:8"]]
- 00b5efa0 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b5f068 ["INT_ADD", "register:40f0:8", ["const:b5f068:8", "const:4:8"]]
+ 00b5f068 ["CALL", null, ["callee:00bddbf0:8"]]
- 00b5efa0 bytes e8fa0194
+ 00b5f068 bytes e2fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-494bf5469789ef4319d3a054c5c3fc6f"></a>

### [`00b5f048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f048.md) → [`00b5f110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f110.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc30.md) · 呼出先 3件 [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddce0.md) · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5f14c",
      "incomplete_value": false,
      "site": "00b5f150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f084",
      "incomplete_value": false,
      "site": "00b5f088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5f120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5f080"
      ]
    ],
    [
      "unmatched:00b5f084",
      "PARAM",
      [
        "storage",
        "002a50d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5f120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f148"
      ]
    ],
    [
      "00b5f14c",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f048.md#insn-00b5f088) · [`00b5f058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f048.md#insn-00b5f058) · [`00b5f06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f048.md#insn-00b5f06c)
- 新版 `00b5f150`（命令位置の公開資料なし） · `00b5f120`（命令位置の公開資料なし）

~~~diff
- 00b5f088 ["INT_ADD", "register:40f0:8", ["const:b5f088:8", "const:4:8"]]
- 00b5f088 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5f150 ["INT_ADD", "register:40f0:8", ["const:b5f150:8", "const:4:8"]]
+ 00b5f150 ["CALL", null, ["callee:00bde130:8"]]
- 00b5f088 bytes fefb0194
+ 00b5f150 bytes f8fb0194
- 00b5f058 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5f058 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5f120 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b5f120 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5f058 bytes 410100b4
+ 00b5f120 bytes 410100b4
- 00b5f06c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00b5f06c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5f06c bytes 020940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42bb9065eb0f81b9a43645e18c4b6258"></a>

### [`00b5f0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md) → [`00b5f194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f194.md) _ZN8firebase4auth4Auth17SignInAnonymouslyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 27.27% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f0fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5f250",
      "incomplete_value": true,
      "site": "00b5f250",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f188",
      "incomplete_value": true,
      "site": "00b5f188",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5f1c4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5f1f0",
      "READ",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f24c",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5f1c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5f1f0",
      "READ",
      [
        "storage",
        "010a1460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f24c",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md#insn-00b5f0fc) · [`00b5f134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md#insn-00b5f134) · [`00b5f1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md#insn-00b5f1b8)
- 新版 `00b5f1fc`（命令位置の公開資料なし） · `00b5f280`（命令位置の公開資料なし）

~~~diff
- 00b5f0fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b5f0fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5f0fc bytes e81700f9
- 00b5f134 ["INT_ADD", "register:40f0:8", ["const:b5f134:8", "const:4:8"]]
- 00b5f134 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5f1fc ["INT_ADD", "register:40f0:8", ["const:b5f1fc:8", "const:4:8"]]
+ 00b5f1fc ["CALL", null, ["callee:0047495c:8"]]
- 00b5f134 bytes 0a56e497
+ 00b5f1fc bytes d855e497
- 00b5f1b8 ["INT_ADD", "register:40f0:8", ["const:b5f1b8:8", "const:4:8"]]
- 00b5f1b8 ["CALL", null, ["callee:00bde070:8"]]
+ 00b5f280 ["INT_ADD", "register:40f0:8", ["const:b5f280:8", "const:4:8"]]
+ 00b5f280 ["CALL", null, ["callee:00bde070:8"]]
- 00b5f1b8 bytes 82fb0194
+ 00b5f280 bytes 7cfb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f623cc470f4b869e8ec47c17eed18f21"></a>

### [`00b5f258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md) → [`00b5f320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f320.md) _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.62% / 新版 86.62%

CFGの説明率　旧版 14.29% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f25c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f25c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f25c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f260",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f264",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5f324",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5f328",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5f32c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f25c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md#insn-00b5f25c) · [`00b5f260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md#insn-00b5f260) · [`00b5f264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md#insn-00b5f264)

~~~diff
- 00b5f25c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5f25c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5f25c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5f25c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f25c bytes fa6704a9
- 00b5f260 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5f260 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5f260 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5f260 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f260 bytes f85f05a9
- 00b5f264 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f264 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f264 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b5f264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f264 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a7e3e66802f9f1de49bf57db77ff4cd"></a>

### [`00b5f4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md) → [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.51% / 新版 84.51%

CFGの説明率　旧版 32.14% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f4ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f4e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f4ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f4f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5f5b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5f5b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5f5b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md#insn-00b5f4e8) · [`00b5f4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md#insn-00b5f4ec) · [`00b5f4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md#insn-00b5f4f0)

~~~diff
- 00b5f4e8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5f4e8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5f4e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5f4e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f4e8 bytes fa6704a9
- 00b5f4ec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5f4ec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5f4ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5f4ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f4ec bytes f85f05a9
- 00b5f4f0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f4f0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f4f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b5f4f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f4f0 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ee276c1ae100e8a1fc3033a2f5bf6a"></a>

### [`00b5f770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f770.md) → [`00b5f838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f838.md) _ZN8firebase4auth4Auth12current_userEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddac0.md) · 呼出先 3件 [`00bddad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddad0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bddb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb70.md) · 呼出先 3件 [`00bddb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb80.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 36.36% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 11件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5f894",
      "incomplete_value": true,
      "site": "00b5f8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f7cc",
      "incomplete_value": true,
      "site": "00b5f7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5f8d4",
      "incomplete_value": true,
      "site": "00b5f8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f80c",
      "incomplete_value": true,
      "site": "00b5f82c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f7a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f7a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f8c0"
      ]
    ],
    [
      "00b5f884",
      "READ",
      [
        "storage",
        "00c1ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f8b4",
      "DATA",
      [
        "storage",
        "00c12a00",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b5f86c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f8c0"
      ]
    ],
    [
      "00b5f884",
      "READ",
      [
        "storage",
        "00c1bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f8b4",
      "DATA",
      [
        "storage",
        "00c12ab0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f770.md#insn-00b5f798) · [`00b5f7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f770.md#insn-00b5f7a4) · [`00b5f7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f770.md#insn-00b5f7b0)
- 新版 `00b5f860`（命令位置の公開資料なし） · `00b5f878`（命令位置の公開資料なし）

~~~diff
- 00b5f798 ["INT_ADD", "register:40f0:8", ["const:b5f798:8", "const:4:8"]]
- 00b5f798 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5f860 ["INT_ADD", "register:40f0:8", ["const:b5f860:8", "const:4:8"]]
+ 00b5f860 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5f798 bytes e2f80194
+ 00b5f860 bytes dcf80194
- 00b5f7a4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5f7a4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b5f7a4 bytes a90200b4
- 00b5f7b0 ["INT_ADD", "register:40f0:8", ["const:b5f7b0:8", "const:4:8"]]
- 00b5f7b0 ["CALL", null, ["callee:00bddb80:8"]]
+ 00b5f878 ["INT_ADD", "register:40f0:8", ["const:b5f878:8", "const:4:8"]]
+ 00b5f878 ["CALL", null, ["callee:00bddb80:8"]]
- 00b5f7b0 bytes c8f80194
+ 00b5f878 bytes c2f80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48c98f45fd7140ad5db4094f9962b41e"></a>

### [`00b5f868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f868.md) → [`00b5f930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f930.md) _ZNK8firebase4auth4Auth13language_codeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f880"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5f948"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5f960",
      "incomplete_value": true,
      "site": "00b5f96c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f898",
      "incomplete_value": true,
      "site": "00b5f8a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:340:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f9a0"
      ]
    ],
    [
      "00b5f960",
      "READ",
      [
        "storage",
        "010a1340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5f948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f9a0"
      ]
    ],
    [
      "00b5f960",
      "READ",
      [
        "storage",
        "010a1400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f868.md#insn-00b5f880) · [`00b5f8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f868.md#insn-00b5f8a4)
- 新版 `00b5f96c`（命令位置の公開資料なし） · `00b5f948`（命令位置の公開資料なし）

~~~diff
- 00b5f880 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5f880 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5f880 bytes c90200b4
- 00b5f8a4 ["INT_ADD", "register:40f0:8", ["const:b5f8a4:8", "const:4:8"]]
- 00b5f8a4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5f96c ["INT_ADD", "register:40f0:8", ["const:b5f96c:8", "const:4:8"]]
+ 00b5f96c ["CALL", null, ["callee:0047495c:8"]]
- 00b5f8a4 bytes 2e54e497
+ 00b5f96c bytes fc53e497
+ 00b5f948 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5f948 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b5f948 bytes c90200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43280d1ec7a2589cd95c602f178bba7c"></a>

### [`00b5f8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f8f0.md) → [`00b5f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f9b8.md) _ZN8firebase4auth4Auth17set_language_codeEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 11.11% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5f90c",
      "incomplete_value": true,
      "site": "00b5f914",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4040:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5fa0c",
      "incomplete_value": true,
      "site": "00b5fa18",
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
      "definition_site": "00b5fa10",
      "incomplete_value": true,
      "site": "00b5fa18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5fa08",
      "READ",
      [
        "storage",
        "010a1348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5fa08",
      "READ",
      [
        "storage",
        "010a1408",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f8f0.md#insn-00b5f914) · [`00b5f950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f8f0.md#insn-00b5f950) · [`00b5f904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f8f0.md#insn-00b5f904)
- 新版 `00b5f9dc`（命令位置の公開資料なし） · `00b5fa18`（命令位置の公開資料なし） · `00b5f9cc`（命令位置の公開資料なし）

~~~diff
- 00b5f914 ["INT_ADD", "register:40f0:8", ["const:b5f914:8", "const:4:8"]]
- 00b5f914 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b5f9dc ["INT_ADD", "register:40f0:8", ["const:b5f9dc:8", "const:4:8"]]
+ 00b5f9dc ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5f914 bytes fbf90194
+ 00b5f9dc bytes f5f90194
- 00b5f950 ["INT_ADD", "register:40f0:8", ["const:b5f950:8", "const:4:8"]]
- 00b5f950 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5fa18 ["INT_ADD", "register:40f0:8", ["const:b5fa18:8", "const:4:8"]]
+ 00b5fa18 ["CALL", null, ["callee:00551e14:8"]]
- 00b5f950 bytes 31c9e797
+ 00b5fa18 bytes ffc8e797
- 00b5f904 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5f904 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b5f9cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5f9cc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5f904 bytes e80300b4
+ 00b5f9cc bytes e80300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd44c8f40f137828887ce517b289d79d"></a>

### [`00b5f990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f990.md) → [`00b5fa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fa58.md) _ZN8firebase4auth4Auth14UseAppLanguageEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5fa80",
      "incomplete_value": true,
      "site": "00b5fa8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f9b8",
      "incomplete_value": true,
      "site": "00b5f9c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f9e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b5faa8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5fa68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fa90"
      ]
    ],
    [
      "00b5fa80",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5f9c8",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5fa68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5faa0"
      ]
    ],
    [
      "00b5fa80",
      "READ",
      [
        "storage",
        "010a1410",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5faa0",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f990.md#insn-00b5f9c4) · [`00b5f9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f990.md#insn-00b5f9e0)
- 新版 `00b5fa8c`（命令位置の公開資料なし） · `00b5faa8`（命令位置の公開資料なし）

~~~diff
- 00b5f9c4 ["INT_ADD", "register:40f0:8", ["const:b5f9c4:8", "const:4:8"]]
- 00b5f9c4 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5fa8c ["INT_ADD", "register:40f0:8", ["const:b5fa8c:8", "const:4:8"]]
+ 00b5fa8c ["CALL", null, ["callee:00551e14:8"]]
- 00b5f9c4 bytes 14c9e797
+ 00b5fa8c bytes e2c8e797
- 00b5f9e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5f9e0 ["RETURN", null, ["register:0:8"]]
- 00b5f9e0 bytes c0035fd6
+ 00b5faa8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b5faa8 ["RETURN", null, ["register:0:8"]]
+ 00b5faa8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac39f911149ab2ff82de28eff0f3ecf8"></a>

### [`00b5fa7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fa7c.md) → [`00b5fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.29% / 新版 86.29%

CFGの説明率　旧版 9.09% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fa90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fa90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fab0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5fa90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5fbe4",
      "READ",
      [
        "storage",
        "010a13b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5fb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5fb78",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5fbe4",
      "READ",
      [
        "storage",
        "010a1478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fa90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fa7c.md#insn-00b5fa90) · [`00b5fab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fa7c.md#insn-00b5fab0) · [`00b5fafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fa7c.md#insn-00b5fafc)
- 新版 `00b5fbc4`（命令位置の公開資料なし）

~~~diff
- 00b5fa90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5fa90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5fa90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b5fa90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5fa90 bytes fd7b09a9
- 00b5fab0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b5fab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5fab0 bytes e82700f9
- 00b5fafc ["INT_ADD", "register:40f0:8", ["const:b5fafc:8", "const:4:8"]]
- 00b5fafc ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b5fbc4 ["INT_ADD", "register:40f0:8", ["const:b5fbc4:8", "const:4:8"]]
+ 00b5fbc4 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b5fafc bytes 81f90194
+ 00b5fbc4 bytes 7bf90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aaef5eb277e9b6f3700d52e4d9de0a5"></a>

### [`00b5fcc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fcc8.md) → [`00b5fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fd90.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c00.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md)
- 新版 呼出元 1件 [`00be0cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cb0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 26.67% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fcec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fcf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fcf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5fcec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fcf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fcf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5fdb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5fdb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5fdbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fcc8.md#insn-00b5fcec) · [`00b5fcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fcc8.md#insn-00b5fcf0) · [`00b5fcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fcc8.md#insn-00b5fcf4)

~~~diff
- 00b5fcec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5fcec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b5fcec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5fcec bytes a8831df8
- 00b5fcf0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b5fcf0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5fcf0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b5fcf0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b5fcf0 bytes ff7f02a9
- 00b5fcf4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5fcf4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5fcf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5fcf4 bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c945112aa8b428800f00c46229c6b9"></a>

### [`00b5fdcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fdcc.md) → [`00b5fe94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fdcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fdcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fdd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5fdcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fdd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fdd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5fe94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5fe98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5fe9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fdcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fdcc.md#insn-00b5fdcc) · [`00b5fdd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fdcc.md#insn-00b5fdd0) · [`00b5fdd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fdcc.md#insn-00b5fdd4)

~~~diff
- 00b5fdcc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5fdcc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5fdcc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5fdcc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5fdcc bytes f657bda9
- 00b5fdd0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5fdd0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5fdd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5fdd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5fdd0 bytes f44f01a9
- 00b5fdd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5fdd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5fdd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5fdd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5fdd4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3017e4c644c77b1ff952d2859fad252b"></a>

### [`00b5fef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fef0.md) → [`00b5ffb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHand

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ad0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b80.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6001c",
      "incomplete_value": false,
      "site": "00b60020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ff54",
      "incomplete_value": false,
      "site": "00b5ff58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6001c",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6001c",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ff58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fef0.md#insn-00b5ff58) · [`00b5ff1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fef0.md#insn-00b5ff1c) · [`00b5ff28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fef0.md#insn-00b5ff28)
- 新版 `00b60020`（命令位置の公開資料なし） · `00b5ffe4`（命令位置の公開資料なし） · `00b5fff0`（命令位置の公開資料なし）

~~~diff
- 00b5ff58 ["INT_ADD", "register:40f0:8", ["const:b5ff58:8", "const:4:8"]]
- 00b5ff58 ["CALL", null, ["callee:00bde130:8"]]
+ 00b60020 ["INT_ADD", "register:40f0:8", ["const:b60020:8", "const:4:8"]]
+ 00b60020 ["CALL", null, ["callee:00bde130:8"]]
- 00b5ff58 bytes 4af80194
+ 00b60020 bytes 44f80194
- 00b5ff1c ["INT_ADD", "register:40f0:8", ["const:b5ff1c:8", "const:4:8"]]
- 00b5ff1c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5ffe4 ["INT_ADD", "register:40f0:8", ["const:b5ffe4:8", "const:4:8"]]
+ 00b5ffe4 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b5ff1c bytes 01f70194
+ 00b5ffe4 bytes fbf60194
- 00b5ff28 ["INT_ADD", "register:40f0:8", ["const:b5ff28:8", "const:4:8"]]
- 00b5ff28 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b5fff0 ["INT_ADD", "register:40f0:8", ["const:b5fff0:8", "const:4:8"]]
+ 00b5fff0 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b5ff28 bytes f6f70194
+ 00b5fff0 bytes f0f70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8200086a5e007eab5a95fd6c8b72ecd1"></a>

### [`00b600cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b600cc.md) → [`00b60194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60194.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobje

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0aa0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b50.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60200",
      "incomplete_value": false,
      "site": "00b60204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60138",
      "incomplete_value": false,
      "site": "00b6013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60200",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b60200",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6013c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b600cc.md#insn-00b6013c) · [`00b60100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b600cc.md#insn-00b60100) · [`00b6010c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b600cc.md#insn-00b6010c)
- 新版 `00b60204`（命令位置の公開資料なし） · `00b601c8`（命令位置の公開資料なし） · `00b601d4`（命令位置の公開資料なし）

~~~diff
- 00b6013c ["INT_ADD", "register:40f0:8", ["const:b6013c:8", "const:4:8"]]
- 00b6013c ["CALL", null, ["callee:00bde130:8"]]
+ 00b60204 ["INT_ADD", "register:40f0:8", ["const:b60204:8", "const:4:8"]]
+ 00b60204 ["CALL", null, ["callee:00bde130:8"]]
- 00b6013c bytes d1f70194
+ 00b60204 bytes cbf70194
- 00b60100 ["INT_ADD", "register:40f0:8", ["const:b60100:8", "const:4:8"]]
- 00b60100 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b601c8 ["INT_ADD", "register:40f0:8", ["const:b601c8:8", "const:4:8"]]
+ 00b601c8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b60100 bytes 88f60194
+ 00b601c8 bytes 82f60194
- 00b6010c ["INT_ADD", "register:40f0:8", ["const:b6010c:8", "const:4:8"]]
- 00b6010c ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b601d4 ["INT_ADD", "register:40f0:8", ["const:b601d4:8", "const:4:8"]]
+ 00b601d4 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b6010c bytes 7df70194
+ 00b601d4 bytes 77f70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dbcb93b5ee5f4116f90a5ed0f1f2a32"></a>

### [`00b603e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b603e4.md) → [`00b604ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b604ac.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12Fut

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a90.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b40.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60518",
      "incomplete_value": false,
      "site": "00b6051c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60450",
      "incomplete_value": false,
      "site": "00b60454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60518",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b60518",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b603e4.md#insn-00b60454) · [`00b60418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b603e4.md#insn-00b60418) · [`00b60424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b603e4.md#insn-00b60424)
- 新版 `00b6051c`（命令位置の公開資料なし） · `00b604e0`（命令位置の公開資料なし） · `00b604ec`（命令位置の公開資料なし）

~~~diff
- 00b60454 ["INT_ADD", "register:40f0:8", ["const:b60454:8", "const:4:8"]]
- 00b60454 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6051c ["INT_ADD", "register:40f0:8", ["const:b6051c:8", "const:4:8"]]
+ 00b6051c ["CALL", null, ["callee:00bde130:8"]]
- 00b60454 bytes 0bf70194
+ 00b6051c bytes 05f70194
- 00b60418 ["INT_ADD", "register:40f0:8", ["const:b60418:8", "const:4:8"]]
- 00b60418 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b604e0 ["INT_ADD", "register:40f0:8", ["const:b604e0:8", "const:4:8"]]
+ 00b604e0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b60418 bytes c2f50194
+ 00b604e0 bytes bcf50194
- 00b60424 ["INT_ADD", "register:40f0:8", ["const:b60424:8", "const:4:8"]]
- 00b60424 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b604ec ["INT_ADD", "register:40f0:8", ["const:b604ec:8", "const:4:8"]]
+ 00b604ec ["CALL", null, ["callee:00bddfb0:8"]]
- 00b60424 bytes b7f60194
+ 00b604ec bytes b1f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483e5a93c18ee4f04dc82368a1e0f336"></a>

### [`00b6051c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b6051c.md) → [`00b605e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b605e4.md) _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c30.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ce0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b60530",
      "incomplete_value": false,
      "site": "00b6053c",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6053c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b6051c.md#insn-00b6053c) · [`00b60550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b6051c.md#insn-00b60550) · [`00b60564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b6051c.md#insn-00b60564)
- 新版 `00b60604`（命令位置の公開資料なし） · `00b60618`（命令位置の公開資料なし） · `00b6062c`（命令位置の公開資料なし）

~~~diff
- 00b6053c ["INT_ADD", "register:40f0:8", ["const:b6053c:8", "const:4:8"]]
- 00b6053c ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b60604 ["INT_ADD", "register:40f0:8", ["const:b60604:8", "const:4:8"]]
+ 00b60604 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b6053c bytes f5f50194
+ 00b60604 bytes eff50194
- 00b60550 ["INT_ADD", "register:40f0:8", ["const:b60550:8", "const:4:8"]]
- 00b60550 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b60618 ["INT_ADD", "register:40f0:8", ["const:b60618:8", "const:4:8"]]
+ 00b60618 ["CALL", null, ["callee:00bddf30:8"]]
- 00b60550 bytes 4cf60194
+ 00b60618 bytes 46f60194
- 00b60564 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60564 ["INT_ADD", "register:40f0:8", ["const:b60564:8", "const:4:8"]]
- 00b60564 ["CALLIND", null, ["register:0:8"]]
+ 00b6062c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6062c ["INT_ADD", "register:40f0:8", ["const:b6062c:8", "const:4:8"]]
+ 00b6062c ["CALLIND", null, ["register:0:8"]]
- 00b60564 bytes 00013fd6
+ 00b6062c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64832a38d730727b2a2df96edf85a393"></a>

### [`00b605d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b605d0.md) → [`00b60698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60698.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ae0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b90.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b606fc",
      "incomplete_value": false,
      "site": "00b60700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60634",
      "incomplete_value": false,
      "site": "00b60638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b606fc",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b606fc",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b605d0.md#insn-00b60638) · [`00b605fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b605d0.md#insn-00b605fc) · [`00b60608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b605d0.md#insn-00b60608)
- 新版 `00b60700`（命令位置の公開資料なし） · `00b606c4`（命令位置の公開資料なし） · `00b606d0`（命令位置の公開資料なし）

~~~diff
- 00b60638 ["INT_ADD", "register:40f0:8", ["const:b60638:8", "const:4:8"]]
- 00b60638 ["CALL", null, ["callee:00bde130:8"]]
+ 00b60700 ["INT_ADD", "register:40f0:8", ["const:b60700:8", "const:4:8"]]
+ 00b60700 ["CALL", null, ["callee:00bde130:8"]]
- 00b60638 bytes 92f60194
+ 00b60700 bytes 8cf60194
- 00b605fc ["INT_ADD", "register:40f0:8", ["const:b605fc:8", "const:4:8"]]
- 00b605fc ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b606c4 ["INT_ADD", "register:40f0:8", ["const:b606c4:8", "const:4:8"]]
+ 00b606c4 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b605fc bytes 49f50194
+ 00b606c4 bytes 43f50194
- 00b60608 ["INT_ADD", "register:40f0:8", ["const:b60608:8", "const:4:8"]]
- 00b60608 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b606d0 ["INT_ADD", "register:40f0:8", ["const:b606d0:8", "const:4:8"]]
+ 00b606d0 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b60608 bytes 3ef60194
+ 00b606d0 bytes 38f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fbdee6152d49c9a14e49512b456e43f"></a>

### [`00b607ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b607ac.md) → [`00b60874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60874.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResu

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ab0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b60.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 70.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b608e0",
      "incomplete_value": false,
      "site": "00b608e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60818",
      "incomplete_value": false,
      "site": "00b6081c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b60850",
      "incomplete_value": true,
      "site": "00b60858",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b60854",
      "incomplete_value": true,
      "site": "00b60858",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b608e0",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b608e0",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6081c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b607ac.md#insn-00b6081c) · [`00b60858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b607ac.md#insn-00b60858) · [`00b607e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b607ac.md#insn-00b607e0)
- 新版 `00b608e4`（命令位置の公開資料なし） · `00b60920`（命令位置の公開資料なし） · `00b608a8`（命令位置の公開資料なし）

~~~diff
- 00b6081c ["INT_ADD", "register:40f0:8", ["const:b6081c:8", "const:4:8"]]
- 00b6081c ["CALL", null, ["callee:00bde130:8"]]
+ 00b608e4 ["INT_ADD", "register:40f0:8", ["const:b608e4:8", "const:4:8"]]
+ 00b608e4 ["CALL", null, ["callee:00bde130:8"]]
- 00b6081c bytes 19f60194
+ 00b608e4 bytes 13f60194
- 00b60858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60858 ["INT_ADD", "register:40f0:8", ["const:b60858:8", "const:4:8"]]
- 00b60858 ["CALLIND", null, ["register:0:8"]]
+ 00b60920 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60920 ["INT_ADD", "register:40f0:8", ["const:b60920:8", "const:4:8"]]
+ 00b60920 ["CALLIND", null, ["register:0:8"]]
- 00b60858 bytes 00013fd6
+ 00b60920 bytes 00013fd6
- 00b607e0 ["INT_ADD", "register:40f0:8", ["const:b607e0:8", "const:4:8"]]
- 00b607e0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b608a8 ["INT_ADD", "register:40f0:8", ["const:b608a8:8", "const:4:8"]]
+ 00b608a8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b607e0 bytes d0f40194
+ 00b608a8 bytes caf40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04874ebbd10277f07dc3b8c48f64dbb8"></a>

### [`00b60984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60984.md) → [`00b60a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60a4c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ac0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b70.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 10.00% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b609e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b60aa8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b609a0",
      "incomplete_value": true,
      "site": "00b609b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b609e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ab8"
      ]
    ],
    [
      "unmatched:00b609e8",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b60a54",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ab8"
      ]
    ],
    [
      "00b60ab0",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ],
    [
      "00b60b1c",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b609b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60984.md#insn-00b609b0) · [`00b609d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60984.md#insn-00b609d8) · [`00b609e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60984.md#insn-00b609e0)
- 新版 `00b60a78`（命令位置の公開資料なし）

~~~diff
- 00b609b0 ["INT_ADD", "register:40f0:8", ["const:b609b0:8", "const:4:8"]]
- 00b609b0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b60a78 ["INT_ADD", "register:40f0:8", ["const:b60a78:8", "const:4:8"]]
+ 00b60a78 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b609b0 bytes 5cf40194
+ 00b60a78 bytes 56f40194
- 00b609d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b609d8 ["INT_ADD", "register:40f0:8", ["const:b609d8:8", "const:4:8"]]
- 00b609d8 ["CALLIND", null, ["register:0:8"]]
- 00b609d8 bytes 00013fd6
- 00b609e0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b609e0 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee89a810ca599b16ee06ca05248caf6"></a>

### [`00b60b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60b60.md) → [`00b60c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60c28.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS_4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0af0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ba0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60c94",
      "incomplete_value": false,
      "site": "00b60c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60bcc",
      "incomplete_value": false,
      "site": "00b60bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60c94",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b60c94",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60b60.md#insn-00b60bd0) · [`00b60b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60b60.md#insn-00b60b94) · [`00b60ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60b60.md#insn-00b60ba0)
- 新版 `00b60c98`（命令位置の公開資料なし） · `00b60c5c`（命令位置の公開資料なし） · `00b60c68`（命令位置の公開資料なし）

~~~diff
- 00b60bd0 ["INT_ADD", "register:40f0:8", ["const:b60bd0:8", "const:4:8"]]
- 00b60bd0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b60c98 ["INT_ADD", "register:40f0:8", ["const:b60c98:8", "const:4:8"]]
+ 00b60c98 ["CALL", null, ["callee:00bde130:8"]]
- 00b60bd0 bytes 2cf50194
+ 00b60c98 bytes 26f50194
- 00b60b94 ["INT_ADD", "register:40f0:8", ["const:b60b94:8", "const:4:8"]]
- 00b60b94 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b60c5c ["INT_ADD", "register:40f0:8", ["const:b60c5c:8", "const:4:8"]]
+ 00b60c5c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b60b94 bytes e3f30194
+ 00b60c5c bytes ddf30194
- 00b60ba0 ["INT_ADD", "register:40f0:8", ["const:b60ba0:8", "const:4:8"]]
- 00b60ba0 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b60c68 ["INT_ADD", "register:40f0:8", ["const:b60c68:8", "const:4:8"]]
+ 00b60c68 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b60ba0 bytes d8f40194
+ 00b60c68 bytes d2f40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e326a3c2e55b6222d62dbb687354f1"></a>

### [`00b60c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60c98.md) → [`00b60d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60d60.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b60d8c",
      "incomplete_value": true,
      "site": "00b60d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60cc4",
      "incomplete_value": true,
      "site": "00b60cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b60d74",
      "incomplete_value": true,
      "site": "00b60d74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60cac",
      "incomplete_value": true,
      "site": "00b60cac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60d80",
      "incomplete_value": false,
      "site": "00b60d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60cb8",
      "incomplete_value": false,
      "site": "00b60cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:f3d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60d70",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60d80",
      "PARAM",
      [
        "storage",
        "002a1f3d",
        null,
        "string"
      ]
    ],
    [
      "00b60d8c",
      "WRITE",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60d70",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60d80",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60d8c",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60c98.md#insn-00b60cbc) · [`00b60cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60c98.md#insn-00b60cc4) · [`00b60ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60c98.md#insn-00b60ca8)
- 新版 `00b60d84`（命令位置の公開資料なし） · `00b60d8c`（命令位置の公開資料なし） · `00b60d70`（命令位置の公開資料なし）

~~~diff
- 00b60cbc ["INT_ADD", "register:40f0:8", ["const:b60cbc:8", "const:4:8"]]
- 00b60cbc ["CALL", null, ["callee:00bde040:8"]]
+ 00b60d84 ["INT_ADD", "register:40f0:8", ["const:b60d84:8", "const:4:8"]]
+ 00b60d84 ["CALL", null, ["callee:00bde040:8"]]
- 00b60cbc bytes b5f40194
+ 00b60d84 bytes aff40194
- 00b60cc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60cc4 bytes 602202f9
+ 00b60d8c bytes 608202f9
- 00b60ca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60ca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60d70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60ca8 bytes 682242f9
+ 00b60d70 bytes 688242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ff228903f05e7c132a43c9230ea92c"></a>

### [`00b60cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60cd8.md) → [`00b60da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60da0.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b60dcc",
      "incomplete_value": true,
      "site": "00b60dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d04",
      "incomplete_value": true,
      "site": "00b60d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b60db4",
      "incomplete_value": true,
      "site": "00b60db4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60cec",
      "incomplete_value": true,
      "site": "00b60cec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60dbc",
      "incomplete_value": false,
      "site": "00b60dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60cf4",
      "incomplete_value": false,
      "site": "00b60cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:f3d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60db0",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60dbc",
      "PARAM",
      [
        "storage",
        "002a1f3d",
        null,
        "string"
      ]
    ],
    [
      "00b60dcc",
      "WRITE",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60db0",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60dbc",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60dcc",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60cd8.md#insn-00b60cfc) · [`00b60d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60cd8.md#insn-00b60d04) · [`00b60ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60cd8.md#insn-00b60ce8)
- 新版 `00b60dc4`（命令位置の公開資料なし） · `00b60dcc`（命令位置の公開資料なし） · `00b60db0`（命令位置の公開資料なし）

~~~diff
- 00b60cfc ["INT_ADD", "register:40f0:8", ["const:b60cfc:8", "const:4:8"]]
- 00b60cfc ["CALL", null, ["callee:00bde040:8"]]
+ 00b60dc4 ["INT_ADD", "register:40f0:8", ["const:b60dc4:8", "const:4:8"]]
+ 00b60dc4 ["CALL", null, ["callee:00bde040:8"]]
- 00b60cfc bytes a5f40194
+ 00b60dc4 bytes 9ff40194
- 00b60d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60d04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60dcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60d04 bytes 602202f9
+ 00b60dcc bytes 608202f9
- 00b60ce8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60ce8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60db0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60ce8 bytes 682242f9
+ 00b60db0 bytes 688242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4b447774dae7a2bdef59cd096f73fc"></a>

### [`00b60d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d18.md) → [`00b60de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60de0.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b60e10",
      "incomplete_value": true,
      "site": "00b60e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d48",
      "incomplete_value": true,
      "site": "00b60d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b60df4",
      "incomplete_value": true,
      "site": "00b60df4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d2c",
      "incomplete_value": true,
      "site": "00b60d2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60e00",
      "incomplete_value": false,
      "site": "00b60e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d38",
      "incomplete_value": false,
      "site": "00b60d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:f3d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60df0",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e00",
      "PARAM",
      [
        "storage",
        "002a1f3d",
        null,
        "string"
      ]
    ],
    [
      "00b60e10",
      "WRITE",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60df0",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e00",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60e10",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d18.md#insn-00b60d40) · [`00b60d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d18.md#insn-00b60d48) · [`00b60d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d18.md#insn-00b60d28)
- 新版 `00b60e08`（命令位置の公開資料なし） · `00b60e10`（命令位置の公開資料なし） · `00b60df0`（命令位置の公開資料なし）

~~~diff
- 00b60d40 ["INT_ADD", "register:40f0:8", ["const:b60d40:8", "const:4:8"]]
- 00b60d40 ["CALL", null, ["callee:00bde040:8"]]
+ 00b60e08 ["INT_ADD", "register:40f0:8", ["const:b60e08:8", "const:4:8"]]
+ 00b60e08 ["CALL", null, ["callee:00bde040:8"]]
- 00b60d40 bytes 94f40194
+ 00b60e08 bytes 8ef40194
- 00b60d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60d48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60e10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60d48 bytes 602202f9
+ 00b60e10 bytes 608202f9
- 00b60d28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60d28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60df0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60df0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60d28 bytes 682242f9
+ 00b60df0 bytes 688242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56da2bd8006cd446ea63153879ded6c6"></a>

### [`00b60d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d5c.md) → [`00b60e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e24.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b60e54",
      "incomplete_value": true,
      "site": "00b60e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d8c",
      "incomplete_value": true,
      "site": "00b60d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b60e38",
      "incomplete_value": true,
      "site": "00b60e38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d70",
      "incomplete_value": true,
      "site": "00b60d70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60e40",
      "incomplete_value": false,
      "site": "00b60e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d78",
      "incomplete_value": false,
      "site": "00b60d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:f3d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60e34",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e40",
      "PARAM",
      [
        "storage",
        "002a1f3d",
        null,
        "string"
      ]
    ],
    [
      "00b60e54",
      "WRITE",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60e34",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e40",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60e54",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d5c.md#insn-00b60d84) · [`00b60d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d5c.md#insn-00b60d8c) · [`00b60d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60d5c.md#insn-00b60d6c)
- 新版 `00b60e4c`（命令位置の公開資料なし） · `00b60e54`（命令位置の公開資料なし） · `00b60e34`（命令位置の公開資料なし）

~~~diff
- 00b60d84 ["INT_ADD", "register:40f0:8", ["const:b60d84:8", "const:4:8"]]
- 00b60d84 ["CALL", null, ["callee:00bde040:8"]]
+ 00b60e4c ["INT_ADD", "register:40f0:8", ["const:b60e4c:8", "const:4:8"]]
+ 00b60e4c ["CALL", null, ["callee:00bde040:8"]]
- 00b60d84 bytes 83f40194
+ 00b60e4c bytes 7df40194
- 00b60d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60e54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60d8c bytes 602202f9
+ 00b60e54 bytes 608202f9
- 00b60d6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:440:8"]]
- 00b60d6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
+ 00b60e34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60d6c bytes 682242f9
+ 00b60e34 bytes 688242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688c686396c465cffa42be8eef350901"></a>

### [`00b60dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60dac.md) → [`00b60e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e74.md) _ZN8firebase4auth10authresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b60ecc",
      "incomplete_value": true,
      "site": "00b60ecc",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e04",
      "incomplete_value": true,
      "site": "00b60e04",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60ea8",
      "incomplete_value": true,
      "site": "00b60eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60de0",
      "incomplete_value": true,
      "site": "00b60dec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60e88",
      "READ",
      [
        "storage",
        "010a1448",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60ea8",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60ecc",
      "WRITE",
      [
        "storage",
        "010a1448",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b60e88",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60ea8",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60ecc",
      "WRITE",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60dac.md#insn-00b60dec) · [`00b60e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60dac.md#insn-00b60e04) · [`00b60dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60dac.md#insn-00b60dc0)
- 新版 `00b60eb4`（命令位置の公開資料なし） · `00b60ecc`（命令位置の公開資料なし） · `00b60e88`（命令位置の公開資料なし）

~~~diff
- 00b60dec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60dec ["INT_ADD", "register:40f0:8", ["const:b60dec:8", "const:4:8"]]
- 00b60dec ["CALLIND", null, ["register:0:8"]]
+ 00b60eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60eb4 ["INT_ADD", "register:40f0:8", ["const:b60eb4:8", "const:4:8"]]
+ 00b60eb4 ["CALLIND", null, ["register:0:8"]]
- 00b60dec bytes 00013fd6
+ 00b60eb4 bytes 00013fd6
- 00b60e04 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b60e04 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:448:8"]]
- 00b60e04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b60ecc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b60ecc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:508:8"]]
+ 00b60ecc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b60e04 bytes a0221139
+ 00b60ecc bytes a0221439
- 00b60dc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
- 00b60dc0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b60dc0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b60e88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
+ 00b60e88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b60e88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b60dc0 bytes a8225139
+ 00b60e88 bytes a8225439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b569c20e23e36d52589825edcd4cb89"></a>

### [`00b60e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e18.md) → [`00b60ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ee0.md) _ZN8firebase4auth10authresult12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b60f1c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60ef4",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f00",
      "READ",
      [
        "storage",
        "010a1448",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b60e58"
      ]
    ]
  ],
  "added": [
    [
      "00b60ef4",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f00",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60f20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e18.md#insn-00b60e30) · [`00b60e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e18.md#insn-00b60e54) · [`00b60e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e18.md#insn-00b60e5c)
- 新版 `00b60ef8`（命令位置の公開資料なし）

~~~diff
- 00b60e30 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b60e30 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b60ef8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b60ef8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b60e30 bytes 410200b4
+ 00b60ef8 bytes 410200b4
- 00b60e54 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b60e54 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b60e54 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:448:8"]]
- 00b60e54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b60e54 bytes bf221139
- 00b60e5c ["INT_ADD", "register:40f0:8", ["const:b60e5c:8", "const:4:8"]]
- 00b60e5c ["CALL", null, ["callee:00bde090:8"]]
- 00b60e5c bytes 61f40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad7b395c30933a04d679de24b67f7b6"></a>

### [`00b60e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e88.md) → [`00b60f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60f50.md) _ZN8firebase4auth10authresult14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60e88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60e8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60e9c",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b60f64",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e88.md#insn-00b60e88) · [`00b60e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e88.md#insn-00b60e8c) · [`00b60ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60e88.md#insn-00b60ea4)

~~~diff
- 00b60e88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b60e88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b60e88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b60e88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60e88 bytes f44fbea9
- 00b60e8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60e8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60e8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60e8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60e8c bytes fd7b01a9
- 00b60ea4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b60ea4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b60ea4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e560ab961f7674cbee403a46ae05a46d"></a>

### [`00b60f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60f34.md) → [`00b60ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ffc.md) _ZN8firebase4auth10authresult13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6103c",
      "incomplete_value": true,
      "site": "00b6103c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f74",
      "incomplete_value": true,
      "site": "00b60f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61018",
      "incomplete_value": true,
      "site": "00b61018",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f50",
      "incomplete_value": true,
      "site": "00b60f50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61020",
      "incomplete_value": false,
      "site": "00b61034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f58",
      "incomplete_value": false,
      "site": "00b60f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:f3d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61010",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61020",
      "PARAM",
      [
        "storage",
        "002a1f3d",
        null,
        "string"
      ]
    ],
    [
      "00b6103c",
      "WRITE",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61010",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61020",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b6103c",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60f34.md#insn-00b60f6c) · [`00b60f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60f34.md#insn-00b60f74) · [`00b60f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60f34.md#insn-00b60f48)
- 新版 `00b61034`（命令位置の公開資料なし） · `00b6103c`（命令位置の公開資料なし） · `00b61010`（命令位置の公開資料なし）

~~~diff
- 00b60f6c ["INT_ADD", "register:40f0:8", ["const:b60f6c:8", "const:4:8"]]
- 00b60f6c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61034 ["INT_ADD", "register:40f0:8", ["const:b61034:8", "const:4:8"]]
+ 00b61034 ["CALL", null, ["callee:00bde040:8"]]
- 00b60f6c bytes 09f40194
+ 00b61034 bytes 03f40194
- 00b60f74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:440:8"]]
- 00b60f74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6103c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
+ 00b6103c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60f74 bytes 802202f9
+ 00b6103c bytes 808202f9
- 00b60f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:440:8"]]
- 00b60f48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
+ 00b61010 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60f48 bytes 812242f9
+ 00b61010 bytes 818242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59291b42696eb10712e146a6f9550c9"></a>

### [`00b60fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fa4.md) → [`00b6106c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6106c.md) _ZN8firebase4auth10authresult10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61088",
      "incomplete_value": false,
      "site": "00b6108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60fc0",
      "incomplete_value": false,
      "site": "00b60fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b61098",
      "incomplete_value": true,
      "site": "00b610a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60fd0",
      "incomplete_value": true,
      "site": "00b60fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61088",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b61098",
      "DATA",
      [
        "storage",
        "010a1468",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61088",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61098",
      "DATA",
      [
        "storage",
        "010a1528",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fa4.md#insn-00b60fc4) · [`00b60fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fa4.md#insn-00b60fc0) · [`00b60fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fa4.md#insn-00b60fcc)
- 新版 `00b6108c`（命令位置の公開資料なし） · `00b61088`（命令位置の公開資料なし） · `00b61094`（命令位置の公開資料なし）

~~~diff
- 00b60fc4 ["INT_ADD", "register:40f0:8", ["const:b60fc4:8", "const:4:8"]]
- 00b60fc4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6108c ["INT_ADD", "register:40f0:8", ["const:b6108c:8", "const:4:8"]]
+ 00b6108c ["CALL", null, ["callee:00bde130:8"]]
- 00b60fc4 bytes 2ff40194
+ 00b6108c bytes 29f40194
- 00b60fc0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b60fc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b60fc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b60fc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61088 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b61088 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61088 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61088 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b60fc0 bytes 00c81791
+ 00b61088 bytes 00fc1991
- 00b60fcc ["COPY", "tmp:0:8", ["const:468:8"]]
- 00b60fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b60fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b60fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61094 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00b61094 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61094 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61094 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b60fcc bytes 08a11191
+ 00b61094 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b67086e215ebd1f6073fafb5e72008b"></a>

### [`00b60fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fe0.md) → [`00b610a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610a8.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b610d4",
      "incomplete_value": true,
      "site": "00b610d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6100c",
      "incomplete_value": true,
      "site": "00b6100c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b610bc",
      "incomplete_value": true,
      "site": "00b610bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60ff4",
      "incomplete_value": true,
      "site": "00b60ff4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b610c8",
      "incomplete_value": false,
      "site": "00b610cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61000",
      "incomplete_value": false,
      "site": "00b61004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fe9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b610b8",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "00b610c8",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ],
    [
      "00b610d4",
      "WRITE",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b610b8",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b610c8",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b610d4",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fe0.md#insn-00b61004) · [`00b6100c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fe0.md#insn-00b6100c) · [`00b60ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60fe0.md#insn-00b60ff0)
- 新版 `00b610cc`（命令位置の公開資料なし） · `00b610d4`（命令位置の公開資料なし） · `00b610b8`（命令位置の公開資料なし）

~~~diff
- 00b61004 ["INT_ADD", "register:40f0:8", ["const:b61004:8", "const:4:8"]]
- 00b61004 ["CALL", null, ["callee:00bde040:8"]]
+ 00b610cc ["INT_ADD", "register:40f0:8", ["const:b610cc:8", "const:4:8"]]
+ 00b610cc ["CALL", null, ["callee:00bde040:8"]]
- 00b61004 bytes e3f30194
+ 00b610cc bytes ddf30194
- 00b6100c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b6100c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b610d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b610d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6100c bytes 603a02f9
+ 00b610d4 bytes 609a02f9
- 00b60ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b60ff0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b610b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b610b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60ff0 bytes 683a42f9
+ 00b610b8 bytes 689a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5430484abae65ca27e5d542f83a085"></a>

### [`00b61020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61020.md) → [`00b610e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610e8.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b61114",
      "incomplete_value": true,
      "site": "00b61114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6104c",
      "incomplete_value": true,
      "site": "00b6104c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b610fc",
      "incomplete_value": true,
      "site": "00b610fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61034",
      "incomplete_value": true,
      "site": "00b61034",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61104",
      "incomplete_value": false,
      "site": "00b6110c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6103c",
      "incomplete_value": false,
      "site": "00b61044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fe9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b610f8",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61104",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ],
    [
      "00b61114",
      "WRITE",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b610f8",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61104",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b61114",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61020.md#insn-00b61044) · [`00b6104c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61020.md#insn-00b6104c) · [`00b61030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61020.md#insn-00b61030)
- 新版 `00b6110c`（命令位置の公開資料なし） · `00b61114`（命令位置の公開資料なし） · `00b610f8`（命令位置の公開資料なし）

~~~diff
- 00b61044 ["INT_ADD", "register:40f0:8", ["const:b61044:8", "const:4:8"]]
- 00b61044 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6110c ["INT_ADD", "register:40f0:8", ["const:b6110c:8", "const:4:8"]]
+ 00b6110c ["CALL", null, ["callee:00bde040:8"]]
- 00b61044 bytes d3f30194
+ 00b6110c bytes cdf30194
- 00b6104c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b6104c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61114 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b61114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6104c bytes 603a02f9
+ 00b61114 bytes 609a02f9
- 00b61030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b61030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b610f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b610f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61030 bytes 683a42f9
+ 00b610f8 bytes 689a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd4e6f944df9cd37c27d8d6eb32213d6"></a>

### [`00b61060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61060.md) → [`00b61128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61128.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b61158",
      "incomplete_value": true,
      "site": "00b61158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61090",
      "incomplete_value": true,
      "site": "00b61090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6113c",
      "incomplete_value": true,
      "site": "00b6113c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61074",
      "incomplete_value": true,
      "site": "00b61074",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61148",
      "incomplete_value": false,
      "site": "00b61150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61080",
      "incomplete_value": false,
      "site": "00b61088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:fe9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61138",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61148",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ],
    [
      "00b61158",
      "WRITE",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61138",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61148",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b61158",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61060.md#insn-00b61088) · [`00b61090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61060.md#insn-00b61090) · [`00b61070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61060.md#insn-00b61070)
- 新版 `00b61150`（命令位置の公開資料なし） · `00b61158`（命令位置の公開資料なし） · `00b61138`（命令位置の公開資料なし）

~~~diff
- 00b61088 ["INT_ADD", "register:40f0:8", ["const:b61088:8", "const:4:8"]]
- 00b61088 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61150 ["INT_ADD", "register:40f0:8", ["const:b61150:8", "const:4:8"]]
+ 00b61150 ["CALL", null, ["callee:00bde040:8"]]
- 00b61088 bytes c2f30194
+ 00b61150 bytes bcf30194
- 00b61090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b61090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b61158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61090 bytes 603a02f9
+ 00b61158 bytes 609a02f9
- 00b61070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b61070 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00b61138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61070 bytes 683a42f9
+ 00b61138 bytes 689a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-029d4a519500d285a40614d7ab860b82"></a>

### [`00b610a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610a4.md) → [`00b6116c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6116c.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b610d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6119c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61180",
      "incomplete_value": true,
      "site": "00b61180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b610b8",
      "incomplete_value": true,
      "site": "00b610b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6117c",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61180",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b610d8"
      ]
    ],
    [
      "unmatched:00b610c0",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6117c",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61180",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b611a0"
      ]
    ],
    [
      "00b61188",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b610cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610a4.md#insn-00b610cc) · [`00b610d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610a4.md#insn-00b610d4) · [`00b610e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610a4.md#insn-00b610e4)
- 新版 `00b61194`（命令位置の公開資料なし）

~~~diff
- 00b610cc ["INT_ADD", "register:40f0:8", ["const:b610cc:8", "const:4:8"]]
- 00b610cc ["CALL", null, ["callee:00bde040:8"]]
+ 00b61194 ["INT_ADD", "register:40f0:8", ["const:b61194:8", "const:4:8"]]
+ 00b61194 ["CALL", null, ["callee:00bde040:8"]]
- 00b610cc bytes b1f30194
+ 00b61194 bytes abf30194
- 00b610d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00b610d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b610d4 bytes 603a02f9
- 00b610e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b610e4 ["RETURN", null, ["register:0:8"]]
- 00b610e4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7084665af9eba9795f9db605a116d8"></a>

### [`00b61160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61160.md) → [`00b61228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61228.md) _ZN8firebase4auth20additional_user_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61160",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61164",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61168",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61228",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6122c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b61230",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61160.md#insn-00b61160) · [`00b61164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61160.md#insn-00b61164) · [`00b61168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61160.md#insn-00b61168)

~~~diff
- 00b61160 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b61160 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b61160 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61160 bytes f50f1df8
- 00b61164 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61164 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61164 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61164 bytes f44f01a9
- 00b61168 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61168 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61168 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b61168 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61168 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9c3b959d2d563d02b9893ca10c4aa3"></a>

### [`00b611d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b611d0.md) → [`00b61298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61298.md) _ZN8firebase4auth20additional_user_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b612d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b611ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b611e4",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b611ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b612dc"
      ]
    ],
    [
      "unmatched:00b611f4",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b612ac",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b612b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b612dc"
      ]
    ],
    [
      "00b612bc",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b611ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b611d0.md#insn-00b611ec) · [`00b61208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b611d0.md#insn-00b61208) · [`00b61210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b611d0.md#insn-00b61210)
- 新版 `00b612d0`（命令位置の公開資料なし）

~~~diff
- 00b611ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b611ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b611ec bytes 410100b5
- 00b61208 ["INT_ADD", "register:40f0:8", ["const:b61208:8", "const:4:8"]]
- 00b61208 ["CALL", null, ["callee:00bde040:8"]]
+ 00b612d0 ["INT_ADD", "register:40f0:8", ["const:b612d0:8", "const:4:8"]]
+ 00b612d0 ["CALL", null, ["callee:00bde040:8"]]
- 00b61208 bytes 62f30194
+ 00b612d0 bytes 5cf30194
- 00b61210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:470:8"]]
- 00b61210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61210 bytes 803a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

