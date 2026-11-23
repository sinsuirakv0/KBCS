# v15.7.2 → v15.7.3 · 最優先の変更候補 (46)

[一覧の目次](README.md)

<a id="compare-40b5fcf711a6b7089377b2bf680390f7"></a>

### [`008b70b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b70b8.md) → [`008b70b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md) _INIT_169

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b70f4",
      "incomplete_value": true,
      "site": "008b7110",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b70f4",
      "incomplete_value": true,
      "site": "008b7110",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7138",
      "incomplete_value": true,
      "site": "008b7154",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7138",
      "incomplete_value": true,
      "site": "008b7154",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7174",
      "incomplete_value": true,
      "site": "008b7190",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7174",
      "incomplete_value": true,
      "site": "008b7190",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:2e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b70f4",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008b7118",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008b7138",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b70f4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008b7118",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008b7138",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b70e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b70b8.md#insn-008b70e4) · [`008b70ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b70b8.md#insn-008b70ec)
- 新版 [`008b70e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md#insn-008b70e4) · [`008b70ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md#insn-008b70ec)

~~~diff
- 008b70e4 ["COPY", "tmp:0:8", ["const:670:8"]]
- 008b70e4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 008b70e4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 bytes 73c21991
+ 008b70e4 bytes 73c21c91
- 008b70ec ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008b70ec bytes 89cfff90
+ 008b70ec ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008b70ec bytes 89cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c955427f8c37f464bf603e90d734080a"></a>

### [`008b7448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7448.md) → [`008b7448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md) FUN_008b7448

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ae96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae96c.md) · 呼出先 2件 [`008b74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md) [`008b7948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7948.md)
- 新版 呼出元 1件 [`006ae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae96c.md) · 呼出先 2件 [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) [`008b7948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7948.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b74a4",
      "incomplete_value": true,
      "site": "008b74a4",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b74a4",
      "incomplete_value": true,
      "site": "008b74a4",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b74cc",
      "incomplete_value": true,
      "site": "008b74cc",
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
            "const:6dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b74cc",
      "incomplete_value": true,
      "site": "008b74cc",
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
            "const:62c:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b7484",
      "READ",
      [
        "storage",
        "00c24628",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74a4",
      "WRITE",
      [
        "storage",
        "00c24628",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74ac",
      "READ",
      [
        "storage",
        "00c2462c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008b7484",
      "READ",
      [
        "storage",
        "00c246d8",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74a4",
      "WRITE",
      [
        "storage",
        "00c246d8",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74ac",
      "READ",
      [
        "storage",
        "00c246dc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b74a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7448.md#insn-008b74a4) · [`008b74cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7448.md#insn-008b74cc) · [`008b7484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7448.md#insn-008b7484)
- 新版 [`008b74a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b74a4) · [`008b74cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b74cc) · [`008b7484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b7484)

~~~diff
- 008b74a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 008b74a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b74a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 008b74a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74a4 bytes 682a06b9
+ 008b74a4 bytes 68da06b9
- 008b74cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:62c:8"]]
- 008b74cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b74cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6dc:8"]]
+ 008b74cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74cc bytes 682e06b9
+ 008b74cc bytes 68de06b9
- 008b7484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 008b7484 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 008b7484 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 008b7484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 008b7484 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 008b7484 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 008b7484 bytes 682a46b9
+ 008b7484 bytes 68da46b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95b005dcd613755df64e74c8c8e62f3f"></a>

### [`008b74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md) → [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) FUN_008b74dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008b7448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7448.md) [`008b8260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b8260.md) [`008c1354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060dcac.md) [`008be334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md)
- 新版 呼出元 4件 [`008b7448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md) [`008b8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md) [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md) [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b7894",
      "incomplete_value": false,
      "site": "008b7894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7894",
      "incomplete_value": false,
      "site": "008b7894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b7704",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008b774c",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "008b7750",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b7704",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b774c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "008b7750",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b76fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md#insn-008b76fc) · [`008b7700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md#insn-008b7700) · [`008b7748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md#insn-008b7748)
- 新版 [`008b76fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b76fc) · [`008b7700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b7700) · [`008b7748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b7748)

~~~diff
- 008b76fc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 008b76fc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 008b76fc bytes 681b00b0
+ 008b76fc bytes 681b00d0
- 008b7700 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008b7700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b7700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b7700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008b7700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b7700 bytes 08e13d91
+ 008b7700 bytes 08e10091
- 008b7748 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008b7748 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008b7748 bytes 601b00b0
+ 008b7748 bytes 601b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9ba03e015586f5b4dffde6d76148c8"></a>

### [`008b7b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7b38.md) → [`008b7b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md) FUN_008b7b38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7b8c",
      "incomplete_value": false,
      "site": "008b7b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7b8c",
      "incomplete_value": false,
      "site": "008b7b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:d3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:46:8"
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
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
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
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
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
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b7b94",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "00295046",
        null,
        "string"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "00295056",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b7b94",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "002950d3",
        null,
        "string"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "002950e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7b38.md#insn-008b7b8c) · [`008b7ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7b38.md#insn-008b7ba8) · [`008b7bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7b38.md#insn-008b7bac)
- 新版 [`008b7b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md#insn-008b7b8c) · [`008b7ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md#insn-008b7ba8)

~~~diff
- 008b7b8c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008b7b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008b7b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c bytes 29e13191
+ 008b7b8c bytes 29a13491
- 008b7ba8 ["COPY", "tmp:0:8", ["const:46:8"]]
- 008b7ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["COPY", "tmp:0:8", ["const:d3:8"]]
+ 008b7ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 bytes 4a190191
+ 008b7ba8 bytes 4a4d0391
- 008b7bac ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 008b7bac bytes c8cfffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c05158b88f55bd8488482f12161973"></a>

### [`008b7f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7f70.md) → [`008b7f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md) FUN_008b7f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md) · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md) [`0063e588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e588.md)
- 新版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) [`0063e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e588.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7fac",
      "incomplete_value": true,
      "site": "008b7fbc",
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
                "const:1b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7fac",
      "incomplete_value": true,
      "site": "008b7fbc",
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
                "const:125:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7fc0",
      "incomplete_value": true,
      "site": "008b7fc0",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7fc0",
      "incomplete_value": true,
      "site": "008b7fc0",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b8010",
      "incomplete_value": true,
      "site": "008b8010",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:6d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b8010",
      "incomplete_value": true,
      "site": "008b8010",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b7fac",
      "READ",
      [
        "storage",
        "00296125",
        null,
        "string"
      ]
    ],
    [
      "008b7fb0",
      "READ",
      [
        "storage",
        "00296134",
        null,
        "string"
      ]
    ],
    [
      "008b8000",
      "READ",
      [
        "storage",
        "002a46e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b7fac",
      "READ",
      [
        "storage",
        "002961b2",
        null,
        "string"
      ]
    ],
    [
      "008b7fb0",
      "READ",
      [
        "storage",
        "002961c1",
        null,
        "string"
      ]
    ],
    [
      "008b8000",
      "READ",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7f70.md#insn-008b7fa4) · [`008b7fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7f70.md#insn-008b7fa8)
- 新版 [`008b7fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md#insn-008b7fa4) · [`008b7fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md#insn-008b7fa8)

~~~diff
- 008b7fa4 ["COPY", "tmp:0:8", ["const:125:8"]]
- 008b7fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 008b7fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 bytes 08950491
+ 008b7fa4 bytes 08c90691
- 008b7fa8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 008b7fa8 bytes c9cfffb0
+ 008b7fa8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 008b7fa8 bytes c9cfffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ea6fe6cf53770c89707be760928708"></a>

### [`008b8260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b8260.md) → [`008b8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md) FUN_008b8260

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.30% / 新版 93.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b834c",
      "incomplete_value": true,
      "site": "008b834c",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b834c",
      "incomplete_value": true,
      "site": "008b834c",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:ac2:8"
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
      "definition_site": "008b84e4",
      "incomplete_value": true,
      "site": "008b84e4",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b5c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b84e4",
      "incomplete_value": true,
      "site": "008b84e4",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:acf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b87fc",
      "incomplete_value": false,
      "site": "008b87fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b87fc",
      "incomplete_value": false,
      "site": "008b87fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b8324",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008b8338",
      "READ",
      [
        "storage",
        "0029bac2",
        null,
        "string"
      ]
    ],
    [
      "008b83c0",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b8324",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b8338",
      "READ",
      [
        "storage",
        "0029bb4f",
        null,
        "string"
      ]
    ],
    [
      "008b83c0",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b87fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b8260.md#insn-008b87fc) · [`008b881c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b8260.md#insn-008b881c) · [`008b831c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b8260.md#insn-008b831c)
- 新版 [`008b87fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b87fc) · [`008b881c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b881c) · [`008b831c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b831c)

~~~diff
- 008b87fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:628:8"]]
- 008b87fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b87fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
+ 008b87fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b87fc bytes 282906b9
+ 008b87fc bytes 28d906b9
- 008b881c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:62c:8"]]
- 008b881c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b881c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6dc:8"]]
+ 008b881c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b881c bytes 282d06b9
+ 008b881c bytes 28dd06b9
- 008b831c ["COPY", "register:40d0:8", ["const:c24000:8"]]
+ 008b831c ["COPY", "register:40d0:8", ["const:c25000:8"]]
- 008b831c bytes 7a1b0090
+ 008b831c bytes 7a1b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2851bb1ef73db5f149778cb33f255d"></a>

### [`008b89f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b89f8.md) → [`008b89f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md) FUN_008b89f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.49% / 新版 98.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b8a14",
      "incomplete_value": true,
      "site": "008b8a14",
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
      "definition_site": "008b8a14",
      "incomplete_value": true,
      "site": "008b8a14",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b8a1c",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b8a1c",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b8a24",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b8a24",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b8a10",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b8a1c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b8a24",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008b8a10",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b8a1c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b8a24",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b8a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b89f8.md#insn-008b8a10) · [`008b8a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b89f8.md#insn-008b8a1c) · [`008b8a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b8/008b89f8.md#insn-008b8a24)
- 新版 [`008b8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a10) · [`008b8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a1c) · [`008b8a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a24)

~~~diff
- 008b8a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008b8a10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b8a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008b8a10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008b8a10 bytes 08dd44f9
+ 008b8a10 bytes 083d45f9
- 008b8a1c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008b8a1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008b8a1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c bytes 21603691
+ 008b8a1c bytes 21203991
- 008b8a24 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008b8a24 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008b8a24 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 bytes 42e01791
+ 008b8a24 bytes 42a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-370de2f529dcfa6e7ab38a7d32c7830a"></a>

### [`008b9174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b9/008b9174.md) → [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) FUN_008b9174

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008bb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md) [`008bf000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf000.md) [`008c2634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md) · 呼出先 53件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md)
- 新版 呼出元 3件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) [`008bf000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf000.md) [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 53件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.18% / 新版 94.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 32件, `store_destination` 50件, `store_value` 19件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b9864",
      "incomplete_value": false,
      "site": "008b9864",
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
            "const:ff9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b9864",
      "incomplete_value": false,
      "site": "008b9864",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b9890",
      "incomplete_value": false,
      "site": "008b9890",
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
            "const:299:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b9890",
      "incomplete_value": false,
      "site": "008b9890",
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
            "const:20c:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b98b8",
      "incomplete_value": false,
      "site": "008b98b8",
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
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b98b8",
      "incomplete_value": false,
      "site": "008b98b8",
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
            "const:c2f:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b9864",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "008b9890",
      "DATA",
      [
        "storage",
        "0029820c",
        null,
        "string"
      ]
    ],
    [
      "008b98b8",
      "DATA",
      [
        "storage",
        "002adc2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b9864",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "008b9890",
      "DATA",
      [
        "storage",
        "00298299",
        null,
        "string"
      ]
    ],
    [
      "008b98b8",
      "DATA",
      [
        "storage",
        "002adb9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b985c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b9/008b9174.md#insn-008b985c) · [`008b9884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b9/008b9174.md#insn-008b9884) · [`008b988c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b9/008b9174.md#insn-008b988c)
- 新版 [`008b985c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md#insn-008b985c) · [`008b9884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md#insn-008b9884)

~~~diff
- 008b985c ["COPY", "tmp:0:8", ["const:f6c:8"]]
- 008b985c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b985c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b985c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["COPY", "tmp:0:8", ["const:ff9:8"]]
+ 008b985c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b985c bytes 08b13d91
+ 008b985c bytes 08e53f91
- 008b9884 ["COPY", "tmp:0:8", ["const:20c:8"]]
- 008b9884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b9884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b9884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["COPY", "tmp:0:8", ["const:299:8"]]
+ 008b9884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b9884 bytes 08310891
+ 008b9884 bytes 08650a91
- 008b988c ["INT_SUB", "register:4008:8", ["register:40e8:8", "const:80:8"]]
- 008b988c bytes a10302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-830f4440776223f6eba9c15ac34b9644"></a>

### [`008bb8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb8c4.md) → [`008bb8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md) FUN_008bb8c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0069ab88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069ab88.md) [`0069bb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069b/0069bb8c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 1件 [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md) [`0069bb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069b/0069bb8c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bb8e4",
      "incomplete_value": true,
      "site": "008bb8e4",
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
      "definition_site": "008bb8e4",
      "incomplete_value": true,
      "site": "008bb8e4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bb8ec",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bb8ec",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bb8f4",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bb8f4",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008bb8e0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bb8ec",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bb8f4",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bb8e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bb8ec",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bb8f4",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bb8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb8c4.md#insn-008bb8e0) · [`008bb8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb8c4.md#insn-008bb8ec) · [`008bb8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb8c4.md#insn-008bb8f4)
- 新版 [`008bb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8e0) · [`008bb8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8ec) · [`008bb8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8f4)

~~~diff
- 008bb8e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008bb8e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bb8e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008bb8e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bb8e0 bytes 08dd44f9
+ 008bb8e0 bytes 083d45f9
- 008bb8ec ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008bb8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008bb8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec bytes 21603691
+ 008bb8ec bytes 21203991
- 008bb8f4 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008bb8f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008bb8f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 bytes 42e01791
+ 008bb8f4 bytes 42a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055e0d92c18b627729e02b5d05055cfc"></a>

### [`008bb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md) → [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) FUN_008bb9b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c26e0.md) · 呼出先 41件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044bf2c.md)
- 新版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c26e0.md) · 呼出先 41件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044bf2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.27% / 新版 98.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008bbd14",
      "incomplete_value": true,
      "site": "008bbd28",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:e27:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bbd14",
      "incomplete_value": true,
      "site": "008bbd28",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:e21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008bbf50",
      "incomplete_value": false,
      "site": "008bbf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bbf50",
      "incomplete_value": false,
      "site": "008bbf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bc5bc",
      "incomplete_value": true,
      "site": "008bc5d4",
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc5bc",
      "incomplete_value": true,
      "site": "008bc5d4",
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 95,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008bbb14",
      "READ",
      [
        "storage",
        "00c1b630",
        null,
        "pointer"
      ]
    ],
    [
      "008bbb20",
      "DATA",
      [
        "storage",
        "00c23fc4",
        null,
        null
      ]
    ],
    [
      "008bbd14",
      "READ",
      [
        "storage",
        "002abe21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008bbb14",
      "READ",
      [
        "storage",
        "00c1b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "008bbb20",
      "DATA",
      [
        "storage",
        "00c24074",
        null,
        null
      ]
    ],
    [
      "008bbd14",
      "READ",
      [
        "storage",
        "002abe27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bbb14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md#insn-008bbb14) · [`008bbd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md#insn-008bbd0c) · [`008bbf4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md#insn-008bbf4c)
- 新版 [`008bbb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bbb14) · [`008bbd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bbd0c) · [`008bbf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bbf4c)

~~~diff
- 008bbb14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:630:8"]]
- 008bbb14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bbb14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e0:8"]]
+ 008bbb14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 008bbb14 bytes 291943f9
+ 008bbb14 bytes 297143f9
- 008bbd0c ["COPY", "tmp:0:8", ["const:e21:8"]]
- 008bbd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008bbd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008bbd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008bbd0c ["COPY", "tmp:0:8", ["const:e27:8"]]
+ 008bbd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008bbd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008bbd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008bbd0c bytes 29853891
+ 008bbd0c bytes 299d3891
- 008bbf4c ["COPY", "tmp:0:8", ["const:620:8"]]
- 008bbf4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 008bbf4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c bytes 08811891
+ 008bbf4c bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-993d7a2e5cc1bc63ad19fb3329eb867c"></a>

### [`008bc990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bc/008bc990.md) → [`008bc990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md) FUN_008bc990

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 99.62% / 新版 99.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bc9d4",
      "incomplete_value": true,
      "site": "008bc9d4",
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
      "definition_site": "008bc9d4",
      "incomplete_value": true,
      "site": "008bc9d4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bc9dc",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc9dc",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bc9e4",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc9e4",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008bc9d0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bc9dc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bc9e4",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bc9d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bc9dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bc9e4",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bc9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bc/008bc990.md#insn-008bc9d0) · [`008bc9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bc/008bc990.md#insn-008bc9dc) · [`008bc9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bc/008bc990.md#insn-008bc9e4)
- 新版 [`008bc9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9d0) · [`008bc9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9dc) · [`008bc9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9e4)

~~~diff
- 008bc9d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008bc9d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bc9d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008bc9d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bc9d0 bytes 08dd44f9
+ 008bc9d0 bytes 083d45f9
- 008bc9dc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008bc9dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008bc9dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc bytes 21603691
+ 008bc9dc bytes 21203991
- 008bc9e4 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008bc9e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008bc9e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 bytes 42e01791
+ 008bc9e4 bytes 42a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9808b36abf119a2b2b08354b366832e0"></a>

### [`008be334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md) → [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md) FUN_008be334

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b74dc.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md) [`00640008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00640/00640008.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008c4a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md)
- 新版 呼出元 1件 [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`00640008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008be458",
      "incomplete_value": true,
      "site": "008be46c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:859:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008be458",
      "incomplete_value": true,
      "site": "008be46c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008be4ac",
      "incomplete_value": true,
      "site": "008be4ac",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:732:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008be4ac",
      "incomplete_value": true,
      "site": "008be4ac",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:7c6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008be5b0",
      "incomplete_value": false,
      "site": "008be5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "008be5b0",
      "incomplete_value": false,
      "site": "008be5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 20,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008be444",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008be458",
      "READ",
      [
        "storage",
        "002a5860",
        null,
        "string"
      ]
    ],
    [
      "008be478",
      "PARAM",
      [
        "storage",
        "002a9c7b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008be444",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008be458",
      "READ",
      [
        "storage",
        "002a5859",
        null,
        "string"
      ]
    ],
    [
      "008be478",
      "PARAM",
      [
        "storage",
        "002a9c72",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008be43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md#insn-008be43c) · [`008be440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md#insn-008be440) · [`008be44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md#insn-008be44c)
- 新版 [`008be43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md#insn-008be43c) · [`008be440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md#insn-008be440)

~~~diff
- 008be43c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 008be43c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 008be43c bytes 281b00d0
+ 008be43c bytes 281b00f0
- 008be440 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008be440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008be440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008be440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008be440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008be440 bytes 08e13d91
+ 008be440 bytes 08e10091
- 008be44c ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 008be44c bytes 29cffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a784aa9a2328f145ec775485464c2171"></a>

### [`008bf204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf204.md) → [`008bf204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md) FUN_008bf204

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2284.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00445e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445e30.md)
- 新版 呼出元 1件 [`008c2284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2284.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bf238",
      "incomplete_value": true,
      "site": "008bf238",
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
      "definition_site": "008bf238",
      "incomplete_value": true,
      "site": "008bf238",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bf240",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bf240",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bf248",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bf248",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008bf230",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bf240",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bf248",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bf230",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bf240",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bf248",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bf230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf204.md#insn-008bf230) · [`008bf240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf204.md#insn-008bf240) · [`008bf248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf204.md#insn-008bf248)
- 新版 [`008bf230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf230) · [`008bf240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf240) · [`008bf248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf248)

~~~diff
- 008bf230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008bf230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bf230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008bf230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bf230 bytes 08dd44f9
+ 008bf230 bytes 083d45f9
- 008bf240 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008bf240 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bf240 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bf240 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008bf240 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bf240 bytes 21603691
+ 008bf240 bytes 21203991
- 008bf248 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008bf248 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bf248 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bf248 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008bf248 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bf248 bytes 42e01791
+ 008bf248 bytes 42a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4175d4749d90375d2cab663c3a8cda"></a>

### [`008bf94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf94c.md) → [`008bf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md) FUN_008bf94c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006ae96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae96c.md) [`008bf94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf94c.md) [`008c1354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md)
- 新版 呼出元 4件 [`006ae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae96c.md) [`008bf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md) [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0794",
      "incomplete_value": false,
      "site": "008c0794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c0794",
      "incomplete_value": false,
      "site": "008c0794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 163,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0840",
      "incomplete_value": true,
      "site": "008c085c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:d5b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c0840",
      "incomplete_value": true,
      "site": "008c085c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:d62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 167,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0860",
      "incomplete_value": true,
      "site": "008c0860",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c0860",
      "incomplete_value": true,
      "site": "008c0860",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 168,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c0794",
      "DATA",
      [
        "storage",
        "00c076a0",
        null,
        "undefined *"
      ]
    ],
    [
      "008c07ec",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c07f8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c0794",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ],
    [
      "008c07ec",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c07f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c0788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf94c.md#insn-008c0788) · [`008c07ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf94c.md#insn-008c07ec) · [`008c07f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bf/008bf94c.md#insn-008c07f8)
- 新版 [`008c0788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c0788) · [`008c07ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c07ec) · [`008c07f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c07f8)

~~~diff
- 008c0788 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 008c0788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c0788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c0788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 008c0788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c0788 bytes 08811a91
+ 008c0788 bytes 08411d91
- 008c07ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008c07ec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c07ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008c07ec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008c07ec bytes 00dd44f9
+ 008c07ec bytes 003d45f9
- 008c07f8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008c07f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008c07f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 bytes 21603691
+ 008c07f8 bytes 21203991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e643a78e7e3b8be4d8124939a2b2c0c"></a>

### [`008c1354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md) → [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) FUN_008c1354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md) · 呼出先 27件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`0063e4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e4a8.md)
- 新版 呼出元 1件 [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 27件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c1960",
      "incomplete_value": false,
      "site": "008c1960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c1960",
      "incomplete_value": false,
      "site": "008c1960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 109,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c1980",
      "incomplete_value": false,
      "site": "008c1980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c1980",
      "incomplete_value": false,
      "site": "008c1980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:62c:8"
          ]
        ]
      ]
    },
    "ordinal": 110,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008c1390",
      "incomplete_value": true,
      "site": "008c1390",
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
      "definition_site": "008c1390",
      "incomplete_value": true,
      "site": "008c1390",
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
      "008c138c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c1398",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c13a0",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c138c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c1398",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c13a0",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c1960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md#insn-008c1960) · [`008c1980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md#insn-008c1980) · [`008c138c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1354.md#insn-008c138c)
- 新版 [`008c1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c1960) · [`008c1980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c1980) · [`008c138c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c138c)

~~~diff
- 008c1960 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:628:8"]]
- 008c1960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c1960 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
+ 008c1960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c1960 bytes 282906b9
+ 008c1960 bytes 28d906b9
- 008c1980 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:62c:8"]]
- 008c1980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c1980 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6dc:8"]]
+ 008c1980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c1980 bytes 282d06b9
+ 008c1980 bytes 28dd06b9
- 008c138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008c138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008c138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008c138c bytes 08dd44f9
+ 008c138c bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c925f48825407771d7bd5427031a5492"></a>

### [`008c1b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1b84.md) → [`008c1b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md) FUN_008c1b84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c26e0.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00650740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00650/00650740.md) [`0069ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069ab94.md) [`0069bc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069b/0069bc74.md)
- 新版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c26e0.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00650740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650740.md) [`0069ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab94.md) [`0069bc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069b/0069bc74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:c6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:bde:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
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
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
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
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fbde",
        null,
        "string"
      ]
    ],
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fbee",
        null,
        "string"
      ]
    ],
    [
      "008c20ec",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fc6b",
        null,
        "string"
      ]
    ],
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fc7b",
        null,
        "string"
      ]
    ],
    [
      "008c20ec",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c20bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1b84.md#insn-008c20bc) · [`008c20e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c1/008c1b84.md#insn-008c20e4)
- 新版 [`008c20bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md#insn-008c20bc) · [`008c20e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md#insn-008c20e4)

~~~diff
- 008c20bc ["COPY", "tmp:0:8", ["const:bde:8"]]
- 008c20bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c20bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c20bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["COPY", "tmp:0:8", ["const:c6b:8"]]
+ 008c20bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c20bc bytes 08792f91
+ 008c20bc bytes 08ad3191
- 008c20e4 ["COPY", "tmp:0:8", ["const:720:8"]]
- 008c20e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 008c20e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 bytes 08811c91
+ 008c20e4 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cda41b6b594655bee2c2dc864bbc8e5"></a>

### [`008c2634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md) → [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) FUN_008c2634

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md) · 呼出先 7件 [`00646dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00646/00646dc4.md) [`0069de18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069d/0069de18.md) [`006a86c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a8/006a86c4.md) [`008b9174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b9/008b9174.md) [`008bb8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb8c4.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 7件 [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`0069de18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069d/0069de18.md) [`006a86c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a86c4.md) [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) [`008bb8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008c264c",
      "incomplete_value": true,
      "site": "008c264c",
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
      "definition_site": "008c264c",
      "incomplete_value": true,
      "site": "008c264c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c2654",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2654",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c265c",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c265c",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c2648",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2654",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c265c",
      "PARAM",
      [
        "storage",
        "00c075f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c2648",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2654",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c265c",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md#insn-008c2648) · [`008c2654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md#insn-008c2654) · [`008c265c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2634.md#insn-008c265c)
- 新版 [`008c2648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c2648) · [`008c2654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c2654) · [`008c265c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c265c)

~~~diff
- 008c2648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008c2648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c2648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008c2648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008c2648 bytes 08dd44f9
+ 008c2648 bytes 083d45f9
- 008c2654 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008c2654 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c2654 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c2654 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008c2654 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c2654 bytes 21603691
+ 008c2654 bytes 21203991
- 008c265c ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008c265c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008c265c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008c265c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008c265c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008c265c bytes 42e01791
+ 008c265c bytes 42a01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8108e9b8d2eb71b18e4cbe03445b457"></a>

### [`008c2704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md) → [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) FUN_008c2704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 16件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`007f96a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f96a4.md) [`007f96d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f96d8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 16件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md) [`007f96d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96d8.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2738",
      "incomplete_value": false,
      "site": "008c2738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2738",
      "incomplete_value": false,
      "site": "008c2738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c272c",
      "incomplete_value": true,
      "site": "008c2738",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c272c",
      "incomplete_value": true,
      "site": "008c2738",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c273c",
      "incomplete_value": false,
      "site": "008c273c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c273c",
      "incomplete_value": false,
      "site": "008c273c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c272c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2730",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2738",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008c272c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2730",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2738",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md#insn-008c2738) · [`008c273c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md#insn-008c273c) · [`008c278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md#insn-008c278c)
- 新版 [`008c2738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c2738) · [`008c273c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c273c) · [`008c278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c278c)

~~~diff
- 008c2738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008c2738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008c2738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008c2738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008c2738 bytes 09d504f9
+ 008c2738 bytes 093505f9
- 008c273c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:9b8:8"]]
- 008c273c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008c273c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
+ 008c273c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008c273c bytes 8adf04f9
+ 008c273c bytes 8a3f05f9
- 008c278c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:9b8:8"]]
- 008c278c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008c278c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
+ 008c278c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008c278c bytes 94df04f9
+ 008c278c bytes 943f05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62f385dfcfbc1302f45b0f3c71499116"></a>

### [`008c2a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md) → [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) FUN_008c2a7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 44件 [`00429060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429060.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 44件 [`00429060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.42% / 新版 96.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 17件, `store_value` 5件

アドレスに依存する影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c2b0c",
      "incomplete_value": true,
      "site": "008c2b0c",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2b0c",
      "incomplete_value": true,
      "site": "008c2b0c",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2d54",
      "incomplete_value": true,
      "site": "008c2d54",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2d54",
      "incomplete_value": true,
      "site": "008c2d54",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2ed4",
      "incomplete_value": true,
      "site": "008c2ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2ed4",
      "incomplete_value": true,
      "site": "008c2ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c2afc",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ],
    [
      "008c2c78",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008c2c80",
      "READ",
      [
        "storage",
        "00c24f70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008c2afc",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ],
    [
      "008c2c78",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c2c80",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md#insn-008c2d54) · [`008c2ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md#insn-008c2ed4) · [`008c2fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md#insn-008c2fb0)
- 新版 [`008c2d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2d54) · [`008c2ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2ed4) · [`008c2fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2fb0)

~~~diff
- 008c2d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 008c2d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 008c2d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2d54 bytes 682a06b9
+ 008c2d54 bytes 68da06b9
- 008c2ed4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:628:8"]]
- 008c2ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2ed4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
+ 008c2ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2ed4 bytes 282906b9
+ 008c2ed4 bytes 28d906b9
- 008c2fb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:62c:8"]]
- 008c2fb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2fb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6dc:8"]]
+ 008c2fb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2fb0 bytes 682e06b9
+ 008c2fb0 bytes 68de06b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc90a964c7b560c96da0b21aa0598f1"></a>

### [`008c3e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md) → [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) FUN_008c3e08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 32件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d88.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 32件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.82% / 新版 94.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c48f8",
      "incomplete_value": false,
      "site": "008c48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c48f8",
      "incomplete_value": false,
      "site": "008c48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c3e48",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008c3e54",
      "READ",
      [
        "storage",
        "00c24f70",
        null,
        "undefined8"
      ]
    ],
    [
      "008c3e6c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008c3e48",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c3e54",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008c3e6c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c3e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md#insn-008c3e30) · [`008c3e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md#insn-008c3e34) · [`008c3e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c3/008c3e08.md#insn-008c3e50)
- 新版 [`008c3e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e30) · [`008c3e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e34) · [`008c3e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e50)

~~~diff
- 008c3e30 ["COPY", "register:40b8:8", ["const:c24000:8"]]
+ 008c3e30 ["COPY", "register:40b8:8", ["const:c25000:8"]]
- 008c3e30 bytes 171b00b0
+ 008c3e30 bytes 171b00d0
- 008c3e34 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008c3e34 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008c3e34 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 bytes f7e23d91
+ 008c3e34 bytes f7e20091
- 008c3e50 ["COPY", "register:40c0:8", ["const:c24000:8"]]
+ 008c3e50 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008c3e50 bytes 181b00b0
+ 008c3e50 bytes 181b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b2398e84f0c1a09e8ec8f9323cb0ac"></a>

### [`008c497c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c497c.md) → [`008c497c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c497c.md) FUN_008c497c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b7b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7b38.md) [`008b7e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b7/008b7e34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b7b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md) [`008b7e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7e34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c4988",
      "incomplete_value": false,
      "site": "008c498c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c4988",
      "incomplete_value": false,
      "site": "008c498c",
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
            "const:30a:8"
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
      "008c4988",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c4988",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c4988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c497c.md#insn-008c4988)
- 新版 [`008c4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c497c.md#insn-008c4988)

~~~diff
- 008c4988 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008c4988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008c4988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008c4988 bytes 00280c91
+ 008c4988 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d208bf72e972cfd382ad7d5c522c3738"></a>

### [`008c4994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4994.md) → [`008c4994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4994.md) FUN_008c4994

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c49b8",
      "incomplete_value": false,
      "site": "008c49b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c49b8",
      "incomplete_value": false,
      "site": "008c49b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "008c49b8",
      "DATA",
      [
        "storage",
        "00c07620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c49b8",
      "DATA",
      [
        "storage",
        "00c076d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c49b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4994.md#insn-008c49b4)
- 新版 [`008c49b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4994.md#insn-008c49b4)

~~~diff
- 008c49b4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 008c49b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 008c49b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 bytes 08811891
+ 008c49b4 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa3b2e7cc081087022cad8e3e420168"></a>

### [`008c49c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c49c8.md) → [`008c49c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c49c8.md) FUN_008c49c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c49d4",
      "incomplete_value": false,
      "site": "008c49d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c49d4",
      "incomplete_value": false,
      "site": "008c49d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "008c49d4",
      "DATA",
      [
        "storage",
        "00c07620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c49d4",
      "DATA",
      [
        "storage",
        "00c076d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c49d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c49c8.md#insn-008c49d0)
- 新版 [`008c49d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c49c8.md#insn-008c49d0)

~~~diff
- 008c49d0 ["COPY", "tmp:0:8", ["const:620:8"]]
- 008c49d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 008c49d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 bytes 29811891
+ 008c49d0 bytes 29411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e2e4ac190e274a77d6821f42f2f983"></a>

### [`008c4a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md) → [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) FUN_008c4a54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008be334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008be/008be334.md) [`008c4a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md) [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c4bb0",
      "incomplete_value": false,
      "site": "008c4bb8",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c4bb0",
      "incomplete_value": false,
      "site": "008c4bb8",
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
            "const:311:8"
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
      "definition_site": "008c4d08",
      "incomplete_value": false,
      "site": "008c4d10",
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
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c4d08",
      "incomplete_value": false,
      "site": "008c4d10",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c4db0",
      "incomplete_value": false,
      "site": "008c4dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c4db0",
      "incomplete_value": false,
      "site": "008c4dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c4bb0",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008c4d08",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008c4db0",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008c4bb0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008c4d08",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008c4db0",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c4bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md#insn-008c4bb0) · [`008c4d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md#insn-008c4d08) · [`008c4db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md#insn-008c4db0)
- 新版 [`008c4bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4bb0) · [`008c4d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4d08) · [`008c4db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4db0)

~~~diff
- 008c4bb0 ["COPY", "tmp:0:8", ["const:311:8"]]
- 008c4bb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008c4bb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 bytes 21440c91
+ 008c4bb0 bytes 21280c91
- 008c4d08 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008c4d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008c4d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 bytes 21d40b91
+ 008c4d08 bytes 21b80b91
- 008c4db0 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 008c4db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4db0 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 008c4db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4db0 bytes 21681f91
+ 008c4db0 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dec78df0d9b5907e6a677486a60abeaa"></a>

### [`008c526c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c526c.md) → [`008c526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md) FUN_008c526c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008c4a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c4/008c4a54.md) [`008c526c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c526c.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) [`008c526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c53c4",
      "incomplete_value": false,
      "site": "008c53cc",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c53c4",
      "incomplete_value": false,
      "site": "008c53cc",
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
            "const:311:8"
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
      "definition_site": "008c58e8",
      "incomplete_value": false,
      "site": "008c58f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c58e8",
      "incomplete_value": false,
      "site": "008c58f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c5988",
      "incomplete_value": false,
      "site": "008c5990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c5988",
      "incomplete_value": false,
      "site": "008c5990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c53c4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008c5480",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008c57f0",
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008c53c4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008c5480",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008c57f0",
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c53c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c526c.md#insn-008c53c4) · [`008c5480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c526c.md#insn-008c5480) · [`008c57f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c526c.md#insn-008c57f0)
- 新版 [`008c53c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c53c4) · [`008c5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c5480) · [`008c57f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c57f0)

~~~diff
- 008c53c4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 008c53c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008c53c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 bytes 21440c91
+ 008c53c4 bytes 21280c91
- 008c5480 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008c5480 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c5480 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c5480 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008c5480 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c5480 bytes 21d40b91
+ 008c5480 bytes 21b80b91
- 008c57f0 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 008c57f0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 008c57f0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 008c57f0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 008c57f0 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 008c57f0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 008c57f0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 008c57f0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 008c57f0 bytes 63941791
+ 008c57f0 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b294f06bfd5a19a1033f01454088c756"></a>

### [`008c5d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c5d2c.md) → [`008c5d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d2c.md) FUN_008c5d2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c5d40",
      "incomplete_value": false,
      "site": "008c5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c5d40",
      "incomplete_value": false,
      "site": "008c5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "008c5d44",
      "DATA",
      [
        "storage",
        "00c076a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c5d44",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c5d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c5d2c.md#insn-008c5d40)
- 新版 [`008c5d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d2c.md#insn-008c5d40)

~~~diff
- 008c5d40 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 008c5d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 008c5d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 bytes 08811a91
+ 008c5d40 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822852e46e9d398d88d747af6da76c63"></a>

### [`008c5d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c5d50.md) → [`008c5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d50.md) FUN_008c5d50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c5d54",
      "incomplete_value": false,
      "site": "008c5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c5d54",
      "incomplete_value": false,
      "site": "008c5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "008c5d58",
      "DATA",
      [
        "storage",
        "00c076a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c5d58",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c5d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c5/008c5d50.md#insn-008c5d54)
- 新版 [`008c5d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d50.md#insn-008c5d54)

~~~diff
- 008c5d54 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 008c5d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 008c5d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 bytes 08811a91
+ 008c5d54 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69b505b1a13858ba09c862bf004b5e41"></a>

### [`008c6ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6ae4.md) → [`008c6ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6ae4.md) FUN_008c6ae4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6af8",
      "incomplete_value": false,
      "site": "008c6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6af8",
      "incomplete_value": false,
      "site": "008c6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "008c6afc",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6afc",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6ae4.md#insn-008c6af8)
- 新版 [`008c6af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6ae4.md#insn-008c6af8)

~~~diff
- 008c6af8 ["COPY", "tmp:0:8", ["const:720:8"]]
- 008c6af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 008c6af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 bytes 08811c91
+ 008c6af8 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0771ab8b5427f368a9682551359c91a"></a>

### [`008c6b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b08.md) → [`008c6b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b08.md) FUN_008c6b08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6b0c",
      "incomplete_value": false,
      "site": "008c6b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6b0c",
      "incomplete_value": false,
      "site": "008c6b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "008c6b10",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6b10",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b08.md#insn-008c6b0c)
- 新版 [`008c6b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b08.md#insn-008c6b0c)

~~~diff
- 008c6b0c ["COPY", "tmp:0:8", ["const:720:8"]]
- 008c6b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 008c6b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c bytes 08811c91
+ 008c6b0c bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d3478e639ed61f2bf15258ee60ee72d"></a>

### [`008c6b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b20.md) → [`008c6b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md) FUN_008c6b20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
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
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:3af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
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
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:322:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
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
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6be4",
      "incomplete_value": false,
      "site": "008c6bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6be4",
      "incomplete_value": false,
      "site": "008c6bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a322",
        null,
        "string"
      ]
    ],
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a332",
        null,
        "string"
      ]
    ],
    [
      "008c6bec",
      "DATA",
      [
        "storage",
        "00c07790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3af",
        null,
        "string"
      ]
    ],
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3bf",
        null,
        "string"
      ]
    ],
    [
      "008c6bec",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b20.md#insn-008c6bbc) · [`008c6be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b20.md#insn-008c6be4) · [`008c6be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6b20.md#insn-008c6be8)
- 新版 [`008c6bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md#insn-008c6bbc) · [`008c6be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md#insn-008c6be4)

~~~diff
- 008c6bbc ["COPY", "tmp:0:8", ["const:322:8"]]
- 008c6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["COPY", "tmp:0:8", ["const:3af:8"]]
+ 008c6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc bytes 08890c91
+ 008c6bbc bytes 08bd0e91
- 008c6be4 ["COPY", "tmp:0:8", ["const:790:8"]]
- 008c6be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 008c6be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 bytes 08411e91
+ 008c6be4 bytes 08012191
- 008c6be8 ["COPY", "tmp:0:8", ["const:30:8"]]
- 008c6be8 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 008c6be8 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 008c6be8 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 008c6be8 bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c975899ded361465b2f7b3f648c67cb4"></a>

### [`008c6d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6d50.md) → [`008c6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d50.md) FUN_008c6d50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6d64",
      "incomplete_value": false,
      "site": "008c6d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6d64",
      "incomplete_value": false,
      "site": "008c6d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "008c6d68",
      "DATA",
      [
        "storage",
        "00c07790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6d68",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6d50.md#insn-008c6d64)
- 新版 [`008c6d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d50.md#insn-008c6d64)

~~~diff
- 008c6d64 ["COPY", "tmp:0:8", ["const:790:8"]]
- 008c6d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 008c6d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 bytes 08411e91
+ 008c6d64 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac8bf7d8bd64d9394dcc08964f5c2465"></a>

### [`008c6d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6d74.md) → [`008c6d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d74.md) FUN_008c6d74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6d78",
      "incomplete_value": false,
      "site": "008c6d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6d78",
      "incomplete_value": false,
      "site": "008c6d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "008c6d7c",
      "DATA",
      [
        "storage",
        "00c07790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6d7c",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6d74.md#insn-008c6d78)
- 新版 [`008c6d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d74.md#insn-008c6d78)

~~~diff
- 008c6d78 ["COPY", "tmp:0:8", ["const:790:8"]]
- 008c6d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 008c6d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 bytes 08411e91
+ 008c6d78 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024334d11e21592c076c9d21ec39cb88"></a>

### [`008c6e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6e18.md) → [`008c6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md) FUN_008c6e18

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2704.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072d/0072dfbc.md) [`00830c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00832/00832580.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`00830c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_destination` 7件, `store_value` 21件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6e50",
      "incomplete_value": false,
      "site": "008c6e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6e50",
      "incomplete_value": false,
      "site": "008c6e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6e98",
      "incomplete_value": true,
      "site": "008c6e98",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:895:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6e98",
      "incomplete_value": true,
      "site": "008c6e98",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:89c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6eb0",
      "incomplete_value": true,
      "site": "008c6eb0",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6eb0",
      "incomplete_value": true,
      "site": "008c6eb0",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:772:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c6e5c",
      "DATA",
      [
        "storage",
        "00c07820",
        null,
        "pointer"
      ]
    ],
    [
      "008c6e68",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008c6e88",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c6e5c",
      "DATA",
      [
        "storage",
        "00c078d0",
        null,
        "pointer"
      ]
    ],
    [
      "008c6e68",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c6e88",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6e18.md#insn-008c6e50) · [`008c6e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c6/008c6e18.md#insn-008c6e54)
- 新版 [`008c6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md#insn-008c6e50) · [`008c6e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md#insn-008c6e54)

~~~diff
- 008c6e50 ["COPY", "tmp:0:8", ["const:820:8"]]
- 008c6e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 008c6e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 bytes 08812091
+ 008c6e50 bytes 08412391
- 008c6e54 ["COPY", "register:40c0:8", ["const:c24000:8"]]
- 008c6e54 bytes f81a00d0
+ 008c6e54 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 008c6e54 bytes f81a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c982c84c465edc0746ad9ac116dbaf11"></a>

### [`008c7afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7afc.md) → [`008c7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md) FUN_008c7afc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7b14",
      "incomplete_value": false,
      "site": "008c7b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7b14",
      "incomplete_value": false,
      "site": "008c7b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7b50",
      "incomplete_value": false,
      "site": "008c7b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7b50",
      "incomplete_value": false,
      "site": "008c7b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c7b18",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "008c7b54",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008c7b18",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "008c7b54",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c7b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7afc.md#insn-008c7b14) · [`008c7b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7afc.md#insn-008c7b50)
- 新版 [`008c7b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md#insn-008c7b14) · [`008c7b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md#insn-008c7b50)

~~~diff
- 008c7b14 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 008c7b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 008c7b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 bytes 08213491
+ 008c7b14 bytes 08e13691
- 008c7b50 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008c7b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008c7b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 bytes 08a10791
+ 008c7b50 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2537a37540be11b0c508e593e896c6ec"></a>

### [`008c7b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7b9c.md) → [`008c7b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md) _INIT_170

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7bd8",
      "incomplete_value": true,
      "site": "008c7bf4",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7bd8",
      "incomplete_value": true,
      "site": "008c7bf4",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7bfc",
      "incomplete_value": true,
      "site": "008c7c18",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7bfc",
      "incomplete_value": true,
      "site": "008c7c18",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008c7c1c",
      "incomplete_value": true,
      "site": "008c7c38",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7c1c",
      "incomplete_value": true,
      "site": "008c7c38",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c7bd8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008c7bfc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008c7c1c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c7bd8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008c7bfc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008c7c1c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c7bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7b9c.md#insn-008c7bc8) · [`008c7bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7b9c.md#insn-008c7bd0)
- 新版 [`008c7bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md#insn-008c7bc8) · [`008c7bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md#insn-008c7bd0)

~~~diff
- 008c7bc8 ["COPY", "tmp:0:8", ["const:688:8"]]
- 008c7bc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 008c7bc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 bytes 73221a91
+ 008c7bc8 bytes 73221d91
- 008c7bd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008c7bd0 bytes 09cfff90
+ 008c7bd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008c7bd0 bytes 09cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c826994ffcad7ddda10efd988014b82"></a>

### [`008c7f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7f2c.md) → [`008c7f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md) _INIT_171

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7f68",
      "incomplete_value": true,
      "site": "008c7f84",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7f68",
      "incomplete_value": true,
      "site": "008c7f84",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7f8c",
      "incomplete_value": true,
      "site": "008c7fa8",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7f8c",
      "incomplete_value": true,
      "site": "008c7fa8",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008c7fac",
      "incomplete_value": true,
      "site": "008c7fc8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7fac",
      "incomplete_value": true,
      "site": "008c7fc8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c7f68",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008c7f8c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008c7fac",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c7f68",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008c7f8c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008c7fac",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c7f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7f2c.md#insn-008c7f58) · [`008c7f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c7/008c7f2c.md#insn-008c7f60)
- 新版 [`008c7f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md#insn-008c7f58) · [`008c7f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md#insn-008c7f60)

~~~diff
- 008c7f58 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 008c7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 008c7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 bytes 73821a91
+ 008c7f58 bytes 73821d91
- 008c7f60 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008c7f60 bytes 09cfff90
+ 008c7f60 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008c7f60 bytes 09cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ceea095121799790ed253fbc34e469d"></a>

### [`008c8b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c8/008c8b30.md) → [`008c8b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8b30.md) FUN_008c8b30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c8580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c8/008c8580.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008c8580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8580.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c8b9c",
      "incomplete_value": false,
      "site": "008c8ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c8b9c",
      "incomplete_value": false,
      "site": "008c8ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8d0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8d10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c8ba0",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008c8cfc",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008c8d00",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008c8ba0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008c8cfc",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "008c8d00",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c8d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c8/008c8b30.md#insn-008c8d0c) · [`008c8d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c8/008c8b30.md#insn-008c8d10)
- 新版 [`008c8d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8b30.md#insn-008c8d0c)

~~~diff
- 008c8d0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008c8d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008c8d0c bytes e80f00f9
+ 008c8d0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 008c8d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008c8d0c bytes e80f00f9
- 008c8d10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 008c8d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008c8d10 bytes e93300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619ecd89e12df6d3b50f3feba17309eb"></a>

### [`008c9490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c9/008c9490.md) → [`008c9490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md) FUN_008c9490

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044b8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8b0.md)
- 新版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c9624",
      "incomplete_value": false,
      "site": "008c9624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c9624",
      "incomplete_value": false,
      "site": "008c9624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c96a4",
      "incomplete_value": false,
      "site": "008c96a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c96a4",
      "incomplete_value": false,
      "site": "008c96a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c9eb0",
      "incomplete_value": false,
      "site": "008c9eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c9eb0",
      "incomplete_value": false,
      "site": "008c9eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c9624",
      "DATA",
      [
        "storage",
        "00c07858",
        null,
        "undefined *"
      ]
    ],
    [
      "008c96a4",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ],
    [
      "008c9844",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c9624",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ],
    [
      "008c96a4",
      "DATA",
      [
        "storage",
        "00c07a08",
        null,
        "undefined *"
      ]
    ],
    [
      "008c9844",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c9620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c9/008c9490.md#insn-008c9620) · [`008c96a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c9/008c9490.md#insn-008c96a0) · [`008c9844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c9/008c9490.md#insn-008c9844)
- 新版 [`008c9620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c9620) · [`008c96a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c96a0) · [`008c9844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c9844)

~~~diff
- 008c9620 ["COPY", "tmp:0:8", ["const:858:8"]]
- 008c9620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c9620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c9620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 008c9620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c9620 bytes 08612191
+ 008c9620 bytes 08212491
- 008c96a0 ["COPY", "tmp:0:8", ["const:958:8"]]
- 008c96a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 008c96a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 bytes 08612591
+ 008c96a0 bytes 08212891
- 008c9844 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008c9844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c9844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c9844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008c9844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c9844 bytes 21603691
+ 008c9844 bytes 21203991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba26c2eae3e8a76c6e6ba114a711788"></a>

### [`008ca5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca5c0.md) → [`008ca5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md) FUN_008ca5c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cafd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cafd4.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`0044626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/0044626c.md) [`00448e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044beb4.md)
- 新版 呼出元 1件 [`008cafd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`0044626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/0044626c.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ca608",
      "incomplete_value": true,
      "site": "008ca614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ca608",
      "incomplete_value": true,
      "site": "008ca614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:830:8"
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
    "new": {
      "definition_site": "008ca698",
      "incomplete_value": false,
      "site": "008ca6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ca698",
      "incomplete_value": false,
      "site": "008ca6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ca5f4",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008ca600",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ca608",
      "PARAM",
      [
        "storage",
        "00c07830",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008ca5f4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008ca600",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ca608",
      "PARAM",
      [
        "storage",
        "00c078e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ca5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca5c0.md#insn-008ca5f4) · [`008ca600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca5c0.md#insn-008ca600) · [`008ca608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca5c0.md#insn-008ca608)
- 新版 [`008ca5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca5f4) · [`008ca600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca600) · [`008ca608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca608)

~~~diff
- 008ca5f4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 008ca5f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008ca5f4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 008ca5f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008ca5f4 bytes c8de44f9
+ 008ca5f4 bytes c83e45f9
- 008ca600 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008ca600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ca600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ca600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008ca600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ca600 bytes 21603691
+ 008ca600 bytes 21203991
- 008ca608 ["COPY", "tmp:0:8", ["const:830:8"]]
- 008ca608 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008ca608 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008ca608 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 008ca608 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008ca608 bytes 42c02091
+ 008ca608 bytes 42802391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78239341358c3532a1cb93edb609c8f2"></a>

### [`008ca974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md) → [`008ca974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md) FUN_008ca974

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 19件 [`0059d12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d12c.md) [`00646dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00646/00646dc4.md) [`008381ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/008381ac.md) [`008c8580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c8/008c8580.md) [`008cb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb860.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 19件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`008381ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/008381ac.md) [`008c8580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8580.md) [`008cb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008caae8",
      "incomplete_value": false,
      "site": "008caae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008caae8",
      "incomplete_value": false,
      "site": "008caae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008caae0",
      "incomplete_value": true,
      "site": "008caae8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008caae0",
      "incomplete_value": true,
      "site": "008caae8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008caaec",
      "incomplete_value": false,
      "site": "008caaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008caaec",
      "incomplete_value": false,
      "site": "008caaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008caae0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae4",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae8",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008caae0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae4",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae8",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008caae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md#insn-008caae8) · [`008caaec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md#insn-008caaec) · [`008cab04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md#insn-008cab04)
- 新版 [`008caae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008caae8) · [`008caaec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008caaec) · [`008cab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008cab04)

~~~diff
- 008caae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008caae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008caae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008caae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008caae8 bytes 09d504f9
+ 008caae8 bytes 093505f9
- 008caaec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 008caaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008caaec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 008caaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008caaec bytes cade04f9
+ 008caaec bytes ca3e05f9
- 008cab04 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 008cab04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008cab04 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 008cab04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008cab04 bytes d4de04f9
+ 008cab04 bytes d43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a3f0a3e45aad4989f3011afef8e3303"></a>

### [`008cacc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md) → [`008cacc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md) FUN_008cacc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00429ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ff4.md) [`0042a200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a200.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00429ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ff4.md) [`0042a200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a200.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.13% / 新版 96.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cadb0",
      "incomplete_value": true,
      "site": "008cadb0",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cadb0",
      "incomplete_value": true,
      "site": "008cadb0",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cae74",
      "incomplete_value": true,
      "site": "008cae74",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cae74",
      "incomplete_value": true,
      "site": "008cae74",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cada0",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ],
    [
      "008cae64",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008cada0",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ],
    [
      "008cae64",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cad98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md#insn-008cad98) · [`008cae5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md#insn-008cae5c)
- 新版 [`008cad98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md#insn-008cad98) · [`008cae5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md#insn-008cae5c)

~~~diff
- 008cad98 ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 008cad98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cad98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cad98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cad98 ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 008cad98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cad98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cad98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cad98 bytes 29851291
+ 008cad98 bytes 299d1291
- 008cae5c ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 008cae5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cae5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cae5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cae5c ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 008cae5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cae5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cae5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cae5c bytes 29851291
+ 008cae5c bytes 299d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b4a2df27b484ab26cb19357665f749"></a>

### [`008cafd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cafd4.md) → [`008cafd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md) FUN_008cafd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008caff4",
      "incomplete_value": true,
      "site": "008caff4",
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
      "definition_site": "008caff4",
      "incomplete_value": true,
      "site": "008caff4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008cb004",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb004",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008cb00c",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb00c",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008caff0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb004",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008cb00c",
      "PARAM",
      [
        "storage",
        "00c07830",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008caff0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb004",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008cb00c",
      "PARAM",
      [
        "storage",
        "00c078e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008caff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cafd4.md#insn-008caff0) · [`008cb004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cafd4.md#insn-008cb004) · [`008cb00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cafd4.md#insn-008cb00c)
- 新版 [`008caff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008caff0) · [`008cb004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008cb004) · [`008cb00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008cb00c)

~~~diff
- 008caff0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008caff0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008caff0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008caff0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008caff0 bytes 08dd44f9
+ 008caff0 bytes 083d45f9
- 008cb004 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008cb004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008cb004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008cb004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008cb004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008cb004 bytes 21603691
+ 008cb004 bytes 21203991
- 008cb00c ["COPY", "tmp:0:8", ["const:830:8"]]
- 008cb00c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008cb00c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008cb00c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 008cb00c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008cb00c bytes 42c02091
+ 008cb00c bytes 42802391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1763edca180aff53010389dab7751f"></a>

### [`008cb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb190.md) → [`008cb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb190.md) FUN_008cb190

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb1b4",
      "incomplete_value": false,
      "site": "008cb1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb1b4",
      "incomplete_value": false,
      "site": "008cb1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "008cb1b4",
      "DATA",
      [
        "storage",
        "00c07858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb1b4",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb190.md#insn-008cb1b0)
- 新版 [`008cb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb190.md#insn-008cb1b0)

~~~diff
- 008cb1b0 ["COPY", "tmp:0:8", ["const:858:8"]]
- 008cb1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 008cb1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 bytes 08612191
+ 008cb1b0 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-392211568ee6f8359951d90b4fa12ec9"></a>

### [`008cb1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb1c4.md) → [`008cb1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb1c4.md) FUN_008cb1c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb1d0",
      "incomplete_value": false,
      "site": "008cb1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb1d0",
      "incomplete_value": false,
      "site": "008cb1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "008cb1d0",
      "DATA",
      [
        "storage",
        "00c07858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb1d0",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb1cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb1c4.md#insn-008cb1cc)
- 新版 [`008cb1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb1c4.md#insn-008cb1cc)

~~~diff
- 008cb1cc ["COPY", "tmp:0:8", ["const:858:8"]]
- 008cb1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["COPY", "tmp:0:8", ["const:908:8"]]
+ 008cb1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc bytes 29612191
+ 008cb1cc bytes 29212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b73cad793ecbfed8df2027297c4d60d2"></a>

### [`008cb258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb258.md) → [`008cb258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb258.md) FUN_008cb258

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d12c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb274",
      "incomplete_value": false,
      "site": "008cb274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb274",
      "incomplete_value": false,
      "site": "008cb274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "008cb274",
      "DATA",
      [
        "storage",
        "00c078d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb274",
      "DATA",
      [
        "storage",
        "00c07988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb258.md#insn-008cb26c)
- 新版 [`008cb26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb258.md#insn-008cb26c)

~~~diff
- 008cb26c ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 008cb26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["COPY", "tmp:0:8", ["const:988:8"]]
+ 008cb26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb26c bytes 08612391
+ 008cb26c bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79fbccca4afac821bc83e776f13cf11b"></a>

### [`008cb2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb2ac.md) → [`008cb2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb2ac.md) FUN_008cb2ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d12c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb2c8",
      "incomplete_value": false,
      "site": "008cb2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb2c8",
      "incomplete_value": false,
      "site": "008cb2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "008cb2c8",
      "DATA",
      [
        "storage",
        "00c078d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb2c8",
      "DATA",
      [
        "storage",
        "00c07988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb2ac.md#insn-008cb2c0)
- 新版 [`008cb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb2ac.md#insn-008cb2c0)

~~~diff
- 008cb2c0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 008cb2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb2c0 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 008cb2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb2c0 bytes 08612391
+ 008cb2c0 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77901ef8b53186db51873212aa0cce46"></a>

### [`008cb2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb2fc.md) → [`008cb2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb2fc.md) FUN_008cb2fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`008cb610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb610.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008cb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb610.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb320",
      "incomplete_value": false,
      "site": "008cb320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb320",
      "incomplete_value": false,
      "site": "008cb320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "008cb320",
      "DATA",
      [
        "storage",
        "00c078d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb320",
      "DATA",
      [
        "storage",
        "00c07988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb2fc.md#insn-008cb31c)
- 新版 [`008cb31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb2fc.md#insn-008cb31c)

~~~diff
- 008cb31c ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 008cb31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb31c ["COPY", "tmp:0:8", ["const:988:8"]]
+ 008cb31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb31c bytes 08612391
+ 008cb31c bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d823dd2a9c90f3b46b80596698b40aec"></a>

### [`008cb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb350.md) → [`008cb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb350.md) FUN_008cb350

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`008cb610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb610.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008cb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb610.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb35c",
      "incomplete_value": false,
      "site": "008cb35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb35c",
      "incomplete_value": false,
      "site": "008cb35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "008cb35c",
      "DATA",
      [
        "storage",
        "00c078d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb35c",
      "DATA",
      [
        "storage",
        "00c07988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb350.md#insn-008cb358)
- 新版 [`008cb358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb350.md#insn-008cb358)

~~~diff
- 008cb358 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 008cb358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cb358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cb358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cb358 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 008cb358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cb358 bytes 29612391
+ 008cb358 bytes 29212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33e38c2f0352f8f6e7a33bcdee94ade4"></a>

### [`008cb708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb708.md) → [`008cb708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb708.md) FUN_008cb708

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb72c",
      "incomplete_value": true,
      "site": "008cb72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb72c",
      "incomplete_value": true,
      "site": "008cb72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "008cb72c",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb72c",
      "DATA",
      [
        "storage",
        "00c07a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb708.md#insn-008cb728)
- 新版 [`008cb728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb708.md#insn-008cb728)

~~~diff
- 008cb728 ["COPY", "tmp:0:8", ["const:958:8"]]
- 008cb728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb728 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 008cb728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb728 bytes 08612591
+ 008cb728 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d89f944a984a7b63bf321566b79aa0"></a>

### [`008cb73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb73c.md) → [`008cb73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb73c.md) FUN_008cb73c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb748",
      "incomplete_value": true,
      "site": "008cb748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb748",
      "incomplete_value": true,
      "site": "008cb748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "008cb748",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb748",
      "DATA",
      [
        "storage",
        "00c07a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb73c.md#insn-008cb744)
- 新版 [`008cb744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb73c.md#insn-008cb744)

~~~diff
- 008cb744 ["COPY", "tmp:0:8", ["const:958:8"]]
- 008cb744 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cb744 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cb744 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cb744 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 008cb744 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb744 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb744 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cb744 bytes 29612591
+ 008cb744 bytes 29212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc34ab966d2f256b8ce63972f1e19bb8"></a>

### [`008cb758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb758.md) → [`008cb758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb758.md) FUN_008cb758

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0072c090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829bb8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829bb8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.27% / 新版 86.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008cb784",
      "incomplete_value": false,
      "site": "008cb784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb784",
      "incomplete_value": false,
      "site": "008cb784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb778",
      "incomplete_value": true,
      "site": "008cb784",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb778",
      "incomplete_value": true,
      "site": "008cb784",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008cb788",
      "incomplete_value": false,
      "site": "008cb788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb788",
      "incomplete_value": false,
      "site": "008cb788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cb778",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb77c",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb784",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008cb778",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb77c",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb784",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb758.md#insn-008cb784) · [`008cb788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb758.md#insn-008cb788) · [`008cb7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb758.md#insn-008cb7a0)
- 新版 [`008cb784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb758.md#insn-008cb784) · [`008cb788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb758.md#insn-008cb788) · [`008cb7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb758.md#insn-008cb7a0)

~~~diff
- 008cb784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008cb784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008cb784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008cb784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008cb784 bytes 09d504f9
+ 008cb784 bytes 093505f9
- 008cb788 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 008cb788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008cb788 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 008cb788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008cb788 bytes aade04f9
+ 008cb788 bytes aa3e05f9
- 008cb7a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 008cb7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 008cb7a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 008cb7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008cb7a0 bytes b3de04f9
+ 008cb7a0 bytes b33e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864c02770e88e34d81cc3fe5dd62b045"></a>

### [`008cb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb860.md) → [`008cb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md) FUN_008cb860

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ca974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md) · 呼出先 29件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044b8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8ec.md)
- 新版 呼出元 1件 [`008ca974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md) · 呼出先 29件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.07% / 新版 92.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `store_destination` 7件, `store_value` 24件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb8a0",
      "incomplete_value": false,
      "site": "008cb8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb8a0",
      "incomplete_value": false,
      "site": "008cb8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "008cb914",
      "incomplete_value": true,
      "site": "008cb914",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:895:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb914",
      "incomplete_value": true,
      "site": "008cb914",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:89c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb92c",
      "incomplete_value": true,
      "site": "008cb92c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb92c",
      "incomplete_value": true,
      "site": "008cb92c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:772:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cb8a4",
      "DATA",
      [
        "storage",
        "00c079d8",
        null,
        "pointer"
      ]
    ],
    [
      "008cb8e4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008cb904",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008cb8a4",
      "DATA",
      [
        "storage",
        "00c07a88",
        null,
        "pointer"
      ]
    ],
    [
      "008cb8e4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008cb904",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb860.md#insn-008cb8a0) · [`008cb8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb860.md#insn-008cb8d8) · [`008cb8dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cb/008cb860.md#insn-008cb8dc)
- 新版 [`008cb8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md#insn-008cb8a0) · [`008cb8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md#insn-008cb8d8) · [`008cb8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md#insn-008cb8dc)

~~~diff
- 008cb8a0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 008cb8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb8a0 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 008cb8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb8a0 bytes 08612791
+ 008cb8a0 bytes 08212a91
- 008cb8d8 ["COPY", "register:40b8:8", ["const:c24000:8"]]
+ 008cb8d8 ["COPY", "register:40b8:8", ["const:c25000:8"]]
- 008cb8d8 bytes d71a00b0
+ 008cb8d8 bytes d71a00d0
- 008cb8dc ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008cb8dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008cb8dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008cb8dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008cb8dc ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008cb8dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008cb8dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008cb8dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008cb8dc bytes f7e23d91
+ 008cb8dc bytes f7e20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280c6837111ba30f19e58e2686d984b8"></a>

### [`008cd120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd120.md) → [`008cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd120.md) FUN_008cd120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008cd248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd248.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`008cd248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd248.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd13c",
      "incomplete_value": false,
      "site": "008cd140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd13c",
      "incomplete_value": false,
      "site": "008cd140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd200",
      "incomplete_value": false,
      "site": "008cd204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd200",
      "incomplete_value": false,
      "site": "008cd204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cd140",
      "DATA",
      [
        "storage",
        "00c079d8",
        null,
        "pointer"
      ]
    ],
    [
      "008cd204",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cd140",
      "DATA",
      [
        "storage",
        "00c07a88",
        null,
        "pointer"
      ]
    ],
    [
      "008cd204",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd120.md#insn-008cd13c) · [`008cd200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd120.md#insn-008cd200)
- 新版 [`008cd13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd120.md#insn-008cd13c) · [`008cd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd120.md#insn-008cd200)

~~~diff
- 008cd13c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 008cd13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd13c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 008cd13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd13c bytes 08612791
+ 008cd13c bytes 08212a91
- 008cd200 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008cd200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd200 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008cd200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd200 bytes 08a10791
+ 008cd200 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9694c3db281e62340548e91effd83c03"></a>

### [`008cd494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd494.md) → [`008cd494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd494.md) FUN_008cd494

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd4a8",
      "incomplete_value": false,
      "site": "008cd4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd4a8",
      "incomplete_value": false,
      "site": "008cd4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "008cd4ac",
      "DATA",
      [
        "storage",
        "00c079f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd4ac",
      "DATA",
      [
        "storage",
        "00c07aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd494.md#insn-008cd4a8)
- 新版 [`008cd4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd494.md#insn-008cd4a8)

~~~diff
- 008cd4a8 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 008cd4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd4a8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 008cd4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd4a8 bytes 08e12791
+ 008cd4a8 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-889779c65e9fef880215c1a6c433fa22"></a>

### [`008cd4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd4b8.md) → [`008cd4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd4b8.md) FUN_008cd4b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd4bc",
      "incomplete_value": false,
      "site": "008cd4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd4bc",
      "incomplete_value": false,
      "site": "008cd4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "008cd4c0",
      "DATA",
      [
        "storage",
        "00c079f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd4c0",
      "DATA",
      [
        "storage",
        "00c07aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd4bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd4b8.md#insn-008cd4bc)
- 新版 [`008cd4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd4b8.md#insn-008cd4bc)

~~~diff
- 008cd4bc ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 008cd4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd4bc ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 008cd4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd4bc bytes 08e12791
+ 008cd4bc bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5561ae97df9e6ec41088d6377544a1ec"></a>

### [`008cd520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd520.md) → [`008cd520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd520.md) FUN_008cd520

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd544",
      "incomplete_value": false,
      "site": "008cd544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd544",
      "incomplete_value": false,
      "site": "008cd544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "008cd544",
      "DATA",
      [
        "storage",
        "00c07a78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd544",
      "DATA",
      [
        "storage",
        "00c07b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd520.md#insn-008cd540)
- 新版 [`008cd540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd520.md#insn-008cd540)

~~~diff
- 008cd540 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 008cd540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd540 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 008cd540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd540 bytes 08e12991
+ 008cd540 bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c56ef84866333efcc3bc896b3385b55"></a>

### [`008cd554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd554.md) → [`008cd554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd554.md) FUN_008cd554

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd560",
      "incomplete_value": false,
      "site": "008cd560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd560",
      "incomplete_value": false,
      "site": "008cd560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "008cd560",
      "DATA",
      [
        "storage",
        "00c07a78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd560",
      "DATA",
      [
        "storage",
        "00c07b28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd554.md#insn-008cd55c)
- 新版 [`008cd55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd554.md#insn-008cd55c)

~~~diff
- 008cd55c ["COPY", "tmp:0:8", ["const:a78:8"]]
- 008cd55c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cd55c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cd55c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cd55c ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 008cd55c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cd55c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cd55c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cd55c bytes 29e12991
+ 008cd55c bytes 29a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aa1144fb3ae51f9de5c5dffecbbadb2"></a>

### [`008cd570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd570.md) → [`008cd570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd570.md) FUN_008cd570

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`008cd6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6d8.md) [`008cd6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6dc.md) [`00a6b3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b3c0.md) [`00a6ca00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6c/00a6ca00.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008cd6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6d8.md) [`008cd6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6dc.md) [`00a6b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b3c0.md) [`00a6ca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ca00.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd5b0",
      "incomplete_value": false,
      "site": "008cd5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd5b0",
      "incomplete_value": false,
      "site": "008cd5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "008cd5b0",
      "DATA",
      [
        "storage",
        "00c07ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "008cd5e8",
      "READ",
      [
        "storage",
        "00c07b08",
        null,
        "pointer"
      ]
    ],
    [
      "008cd5e8",
      "READ",
      [
        "storage",
        "00c07b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd5b0",
      "DATA",
      [
        "storage",
        "00c07b98",
        null,
        "undefined *"
      ]
    ],
    [
      "008cd5e8",
      "READ",
      [
        "storage",
        "00c07bb8",
        null,
        "pointer"
      ]
    ],
    [
      "008cd5e8",
      "READ",
      [
        "storage",
        "00c07bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd570.md#insn-008cd5a8)
- 新版 [`008cd5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd570.md#insn-008cd5a8)

~~~diff
- 008cd5a8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 008cd5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd5a8 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 008cd5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd5a8 bytes 08a12b91
+ 008cd5a8 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f6fc8384a7cc0c6c4b7179b0c7c57b"></a>

### [`008cd690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd690.md) → [`008cd690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd690.md) FUN_008cd690

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd6b4",
      "incomplete_value": false,
      "site": "008cd6b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd6b4",
      "incomplete_value": false,
      "site": "008cd6b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "008cd6b4",
      "DATA",
      [
        "storage",
        "00c07ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd6b4",
      "DATA",
      [
        "storage",
        "00c07b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd690.md#insn-008cd6b0)
- 新版 [`008cd6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd690.md#insn-008cd6b0)

~~~diff
- 008cd6b0 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 008cd6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cd6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cd6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cd6b0 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 008cd6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cd6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cd6b0 bytes 08a12b91
+ 008cd6b0 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63301c9a7fc648f90b56c68a871b076e"></a>

### [`008cd6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6c4.md) → [`008cd6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6c4.md) FUN_008cd6c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd6d0",
      "incomplete_value": false,
      "site": "008cd6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd6d0",
      "incomplete_value": false,
      "site": "008cd6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "008cd6d0",
      "DATA",
      [
        "storage",
        "00c07ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd6d0",
      "DATA",
      [
        "storage",
        "00c07b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6c4.md#insn-008cd6cc)
- 新版 [`008cd6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6c4.md#insn-008cd6cc)

~~~diff
- 008cd6cc ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 008cd6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cd6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cd6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cd6cc ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 008cd6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cd6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cd6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cd6cc bytes 29a12b91
+ 008cd6cc bytes 29612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8071c52e151a04a4a88ddb5fdc4e8ca"></a>

### [`008cd6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6e0.md) → [`008cd6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6e0.md) FUN_008cd6e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0072c090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829bb8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829bb8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.78% / 新版 84.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008cd714",
      "incomplete_value": false,
      "site": "008cd714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd714",
      "incomplete_value": false,
      "site": "008cd714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd708",
      "incomplete_value": true,
      "site": "008cd714",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd708",
      "incomplete_value": true,
      "site": "008cd714",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008cd718",
      "incomplete_value": false,
      "site": "008cd718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd718",
      "incomplete_value": false,
      "site": "008cd718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cd708",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cd70c",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cd714",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008cd708",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008cd70c",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008cd714",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6e0.md#insn-008cd714) · [`008cd718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6e0.md#insn-008cd718) · [`008cd740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd6e0.md#insn-008cd740)
- 新版 [`008cd714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6e0.md#insn-008cd714) · [`008cd718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6e0.md#insn-008cd718) · [`008cd740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd6e0.md#insn-008cd740)

~~~diff
- 008cd714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008cd714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008cd714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008cd714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008cd714 bytes 09d504f9
+ 008cd714 bytes 093505f9
- 008cd718 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 008cd718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008cd718 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 008cd718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008cd718 bytes cade04f9
+ 008cd718 bytes ca3e05f9
- 008cd740 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 008cd740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008cd740 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 008cd740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008cd740 bytes d4de04f9
+ 008cd740 bytes d43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56663cca15b959a5ba855e672a786e85"></a>

### [`008cd7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd7d4.md) → [`008cd7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd7d4.md) _INIT_172

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd810",
      "incomplete_value": true,
      "site": "008cd82c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd810",
      "incomplete_value": true,
      "site": "008cd82c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cd834",
      "incomplete_value": true,
      "site": "008cd850",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd834",
      "incomplete_value": true,
      "site": "008cd850",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008cd854",
      "incomplete_value": true,
      "site": "008cd870",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cd854",
      "incomplete_value": true,
      "site": "008cd870",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cd810",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008cd834",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008cd854",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008cd810",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008cd834",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008cd854",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd7d4.md#insn-008cd800) · [`008cd808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cd7d4.md#insn-008cd808)
- 新版 [`008cd800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd7d4.md#insn-008cd800) · [`008cd808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cd7d4.md#insn-008cd808)

~~~diff
- 008cd800 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 008cd800 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008cd800 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008cd800 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008cd800 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 008cd800 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008cd800 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008cd800 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008cd800 bytes 73e21a91
+ 008cd800 bytes 73e21d91
- 008cd808 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008cd808 bytes c9ceffd0
+ 008cd808 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008cd808 bytes c9ceffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d061bedd83153d83a94b22c272bd3fd"></a>

### [`008cdb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cdb64.md) → [`008cdb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cdb64.md) FUN_008cdb64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`009eadc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009ea/009eadc8.md) · 呼出先 17件 [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md) [`00574054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574054.md) [`00574730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574730.md)
- 新版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`009eadc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ea/009eadc8.md) · 呼出先 17件 [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00574730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574730.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.57% / 新版 92.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cdba4",
      "incomplete_value": false,
      "site": "008cdbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cdba4",
      "incomplete_value": false,
      "site": "008cdbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cdd14",
      "incomplete_value": true,
      "site": "008cdd18",
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
      "definition_site": "008cdd14",
      "incomplete_value": true,
      "site": "008cdd18",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cdd10",
      "incomplete_value": true,
      "site": "008cdd1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cdd10",
      "incomplete_value": true,
      "site": "008cdd1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cdbb0",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008cdd04",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "008cdd08",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cdbb0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008cdd04",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "008cdd08",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cdba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cdb64.md#insn-008cdba4) · [`008cdd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cdb64.md#insn-008cdd04) · [`008cdd08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cdb64.md#insn-008cdd08)
- 新版 [`008cdba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cdb64.md#insn-008cdba4) · [`008cdd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cdb64.md#insn-008cdd04) · [`008cdd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cdb64.md#insn-008cdd08)

~~~diff
- 008cdba4 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008cdba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cdba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cdba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cdba4 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008cdba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cdba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cdba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cdba4 bytes 08e13191
+ 008cdba4 bytes 08a13491
- 008cdd04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 008cdd04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008cdd04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 008cdd04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008cdd04 bytes 086146f9
+ 008cdd04 bytes 08b946f9
- 008cdd08 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc8:8"]]
- 008cdd08 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 008cdd08 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 008cdd08 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 008cdd08 bytes d66646f9
+ 008cdd08 bytes d6be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60a78190fc5175c7f32adaed233714f9"></a>

### [`008cde24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cde24.md) → [`008cde24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cde24.md) FUN_008cde24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008cdb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cdb64.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00470c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470c48.md) [`0059d12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`008cdb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cdb64.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00470c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470c48.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.67% / 新版 99.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cefc4",
      "incomplete_value": true,
      "site": "008cefc4",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:f6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cefc4",
      "incomplete_value": true,
      "site": "008cefc4",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 176,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ce51c",
      "READ",
      [
        "storage",
        "002a5d79",
        null,
        "string"
      ]
    ],
    [
      "008cefb0",
      "READ",
      [
        "storage",
        "00295069",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ce51c",
      "READ",
      [
        "storage",
        "002a5d72",
        null,
        "string"
      ]
    ],
    [
      "008cefb0",
      "READ",
      [
        "storage",
        "002950f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ce518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cde24.md#insn-008ce518) · [`008cefa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cde24.md#insn-008cefa8)
- 新版 [`008ce518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cde24.md#insn-008ce518) · [`008cefa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cde24.md#insn-008cefa8)

~~~diff
- 008ce518 ["COPY", "tmp:0:8", ["const:d79:8"]]
- 008ce518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ce518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ce518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ce518 ["COPY", "tmp:0:8", ["const:d72:8"]]
+ 008ce518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ce518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ce518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ce518 bytes 08e53591
+ 008ce518 bytes 08c93591
- 008cefa8 ["COPY", "tmp:0:8", ["const:69:8"]]
- 008cefa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cefa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cefa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cefa8 ["COPY", "tmp:0:8", ["const:f6:8"]]
+ 008cefa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cefa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cefa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cefa8 bytes 29a50191
+ 008cefa8 bytes 29d90391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48559012d123fc5a7368d63ef6e2b872"></a>

### [`008cf74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf74c.md) → [`008cf74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf74c.md) FUN_008cf74c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cf728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf728.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008cf728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf728.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.08% / 新版 91.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf784",
      "incomplete_value": false,
      "site": "008cf788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf784",
      "incomplete_value": false,
      "site": "008cf788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf7a0",
      "incomplete_value": true,
      "site": "008cf7b8",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:c74:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf7a0",
      "incomplete_value": true,
      "site": "008cf7b8",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:c7d:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008cf920",
      "incomplete_value": true,
      "site": "008cf924",
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
      "definition_site": "008cf920",
      "incomplete_value": true,
      "site": "008cf924",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf788",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008cf7a0",
      "READ",
      [
        "storage",
        "002a9c7d",
        null,
        "string"
      ]
    ],
    [
      "008cf910",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cf788",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008cf7a0",
      "READ",
      [
        "storage",
        "002a9c74",
        null,
        "string"
      ]
    ],
    [
      "008cf910",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf74c.md#insn-008cf784) · [`008cf798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf74c.md#insn-008cf798) · [`008cf910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf74c.md#insn-008cf910)
- 新版 [`008cf784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf74c.md#insn-008cf784) · [`008cf798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf74c.md#insn-008cf798) · [`008cf910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf74c.md#insn-008cf910)

~~~diff
- 008cf784 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008cf784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf784 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008cf784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf784 bytes 08e13191
+ 008cf784 bytes 08a13491
- 008cf798 ["COPY", "tmp:0:8", ["const:c7d:8"]]
- 008cf798 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cf798 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cf798 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cf798 ["COPY", "tmp:0:8", ["const:c74:8"]]
+ 008cf798 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cf798 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cf798 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cf798 bytes 29f53191
+ 008cf798 bytes 29d13191
- 008cf910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 008cf910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008cf910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 008cf910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008cf910 bytes 086146f9
+ 008cf910 bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-998e0e9b5a5f3f9cc4e58b5f8938c2f7"></a>

### [`008cfa1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cfa1c.md) → [`008cfa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfa1c.md) FUN_008cfa1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cf728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cf728.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008cf728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cf728.md) · 呼出先 12件 [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.14% / 新版 91.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfa54",
      "incomplete_value": false,
      "site": "008cfa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfa54",
      "incomplete_value": false,
      "site": "008cfa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfa74",
      "incomplete_value": true,
      "site": "008cfa8c",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:ae4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfa74",
      "incomplete_value": true,
      "site": "008cfa8c",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:a57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfbf4",
      "incomplete_value": true,
      "site": "008cfbf8",
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
      "definition_site": "008cfbf4",
      "incomplete_value": true,
      "site": "008cfbf8",
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
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cfa5c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008cfa74",
      "READ",
      [
        "storage",
        "0029ca57",
        null,
        "string"
      ]
    ],
    [
      "008cfbe4",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cfa5c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008cfa74",
      "READ",
      [
        "storage",
        "0029cae4",
        null,
        "string"
      ]
    ],
    [
      "008cfbe4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cfa1c.md#insn-008cfa54) · [`008cfa6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cfa1c.md#insn-008cfa6c) · [`008cfbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cf/008cfa1c.md#insn-008cfbe4)
- 新版 [`008cfa54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfa1c.md#insn-008cfa54) · [`008cfa6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfa1c.md#insn-008cfa6c) · [`008cfbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfa1c.md#insn-008cfbe4)

~~~diff
- 008cfa54 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008cfa54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cfa54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cfa54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cfa54 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008cfa54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfa54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfa54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cfa54 bytes 08e13191
+ 008cfa54 bytes 08a13491
- 008cfa6c ["COPY", "tmp:0:8", ["const:a57:8"]]
- 008cfa6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cfa6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cfa6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cfa6c ["COPY", "tmp:0:8", ["const:ae4:8"]]
+ 008cfa6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfa6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfa6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cfa6c bytes 295d2991
+ 008cfa6c bytes 29912b91
- 008cfbe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 008cfbe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008cfbe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 008cfbe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008cfbe4 bytes 086146f9
+ 008cfbe4 bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767076a0db2f920ee2a5240ee632cdcf"></a>

### [`008d008c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d008c.md) → [`008d008c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d008c.md) FUN_008d008c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cde24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008cd/008cde24.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008cde24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cd/008cde24.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d0098",
      "incomplete_value": false,
      "site": "008d009c",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0098",
      "incomplete_value": false,
      "site": "008d009c",
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
            "const:30a:8"
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
      "008d0098",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d0098",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d008c.md#insn-008d0098)
- 新版 [`008d0098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d008c.md#insn-008d0098)

~~~diff
- 008d0098 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008d0098 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d0098 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d0098 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d0098 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008d0098 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d0098 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d0098 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d0098 bytes 00280c91
+ 008d0098 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32524e8fb684483cb0643e8ed53a8560"></a>

### [`008d0224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0224.md) → [`008d0224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0224.md) FUN_008d0224

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008d00a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d00a0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008d00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d00a0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d0230",
      "incomplete_value": false,
      "site": "008d0234",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0230",
      "incomplete_value": false,
      "site": "008d0234",
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
            "const:30a:8"
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
      "008d0230",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d0230",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0224.md#insn-008d0230)
- 新版 [`008d0230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0224.md#insn-008d0230)

~~~diff
- 008d0230 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008d0230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d0230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d0230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d0230 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008d0230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d0230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d0230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d0230 bytes 00280c91
+ 008d0230 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a002af0fc122aca698b6b3f84ce0071"></a>

### [`008d03bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d03bc.md) → [`008d03bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d03bc.md) FUN_008d03bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008d0238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0238.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008d0238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0238.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d03c8",
      "incomplete_value": false,
      "site": "008d03cc",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d03c8",
      "incomplete_value": false,
      "site": "008d03cc",
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
            "const:30a:8"
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
      "008d03c8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d03c8",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d03c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d03bc.md#insn-008d03c8)
- 新版 [`008d03c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d03bc.md#insn-008d03c8)

~~~diff
- 008d03c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008d03c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d03c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d03c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d03c8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008d03c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d03c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d03c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d03c8 bytes 00280c91
+ 008d03c8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f2376ad93ad7778f6f001576c71589"></a>

### [`008d03d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d03d0.md) → [`008d03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d03d0.md) _INIT_173

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d040c",
      "incomplete_value": true,
      "site": "008d0428",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d040c",
      "incomplete_value": true,
      "site": "008d0428",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0430",
      "incomplete_value": true,
      "site": "008d044c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0430",
      "incomplete_value": true,
      "site": "008d044c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008d0450",
      "incomplete_value": true,
      "site": "008d046c",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0450",
      "incomplete_value": true,
      "site": "008d046c",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d040c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008d0430",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008d0450",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d040c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008d0430",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008d0450",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d03fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d03d0.md#insn-008d03fc) · [`008d0404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d03d0.md#insn-008d0404)
- 新版 [`008d03fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d03d0.md#insn-008d03fc) · [`008d0404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d03d0.md#insn-008d0404)

~~~diff
- 008d03fc ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 008d03fc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008d03fc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008d03fc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008d03fc ["COPY", "tmp:0:8", ["const:790:8"]]
+ 008d03fc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008d03fc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008d03fc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008d03fc bytes 73421b91
+ 008d03fc bytes 73421e91
- 008d0404 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008d0404 bytes a9cefff0
+ 008d0404 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008d0404 bytes a9cefff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f673005bf9ce52ef6baa087679b3e96a"></a>

### [`008d0760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md) → [`008d0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md) FUN_008d0760

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008dd98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd98c.md) [`00a1e428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a1e/00a1e428.md) · 呼出先 48件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md)
- 新版 呼出元 2件 [`008dd98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd98c.md) [`00a1e428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e428.md) · 呼出先 48件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.88% / 新版 88.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 88件, `store_destination` 77件, `store_value` 63件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d07a0",
      "incomplete_value": false,
      "site": "008d07a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d07a0",
      "incomplete_value": false,
      "site": "008d07a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "definition_site": "008d090c",
      "incomplete_value": true,
      "site": "008d090c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:895:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d090c",
      "incomplete_value": true,
      "site": "008d090c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:89c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0924",
      "incomplete_value": true,
      "site": "008d0924",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0924",
      "incomplete_value": true,
      "site": "008d0924",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:772:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d07a8",
      "DATA",
      [
        "storage",
        "00c07b78",
        null,
        "pointer"
      ]
    ],
    [
      "008d08dc",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d08fc",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d07a8",
      "DATA",
      [
        "storage",
        "00c07c28",
        null,
        "pointer"
      ]
    ],
    [
      "008d08dc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d08fc",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d07a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md#insn-008d07a0) · [`008d08d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md#insn-008d08d4) · [`008d08d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md#insn-008d08d8)
- 新版 [`008d07a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md#insn-008d07a0) · [`008d08d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md#insn-008d08d4) · [`008d08d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md#insn-008d08d8)

~~~diff
- 008d07a0 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 008d07a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d07a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d07a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d07a0 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008d07a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d07a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d07a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d07a0 bytes 08e12d91
+ 008d07a0 bytes 08a13091
- 008d08d4 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 008d08d4 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 008d08d4 bytes a81a0090
+ 008d08d4 bytes a81a00b0
- 008d08d8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d08d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d08d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d08d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d08d8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d08d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d08d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d08d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d08d8 bytes 08e13d91
+ 008d08d8 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6253e4fbb2f5aeabc2ceca5d0b9acbda"></a>

### [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) → [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) FUN_008d40c0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d0760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md) [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) · 呼出先 19件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00832/00832580.md)
- 新版 呼出元 2件 [`008d0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 19件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 25件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d40fc",
      "incomplete_value": false,
      "site": "008d4100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d40fc",
      "incomplete_value": false,
      "site": "008d4100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d416c",
      "incomplete_value": true,
      "site": "008d416c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:895:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d416c",
      "incomplete_value": true,
      "site": "008d416c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:89c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d4184",
      "incomplete_value": true,
      "site": "008d4184",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d4184",
      "incomplete_value": true,
      "site": "008d4184",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:772:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d4100",
      "DATA",
      [
        "storage",
        "00c07b98",
        null,
        "pointer"
      ]
    ],
    [
      "008d413c",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d415c",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d4100",
      "DATA",
      [
        "storage",
        "00c07c48",
        null,
        "pointer"
      ]
    ],
    [
      "008d413c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d415c",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d40fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md#insn-008d40fc) · [`008d4110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md#insn-008d4110) · [`008d4114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md#insn-008d4114)
- 新版 [`008d40fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md#insn-008d40fc) · [`008d4110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md#insn-008d4110) · [`008d4114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md#insn-008d4114)

~~~diff
- 008d40fc ["COPY", "tmp:0:8", ["const:b98:8"]]
- 008d40fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d40fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d40fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d40fc ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 008d40fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d40fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d40fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d40fc bytes 08612e91
+ 008d40fc bytes 08213191
- 008d4110 ["COPY", "register:40c0:8", ["const:c24000:8"]]
+ 008d4110 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008d4110 bytes 981a0090
+ 008d4110 bytes 981a00b0
- 008d4114 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d4114 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 008d4114 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 008d4114 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 008d4114 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d4114 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 008d4114 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 008d4114 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 008d4114 bytes 18e33d91
+ 008d4114 bytes 18e30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0da0ccc431059bd59fa6592eb29e6eec"></a>

### [`008d5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md) → [`008d5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md) FUN_008d5008

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdad7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad7c.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`005b39e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b39e0.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008d5a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a80.md) [`008d5ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5ad4.md)
- 新版 呼出元 1件 [`00bdae3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae3c.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`005b39e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b39e0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008d5a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a80.md) [`008d5ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5ad4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d5034",
      "incomplete_value": true,
      "site": "008d5044",
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
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e76:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5034",
      "incomplete_value": true,
      "site": "008d5044",
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
                "const:291000:8"
              ],
              [
                "leaf",
                "const:de9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d5038",
      "incomplete_value": true,
      "site": "008d5048",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5038",
      "incomplete_value": true,
      "site": "008d5048",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d515c",
      "incomplete_value": true,
      "site": "008d5170",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:ec6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d515c",
      "incomplete_value": true,
      "site": "008d5170",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:e39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d5034",
      "READ",
      [
        "storage",
        "00291de9",
        null,
        "string"
      ]
    ],
    [
      "008d5038",
      "READ",
      [
        "storage",
        "00291df3",
        null,
        "string"
      ]
    ],
    [
      "008d515c",
      "READ",
      [
        "storage",
        "00295e39",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d5034",
      "READ",
      [
        "storage",
        "00291e76",
        null,
        "string"
      ]
    ],
    [
      "008d5038",
      "READ",
      [
        "storage",
        "00291e80",
        null,
        "string"
      ]
    ],
    [
      "008d515c",
      "READ",
      [
        "storage",
        "00295ec6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d502c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md#insn-008d502c) · [`008d5030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md#insn-008d5030)
- 新版 [`008d502c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md#insn-008d502c) · [`008d5030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md#insn-008d5030)

~~~diff
- 008d502c ["COPY", "tmp:0:8", ["const:de9:8"]]
- 008d502c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d502c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d502c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d502c ["COPY", "tmp:0:8", ["const:e76:8"]]
+ 008d502c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d502c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d502c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d502c bytes 08a53791
+ 008d502c bytes 08d93991
- 008d5030 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 008d5030 bytes e9ceff90
+ 008d5030 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 008d5030 bytes e9ceff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18ef7bcc0e2c2b2c591ca2a0d43813a7"></a>

### [`008d5738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5738.md) → [`008d5738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5738.md) FUN_008d5738

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d573c",
      "incomplete_value": false,
      "site": "008d5740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d573c",
      "incomplete_value": false,
      "site": "008d5740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d575c",
      "incomplete_value": false,
      "site": "008d5778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d575c",
      "incomplete_value": false,
      "site": "008d5778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5780",
      "incomplete_value": false,
      "site": "008d5784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5780",
      "incomplete_value": false,
      "site": "008d5784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d573c",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5754",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d575c",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d573c",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5754",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d575c",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5738.md#insn-008d5738) · [`008d573c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5738.md#insn-008d573c) · [`008d575c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5738.md#insn-008d575c)
- 新版 [`008d5738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5738.md#insn-008d5738) · [`008d573c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5738.md#insn-008d573c) · [`008d575c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5738.md#insn-008d575c)

~~~diff
- 008d5738 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5738 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5738 bytes 601a00f0
+ 008d5738 bytes 801a0090
- 008d573c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d573c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d573c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d573c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d573c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d573c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d573c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d573c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d573c bytes 00e03d91
+ 008d573c bytes 00e00091
- 008d575c ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d575c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d575c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d575c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d575c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d575c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d575c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d575c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d575c bytes 42403b91
+ 008d575c bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a57d1827ad990462f742bbc738b69a6"></a>

### [`008d578c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d578c.md) → [`008d578c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d578c.md) FUN_008d578c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5790",
      "incomplete_value": false,
      "site": "008d5794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5790",
      "incomplete_value": false,
      "site": "008d5794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d57b0",
      "incomplete_value": false,
      "site": "008d57cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d57b0",
      "incomplete_value": false,
      "site": "008d57cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d57d4",
      "incomplete_value": false,
      "site": "008d57d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d57d4",
      "incomplete_value": false,
      "site": "008d57d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5790",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d57a8",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d57b0",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d5790",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d57a8",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d57b0",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d578c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d578c.md#insn-008d578c) · [`008d5790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d578c.md#insn-008d5790) · [`008d57b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d578c.md#insn-008d57b0)
- 新版 [`008d578c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d578c.md#insn-008d578c) · [`008d5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d578c.md#insn-008d5790) · [`008d57b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d578c.md#insn-008d57b0)

~~~diff
- 008d578c ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d578c ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d578c bytes 601a00f0
+ 008d578c bytes 801a0090
- 008d5790 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5790 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5790 bytes 00e03d91
+ 008d5790 bytes 00e00091
- 008d57b0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d57b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d57b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d57b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d57b0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d57b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d57b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d57b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d57b0 bytes 42403b91
+ 008d57b0 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a60ab82423639c2cc2148b8b439ea5da"></a>

### [`008d57e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d57e0.md) → [`008d57e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d57e0.md) FUN_008d57e0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d57e4",
      "incomplete_value": false,
      "site": "008d57e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d57e4",
      "incomplete_value": false,
      "site": "008d57e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5804",
      "incomplete_value": false,
      "site": "008d5820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5804",
      "incomplete_value": false,
      "site": "008d5820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5828",
      "incomplete_value": false,
      "site": "008d582c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5828",
      "incomplete_value": false,
      "site": "008d582c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d57e4",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d57fc",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5804",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d57e4",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d57fc",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5804",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d57e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d57e0.md#insn-008d57e0) · [`008d57e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d57e0.md#insn-008d57e4) · [`008d5804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d57e0.md#insn-008d5804)
- 新版 [`008d57e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d57e0.md#insn-008d57e0) · [`008d57e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d57e0.md#insn-008d57e4) · [`008d5804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d57e0.md#insn-008d5804)

~~~diff
- 008d57e0 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d57e0 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d57e0 bytes 601a00f0
+ 008d57e0 bytes 801a0090
- 008d57e4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d57e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d57e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d57e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d57e4 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d57e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d57e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d57e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d57e4 bytes 00e03d91
+ 008d57e4 bytes 00e00091
- 008d5804 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5804 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5804 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5804 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5804 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5804 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5804 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5804 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5804 bytes 42403b91
+ 008d5804 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38a2f1f51d642a114c3ccd8ce81b542b"></a>

### [`008d5834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5834.md) → [`008d5834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5834.md) FUN_008d5834

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5838",
      "incomplete_value": false,
      "site": "008d583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5838",
      "incomplete_value": false,
      "site": "008d583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5858",
      "incomplete_value": false,
      "site": "008d5874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5858",
      "incomplete_value": false,
      "site": "008d5874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d587c",
      "incomplete_value": false,
      "site": "008d5880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d587c",
      "incomplete_value": false,
      "site": "008d5880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5838",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5850",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5858",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d5838",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5850",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5858",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5834.md#insn-008d5834) · [`008d5838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5834.md#insn-008d5838) · [`008d5858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5834.md#insn-008d5858)
- 新版 [`008d5834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5834.md#insn-008d5834) · [`008d5838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5834.md#insn-008d5838) · [`008d5858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5834.md#insn-008d5858)

~~~diff
- 008d5834 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5834 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5834 bytes 601a00f0
+ 008d5834 bytes 801a0090
- 008d5838 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5838 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5838 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5838 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5838 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5838 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5838 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5838 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5838 bytes 00e03d91
+ 008d5838 bytes 00e00091
- 008d5858 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5858 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5858 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5858 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5858 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5858 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5858 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5858 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5858 bytes 42403b91
+ 008d5858 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0487296efd507fb28be93b33ecc1a72"></a>

### [`008d5888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5888.md) → [`008d5888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5888.md) FUN_008d5888

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d588c",
      "incomplete_value": false,
      "site": "008d5890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d588c",
      "incomplete_value": false,
      "site": "008d5890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d58ac",
      "incomplete_value": false,
      "site": "008d58c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d58ac",
      "incomplete_value": false,
      "site": "008d58c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d58d0",
      "incomplete_value": false,
      "site": "008d58d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d58d0",
      "incomplete_value": false,
      "site": "008d58d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d588c",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d58a4",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d58ac",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d588c",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d58a4",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d58ac",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5888.md#insn-008d5888) · [`008d588c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5888.md#insn-008d588c) · [`008d58ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5888.md#insn-008d58ac)
- 新版 [`008d5888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5888.md#insn-008d5888) · [`008d588c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5888.md#insn-008d588c) · [`008d58ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5888.md#insn-008d58ac)

~~~diff
- 008d5888 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5888 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5888 bytes 601a00f0
+ 008d5888 bytes 801a0090
- 008d588c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d588c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d588c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d588c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d588c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d588c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d588c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d588c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d588c bytes 00e03d91
+ 008d588c bytes 00e00091
- 008d58ac ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d58ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d58ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d58ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d58ac ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d58ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d58ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d58ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d58ac bytes 42403b91
+ 008d58ac bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855b4bf929b84f0b85de60bd939a03a0"></a>

### [`008d5930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5930.md) → [`008d5930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5930.md) FUN_008d5930

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5934",
      "incomplete_value": false,
      "site": "008d5938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5934",
      "incomplete_value": false,
      "site": "008d5938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5954",
      "incomplete_value": false,
      "site": "008d5970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5954",
      "incomplete_value": false,
      "site": "008d5970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5978",
      "incomplete_value": false,
      "site": "008d597c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5978",
      "incomplete_value": false,
      "site": "008d597c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5934",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d594c",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5954",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d5934",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d594c",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5954",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5930.md#insn-008d5930) · [`008d5934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5930.md#insn-008d5934) · [`008d5954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5930.md#insn-008d5954)
- 新版 [`008d5930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5930.md#insn-008d5930) · [`008d5934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5930.md#insn-008d5934) · [`008d5954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5930.md#insn-008d5954)

~~~diff
- 008d5930 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5930 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5930 bytes 601a00f0
+ 008d5930 bytes 801a0090
- 008d5934 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5934 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5934 bytes 00e03d91
+ 008d5934 bytes 00e00091
- 008d5954 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5954 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5954 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5954 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5954 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5954 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5954 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5954 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5954 bytes 42403b91
+ 008d5954 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-128c2c75bff86b7797505d4b2756b54f"></a>

### [`008d5984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5984.md) → [`008d5984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5984.md) FUN_008d5984

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5988",
      "incomplete_value": false,
      "site": "008d598c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5988",
      "incomplete_value": false,
      "site": "008d598c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d59a8",
      "incomplete_value": false,
      "site": "008d59c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d59a8",
      "incomplete_value": false,
      "site": "008d59c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d59cc",
      "incomplete_value": false,
      "site": "008d59d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d59cc",
      "incomplete_value": false,
      "site": "008d59d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5988",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d59a0",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d59a8",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d5988",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d59a0",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d59a8",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5984.md#insn-008d5984) · [`008d5988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5984.md#insn-008d5988) · [`008d59a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5984.md#insn-008d59a8)
- 新版 [`008d5984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5984.md#insn-008d5984) · [`008d5988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5984.md#insn-008d5988) · [`008d59a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5984.md#insn-008d59a8)

~~~diff
- 008d5984 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5984 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5984 bytes 601a00f0
+ 008d5984 bytes 801a0090
- 008d5988 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5988 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5988 bytes 00e03d91
+ 008d5988 bytes 00e00091
- 008d59a8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d59a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d59a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d59a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d59a8 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d59a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d59a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d59a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d59a8 bytes 42403b91
+ 008d59a8 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca14ebedf22f32ac78d6e08f42df6ef8"></a>

### [`008d59d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d59d8.md) → [`008d59d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d59d8.md) FUN_008d59d8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d59dc",
      "incomplete_value": false,
      "site": "008d59e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d59dc",
      "incomplete_value": false,
      "site": "008d59e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d59fc",
      "incomplete_value": false,
      "site": "008d5a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d59fc",
      "incomplete_value": false,
      "site": "008d5a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5a20",
      "incomplete_value": false,
      "site": "008d5a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5a20",
      "incomplete_value": false,
      "site": "008d5a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d59dc",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d59f4",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d59fc",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d59dc",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d59f4",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d59fc",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d59d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d59d8.md#insn-008d59d8) · [`008d59dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d59d8.md#insn-008d59dc) · [`008d59fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d59d8.md#insn-008d59fc)
- 新版 [`008d59d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d59d8.md#insn-008d59d8) · [`008d59dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d59d8.md#insn-008d59dc) · [`008d59fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d59d8.md#insn-008d59fc)

~~~diff
- 008d59d8 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d59d8 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d59d8 bytes 601a00f0
+ 008d59d8 bytes 801a0090
- 008d59dc ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d59dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d59dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d59dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d59dc ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d59dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d59dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d59dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d59dc bytes 00e03d91
+ 008d59dc bytes 00e00091
- 008d59fc ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d59fc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d59fc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d59fc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d59fc ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d59fc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d59fc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d59fc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d59fc bytes 42403b91
+ 008d59fc bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb7349830dcdac0b79f43e71151456ab"></a>

### [`008d5a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a2c.md) → [`008d5a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a2c.md) FUN_008d5a2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5a30",
      "incomplete_value": false,
      "site": "008d5a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5a30",
      "incomplete_value": false,
      "site": "008d5a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5a50",
      "incomplete_value": false,
      "site": "008d5a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5a50",
      "incomplete_value": false,
      "site": "008d5a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5a74",
      "incomplete_value": false,
      "site": "008d5a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5a74",
      "incomplete_value": false,
      "site": "008d5a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5a30",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5a48",
      "WRITE",
      [
        "storage",
        "00c24f48",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5a50",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d5a30",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5a48",
      "WRITE",
      [
        "storage",
        "00c25008",
        null,
        "undefined8"
      ]
    ],
    [
      "008d5a50",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a2c.md#insn-008d5a2c) · [`008d5a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a2c.md#insn-008d5a30) · [`008d5a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a2c.md#insn-008d5a50)
- 新版 [`008d5a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a2c.md#insn-008d5a2c) · [`008d5a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a2c.md#insn-008d5a30) · [`008d5a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a2c.md#insn-008d5a50)

~~~diff
- 008d5a2c ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5a2c ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5a2c bytes 601a00f0
+ 008d5a2c bytes 801a0090
- 008d5a30 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5a30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5a30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5a30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5a30 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5a30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5a30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5a30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5a30 bytes 00e03d91
+ 008d5a30 bytes 00e00091
- 008d5a50 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5a50 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5a50 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5a50 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5a50 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5a50 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5a50 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5a50 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5a50 bytes 42403b91
+ 008d5a50 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-806dceba8cbfe4bfd866e0cf56a128d2"></a>

### [`008d5a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a80.md) → [`008d5a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a80.md) FUN_008d5a80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5a84",
      "incomplete_value": false,
      "site": "008d5a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5a84",
      "incomplete_value": false,
      "site": "008d5a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5aa4",
      "incomplete_value": false,
      "site": "008d5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5aa4",
      "incomplete_value": false,
      "site": "008d5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5ac8",
      "incomplete_value": false,
      "site": "008d5acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5ac8",
      "incomplete_value": false,
      "site": "008d5acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5a84",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5aa4",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008d5ac8",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d5a84",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5aa4",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "008d5ac8",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a80.md#insn-008d5a80) · [`008d5a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a80.md#insn-008d5a84) · [`008d5aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5a80.md#insn-008d5aa4)
- 新版 [`008d5a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a80.md#insn-008d5a80) · [`008d5a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a80.md#insn-008d5a84) · [`008d5aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5a80.md#insn-008d5aa4)

~~~diff
- 008d5a80 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5a80 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5a80 bytes 601a00f0
+ 008d5a80 bytes 801a0090
- 008d5a84 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5a84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5a84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5a84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5a84 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5a84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5a84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5a84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5a84 bytes 00e03d91
+ 008d5a84 bytes 00e00091
- 008d5aa4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5aa4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5aa4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5aa4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5aa4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5aa4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5aa4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5aa4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5aa4 bytes 42403b91
+ 008d5aa4 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f66a6b4e6abad8ac5ce61c90680d4e6"></a>

### [`008d5ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5ad4.md) → [`008d5ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5ad4.md) FUN_008d5ad4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5ad8",
      "incomplete_value": false,
      "site": "008d5adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5ad8",
      "incomplete_value": false,
      "site": "008d5adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5af8",
      "incomplete_value": false,
      "site": "008d5b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5af8",
      "incomplete_value": false,
      "site": "008d5b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5b1c",
      "incomplete_value": false,
      "site": "008d5b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5b1c",
      "incomplete_value": false,
      "site": "008d5b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5ad8",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5af8",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008d5b1c",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d5ad8",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5af8",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "008d5b1c",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5ad4.md#insn-008d5ad4) · [`008d5ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5ad4.md#insn-008d5ad8) · [`008d5af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5ad4.md#insn-008d5af8)
- 新版 [`008d5ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5ad4.md#insn-008d5ad4) · [`008d5ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5ad4.md#insn-008d5ad8) · [`008d5af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5ad4.md#insn-008d5af8)

~~~diff
- 008d5ad4 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5ad4 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5ad4 bytes 601a00f0
+ 008d5ad4 bytes 801a0090
- 008d5ad8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5ad8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5ad8 bytes 00e03d91
+ 008d5ad8 bytes 00e00091
- 008d5af8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5af8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5af8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5af8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5af8 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5af8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5af8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5af8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5af8 bytes 42403b91
+ 008d5af8 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c5e7adb514c92cba28c51090ebf313"></a>

### [`008d5b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b28.md) → [`008d5b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b28.md) FUN_008d5b28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`008d5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5b2c",
      "incomplete_value": false,
      "site": "008d5b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5b2c",
      "incomplete_value": false,
      "site": "008d5b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5b4c",
      "incomplete_value": false,
      "site": "008d5b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5b4c",
      "incomplete_value": false,
      "site": "008d5b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008d5b70",
      "incomplete_value": false,
      "site": "008d5b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5b70",
      "incomplete_value": false,
      "site": "008d5b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5b2c",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5b4c",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008d5b70",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d5b2c",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5b4c",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "008d5b70",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b28.md#insn-008d5b28) · [`008d5b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b28.md#insn-008d5b2c) · [`008d5b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b28.md#insn-008d5b4c)
- 新版 [`008d5b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b28.md#insn-008d5b28) · [`008d5b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b28.md#insn-008d5b2c) · [`008d5b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b28.md#insn-008d5b4c)

~~~diff
- 008d5b28 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5b28 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5b28 bytes 601a00f0
+ 008d5b28 bytes 801a0090
- 008d5b2c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5b2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5b2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5b2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5b2c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5b2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5b2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5b2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5b2c bytes 00e03d91
+ 008d5b2c bytes 00e00091
- 008d5b4c ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5b4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5b4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5b4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5b4c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5b4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5b4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5b4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5b4c bytes 42403b91
+ 008d5b4c bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62dcf3b068adb67d8e389ad4080b6583"></a>

### [`008d5b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b7c.md) → [`008d5b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b7c.md) FUN_008d5b7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008d5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5008.md) · 呼出先 5件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`008d5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5008.md) · 呼出先 5件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d5b80",
      "incomplete_value": false,
      "site": "008d5b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5b80",
      "incomplete_value": false,
      "site": "008d5b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "definition_site": "008d5bc4",
      "incomplete_value": false,
      "site": "008d5bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5bc4",
      "incomplete_value": false,
      "site": "008d5bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
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
      "008d5b80",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5ba0",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008d5bc4",
      "PARAM",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d5b80",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d5ba0",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "008d5bc4",
      "PARAM",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b7c.md#insn-008d5b7c) · [`008d5b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b7c.md#insn-008d5b80) · [`008d5ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5b7c.md#insn-008d5ba0)
- 新版 [`008d5b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b7c.md#insn-008d5b7c) · [`008d5b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b7c.md#insn-008d5b80) · [`008d5ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5b7c.md#insn-008d5ba0)

~~~diff
- 008d5b7c ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 008d5b7c ["COPY", "register:4000:8", ["const:c25000:8"]]
- 008d5b7c bytes 601a00f0
+ 008d5b7c bytes 801a0090
- 008d5b80 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008d5b80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d5b80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d5b80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d5b80 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d5b80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5b80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d5b80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d5b80 bytes 00e03d91
+ 008d5b80 bytes 00e00091
- 008d5ba0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008d5ba0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d5ba0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d5ba0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d5ba0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008d5ba0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5ba0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d5ba0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d5ba0 bytes 42403b91
+ 008d5ba0 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8e5a948e70fff94400523e2656d2aa7"></a>

### [`008d5f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5f78.md) → [`008d5f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5f78.md) FUN_008d5f78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008d0760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md) [`008d9aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0053f81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f81c.md)
- 新版 呼出元 3件 [`008d0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md) [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.03% / 新版 95.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d5fa8",
      "incomplete_value": true,
      "site": "008d5fbc",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:4df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d5fa8",
      "incomplete_value": true,
      "site": "008d5fbc",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:452:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d5fa8",
      "READ",
      [
        "storage",
        "00299452",
        null,
        "string"
      ]
    ],
    [
      "008d6054",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ],
    [
      "008d6080",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d5fa8",
      "READ",
      [
        "storage",
        "002994df",
        null,
        "string"
      ]
    ],
    [
      "008d6054",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "008d6080",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5f78.md#insn-008d5fa0) · [`008d6054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5f78.md#insn-008d6054) · [`008d605c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5f78.md#insn-008d605c)
- 新版 [`008d5fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5f78.md#insn-008d5fa0) · [`008d6054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5f78.md#insn-008d6054)

~~~diff
- 008d5fa0 ["COPY", "tmp:0:8", ["const:452:8"]]
- 008d5fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d5fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d5fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d5fa0 ["COPY", "tmp:0:8", ["const:4df:8"]]
+ 008d5fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d5fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d5fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d5fa0 bytes 29491191
+ 008d5fa0 bytes 297d1391
- 008d6054 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:db0:8"]]
- 008d6054 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 008d6054 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:e60:8"]]
+ 008d6054 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 008d6054 bytes d6da46f9
+ 008d6054 bytes d63247f9
- 008d605c ["COPY", "register:4098:8", ["const:c24000:8"]]
- 008d605c bytes 731a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a2f14353c067f876e09123f0987231"></a>

### [`008d6360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d6/008d6360.md) → [`008d6360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d6/008d6360.md) FUN_008d6360

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) [`00996eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md)
- 新版 呼出元 2件 [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.97% / 新版 89.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_destination` 21件, `store_value` 29件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d6770",
      "incomplete_value": true,
      "site": "008d6770",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:af9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d6770",
      "incomplete_value": true,
      "site": "008d6770",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:a6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d6774",
      "incomplete_value": true,
      "site": "008d6774",
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
      "definition_site": "008d6774",
      "incomplete_value": true,
      "site": "008d6774",
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
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d6798",
      "incomplete_value": true,
      "site": "008d67a8",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d6798",
      "incomplete_value": true,
      "site": "008d67a8",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:963:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d6390",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008d63a4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d63ac",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008d6390",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d63a4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d63ac",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d6390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d6/008d6360.md#insn-008d6390) · [`008d63a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d6/008d6360.md#insn-008d63a4) · [`008d63ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d6/008d6360.md#insn-008d63ac)
- 新版 [`008d6390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d6/008d6360.md#insn-008d6390) · [`008d63a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d6/008d6360.md#insn-008d63a4) · [`008d63ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d6/008d6360.md#insn-008d63ac)

~~~diff
- 008d6390 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008d6390 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008d6390 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008d6390 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008d6390 bytes 08dd44f9
+ 008d6390 bytes 083d45f9
- 008d63a4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008d63a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008d63a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008d63a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008d63a4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008d63a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008d63a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008d63a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008d63a4 bytes 21603691
+ 008d63a4 bytes 21203991
- 008d63ac ["COPY", "tmp:0:8", ["const:998:8"]]
- 008d63ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d63ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d63ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d63ac ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008d63ac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d63ac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d63ac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d63ac bytes 42602691
+ 008d63ac bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96ad39fdb604c8996e7288b9522f82ab"></a>

### [`008d76b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d7/008d76b0.md) → [`008d76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d7/008d76b0.md) FUN_008d76b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) [`00996eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996eec.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.13% / 新版 91.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `store_destination` 35件, `store_value` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d7754",
      "incomplete_value": true,
      "site": "008d7764",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:6c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d7754",
      "incomplete_value": true,
      "site": "008d7764",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:637:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d7754",
      "incomplete_value": true,
      "site": "008d7768",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:6c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d7754",
      "incomplete_value": true,
      "site": "008d7768",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:637:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d7758",
      "incomplete_value": true,
      "site": "008d776c",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d7758",
      "incomplete_value": true,
      "site": "008d776c",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d76e0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008d76f0",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d76f8",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008d76e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d76f0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d76f8",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d76e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d7/008d76b0.md#insn-008d76e0) · [`008d76f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d7/008d76b0.md#insn-008d76f0) · [`008d76f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d7/008d76b0.md#insn-008d76f8)
- 新版 [`008d76e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d7/008d76b0.md#insn-008d76e0) · [`008d76f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d7/008d76b0.md#insn-008d76f0) · [`008d76f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d7/008d76b0.md#insn-008d76f8)

~~~diff
- 008d76e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008d76e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008d76e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008d76e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008d76e0 bytes 08dd44f9
+ 008d76e0 bytes 083d45f9
- 008d76f0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008d76f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008d76f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008d76f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008d76f0 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008d76f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008d76f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008d76f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008d76f0 bytes 21603691
+ 008d76f0 bytes 21203991
- 008d76f8 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008d76f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d76f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d76f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d76f8 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008d76f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d76f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d76f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d76f8 bytes 42602691
+ 008d76f8 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004a6d0408bffce644863509f505347c"></a>

### [`008d89fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d8/008d89fc.md) → [`008d89fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d8/008d89fc.md) FUN_008d89fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md) [`008dd98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00467864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467864.md)
- 新版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) [`008dd98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467864.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.55% / 新版 84.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `store_destination` 42件, `store_value` 16件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8ce0",
      "incomplete_value": true,
      "site": "008d8ce0",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:2cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8ce0",
      "incomplete_value": true,
      "site": "008d8ce0",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8ce4",
      "incomplete_value": true,
      "site": "008d8ce4",
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
      "definition_site": "008d8ce4",
      "incomplete_value": true,
      "site": "008d8ce4",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d90f4",
      "incomplete_value": true,
      "site": "008d90f4",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:ed5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d90f4",
      "incomplete_value": true,
      "site": "008d90f4",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8a34",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008d8a40",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d8a48",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008d8a34",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d8a40",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d8a48",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d8/008d89fc.md#insn-008d8a34) · [`008d8a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d8/008d89fc.md#insn-008d8a40) · [`008d8a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d8/008d89fc.md#insn-008d8a48)
- 新版 [`008d8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d8/008d89fc.md#insn-008d8a34) · [`008d8a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d8/008d89fc.md#insn-008d8a40) · [`008d8a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d8/008d89fc.md#insn-008d8a48)

~~~diff
- 008d8a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008d8a34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008d8a34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008d8a34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008d8a34 bytes 08dd44f9
+ 008d8a34 bytes 083d45f9
- 008d8a40 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008d8a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008d8a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008d8a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008d8a40 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008d8a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008d8a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008d8a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008d8a40 bytes 21603691
+ 008d8a40 bytes 21203991
- 008d8a48 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008d8a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008d8a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008d8a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008d8a48 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008d8a48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008d8a48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008d8a48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008d8a48 bytes 42602691
+ 008d8a48 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df990149fe09913e6f49f5c0a219d100"></a>

### [`008d99b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d99b0.md) → [`008d99b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d99b0.md) FUN_008d99b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00714cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00714/00714cf0.md) [`008e68f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md) [`00963004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00963/00963004.md) [`00a1bb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a1b/00a1bb38.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`006f0c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f0/006f0c7c.md) [`006f1828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f1/006f1828.md) [`006f1bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f1/006f1bc8.md)
- 新版 呼出元 4件 [`00714cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00714/00714cf0.md) [`008e68f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md) [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) [`00a1bb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1b/00a1bb38.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`006f0c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f0/006f0c7c.md) [`006f1828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1828.md) [`006f1bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1bc8.md)

変更の種類 call, call_target, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d9a30",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d9a30",
      "value": [
        "leaf",
        "ram:ace4cc:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d9a4c",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d9a4c",
      "value": [
        "leaf",
        "ram:ace4cc:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d9a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ],
    [
      "008d9a4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      "008d9a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ],
    [
      "008d9a4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d99b0.md#insn-008d9a30) · [`008d9a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d99b0.md#insn-008d9a4c)
- 新版 [`008d9a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d99b0.md#insn-008d9a30) · [`008d9a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d99b0.md#insn-008d9a4c)

~~~diff
- 008d9a30 ["INT_ADD", "register:40f0:8", ["const:8d9a30:8", "const:4:8"]]
- 008d9a30 ["CALL", null, ["ram:ace4cc:8"]]
+ 008d9a30 ["INT_ADD", "register:40f0:8", ["const:8d9a30:8", "const:4:8"]]
+ 008d9a30 ["CALL", null, ["ram:ace594:8"]]
- 008d9a30 bytes a7d20794
+ 008d9a30 bytes d9d20794
- 008d9a4c ["INT_ADD", "register:40f0:8", ["const:8d9a4c:8", "const:4:8"]]
- 008d9a4c ["CALL", null, ["ram:ace4cc:8"]]
+ 008d9a4c ["INT_ADD", "register:40f0:8", ["const:8d9a4c:8", "const:4:8"]]
+ 008d9a4c ["CALL", null, ["ram:ace594:8"]]
- 008d9a4c bytes a0d20794
+ 008d9a4c bytes d2d20794
~~~


<a id="compare-a363638cfbfe2892afa67035f0d0d41c"></a>

### [`008d9aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md) → [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) FUN_008d9aa4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) [`008ee26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee26c.md) [`009121c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00912/009121c4.md) · 呼出先 81件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md)
- 新版 呼出元 3件 [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) [`008ee26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee26c.md) [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) · 呼出先 81件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 7件, `store_value` 25件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9d24",
      "incomplete_value": false,
      "site": "008d9d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:6a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9d24",
      "incomplete_value": false,
      "site": "008d9d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:617:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9d50",
      "incomplete_value": false,
      "site": "008d9d50",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9d50",
      "incomplete_value": false,
      "site": "008d9d50",
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
            "const:b65:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9d70",
      "incomplete_value": false,
      "site": "008d9d70",
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
            "const:731:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9d70",
      "incomplete_value": false,
      "site": "008d9d70",
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
            "const:6a4:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d9d24",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "008d9d50",
      "DATA",
      [
        "storage",
        "002a7b65",
        null,
        "string"
      ]
    ],
    [
      "008d9d70",
      "DATA",
      [
        "storage",
        "002a16a4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d9d24",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "008d9d50",
      "DATA",
      [
        "storage",
        "002a7ad1",
        null,
        "string"
      ]
    ],
    [
      "008d9d70",
      "DATA",
      [
        "storage",
        "002a1731",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md#insn-008d9d1c) · [`008d9d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md#insn-008d9d20)
- 新版 [`008d9d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md#insn-008d9d1c) · [`008d9d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md#insn-008d9d20)

~~~diff
- 008d9d1c ["COPY", "tmp:0:8", ["const:617:8"]]
- 008d9d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d9d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d9d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9d1c ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 008d9d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d9d1c bytes 085d1891
+ 008d9d1c bytes 08911a91
- 008d9d20 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:90:8"]]
- 008d9d20 bytes b44302d1
+ 008d9d20 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:90:8"]]
+ 008d9d20 bytes b44302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284c83aeef98ba0d296c262ab68cef95"></a>

### [`008dd308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd308.md) → [`008dd308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd308.md) FUN_008dd308

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d9/008d9aa4.md) [`008dd98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md)
- 新版 呼出元 3件 [`008d9aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d9/008d9aa4.md) [`008dd98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008dd804",
      "incomplete_value": true,
      "site": "008dd804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dd804",
      "incomplete_value": true,
      "site": "008dd804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008dd8a8",
      "incomplete_value": false,
      "site": "008dd8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
              ]
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
      "definition_site": "008dd8a8",
      "incomplete_value": false,
      "site": "008dd8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008dd738",
      "incomplete_value": true,
      "site": "008dd738",
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
      "definition_site": "008dd738",
      "incomplete_value": true,
      "site": "008dd738",
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
    "ordinal": 30,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008dd72c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008dd740",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008dd748",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008dd72c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008dd740",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008dd748",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dd72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd308.md#insn-008dd72c) · [`008dd740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd308.md#insn-008dd740) · [`008dd748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd308.md#insn-008dd748)
- 新版 [`008dd72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd308.md#insn-008dd72c) · [`008dd740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd308.md#insn-008dd740) · [`008dd748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd308.md#insn-008dd748)

~~~diff
- 008dd72c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008dd72c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008dd72c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008dd72c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008dd72c bytes 00dd44f9
+ 008dd72c bytes 003d45f9
- 008dd740 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008dd740 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008dd740 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008dd740 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008dd740 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008dd740 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008dd740 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008dd740 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008dd740 bytes 21603691
+ 008dd740 bytes 21203991
- 008dd748 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008dd748 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008dd748 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008dd748 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008dd748 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008dd748 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008dd748 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008dd748 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008dd748 bytes 42602691
+ 008dd748 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6971c3e20904408968d20436e0428318"></a>

### [`008de844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008de/008de844.md) → [`008de844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008de/008de844.md) FUN_008de844

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008dd98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 33件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c80c.md)
- 新版 呼出元 2件 [`008dd98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008dd/008dd98c.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 33件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.90% / 新版 90.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 52件, `store_destination` 30件, `store_value` 26件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008de99c",
      "incomplete_value": true,
      "site": "008de9ac",
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
                "const:1ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008de99c",
      "incomplete_value": true,
      "site": "008de9ac",
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
                "const:13d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008de9b8",
      "incomplete_value": true,
      "site": "008de9b8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008de9b8",
      "incomplete_value": true,
      "site": "008de9b8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008dea14",
      "incomplete_value": true,
      "site": "008dea24",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:74a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dea14",
      "incomplete_value": true,
      "site": "008dea24",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:6bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008de878",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008de88c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008de894",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008de878",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008de88c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008de894",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008de878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008de/008de844.md#insn-008de878) · [`008de88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008de/008de844.md#insn-008de88c) · [`008de894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008de/008de844.md#insn-008de894)
- 新版 [`008de878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008de/008de844.md#insn-008de878) · [`008de88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008de/008de844.md#insn-008de88c) · [`008de894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008de/008de844.md#insn-008de894)

~~~diff
- 008de878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008de878 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008de878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008de878 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008de878 bytes 00dd44f9
+ 008de878 bytes 003d45f9
- 008de88c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008de88c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008de88c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008de88c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008de88c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008de88c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008de88c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008de88c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008de88c bytes 21603691
+ 008de88c bytes 21203991
- 008de894 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008de894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008de894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008de894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008de894 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008de894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008de894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008de894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008de894 bytes 42602691
+ 008de894 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8639c440e70d3ac994b310c6d93c0745"></a>

### [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) → [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) FUN_008e0bc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 114件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 114件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 23件, `store_destination` 2件, `store_value` 12件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e0d08",
      "incomplete_value": true,
      "site": "008e0d08",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0d08",
      "incomplete_value": true,
      "site": "008e0d08",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a1:8"
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
      "definition_site": "008e0d3c",
      "incomplete_value": true,
      "site": "008e0d54",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0d3c",
      "incomplete_value": true,
      "site": "008e0d54",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:279:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e0eac",
      "incomplete_value": true,
      "site": "008e0eac",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0eac",
      "incomplete_value": true,
      "site": "008e0eac",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e0bf4",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008e0c08",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e0c10",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e0bf4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008e0c08",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e0c10",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e0bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md#insn-008e0bf4) · [`008e0c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md#insn-008e0c08) · [`008e0c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md#insn-008e0c10)
- 新版 [`008e0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md#insn-008e0bf4) · [`008e0c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md#insn-008e0c08) · [`008e0c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md#insn-008e0c10)

~~~diff
- 008e0bf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008e0bf4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008e0bf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008e0bf4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008e0bf4 bytes 00dd44f9
+ 008e0bf4 bytes 003d45f9
- 008e0c08 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008e0c08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008e0c08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008e0c08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008e0c08 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008e0c08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008e0c08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008e0c08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008e0c08 bytes 21603691
+ 008e0c08 bytes 21203991
- 008e0c10 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008e0c10 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008e0c10 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008e0c10 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008e0c10 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008e0c10 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008e0c10 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008e0c10 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008e0c10 bytes 42602691
+ 008e0c10 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-070a07c36aaff50259fc1121660db3b7"></a>

### [`008e6014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md) → [`008e6014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md) FUN_008e6014

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0086a350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`0042a40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a40c.md) [`005416b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00541/005416b0.md)
- 新版 呼出元 2件 [`0086a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0042a40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a40c.md) [`005416b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005416b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e6078",
      "incomplete_value": true,
      "site": "008e6080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:b75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e6078",
      "incomplete_value": true,
      "site": "008e6080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:b7c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e60b0",
      "incomplete_value": false,
      "site": "008e60b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:8b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e60b0",
      "incomplete_value": false,
      "site": "008e60b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:94b:8"
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
      "definition_site": "008e6134",
      "incomplete_value": false,
      "site": "008e613c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:caf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e6134",
      "incomplete_value": false,
      "site": "008e613c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:c22:8"
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
      "008e6064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008e60ac"
      ]
    ],
    [
      "008e6078",
      "PARAM",
      [
        "storage",
        "002a4b7c",
        null,
        null
      ]
    ],
    [
      "008e6088",
      "PARAM",
      [
        "storage",
        "0029a363",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008e6064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e60ac"
      ]
    ],
    [
      "008e6078",
      "PARAM",
      [
        "storage",
        "002a4b75",
        null,
        null
      ]
    ],
    [
      "008e6088",
      "PARAM",
      [
        "storage",
        "0029a3f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e6078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md#insn-008e6078) · [`008e6088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md#insn-008e6088) · [`008e6094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md#insn-008e6094)
- 新版 [`008e6078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md#insn-008e6078) · [`008e6088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md#insn-008e6088) · [`008e6094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md#insn-008e6094)

~~~diff
- 008e6078 ["COPY", "tmp:0:8", ["const:b7c:8"]]
- 008e6078 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008e6078 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008e6078 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008e6078 ["COPY", "tmp:0:8", ["const:b75:8"]]
+ 008e6078 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6078 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6078 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008e6078 bytes 21f02d91
+ 008e6078 bytes 21d42d91
- 008e6088 ["COPY", "tmp:0:8", ["const:363:8"]]
- 008e6088 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008e6088 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008e6088 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008e6088 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 008e6088 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6088 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6088 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008e6088 bytes 218c0d91
+ 008e6088 bytes 21c00f91
- 008e6094 ["COPY", "tmp:0:8", ["const:cb1:8"]]
- 008e6094 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008e6094 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008e6094 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008e6094 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 008e6094 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6094 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6094 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008e6094 bytes 21c43291
+ 008e6094 bytes 21a03291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aa747bea736795a4089f625a8a75b25"></a>

### [`008e68f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md) → [`008e68f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md) FUN_008e68f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 71件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444bb0.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 71件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e6988",
      "incomplete_value": true,
      "site": "008e6988",
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
      "definition_site": "008e6988",
      "incomplete_value": true,
      "site": "008e6988",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e6990",
      "incomplete_value": false,
      "site": "008e69a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e6990",
      "incomplete_value": false,
      "site": "008e69a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e6998",
      "incomplete_value": false,
      "site": "008e69a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e6998",
      "incomplete_value": false,
      "site": "008e69a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e6968",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008e6990",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e6998",
      "PARAM",
      [
        "storage",
        "00bf7998",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e6968",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008e6990",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e6998",
      "PARAM",
      [
        "storage",
        "00bf7a48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e6968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md#insn-008e6968) · [`008e6990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md#insn-008e6990) · [`008e6998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md#insn-008e6998)
- 新版 [`008e6968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md#insn-008e6968) · [`008e6990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md#insn-008e6990) · [`008e6998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md#insn-008e6998)

~~~diff
- 008e6968 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:9b8:8"]]
- 008e6968 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008e6968 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a78:8"]]
+ 008e6968 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008e6968 bytes 40dd44f9
+ 008e6968 bytes 403d45f9
- 008e6990 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008e6990 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008e6990 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008e6990 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008e6990 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008e6990 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6990 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008e6990 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008e6990 bytes 21603691
+ 008e6990 bytes 21203991
- 008e6998 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008e6998 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008e6998 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008e6998 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008e6998 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 008e6998 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008e6998 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008e6998 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008e6998 bytes 42602691
+ 008e6998 bytes 42202991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7817bde90606cb52cb22938ae1779328"></a>

### [`008ec0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec0b0.md) → [`008ec0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec0b0.md) FUN_008ec0b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008ebd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008eb/008ebd34.md) [`008ec2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2b4.md) · 呼出先 5件 [`0064c428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c428.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`008ebd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008eb/008ebd34.md) [`008ec2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2b4.md) · 呼出先 5件 [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ec0cc",
      "incomplete_value": false,
      "site": "008ec0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec0cc",
      "incomplete_value": false,
      "site": "008ec0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ec1a0",
      "incomplete_value": false,
      "site": "008ec1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec1a0",
      "incomplete_value": false,
      "site": "008ec1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ec1dc",
      "incomplete_value": false,
      "site": "008ec1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec1dc",
      "incomplete_value": false,
      "site": "008ec1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "008ec0d0",
      "DATA",
      [
        "storage",
        "00c07b98",
        null,
        "pointer"
      ]
    ],
    [
      "008ec1a4",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "008ec1e0",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008ec0d0",
      "DATA",
      [
        "storage",
        "00c07c48",
        null,
        "pointer"
      ]
    ],
    [
      "008ec1a4",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "008ec1e0",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ec0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec0b0.md#insn-008ec0cc) · [`008ec1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec0b0.md#insn-008ec1a0) · [`008ec1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec0b0.md#insn-008ec1dc)
- 新版 [`008ec0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec0b0.md#insn-008ec0cc) · [`008ec1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec0b0.md#insn-008ec1a0) · [`008ec1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec0b0.md#insn-008ec1dc)

~~~diff
- 008ec0cc ["COPY", "tmp:0:8", ["const:b98:8"]]
- 008ec0cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ec0cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ec0cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ec0cc ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 008ec0cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec0cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec0cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ec0cc bytes 08612e91
+ 008ec0cc bytes 08213191
- 008ec1a0 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 008ec1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ec1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ec1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ec1a0 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 008ec1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ec1a0 bytes 08213491
+ 008ec1a0 bytes 08e13691
- 008ec1dc ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008ec1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ec1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ec1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ec1dc ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008ec1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ec1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ec1dc bytes 08a10791
+ 008ec1dc bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f5331ff12c8fe560385e71cebf2d72"></a>

### [`008ec2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2d8.md) → [`008ec2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2d8.md) FUN_008ec2d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d5d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d5/008d5d88.md) [`008ec2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2d8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008d5d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d5/008d5d88.md) [`008ec2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2d8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ec434",
      "incomplete_value": false,
      "site": "008ec43c",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec434",
      "incomplete_value": false,
      "site": "008ec43c",
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
            "const:311:8"
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
      "definition_site": "008ec5bc",
      "incomplete_value": false,
      "site": "008ec5c4",
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
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec5bc",
      "incomplete_value": false,
      "site": "008ec5c4",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008eca0c",
      "incomplete_value": false,
      "site": "008eca14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eca0c",
      "incomplete_value": false,
      "site": "008eca14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ec434",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008ec5bc",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008ec694",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008ec434",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008ec5bc",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008ec694",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ec434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2d8.md#insn-008ec434) · [`008ec5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2d8.md#insn-008ec5bc) · [`008ec694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008ec2d8.md#insn-008ec694)
- 新版 [`008ec434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2d8.md#insn-008ec434) · [`008ec5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2d8.md#insn-008ec5bc) · [`008ec694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008ec2d8.md#insn-008ec694)

~~~diff
- 008ec434 ["COPY", "tmp:0:8", ["const:311:8"]]
- 008ec434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ec434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ec434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ec434 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008ec434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ec434 bytes 21440c91
+ 008ec434 bytes 21280c91
- 008ec5bc ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008ec5bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ec5bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ec5bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ec5bc ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008ec5bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec5bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec5bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ec5bc bytes 21d40b91
+ 008ec5bc bytes 21b80b91
- 008ec694 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 008ec694 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ec694 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ec694 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ec694 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 008ec694 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec694 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ec694 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ec694 bytes 21681f91
+ 008ec694 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9a0084a181c23755b0a5a4b0eabca1"></a>

### [`008eccc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008eccc4.md) → [`008eccc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008eccc4.md) FUN_008eccc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`008d0760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008d0/008d0760.md) [`008eccc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008eccc4.md) [`00a11cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a11/00a11cc0.md) [`00a15464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a15/00a15464.md) [`00a1e428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a1e/00a1e428.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 6件 [`008d0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md) [`008eccc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008eccc4.md) [`00a11cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a11/00a11cc0.md) [`00a15464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a15/00a15464.md) [`00a1e428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e428.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.98% / 新版 98.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ece14",
      "incomplete_value": false,
      "site": "008ece1c",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ece14",
      "incomplete_value": false,
      "site": "008ece1c",
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
            "const:311:8"
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
      "definition_site": "008ecf9c",
      "incomplete_value": false,
      "site": "008ecfa4",
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
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ecf9c",
      "incomplete_value": false,
      "site": "008ecfa4",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ed074",
      "incomplete_value": false,
      "site": "008ed080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed074",
      "incomplete_value": false,
      "site": "008ed080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ece14",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008ecf9c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008ed074",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008ece14",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008ecf9c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008ed074",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ece14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008eccc4.md#insn-008ece14) · [`008ecf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008eccc4.md#insn-008ecf9c) · [`008ed074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ec/008eccc4.md#insn-008ed074)
- 新版 [`008ece14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008eccc4.md#insn-008ece14) · [`008ecf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008eccc4.md#insn-008ecf9c) · [`008ed074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ec/008eccc4.md#insn-008ed074)

~~~diff
- 008ece14 ["COPY", "tmp:0:8", ["const:311:8"]]
- 008ece14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ece14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ece14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ece14 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008ece14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ece14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ece14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ece14 bytes 21440c91
+ 008ece14 bytes 21280c91
- 008ecf9c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008ecf9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ecf9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ecf9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ecf9c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008ecf9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ecf9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ecf9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ecf9c bytes 21d40b91
+ 008ecf9c bytes 21b80b91
- 008ed074 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 008ed074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ed074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ed074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ed074 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 008ed074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ed074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ed074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ed074 bytes 21681f91
+ 008ed074 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

