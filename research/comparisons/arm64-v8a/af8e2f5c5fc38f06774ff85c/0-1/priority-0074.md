# v15.7.2 → v15.7.3 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-e0bf0f5373002be0cf42c5e216c404c2"></a>

### [`00b71fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71fc4.md) → [`00b7208c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7208c.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b720a8",
      "incomplete_value": true,
      "site": "00b720ac",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b71ff4",
      "incomplete_value": true,
      "site": "00b71ffc",
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
      "definition_site": "00b71ff8",
      "incomplete_value": false,
      "site": "00b71ffc",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b71fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71fc4.md#insn-00b71fe4) · [`00b71ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71fc4.md#insn-00b71ffc) · [`00b7200c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71fc4.md#insn-00b7200c)
- 新版 `00b720ac`（命令位置の公開資料なし） · `00b720c4`（命令位置の公開資料なし） · `00b720d4`（命令位置の公開資料なし）

~~~diff
- 00b71fe4 ["INT_ADD", "register:40f0:8", ["const:b71fe4:8", "const:4:8"]]
- 00b71fe4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b720ac ["INT_ADD", "register:40f0:8", ["const:b720ac:8", "const:4:8"]]
+ 00b720ac ["CALL", null, ["callee:00bddbd0:8"]]
- 00b71fe4 bytes cfae0194
+ 00b720ac bytes c9ae0194
- 00b71ffc ["INT_ADD", "register:40f0:8", ["const:b71ffc:8", "const:4:8"]]
- 00b71ffc ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b720c4 ["INT_ADD", "register:40f0:8", ["const:b720c4:8", "const:4:8"]]
+ 00b720c4 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b71ffc bytes 45af0194
+ 00b720c4 bytes 3faf0194
- 00b7200c ["INT_ADD", "register:40f0:8", ["const:b7200c:8", "const:4:8"]]
- 00b7200c ["CALL", null, ["callee:00bddf40:8"]]
+ 00b720d4 ["INT_ADD", "register:40f0:8", ["const:b720d4:8", "const:4:8"]]
+ 00b720d4 ["CALL", null, ["callee:00bddf40:8"]]
- 00b7200c bytes a1af0194
+ 00b720d4 bytes 9baf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd3b72aa5aa5c6c93501a6eac75968c7"></a>

### [`00b72174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72174.md) → [`00b7223c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7223c.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72280",
      "incomplete_value": true,
      "site": "00b72284",
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
    "old": {
      "definition_site": "00b721b8",
      "incomplete_value": true,
      "site": "00b721bc",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b721bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72174.md#insn-00b721bc) · [`00b72194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72174.md#insn-00b72194) · [`00b721a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72174.md#insn-00b721a0)
- 新版 `00b72284`（命令位置の公開資料なし） · `00b7225c`（命令位置の公開資料なし） · `00b72268`（命令位置の公開資料なし）

~~~diff
- 00b721bc ["INT_ADD", "register:40f0:8", ["const:b721bc:8", "const:4:8"]]
- 00b721bc ["CALL", null, ["callee:00bddf40:8"]]
+ 00b72284 ["INT_ADD", "register:40f0:8", ["const:b72284:8", "const:4:8"]]
+ 00b72284 ["CALL", null, ["callee:00bddf40:8"]]
- 00b721bc bytes 35af0194
+ 00b72284 bytes 2faf0194
- 00b72194 ["INT_ADD", "register:40f0:8", ["const:b72194:8", "const:4:8"]]
- 00b72194 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7225c ["INT_ADD", "register:40f0:8", ["const:b7225c:8", "const:4:8"]]
+ 00b7225c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b72194 bytes 63ae0194
+ 00b7225c bytes 5dae0194
- 00b721a0 ["INT_ADD", "register:40f0:8", ["const:b721a0:8", "const:4:8"]]
- 00b721a0 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b72268 ["INT_ADD", "register:40f0:8", ["const:b72268:8", "const:4:8"]]
+ 00b72268 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b721a0 bytes 64ae0194
+ 00b72268 bytes 5eae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a661f98fc6ac99d234ae3cbe8bc58cff"></a>

### [`00b72324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72324.md) → [`00b723ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b723ec.md) _ZNK8firebase4auth4User27UpdateUserProfileLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72408",
      "incomplete_value": true,
      "site": "00b7240c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b72368",
      "incomplete_value": true,
      "site": "00b7236c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b72374",
      "incomplete_value": true,
      "site": "00b72378",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b72344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72324.md#insn-00b72344) · [`00b7236c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72324.md#insn-00b7236c) · [`00b72378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72324.md#insn-00b72378)
- 新版 `00b7240c`（命令位置の公開資料なし） · `00b72434`（命令位置の公開資料なし） · `00b72440`（命令位置の公開資料なし）

~~~diff
- 00b72344 ["INT_ADD", "register:40f0:8", ["const:b72344:8", "const:4:8"]]
- 00b72344 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7240c ["INT_ADD", "register:40f0:8", ["const:b7240c:8", "const:4:8"]]
+ 00b7240c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b72344 bytes f7ad0194
+ 00b7240c bytes f1ad0194
- 00b7236c ["INT_ADD", "register:40f0:8", ["const:b7236c:8", "const:4:8"]]
- 00b7236c ["CALL", null, ["callee:00bddf40:8"]]
+ 00b72434 ["INT_ADD", "register:40f0:8", ["const:b72434:8", "const:4:8"]]
+ 00b72434 ["CALL", null, ["callee:00bddf40:8"]]
- 00b7236c bytes c9ae0194
+ 00b72434 bytes c3ae0194
- 00b72378 ["INT_ADD", "register:40f0:8", ["const:b72378:8", "const:4:8"]]
- 00b72378 ["CALL", null, ["callee:00bddea0:8"]]
+ 00b72440 ["INT_ADD", "register:40f0:8", ["const:b72440:8", "const:4:8"]]
+ 00b72440 ["CALL", null, ["callee:00bddea0:8"]]
- 00b72378 bytes 9eae0194
+ 00b72440 bytes 98ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2e77d12c53554a2c9a36463740c2b70"></a>

### [`00b723b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b723b4.md) → [`00b7247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7247c.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b723b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b723b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b723b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b723b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b723b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b723bc",
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
      "00b7247c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b72480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b72484",
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

- 旧版 [`00b723b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b723b4.md#insn-00b723b4) · [`00b723b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b723b4.md#insn-00b723b8) · [`00b723bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b723b4.md#insn-00b723bc)

~~~diff
- 00b723b4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b723b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b723b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b723b4 bytes f50f1df8
- 00b723b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b723b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b723b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b723b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b723b8 bytes f44f01a9
- 00b723bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b723bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b723bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b723bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b723bc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d61210ee8e1ce0c6fcdac1e562d806d"></a>

### [`00b72444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72444.md) → [`00b7250c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7250c.md) _ZNK8firebase4auth4User16DeleteLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72444",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b72448",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7244c",
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
      "00b7250c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b72510",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b72514",
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

- 旧版 [`00b72444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72444.md#insn-00b72444) · [`00b72448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72444.md#insn-00b72448) · [`00b7244c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72444.md#insn-00b7244c)

~~~diff
- 00b72444 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b72444 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b72444 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b72444 bytes f50f1df8
- 00b72448 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b72448 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b72448 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b72448 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b72448 bytes f44f01a9
- 00b7244c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7244c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7244c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7244c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7244c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0560a20c49f2f1d83225cac7c0245da0"></a>

### [`00b724d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b724d4.md) → [`00b7259c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7259c.md) _ZNK8firebase4auth4User37UpdatePhoneNumberCredentialLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b724f0",
      "incomplete_value": true,
      "site": "00b724f4",
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
            "const:18:8"
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
      "definition_site": "00b725e0",
      "incomplete_value": true,
      "site": "00b725e4",
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
    "old": {
      "definition_site": "00b72518",
      "incomplete_value": true,
      "site": "00b7251c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72538"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b724f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b724d4.md#insn-00b724f4) · [`00b7251c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b724d4.md#insn-00b7251c) · [`00b72538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b724d4.md#insn-00b72538)
- 新版 `00b725bc`（命令位置の公開資料なし） · `00b725e4`（命令位置の公開資料なし）

~~~diff
- 00b724f4 ["INT_ADD", "register:40f0:8", ["const:b724f4:8", "const:4:8"]]
- 00b724f4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b725bc ["INT_ADD", "register:40f0:8", ["const:b725bc:8", "const:4:8"]]
+ 00b725bc ["CALL", null, ["callee:00bddbd0:8"]]
- 00b724f4 bytes 8bad0194
+ 00b725bc bytes 85ad0194
- 00b7251c ["INT_ADD", "register:40f0:8", ["const:b7251c:8", "const:4:8"]]
- 00b7251c ["CALL", null, ["callee:00bddf40:8"]]
+ 00b725e4 ["INT_ADD", "register:40f0:8", ["const:b725e4:8", "const:4:8"]]
+ 00b725e4 ["CALL", null, ["callee:00bddf40:8"]]
- 00b7251c bytes 5dae0194
+ 00b725e4 bytes 57ae0194
- 00b72538 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72538 ["RETURN", null, ["register:0:8"]]
- 00b72538 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29de0f10c686c01d28ce65911a993c15"></a>

### [`00b72564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72564.md) → [`00b7262c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7262c.md) _ZN8firebase4auth4User18GetTokenThreadSafeEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00848b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00848/00848b34.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb00.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbb0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 13.33% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7258c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72654"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72660",
      "incomplete_value": true,
      "site": "00b72664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7258c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b725b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b72654",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b72680",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7258c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72564.md#insn-00b7258c) · [`00b7259c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72564.md#insn-00b7259c) · [`00b725b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72564.md#insn-00b725b8)
- 新版 `00b72664`（命令位置の公開資料なし）

~~~diff
- 00b7258c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7258c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b7258c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b7258c bytes a8831df8
- 00b7259c ["INT_ADD", "register:40f0:8", ["const:b7259c:8", "const:4:8"]]
- 00b7259c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b72664 ["INT_ADD", "register:40f0:8", ["const:b72664:8", "const:4:8"]]
+ 00b72664 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b7259c bytes 61ad0194
+ 00b72664 bytes 5bad0194
- 00b725b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b725b8 ["INT_ADD", "register:40f0:8", ["const:b725b8:8", "const:4:8"]]
- 00b725b8 ["CALLIND", null, ["register:0:8"]]
- 00b725b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ccd2e4c76081a98b5af62e8d0608c6e"></a>

### [`00b726f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b726f0.md) → [`00b727b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b727b8.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00be0a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a70.md) [`00be0a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a80.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`00be0b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b20.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 90.91% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b727d4",
      "incomplete_value": true,
      "site": "00b727d8",
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
      "definition_site": "00b7270c",
      "incomplete_value": true,
      "site": "00b72710",
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
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b727cc",
      "READ",
      [
        "storage",
        "00c1ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00b727d8",
      "DATA",
      [
        "storage",
        "00c12ad0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b727cc",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b727d8",
      "DATA",
      [
        "storage",
        "00c12b80",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b726f0.md#insn-00b72704) · [`00b72750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b726f0.md#insn-00b72750) · [`00b72760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b726f0.md#insn-00b72760)
- 新版 `00b727cc`（命令位置の公開資料なし） · `00b72818`（命令位置の公開資料なし） · `00b72828`（命令位置の公開資料なし）

~~~diff
- 00b72704 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a98:8"]]
- 00b72704 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b727cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b48:8"]]
+ 00b727cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b72704 bytes 294d45f9
+ 00b727cc bytes 29a545f9
- 00b72750 ["INT_ADD", "register:40f0:8", ["const:b72750:8", "const:4:8"]]
- 00b72750 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b72818 ["INT_ADD", "register:40f0:8", ["const:b72818:8", "const:4:8"]]
+ 00b72818 ["CALL", null, ["callee:00bdb010:8"]]
- 00b72750 bytes 04a20194
+ 00b72818 bytes fea10194
- 00b72760 ["INT_ADD", "register:40f0:8", ["const:b72760:8", "const:4:8"]]
- 00b72760 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b72828 ["INT_ADD", "register:40f0:8", ["const:b72828:8", "const:4:8"]]
+ 00b72828 ["CALL", null, ["callee:00bdb010:8"]]
- 00b72760 bytes 00a20194
+ 00b72828 bytes faa10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b2fe330445fcc34eacd6d000af3c59"></a>

### [`00b72950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72950.md) → [`00b72a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a18.md) _ZNSt13exception_ptrD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) · 呼出先 1件 [`00be0e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e10.md)
- 新版 呼出元 1件 [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) · 呼出先 1件 [`00be0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ec0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72958",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0ec0"
      ]
    ]
  ],
  "added": [
    [
      "00b72a20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0ec0"
      ]
    ]
  ]
}
~~~


<a id="compare-3102606b7a819dc4019dd4efd0ef5181"></a>

### [`00b729c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b729c4.md) → [`00b72a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a8c.md) _ZNSt13exception_ptr31__from_native_exception_pointerEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bdb400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb400.md) · 呼出先 1件 [`00be0e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e20.md)
- 新版 呼出元 1件 [`00bdb4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4b0.md) · 呼出先 1件 [`00be0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ed0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b729cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0ed0"
      ]
    ]
  ],
  "added": [
    [
      "00b72a94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0ed0"
      ]
    ]
  ]
}
~~~


<a id="compare-a03479fc966517ffe382d78f6575acfa"></a>

### [`00b72a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a0c.md) → [`00b72ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72ad4.md) _ZSt17current_exceptionv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb610.md) · 呼出先 1件 [`00be0e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e40.md)
- 新版 呼出元 1件 [`00bdb6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6c0.md) · 呼出先 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a0c.md#insn-00b72a20)
- 新版 `00b72ae8`（命令位置の公開資料なし）

~~~diff
- 00b72a20 ["INT_ADD", "register:40f0:8", ["const:b72a20:8", "const:4:8"]]
- 00b72a20 ["CALL", null, ["callee:00be0ef0:8"]]
+ 00b72ae8 ["INT_ADD", "register:40f0:8", ["const:b72ae8:8", "const:4:8"]]
+ 00b72ae8 ["CALL", null, ["callee:00be0ef0:8"]]
- 00b72a20 bytes 08b90194
+ 00b72ae8 bytes 02b90194
~~~


<a id="compare-e2d1d1653b4c1137b49e98efbec11d3c"></a>

### [`00b72a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a50.md) → [`00b72b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b18.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f00.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a50.md#insn-00b72a64)
- 新版 `00b72b2c`（命令位置の公開資料なし）

~~~diff
- 00b72a64 ["INT_ADD", "register:40f0:8", ["const:b72a64:8", "const:4:8"]]
- 00b72a64 ["CALL", null, ["callee:00be0f00:8"]]
+ 00b72b2c ["INT_ADD", "register:40f0:8", ["const:b72b2c:8", "const:4:8"]]
+ 00b72b2c ["CALL", null, ["callee:00be0f00:8"]]
- 00b72a64 bytes fbb80194
+ 00b72b2c bytes f5b80194
~~~


<a id="compare-d868a0376794dee526973560ecbfba95"></a>

### [`00b72a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a7c.md) → [`00b72b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md) _ZNKSt16nested_exception14rethrow_nestedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md) [`00bdb570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb570.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md) [`00bdb620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb620.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72b60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72b5c",
      "incomplete_value": true,
      "site": "00b72b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b72a94",
      "incomplete_value": true,
      "site": "00b72aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
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
      "unmatched:00b72a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b72b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a7c.md#insn-00b72a98) · [`00b72aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a7c.md#insn-00b72aa0) · [`00b72ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a7c.md#insn-00b72ab4)
- 新版 `00b72b68`（命令位置の公開資料なし） · `00b72b7c`（命令位置の公開資料なし）

~~~diff
- 00b72a98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b72a98 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b72a98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b72a98 bytes ff0700f9
- 00b72aa0 ["INT_ADD", "register:40f0:8", ["const:b72aa0:8", "const:4:8"]]
- 00b72aa0 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b72b68 ["INT_ADD", "register:40f0:8", ["const:b72b68:8", "const:4:8"]]
+ 00b72b68 ["CALL", null, ["callee:00bdb450:8"]]
- 00b72aa0 bytes 40a20194
+ 00b72b68 bytes 3aa20194
- 00b72ab4 ["INT_ADD", "register:40f0:8", ["const:b72ab4:8", "const:4:8"]]
- 00b72ab4 ["CALL", null, ["callee:00bdb610:8"]]
+ 00b72b7c ["INT_ADD", "register:40f0:8", ["const:b72b7c:8", "const:4:8"]]
+ 00b72b7c ["CALL", null, ["callee:00bdb610:8"]]
- 00b72ab4 bytes aba20194
+ 00b72b7c bytes a5a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e55e00125bf0d35ff1dc0c2464b0a1eb"></a>

### [`00b7320c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md) → [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md) FUN_00b732d4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b72aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72aec.md) · 呼出先 4件 [`00b73260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73260.md) [`00bbade0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00b72bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72bb4.md) · 呼出先 4件 [`00b73328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73328.md) [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73308",
      "incomplete_value": true,
      "site": "00b73310",
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73240",
      "incomplete_value": true,
      "site": "00b73248",
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
                "const:b48:8"
              ]
            ]
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
      "definition_site": "00b7330c",
      "incomplete_value": true,
      "site": "00b73310",
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
                "const:c00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73244",
      "incomplete_value": true,
      "site": "00b73248",
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
                "const:b50:8"
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
      "00b73308",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b73308",
      "PARAM",
      [
        "storage",
        "00c16a08",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7330c",
      "READ",
      [
        "storage",
        "00c1bb50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b73308",
      "READ",
      [
        "storage",
        "00c1bbf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b73308",
      "PARAM",
      [
        "storage",
        "00c16ab8",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7330c",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md#insn-00b73248) · [`00b73224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md#insn-00b73224) · [`00b73230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md#insn-00b73230)
- 新版 `00b73310`（命令位置の公開資料なし） · `00b732ec`（命令位置の公開資料なし） · `00b732f8`（命令位置の公開資料なし）

~~~diff
- 00b73248 ["INT_ADD", "register:40f0:8", ["const:b73248:8", "const:4:8"]]
- 00b73248 ["CALL", null, ["callee:00bdb070:8"]]
+ 00b73310 ["INT_ADD", "register:40f0:8", ["const:b73310:8", "const:4:8"]]
+ 00b73310 ["CALL", null, ["callee:00bdb070:8"]]
- 00b73248 bytes 5e9f0194
+ 00b73310 bytes 589f0194
- 00b73224 ["INT_ADD", "register:40f0:8", ["const:b73224:8", "const:4:8"]]
- 00b73224 ["CALL", null, ["callee:00bdb050:8"]]
+ 00b732ec ["INT_ADD", "register:40f0:8", ["const:b732ec:8", "const:4:8"]]
+ 00b732ec ["CALL", null, ["callee:00bdb050:8"]]
- 00b73224 bytes 5f9f0194
+ 00b732ec bytes 599f0194
- 00b73230 ["INT_ADD", "register:40f0:8", ["const:b73230:8", "const:4:8"]]
- 00b73230 ["CALL", null, ["callee:00b73328:8"]]
+ 00b732f8 ["INT_ADD", "register:40f0:8", ["const:b732f8:8", "const:4:8"]]
+ 00b732f8 ["CALL", null, ["callee:00b73328:8"]]
- 00b73230 bytes 0c000094
+ 00b732f8 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e97e8e5e9417d5225c7aa12b2d18f863"></a>

### [`00b732cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732cc.md) → [`00b73394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73394.md) _ZNKSt6__ndk112bad_weak_ptr4whatEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b7339c",
      "incomplete_value": false,
      "site": "00b733a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:34f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b732d4",
      "incomplete_value": false,
      "site": "00b732d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:349:8"
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
      "00b7339c",
      "DATA",
      [
        "storage",
        "002aa349",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7339c",
      "DATA",
      [
        "storage",
        "002aa34f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b732d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b732cc.md#insn-00b732d4)
- 新版 `00b7339c`（命令位置の公開資料なし）

~~~diff
- 00b732d4 ["COPY", "tmp:0:8", ["const:349:8"]]
- 00b732d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b732d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b732d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7339c ["COPY", "tmp:0:8", ["const:34f:8"]]
+ 00b7339c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7339c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7339c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b732d4 bytes 00240d91
+ 00b7339c bytes 003c0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a482d844b85acf1ac64e1570becdfc33"></a>

### [`00b735dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b735dc.md) → [`00b736a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736a4.md) _ZSt17__throw_bad_allocv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e80.md) · 呼出先 4件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdbaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbaf0.md)
- 新版 呼出元 1件 [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md) · 呼出先 4件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b736d0",
      "incomplete_value": true,
      "site": "00b736d8",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:fa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73608",
      "incomplete_value": true,
      "site": "00b73610",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef8:8"
              ]
            ]
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
      "definition_site": "00b736d4",
      "incomplete_value": true,
      "site": "00b736d8",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7360c",
      "incomplete_value": true,
      "site": "00b73610",
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
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "00b736d0",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00b736d0",
      "PARAM",
      [
        "storage",
        "00c167f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b736d4",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b736d0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b736d0",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b736d4",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b735dc.md#insn-00b73610) · [`00b735f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b735dc.md#insn-00b735f0) · [`00b735f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b735dc.md#insn-00b735f8)
- 新版 `00b736d8`（命令位置の公開資料なし） · `00b736b8`（命令位置の公開資料なし） · `00b736c0`（命令位置の公開資料なし）

~~~diff
- 00b73610 ["INT_ADD", "register:40f0:8", ["const:b73610:8", "const:4:8"]]
- 00b73610 ["CALL", null, ["callee:00bdb070:8"]]
+ 00b736d8 ["INT_ADD", "register:40f0:8", ["const:b736d8:8", "const:4:8"]]
+ 00b736d8 ["CALL", null, ["callee:00bdb070:8"]]
- 00b73610 bytes 6c9e0194
+ 00b736d8 bytes 669e0194
- 00b735f0 ["INT_ADD", "register:40f0:8", ["const:b735f0:8", "const:4:8"]]
- 00b735f0 ["CALL", null, ["callee:00bdb050:8"]]
+ 00b736b8 ["INT_ADD", "register:40f0:8", ["const:b736b8:8", "const:4:8"]]
+ 00b736b8 ["CALL", null, ["callee:00bdb050:8"]]
- 00b735f0 bytes 6c9e0194
+ 00b736b8 bytes 669e0194
- 00b735f8 ["INT_ADD", "register:40f0:8", ["const:b735f8:8", "const:4:8"]]
- 00b735f8 ["CALL", null, ["callee:00bdbba0:8"]]
+ 00b736c0 ["INT_ADD", "register:40f0:8", ["const:b736c0:8", "const:4:8"]]
+ 00b736c0 ["CALL", null, ["callee:00bdbba0:8"]]
- 00b735f8 bytes 3ea10194
+ 00b736c0 bytes 38a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c313057e6a9c90722a034164c8ab6a8"></a>

### [`00b73614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73614.md) → [`00b736dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b736dc.md) _ZNSt11logic_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e90.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00be0f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f40.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b736fc",
      "incomplete_value": true,
      "site": "00b73700",
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
      "definition_site": "00b73634",
      "incomplete_value": true,
      "site": "00b73638",
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
    "ordinal": 6,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b736f8",
      "READ",
      [
        "storage",
        "00c1bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00b73700",
      "DATA",
      [
        "storage",
        "00c16830",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b736f8",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b73700",
      "DATA",
      [
        "storage",
        "00c168e0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73614.md#insn-00b73630) · [`00b73650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73614.md#insn-00b73650) · [`00b7365c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73614.md#insn-00b7365c)
- 新版 `00b736f8`（命令位置の公開資料なし） · `00b73718`（命令位置の公開資料なし） · `00b73724`（命令位置の公開資料なし）

~~~diff
- 00b73630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00b73630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b736f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
+ 00b736f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b73630 bytes 08b145f9
+ 00b736f8 bytes 080946f9
- 00b73650 ["INT_ADD", "register:40f0:8", ["const:b73650:8", "const:4:8"]]
- 00b73650 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b73718 ["INT_ADD", "register:40f0:8", ["const:b73718:8", "const:4:8"]]
+ 00b73718 ["CALL", null, ["callee:00bdb140:8"]]
- 00b73650 bytes 909e0194
+ 00b73718 bytes 8a9e0194
- 00b7365c ["INT_ADD", "register:40f0:8", ["const:b7365c:8", "const:4:8"]]
- 00b7365c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b73724 ["INT_ADD", "register:40f0:8", ["const:b73724:8", "const:4:8"]]
+ 00b73724 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7365c bytes 399e0194
+ 00b73724 bytes 339e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c644f0dfc28ae89a4953c27b913271a9"></a>

### [`00b73768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73768.md) → [`00b73830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7384c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73850",
      "incomplete_value": true,
      "site": "00b73858",
      "value": [
        "INT_SUB",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73788",
      "incomplete_value": true,
      "site": "00b73790",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:8:8"
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

- 旧版 [`00b73784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73768.md#insn-00b73784) · [`00b73790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73768.md#insn-00b73790)
- 新版 `00b73858`（命令位置の公開資料なし） · `00b7384c`（命令位置の公開資料なし）

~~~diff
- 00b73784 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b73784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b73784 bytes 080400f9
- 00b73790 ["INT_ADD", "register:40f0:8", ["const:b73790:8", "const:4:8"]]
- 00b73790 ["CALL", null, ["callee:00bd6df0:8"]]
+ 00b73858 ["INT_ADD", "register:40f0:8", ["const:b73858:8", "const:4:8"]]
+ 00b73858 ["CALL", null, ["callee:00bd6df0:8"]]
- 00b73790 bytes 688d0194
+ 00b73858 bytes 668d0194
+ 00b7384c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
+ 00b7384c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b7384c bytes 080400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85f1d7013c782b4f73daf358a94ec6c"></a>

### [`00b737c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b737c4.md) → [`00b7388c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7388c.md) _ZNSt13runtime_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ea0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00be0f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f50.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b738ac",
      "incomplete_value": true,
      "site": "00b738b0",
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
      "definition_site": "00b737e4",
      "incomplete_value": true,
      "site": "00b737e8",
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
    "ordinal": 6,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b738a8",
      "READ",
      [
        "storage",
        "00c1bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00b738b0",
      "DATA",
      [
        "storage",
        "00c16858",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b738a8",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b738b0",
      "DATA",
      [
        "storage",
        "00c16908",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b737e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b737c4.md#insn-00b737e0) · [`00b73800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b737c4.md#insn-00b73800) · [`00b7380c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b737c4.md#insn-00b7380c)
- 新版 `00b738a8`（命令位置の公開資料なし） · `00b738c8`（命令位置の公開資料なし） · `00b738d4`（命令位置の公開資料なし）

~~~diff
- 00b737e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00b737e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b738a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 00b738a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b737e0 bytes 08b545f9
+ 00b738a8 bytes 080d46f9
- 00b73800 ["INT_ADD", "register:40f0:8", ["const:b73800:8", "const:4:8"]]
- 00b73800 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b738c8 ["INT_ADD", "register:40f0:8", ["const:b738c8:8", "const:4:8"]]
+ 00b738c8 ["CALL", null, ["callee:00bdb140:8"]]
- 00b73800 bytes 249e0194
+ 00b738c8 bytes 1e9e0194
- 00b7380c ["INT_ADD", "register:40f0:8", ["const:b7380c:8", "const:4:8"]]
- 00b7380c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b738d4 ["INT_ADD", "register:40f0:8", ["const:b738d4:8", "const:4:8"]]
+ 00b738d4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7380c bytes cd9d0194
+ 00b738d4 bytes c79d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613c5d8a14fc740e88454be3ae3494a6"></a>

### [`00b73858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73858.md) → [`00b73920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73920.md) _ZNSt13runtime_errorC2EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdd980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd980.md) [`00be0ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ec0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 2件 [`00bdda30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda30.md) [`00be0f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f70.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b73944",
      "incomplete_value": true,
      "site": "00b73948",
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
      "definition_site": "00b7387c",
      "incomplete_value": true,
      "site": "00b73880",
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
    "ordinal": 6,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b73940",
      "READ",
      [
        "storage",
        "00c1bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00b73948",
      "DATA",
      [
        "storage",
        "00c16858",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b73940",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b73948",
      "DATA",
      [
        "storage",
        "00c16908",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73858.md#insn-00b73878) · [`00b73888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73858.md#insn-00b73888) · [`00b73894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73858.md#insn-00b73894)
- 新版 `00b73940`（命令位置の公開資料なし） · `00b73950`（命令位置の公開資料なし） · `00b7395c`（命令位置の公開資料なし）

~~~diff
- 00b73878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00b73878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b73940 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 00b73940 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b73878 bytes 08b545f9
+ 00b73940 bytes 080d46f9
- 00b73888 ["INT_ADD", "register:40f0:8", ["const:b73888:8", "const:4:8"]]
- 00b73888 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b73950 ["INT_ADD", "register:40f0:8", ["const:b73950:8", "const:4:8"]]
+ 00b73950 ["CALL", null, ["callee:00bdb140:8"]]
- 00b73888 bytes 029e0194
+ 00b73950 bytes fc9d0194
- 00b73894 ["INT_ADD", "register:40f0:8", ["const:b73894:8", "const:4:8"]]
- 00b73894 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7395c ["INT_ADD", "register:40f0:8", ["const:b7395c:8", "const:4:8"]]
+ 00b7395c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b73894 bytes ab9d0194
+ 00b7395c bytes a59d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89f44825e307fab34a147126c73888d"></a>

### [`00b73974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73974.md) → [`00b73a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) · 呼出先 4件 [`00bbade0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00be0ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ec0.md)
- 新版 呼出元 1件 [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) · 呼出先 4件 [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be0f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73a70",
      "incomplete_value": true,
      "site": "00b73a78",
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
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b739a8",
      "incomplete_value": true,
      "site": "00b739b0",
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
                "const:b70:8"
              ]
            ]
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
      "definition_site": "00b73a74",
      "incomplete_value": true,
      "site": "00b73a78",
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b739ac",
      "incomplete_value": true,
      "site": "00b739b0",
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
                "const:b78:8"
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
      "00b73a70",
      "READ",
      [
        "storage",
        "00c1bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00b73a70",
      "PARAM",
      [
        "storage",
        "00c169b0",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73a74",
      "READ",
      [
        "storage",
        "00c1bb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b73a70",
      "READ",
      [
        "storage",
        "00c1bc20",
        null,
        "pointer"
      ]
    ],
    [
      "00b73a70",
      "PARAM",
      [
        "storage",
        "00c16a60",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b73a74",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b739b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73974.md#insn-00b739b0) · [`00b7398c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73974.md#insn-00b7398c) · [`00b73998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73974.md#insn-00b73998)
- 新版 `00b73a78`（命令位置の公開資料なし） · `00b73a54`（命令位置の公開資料なし） · `00b73a60`（命令位置の公開資料なし）

~~~diff
- 00b739b0 ["INT_ADD", "register:40f0:8", ["const:b739b0:8", "const:4:8"]]
- 00b739b0 ["CALL", null, ["callee:00bdb070:8"]]
+ 00b73a78 ["INT_ADD", "register:40f0:8", ["const:b73a78:8", "const:4:8"]]
+ 00b73a78 ["CALL", null, ["callee:00bdb070:8"]]
- 00b739b0 bytes 849d0194
+ 00b73a78 bytes 7e9d0194
- 00b7398c ["INT_ADD", "register:40f0:8", ["const:b7398c:8", "const:4:8"]]
- 00b7398c ["CALL", null, ["callee:00bdb050:8"]]
+ 00b73a54 ["INT_ADD", "register:40f0:8", ["const:b73a54:8", "const:4:8"]]
+ 00b73a54 ["CALL", null, ["callee:00bdb050:8"]]
- 00b7398c bytes 859d0194
+ 00b73a54 bytes 7f9d0194
- 00b73998 ["INT_ADD", "register:40f0:8", ["const:b73998:8", "const:4:8"]]
- 00b73998 ["CALL", null, ["callee:00be0f70:8"]]
+ 00b73a60 ["INT_ADD", "register:40f0:8", ["const:b73a60:8", "const:4:8"]]
+ 00b73a60 ["CALL", null, ["callee:00be0f70:8"]]
- 00b73998 bytes 4ab50194
+ 00b73a60 bytes 44b50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca119479044fa37ced6a720e68e28eb7"></a>

### [`00b739c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b739c8.md) → [`00b73a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a90.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb120.md) · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md)
- 新版 呼出元 1件 [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md) · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 76.92% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73b24",
      "incomplete_value": true,
      "site": "00b73b30",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              [
                "live",
                "register:4008:8"
              ]
            ]
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b73a5c",
      "incomplete_value": true,
      "site": "00b73a68",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:4008:8"
              ]
            ]
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b73aa8",
      "incomplete_value": true,
      "site": "00b73ab4",
      "value": [
        "live",
        "register:40d0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b73aac",
      "incomplete_value": true,
      "site": "00b73ab4",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b73a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b739c8.md#insn-00b73a68) · [`00b73ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b739c8.md#insn-00b73ab4) · [`00b73b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b739c8.md#insn-00b73b10)
- 新版 `00b73b30`（命令位置の公開資料なし） · `00b73b7c`（命令位置の公開資料なし） · `00b73bd8`（命令位置の公開資料なし）

~~~diff
- 00b73a68 ["INT_ADD", "register:40f0:8", ["const:b73a68:8", "const:4:8"]]
- 00b73a68 ["CALL", null, ["callee:00bde1d0:8"]]
+ 00b73b30 ["INT_ADD", "register:40f0:8", ["const:b73b30:8", "const:4:8"]]
+ 00b73b30 ["CALL", null, ["callee:00bde1d0:8"]]
- 00b73a68 bytes aea90194
+ 00b73b30 bytes a8a90194
- 00b73ab4 ["INT_ADD", "register:40f0:8", ["const:b73ab4:8", "const:4:8"]]
- 00b73ab4 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b73b7c ["INT_ADD", "register:40f0:8", ["const:b73b7c:8", "const:4:8"]]
+ 00b73b7c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b73ab4 bytes 4f9d0194
+ 00b73b7c bytes 499d0194
- 00b73b10 ["INT_ADD", "register:40f0:8", ["const:b73b10:8", "const:4:8"]]
- 00b73b10 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b73bd8 ["INT_ADD", "register:40f0:8", ["const:b73bd8:8", "const:4:8"]]
+ 00b73bd8 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b73b10 bytes 389d0194
+ 00b73bd8 bytes 329d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2ae9acdc81ef4b9d888b8bc5ee79ca"></a>

### [`00b73ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73ec8.md) → [`00b73f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f90.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ee0.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00be0f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f90.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 62.16% / 新版 67.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73f04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73f3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b73f04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74140"
      ]
    ],
    [
      "unmatched:00b73f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74058"
      ]
    ],
    [
      "unmatched:00b73f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7407c"
      ]
    ]
  ],
  "added": [
    [
      "00b73fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74140"
      ]
    ],
    [
      "00b74004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74058"
      ]
    ],
    [
      "00b74038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7407c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73ec8.md#insn-00b73f04) · [`00b73f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73ec8.md#insn-00b73f30) · [`00b73f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73ec8.md#insn-00b73f3c)

~~~diff
- 00b73f04 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b73f04 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00b73f04 bytes a30b0054
- 00b73f30 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b73f30 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b73f30 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b73f30 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b73f30 bytes 4801889a
- 00b73f3c ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00b73f3c bytes a2020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d42e3411e698d98e035a271e68693178"></a>

### [`00b741f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b741f0.md) → [`00b742b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b742b8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7420c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b741f0.md#insn-00b7420c) · [`00b7424c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b741f0.md#insn-00b7424c) · [`00b7426c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b741f0.md#insn-00b7426c)
- 新版 `00b742d4`（命令位置の公開資料なし） · `00b74314`（命令位置の公開資料なし） · `00b74334`（命令位置の公開資料なし）

~~~diff
- 00b7420c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
+ 00b742d4 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b7420c bytes e2030054
+ 00b742d4 bytes e2030054
- 00b7424c ["INT_ADD", "register:40f0:8", ["const:b7424c:8", "const:4:8"]]
- 00b7424c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b74314 ["INT_ADD", "register:40f0:8", ["const:b74314:8", "const:4:8"]]
+ 00b74314 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7424c bytes 3d9b0194
+ 00b74314 bytes 379b0194
- 00b7426c ["INT_ADD", "register:40f0:8", ["const:b7426c:8", "const:4:8"]]
- 00b7426c ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b74334 ["INT_ADD", "register:40f0:8", ["const:b74334:8", "const:4:8"]]
+ 00b74334 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b7426c bytes 619b0194
+ 00b74334 bytes 5b9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4137f181a8194638bfd19f42be33b8"></a>

### [`00b74484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md) → [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md) FUN_00b7454c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b745d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b745d0.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 2件 [`00b74698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74698.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 12.00% / 新版 10.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b744c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b744cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b744dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b744cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b745e4"
      ]
    ],
    [
      "unmatched:00b744dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74690"
      ]
    ],
    [
      "unmatched:00b744f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74614"
      ]
    ]
  ],
  "added": [
    [
      "00b74594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b745e4"
      ]
    ],
    [
      "00b745a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74690"
      ]
    ],
    [
      "00b745c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74614"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b744c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md#insn-00b744c4) · [`00b744cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md#insn-00b744cc) · [`00b744dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md#insn-00b744dc)

~~~diff
- 00b744c4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b744c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b744c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b744c4 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b744c4 bytes 4901899a
- 00b744cc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b744cc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b744cc ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b744cc bytes 89020054
- 00b744dc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b744dc ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b744dc bytes 63070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f590d078c7412c992367820e2d561718"></a>

### [`00b745d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b745d0.md) → [`00b74698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74698.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00b74484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b745ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b746b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "00b745ec"
      ],
      [
        "CONDITIONAL_JUMP",
        "00b746b4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b746b4",
      "incomplete_value": true,
      "site": "00b746dc",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "live",
                "register:4010:8"
              ],
              [
                "live",
                "register:4040:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b745ec",
      "incomplete_value": true,
      "site": "00b74614",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:102:1"
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
      "unmatched:00b745ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b746d8"
      ]
    ]
  ],
  "added": [
    [
      "00b746b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b746d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b745ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b745d0.md#insn-00b745ec) · [`00b74604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b745d0.md#insn-00b74604)
- 新版 `00b746b4`（命令位置の公開資料なし）

~~~diff
- 00b745ec ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b745ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b745ec bytes 23010054
+ 00b746b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b746b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b746b4 bytes 23010054
- 00b74604 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00b74604 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b74604 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b74604 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b74604 bytes 2101028b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-964e87ee8cff6d59371dbdd56ef7576f"></a>

### [`00b74c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c90.md) → [`00b74d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md) FUN_00b74d58

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00b74c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c18.md) [`00bb913c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb913c.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`00b74ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md) [`00bb9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c90.md#insn-00b74c94) · [`00b74ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c90.md#insn-00b74ce8) · [`00b74cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c90.md#insn-00b74cf8)
- 新版 `00b74d5c`（命令位置の公開資料なし） · `00b74db0`（命令位置の公開資料なし） · `00b74dc0`（命令位置の公開資料なし）

~~~diff
- 00b74c94 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b74c94 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b74d5c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 00b74d5c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b74c94 bytes 620400b4
+ 00b74d5c bytes 620400b4
- 00b74ce8 ["INT_ADD", "register:40f0:8", ["const:b74ce8:8", "const:4:8"]]
- 00b74ce8 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b74db0 ["INT_ADD", "register:40f0:8", ["const:b74db0:8", "const:4:8"]]
+ 00b74db0 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b74ce8 bytes c2980194
+ 00b74db0 bytes bc980194
- 00b74cf8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b74cf8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b74cf8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b74cf8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b74dc0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b74dc0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b74dc0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b74dc0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b74cf8 bytes 88000037
+ 00b74dc0 bytes 88000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6d0c015fbd5d37e34a25798aaabc36e"></a>

### [`00b74fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74fd0.md) → [`00b75098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75098.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74fd0.md#insn-00b74fec) · [`00b75010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74fd0.md#insn-00b75010)
- 新版 `00b750b4`（命令位置の公開資料なし） · `00b750d8`（命令位置の公開資料なし）

~~~diff
- 00b74fec ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74fec ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b74fec ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 00b750b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b750b4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b750b4 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00b74fec bytes c9000054
+ 00b750b4 bytes c9000054
- 00b75010 ["INT_ADD", "register:40f0:8", ["const:b75010:8", "const:4:8"]]
- 00b75010 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b750d8 ["INT_ADD", "register:40f0:8", ["const:b750d8:8", "const:4:8"]]
+ 00b750d8 ["CALL", null, ["callee:0041fddc:8"]]
- 00b75010 bytes 73abe297
+ 00b750d8 bytes 41abe297
~~~


<a id="compare-5de6dd4319d54fcad04e3e65f0bf4603"></a>

### [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) → [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) FUN_00b750e4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`00b75014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75014.md) [`00baf2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf2ac.md) [`00baf6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf6a8.md) [`00bb3af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md) [`00bb5b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5b08.md) · 呼出先 2件 [`00b74484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74484.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 8件 [`00b750dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750dc.md) [`00baf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md) [`00baf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md) [`00bb3bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3bbc.md) [`00bb5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md) · 呼出先 2件 [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md#insn-00b75038)
- 新版 `00b75100`（命令位置の公開資料なし）

~~~diff
- 00b75038 ["INT_ADD", "register:40f0:8", ["const:b75038:8", "const:4:8"]]
- 00b75038 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b75100 ["INT_ADD", "register:40f0:8", ["const:b75100:8", "const:4:8"]]
+ 00b75100 ["CALL", null, ["callee:00bdb140:8"]]
- 00b75038 bytes 16980194
+ 00b75100 bytes 10980194
~~~


<a id="compare-34d9b81495291c6ff53bb2aeefe067fc"></a>

### [`00b7522c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7522c.md) → [`00b752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md) FUN_00b752f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00b751d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b751d8.md) [`00b88204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88204.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 2件 [`00b752a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752a0.md) [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00b752b8",
      "incomplete_value": true,
      "site": "00b752d4",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7526c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7522c.md#insn-00b7526c) · [`00b7527c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7522c.md#insn-00b7527c) · [`00b75298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7522c.md#insn-00b75298)
- 新版 `00b75334`（命令位置の公開資料なし） · `00b75344`（命令位置の公開資料なし） · `00b75360`（命令位置の公開資料なし）

~~~diff
- 00b7526c ["INT_ADD", "register:40f0:8", ["const:b7526c:8", "const:4:8"]]
- 00b7526c ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b75334 ["INT_ADD", "register:40f0:8", ["const:b75334:8", "const:4:8"]]
+ 00b75334 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b7526c bytes 61970194
+ 00b75334 bytes 5b970194
- 00b7527c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7527c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b7527c ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00b75344 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b75344 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b75344 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00b7527c bytes e9020054
+ 00b75344 bytes e9020054
- 00b75298 ["INT_ADD", "register:40f0:8", ["const:b75298:8", "const:4:8"]]
- 00b75298 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b75360 ["INT_ADD", "register:40f0:8", ["const:b75360:8", "const:4:8"]]
+ 00b75360 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b75298 bytes 2a970194
+ 00b75360 bytes 24970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b6c1657624a7a2a7c3362fe699d6f22"></a>

### [`00b752e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b752e0.md) → [`00b753a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md) FUN_00b753a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b751d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b751d8.md) [`00b88204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88204.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 2件 [`00b752a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752a0.md) [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 52.63% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b752f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b752f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b753b8"
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
      "unmatched:00b752f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7530c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b753f4"
      ]
    ]
  ],
  "added": [
    [
      "00b753b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b753d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b753f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b752f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b752e0.md#insn-00b752f0) · [`00b7530c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b752e0.md#insn-00b7530c)
- 新版 `00b753b8`（命令位置の公開資料なし）

~~~diff
- 00b752f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b752f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b752f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b752f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b752f0 bytes f44f03a9
- 00b7530c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7530c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b7530c ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00b7530c bytes 09010054
+ 00b753b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b753b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b753b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
+ 00b753b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b753b8 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e25f48480f8a16aeea625ede205441"></a>

### [`00b75404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75404.md) → [`00b754cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b754cc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md)
- 新版 呼出元 1件 [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 41.67% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b75538",
      "incomplete_value": true,
      "site": "00b7554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7553c",
      "incomplete_value": true,
      "site": "00b7554c",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 5
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b75540",
      "incomplete_value": false,
      "site": "00b7554c",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 6
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b75484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75404.md#insn-00b75484) · [`00b75428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75404.md#insn-00b75428) · [`00b75460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75404.md#insn-00b75460)
- 新版 `00b7554c`（命令位置の公開資料なし） · `00b754f0`（命令位置の公開資料なし） · `00b75528`（命令位置の公開資料なし）

~~~diff
- 00b75484 ["INT_ADD", "register:40f0:8", ["const:b75484:8", "const:4:8"]]
- 00b75484 ["CALL", null, ["callee:00bde1d0:8"]]
+ 00b7554c ["INT_ADD", "register:40f0:8", ["const:b7554c:8", "const:4:8"]]
+ 00b7554c ["CALL", null, ["callee:00bde1d0:8"]]
- 00b75484 bytes 27a30194
+ 00b7554c bytes 21a30194
- 00b75428 ["INT_ADD", "register:40f0:8", ["const:b75428:8", "const:4:8"]]
- 00b75428 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b754f0 ["INT_ADD", "register:40f0:8", ["const:b754f0:8", "const:4:8"]]
+ 00b754f0 ["CALL", null, ["callee:00bdb140:8"]]
- 00b75428 bytes 1a970194
+ 00b754f0 bytes 14970194
- 00b75460 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00b75528 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b75460 bytes 62010054
+ 00b75528 bytes 62010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97270d85ccd164858747a6344f30caf"></a>

### [`00b754e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b754e8.md) → [`00b755b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b755b0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdb120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b754e8.md#insn-00b75534)
- 新版 `00b755fc`（命令位置の公開資料なし）

~~~diff
- 00b75534 ["INT_ADD", "register:40f0:8", ["const:b75534:8", "const:4:8"]]
- 00b75534 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b755fc ["INT_ADD", "register:40f0:8", ["const:b755fc:8", "const:4:8"]]
+ 00b755fc ["CALL", null, ["callee:0041fddc:8"]]
- 00b75534 bytes 2aaae297
+ 00b755fc bytes f8a9e297
~~~


<a id="compare-6c9a841c7ee4bec69a56ac0fadc11586"></a>

### [`00b75538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75538.md) → [`00b75600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75600.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertENS_11__wrap_iterIPKcEEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.26% / 新版 84.26%

CFGの説明率　旧版 31.43% / 新版 29.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7554c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7554c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75550"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7554c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b75550",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7559c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b756ac"
      ]
    ]
  ],
  "added": [
    [
      "00b75614",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b75618",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b75664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b756ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7554c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75538.md#insn-00b7554c) · [`00b75550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75538.md#insn-00b75550) · [`00b75584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75538.md#insn-00b75584)

~~~diff
- 00b7554c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7554c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7554c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b7554c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7554c bytes f65704a9
- 00b75550 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b75550 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b75550 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b75550 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b75550 bytes f44f05a9
- 00b75584 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b75584 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b75584 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b75584 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b75584 bytes 1c15809a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ea2df7bc7eeea0874794a787693436"></a>

### [`00b75784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75784.md) → [`00b7584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ef0.md) · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 1件 [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 53.85% / 新版 51.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b758a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b7596c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b75804",
      "incomplete_value": true,
      "site": "00b75824",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00b758a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b759b4"
      ]
    ]
  ],
  "added": [
    [
      "00b7596c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b759b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75784.md#insn-00b75824) · [`00b758a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75784.md#insn-00b758a4)
- 新版 `00b758ec`（命令位置の公開資料なし） · `00b7596c`（命令位置の公開資料なし）

~~~diff
- 00b75824 ["INT_ADD", "register:40f0:8", ["const:b75824:8", "const:4:8"]]
- 00b75824 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b758ec ["INT_ADD", "register:40f0:8", ["const:b758ec:8", "const:4:8"]]
+ 00b758ec ["CALL", null, ["callee:00be0fb0:8"]]
- 00b75824 bytes b7ad0194
+ 00b758ec bytes b1ad0194
- 00b758a4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b758a4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b758a4 ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
- 00b758a4 bytes 49020054
+ 00b7596c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b7596c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b7596c ["CBRANCH", null, ["local:b21:8", "tmp:1:1"]]
+ 00b7596c bytes 49020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09fea52d9f106986d2cc1088b3b27384"></a>

### [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) → [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) FUN_00b75a24

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 17件 [`00b75784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75784.md) [`00b75e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75e60.md) [`00b760a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760a0.md) [`00b760e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760e8.md) [`00b76294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76294.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 17件 [`00b7584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md) [`00b75f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md) [`00b76168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76168.md) [`00b761b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md) [`00b7635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7596c",
      "incomplete_value": false,
      "site": "00b75970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:246:8"
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
      "unmatched:00b7596c",
      "PARAM",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b75a34",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md#insn-00b75970) · [`00b7596c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md#insn-00b7596c)
- 新版 `00b75a38`（命令位置の公開資料なし） · `00b75a34`（命令位置の公開資料なし）

~~~diff
- 00b75970 ["INT_ADD", "register:40f0:8", ["const:b75970:8", "const:4:8"]]
- 00b75970 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00b75a38 ["INT_ADD", "register:40f0:8", ["const:b75a38:8", "const:4:8"]]
+ 00b75a38 ["CALL", null, ["callee:0041fdf0:8"]]
- 00b75970 bytes 20a9e297
+ 00b75a38 bytes eea8e297
- 00b7596c ["COPY", "tmp:0:8", ["const:246:8"]]
- 00b7596c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7596c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7596c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7596c bytes 00180991
+ 00b75a34 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00b75a34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b75a34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b75a34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b75a34 bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acde79e8a19f58a004169b45792090c5"></a>

### [`00b75af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75af4.md) → [`00b75bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75bbc.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5rfindEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 40.91% / 新版 39.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b75b6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75c5c"
      ]
    ],
    [
      "00b75c34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75c30"
      ]
    ]
  ],
  "added": [
    [
      "00b75c34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75c5c"
      ]
    ],
    [
      "00b75c54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75c30"
      ]
    ]
  ]
}
~~~


<a id="compare-537d89c2e251aadeb1608d22c5c4f335"></a>

### [`00b75bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75bb8.md) → [`00b75c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75c80.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 12.50% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b75cac"
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
      "unmatched:00b75be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75ce0"
      ]
    ],
    [
      "unmatched:00b75c34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75d34"
      ]
    ]
  ],
  "added": [
    [
      "00b75cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75ce0"
      ]
    ],
    [
      "00b75cfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75d34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75bb8.md#insn-00b75be4) · [`00b75c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75bb8.md#insn-00b75c34)
- 新版 `00b75cac`（命令位置の公開資料なし）

~~~diff
- 00b75be4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b75be4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b75be4 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00b75be4 bytes a8010054
- 00b75c34 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b75c34 bytes c2010054
+ 00b75cac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b75cac ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b75cac ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00b75cac bytes a8010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4438b0376741e3c45095af94be25ace"></a>

### [`00b75d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75d1c.md) → [`00b75de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75de4.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE16find_last_not_ofEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 30.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b75d78",
      "incomplete_value": true,
      "site": "00b75d80",
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

- 旧版 [`00b75d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75d1c.md#insn-00b75d80) · [`00b75d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75d1c.md#insn-00b75d5c) · [`00b75d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75d1c.md#insn-00b75d60)
- 新版 `00b75e48`（命令位置の公開資料なし）

~~~diff
- 00b75d80 ["INT_ADD", "register:40f0:8", ["const:b75d80:8", "const:4:8"]]
- 00b75d80 ["CALL", null, ["callee:00bdb5b0:8"]]
+ 00b75e48 ["INT_ADD", "register:40f0:8", ["const:b75e48:8", "const:4:8"]]
+ 00b75e48 ["CALL", null, ["callee:00bdb5b0:8"]]
- 00b75d80 bytes e0950194
+ 00b75e48 bytes da950194
- 00b75d5c ["INT_LEFT", "register:4040:8", ["register:4040:8", "const:2:8"]]
- 00b75d5c bytes 08f57ed3
- 00b75d60 ["INT_SUB", "register:4040:8", ["register:4040:8", "const:4:8"]]
- 00b75d60 bytes 081100d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c79b6e4f5e1c1b63c9fdce417d0f64a3"></a>

### [`00b75dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dc4.md) → [`00b75e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e8c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 6.25% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b75e9c"
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
      "unmatched:00b75dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b75ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b75e40"
      ]
    ],
    [
      "00b75ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b75e40"
      ]
    ]
  ],
  "added": [
    [
      "00b75e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b75ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75f08"
      ]
    ],
    [
      "00b75ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75f08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dc4.md#insn-00b75dd4) · [`00b75e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dc4.md#insn-00b75e24) · [`00b75e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dc4.md#insn-00b75e34)
- 新版 `00b75eec`（命令位置の公開資料なし）

~~~diff
- 00b75dd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b75dd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b75dd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b75dd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b75dd4 bytes f44f03a9
- 00b75e24 ["INT_ADD", "register:40f0:8", ["const:b75e24:8", "const:4:8"]]
- 00b75e24 ["CALL", null, ["callee:00bdb5b0:8"]]
+ 00b75eec ["INT_ADD", "register:40f0:8", ["const:b75eec:8", "const:4:8"]]
+ 00b75eec ["CALL", null, ["callee:00bdb5b0:8"]]
- 00b75e24 bytes b7950194
+ 00b75eec bytes b1950194
- 00b75e34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b75e34 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b75e34 bytes 21ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05c884a33c35db620fa103fa20f16d72"></a>

### [`00b760e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760e8.md) → [`00b761b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f30.md) · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 1件 [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 56.25% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b76154",
      "incomplete_value": true,
      "site": "00b7616c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7615c",
      "incomplete_value": true,
      "site": "00b7616c",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              [
                "live",
                "register:40a0:8"
              ]
            ]
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b76158",
      "incomplete_value": true,
      "site": "00b7616c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7616c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760e8.md#insn-00b7616c) · [`00b7611c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760e8.md#insn-00b7611c) · [`00b7614c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b760e8.md#insn-00b7614c)
- 新版 `00b76234`（命令位置の公開資料なし） · `00b761e4`（命令位置の公開資料なし） · `00b76214`（命令位置の公開資料なし）

~~~diff
- 00b7616c ["INT_ADD", "register:40f0:8", ["const:b7616c:8", "const:4:8"]]
- 00b7616c ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b76234 ["INT_ADD", "register:40f0:8", ["const:b76234:8", "const:4:8"]]
+ 00b76234 ["CALL", null, ["callee:00be0fb0:8"]]
- 00b7616c bytes 65ab0194
+ 00b76234 bytes 5fab0194
- 00b7611c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7611c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b761e4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b761e4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b7611c bytes 43070054
+ 00b761e4 bytes 43070054
- 00b7614c ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00b76214 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b7614c bytes 42010054
+ 00b76214 bytes 42010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3bb5dbe957f02db8917f6a7c3e8db85"></a>

### [`00b76588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76588.md) → [`00b76650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md) FUN_00b76650

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b764ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b764ec.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00b765b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 91.67% / 新版 88.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b765ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76588.md#insn-00b765ec) · [`00b765f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76588.md#insn-00b765f0) · [`00b765f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76588.md#insn-00b765f8)
- 新版 `00b766b4`（命令位置の公開資料なし） · `00b766b8`（命令位置の公開資料なし） · `00b766c0`（命令位置の公開資料なし）

~~~diff
- 00b765ec ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
+ 00b766b4 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b765ec bytes 62040054
+ 00b766b4 bytes 62040054
- 00b765f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b765f0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00b766b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b766b8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b765f0 bytes a80500b5
+ 00b766b8 bytes a80500b5
- 00b765f8 ["INT_ADD", "register:40f0:8", ["const:b765f8:8", "const:4:8"]]
- 00b765f8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b766c0 ["INT_ADD", "register:40f0:8", ["const:b766c0:8", "const:4:8"]]
+ 00b766c0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b765f8 bytes 52920194
+ 00b766c0 bytes 4c920194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbee62fb0009b8caf6c0eb2c11e4ecd6"></a>

### [`00b766cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b766cc.md) → [`00b76794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76794.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd960.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 1件 [`00bdda10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda10.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b767ec",
      "incomplete_value": true,
      "site": "00b76808",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b767f4",
      "incomplete_value": true,
      "site": "00b76808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
              [
                "live",
                "register:4040:8"
              ]
            ]
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7672c",
      "incomplete_value": true,
      "site": "00b76740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b76740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b766cc.md#insn-00b76740) · [`00b7671c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b766cc.md#insn-00b7671c) · [`00b7672c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b766cc.md#insn-00b7672c)
- 新版 `00b76808`（命令位置の公開資料なし） · `00b767e4`（命令位置の公開資料なし）

~~~diff
- 00b76740 ["INT_ADD", "register:40f0:8", ["const:b76740:8", "const:4:8"]]
- 00b76740 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00b76808 ["INT_ADD", "register:40f0:8", ["const:b76808:8", "const:4:8"]]
+ 00b76808 ["CALL", null, ["callee:00be0fb0:8"]]
- 00b76740 bytes f0a90194
+ 00b76808 bytes eaa90194
- 00b7671c ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00b767e4 ["CBRANCH", null, ["local:b2:8", "register:102:1"]]
- 00b7671c bytes 62010054
+ 00b767e4 bytes 62010054
- 00b7672c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b7672c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b7672c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b7672c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b7672c bytes 2201158b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d61baa6a6067031d2b7f331ba1a1e5b7"></a>

### [`00b76bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76bac.md) → [`00b76c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76c74.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.25% / 新版 76.25%

CFGの説明率　旧版 13.04% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b76d84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76c10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76d24"
      ]
    ],
    [
      "unmatched:00b76c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76d04"
      ]
    ],
    [
      "unmatched:00b76c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76db0"
      ]
    ]
  ],
  "added": [
    [
      "00b76ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76d24"
      ]
    ],
    [
      "00b76cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76d04"
      ]
    ],
    [
      "00b76d20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76db0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76bac.md#insn-00b76c10) · [`00b76c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76bac.md#insn-00b76c18) · [`00b76c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76bac.md#insn-00b76c28)

~~~diff
- 00b76c10 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76c10 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76c10 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b76c10 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b76c10 bytes 5701899a
- 00b76c18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b76c18 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b76c18 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00b76c18 bytes 28020054
- 00b76c28 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b76c28 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b76c28 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b76c28 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b76c28 bytes 2881889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea80e5d64431b88973a822df9965dce8"></a>

### [`00b76cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76cec.md) → [`00b76db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76db4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9push_backEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f40.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00be0ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ff0.md) · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.33% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76cec.md#insn-00b76d0c) · [`00b76d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76cec.md#insn-00b76d14) · [`00b76d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76cec.md#insn-00b76d1c)
- 新版 `00b76dd4`（命令位置の公開資料なし） · `00b76ddc`（命令位置の公開資料なし） · `00b76de4`（命令位置の公開資料なし）

~~~diff
- 00b76d0c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b76d0c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b76d0c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b76d0c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b76dd4 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00b76dd4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b76dd4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b76dd4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b76d0c bytes a9000037
+ 00b76dd4 bytes a9000037
- 00b76d14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b76d14 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b76ddc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b76ddc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b76d14 bytes a1020054
+ 00b76ddc bytes a1020054
- 00b76d1c ["BRANCH", null, ["local:b5:8"]]
+ 00b76de4 ["BRANCH", null, ["local:b6:8"]]
- 00b76d1c bytes 06000014
+ 00b76de4 bytes 06000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e551260fb225dd1d15842c5dea9925"></a>

### [`00b76d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76d94.md) → [`00b76e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76e5c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.73% / 新版 79.73%

CFGの説明率　旧版 50.00% / 新版 47.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76de0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76de0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76ef0"
      ]
    ],
    [
      "unmatched:00b76e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76f44"
      ]
    ]
  ],
  "added": [
    [
      "00b76ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76ef0"
      ]
    ],
    [
      "00b76f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76f44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76d94.md#insn-00b76dcc) · [`00b76dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76d94.md#insn-00b76dd4) · [`00b76de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76d94.md#insn-00b76de0)

~~~diff
- 00b76dcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b76dcc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76dcc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b76dcc ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b76dcc bytes 08018b9a
- 00b76dd4 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b76dd4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76dd4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76dd4 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00b76dd4 bytes 93018a9a
- 00b76de0 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00b76de0 bytes 42020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fc7ecaf946b3e45ab0a47515594db7"></a>

### [`00b76f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76f14.md) → [`00b76fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76fdc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignEmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 16.00% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b770bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76f48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77064"
      ]
    ],
    [
      "unmatched:00b76fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b76ff0"
      ]
    ],
    [
      "unmatched:00b76fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b770c4"
      ]
    ]
  ],
  "added": [
    [
      "00b7701c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77064"
      ]
    ],
    [
      "00b77084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b770b8"
      ]
    ],
    [
      "00b770b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b770c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76f14.md#insn-00b76f48) · [`00b76f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76f14.md#insn-00b76f54) · [`00b76f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76f14.md#insn-00b76f78)
- 新版 `00b77040`（命令位置の公開資料なし）

~~~diff
- 00b76f48 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b76f48 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76f48 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76f48 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b76f48 bytes 21018a9a
- 00b76f54 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b76f54 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b76f54 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b76f54 bytes 49020054
- 00b76f78 ["INT_ADD", "register:40f0:8", ["const:b76f78:8", "const:4:8"]]
- 00b76f78 ["CALL", null, ["callee:00bdda00:8"]]
+ 00b77040 ["INT_ADD", "register:40f0:8", ["const:b77040:8", "const:4:8"]]
+ 00b77040 ["CALL", null, ["callee:00bdda00:8"]]
- 00b76f78 bytes 769a0194
+ 00b77040 bytes 709a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18af4d9f526cb622566ad1e8ab86f6c4"></a>

### [`00b770a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b770a4.md) → [`00b7716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md) FUN_00b7716c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7702c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7702c.md) [`00bb9194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9194.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`00b770f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md) [`00bb925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 6.67% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b770e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b770e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b771ac"
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
      "unmatched:00b770e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b771d8"
      ]
    ]
  ],
  "added": [
    [
      "00b771b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b771d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b770e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b770a4.md#insn-00b770e4) · [`00b770e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b770a4.md#insn-00b770e8) · [`00b77104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b770a4.md#insn-00b77104)
- 新版 `00b771cc`（命令位置の公開資料なし）

~~~diff
- 00b770e4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b770e4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b770e4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b770e4 ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b770e4 bytes 3531829a
- 00b770e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b770e8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b770e8 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b770e8 bytes 49010054
- 00b77104 ["INT_ADD", "register:40f0:8", ["const:b77104:8", "const:4:8"]]
- 00b77104 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b771cc ["INT_ADD", "register:40f0:8", ["const:b771cc:8", "const:4:8"]]
+ 00b771cc ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b77104 bytes bb8f0194
+ 00b771cc bytes b58f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137eff6cd9468e32b3ec5e136248f2c3"></a>

### [`00b7724c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7724c.md) → [`00b77314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77314.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md) [`00be0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 22.22% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77280"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b772ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b77348"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b77280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7724c.md#insn-00b77280) · [`00b772ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7724c.md#insn-00b772ac) · [`00b772dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7724c.md#insn-00b772dc)
- 新版 `00b773a4`（命令位置の公開資料なし）

~~~diff
- 00b77280 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b77280 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b77280 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b77280 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b77280 bytes 5601899a
- 00b772ac ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b772ac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b772ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b772ac ["COPY", "register:4000:8", ["tmp:0:8"]]
- 00b772ac bytes 4001899a
- 00b772dc ["INT_ADD", "register:40f0:8", ["const:b772dc:8", "const:4:8"]]
- 00b772dc ["CALL", null, ["callee:00b75a24:8"]]
+ 00b773a4 ["INT_ADD", "register:40f0:8", ["const:b773a4:8", "const:4:8"]]
+ 00b773a4 ["CALL", null, ["callee:00b75a24:8"]]
- 00b772dc bytes a0f9ff97
+ 00b773a4 bytes a0f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4747e5baeb480a4c25b192b1e4307a6b"></a>

### [`00b77594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77594.md) → [`00b7765c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7765c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00be0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 55.56% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b775c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b775c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b775d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b775d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77708"
      ]
    ],
    [
      "00b7770c",
      "PARAM",
      [
        "storage",
        "0029f1a9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b776a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77708"
      ]
    ],
    [
      "00b7770c",
      "PARAM",
      [
        "storage",
        "0029f236",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b775c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77594.md#insn-00b775c4) · [`00b775c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77594.md#insn-00b775c8) · [`00b775d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77594.md#insn-00b775d0)

~~~diff
- 00b775c4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b775c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b775c4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b775c4 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b775c4 bytes 48018b9a
- 00b775c8 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b775c8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b775c8 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b775c8 ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00b775c8 bytes aa018c9a
- 00b775d0 ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00b775d0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b775d0 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b775d0 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00b775d0 bytes eb018e9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12bd9734b30b82a0c5bad562ee1e27c"></a>

### [`00b776a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b776a4.md) → [`00b7776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md) FUN_00b7776c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7764c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7764c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00b77714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77714.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 41.67% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77700"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b777c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7774c",
      "incomplete_value": true,
      "site": "00b77768",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00b77700",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77834"
      ]
    ]
  ],
  "added": [
    [
      "00b777c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77834"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b776a4.md#insn-00b77700) · [`00b776d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b776a4.md#insn-00b776d8)
- 新版 `00b777c8`（命令位置の公開資料なし） · `00b777a0`（命令位置の公開資料なし）

~~~diff
- 00b77700 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b77700 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b77700 bytes 63030054
+ 00b777c8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b777c8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b777c8 bytes 63030054
- 00b776d8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b776d8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b777a0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00b777a0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b776d8 bytes b30300b4
+ 00b777a0 bytes b30300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-383c4d90ce70e356461f093b1eda329a"></a>

### [`00b77bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77bf4.md) → [`00b77cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cbc.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde110.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00bde1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b77ccc",
      "incomplete_value": false,
      "site": "00b77cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:1b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77c04",
      "incomplete_value": false,
      "site": "00b77c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:246:8"
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
      "00b77ccc",
      "PARAM",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77ccc",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77bf4.md#insn-00b77c08) · [`00b77c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77bf4.md#insn-00b77c04)
- 新版 `00b77cd0`（命令位置の公開資料なし） · `00b77ccc`（命令位置の公開資料なし）

~~~diff
- 00b77c08 ["INT_ADD", "register:40f0:8", ["const:b77c08:8", "const:4:8"]]
- 00b77c08 ["CALL", null, ["callee:00418c38:8"]]
+ 00b77cd0 ["INT_ADD", "register:40f0:8", ["const:b77cd0:8", "const:4:8"]]
+ 00b77cd0 ["CALL", null, ["callee:00418c38:8"]]
- 00b77c08 bytes 0c84e297
+ 00b77cd0 bytes da83e297
- 00b77c04 ["COPY", "tmp:0:8", ["const:246:8"]]
- 00b77c04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b77c04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b77c04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b77ccc ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00b77ccc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77ccc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77ccc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b77c04 bytes 00180991
+ 00b77ccc bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74698dd9825797500f79a54a01bff185"></a>

### [`00b77c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c0c.md) → [`00b77cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cd4.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0380.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00be0430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0430.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b77ce4",
      "incomplete_value": false,
      "site": "00b77ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:1b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77c1c",
      "incomplete_value": false,
      "site": "00b77c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:246:8"
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
      "00b77ce4",
      "PARAM",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77ce4",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c0c.md#insn-00b77c20) · [`00b77c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c0c.md#insn-00b77c1c)
- 新版 `00b77ce8`（命令位置の公開資料なし） · `00b77ce4`（命令位置の公開資料なし）

~~~diff
- 00b77c20 ["INT_ADD", "register:40f0:8", ["const:b77c20:8", "const:4:8"]]
- 00b77c20 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00b77ce8 ["INT_ADD", "register:40f0:8", ["const:b77ce8:8", "const:4:8"]]
+ 00b77ce8 ["CALL", null, ["callee:0041fdf0:8"]]
- 00b77c20 bytes 74a0e297
+ 00b77ce8 bytes 42a0e297
- 00b77c1c ["COPY", "tmp:0:8", ["const:246:8"]]
- 00b77c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b77c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b77c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b77ce4 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00b77ce4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77ce4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b77ce4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b77c1c bytes 00180991
+ 00b77ce4 bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414111956b93bbd229c27c63de95c28c"></a>

### [`00b77c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c24.md) → [`00b77cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb110.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045efa8.md) [`00b7b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb640.md)
- 新版 呼出元 1件 [`00bdb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1c0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77c6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b77c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x6b]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b77c64",
      "WRITE",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b77c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b77d28",
      "WRITE",
      [
        "storage",
        "Stack[-0x6b]",
        null,
        null
      ]
    ],
    [
      "00b77d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "00b77d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c24.md#insn-00b77c60) · [`00b77c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c24.md#insn-00b77c64) · [`00b77c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c24.md#insn-00b77c6c)

~~~diff
- 00b77c60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b77c60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b77c60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:5:8"]]
- 00b77c60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b77c60 bytes ff170039
- 00b77c64 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b77c64 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:1:8"]]
- 00b77c64 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b77c64 bytes e81300b8
- 00b77c6c ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:18:8"]]
- 00b77c6c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b77c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b77c6c bytes bf0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c13a4e721aa81281e114d9f4a9cab8a"></a>

### [`00b77d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77d80.md) → [`00b77e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77e48.md) _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045efa8.md) [`00b7b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 12.50% / 新版 3.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b77ed0"
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
      "00b77ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b77e40"
      ]
    ],
    [
      "unmatched:00b77e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77f34"
      ]
    ],
    [
      "unmatched:00b77e44",
      "PARAM",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77f08"
      ]
    ],
    [
      "00b77ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77f34"
      ]
    ],
    [
      "00b77f0c",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77d80.md#insn-00b77e08) · [`00b77e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77d80.md#insn-00b77e3c) · [`00b77e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77d80.md#insn-00b77e54)
- 新版 `00b77f1c`（命令位置の公開資料なし）

~~~diff
- 00b77e08 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b77e08 bytes 20030054
- 00b77e3c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b77e3c ["RETURN", null, ["register:0:8"]]
- 00b77e3c bytes c0035fd6
- 00b77e54 ["INT_ADD", "register:40f0:8", ["const:b77e54:8", "const:4:8"]]
- 00b77e54 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b77f1c ["INT_ADD", "register:40f0:8", ["const:b77f1c:8", "const:4:8"]]
+ 00b77f1c ["CALL", null, ["callee:0045efa8:8"]]
- 00b77e54 bytes 559ce397
+ 00b77f1c bytes 239ce397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-120568b97e25a72a1adc98456964a6ee"></a>

### [`00b77e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77e98.md) → [`00b77f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdbaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbaa0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00bdbb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb50.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 2.17% / 新版 2.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77ea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b77ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b77ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b77ea8",
      "WRITE",
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
      "00b77f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b77f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b77f70",
      "WRITE",
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

- 旧版 [`00b77ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77e98.md#insn-00b77ea0) · [`00b77ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77e98.md#insn-00b77ea4) · [`00b77ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77e98.md#insn-00b77ea8)

~~~diff
- 00b77ea0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b77ea0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b77ea0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b77ea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b77ea0 bytes fd7b04a9
- 00b77ea4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b77ea4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b77ea4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b77ea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b77ea4 bytes f85f05a9
- 00b77ea8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b77ea8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b77ea8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b77ea8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b77ea8 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea38b7dd3275e2b665e7c5dba9c3a9f7"></a>

### [`00b78004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78004.md) → [`00b780cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md) _ZNSt6__ndk15stollERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2e0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb650.md)
- 新版 呼出元 1件 [`00bdb390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb390.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb700.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.13% / 新版 68.13%

CFGの説明率　旧版 9.09% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7800c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7800c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78010"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7800c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78010",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78050",
      "WRITE",
      [
        "storage",
        "Stack[-0x73]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b780d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b780d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b78118",
      "WRITE",
      [
        "storage",
        "Stack[-0x73]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7800c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78004.md#insn-00b7800c) · [`00b78010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78004.md#insn-00b78010) · [`00b7804c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78004.md#insn-00b7804c)

~~~diff
- 00b7800c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7800c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7800c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b7800c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7800c bytes fd7b04a9
- 00b78010 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b78010 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b78010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b78010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b78010 bytes f85f05a9
- 00b7804c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7804c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b7804c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b7804c ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b7804c bytes 5415809a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba92de59fac9910738fb1dbc0db4d5f"></a>

### [`00b78170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md) → [`00b78238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2f0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0150.md)
- 新版 呼出元 1件 [`00bdb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3a0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be0200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0200.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.09% / 新版 76.09%

CFGの説明率　旧版 10.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7817c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b78178",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7817c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78180",
      "WRITE",
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
      "00b78240",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b78244",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b78248",
      "WRITE",
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

- 旧版 [`00b78178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md#insn-00b78178) · [`00b7817c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md#insn-00b7817c) · [`00b78180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md#insn-00b78180)

~~~diff
- 00b78178 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b78178 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b78178 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b78178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b78178 bytes fd7b04a9
- 00b7817c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b7817c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b7817c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b7817c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7817c bytes f85f05a9
- 00b78180 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b78180 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b78180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b78180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b78180 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f508ccbded050819923f765ecb28884d"></a>

### [`00b782e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b782e0.md) → [`00b783a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md) _ZNSt6__ndk14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb690.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb660.md)
- 新版 呼出元 1件 [`00bdb740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb740.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb710.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.98% / 新版 60.98%

CFGの説明率　旧版 11.11% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 5件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7831c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b78308",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78318",
      "WRITE",
      [
        "storage",
        "Stack[-0x6b]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7831c",
      "WRITE",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b783d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b783e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x6b]",
        null,
        null
      ]
    ],
    [
      "00b783e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b782e0.md#insn-00b78308) · [`00b78318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b782e0.md#insn-00b78318) · [`00b7831c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b782e0.md#insn-00b7831c)

~~~diff
- 00b78308 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b78308 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00b78308 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b78308 bytes e8030039
- 00b78318 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b78318 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b78318 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:5:8"]]
- 00b78318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b78318 bytes ff170039
- 00b7831c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b7831c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:1:8"]]
- 00b7831c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b7831c bytes e81300b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc360f58eb5e66ececbd39bb69e67bd0"></a>

### [`00b78428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78428.md) → [`00b784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md) _ZNSt6__ndk14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb300.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb670.md)
- 新版 呼出元 1件 [`00bdb3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3b0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb720.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b785cc",
      "incomplete_value": true,
      "site": "00b785cc",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78504",
      "incomplete_value": true,
      "site": "00b78504",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b785d4",
      "incomplete_value": true,
      "site": "00b785d4",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7850c",
      "incomplete_value": true,
      "site": "00b7850c",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78604",
      "incomplete_value": true,
      "site": "00b78604",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7853c",
      "incomplete_value": true,
      "site": "00b7853c",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b785bc",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b785c0",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b785f4",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b785bc",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b785c0",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b785f4",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78428.md#insn-00b78474) · [`00b7848c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78428.md#insn-00b7848c) · [`00b784bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78428.md#insn-00b784bc)
- 新版 `00b7853c`（命令位置の公開資料なし） · `00b78554`（命令位置の公開資料なし） · `00b78584`（命令位置の公開資料なし）

~~~diff
- 00b78474 ["INT_ADD", "register:40f0:8", ["const:b78474:8", "const:4:8"]]
- 00b78474 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b7853c ["INT_ADD", "register:40f0:8", ["const:b7853c:8", "const:4:8"]]
+ 00b7853c ["CALL", null, ["callee:00bdb220:8"]]
- 00b78474 bytes 3f8b0194
+ 00b7853c bytes 398b0194
- 00b7848c ["INT_ADD", "register:40f0:8", ["const:b7848c:8", "const:4:8"]]
- 00b7848c ["CALL", null, ["callee:00bdb720:8"]]
+ 00b78554 ["INT_ADD", "register:40f0:8", ["const:b78554:8", "const:4:8"]]
+ 00b78554 ["CALL", null, ["callee:00bdb720:8"]]
- 00b7848c bytes 798c0194
+ 00b78554 bytes 738c0194
- 00b784bc ["INT_ADD", "register:40f0:8", ["const:b784bc:8", "const:4:8"]]
- 00b784bc ["CALL", null, ["callee:00be1010:8"]]
+ 00b78584 ["INT_ADD", "register:40f0:8", ["const:b78584:8", "const:4:8"]]
+ 00b78584 ["CALL", null, ["callee:00be1010:8"]]
- 00b784bc bytes a9a20194
+ 00b78584 bytes a3a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a32b2e15d2fbf45bc58785b6a18f4dd"></a>

### [`00b78570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78570.md) → [`00b78638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78638.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7872c",
      "incomplete_value": true,
      "site": "00b7872c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78664",
      "incomplete_value": true,
      "site": "00b78664",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78730",
      "incomplete_value": true,
      "site": "00b78730",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78668",
      "incomplete_value": true,
      "site": "00b78668",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7876c",
      "incomplete_value": true,
      "site": "00b7876c",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b786a4",
      "incomplete_value": true,
      "site": "00b786a4",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78714",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b78718",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78754",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78714",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78718",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78754",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b785e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78570.md#insn-00b785e0) · [`00b785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78570.md#insn-00b785c8) · [`00b78610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78570.md#insn-00b78610)
- 新版 `00b786a8`（命令位置の公開資料なし） · `00b78690`（命令位置の公開資料なし） · `00b786d8`（命令位置の公開資料なし）

~~~diff
- 00b785e0 ["INT_ADD", "register:40f0:8", ["const:b785e0:8", "const:4:8"]]
- 00b785e0 ["CALL", null, ["callee:00be1030:8"]]
+ 00b786a8 ["INT_ADD", "register:40f0:8", ["const:b786a8:8", "const:4:8"]]
+ 00b786a8 ["CALL", null, ["callee:00be1030:8"]]
- 00b785e0 bytes 68a20194
+ 00b786a8 bytes 62a20194
- 00b785c8 ["INT_ADD", "register:40f0:8", ["const:b785c8:8", "const:4:8"]]
- 00b785c8 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78690 ["INT_ADD", "register:40f0:8", ["const:b78690:8", "const:4:8"]]
+ 00b78690 ["CALL", null, ["callee:00bdb220:8"]]
- 00b785c8 bytes ea8a0194
+ 00b78690 bytes e48a0194
- 00b78610 ["INT_ADD", "register:40f0:8", ["const:b78610:8", "const:4:8"]]
- 00b78610 ["CALL", null, ["callee:00be1010:8"]]
+ 00b786d8 ["INT_ADD", "register:40f0:8", ["const:b786d8:8", "const:4:8"]]
+ 00b786d8 ["CALL", null, ["callee:00be1010:8"]]
- 00b78610 bytes 54a20194
+ 00b786d8 bytes 4ea20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb4a01b2f4522c70d1f8a709435d5f0d"></a>

### [`00b786d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b786d4.md) → [`00b7879c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045efa8.md) [`00b7b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 91.14% / 新版 91.14%

CFGの説明率　旧版 90.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b788c4",
      "incomplete_value": true,
      "site": "00b788c4",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b787fc",
      "incomplete_value": true,
      "site": "00b787fc",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b788cc",
      "incomplete_value": true,
      "site": "00b788cc",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78804",
      "incomplete_value": true,
      "site": "00b78804",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b787c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b787a8",
      "PARAM",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b788b4",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b788b8",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78870",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b788b4",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b788b8",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b787b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b786d4.md#insn-00b787b8) · [`00b787c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b786d4.md#insn-00b787c8)
- 新版 `00b78880`（命令位置の公開資料なし） · `00b78890`（命令位置の公開資料なし）

~~~diff
- 00b787b8 ["INT_ADD", "register:40f0:8", ["const:b787b8:8", "const:4:8"]]
- 00b787b8 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b78880 ["INT_ADD", "register:40f0:8", ["const:b78880:8", "const:4:8"]]
+ 00b78880 ["CALL", null, ["callee:0045efa8:8"]]
- 00b787b8 bytes fc99e397
+ 00b78880 bytes ca99e397
- 00b787c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b787c8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b787c8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b787c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b787c8 bytes 2015939a
+ 00b78890 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b78890 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b78890 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b78890 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
+ 00b78890 bytes 2015939a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87fe2dc2a6448d50095bf63ab8e2635e"></a>

### [`00b78838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78838.md) → [`00b78900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md) _ZNSt6__ndk14stolERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045efa8.md) [`00b7b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b789cc",
      "incomplete_value": false,
      "site": "00b789dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78904",
      "incomplete_value": false,
      "site": "00b78914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:e9:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b78904",
      "PARAM",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b789cc",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78838.md#insn-00b78914) · [`00b7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78838.md#insn-00b7888c) · [`00b788a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78838.md#insn-00b788a8)
- 新版 `00b789dc`（命令位置の公開資料なし） · `00b78954`（命令位置の公開資料なし） · `00b78970`（命令位置の公開資料なし）

~~~diff
- 00b78914 ["INT_ADD", "register:40f0:8", ["const:b78914:8", "const:4:8"]]
- 00b78914 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b789dc ["INT_ADD", "register:40f0:8", ["const:b789dc:8", "const:4:8"]]
+ 00b789dc ["CALL", null, ["callee:0045efa8:8"]]
- 00b78914 bytes a599e397
+ 00b789dc bytes 7399e397
- 00b7888c ["INT_ADD", "register:40f0:8", ["const:b7888c:8", "const:4:8"]]
- 00b7888c ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78954 ["INT_ADD", "register:40f0:8", ["const:b78954:8", "const:4:8"]]
+ 00b78954 ["CALL", null, ["callee:00bdb220:8"]]
- 00b7888c bytes 398a0194
+ 00b78954 bytes 338a0194
- 00b788a8 ["INT_ADD", "register:40f0:8", ["const:b788a8:8", "const:4:8"]]
- 00b788a8 ["CALL", null, ["callee:00be1040:8"]]
+ 00b78970 ["INT_ADD", "register:40f0:8", ["const:b78970:8", "const:4:8"]]
+ 00b78970 ["CALL", null, ["callee:00be1040:8"]]
- 00b788a8 bytes baa10194
+ 00b78970 bytes b4a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1bf0f590f74d066321b756b6e3b12fd"></a>

### [`00b78958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78958.md) → [`00b78a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78a20.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78b24",
      "incomplete_value": true,
      "site": "00b78b24",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78a5c",
      "incomplete_value": true,
      "site": "00b78a5c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78b28",
      "incomplete_value": true,
      "site": "00b78b28",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78a60",
      "incomplete_value": true,
      "site": "00b78a60",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78b64",
      "incomplete_value": true,
      "site": "00b78b64",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78a9c",
      "incomplete_value": true,
      "site": "00b78a9c",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78b0c",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b78b14",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78b4c",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78b0c",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78b14",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78b4c",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b789b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78958.md#insn-00b789b0) · [`00b789cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78958.md#insn-00b789cc) · [`00b78a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78958.md#insn-00b78a08)
- 新版 `00b78a78`（命令位置の公開資料なし） · `00b78a94`（命令位置の公開資料なし） · `00b78ad0`（命令位置の公開資料なし）

~~~diff
- 00b789b0 ["INT_ADD", "register:40f0:8", ["const:b789b0:8", "const:4:8"]]
- 00b789b0 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78a78 ["INT_ADD", "register:40f0:8", ["const:b78a78:8", "const:4:8"]]
+ 00b78a78 ["CALL", null, ["callee:00bdb220:8"]]
- 00b789b0 bytes f0890194
+ 00b78a78 bytes ea890194
- 00b789cc ["INT_ADD", "register:40f0:8", ["const:b789cc:8", "const:4:8"]]
- 00b789cc ["CALL", null, ["callee:00be1050:8"]]
+ 00b78a94 ["INT_ADD", "register:40f0:8", ["const:b78a94:8", "const:4:8"]]
+ 00b78a94 ["CALL", null, ["callee:00be1050:8"]]
- 00b789cc bytes 75a10194
+ 00b78a94 bytes 6fa10194
- 00b78a08 ["INT_ADD", "register:40f0:8", ["const:b78a08:8", "const:4:8"]]
- 00b78a08 ["CALL", null, ["callee:00be1010:8"]]
+ 00b78ad0 ["INT_ADD", "register:40f0:8", ["const:b78ad0:8", "const:4:8"]]
+ 00b78ad0 ["CALL", null, ["callee:00be1010:8"]]
- 00b78a08 bytes 56a10194
+ 00b78ad0 bytes 50a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9444403336f2ceb487ed84c834a70f"></a>

### [`00b78ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78ad4.md) → [`00b78b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78b9c.md) _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78ca0",
      "incomplete_value": true,
      "site": "00b78ca0",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78bd8",
      "incomplete_value": true,
      "site": "00b78bd8",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78ca4",
      "incomplete_value": true,
      "site": "00b78ca4",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78bdc",
      "incomplete_value": true,
      "site": "00b78bdc",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78ce0",
      "incomplete_value": true,
      "site": "00b78ce0",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78c18",
      "incomplete_value": true,
      "site": "00b78c18",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78c88",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b78c90",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78cc8",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78c88",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78c90",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78cc8",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78ad4.md#insn-00b78b2c) · [`00b78b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78ad4.md#insn-00b78b48) · [`00b78b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78ad4.md#insn-00b78b84)
- 新版 `00b78bf4`（命令位置の公開資料なし） · `00b78c10`（命令位置の公開資料なし） · `00b78c4c`（命令位置の公開資料なし）

~~~diff
- 00b78b2c ["INT_ADD", "register:40f0:8", ["const:b78b2c:8", "const:4:8"]]
- 00b78b2c ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78bf4 ["INT_ADD", "register:40f0:8", ["const:b78bf4:8", "const:4:8"]]
+ 00b78bf4 ["CALL", null, ["callee:00bdb220:8"]]
- 00b78b2c bytes 91890194
+ 00b78bf4 bytes 8b890194
- 00b78b48 ["INT_ADD", "register:40f0:8", ["const:b78b48:8", "const:4:8"]]
- 00b78b48 ["CALL", null, ["callee:00be1060:8"]]
+ 00b78c10 ["INT_ADD", "register:40f0:8", ["const:b78c10:8", "const:4:8"]]
+ 00b78c10 ["CALL", null, ["callee:00be1060:8"]]
- 00b78b48 bytes 1aa10194
+ 00b78c10 bytes 14a10194
- 00b78b84 ["INT_ADD", "register:40f0:8", ["const:b78b84:8", "const:4:8"]]
- 00b78b84 ["CALL", null, ["callee:00be1010:8"]]
+ 00b78c4c ["INT_ADD", "register:40f0:8", ["const:b78c4c:8", "const:4:8"]]
+ 00b78c4c ["CALL", null, ["callee:00be1010:8"]]
- 00b78b84 bytes f7a00194
+ 00b78c4c bytes f1a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9564f24fc11cf8ade87eb913a9b4b29b"></a>

### [`00b78c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78c50.md) → [`00b78d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78d18.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78e20",
      "incomplete_value": true,
      "site": "00b78e20",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78d58",
      "incomplete_value": true,
      "site": "00b78d58",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78e24",
      "incomplete_value": true,
      "site": "00b78e24",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78d5c",
      "incomplete_value": true,
      "site": "00b78d5c",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78e60",
      "incomplete_value": true,
      "site": "00b78e60",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78d98",
      "incomplete_value": true,
      "site": "00b78d98",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78e08",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b78e10",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78e48",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78e08",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78e10",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78e48",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78c50.md#insn-00b78cac) · [`00b78cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78c50.md#insn-00b78cc8) · [`00b78d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78c50.md#insn-00b78d04)
- 新版 `00b78d74`（命令位置の公開資料なし） · `00b78d90`（命令位置の公開資料なし） · `00b78dcc`（命令位置の公開資料なし）

~~~diff
- 00b78cac ["INT_ADD", "register:40f0:8", ["const:b78cac:8", "const:4:8"]]
- 00b78cac ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78d74 ["INT_ADD", "register:40f0:8", ["const:b78d74:8", "const:4:8"]]
+ 00b78d74 ["CALL", null, ["callee:00bdb220:8"]]
- 00b78cac bytes 31890194
+ 00b78d74 bytes 2b890194
- 00b78cc8 ["INT_ADD", "register:40f0:8", ["const:b78cc8:8", "const:4:8"]]
- 00b78cc8 ["CALL", null, ["callee:00be1070:8"]]
+ 00b78d90 ["INT_ADD", "register:40f0:8", ["const:b78d90:8", "const:4:8"]]
+ 00b78d90 ["CALL", null, ["callee:00be1070:8"]]
- 00b78cc8 bytes bea00194
+ 00b78d90 bytes b8a00194
- 00b78d04 ["INT_ADD", "register:40f0:8", ["const:b78d04:8", "const:4:8"]]
- 00b78d04 ["CALL", null, ["callee:00be1010:8"]]
+ 00b78dcc ["INT_ADD", "register:40f0:8", ["const:b78dcc:8", "const:4:8"]]
+ 00b78dcc ["CALL", null, ["callee:00be1010:8"]]
- 00b78d04 bytes 97a00194
+ 00b78dcc bytes 91a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73d313e81a5c608220e0c9be0aabdb21"></a>

### [`00b78dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78dd0.md) → [`00b78e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78e98.md) _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78f7c",
      "incomplete_value": true,
      "site": "00b78f7c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78eb4",
      "incomplete_value": true,
      "site": "00b78eb4",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78f84",
      "incomplete_value": true,
      "site": "00b78f84",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78ebc",
      "incomplete_value": true,
      "site": "00b78ebc",
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
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78fb4",
      "incomplete_value": true,
      "site": "00b78fb4",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78eec",
      "incomplete_value": true,
      "site": "00b78eec",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78f6c",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ],
    [
      "00b78f70",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78fa4",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78f6c",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78f70",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78fa4",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78dd0.md#insn-00b78e20) · [`00b78e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78dd0.md#insn-00b78e38) · [`00b78e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78dd0.md#insn-00b78e6c)
- 新版 `00b78ee8`（命令位置の公開資料なし） · `00b78f00`（命令位置の公開資料なし） · `00b78f34`（命令位置の公開資料なし）

~~~diff
- 00b78e20 ["INT_ADD", "register:40f0:8", ["const:b78e20:8", "const:4:8"]]
- 00b78e20 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b78ee8 ["INT_ADD", "register:40f0:8", ["const:b78ee8:8", "const:4:8"]]
+ 00b78ee8 ["CALL", null, ["callee:00bdb220:8"]]
- 00b78e20 bytes d4880194
+ 00b78ee8 bytes ce880194
- 00b78e38 ["INT_ADD", "register:40f0:8", ["const:b78e38:8", "const:4:8"]]
- 00b78e38 ["CALL", null, ["callee:00be1080:8"]]
+ 00b78f00 ["INT_ADD", "register:40f0:8", ["const:b78f00:8", "const:4:8"]]
+ 00b78f00 ["CALL", null, ["callee:00be1080:8"]]
- 00b78e38 bytes 66a00194
+ 00b78f00 bytes 60a00194
- 00b78e6c ["INT_ADD", "register:40f0:8", ["const:b78e6c:8", "const:4:8"]]
- 00b78e6c ["CALL", null, ["callee:00be1010:8"]]
+ 00b78f34 ["INT_ADD", "register:40f0:8", ["const:b78f34:8", "const:4:8"]]
+ 00b78f34 ["CALL", null, ["callee:00be1010:8"]]
- 00b78e6c bytes 3da00194
+ 00b78f34 bytes 37a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce4af4aeeb39f50c22de1fed272782fc"></a>

### [`00b78f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78f28.md) → [`00b78ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78ff0.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 66.67% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b78ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b78ff4",
      "READ",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b78ffc",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b790bc",
      "READ",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "00b790c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b790c4",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78f28.md#insn-00b78f78) · [`00b78ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78f28.md#insn-00b78ff8) · [`00b79004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78f28.md#insn-00b79004)
- 新版 `00b79040`（命令位置の公開資料なし）

~~~diff
- 00b78f78 ["INT_ADD", "register:40f0:8", ["const:b78f78:8", "const:4:8"]]
- 00b78f78 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b79040 ["INT_ADD", "register:40f0:8", ["const:b79040:8", "const:4:8"]]
+ 00b79040 ["CALL", null, ["callee:00bdb220:8"]]
- 00b78f78 bytes 7e880194
+ 00b79040 bytes 78880194
- 00b78ff8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b78ff8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b78ff8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b78ff8 bytes e8630039
- 00b79004 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b79004 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b79004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b79004 bytes ff1700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fad6af0febf37bab18be147c14901c2"></a>

### [`00b79080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79080.md) → [`00b79148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79148.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 25.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b790c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7911c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79160"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b790c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x63]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7920c"
      ]
    ],
    [
      "unmatched:00b7915c",
      "READ",
      [
        "storage",
        "002a90e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7918c",
      "WRITE",
      [
        "storage",
        "Stack[-0x63]",
        null,
        null
      ]
    ],
    [
      "00b791c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7920c"
      ]
    ],
    [
      "00b79224",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b790c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79080.md#insn-00b790c4) · [`00b790cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79080.md#insn-00b790cc) · [`00b790e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79080.md#insn-00b790e8)
- 新版 `00b791b0`（命令位置の公開資料なし）

~~~diff
- 00b790c4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b790c4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:1d:8"]]
- 00b790c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b790c4 bytes e8d30178
- 00b790cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b790cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b790cc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b790cc ["COPY", "register:40a0:8", ["tmp:0:8"]]
- 00b790cc bytes 14018a9a
- 00b790e8 ["INT_ADD", "register:40f0:8", ["const:b790e8:8", "const:4:8"]]
- 00b790e8 ["CALL", null, ["callee:00be10a0:8"]]
+ 00b791b0 ["INT_ADD", "register:40f0:8", ["const:b791b0:8", "const:4:8"]]
+ 00b791b0 ["CALL", null, ["callee:00be10a0:8"]]
- 00b790e8 bytes c29f0194
+ 00b791b0 bytes bc9f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d882bf9f1c79fca7109dc46c0e3fd43c"></a>

### [`00b791ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b791ec.md) → [`00b792b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md) _ZNSt6__ndk19to_stringEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb000.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdb0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 77.78% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b79270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b791ec.md#insn-00b79270) · [`00b79274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b791ec.md#insn-00b79274) · [`00b79288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b791ec.md#insn-00b79288)
- 新版 `00b79338`（命令位置の公開資料なし） · `00b7933c`（命令位置の公開資料なし） · `00b79350`（命令位置の公開資料なし）

~~~diff
- 00b79270 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b79270 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b79338 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b79338 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b79270 bytes 6b000054
+ 00b79338 bytes 6b000054
- 00b79274 ["INT_ADD", "register:40f0:8", ["const:b79274:8", "const:4:8"]]
- 00b79274 ["CALL", null, ["callee:00b7b3a4:8"]]
+ 00b7933c ["INT_ADD", "register:40f0:8", ["const:b7933c:8", "const:4:8"]]
+ 00b7933c ["CALL", null, ["callee:00b7b3a4:8"]]
- 00b79274 bytes 1a080094
+ 00b7933c bytes 1a080094
- 00b79288 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
+ 00b79350 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b79288 bytes 22040054
+ 00b79350 bytes 22040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc18c4f34da9912c2bb4e0ac731de4f9"></a>

### [`00b79810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79810.md) → [`00b798d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md) _ZNSt6__ndk19to_stringEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb210.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2c0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.19% / 新版 77.19%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79914"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79930"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b79910",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b79940"
      ]
    ],
    [
      "unmatched:00b798fc",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7990c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b79910",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79a08"
      ]
    ],
    [
      "00b799c4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00b799d4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79810.md#insn-00b79904) · [`00b79914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79810.md#insn-00b79914) · [`00b79930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79810.md#insn-00b79930)

~~~diff
- 00b79904 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79904 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79904 bytes 08000079
- 00b79914 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79914 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79914 bytes 0a040079
- 00b79930 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:6:8"]]
- 00b79930 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79930 bytes 080c0079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a44122e74544d7f09ada0a11447bc15"></a>

### [`00b799d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b799d8.md) → [`00b79aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79aa0.md) _ZNSt6__ndk19to_stringEy

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 18.18% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b79b94"
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
      "unmatched:00b79a24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79b20"
      ]
    ],
    [
      "unmatched:00b79ac4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79ad4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b79aec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79b20"
      ]
    ],
    [
      "00b79b8c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00b79b9c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b799d8.md#insn-00b79a24) · [`00b79a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b799d8.md#insn-00b79a48) · [`00b79acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b799d8.md#insn-00b79acc)
- 新版 `00b79b10`（命令位置の公開資料なし）

~~~diff
- 00b79a24 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b79a24 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b79a24 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00b79a24 bytes a9010054
- 00b79a48 ["INT_ADD", "register:40f0:8", ["const:b79a48:8", "const:4:8"]]
- 00b79a48 ["CALL", null, ["callee:00b7b3a4:8"]]
+ 00b79b10 ["INT_ADD", "register:40f0:8", ["const:b79b10:8", "const:4:8"]]
+ 00b79b10 ["CALL", null, ["callee:00b7b3a4:8"]]
- 00b79a48 bytes 25060094
+ 00b79b10 bytes 25060094
- 00b79acc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79acc ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79acc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79acc bytes 08000079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f6ce2584d7cf195f4d0c596388a88c"></a>

### [`00b79ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79ba0.md) → [`00b79c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79c68.md) _ZNSt6__ndk110to_wstringEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.51% / 新版 80.51%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b79c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79d20"
      ]
    ],
    [
      "unmatched:00b79c74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79e3c"
      ]
    ],
    [
      "unmatched:00b79cc8",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b79d10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79d20"
      ]
    ],
    [
      "00b79d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b79e3c"
      ]
    ],
    [
      "00b79d90",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79ba0.md#insn-00b79c48) · [`00b79c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79ba0.md#insn-00b79c68) · [`00b79c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79ba0.md#insn-00b79c74)

~~~diff
- 00b79c48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b79c48 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b79c48 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00b79c48 bytes 88000054
- 00b79c68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b79c68 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b79c68 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b79c68 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b79c68 bytes 0801899a
- 00b79c74 ["CBRANCH", null, ["local:b24:8", "register:102:1"]]
- 00b79c74 bytes 02080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9a5a51443a82eb78a4a18c8827e325"></a>

### [`00b7a044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a044.md) → [`00b7a10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a10c.md) _ZNSt6__ndk110to_wstringEx

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.77% / 新版 78.77%

CFGの説明率　旧版 25.00% / 新版 26.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a18c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a19c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a1b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7a0b0",
      "DATA",
      [
        "storage",
        "002faa70",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7a0f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a1e8"
      ]
    ],
    [
      "unmatched:00b7a184",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7a178",
      "DATA",
      [
        "storage",
        "002faa70",
        null,
        null
      ]
    ],
    [
      "00b7a1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a1e8"
      ]
    ],
    [
      "00b7a24c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a044.md#insn-00b7a0f4) · [`00b7a18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a044.md#insn-00b7a18c) · [`00b7a19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a044.md#insn-00b7a19c)

~~~diff
- 00b7a0f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7a0f4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b7a0f4 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00b7a0f4 bytes 69010054
- 00b7a18c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b7a18c ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b7a18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b7a18c bytes 08000079
- 00b7a19c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b7a19c ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b7a19c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b7a19c bytes 0a040079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e1ed9932da84642009f800caa5a841a"></a>

### [`00b7a974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a974.md) → [`00b7aa3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7aa3c.md) _ZNSt6__ndk19to_stringEf

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd080.md) · 呼出先 3件 [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md) [`00be1000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1000.md)
- 新版 呼出元 1件 [`00bdd130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd130.md) · 呼出先 3件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 33.33% / 新版 39.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a9a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7a99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7a9a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7aa44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7aaac"
      ]
    ]
  ],
  "added": [
    [
      "00b7aa64",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b7aa68",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b7ab0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7aaac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a974.md#insn-00b7a99c) · [`00b7a9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a974.md#insn-00b7a9a0) · [`00b7a9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a974.md#insn-00b7a9b4)
- 新版 `00b7aa7c`（命令位置の公開資料なし）

~~~diff
- 00b7a99c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b7a99c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b7a99c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b7a99c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b7a99c bytes ffff00a9
- 00b7a9a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b7a9a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b7a9a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b7a9a0 bytes ff0f00f9
- 00b7a9b4 ["INT_ADD", "register:40f0:8", ["const:b7a9b4:8", "const:4:8"]]
- 00b7a9b4 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b7aa7c ["INT_ADD", "register:40f0:8", ["const:b7aa7c:8", "const:4:8"]]
+ 00b7aa7c ["CALL", null, ["callee:00bdef70:8"]]
- 00b7a9b4 bytes 43910194
+ 00b7aa7c bytes 3d910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db820d6cb629152f2a316a91a405bbd1"></a>

### [`00b7b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md) → [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) FUN_00b7b2c8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b77c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c24.md) [`00b77d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77d80.md) [`00b786d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b786d4.md) [`00b78838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78838.md) · 呼出先 4件 [`0045efa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045efa8.md) [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00be0f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f60.md)
- 新版 呼出元 4件 [`00b77cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md) [`00b77e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77e48.md) [`00b7879c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md) [`00b78900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md) · 呼出先 4件 [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7b2e0",
      "incomplete_value": false,
      "site": "00b7b2ec",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b218",
      "incomplete_value": false,
      "site": "00b7b224",
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
            "const:7f3:8"
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
      "00b7b2e0",
      "PARAM",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7b2e0",
      "PARAM",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md#insn-00b7b224) · [`00b7b218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md#insn-00b7b218) · [`00b7b238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b200.md#insn-00b7b238)
- 新版 `00b7b2ec`（命令位置の公開資料なし） · `00b7b2e0`（命令位置の公開資料なし） · `00b7b300`（命令位置の公開資料なし）

~~~diff
- 00b7b224 ["INT_ADD", "register:40f0:8", ["const:b7b224:8", "const:4:8"]]
- 00b7b224 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b7b2ec ["INT_ADD", "register:40f0:8", ["const:b7b2ec:8", "const:4:8"]]
+ 00b7b2ec ["CALL", null, ["callee:0045efa8:8"]]
- 00b7b224 bytes 618fe397
+ 00b7b2ec bytes 2f8fe397
- 00b7b218 ["COPY", "tmp:0:8", ["const:7f3:8"]]
- 00b7b218 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7b218 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7b218 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7b2e0 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00b7b2e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7b2e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7b2e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7b218 bytes 21cc1f91
+ 00b7b2e0 bytes 21002291
- 00b7b238 ["INT_ADD", "register:40f0:8", ["const:b7b238:8", "const:4:8"]]
- 00b7b238 ["CALL", null, ["callee:00b7b318:8"]]
+ 00b7b300 ["INT_ADD", "register:40f0:8", ["const:b7b300:8", "const:4:8"]]
+ 00b7b300 ["CALL", null, ["callee:00b7b318:8"]]
- 00b7b238 bytes 06000094
+ 00b7b300 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d684d246af009cc9444a81c3e39b549"></a>

### [`00b7b250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md) → [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) FUN_00b7b318

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`00b77e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77e98.md) [`00b78004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78004.md) [`00b78170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md) [`00b782e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b782e0.md) [`00b78428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78428.md) · 呼出先 4件 [`00b7b2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2a4.md) [`00bbad50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbad50.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 13件 [`00b77f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md) [`00b780cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md) [`00b78238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md) [`00b783a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md) [`00b784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md) · 呼出先 4件 [`00b7b36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b36c.md) [`00bbae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7b34c",
      "incomplete_value": true,
      "site": "00b7b354",
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b284",
      "incomplete_value": true,
      "site": "00b7b28c",
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
                "const:b88:8"
              ]
            ]
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
      "definition_site": "00b7b350",
      "incomplete_value": true,
      "site": "00b7b354",
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
                "const:c40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b288",
      "incomplete_value": true,
      "site": "00b7b28c",
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
                "const:b90:8"
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
      "00b7b34c",
      "READ",
      [
        "storage",
        "00c1bb88",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b34c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7b350",
      "READ",
      [
        "storage",
        "00c1bb90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7b34c",
      "READ",
      [
        "storage",
        "00c1bc38",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b34c",
      "PARAM",
      [
        "storage",
        "00c169a0",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7b350",
      "READ",
      [
        "storage",
        "00c1bc40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md#insn-00b7b28c) · [`00b7b268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md#insn-00b7b268) · [`00b7b274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b250.md#insn-00b7b274)
- 新版 `00b7b354`（命令位置の公開資料なし） · `00b7b330`（命令位置の公開資料なし） · `00b7b33c`（命令位置の公開資料なし）

~~~diff
- 00b7b28c ["INT_ADD", "register:40f0:8", ["const:b7b28c:8", "const:4:8"]]
- 00b7b28c ["CALL", null, ["callee:00bdb070:8"]]
+ 00b7b354 ["INT_ADD", "register:40f0:8", ["const:b7b354:8", "const:4:8"]]
+ 00b7b354 ["CALL", null, ["callee:00bdb070:8"]]
- 00b7b28c bytes 4d7f0194
+ 00b7b354 bytes 477f0194
- 00b7b268 ["INT_ADD", "register:40f0:8", ["const:b7b268:8", "const:4:8"]]
- 00b7b268 ["CALL", null, ["callee:00bdb050:8"]]
+ 00b7b330 ["INT_ADD", "register:40f0:8", ["const:b7b330:8", "const:4:8"]]
+ 00b7b330 ["CALL", null, ["callee:00bdb050:8"]]
- 00b7b268 bytes 4e7f0194
+ 00b7b330 bytes 487f0194
- 00b7b274 ["INT_ADD", "register:40f0:8", ["const:b7b274:8", "const:4:8"]]
- 00b7b274 ["CALL", null, ["callee:00b7b36c:8"]]
+ 00b7b33c ["INT_ADD", "register:40f0:8", ["const:b7b33c:8", "const:4:8"]]
+ 00b7b33c ["CALL", null, ["callee:00b7b36c:8"]]
- 00b7b274 bytes 0c000094
+ 00b7b33c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745520dab6d9db5030d4ce1936cf52a2"></a>

### [`00b7b694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md) → [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) FUN_00b7b75c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00b7b7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b7c8.md) [`00b7b890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b890.md) [`00b7defc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7defc.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md)
- 新版 呼出元 3件 [`00b7b890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md) [`00b7b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md) [`00b7dfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7b7cc",
      "incomplete_value": false,
      "site": "00b7b7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:212:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b704",
      "incomplete_value": false,
      "site": "00b7b718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:219:8"
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
      "00b7b7c0",
      "READ",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b7cc",
      "PARAM",
      [
        "storage",
        "002a7219",
        null,
        "string"
      ]
    ],
    [
      "00b7b7e4",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7b7c0",
      "READ",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b7cc",
      "PARAM",
      [
        "storage",
        "002a7212",
        null,
        "string"
      ]
    ],
    [
      "00b7b7e4",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md#insn-00b7b718) · [`00b7b6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md#insn-00b7b6b8) · [`00b7b6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md#insn-00b7b6d4)
- 新版 `00b7b7e0`（命令位置の公開資料なし） · `00b7b780`（命令位置の公開資料なし） · `00b7b79c`（命令位置の公開資料なし）

~~~diff
- 00b7b718 ["INT_ADD", "register:40f0:8", ["const:b7b718:8", "const:4:8"]]
- 00b7b718 ["CALL", null, ["callee:00be10b0:8"]]
+ 00b7b7e0 ["INT_ADD", "register:40f0:8", ["const:b7b7e0:8", "const:4:8"]]
+ 00b7b7e0 ["CALL", null, ["callee:00be10b0:8"]]
- 00b7b718 bytes 3a960194
+ 00b7b7e0 bytes 34960194
- 00b7b6b8 ["INT_ADD", "register:40f0:8", ["const:b7b6b8:8", "const:4:8"]]
- 00b7b6b8 ["CALL", null, ["callee:00bdb220:8"]]
+ 00b7b780 ["INT_ADD", "register:40f0:8", ["const:b7b780:8", "const:4:8"]]
+ 00b7b780 ["CALL", null, ["callee:00bdb220:8"]]
- 00b7b6b8 bytes ae7e0194
+ 00b7b780 bytes a87e0194
- 00b7b6d4 ["INT_ADD", "register:40f0:8", ["const:b7b6d4:8", "const:4:8"]]
- 00b7b6d4 ["CALL", null, ["callee:00be1140:8"]]
+ 00b7b79c ["INT_ADD", "register:40f0:8", ["const:b7b79c:8", "const:4:8"]]
+ 00b7b79c ["CALL", null, ["callee:00be1140:8"]]
- 00b7b6d4 bytes 6f960194
+ 00b7b79c bytes 69960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95bc620a5129a455d0e237b908971e87"></a>

### [`00b7b7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b7c8.md) → [`00b7b890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md) FUN_00b7b890

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7b8d0",
      "incomplete_value": true,
      "site": "00b7b8dc",
      "value": [
        "LOAD",
        "16",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b808",
      "incomplete_value": true,
      "site": "00b7b814",
      "value": [
        "LOAD",
        "16",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:6b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7b8d0",
      "incomplete_value": true,
      "site": "00b7b8dc",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b808",
      "incomplete_value": true,
      "site": "00b7b814",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7b8d0",
      "READ",
      [
        "storage",
        "002966b3",
        null,
        "string"
      ]
    ],
    [
      "00b7b8d0",
      "READ",
      [
        "storage",
        "002966c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7b8d0",
      "READ",
      [
        "storage",
        "00296740",
        null,
        "string"
      ]
    ],
    [
      "00b7b8d0",
      "READ",
      [
        "storage",
        "00296750",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b7c8.md#insn-00b7b7ec) · [`00b7b804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b7c8.md#insn-00b7b804)
- 新版 `00b7b8b4`（命令位置の公開資料なし） · `00b7b8cc`（命令位置の公開資料なし）

~~~diff
- 00b7b7ec ["INT_ADD", "register:40f0:8", ["const:b7b7ec:8", "const:4:8"]]
- 00b7b7ec ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7b8b4 ["INT_ADD", "register:40f0:8", ["const:b7b8b4:8", "const:4:8"]]
+ 00b7b8b4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7b7ec bytes d57d0194
+ 00b7b8b4 bytes cf7d0194
- 00b7b804 ["COPY", "tmp:0:8", ["const:6b3:8"]]
- 00b7b804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7b8cc ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00b7b8cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b8cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b8cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7b804 bytes 08cd1a91
+ 00b7b8cc bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fa4ebec79cca4dfa48db95df62a2195"></a>

### [`00b7b830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b830.md) → [`00b7b8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b8f8.md) _ZNSt6__ndk116generic_categoryEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7b92c",
      "incomplete_value": false,
      "site": "00b7b930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b864",
      "incomplete_value": false,
      "site": "00b7b868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "definition_site": "00b7b93c",
      "incomplete_value": false,
      "site": "00b7b940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b874",
      "incomplete_value": false,
      "site": "00b7b878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b7b918",
      "incomplete_value": false,
      "site": "00b7b924",
      "value": [
        "leaf",
        "const:c248b8:8"
      ]
    },
    "old": {
      "definition_site": "00b7b850",
      "incomplete_value": false,
      "site": "00b7b85c",
      "value": [
        "leaf",
        "const:c24808:8"
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
      "00b7b90c",
      "READ",
      [
        "storage",
        "010a1f58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b918",
      "DATA",
      [
        "storage",
        "00c24808",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b92c",
      "PARAM",
      [
        "storage",
        "010a1f58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7b90c",
      "READ",
      [
        "storage",
        "010a2018",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b918",
      "DATA",
      [
        "storage",
        "00c248b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b92c",
      "PARAM",
      [
        "storage",
        "010a2018",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b830.md#insn-00b7b868) · [`00b7b878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b830.md#insn-00b7b878) · [`00b7b83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b830.md#insn-00b7b83c)
- 新版 `00b7b930`（命令位置の公開資料なし） · `00b7b940`（命令位置の公開資料なし） · `00b7b904`（命令位置の公開資料なし）

~~~diff
- 00b7b868 ["INT_ADD", "register:40f0:8", ["const:b7b868:8", "const:4:8"]]
- 00b7b868 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7b930 ["INT_ADD", "register:40f0:8", ["const:b7b930:8", "const:4:8"]]
+ 00b7b930 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7b868 bytes a67d0194
+ 00b7b930 bytes a07d0194
- 00b7b878 ["INT_ADD", "register:40f0:8", ["const:b7b878:8", "const:4:8"]]
- 00b7b878 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00b7b940 ["INT_ADD", "register:40f0:8", ["const:b7b940:8", "const:4:8"]]
+ 00b7b940 ["CALL", null, ["callee:00bdafd0:8"]]
- 00b7b878 bytes aa7d0194
+ 00b7b940 bytes a47d0194
- 00b7b83c ["COPY", "register:4040:8", ["const:10a1000:8"]]
+ 00b7b904 ["COPY", "register:4040:8", ["const:10a2000:8"]]
- 00b7b83c bytes 282900d0
+ 00b7b904 bytes 282900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50d0dfe8f8c40684d1964d89ab43dd0e"></a>

### [`00b7b918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b918.md) → [`00b7b9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b9e0.md) _ZNSt6__ndk115system_categoryEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ba14",
      "incomplete_value": false,
      "site": "00b7ba18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b94c",
      "incomplete_value": false,
      "site": "00b7b950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "definition_site": "00b7ba24",
      "incomplete_value": false,
      "site": "00b7ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b95c",
      "incomplete_value": false,
      "site": "00b7b960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b7ba00",
      "incomplete_value": false,
      "site": "00b7ba0c",
      "value": [
        "leaf",
        "const:c248c0:8"
      ]
    },
    "old": {
      "definition_site": "00b7b938",
      "incomplete_value": false,
      "site": "00b7b944",
      "value": [
        "leaf",
        "const:c24810:8"
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
      "00b7b9f4",
      "READ",
      [
        "storage",
        "010a1f60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ba00",
      "DATA",
      [
        "storage",
        "00c24810",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ba14",
      "PARAM",
      [
        "storage",
        "010a1f60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7b9f4",
      "READ",
      [
        "storage",
        "010a2020",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ba00",
      "DATA",
      [
        "storage",
        "00c248c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ba14",
      "PARAM",
      [
        "storage",
        "010a2020",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b918.md#insn-00b7b950) · [`00b7b960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b918.md#insn-00b7b960) · [`00b7b924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b918.md#insn-00b7b924)
- 新版 `00b7ba18`（命令位置の公開資料なし） · `00b7ba28`（命令位置の公開資料なし） · `00b7b9ec`（命令位置の公開資料なし）

~~~diff
- 00b7b950 ["INT_ADD", "register:40f0:8", ["const:b7b950:8", "const:4:8"]]
- 00b7b950 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7ba18 ["INT_ADD", "register:40f0:8", ["const:b7ba18:8", "const:4:8"]]
+ 00b7ba18 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7b950 bytes 6c7d0194
+ 00b7ba18 bytes 667d0194
- 00b7b960 ["INT_ADD", "register:40f0:8", ["const:b7b960:8", "const:4:8"]]
- 00b7b960 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00b7ba28 ["INT_ADD", "register:40f0:8", ["const:b7ba28:8", "const:4:8"]]
+ 00b7ba28 ["CALL", null, ["callee:00bdafd0:8"]]
- 00b7b960 bytes 707d0194
+ 00b7ba28 bytes 6a7d0194
- 00b7b924 ["COPY", "register:4040:8", ["const:10a1000:8"]]
+ 00b7b9ec ["COPY", "register:4040:8", ["const:10a2000:8"]]
- 00b7b924 bytes 282900d0
+ 00b7b9ec bytes 282900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d39c49ce1a31660e0b091cc75fce41"></a>

### [`00b7ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7ba98.md) → [`00b7bb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md) FUN_00b7bb60

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00b7b9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b9a0.md) [`00b7bb6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bb6c.md) [`00b7bd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bd80.md) [`00b7be8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7be8c.md) · 呼出先 3件 [`007aae6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007aa/007aae6c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 4件 [`00b7ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7ba68.md) [`00b7bc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bc34.md) [`00b7be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7be48.md) [`00b7bf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bf54.md) · 呼出先 3件 [`007aae6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007aa/007aae6c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7bba8",
      "incomplete_value": false,
      "site": "00b7bbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7bae0",
      "incomplete_value": false,
      "site": "00b7bae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:6bf:8"
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
      "00b7bba8",
      "PARAM",
      [
        "storage",
        "002ac6bf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7bba8",
      "PARAM",
      [
        "storage",
        "002ac6b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7ba98.md#insn-00b7bae8) · [`00b7bae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7ba98.md#insn-00b7bae0) · [`00b7bb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7ba98.md#insn-00b7bb00)
- 新版 `00b7bbb0`（命令位置の公開資料なし） · `00b7bba8`（命令位置の公開資料なし） · `00b7bbc8`（命令位置の公開資料なし）

~~~diff
- 00b7bae8 ["INT_ADD", "register:40f0:8", ["const:b7bae8:8", "const:4:8"]]
- 00b7bae8 ["CALL", null, ["callee:00bdb0d0:8"]]
+ 00b7bbb0 ["INT_ADD", "register:40f0:8", ["const:b7bbb0:8", "const:4:8"]]
+ 00b7bbb0 ["CALL", null, ["callee:00bdb0d0:8"]]
- 00b7bae8 bytes 4e7d0194
+ 00b7bbb0 bytes 487d0194
- 00b7bae0 ["COPY", "tmp:0:8", ["const:6bf:8"]]
- 00b7bae0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7bae0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7bae0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7bba8 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 00b7bba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7bba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7bba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7bae0 bytes 21fc1a91
+ 00b7bba8 bytes 21d81a91
- 00b7bb00 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7bb00 ["INT_ADD", "register:40f0:8", ["const:b7bb00:8", "const:4:8"]]
- 00b7bb00 ["CALLIND", null, ["register:0:8"]]
+ 00b7bbc8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b7bbc8 ["INT_ADD", "register:40f0:8", ["const:b7bbc8:8", "const:4:8"]]
+ 00b7bbc8 ["CALLIND", null, ["register:0:8"]]
- 00b7bb00 bytes 20013fd6
+ 00b7bbc8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758013a454dbf61da64f5d13ee92fe17"></a>

### [`00b7bb6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bb6c.md) → [`00b7bc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bc34.md) _ZNSt6__ndk112system_errorC1ENS_10error_codeEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00be1060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1060.md) [`00be10b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10b0.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7ba98.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00be1110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1110.md) [`00be1160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1160.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7bb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bb60.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7bd1c",
      "incomplete_value": true,
      "site": "00b7bd20",
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
      "definition_site": "00b7bc54",
      "incomplete_value": true,
      "site": "00b7bc58",
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7bbf8",
      "incomplete_value": true,
      "site": "00b7bc04",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7bd14",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7bd20",
      "DATA",
      [
        "storage",
        "00c12cc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b7bd14",
      "READ",
      [
        "storage",
        "00c1bc50",
        null,
        "pointer"
      ]
    ],
    [
      "00b7bd20",
      "DATA",
      [
        "storage",
        "00c12d78",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bb6c.md#insn-00b7bc04) · [`00b7bb98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bb6c.md#insn-00b7bb98) · [`00b7bba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bb6c.md#insn-00b7bba0)
- 新版 `00b7bccc`（命令位置の公開資料なし） · `00b7bc60`（命令位置の公開資料なし） · `00b7bc68`（命令位置の公開資料なし）

~~~diff
- 00b7bc04 ["INT_ADD", "register:40f0:8", ["const:b7bc04:8", "const:4:8"]]
- 00b7bc04 ["CALL", null, ["callee:00bdb160:8"]]
+ 00b7bccc ["INT_ADD", "register:40f0:8", ["const:b7bccc:8", "const:4:8"]]
+ 00b7bccc ["CALL", null, ["callee:00bdb160:8"]]
- 00b7bc04 bytes 2b7d0194
+ 00b7bccc bytes 257d0194
- 00b7bb98 ["INT_ADD", "register:40f0:8", ["const:b7bb98:8", "const:4:8"]]
- 00b7bb98 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b7bc60 ["INT_ADD", "register:40f0:8", ["const:b7bc60:8", "const:4:8"]]
+ 00b7bc60 ["CALL", null, ["callee:00bdb140:8"]]
- 00b7bb98 bytes 3e7d0194
+ 00b7bc60 bytes 387d0194
- 00b7bba0 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
+ 00b7bc68 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b7bba0 bytes e2060054
+ 00b7bc68 bytes e2060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e25aa0e0dcd8c7f6c59ed9a32d3524c8"></a>

### [`00b7bcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bcd0.md) → [`00b7bd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7bd98.md) _ZNSt6__ndk112system_errorC2ENS_10error_codeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 44.44% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7be08",
      "incomplete_value": true,
      "site": "00b7be0c",
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
      "definition_site": "00b7bd40",
      "incomplete_value": true,
      "site": "00b7bd44",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7bd0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b7bdd4"
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
      "00b7be04",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7be0c",
      "DATA",
      [
        "storage",
        "00c12cc8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "unmatched:00b7bd0c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7be04",
      "READ",
      [
        "storage",
        "00c1bc50",
        null,
        "pointer"
      ]
    ],
    [
      "00b7be0c",
      "DATA",
      [
        "storage",
        "00c12d78",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00b7bdd4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bcd0.md#insn-00b7bd0c) · [`00b7bce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7bcd0.md#insn-00b7bce4)
- 新版 `00b7bdd4`（命令位置の公開資料なし）

~~~diff
- 00b7bd0c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7bd0c ["INT_ADD", "register:40f0:8", ["const:b7bd0c:8", "const:4:8"]]
- 00b7bd0c ["CALLIND", null, ["register:0:8"]]
- 00b7bd0c bytes 20013fd6
+ 00b7bdd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b7bdd4 ["INT_ADD", "register:40f0:8", ["const:b7bdd4:8", "const:4:8"]]
+ 00b7bdd4 ["CALLIND", null, ["register:0:8"]]
+ 00b7bdd4 bytes 20013fd6
- 00b7bce4 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00b7bce4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00b7bce4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00b7bce4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00b7bce4 bytes fd830091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b0c48318cd6410cd422d581c0a06810"></a>

### [`00b7c10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c10c.md) → [`00b7c1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1d4.md) FUN_00b7c1d4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b7c0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c0ec.md) · 呼出先 4件 [`00b7c0b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c0b8.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00be10b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10b0.md)
- 新版 呼出元 1件 [`00b7c1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1b4.md) · 呼出先 4件 [`00b7c180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c180.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be1160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7c21c",
      "incomplete_value": true,
      "site": "00b7c224",
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
                "const:c60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c154",
      "incomplete_value": true,
      "site": "00b7c15c",
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
                "const:bb0:8"
              ]
            ]
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
      "definition_site": "00b7c220",
      "incomplete_value": true,
      "site": "00b7c224",
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c158",
      "incomplete_value": true,
      "site": "00b7c15c",
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
                "const:ba8:8"
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
      "00b7c21c",
      "READ",
      [
        "storage",
        "00c1bbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7c21c",
      "PARAM",
      [
        "storage",
        "00c12cf8",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7c220",
      "READ",
      [
        "storage",
        "00c1bba8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7c21c",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7c21c",
      "PARAM",
      [
        "storage",
        "00c12da8",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7c220",
      "READ",
      [
        "storage",
        "00c1bc58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c10c.md#insn-00b7c15c) · [`00b7c130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c10c.md#insn-00b7c130) · [`00b7c144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c10c.md#insn-00b7c144)
- 新版 `00b7c224`（命令位置の公開資料なし） · `00b7c1f8`（命令位置の公開資料なし） · `00b7c20c`（命令位置の公開資料なし）

~~~diff
- 00b7c15c ["INT_ADD", "register:40f0:8", ["const:b7c15c:8", "const:4:8"]]
- 00b7c15c ["CALL", null, ["callee:00bdb070:8"]]
+ 00b7c224 ["INT_ADD", "register:40f0:8", ["const:b7c224:8", "const:4:8"]]
+ 00b7c224 ["CALL", null, ["callee:00bdb070:8"]]
- 00b7c15c bytes 997b0194
+ 00b7c224 bytes 937b0194
- 00b7c130 ["INT_ADD", "register:40f0:8", ["const:b7c130:8", "const:4:8"]]
- 00b7c130 ["CALL", null, ["callee:00bdb050:8"]]
+ 00b7c1f8 ["INT_ADD", "register:40f0:8", ["const:b7c1f8:8", "const:4:8"]]
+ 00b7c1f8 ["CALL", null, ["callee:00bdb050:8"]]
- 00b7c130 bytes 9c7b0194
+ 00b7c1f8 bytes 967b0194
- 00b7c144 ["INT_ADD", "register:40f0:8", ["const:b7c144:8", "const:4:8"]]
- 00b7c144 ["CALL", null, ["callee:00be1160:8"]]
+ 00b7c20c ["INT_ADD", "register:40f0:8", ["const:b7c20c:8", "const:4:8"]]
+ 00b7c20c ["CALL", null, ["callee:00be1160:8"]]
- 00b7c144 bytes db930194
+ 00b7c20c bytes d5930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a8cd2d72d4e0326a7b2fe3d46f69bf"></a>

### [`00b7c454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c454.md) → [`00b7c51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c51c.md) FUN_00b7c51c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7c57c",
      "incomplete_value": true,
      "site": "00b7c588",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c4b4",
      "incomplete_value": true,
      "site": "00b7c4c0",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7c584",
      "incomplete_value": true,
      "site": "00b7c58c",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c4bc",
      "incomplete_value": true,
      "site": "00b7c4c4",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7c584",
      "incomplete_value": true,
      "site": "00b7c58c",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c4bc",
      "incomplete_value": true,
      "site": "00b7c4c4",
      "value": [
        "LOAD",
        "16",
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
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7c57c",
      "READ",
      [
        "storage",
        "00294399",
        null,
        "string"
      ]
    ],
    [
      "00b7c584",
      "READ",
      [
        "storage",
        "00294379",
        null,
        "string"
      ]
    ],
    [
      "00b7c584",
      "READ",
      [
        "storage",
        "00294389",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7c57c",
      "READ",
      [
        "storage",
        "00294426",
        null,
        "string"
      ]
    ],
    [
      "00b7c584",
      "READ",
      [
        "storage",
        "00294406",
        null,
        "string"
      ]
    ],
    [
      "00b7c584",
      "READ",
      [
        "storage",
        "00294416",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c49c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c454.md#insn-00b7c49c) · [`00b7c4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c454.md#insn-00b7c4b0) · [`00b7c4dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c454.md#insn-00b7c4dc)
- 新版 `00b7c564`（命令位置の公開資料なし） · `00b7c578`（命令位置の公開資料なし） · `00b7c5a4`（命令位置の公開資料なし）

~~~diff
- 00b7c49c ["INT_ADD", "register:40f0:8", ["const:b7c49c:8", "const:4:8"]]
- 00b7c49c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7c564 ["INT_ADD", "register:40f0:8", ["const:b7c564:8", "const:4:8"]]
+ 00b7c564 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7c49c bytes a97a0194
+ 00b7c564 bytes a37a0194
- 00b7c4b0 ["COPY", "tmp:0:8", ["const:359:8"]]
- 00b7c4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7c578 ["COPY", "tmp:0:8", ["const:3e6:8"]]
+ 00b7c578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7c4b0 bytes 08650d91
+ 00b7c578 bytes 08990f91
- 00b7c4dc ["INT_ADD", "register:40f0:8", ["const:b7c4dc:8", "const:4:8"]]
- 00b7c4dc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7c5a4 ["INT_ADD", "register:40f0:8", ["const:b7c5a4:8", "const:4:8"]]
+ 00b7c5a4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7c4dc bytes 997a0194
+ 00b7c5a4 bytes 937a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a623ae7fdb38f07485f6c04f1f637fa"></a>

### [`00b7c5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c5e0.md) → [`00b7c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c6a8.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3c0.md) · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bdb470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb470.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7c6dc",
      "incomplete_value": false,
      "site": "00b7c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c614",
      "incomplete_value": false,
      "site": "00b7c618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "definition_site": "00b7c6ec",
      "incomplete_value": false,
      "site": "00b7c6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c624",
      "incomplete_value": false,
      "site": "00b7c628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b7c6c8",
      "incomplete_value": false,
      "site": "00b7c6d4",
      "value": [
        "leaf",
        "const:c248c8:8"
      ]
    },
    "old": {
      "definition_site": "00b7c600",
      "incomplete_value": false,
      "site": "00b7c60c",
      "value": [
        "leaf",
        "const:c24818:8"
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
      "00b7c6bc",
      "READ",
      [
        "storage",
        "010a1f68",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7c6c8",
      "DATA",
      [
        "storage",
        "00c24818",
        null,
        null
      ]
    ],
    [
      "00b7c6dc",
      "PARAM",
      [
        "storage",
        "010a1f68",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7c6bc",
      "READ",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7c6c8",
      "DATA",
      [
        "storage",
        "00c248c8",
        null,
        null
      ]
    ],
    [
      "00b7c6dc",
      "PARAM",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c5e0.md#insn-00b7c618) · [`00b7c628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c5e0.md#insn-00b7c628) · [`00b7c5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c5e0.md#insn-00b7c5ec)
- 新版 `00b7c6e0`（命令位置の公開資料なし） · `00b7c6f0`（命令位置の公開資料なし） · `00b7c6b4`（命令位置の公開資料なし）

~~~diff
- 00b7c618 ["INT_ADD", "register:40f0:8", ["const:b7c618:8", "const:4:8"]]
- 00b7c618 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7c6e0 ["INT_ADD", "register:40f0:8", ["const:b7c6e0:8", "const:4:8"]]
+ 00b7c6e0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7c618 bytes 3a7a0194
+ 00b7c6e0 bytes 347a0194
- 00b7c628 ["INT_ADD", "register:40f0:8", ["const:b7c628:8", "const:4:8"]]
- 00b7c628 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00b7c6f0 ["INT_ADD", "register:40f0:8", ["const:b7c6f0:8", "const:4:8"]]
+ 00b7c6f0 ["CALL", null, ["callee:00bdafd0:8"]]
- 00b7c628 bytes 3e7a0194
+ 00b7c6f0 bytes 387a0194
- 00b7c5ec ["COPY", "register:4040:8", ["const:10a1000:8"]]
+ 00b7c6b4 ["COPY", "register:4040:8", ["const:10a2000:8"]]
- 00b7c5ec bytes 282900b0
+ 00b7c6b4 bytes 282900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d330a36de7fd1796fd8e1c2ca983f8"></a>

### [`00b7ca94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7ca94.md) → [`00b7cb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb550.md) · 呼出先 3件 [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdb530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00bdb600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb600.md) · 呼出先 3件 [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7cbe0",
      "incomplete_value": false,
      "site": "00b7cbe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cb18",
      "incomplete_value": false,
      "site": "00b7cb20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:6be:8"
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
      "00b7cbe0",
      "PARAM",
      [
        "storage",
        "002ad6be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7cbe0",
      "PARAM",
      [
        "storage",
        "002ad6b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7ca94.md#insn-00b7cb20) · [`00b7cac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7ca94.md#insn-00b7cac0) · [`00b7caf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7ca94.md#insn-00b7caf0)
- 新版 `00b7cbe8`（命令位置の公開資料なし） · `00b7cb88`（命令位置の公開資料なし） · `00b7cbb8`（命令位置の公開資料なし）

~~~diff
- 00b7cb20 ["INT_ADD", "register:40f0:8", ["const:b7cb20:8", "const:4:8"]]
- 00b7cb20 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7cbe8 ["INT_ADD", "register:40f0:8", ["const:b7cbe8:8", "const:4:8"]]
+ 00b7cbe8 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7cb20 bytes ac790194
+ 00b7cbe8 bytes a6790194
- 00b7cac0 ["INT_ADD", "register:40f0:8", ["const:b7cac0:8", "const:4:8"]]
- 00b7cac0 ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00b7cb88 ["INT_ADD", "register:40f0:8", ["const:b7cb88:8", "const:4:8"]]
+ 00b7cb88 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00b7cac0 bytes 9c7a0194
+ 00b7cb88 bytes 967a0194
- 00b7caf0 ["INT_ADD", "register:40f0:8", ["const:b7caf0:8", "const:4:8"]]
- 00b7caf0 ["CALL", null, ["callee:00bdb250:8"]]
+ 00b7cbb8 ["INT_ADD", "register:40f0:8", ["const:b7cbb8:8", "const:4:8"]]
+ 00b7cbb8 ["CALL", null, ["callee:00bdb250:8"]]
- 00b7caf0 bytes ac790194
+ 00b7cbb8 bytes a6790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc9726f262b2523c539bb3ba4c2325a"></a>

### [`00b7cd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd28.md) → [`00b7cdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cdf0.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7ce20",
      "incomplete_value": true,
      "site": "00b7ce20",
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
      "definition_site": "00b7cd58",
      "incomplete_value": true,
      "site": "00b7cd58",
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
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7ce14",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ce20",
      "DATA",
      [
        "storage",
        "00c12e30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00b7ce14",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ce20",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd28.md#insn-00b7cd40) · [`00b7cd4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd28.md#insn-00b7cd4c)
- 新版 `00b7ce08`（命令位置の公開資料なし） · `00b7ce14`（命令位置の公開資料なし）

~~~diff
- 00b7cd40 ["INT_ADD", "register:40f0:8", ["const:b7cd40:8", "const:4:8"]]
- 00b7cd40 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7ce08 ["INT_ADD", "register:40f0:8", ["const:b7ce08:8", "const:4:8"]]
+ 00b7ce08 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7cd40 bytes 80780194
+ 00b7ce08 bytes 7a780194
- 00b7cd4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 00b7cd4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7ce14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00b7ce14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7cd4c bytes 08b146f9
+ 00b7ce14 bytes 080947f9
~~~


<a id="compare-5f2f52d7d603c70951ab931dbbbbf660"></a>

### [`00b7cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd7c.md) → [`00b7ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ce44.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377f0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.32% / 新版 81.32%

CFGの説明率　旧版 40.91% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cde8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cde8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7ceec",
      "incomplete_value": true,
      "site": "00b7cef4",
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
      "definition_site": "00b7ce24",
      "incomplete_value": true,
      "site": "00b7ce2c",
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
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7ce9c",
      "READ",
      [
        "storage",
        "010a1f68",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7cea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7cec8"
      ]
    ],
    [
      "unmatched:00b7cde8",
      "DATA",
      [
        "storage",
        "00c24818",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7ce9c",
      "READ",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7cea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7cf90"
      ]
    ],
    [
      "00b7ceb0",
      "DATA",
      [
        "storage",
        "00c248c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd7c.md#insn-00b7cde4) · [`00b7cde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd7c.md#insn-00b7cde8) · [`00b7cdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cd7c.md#insn-00b7cdf4)
- 新版 `00b7ceac`（命令位置の公開資料なし） · `00b7cebc`（命令位置の公開資料なし）

~~~diff
- 00b7cde4 ["COPY", "register:4048:8", ["const:c24818:8"]]
+ 00b7ceac ["COPY", "register:4048:8", ["const:c248c8:8"]]
- 00b7cde4 bytes a9d15310
+ 00b7ceac bytes e9d05310
- 00b7cde8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7cde8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b7cde8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b7cde8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7cde8 bytes a8273fa9
- 00b7cdf4 ["INT_ADD", "register:40f0:8", ["const:b7cdf4:8", "const:4:8"]]
- 00b7cdf4 ["CALL", null, ["callee:00be10f0:8"]]
+ 00b7cebc ["INT_ADD", "register:40f0:8", ["const:b7cebc:8", "const:4:8"]]
+ 00b7cebc ["CALL", null, ["callee:00be10f0:8"]]
- 00b7cdf4 bytes 93900194
+ 00b7cebc bytes 8d900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a7af201fc0d0c3a09bc9a966792f09"></a>

### [`00b7cfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfbc.md) → [`00b7d084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d084.md) _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00be1120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00be11d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be11d0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7cfdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cfbc.md#insn-00b7cfdc)
- 新版 `00b7d0a4`（命令位置の公開資料なし）

~~~diff
- 00b7cfdc ["INT_ADD", "register:40f0:8", ["const:b7cfdc:8", "const:4:8"]]
- 00b7cfdc ["CALL", null, ["callee:004377fc:8"]]
+ 00b7d0a4 ["INT_ADD", "register:40f0:8", ["const:b7d0a4:8", "const:4:8"]]
+ 00b7d0a4 ["CALL", null, ["callee:004377fc:8"]]
- 00b7cfdc bytes 08eae297
+ 00b7d0a4 bytes d6e9e297
~~~


<a id="compare-2302eef12a3acad0afe7864e78e1ea86"></a>

### [`00b7d10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d10c.md) → [`00b7d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d1d4.md) FUN_00b7d1d4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7d1fc",
      "incomplete_value": true,
      "site": "00b7d1fc",
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
      "definition_site": "00b7d134",
      "incomplete_value": true,
      "site": "00b7d134",
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
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d1f0",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d1fc",
      "DATA",
      [
        "storage",
        "00c12e30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00b7d1f0",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d1fc",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d10c.md#insn-00b7d128) · [`00b7d138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d10c.md#insn-00b7d138) · [`00b7d140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d10c.md#insn-00b7d140)
- 新版 `00b7d1f0`（命令位置の公開資料なし） · `00b7d200`（命令位置の公開資料なし） · `00b7d208`（命令位置の公開資料なし）

~~~diff
- 00b7d128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 00b7d128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7d1f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00b7d1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7d128 bytes 08b146f9
+ 00b7d1f0 bytes 080947f9
- 00b7d138 ["INT_ADD", "register:40f0:8", ["const:b7d138:8", "const:4:8"]]
- 00b7d138 ["CALL", null, ["callee:00bdb230:8"]]
+ 00b7d200 ["INT_ADD", "register:40f0:8", ["const:b7d200:8", "const:4:8"]]
+ 00b7d200 ["CALL", null, ["callee:00bdb230:8"]]
- 00b7d138 bytes 12780194
+ 00b7d200 bytes 0c780194
- 00b7d140 ["INT_ADD", "register:40f0:8", ["const:b7d140:8", "const:4:8"]]
- 00b7d140 ["CALL", null, ["callee:00bdafc0:8"]]
+ 00b7d208 ["INT_ADD", "register:40f0:8", ["const:b7d208:8", "const:4:8"]]
+ 00b7d208 ["CALL", null, ["callee:00bdafc0:8"]]
- 00b7d140 bytes 74770194
+ 00b7d208 bytes 6e770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7edf63c78a1046045263d98037520499"></a>

### [`00b7d168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d168.md) → [`00b7d230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d230.md) FUN_00b7d230

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ea0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d168.md#insn-00b7d17c)
- 新版 `00b7d244`（命令位置の公開資料なし）

~~~diff
- 00b7d17c ["INT_ADD", "register:40f0:8", ["const:b7d17c:8", "const:4:8"]]
- 00b7d17c ["CALL", null, ["callee:00be0ea0:8"]]
+ 00b7d244 ["INT_ADD", "register:40f0:8", ["const:b7d244:8", "const:4:8"]]
+ 00b7d244 ["CALL", null, ["callee:00be0ea0:8"]]
- 00b7d17c bytes 1d8f0194
+ 00b7d244 bytes 178f0194
~~~


<a id="compare-ee91145f6571a8c44d046889bdb1c9b6"></a>

### [`00b7d194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md) → [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`00418338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md) [`0042f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`00468c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00468/00468c18.md) [`0056c7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7d8.md) · 呼出先 1件 [`00bde710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde710.md)
- 新版 呼出元 6件 [`00418338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00468c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00468/00468c18.md) [`0056c7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md) · 呼出先 1件 [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md#insn-00b7d1a0)
- 新版 `00b7d268`（命令位置の公開資料なし）

~~~diff
- 00b7d1a0 ["INT_ADD", "register:40f0:8", ["const:b7d1a0:8", "const:4:8"]]
- 00b7d1a0 ["CALL", null, ["callee:00bde7c0:8"]]
+ 00b7d268 ["INT_ADD", "register:40f0:8", ["const:b7d268:8", "const:4:8"]]
+ 00b7d268 ["CALL", null, ["callee:00bde7c0:8"]]
- 00b7d1a0 bytes 5c850194
+ 00b7d268 bytes 56850194
~~~


<a id="compare-ebe0890d7293f08d7436d481f13d3e3d"></a>

### [`00b7d228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d228.md) → [`00b7d2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md) · 呼出先 6件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bde710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde710.md) [`00bdeed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeed0.md) [`00bdeee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeee0.md) [`00bdeef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeef0.md)
- 新版 呼出元 1件 [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md) · 呼出先 6件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md) [`00bdef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef80.md) [`00bdef90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefa0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 40.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7d308",
      "incomplete_value": true,
      "site": "00b7d30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d240",
      "incomplete_value": true,
      "site": "00b7d244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7d260",
      "incomplete_value": true,
      "site": "00b7d264",
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
      "definition_site": "00b7d25c",
      "incomplete_value": true,
      "site": "00b7d264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00b7d38c",
      "PARAM",
      [
        "storage",
        "00298a38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d38c",
      "PARAM",
      [
        "storage",
        "00298ac5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d228.md#insn-00b7d244) · [`00b7d264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d228.md#insn-00b7d264) · [`00b7d2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d228.md#insn-00b7d2c8)
- 新版 `00b7d30c`（命令位置の公開資料なし） · `00b7d32c`（命令位置の公開資料なし） · `00b7d390`（命令位置の公開資料なし）

~~~diff
- 00b7d244 ["INT_ADD", "register:40f0:8", ["const:b7d244:8", "const:4:8"]]
- 00b7d244 ["CALL", null, ["callee:00bdefa0:8"]]
+ 00b7d30c ["INT_ADD", "register:40f0:8", ["const:b7d30c:8", "const:4:8"]]
+ 00b7d30c ["CALL", null, ["callee:00bdefa0:8"]]
- 00b7d244 bytes 2b870194
+ 00b7d30c bytes 25870194
- 00b7d264 ["INT_ADD", "register:40f0:8", ["const:b7d264:8", "const:4:8"]]
- 00b7d264 ["CALL", null, ["callee:00bdef80:8"]]
+ 00b7d32c ["INT_ADD", "register:40f0:8", ["const:b7d32c:8", "const:4:8"]]
+ 00b7d32c ["CALL", null, ["callee:00bdef80:8"]]
- 00b7d264 bytes 1b870194
+ 00b7d32c bytes 15870194
- 00b7d2c8 ["INT_ADD", "register:40f0:8", ["const:b7d2c8:8", "const:4:8"]]
- 00b7d2c8 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d390 ["INT_ADD", "register:40f0:8", ["const:b7d390:8", "const:4:8"]]
+ 00b7d390 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d2c8 bytes c2770194
+ 00b7d390 bytes bc770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c7ffbae67ecf7204ba7b8a34f8fb929"></a>

### [`00b7d2ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2ec.md) → [`00b7d3b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd190.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md)
- 新版 呼出元 1件 [`00bdd240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7d3d8",
      "incomplete_value": false,
      "site": "00b7d3dc",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d310",
      "incomplete_value": false,
      "site": "00b7d314",
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
            "const:803:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d3d8",
      "PARAM",
      [
        "storage",
        "00297803",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d3d8",
      "PARAM",
      [
        "storage",
        "00297890",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2ec.md#insn-00b7d314) · [`00b7d2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2ec.md#insn-00b7d2f8) · [`00b7d310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2ec.md#insn-00b7d310)
- 新版 `00b7d3dc`（命令位置の公開資料なし） · `00b7d3c0`（命令位置の公開資料なし） · `00b7d3d8`（命令位置の公開資料なし）

~~~diff
- 00b7d314 ["INT_ADD", "register:40f0:8", ["const:b7d314:8", "const:4:8"]]
- 00b7d314 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d3dc ["INT_ADD", "register:40f0:8", ["const:b7d3dc:8", "const:4:8"]]
+ 00b7d3dc ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d314 bytes af770194
+ 00b7d3dc bytes a9770194
- 00b7d2f8 ["INT_ADD", "register:40f0:8", ["const:b7d2f8:8", "const:4:8"]]
- 00b7d2f8 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d3c0 ["INT_ADD", "register:40f0:8", ["const:b7d3c0:8", "const:4:8"]]
+ 00b7d3c0 ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d2f8 bytes 0a850194
+ 00b7d3c0 bytes 04850194
- 00b7d310 ["COPY", "tmp:0:8", ["const:803:8"]]
- 00b7d310 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d310 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d310 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d3d8 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00b7d3d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d3d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d3d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d310 bytes 210c2091
+ 00b7d3d8 bytes 21402291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4e3b2818ad1f0cc505c156faa19ff5"></a>

### [`00b7d338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d338.md) → [`00b7d400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d400.md) _ZNSt6__ndk115recursive_mutex8try_lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1170.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1220.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d338.md#insn-00b7d344)
- 新版 `00b7d40c`（命令位置の公開資料なし）

~~~diff
- 00b7d344 ["INT_ADD", "register:40f0:8", ["const:b7d344:8", "const:4:8"]]
- 00b7d344 ["CALL", null, ["callee:00be1220:8"]]
+ 00b7d40c ["INT_ADD", "register:40f0:8", ["const:b7d40c:8", "const:4:8"]]
+ 00b7d40c ["CALL", null, ["callee:00be1220:8"]]
- 00b7d344 bytes 8b8f0194
+ 00b7d40c bytes 858f0194
~~~


<a id="compare-35f2b7f5fdeae039c59f99ff4afbda55"></a>

### [`00b7d37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d37c.md) → [`00b7d444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d444.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7d488",
      "incomplete_value": false,
      "site": "00b7d48c",
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
            "const:87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d3c0",
      "incomplete_value": false,
      "site": "00b7d3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:ffa:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d488",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d488",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d37c.md#insn-00b7d3c4) · [`00b7d390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d37c.md#insn-00b7d390) · [`00b7d39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d37c.md#insn-00b7d39c)
- 新版 `00b7d48c`（命令位置の公開資料なし） · `00b7d458`（命令位置の公開資料なし） · `00b7d464`（命令位置の公開資料なし）

~~~diff
- 00b7d3c4 ["INT_ADD", "register:40f0:8", ["const:b7d3c4:8", "const:4:8"]]
- 00b7d3c4 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d48c ["INT_ADD", "register:40f0:8", ["const:b7d48c:8", "const:4:8"]]
+ 00b7d48c ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d3c4 bytes 83770194
+ 00b7d48c bytes 7d770194
- 00b7d390 ["INT_ADD", "register:40f0:8", ["const:b7d390:8", "const:4:8"]]
- 00b7d390 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d458 ["INT_ADD", "register:40f0:8", ["const:b7d458:8", "const:4:8"]]
+ 00b7d458 ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d390 bytes e4840194
+ 00b7d458 bytes de840194
- 00b7d39c ["INT_ADD", "register:40f0:8", ["const:b7d39c:8", "const:4:8"]]
- 00b7d39c ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d464 ["INT_ADD", "register:40f0:8", ["const:b7d464:8", "const:4:8"]]
+ 00b7d464 ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d39c bytes e5840194
+ 00b7d464 bytes df840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad04c7f5655c7e42a361319ce6b086dc"></a>

### [`00b7d3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d3d0.md) → [`00b7d498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d498.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdb530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb530.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7d51c",
      "incomplete_value": false,
      "site": "00b7d520",
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
            "const:87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d454",
      "incomplete_value": false,
      "site": "00b7d458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:ffa:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d51c",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d51c",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d3d0.md#insn-00b7d458) · [`00b7d3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d3d0.md#insn-00b7d3f4) · [`00b7d40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d3d0.md#insn-00b7d40c)
- 新版 `00b7d520`（命令位置の公開資料なし） · `00b7d4bc`（命令位置の公開資料なし） · `00b7d4d4`（命令位置の公開資料なし）

~~~diff
- 00b7d458 ["INT_ADD", "register:40f0:8", ["const:b7d458:8", "const:4:8"]]
- 00b7d458 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d520 ["INT_ADD", "register:40f0:8", ["const:b7d520:8", "const:4:8"]]
+ 00b7d520 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d458 bytes 5e770194
+ 00b7d520 bytes 58770194
- 00b7d3f4 ["INT_ADD", "register:40f0:8", ["const:b7d3f4:8", "const:4:8"]]
- 00b7d3f4 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d4bc ["INT_ADD", "register:40f0:8", ["const:b7d4bc:8", "const:4:8"]]
+ 00b7d4bc ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d3f4 bytes cb840194
+ 00b7d4bc bytes c5840194
- 00b7d40c ["INT_ADD", "register:40f0:8", ["const:b7d40c:8", "const:4:8"]]
- 00b7d40c ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00b7d4d4 ["INT_ADD", "register:40f0:8", ["const:b7d4d4:8", "const:4:8"]]
+ 00b7d4d4 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00b7d40c bytes 49780194
+ 00b7d4d4 bytes 43780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7505dd291176192e72a2d1bde76fe3b4"></a>

### [`00b7d4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d4c0.md) → [`00b7d588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdc1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7d5cc",
      "incomplete_value": false,
      "site": "00b7d5d0",
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
            "const:87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d504",
      "incomplete_value": false,
      "site": "00b7d508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:ffa:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d5cc",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d5cc",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d4c0.md#insn-00b7d508) · [`00b7d4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d4c0.md#insn-00b7d4d4) · [`00b7d4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d4c0.md#insn-00b7d4e4)
- 新版 `00b7d5d0`（命令位置の公開資料なし） · `00b7d59c`（命令位置の公開資料なし） · `00b7d5ac`（命令位置の公開資料なし）

~~~diff
- 00b7d508 ["INT_ADD", "register:40f0:8", ["const:b7d508:8", "const:4:8"]]
- 00b7d508 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d5d0 ["INT_ADD", "register:40f0:8", ["const:b7d5d0:8", "const:4:8"]]
+ 00b7d5d0 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d508 bytes 32770194
+ 00b7d5d0 bytes 2c770194
- 00b7d4d4 ["INT_ADD", "register:40f0:8", ["const:b7d4d4:8", "const:4:8"]]
- 00b7d4d4 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d59c ["INT_ADD", "register:40f0:8", ["const:b7d59c:8", "const:4:8"]]
+ 00b7d59c ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d4d4 bytes 93840194
+ 00b7d59c bytes 8d840194
- 00b7d4e4 ["INT_ADD", "register:40f0:8", ["const:b7d4e4:8", "const:4:8"]]
- 00b7d4e4 ["CALL", null, ["callee:00bdc270:8"]]
+ 00b7d5ac ["INT_ADD", "register:40f0:8", ["const:b7d5ac:8", "const:4:8"]]
+ 00b7d5ac ["CALL", null, ["callee:00bdc270:8"]]
- 00b7d4e4 bytes 377b0194
+ 00b7d5ac bytes 317b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

