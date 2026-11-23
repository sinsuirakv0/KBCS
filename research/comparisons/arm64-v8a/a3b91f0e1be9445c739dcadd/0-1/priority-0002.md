# v15.7.2 → v15.7.3 · 最優先の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-d1150a4de9147cc458adf2540862e51d"></a>

### [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) → [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) FUN_004289a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0043344c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/0043344c.md) [`00434024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 7件 [`0043344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md) [`00434024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5a6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5ad:8"
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
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
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
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
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
      "004289d4",
      "READ",
      [
        "storage",
        "002a65ad",
        null,
        "string"
      ]
    ],
    [
      "004289d4",
      "READ",
      [
        "storage",
        "002a65bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004289d4",
      "READ",
      [
        "storage",
        "002a65a6",
        null,
        "string"
      ]
    ],
    [
      "004289d4",
      "READ",
      [
        "storage",
        "002a65b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004289d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md#insn-004289d0)
- 新版 [`004289d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md#insn-004289d0)

~~~diff
- 004289d0 ["COPY", "tmp:0:8", ["const:5ad:8"]]
- 004289d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004289d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004289d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004289d0 ["COPY", "tmp:0:8", ["const:5a6:8"]]
+ 004289d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004289d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004289d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004289d0 bytes 08b51691
+ 004289d0 bytes 08991691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c6650e85a6c87dfd7af6e4af28c0f4b"></a>

### [`004289f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md) → [`004289f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md) FUN_004289f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0042ca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ce34.md) [`00431534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md) [`00a26ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a26/00a26ddc.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 5件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md) [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`00a26ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:c6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:be0:8"
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
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
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
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428a30",
      "incomplete_value": true,
      "site": "00428a30",
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
                "const:1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a30",
      "incomplete_value": true,
      "site": "00428a30",
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
                "const:1e:8"
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
      "00428a18",
      "READ",
      [
        "storage",
        "00298be0",
        null,
        "string"
      ]
    ],
    [
      "00428a18",
      "READ",
      [
        "storage",
        "00298bf0",
        null,
        "string"
      ]
    ],
    [
      "00428a20",
      "READ",
      [
        "storage",
        "00298bfe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428a18",
      "READ",
      [
        "storage",
        "00298c6d",
        null,
        "string"
      ]
    ],
    [
      "00428a18",
      "READ",
      [
        "storage",
        "00298c7d",
        null,
        "string"
      ]
    ],
    [
      "00428a20",
      "READ",
      [
        "storage",
        "00298c8b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md#insn-00428a10) · [`00428a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md#insn-00428a14)
- 新版 [`00428a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md#insn-00428a10) · [`00428a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md#insn-00428a14)

~~~diff
- 00428a10 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00428a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428a10 ["COPY", "tmp:0:8", ["const:c6d:8"]]
+ 00428a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428a10 bytes 08812f91
+ 00428a10 bytes 08b53191
- 00428a14 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00428a14 bytes 49f4ffb0
+ 00428a14 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00428a14 bytes 49f4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c59258f56a4c3af45def0b6e1ac27b38"></a>

### [`00428a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428a44.md) → [`00428a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428a44.md) FUN_00428a44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004508a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/004508a4.md) [`00454f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00454/00454f34.md) · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md) [`00454f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454f34.md) · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0b0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428aac",
      "incomplete_value": false,
      "site": "00428ab4",
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
            "const:68c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428aac",
      "incomplete_value": false,
      "site": "00428ab4",
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
            "const:695:8"
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
      "00428aac",
      "PARAM",
      [
        "storage",
        "002ac695",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00428aac",
      "PARAM",
      [
        "storage",
        "002ac68c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428a44.md#insn-00428aac)
- 新版 [`00428aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428a44.md#insn-00428aac)

~~~diff
- 00428aac ["COPY", "tmp:0:8", ["const:695:8"]]
- 00428aac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00428aac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00428aac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00428aac ["COPY", "tmp:0:8", ["const:68c:8"]]
+ 00428aac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00428aac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00428aac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00428aac bytes 21541a91
+ 00428aac bytes 21301a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57cf6c3b7fbf7644ca7095d0ad8a448"></a>

### [`00428b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428b68.md) → [`00428b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428b68.md) FUN_00428b68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00453c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/00453c78.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428b90",
      "incomplete_value": true,
      "site": "00428b98",
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
      "definition_site": "00428b90",
      "incomplete_value": true,
      "site": "00428b98",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428b8c",
      "incomplete_value": true,
      "site": "00428b9c",
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
                "const:28b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428b8c",
      "incomplete_value": true,
      "site": "00428b9c",
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
                "const:1fe:8"
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
      "definition_site": "00428b8c",
      "incomplete_value": true,
      "site": "00428b9c",
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
      "definition_site": "00428b8c",
      "incomplete_value": true,
      "site": "00428b9c",
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
      "00428b8c",
      "READ",
      [
        "storage",
        "0029d1fe",
        null,
        "string"
      ]
    ],
    [
      "00428b8c",
      "READ",
      [
        "storage",
        "0029d20e",
        null,
        "string"
      ]
    ],
    [
      "00428b90",
      "READ",
      [
        "storage",
        "0029d21e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428b8c",
      "READ",
      [
        "storage",
        "0029d28b",
        null,
        "string"
      ]
    ],
    [
      "00428b8c",
      "READ",
      [
        "storage",
        "0029d29b",
        null,
        "string"
      ]
    ],
    [
      "00428b90",
      "READ",
      [
        "storage",
        "0029d2ab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428b68.md#insn-00428b84) · [`00428b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428b68.md#insn-00428b88)
- 新版 [`00428b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428b68.md#insn-00428b84) · [`00428b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428b68.md#insn-00428b88)

~~~diff
- 00428b84 ["COPY", "tmp:0:8", ["const:1fe:8"]]
- 00428b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428b84 ["COPY", "tmp:0:8", ["const:28b:8"]]
+ 00428b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428b84 bytes 08f90791
+ 00428b84 bytes 082d0a91
- 00428b88 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00428b88 bytes 49f4ffb0
+ 00428b88 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00428b88 bytes 49f4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435676c5cde8a9928d7ef54f7a47f106"></a>

### [`00428bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428bc0.md) → [`00428bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428bc0.md) FUN_00428bc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0043196c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md) [`00431e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md) [`00432420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0043196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md) [`00431e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md) [`00432420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428bf0",
      "incomplete_value": true,
      "site": "00428c00",
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
                "const:1f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428bf0",
      "incomplete_value": true,
      "site": "00428c00",
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
                "const:287:8"
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
      "definition_site": "00428bf0",
      "incomplete_value": true,
      "site": "00428c00",
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
      "definition_site": "00428bf0",
      "incomplete_value": true,
      "site": "00428c00",
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
      "00428bf0",
      "READ",
      [
        "storage",
        "002a9287",
        null,
        "string"
      ]
    ],
    [
      "00428bf0",
      "READ",
      [
        "storage",
        "002a9297",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428bf0",
      "READ",
      [
        "storage",
        "002a91f3",
        null,
        "string"
      ]
    ],
    [
      "00428bf0",
      "READ",
      [
        "storage",
        "002a9203",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428bc0.md#insn-00428bec)
- 新版 [`00428bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428bc0.md#insn-00428bec)

~~~diff
- 00428bec ["COPY", "tmp:0:8", ["const:287:8"]]
- 00428bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428bec ["COPY", "tmp:0:8", ["const:1f3:8"]]
+ 00428bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428bec bytes 081d0a91
+ 00428bec bytes 08cd0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a8e826015129d8a258a563175012d1"></a>

### [`00428c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c14.md) → [`00428c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md) FUN_00428c14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`00582d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/00582d50.md) [`00583d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00583/00583d60.md) [`00585038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00585/00585038.md) [`00586748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00586/00586748.md) [`005878b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00587/005878b8.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 7件 [`00582d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582d50.md) [`00583d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d60.md) [`00585038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/00585038.md) [`00586748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00586/00586748.md) [`005878b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00587/005878b8.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428c38",
      "incomplete_value": true,
      "site": "00428c4c",
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
                "const:309:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428c38",
      "incomplete_value": true,
      "site": "00428c4c",
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
                "const:27c:8"
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
      "definition_site": "00428c38",
      "incomplete_value": true,
      "site": "00428c4c",
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
      "definition_site": "00428c38",
      "incomplete_value": true,
      "site": "00428c4c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428c50",
      "incomplete_value": true,
      "site": "00428c50",
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
                "const:1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428c50",
      "incomplete_value": true,
      "site": "00428c50",
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
                "const:1d:8"
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
      "00428c38",
      "READ",
      [
        "storage",
        "0029f27c",
        null,
        "string"
      ]
    ],
    [
      "00428c38",
      "READ",
      [
        "storage",
        "0029f28c",
        null,
        "string"
      ]
    ],
    [
      "00428c40",
      "READ",
      [
        "storage",
        "0029f299",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428c38",
      "READ",
      [
        "storage",
        "0029f309",
        null,
        "string"
      ]
    ],
    [
      "00428c38",
      "READ",
      [
        "storage",
        "0029f319",
        null,
        "string"
      ]
    ],
    [
      "00428c40",
      "READ",
      [
        "storage",
        "0029f326",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c14.md#insn-00428c30) · [`00428c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c14.md#insn-00428c34)
- 新版 [`00428c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md#insn-00428c30) · [`00428c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md#insn-00428c34)

~~~diff
- 00428c30 ["COPY", "tmp:0:8", ["const:27c:8"]]
- 00428c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428c30 ["COPY", "tmp:0:8", ["const:309:8"]]
+ 00428c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428c30 bytes 08f10991
+ 00428c30 bytes 08250c91
- 00428c34 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00428c34 bytes 49f4ffb0
+ 00428c34 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00428c34 bytes 49f4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ea043f77ef915b929e2749e53740ed"></a>

### [`00428c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c64.md) → [`00428c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c64.md) FUN_00428c64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428c94",
      "incomplete_value": true,
      "site": "00428ca0",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428c94",
      "incomplete_value": true,
      "site": "00428ca0",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:fa:8"
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
      "definition_site": "00428c94",
      "incomplete_value": true,
      "site": "00428ca0",
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
      "definition_site": "00428c94",
      "incomplete_value": true,
      "site": "00428ca0",
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
      "00428c94",
      "READ",
      [
        "storage",
        "002a30fa",
        null,
        "string"
      ]
    ],
    [
      "00428c94",
      "READ",
      [
        "storage",
        "002a310a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428c94",
      "READ",
      [
        "storage",
        "002a30f3",
        null,
        "string"
      ]
    ],
    [
      "00428c94",
      "READ",
      [
        "storage",
        "002a3103",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c64.md#insn-00428c90)
- 新版 [`00428c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c64.md#insn-00428c90)

~~~diff
- 00428c90 ["COPY", "tmp:0:8", ["const:fa:8"]]
- 00428c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428c90 ["COPY", "tmp:0:8", ["const:f3:8"]]
+ 00428c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428c90 bytes 08e90391
+ 00428c90 bytes 08cd0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eabe82238aadec83bbeea6fb5c6c8c6"></a>

### [`00428cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428cb4.md) → [`00428cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md) FUN_00428cb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428ce4",
      "incomplete_value": true,
      "site": "00428cf4",
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
                "const:315:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428ce4",
      "incomplete_value": true,
      "site": "00428cf4",
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
                "const:31c:8"
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
      "definition_site": "00428ce4",
      "incomplete_value": true,
      "site": "00428cf4",
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
      "definition_site": "00428ce4",
      "incomplete_value": true,
      "site": "00428cf4",
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
      "00428ce4",
      "READ",
      [
        "storage",
        "002a531c",
        null,
        "string"
      ]
    ],
    [
      "00428ce4",
      "READ",
      [
        "storage",
        "002a532c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428ce4",
      "READ",
      [
        "storage",
        "002a5315",
        null,
        "string"
      ]
    ],
    [
      "00428ce4",
      "READ",
      [
        "storage",
        "002a5325",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428cb4.md#insn-00428ce0)
- 新版 [`00428ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md#insn-00428ce0)

~~~diff
- 00428ce0 ["COPY", "tmp:0:8", ["const:31c:8"]]
- 00428ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428ce0 ["COPY", "tmp:0:8", ["const:315:8"]]
+ 00428ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428ce0 bytes 08710c91
+ 00428ce0 bytes 08550c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bec3f2f535c81656fc842fad63e2a1b"></a>

### [`00428d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428d08.md) → [`00428d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428d08.md) FUN_00428d08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428d24",
      "incomplete_value": false,
      "site": "00428d3c",
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
            "const:33a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d24",
      "incomplete_value": false,
      "site": "00428d3c",
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
            "const:341:8"
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
      "definition_site": "00428d30",
      "incomplete_value": false,
      "site": "00428d3c",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d30",
      "incomplete_value": false,
      "site": "00428d3c",
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
            "const:aa8:8"
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
      "definition_site": "00428d44",
      "incomplete_value": false,
      "site": "00428d4c",
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
            "const:95d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d44",
      "incomplete_value": false,
      "site": "00428d4c",
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
            "const:8d0:8"
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
      "00428d24",
      "PARAM",
      [
        "storage",
        "002a5341",
        null,
        "string"
      ]
    ],
    [
      "00428d30",
      "PARAM",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined2"
      ]
    ],
    [
      "00428d44",
      "PARAM",
      [
        "storage",
        "002978d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428d24",
      "PARAM",
      [
        "storage",
        "002a533a",
        null,
        "string"
      ]
    ],
    [
      "00428d30",
      "PARAM",
      [
        "storage",
        "00c24b68",
        null,
        "undefined2"
      ]
    ],
    [
      "00428d44",
      "PARAM",
      [
        "storage",
        "0029795d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428d08.md#insn-00428d24) · [`00428d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428d08.md#insn-00428d2c)
- 新版 [`00428d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428d08.md#insn-00428d24) · [`00428d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428d08.md#insn-00428d2c)

~~~diff
- 00428d24 ["COPY", "tmp:0:8", ["const:341:8"]]
- 00428d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00428d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00428d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00428d24 ["COPY", "tmp:0:8", ["const:33a:8"]]
+ 00428d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00428d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00428d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00428d24 bytes 00040d91
+ 00428d24 bytes 00e80c91
- 00428d2c ["COPY", "register:4008:8", ["const:c24000:8"]]
- 00428d2c bytes e13f0090
+ 00428d2c ["COPY", "register:4008:8", ["const:c24000:8"]]
+ 00428d2c bytes e13f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba11bf90e70842cc213c6a65bd7f12f"></a>

### [`00428dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428dc8.md) → [`00428dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428dc8.md) FUN_00428dc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00435c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428de4",
      "incomplete_value": false,
      "site": "00428dfc",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428de4",
      "incomplete_value": false,
      "site": "00428dfc",
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
            "const:803:8"
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
      "definition_site": "00428df0",
      "incomplete_value": false,
      "site": "00428dfc",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428df0",
      "incomplete_value": false,
      "site": "00428dfc",
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
            "const:aa8:8"
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
      "definition_site": "00428e04",
      "incomplete_value": false,
      "site": "00428e0c",
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
            "const:2dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428e04",
      "incomplete_value": false,
      "site": "00428e0c",
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
            "const:250:8"
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
      "00428de4",
      "PARAM",
      [
        "storage",
        "00296803",
        null,
        "string"
      ]
    ],
    [
      "00428df0",
      "PARAM",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined2"
      ]
    ],
    [
      "00428e04",
      "PARAM",
      [
        "storage",
        "002a0250",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428de4",
      "PARAM",
      [
        "storage",
        "00296890",
        null,
        "string"
      ]
    ],
    [
      "00428df0",
      "PARAM",
      [
        "storage",
        "00c24b68",
        null,
        "undefined2"
      ]
    ],
    [
      "00428e04",
      "PARAM",
      [
        "storage",
        "002a02dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428dc8.md#insn-00428de4) · [`00428dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428dc8.md#insn-00428dec)
- 新版 [`00428de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428dc8.md#insn-00428de4) · [`00428dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428dc8.md#insn-00428dec)

~~~diff
- 00428de4 ["COPY", "tmp:0:8", ["const:803:8"]]
- 00428de4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00428de4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00428de4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00428de4 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00428de4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00428de4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00428de4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00428de4 bytes 000c2091
+ 00428de4 bytes 00402291
- 00428dec ["COPY", "register:4008:8", ["const:c24000:8"]]
- 00428dec bytes e13f0090
+ 00428dec ["COPY", "register:4008:8", ["const:c24000:8"]]
+ 00428dec bytes e13f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3a6d07ae2b5ea5b9a9b2017b9ff05f6"></a>

### [`00428e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428e88.md) → [`00428e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md) FUN_00428e88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00949c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428ea4",
      "incomplete_value": false,
      "site": "00428ebc",
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
            "const:2eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428ea4",
      "incomplete_value": false,
      "site": "00428ebc",
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
            "const:25e:8"
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
      "definition_site": "00428eb0",
      "incomplete_value": false,
      "site": "00428ebc",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428eb0",
      "incomplete_value": false,
      "site": "00428ebc",
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
            "const:aa8:8"
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
      "definition_site": "00428ec4",
      "incomplete_value": false,
      "site": "00428ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:8d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428ec4",
      "incomplete_value": false,
      "site": "00428ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:845:8"
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
      "00428ea4",
      "PARAM",
      [
        "storage",
        "002a025e",
        null,
        "string"
      ]
    ],
    [
      "00428eb0",
      "PARAM",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined2"
      ]
    ],
    [
      "00428ec4",
      "PARAM",
      [
        "storage",
        "00295845",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428ea4",
      "PARAM",
      [
        "storage",
        "002a02eb",
        null,
        "string"
      ]
    ],
    [
      "00428eb0",
      "PARAM",
      [
        "storage",
        "00c24b68",
        null,
        "undefined2"
      ]
    ],
    [
      "00428ec4",
      "PARAM",
      [
        "storage",
        "002958d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428e88.md#insn-00428ea4) · [`00428eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428e88.md#insn-00428eac)
- 新版 [`00428ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md#insn-00428ea4) · [`00428eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md#insn-00428eac)

~~~diff
- 00428ea4 ["COPY", "tmp:0:8", ["const:25e:8"]]
- 00428ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00428ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00428ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00428ea4 ["COPY", "tmp:0:8", ["const:2eb:8"]]
+ 00428ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00428ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00428ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00428ea4 bytes 00780991
+ 00428ea4 bytes 00ac0b91
- 00428eac ["COPY", "register:4008:8", ["const:c24000:8"]]
- 00428eac bytes e13f0090
+ 00428eac ["COPY", "register:4008:8", ["const:c24000:8"]]
+ 00428eac bytes e13f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a38d4fcaad3cdf68bf22c12cce27edb"></a>

### [`00428f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428f48.md) → [`00428f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428f48.md) FUN_00428f48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006833dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00683/006833dc.md) [`00a17ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`006833dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00683/006833dc.md) [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428f70",
      "incomplete_value": true,
      "site": "00428f80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428f70",
      "incomplete_value": true,
      "site": "00428f80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00428f84",
      "incomplete_value": true,
      "site": "00428f84",
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
      "definition_site": "00428f84",
      "incomplete_value": true,
      "site": "00428f84",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428f90",
      "incomplete_value": false,
      "site": "00428f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428f90",
      "incomplete_value": false,
      "site": "00428f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00428f70",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00428f78",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00428f90",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428f70",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00428f78",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00428f90",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428f48.md#insn-00428f64) · [`00428f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428f48.md#insn-00428f90) · [`00428fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428f48.md#insn-00428fc8)
- 新版 [`00428f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428f48.md#insn-00428f64) · [`00428f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428f48.md#insn-00428f90) · [`00428fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428f48.md#insn-00428fc8)

~~~diff
- 00428f64 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00428f64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00428f64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00428f64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00428f64 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00428f64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00428f64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00428f64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00428f64 bytes 29291c91
+ 00428f64 bytes 29d91991
- 00428f90 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00428f90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00428f90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00428f90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00428f90 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00428f90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00428f90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00428f90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00428f90 bytes 21e41791
+ 00428f90 bytes 21181a91
- 00428fc8 ["COPY", "tmp:0:8", ["const:2ab:8"]]
- 00428fc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00428fc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00428fc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00428fc8 ["COPY", "tmp:0:8", ["const:217:8"]]
+ 00428fc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00428fc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00428fc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00428fc8 bytes 21ac0a91
+ 00428fc8 bytes 215c0891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-199b0a9af0e2de28634abed276e82e5c"></a>

### [`00429060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429060.md) → [`00429060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md) FUN_00429060

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0068d810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d810.md) [`008c2a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00429088",
      "incomplete_value": true,
      "site": "00429098",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429088",
      "incomplete_value": true,
      "site": "00429098",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042909c",
      "incomplete_value": true,
      "site": "0042909c",
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
      "definition_site": "0042909c",
      "incomplete_value": true,
      "site": "0042909c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004290a8",
      "incomplete_value": false,
      "site": "004290b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004290a8",
      "incomplete_value": false,
      "site": "004290b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00429088",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00429090",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "004290a8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429088",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00429090",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "004290a8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042907c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429060.md#insn-0042907c) · [`004290a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429060.md#insn-004290a8) · [`004290e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429060.md#insn-004290e0)
- 新版 [`0042907c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md#insn-0042907c) · [`004290a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md#insn-004290a8) · [`004290e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md#insn-004290e0)

~~~diff
- 0042907c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042907c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042907c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042907c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042907c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042907c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042907c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042907c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042907c bytes 29291c91
+ 0042907c bytes 29d91991
- 004290a8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004290a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004290a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004290a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004290a8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 004290a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004290a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004290a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004290a8 bytes 21e41791
+ 004290a8 bytes 21181a91
- 004290e0 ["COPY", "tmp:0:8", ["const:f2:8"]]
- 004290e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004290e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004290e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004290e0 ["COPY", "tmp:0:8", ["const:5e:8"]]
+ 004290e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004290e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004290e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004290e0 bytes 21c80391
+ 004290e0 bytes 21780191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484aaa55320393077a7bad1b24267a04"></a>

### [`00429178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429178.md) → [`00429178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429178.md) FUN_00429178

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004291a4",
      "incomplete_value": true,
      "site": "004291b8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004291a4",
      "incomplete_value": true,
      "site": "004291b8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "004291bc",
      "incomplete_value": true,
      "site": "004291bc",
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
      "definition_site": "004291bc",
      "incomplete_value": true,
      "site": "004291bc",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004291c8",
      "incomplete_value": false,
      "site": "004291d0",
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
            "const:2f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004291c8",
      "incomplete_value": false,
      "site": "004291d0",
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
            "const:2f8:8"
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
      "004291a4",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "004291b0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "004291c8",
      "PARAM",
      [
        "storage",
        "002a52f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004291a4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "004291b0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "004291c8",
      "PARAM",
      [
        "storage",
        "002a52f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429178.md#insn-00429198) · [`004291c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429178.md#insn-004291c8) · [`00429200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429178.md#insn-00429200)
- 新版 [`00429198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429178.md#insn-00429198) · [`004291c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429178.md#insn-004291c8) · [`00429200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429178.md#insn-00429200)

~~~diff
- 00429198 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429198 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429198 bytes 29291c91
+ 00429198 bytes 29d91991
- 004291c8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 004291c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004291c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004291c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004291c8 ["COPY", "tmp:0:8", ["const:2f1:8"]]
+ 004291c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004291c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004291c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004291c8 bytes 21e00b91
+ 004291c8 bytes 21c40b91
- 00429200 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 00429200 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429200 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429200 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429200 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 00429200 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429200 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429200 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429200 bytes 21f42091
+ 00429200 bytes 21282391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a41dc80ee1cbfe21bfe4f6bc29dbf66"></a>

### [`00429384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429384.md) → [`00429384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429384.md) FUN_00429384

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004293ac",
      "incomplete_value": true,
      "site": "004293bc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004293ac",
      "incomplete_value": true,
      "site": "004293bc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "004293c0",
      "incomplete_value": true,
      "site": "004293c0",
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
      "definition_site": "004293c0",
      "incomplete_value": true,
      "site": "004293c0",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004293cc",
      "incomplete_value": false,
      "site": "004293d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004293cc",
      "incomplete_value": false,
      "site": "004293d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "004293ac",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "004293b4",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "004293cc",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004293ac",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "004293b4",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "004293cc",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004293a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429384.md#insn-004293a0) · [`004293cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429384.md#insn-004293cc) · [`00429404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429384.md#insn-00429404)
- 新版 [`004293a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429384.md#insn-004293a0) · [`004293cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429384.md#insn-004293cc) · [`00429404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429384.md#insn-00429404)

~~~diff
- 004293a0 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 004293a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004293a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004293a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004293a0 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004293a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004293a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004293a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004293a0 bytes 29291c91
+ 004293a0 bytes 29d91991
- 004293cc ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004293cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004293cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004293cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004293cc ["COPY", "tmp:0:8", ["const:686:8"]]
+ 004293cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004293cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004293cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004293cc bytes 21e41791
+ 004293cc bytes 21181a91
- 00429404 ["COPY", "tmp:0:8", ["const:16f:8"]]
- 00429404 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429404 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429404 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429404 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00429404 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429404 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429404 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429404 bytes 21bc0591
+ 00429404 bytes 21f00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a7d8c47a193e8ce97e601b63f0309e"></a>

### [`0042949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/0042949c.md) → [`0042949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/0042949c.md) FUN_0042949c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004294c4",
      "incomplete_value": true,
      "site": "004294d4",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004294c4",
      "incomplete_value": true,
      "site": "004294d4",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "004294d8",
      "incomplete_value": true,
      "site": "004294d8",
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
      "definition_site": "004294d8",
      "incomplete_value": true,
      "site": "004294d8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004294e4",
      "incomplete_value": false,
      "site": "004294ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004294e4",
      "incomplete_value": false,
      "site": "004294ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "004294c4",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "004294cc",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "004294e4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004294c4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "004294cc",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "004294e4",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004294b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/0042949c.md#insn-004294b8) · [`004294e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/0042949c.md#insn-004294e4) · [`0042951c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/0042949c.md#insn-0042951c)
- 新版 [`004294b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/0042949c.md#insn-004294b8) · [`004294e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/0042949c.md#insn-004294e4) · [`0042951c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/0042949c.md#insn-0042951c)

~~~diff
- 004294b8 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 004294b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004294b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004294b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004294b8 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004294b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004294b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004294b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004294b8 bytes 29291c91
+ 004294b8 bytes 29d91991
- 004294e4 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004294e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004294e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004294e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004294e4 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 004294e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004294e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004294e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004294e4 bytes 21e41791
+ 004294e4 bytes 21181a91
- 0042951c ["COPY", "tmp:0:8", ["const:8dc:8"]]
- 0042951c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042951c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042951c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042951c ["COPY", "tmp:0:8", ["const:969:8"]]
+ 0042951c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042951c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042951c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042951c bytes 21702391
+ 0042951c bytes 21a42591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc9dcc85d1d6f32f65d3d5075661fa5"></a>

### [`004295b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004295b4.md) → [`004295b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004295b4.md) FUN_004295b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004295dc",
      "incomplete_value": true,
      "site": "004295ec",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004295dc",
      "incomplete_value": true,
      "site": "004295ec",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "004295f0",
      "incomplete_value": true,
      "site": "004295f0",
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
      "definition_site": "004295f0",
      "incomplete_value": true,
      "site": "004295f0",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004295fc",
      "incomplete_value": false,
      "site": "00429604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004295fc",
      "incomplete_value": false,
      "site": "00429604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "004295dc",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "004295e4",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "004295fc",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004295dc",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "004295e4",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "004295fc",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004295d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004295b4.md#insn-004295d0) · [`004295fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004295b4.md#insn-004295fc) · [`00429634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004295b4.md#insn-00429634)
- 新版 [`004295d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004295b4.md#insn-004295d0) · [`004295fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004295b4.md#insn-004295fc) · [`00429634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004295b4.md#insn-00429634)

~~~diff
- 004295d0 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 004295d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004295d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004295d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004295d0 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004295d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004295d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004295d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004295d0 bytes 29291c91
+ 004295d0 bytes 29d91991
- 004295fc ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004295fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004295fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004295fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004295fc ["COPY", "tmp:0:8", ["const:686:8"]]
+ 004295fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004295fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004295fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004295fc bytes 21e41791
+ 004295fc bytes 21181a91
- 00429634 ["COPY", "tmp:0:8", ["const:123:8"]]
- 00429634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429634 ["COPY", "tmp:0:8", ["const:11c:8"]]
+ 00429634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429634 bytes 218c0491
+ 00429634 bytes 21700491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d1c2169641c14a802e20709463f1dd9"></a>

### [`004296cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004296cc.md) → [`004296cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md) FUN_004296cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f9cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f9cd4.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`007f9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f9cd4.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004296f4",
      "incomplete_value": true,
      "site": "00429704",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004296f4",
      "incomplete_value": true,
      "site": "00429704",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429708",
      "incomplete_value": true,
      "site": "00429708",
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
      "definition_site": "00429708",
      "incomplete_value": true,
      "site": "00429708",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429714",
      "incomplete_value": false,
      "site": "0042971c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429714",
      "incomplete_value": false,
      "site": "0042971c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "004296f4",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "004296fc",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00429714",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004296f4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "004296fc",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00429714",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004296e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004296cc.md#insn-004296e8) · [`00429714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004296cc.md#insn-00429714) · [`0042974c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004296cc.md#insn-0042974c)
- 新版 [`004296e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md#insn-004296e8) · [`00429714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md#insn-00429714) · [`0042974c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004296cc.md#insn-0042974c)

~~~diff
- 004296e8 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 004296e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004296e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004296e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004296e8 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004296e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004296e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004296e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004296e8 bytes 29291c91
+ 004296e8 bytes 29d91991
- 00429714 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00429714 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429714 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429714 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429714 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00429714 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429714 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429714 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429714 bytes 21e41791
+ 00429714 bytes 21181a91
- 0042974c ["COPY", "tmp:0:8", ["const:721:8"]]
- 0042974c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042974c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042974c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042974c ["COPY", "tmp:0:8", ["const:68d:8"]]
+ 0042974c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042974c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042974c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042974c bytes 21841c91
+ 0042974c bytes 21341a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e167696f7f4facd99f4c7495067be10f"></a>

### [`004297e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004297e4.md) → [`004297e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md) FUN_004297e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007e0354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e0/007e0354.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`007e0354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0354.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042980c",
      "incomplete_value": true,
      "site": "0042981c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042980c",
      "incomplete_value": true,
      "site": "0042981c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429820",
      "incomplete_value": true,
      "site": "00429820",
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
      "definition_site": "00429820",
      "incomplete_value": true,
      "site": "00429820",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042982c",
      "incomplete_value": false,
      "site": "00429834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042982c",
      "incomplete_value": false,
      "site": "00429834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042980c",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00429814",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042982c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042980c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00429814",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042982c",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004297e4.md#insn-00429800) · [`0042982c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004297e4.md#insn-0042982c) · [`00429864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004297e4.md#insn-00429864)
- 新版 [`00429800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md#insn-00429800) · [`0042982c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md#insn-0042982c) · [`00429864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004297e4.md#insn-00429864)

~~~diff
- 00429800 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429800 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429800 bytes 29291c91
+ 00429800 bytes 29d91991
- 0042982c ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042982c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042982c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042982c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042982c ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042982c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042982c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042982c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042982c bytes 21e41791
+ 0042982c bytes 21181a91
- 00429864 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00429864 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429864 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429864 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429864 ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 00429864 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429864 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429864 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429864 bytes 21401791
+ 00429864 bytes 21241791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad4c810b59b3ccf47a3feb822b2cf96e"></a>

### [`004298fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004298fc.md) → [`004298fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004298fc.md) FUN_004298fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00429924",
      "incomplete_value": true,
      "site": "00429934",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429924",
      "incomplete_value": true,
      "site": "00429934",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429938",
      "incomplete_value": true,
      "site": "00429938",
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
      "definition_site": "00429938",
      "incomplete_value": true,
      "site": "00429938",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429944",
      "incomplete_value": false,
      "site": "0042994c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429944",
      "incomplete_value": false,
      "site": "0042994c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00429924",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042992c",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00429944",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429924",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042992c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00429944",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004298fc.md#insn-00429918) · [`00429944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004298fc.md#insn-00429944) · [`0042997c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/004298fc.md#insn-0042997c)
- 新版 [`00429918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004298fc.md#insn-00429918) · [`00429944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004298fc.md#insn-00429944) · [`0042997c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/004298fc.md#insn-0042997c)

~~~diff
- 00429918 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429918 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429918 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429918 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429918 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429918 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429918 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429918 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429918 bytes 29291c91
+ 00429918 bytes 29d91991
- 00429944 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00429944 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429944 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429944 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429944 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00429944 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429944 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429944 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429944 bytes 21e41791
+ 00429944 bytes 21181a91
- 0042997c ["COPY", "tmp:0:8", ["const:aa1:8"]]
- 0042997c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042997c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042997c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042997c ["COPY", "tmp:0:8", ["const:b2e:8"]]
+ 0042997c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042997c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042997c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042997c bytes 21842a91
+ 0042997c bytes 21b82c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b677119a2d355a7ae52e91cbe9ecc03"></a>

### [`00429a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429a14.md) → [`00429a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md) FUN_00429a14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008594d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md) · 呼出先 4件 [`00428714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428714.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`008594d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md) · 呼出先 4件 [`00428714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429a40",
      "incomplete_value": false,
      "site": "00429a48",
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
            "const:335:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429a40",
      "incomplete_value": false,
      "site": "00429a48",
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
            "const:33c:8"
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
      "00429a40",
      "PARAM",
      [
        "storage",
        "002a733c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429a40",
      "PARAM",
      [
        "storage",
        "002a7335",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429a14.md#insn-00429a40)
- 新版 [`00429a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md#insn-00429a40)

~~~diff
- 00429a40 ["COPY", "tmp:0:8", ["const:33c:8"]]
- 00429a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429a40 ["COPY", "tmp:0:8", ["const:335:8"]]
+ 00429a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429a40 bytes 21f00c91
+ 00429a40 bytes 21d40c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0c3227861183b9b7f4add1047559a1"></a>

### [`00429ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ac4.md) → [`00429ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ac4.md) FUN_00429ac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00897400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00897/00897400.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00897400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00897/00897400.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00429aec",
      "incomplete_value": true,
      "site": "00429afc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429aec",
      "incomplete_value": true,
      "site": "00429afc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429b00",
      "incomplete_value": true,
      "site": "00429b00",
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
      "definition_site": "00429b00",
      "incomplete_value": true,
      "site": "00429b00",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429b0c",
      "incomplete_value": false,
      "site": "00429b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429b0c",
      "incomplete_value": false,
      "site": "00429b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00429aec",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00429af4",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00429b0c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429aec",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00429af4",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00429b0c",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ac4.md#insn-00429ae0) · [`00429b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ac4.md#insn-00429b0c) · [`00429b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ac4.md#insn-00429b44)
- 新版 [`00429ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ac4.md#insn-00429ae0) · [`00429b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ac4.md#insn-00429b0c) · [`00429b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ac4.md#insn-00429b44)

~~~diff
- 00429ae0 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429ae0 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429ae0 bytes 29291c91
+ 00429ae0 bytes 29d91991
- 00429b0c ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00429b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429b0c ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00429b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429b0c bytes 21e41791
+ 00429b0c bytes 21181a91
- 00429b44 ["COPY", "tmp:0:8", ["const:2c1:8"]]
- 00429b44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429b44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429b44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429b44 ["COPY", "tmp:0:8", ["const:22d:8"]]
+ 00429b44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429b44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429b44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429b44 bytes 21040b91
+ 00429b44 bytes 21b40891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b6c07bc2d36194625105ecb9389db0"></a>

### [`00429bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429bdc.md) → [`00429bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429bdc.md) FUN_00429bdc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e10dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e1/009e10dc.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`009e10dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e10dc.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00429c08",
      "incomplete_value": true,
      "site": "00429c1c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429c08",
      "incomplete_value": true,
      "site": "00429c1c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429c20",
      "incomplete_value": true,
      "site": "00429c20",
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
      "definition_site": "00429c20",
      "incomplete_value": true,
      "site": "00429c20",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429c2c",
      "incomplete_value": false,
      "site": "00429c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429c2c",
      "incomplete_value": false,
      "site": "00429c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00429c08",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00429c14",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00429c2c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429c08",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00429c14",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00429c2c",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429bdc.md#insn-00429bfc) · [`00429c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429bdc.md#insn-00429c2c) · [`00429c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429bdc.md#insn-00429c64)
- 新版 [`00429bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429bdc.md#insn-00429bfc) · [`00429c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429bdc.md#insn-00429c2c) · [`00429c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429bdc.md#insn-00429c64)

~~~diff
- 00429bfc ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429bfc ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429bfc bytes 29291c91
+ 00429bfc bytes 29d91991
- 00429c2c ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00429c2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429c2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429c2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429c2c ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00429c2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429c2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429c2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429c2c bytes 21e41791
+ 00429c2c bytes 21181a91
- 00429c64 ["COPY", "tmp:0:8", ["const:125:8"]]
- 00429c64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429c64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429c64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429c64 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00429c64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429c64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429c64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429c64 bytes 21940491
+ 00429c64 bytes 21c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1f3d9491c173a860762feff7225e7c"></a>

### [`00429de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429de8.md) → [`00429de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429de8.md) FUN_00429de8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) [`009e10dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e1/009e10dc.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`009e10dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e10dc.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00429e14",
      "incomplete_value": true,
      "site": "00429e28",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429e14",
      "incomplete_value": true,
      "site": "00429e28",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "00429e2c",
      "incomplete_value": true,
      "site": "00429e2c",
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
      "definition_site": "00429e2c",
      "incomplete_value": true,
      "site": "00429e2c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00429e38",
      "incomplete_value": false,
      "site": "00429e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429e38",
      "incomplete_value": false,
      "site": "00429e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "00429e14",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00429e20",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00429e38",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00429e14",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00429e20",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00429e38",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429de8.md#insn-00429e08) · [`00429e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429de8.md#insn-00429e38) · [`00429e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429de8.md#insn-00429e70)
- 新版 [`00429e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429de8.md#insn-00429e08) · [`00429e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429de8.md#insn-00429e38) · [`00429e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429de8.md#insn-00429e70)

~~~diff
- 00429e08 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00429e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00429e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00429e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00429e08 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00429e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00429e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00429e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00429e08 bytes 29291c91
+ 00429e08 bytes 29d91991
- 00429e38 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00429e38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429e38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429e38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429e38 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00429e38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429e38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429e38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429e38 bytes 21e41791
+ 00429e38 bytes 21181a91
- 00429e70 ["COPY", "tmp:0:8", ["const:55e:8"]]
- 00429e70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00429e70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00429e70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00429e70 ["COPY", "tmp:0:8", ["const:5eb:8"]]
+ 00429e70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00429e70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00429e70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00429e70 bytes 21781591
+ 00429e70 bytes 21ac1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf55a194d91cdc8b44f90d881e8f401d"></a>

### [`00429ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ff4.md) → [`00429ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ff4.md) FUN_00429ff4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.55% / 新版 92.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a020",
      "incomplete_value": true,
      "site": "0042a034",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a020",
      "incomplete_value": true,
      "site": "0042a034",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a038",
      "incomplete_value": true,
      "site": "0042a038",
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
      "definition_site": "0042a038",
      "incomplete_value": true,
      "site": "0042a038",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a044",
      "incomplete_value": false,
      "site": "0042a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a044",
      "incomplete_value": false,
      "site": "0042a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a020",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a02c",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a044",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a020",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a02c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a044",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ff4.md#insn-0042a014) · [`0042a044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ff4.md#insn-0042a044) · [`0042a0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429ff4.md#insn-0042a0dc)
- 新版 [`0042a014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ff4.md#insn-0042a014) · [`0042a044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ff4.md#insn-0042a044) · [`0042a0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429ff4.md#insn-0042a0dc)

~~~diff
- 0042a014 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042a014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042a014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042a014 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042a014 bytes 29291c91
+ 0042a014 bytes 29d91991
- 0042a044 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a044 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a044 bytes 21e41791
+ 0042a044 bytes 21181a91
- 0042a0dc ["COPY", "tmp:0:8", ["const:11d:8"]]
- 0042a0dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a0dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a0dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a0dc ["COPY", "tmp:0:8", ["const:116:8"]]
+ 0042a0dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a0dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a0dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a0dc bytes 21740491
+ 0042a0dc bytes 21580491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05dd6d81ca7e55ce08e6237e2bc54c9b"></a>

### [`0042a200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a200.md) → [`0042a200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a200.md) FUN_0042a200

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.55% / 新版 92.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a22c",
      "incomplete_value": true,
      "site": "0042a240",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a22c",
      "incomplete_value": true,
      "site": "0042a240",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a244",
      "incomplete_value": true,
      "site": "0042a244",
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
      "definition_site": "0042a244",
      "incomplete_value": true,
      "site": "0042a244",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a250",
      "incomplete_value": false,
      "site": "0042a258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a250",
      "incomplete_value": false,
      "site": "0042a258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a22c",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a238",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a250",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a22c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a238",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a250",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a200.md#insn-0042a220) · [`0042a250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a200.md#insn-0042a250) · [`0042a2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a200.md#insn-0042a2e8)
- 新版 [`0042a220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a200.md#insn-0042a220) · [`0042a250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a200.md#insn-0042a250) · [`0042a2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a200.md#insn-0042a2e8)

~~~diff
- 0042a220 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042a220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042a220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042a220 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042a220 bytes 29291c91
+ 0042a220 bytes 29d91991
- 0042a250 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a250 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a250 bytes 21e41791
+ 0042a250 bytes 21181a91
- 0042a2e8 ["COPY", "tmp:0:8", ["const:11d:8"]]
- 0042a2e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a2e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a2e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a2e8 ["COPY", "tmp:0:8", ["const:116:8"]]
+ 0042a2e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a2e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a2e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a2e8 bytes 21740491
+ 0042a2e8 bytes 21580491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa404c5a24f3cbe73e2900d574f18350"></a>

### [`0042a40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a40c.md) → [`0042a40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a40c.md) FUN_0042a40c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e6014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e6014.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008e6014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e6014.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a444",
      "incomplete_value": true,
      "site": "0042a458",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a444",
      "incomplete_value": true,
      "site": "0042a458",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a45c",
      "incomplete_value": true,
      "site": "0042a45c",
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
      "definition_site": "0042a45c",
      "incomplete_value": true,
      "site": "0042a45c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a464",
      "incomplete_value": false,
      "site": "0042a46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a464",
      "incomplete_value": false,
      "site": "0042a46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a444",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a448",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a464",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a444",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a448",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a464",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a40c.md#insn-0042a440) · [`0042a464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a40c.md#insn-0042a464) · [`0042a49c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a40c.md#insn-0042a49c)
- 新版 [`0042a440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a40c.md#insn-0042a440) · [`0042a464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a40c.md#insn-0042a464) · [`0042a49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a40c.md#insn-0042a49c)

~~~diff
- 0042a440 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042a440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042a440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042a440 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042a440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042a440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042a440 bytes 08291c91
+ 0042a440 bytes 08d91991
- 0042a464 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a464 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a464 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a464 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a464 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a464 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a464 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a464 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a464 bytes 21e41791
+ 0042a464 bytes 21181a91
- 0042a49c ["COPY", "tmp:0:8", ["const:104:8"]]
- 0042a49c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a49c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a49c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a49c ["COPY", "tmp:0:8", ["const:70:8"]]
+ 0042a49c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a49c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a49c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a49c bytes 21100491
+ 0042a49c bytes 21c00191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67cdff8df71df18db0596c5cda09042a"></a>

### [`0042a700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a700.md) → [`0042a700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a700.md) FUN_0042a700

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a728",
      "incomplete_value": true,
      "site": "0042a738",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a728",
      "incomplete_value": true,
      "site": "0042a738",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a73c",
      "incomplete_value": true,
      "site": "0042a73c",
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
      "definition_site": "0042a73c",
      "incomplete_value": true,
      "site": "0042a73c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a748",
      "incomplete_value": false,
      "site": "0042a750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a748",
      "incomplete_value": false,
      "site": "0042a750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a728",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a730",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a748",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a728",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a730",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a748",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a700.md#insn-0042a71c) · [`0042a748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a700.md#insn-0042a748) · [`0042a780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a700.md#insn-0042a780)
- 新版 [`0042a71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a700.md#insn-0042a71c) · [`0042a748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a700.md#insn-0042a748) · [`0042a780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a700.md#insn-0042a780)

~~~diff
- 0042a71c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a71c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042a71c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042a71c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042a71c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a71c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a71c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a71c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042a71c bytes 29291c91
+ 0042a71c bytes 29d91991
- 0042a748 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a748 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a748 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a748 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a748 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a748 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a748 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a748 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a748 bytes 21e41791
+ 0042a748 bytes 21181a91
- 0042a780 ["COPY", "tmp:0:8", ["const:8f9:8"]]
- 0042a780 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a780 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a780 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a780 ["COPY", "tmp:0:8", ["const:986:8"]]
+ 0042a780 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a780 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a780 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a780 bytes 21e42391
+ 0042a780 bytes 21182691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72986f6a0c39ad4ce35d02df7dc0f01c"></a>

### [`0042a818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a818.md) → [`0042a818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a818.md) FUN_0042a818

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a840",
      "incomplete_value": true,
      "site": "0042a850",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a840",
      "incomplete_value": true,
      "site": "0042a850",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a854",
      "incomplete_value": true,
      "site": "0042a854",
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
      "definition_site": "0042a854",
      "incomplete_value": true,
      "site": "0042a854",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a860",
      "incomplete_value": false,
      "site": "0042a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a860",
      "incomplete_value": false,
      "site": "0042a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a840",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a848",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a860",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a840",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a848",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a860",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a818.md#insn-0042a834) · [`0042a860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a818.md#insn-0042a860) · [`0042a898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a818.md#insn-0042a898)
- 新版 [`0042a834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a818.md#insn-0042a834) · [`0042a860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a818.md#insn-0042a860) · [`0042a898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a818.md#insn-0042a898)

~~~diff
- 0042a834 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042a834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042a834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042a834 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042a834 bytes 29291c91
+ 0042a834 bytes 29d91991
- 0042a860 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a860 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a860 bytes 21e41791
+ 0042a860 bytes 21181a91
- 0042a898 ["COPY", "tmp:0:8", ["const:23b:8"]]
- 0042a898 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a898 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a898 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a898 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0042a898 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a898 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a898 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a898 bytes 21ec0891
+ 0042a898 bytes 21200b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53dcf47c24536eecc3bb64b4cd27d29"></a>

### [`0042a930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a930.md) → [`0042a930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a930.md) FUN_0042a930

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042a958",
      "incomplete_value": true,
      "site": "0042a968",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a958",
      "incomplete_value": true,
      "site": "0042a968",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042a96c",
      "incomplete_value": true,
      "site": "0042a96c",
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
      "definition_site": "0042a96c",
      "incomplete_value": true,
      "site": "0042a96c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042a978",
      "incomplete_value": false,
      "site": "0042a980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a978",
      "incomplete_value": false,
      "site": "0042a980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042a958",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042a960",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042a978",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042a958",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042a960",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042a978",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a930.md#insn-0042a94c) · [`0042a978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a930.md#insn-0042a978) · [`0042a9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042a930.md#insn-0042a9b0)
- 新版 [`0042a94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a930.md#insn-0042a94c) · [`0042a978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a930.md#insn-0042a978) · [`0042a9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042a930.md#insn-0042a9b0)

~~~diff
- 0042a94c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042a94c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042a94c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042a94c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042a94c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042a94c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a94c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042a94c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042a94c bytes 29291c91
+ 0042a94c bytes 29d91991
- 0042a978 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042a978 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a978 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a978 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a978 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042a978 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a978 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a978 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a978 bytes 21e41791
+ 0042a978 bytes 21181a91
- 0042a9b0 ["COPY", "tmp:0:8", ["const:2d3:8"]]
- 0042a9b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042a9b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042a9b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042a9b0 ["COPY", "tmp:0:8", ["const:23f:8"]]
+ 0042a9b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a9b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042a9b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042a9b0 bytes 214c0b91
+ 0042a9b0 bytes 21fc0891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9902a56bedbc0080737d6ebaea5685b0"></a>

### [`0042aa48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aa48.md) → [`0042aa48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aa48.md) FUN_0042aa48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a2308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a2/005a2308.md) [`00a17ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042aa70",
      "incomplete_value": true,
      "site": "0042aa80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aa70",
      "incomplete_value": true,
      "site": "0042aa80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042aa84",
      "incomplete_value": true,
      "site": "0042aa84",
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
      "definition_site": "0042aa84",
      "incomplete_value": true,
      "site": "0042aa84",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042aa90",
      "incomplete_value": false,
      "site": "0042aa98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aa90",
      "incomplete_value": false,
      "site": "0042aa98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042aa70",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042aa78",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042aa90",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042aa70",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042aa78",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042aa90",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042aa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aa48.md#insn-0042aa64) · [`0042aa90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aa48.md#insn-0042aa90) · [`0042aac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aa48.md#insn-0042aac8)
- 新版 [`0042aa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aa48.md#insn-0042aa64) · [`0042aa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aa48.md#insn-0042aa90) · [`0042aac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aa48.md#insn-0042aac8)

~~~diff
- 0042aa64 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042aa64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042aa64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042aa64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042aa64 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042aa64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042aa64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042aa64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042aa64 bytes 29291c91
+ 0042aa64 bytes 29d91991
- 0042aa90 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042aa90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042aa90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042aa90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042aa90 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042aa90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aa90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aa90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042aa90 bytes 21e41791
+ 0042aa90 bytes 21181a91
- 0042aac8 ["COPY", "tmp:0:8", ["const:132:8"]]
- 0042aac8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042aac8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042aac8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042aac8 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0042aac8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aac8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aac8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042aac8 bytes 21c80491
+ 0042aac8 bytes 21fc0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74e5e5ab07e65d3778300ec807b73f0"></a>

### [`0042ab60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ab60.md) → [`0042ab60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ab60.md) FUN_0042ab60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0089f1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0089f/0089f1c4.md) [`008a5bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`0089f1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089f/0089f1c4.md) [`008a5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bd0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042ab88",
      "incomplete_value": true,
      "site": "0042ab98",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ab88",
      "incomplete_value": true,
      "site": "0042ab98",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042ab9c",
      "incomplete_value": true,
      "site": "0042ab9c",
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
      "definition_site": "0042ab9c",
      "incomplete_value": true,
      "site": "0042ab9c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042aba8",
      "incomplete_value": false,
      "site": "0042abb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aba8",
      "incomplete_value": false,
      "site": "0042abb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042ab88",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042ab90",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042aba8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042ab88",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042ab90",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042aba8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ab7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ab60.md#insn-0042ab7c) · [`0042aba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ab60.md#insn-0042aba8) · [`0042abe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ab60.md#insn-0042abe0)
- 新版 [`0042ab7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ab60.md#insn-0042ab7c) · [`0042aba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ab60.md#insn-0042aba8) · [`0042abe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ab60.md#insn-0042abe0)

~~~diff
- 0042ab7c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042ab7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042ab7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042ab7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042ab7c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042ab7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042ab7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042ab7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042ab7c bytes 29291c91
+ 0042ab7c bytes 29d91991
- 0042aba8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042aba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042aba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042aba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042aba8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042aba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042aba8 bytes 21e41791
+ 0042aba8 bytes 21181a91
- 0042abe0 ["COPY", "tmp:0:8", ["const:13f:8"]]
- 0042abe0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042abe0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042abe0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042abe0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0042abe0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042abe0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042abe0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042abe0 bytes 21fc0491
+ 0042abe0 bytes 21e00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be85d43c4e484febae08453ef38bb87d"></a>

### [`0042ac78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ac78.md) → [`0042ac78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ac78.md) FUN_0042ac78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00632468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00632/00632468.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00632468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632468.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042aca0",
      "incomplete_value": true,
      "site": "0042acb0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aca0",
      "incomplete_value": true,
      "site": "0042acb0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042acb4",
      "incomplete_value": true,
      "site": "0042acb4",
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
      "definition_site": "0042acb4",
      "incomplete_value": true,
      "site": "0042acb4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042acc0",
      "incomplete_value": false,
      "site": "0042acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042acc0",
      "incomplete_value": false,
      "site": "0042acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042aca0",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042aca8",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042acc0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042aca0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042aca8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042acc0",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ac94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ac78.md#insn-0042ac94) · [`0042acc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ac78.md#insn-0042acc0) · [`0042acf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ac78.md#insn-0042acf8)
- 新版 [`0042ac94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ac78.md#insn-0042ac94) · [`0042acc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ac78.md#insn-0042acc0) · [`0042acf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ac78.md#insn-0042acf8)

~~~diff
- 0042ac94 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042ac94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042ac94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042ac94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042ac94 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042ac94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042ac94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042ac94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042ac94 bytes 29291c91
+ 0042ac94 bytes 29d91991
- 0042acc0 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042acc0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042acc0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042acc0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042acc0 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042acc0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042acc0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042acc0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042acc0 bytes 21e41791
+ 0042acc0 bytes 21181a91
- 0042acf8 ["COPY", "tmp:0:8", ["const:2f3:8"]]
- 0042acf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042acf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042acf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042acf8 ["COPY", "tmp:0:8", ["const:25f:8"]]
+ 0042acf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042acf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042acf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042acf8 bytes 21cc0b91
+ 0042acf8 bytes 217c0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a66c053b765b8de2141371a4ab33ed4e"></a>

### [`0042ad90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ad90.md) → [`0042ad90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ad90.md) FUN_0042ad90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00629194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00629/00629194.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042adb8",
      "incomplete_value": true,
      "site": "0042adc8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042adb8",
      "incomplete_value": true,
      "site": "0042adc8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042adcc",
      "incomplete_value": true,
      "site": "0042adcc",
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
      "definition_site": "0042adcc",
      "incomplete_value": true,
      "site": "0042adcc",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042add8",
      "incomplete_value": false,
      "site": "0042ade0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042add8",
      "incomplete_value": false,
      "site": "0042ade0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042adb8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042adc0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042add8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042adb8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042adc0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042add8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042adac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ad90.md#insn-0042adac) · [`0042add8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ad90.md#insn-0042add8) · [`0042ae10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ad90.md#insn-0042ae10)
- 新版 [`0042adac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ad90.md#insn-0042adac) · [`0042add8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ad90.md#insn-0042add8) · [`0042ae10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ad90.md#insn-0042ae10)

~~~diff
- 0042adac ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042adac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042adac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042adac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042adac ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042adac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042adac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042adac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042adac bytes 29291c91
+ 0042adac bytes 29d91991
- 0042add8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042add8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042add8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042add8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042add8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042add8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042add8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042add8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042add8 bytes 21e41791
+ 0042add8 bytes 21181a91
- 0042ae10 ["COPY", "tmp:0:8", ["const:1e2:8"]]
- 0042ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042ae10 ["COPY", "tmp:0:8", ["const:26f:8"]]
+ 0042ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042ae10 bytes 21880791
+ 0042ae10 bytes 21bc0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ea96578369ab0c448e01f0d8cfdaf90"></a>

### [`0042aea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aea8.md) → [`0042aea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md) FUN_0042aea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083d5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md) [`008629ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`0083d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md) [`008629ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042aed0",
      "incomplete_value": true,
      "site": "0042aee0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aed0",
      "incomplete_value": true,
      "site": "0042aee0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042aee4",
      "incomplete_value": true,
      "site": "0042aee4",
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
      "definition_site": "0042aee4",
      "incomplete_value": true,
      "site": "0042aee4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042aef0",
      "incomplete_value": false,
      "site": "0042aef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aef0",
      "incomplete_value": false,
      "site": "0042aef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042aed0",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042aed8",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042aef0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042aed0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042aed8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042aef0",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042aec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aea8.md#insn-0042aec4) · [`0042aef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aea8.md#insn-0042aef0) · [`0042af28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aea8.md#insn-0042af28)
- 新版 [`0042aec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md#insn-0042aec4) · [`0042aef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md#insn-0042aef0) · [`0042af28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md#insn-0042af28)

~~~diff
- 0042aec4 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042aec4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042aec4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042aec4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042aec4 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042aec4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042aec4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042aec4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042aec4 bytes 29291c91
+ 0042aec4 bytes 29d91991
- 0042aef0 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042aef0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042aef0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042aef0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042aef0 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042aef0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aef0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042aef0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042aef0 bytes 21e41791
+ 0042aef0 bytes 21181a91
- 0042af28 ["COPY", "tmp:0:8", ["const:90c:8"]]
- 0042af28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042af28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042af28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042af28 ["COPY", "tmp:0:8", ["const:999:8"]]
+ 0042af28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042af28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042af28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042af28 bytes 21302491
+ 0042af28 bytes 21642691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef4c75db1080062f1f2ac31e123878e0"></a>

### [`0042afc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042afc0.md) → [`0042afc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042afc0.md) FUN_0042afc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042afe8",
      "incomplete_value": true,
      "site": "0042aff8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042afe8",
      "incomplete_value": true,
      "site": "0042aff8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042affc",
      "incomplete_value": true,
      "site": "0042affc",
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
      "definition_site": "0042affc",
      "incomplete_value": true,
      "site": "0042affc",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b008",
      "incomplete_value": false,
      "site": "0042b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b008",
      "incomplete_value": false,
      "site": "0042b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042afe8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042aff0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b008",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042afe8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042aff0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b008",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042afdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042afc0.md#insn-0042afdc) · [`0042b008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042afc0.md#insn-0042b008) · [`0042b040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042afc0.md#insn-0042b040)
- 新版 [`0042afdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042afc0.md#insn-0042afdc) · [`0042b008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042afc0.md#insn-0042b008) · [`0042b040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042afc0.md#insn-0042b040)

~~~diff
- 0042afdc ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042afdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042afdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042afdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042afdc ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042afdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042afdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042afdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042afdc bytes 29291c91
+ 0042afdc bytes 29d91991
- 0042b008 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b008 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b008 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b008 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b008 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b008 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b008 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b008 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b008 bytes 21e41791
+ 0042b008 bytes 21181a91
- 0042b040 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 0042b040 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b040 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b040 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b040 ["COPY", "tmp:0:8", ["const:775:8"]]
+ 0042b040 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b040 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b040 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b040 bytes 21a01b91
+ 0042b040 bytes 21d41d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68457f22d7d5a83bbaf652cd726b543f"></a>

### [`0042b0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b0d8.md) → [`0042b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b0d8.md) FUN_0042b0d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b100",
      "incomplete_value": true,
      "site": "0042b110",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b100",
      "incomplete_value": true,
      "site": "0042b110",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b114",
      "incomplete_value": true,
      "site": "0042b114",
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
      "definition_site": "0042b114",
      "incomplete_value": true,
      "site": "0042b114",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b120",
      "incomplete_value": false,
      "site": "0042b128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b120",
      "incomplete_value": false,
      "site": "0042b128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b100",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b108",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b120",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b100",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b108",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b120",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b0d8.md#insn-0042b0f4) · [`0042b120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b0d8.md#insn-0042b120) · [`0042b158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b0d8.md#insn-0042b158)
- 新版 [`0042b0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b0d8.md#insn-0042b0f4) · [`0042b120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b0d8.md#insn-0042b120) · [`0042b158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b0d8.md#insn-0042b158)

~~~diff
- 0042b0f4 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b0f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b0f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b0f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b0f4 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b0f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b0f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b0f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b0f4 bytes 29291c91
+ 0042b0f4 bytes 29d91991
- 0042b120 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b120 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b120 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b120 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b120 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b120 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b120 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b120 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b120 bytes 21e41791
+ 0042b120 bytes 21181a91
- 0042b158 ["COPY", "tmp:0:8", ["const:183:8"]]
- 0042b158 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b158 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b158 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b158 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0042b158 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b158 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b158 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b158 bytes 210c0691
+ 0042b158 bytes 21400891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af1af8cb444eeea5f837694c7166d99"></a>

### [`0042b1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b1f0.md) → [`0042b1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b1f0.md) FUN_0042b1f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b218",
      "incomplete_value": true,
      "site": "0042b228",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b218",
      "incomplete_value": true,
      "site": "0042b228",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b22c",
      "incomplete_value": true,
      "site": "0042b22c",
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
      "definition_site": "0042b22c",
      "incomplete_value": true,
      "site": "0042b22c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b238",
      "incomplete_value": false,
      "site": "0042b240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b238",
      "incomplete_value": false,
      "site": "0042b240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b218",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b220",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b238",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b218",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b220",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b238",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b20c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b1f0.md#insn-0042b20c) · [`0042b238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b1f0.md#insn-0042b238) · [`0042b270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b1f0.md#insn-0042b270)
- 新版 [`0042b20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b1f0.md#insn-0042b20c) · [`0042b238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b1f0.md#insn-0042b238) · [`0042b270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b1f0.md#insn-0042b270)

~~~diff
- 0042b20c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b20c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b20c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b20c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b20c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b20c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b20c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b20c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b20c bytes 29291c91
+ 0042b20c bytes 29d91991
- 0042b238 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b238 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b238 bytes 21e41791
+ 0042b238 bytes 21181a91
- 0042b270 ["COPY", "tmp:0:8", ["const:c07:8"]]
- 0042b270 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b270 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b270 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b270 ["COPY", "tmp:0:8", ["const:c94:8"]]
+ 0042b270 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b270 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b270 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b270 bytes 211c3091
+ 0042b270 bytes 21503291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7e79ece6657faa10c62d64c1e08dab"></a>

### [`0042b308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b308.md) → [`0042b308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b308.md) FUN_0042b308

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b330",
      "incomplete_value": true,
      "site": "0042b340",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b330",
      "incomplete_value": true,
      "site": "0042b340",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b344",
      "incomplete_value": true,
      "site": "0042b344",
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
      "definition_site": "0042b344",
      "incomplete_value": true,
      "site": "0042b344",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b350",
      "incomplete_value": false,
      "site": "0042b358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b350",
      "incomplete_value": false,
      "site": "0042b358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b330",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b338",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b350",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b330",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b338",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b350",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b308.md#insn-0042b324) · [`0042b350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b308.md#insn-0042b350)
- 新版 [`0042b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b308.md#insn-0042b324) · [`0042b350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b308.md#insn-0042b350)

~~~diff
- 0042b324 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b324 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b324 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b324 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b324 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b324 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b324 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b324 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b324 bytes 29291c91
+ 0042b324 bytes 29d91991
- 0042b350 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b350 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b350 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b350 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b350 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b350 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b350 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b350 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b350 bytes 21e41791
+ 0042b350 bytes 21181a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683fdff313b3e6e4d83dd3f8c9fa8eb3"></a>

### [`0042b420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b420.md) → [`0042b420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b420.md) FUN_0042b420

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b448",
      "incomplete_value": true,
      "site": "0042b458",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b448",
      "incomplete_value": true,
      "site": "0042b458",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b45c",
      "incomplete_value": true,
      "site": "0042b45c",
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
      "definition_site": "0042b45c",
      "incomplete_value": true,
      "site": "0042b45c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b468",
      "incomplete_value": false,
      "site": "0042b470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b468",
      "incomplete_value": false,
      "site": "0042b470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b448",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b450",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b468",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b448",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b450",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b468",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b420.md#insn-0042b43c) · [`0042b468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b420.md#insn-0042b468)
- 新版 [`0042b43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b420.md#insn-0042b43c) · [`0042b468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b420.md#insn-0042b468)

~~~diff
- 0042b43c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b43c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b43c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b43c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b43c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b43c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b43c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b43c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b43c bytes 29291c91
+ 0042b43c bytes 29d91991
- 0042b468 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b468 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b468 bytes 21e41791
+ 0042b468 bytes 21181a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f0276522f1545bfdcf03b45b46988a9"></a>

### [`0042b538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b538.md) → [`0042b538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b538.md) FUN_0042b538

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b560",
      "incomplete_value": true,
      "site": "0042b570",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b560",
      "incomplete_value": true,
      "site": "0042b570",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b574",
      "incomplete_value": true,
      "site": "0042b574",
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
      "definition_site": "0042b574",
      "incomplete_value": true,
      "site": "0042b574",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b580",
      "incomplete_value": false,
      "site": "0042b588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b580",
      "incomplete_value": false,
      "site": "0042b588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b560",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b568",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b580",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b560",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b568",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b580",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b538.md#insn-0042b554) · [`0042b580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b538.md#insn-0042b580) · [`0042b5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b538.md#insn-0042b5b8)
- 新版 [`0042b554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b538.md#insn-0042b554) · [`0042b580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b538.md#insn-0042b580) · [`0042b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b538.md#insn-0042b5b8)

~~~diff
- 0042b554 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b554 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b554 bytes 29291c91
+ 0042b554 bytes 29d91991
- 0042b580 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b580 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b580 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b580 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b580 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b580 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b580 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b580 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b580 bytes 21e41791
+ 0042b580 bytes 21181a91
- 0042b5b8 ["COPY", "tmp:0:8", ["const:34d:8"]]
- 0042b5b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b5b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b5b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b5b8 ["COPY", "tmp:0:8", ["const:346:8"]]
+ 0042b5b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b5b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b5b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b5b8 bytes 21340d91
+ 0042b5b8 bytes 21180d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f51959dba5e6573c2dba8d93ab9e2f8c"></a>

### [`0042b650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b650.md) → [`0042b650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b650.md) FUN_0042b650

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b678",
      "incomplete_value": true,
      "site": "0042b688",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b678",
      "incomplete_value": true,
      "site": "0042b688",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b68c",
      "incomplete_value": true,
      "site": "0042b68c",
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
      "definition_site": "0042b68c",
      "incomplete_value": true,
      "site": "0042b68c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b698",
      "incomplete_value": false,
      "site": "0042b6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b698",
      "incomplete_value": false,
      "site": "0042b6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b678",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b680",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b698",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b678",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b680",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b698",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b66c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b650.md#insn-0042b66c) · [`0042b698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b650.md#insn-0042b698) · [`0042b6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b650.md#insn-0042b6d0)
- 新版 [`0042b66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b650.md#insn-0042b66c) · [`0042b698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b650.md#insn-0042b698) · [`0042b6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b650.md#insn-0042b6d0)

~~~diff
- 0042b66c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b66c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b66c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b66c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b66c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b66c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b66c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b66c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b66c bytes 29291c91
+ 0042b66c bytes 29d91991
- 0042b698 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b698 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b698 bytes 21e41791
+ 0042b698 bytes 21181a91
- 0042b6d0 ["COPY", "tmp:0:8", ["const:1d7:8"]]
- 0042b6d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b6d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b6d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b6d0 ["COPY", "tmp:0:8", ["const:264:8"]]
+ 0042b6d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b6d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b6d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b6d0 bytes 215c0791
+ 0042b6d0 bytes 21900991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c44443fd2271f2b587c7693fae5cfd6f"></a>

### [`0042b768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b768.md) → [`0042b768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b768.md) FUN_0042b768

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a62704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62704.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00a62704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62704.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b790",
      "incomplete_value": true,
      "site": "0042b7a0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b790",
      "incomplete_value": true,
      "site": "0042b7a0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b7a4",
      "incomplete_value": true,
      "site": "0042b7a4",
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
      "definition_site": "0042b7a4",
      "incomplete_value": true,
      "site": "0042b7a4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b7b0",
      "incomplete_value": false,
      "site": "0042b7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b7b0",
      "incomplete_value": false,
      "site": "0042b7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b790",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b798",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b7b0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b790",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b798",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b7b0",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b768.md#insn-0042b784) · [`0042b7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b768.md#insn-0042b7b0) · [`0042b7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b768.md#insn-0042b7e8)
- 新版 [`0042b784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b768.md#insn-0042b784) · [`0042b7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b768.md#insn-0042b7b0) · [`0042b7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b768.md#insn-0042b7e8)

~~~diff
- 0042b784 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b784 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b784 bytes 29291c91
+ 0042b784 bytes 29d91991
- 0042b7b0 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b7b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b7b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b7b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b7b0 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b7b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b7b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b7b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b7b0 bytes 21e41791
+ 0042b7b0 bytes 21181a91
- 0042b7e8 ["COPY", "tmp:0:8", ["const:10c:8"]]
- 0042b7e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b7e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b7e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b7e8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0042b7e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b7e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b7e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b7e8 bytes 21300491
+ 0042b7e8 bytes 21e00191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6212ddd8998978778cf5442d5046fd32"></a>

### [`0042b880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b880.md) → [`0042b880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b880.md) FUN_0042b880

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b8a8",
      "incomplete_value": true,
      "site": "0042b8b8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b8a8",
      "incomplete_value": true,
      "site": "0042b8b8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b8bc",
      "incomplete_value": true,
      "site": "0042b8bc",
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
      "definition_site": "0042b8bc",
      "incomplete_value": true,
      "site": "0042b8bc",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b8c8",
      "incomplete_value": false,
      "site": "0042b8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b8c8",
      "incomplete_value": false,
      "site": "0042b8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b8a8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b8b0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b8c8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b8a8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b8b0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b8c8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b880.md#insn-0042b89c) · [`0042b8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b880.md#insn-0042b8c8) · [`0042b900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b880.md#insn-0042b900)
- 新版 [`0042b89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b880.md#insn-0042b89c) · [`0042b8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b880.md#insn-0042b8c8) · [`0042b900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b880.md#insn-0042b900)

~~~diff
- 0042b89c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b89c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b89c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b89c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b89c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b89c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b89c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b89c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b89c bytes 29291c91
+ 0042b89c bytes 29d91991
- 0042b8c8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b8c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b8c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b8c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b8c8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b8c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b8c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b8c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b8c8 bytes 21e41791
+ 0042b8c8 bytes 21181a91
- 0042b900 ["COPY", "tmp:0:8", ["const:1f6:8"]]
- 0042b900 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b900 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b900 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b900 ["COPY", "tmp:0:8", ["const:283:8"]]
+ 0042b900 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b900 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b900 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b900 bytes 21d80791
+ 0042b900 bytes 210c0a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8c63b85fcff5b2863f8dbab1b128f00"></a>

### [`0042b998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b998.md) → [`0042b998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b998.md) FUN_0042b998

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042b9c0",
      "incomplete_value": true,
      "site": "0042b9d0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b9c0",
      "incomplete_value": true,
      "site": "0042b9d0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042b9d4",
      "incomplete_value": true,
      "site": "0042b9d4",
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
      "definition_site": "0042b9d4",
      "incomplete_value": true,
      "site": "0042b9d4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042b9e0",
      "incomplete_value": false,
      "site": "0042b9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b9e0",
      "incomplete_value": false,
      "site": "0042b9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042b9c0",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042b9c8",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042b9e0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042b9c0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042b9c8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042b9e0",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b998.md#insn-0042b9b4) · [`0042b9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b998.md#insn-0042b9e0) · [`0042ba18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b998.md#insn-0042ba18)
- 新版 [`0042b9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b998.md#insn-0042b9b4) · [`0042b9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b998.md#insn-0042b9e0) · [`0042ba18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b998.md#insn-0042ba18)

~~~diff
- 0042b9b4 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042b9b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042b9b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042b9b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042b9b4 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042b9b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b9b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042b9b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042b9b4 bytes 29291c91
+ 0042b9b4 bytes 29d91991
- 0042b9e0 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042b9e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042b9e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042b9e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042b9e0 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042b9e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b9e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042b9e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042b9e0 bytes 21e41791
+ 0042b9e0 bytes 21181a91
- 0042ba18 ["COPY", "tmp:0:8", ["const:2fe:8"]]
- 0042ba18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042ba18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042ba18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042ba18 ["COPY", "tmp:0:8", ["const:38b:8"]]
+ 0042ba18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ba18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ba18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042ba18 bytes 21f80b91
+ 0042ba18 bytes 212c0e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004bb7de474c10f46969aff56f15cfde"></a>

### [`0042bab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bab0.md) → [`0042bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md) FUN_0042bab0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`008b266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bad8",
      "incomplete_value": true,
      "site": "0042bae8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bad8",
      "incomplete_value": true,
      "site": "0042bae8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042baec",
      "incomplete_value": true,
      "site": "0042baec",
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
      "definition_site": "0042baec",
      "incomplete_value": true,
      "site": "0042baec",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042baf8",
      "incomplete_value": false,
      "site": "0042bb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042baf8",
      "incomplete_value": false,
      "site": "0042bb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042bad8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042bae0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042baf8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042bad8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042bae0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042baf8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bab0.md#insn-0042bacc) · [`0042baf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bab0.md#insn-0042baf8) · [`0042bb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bab0.md#insn-0042bb30)
- 新版 [`0042bacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md#insn-0042bacc) · [`0042baf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md#insn-0042baf8) · [`0042bb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md#insn-0042bb30)

~~~diff
- 0042bacc ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042bacc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042bacc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042bacc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042bacc ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042bacc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bacc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bacc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042bacc bytes 29291c91
+ 0042bacc bytes 29d91991
- 0042baf8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042baf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042baf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042baf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042baf8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042baf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042baf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042baf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042baf8 bytes 21e41791
+ 0042baf8 bytes 21181a91
- 0042bb30 ["COPY", "tmp:0:8", ["const:617:8"]]
- 0042bb30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bb30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bb30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bb30 ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 0042bb30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bb30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bb30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bb30 bytes 215c1891
+ 0042bb30 bytes 21901a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5559cbe678213f998573842226b60b60"></a>

### [`0042bbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bbc8.md) → [`0042bbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bbc8.md) FUN_0042bbc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00734374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/00734374.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00734374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734374.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bbec",
      "incomplete_value": true,
      "site": "0042bbfc",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:13e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bbec",
      "incomplete_value": true,
      "site": "0042bbfc",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:145:8"
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
      "definition_site": "0042bbec",
      "incomplete_value": true,
      "site": "0042bbfc",
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
      "definition_site": "0042bbec",
      "incomplete_value": true,
      "site": "0042bbfc",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bc00",
      "incomplete_value": true,
      "site": "0042bc04",
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
                "const:1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bc00",
      "incomplete_value": true,
      "site": "0042bc04",
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
                "const:1a:8"
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
      "0042bbec",
      "READ",
      [
        "storage",
        "002a3145",
        null,
        "string"
      ]
    ],
    [
      "0042bbec",
      "READ",
      [
        "storage",
        "002a3155",
        null,
        "string"
      ]
    ],
    [
      "0042bc00",
      "READ",
      [
        "storage",
        "002a315f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042bbec",
      "READ",
      [
        "storage",
        "002a313e",
        null,
        "string"
      ]
    ],
    [
      "0042bbec",
      "READ",
      [
        "storage",
        "002a314e",
        null,
        "string"
      ]
    ],
    [
      "0042bc00",
      "READ",
      [
        "storage",
        "002a3158",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bbc8.md#insn-0042bbe4) · [`0042bbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bbc8.md#insn-0042bbe8)
- 新版 [`0042bbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bbc8.md#insn-0042bbe4) · [`0042bbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bbc8.md#insn-0042bbe8)

~~~diff
- 0042bbe4 ["COPY", "tmp:0:8", ["const:145:8"]]
- 0042bbe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042bbe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042bbe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042bbe4 ["COPY", "tmp:0:8", ["const:13e:8"]]
+ 0042bbe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042bbe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042bbe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042bbe4 bytes 08150591
+ 0042bbe4 bytes 08f90491
- 0042bbe8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0042bbe8 bytes 29f4ffb0
+ 0042bbe8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0042bbe8 bytes 29f4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d0cd3d1f351dd00084f315c338bbc8"></a>

### [`0042bc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bc18.md) → [`0042bc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bc18.md) FUN_0042bc18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bc40",
      "incomplete_value": true,
      "site": "0042bc50",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bc40",
      "incomplete_value": true,
      "site": "0042bc50",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042bc54",
      "incomplete_value": true,
      "site": "0042bc54",
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
      "definition_site": "0042bc54",
      "incomplete_value": true,
      "site": "0042bc54",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042bc60",
      "incomplete_value": false,
      "site": "0042bc68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bc60",
      "incomplete_value": false,
      "site": "0042bc68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042bc40",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042bc48",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042bc60",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042bc40",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042bc48",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042bc60",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bc18.md#insn-0042bc34) · [`0042bc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bc18.md#insn-0042bc60) · [`0042bc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bc18.md#insn-0042bc98)
- 新版 [`0042bc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bc18.md#insn-0042bc34) · [`0042bc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bc18.md#insn-0042bc60) · [`0042bc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bc18.md#insn-0042bc98)

~~~diff
- 0042bc34 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042bc34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042bc34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042bc34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042bc34 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042bc34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bc34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bc34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042bc34 bytes 29291c91
+ 0042bc34 bytes 29d91991
- 0042bc60 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042bc60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bc60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bc60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bc60 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042bc60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bc60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bc60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bc60 bytes 21e41791
+ 0042bc60 bytes 21181a91
- 0042bc98 ["COPY", "tmp:0:8", ["const:629:8"]]
- 0042bc98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bc98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bc98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bc98 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 0042bc98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bc98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bc98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bc98 bytes 21a41891
+ 0042bc98 bytes 21d81a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aee765fe807279b4f6f7d91aac50f82e"></a>

### [`0042bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bd30.md) → [`0042bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bd30.md) FUN_0042bd30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bd58",
      "incomplete_value": true,
      "site": "0042bd68",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bd58",
      "incomplete_value": true,
      "site": "0042bd68",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042bd6c",
      "incomplete_value": true,
      "site": "0042bd6c",
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
      "definition_site": "0042bd6c",
      "incomplete_value": true,
      "site": "0042bd6c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042bd78",
      "incomplete_value": false,
      "site": "0042bd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bd78",
      "incomplete_value": false,
      "site": "0042bd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042bd58",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042bd60",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042bd78",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042bd58",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042bd60",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042bd78",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bd4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bd30.md#insn-0042bd4c) · [`0042bd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bd30.md#insn-0042bd78) · [`0042bdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bd30.md#insn-0042bdb0)
- 新版 [`0042bd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bd30.md#insn-0042bd4c) · [`0042bd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bd30.md#insn-0042bd78) · [`0042bdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bd30.md#insn-0042bdb0)

~~~diff
- 0042bd4c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042bd4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042bd4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042bd4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042bd4c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042bd4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bd4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bd4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042bd4c bytes 29291c91
+ 0042bd4c bytes 29d91991
- 0042bd78 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042bd78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bd78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bd78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bd78 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042bd78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bd78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bd78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bd78 bytes 21e41791
+ 0042bd78 bytes 21181a91
- 0042bdb0 ["COPY", "tmp:0:8", ["const:915:8"]]
- 0042bdb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bdb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bdb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bdb0 ["COPY", "tmp:0:8", ["const:9a2:8"]]
+ 0042bdb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bdb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bdb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bdb0 bytes 21542491
+ 0042bdb0 bytes 21882691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c680f93da205a6a529c6922d712604af"></a>

### [`0042be48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042be48.md) → [`0042be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md) FUN_0042be48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00871a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a6c.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00871a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042be70",
      "incomplete_value": true,
      "site": "0042be80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042be70",
      "incomplete_value": true,
      "site": "0042be80",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042be84",
      "incomplete_value": true,
      "site": "0042be84",
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
      "definition_site": "0042be84",
      "incomplete_value": true,
      "site": "0042be84",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042be90",
      "incomplete_value": false,
      "site": "0042be98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042be90",
      "incomplete_value": false,
      "site": "0042be98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042be70",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042be78",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042be90",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042be70",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042be78",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042be90",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042be64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042be48.md#insn-0042be64) · [`0042be90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042be48.md#insn-0042be90) · [`0042bec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042be48.md#insn-0042bec8)
- 新版 [`0042be64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md#insn-0042be64) · [`0042be90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md#insn-0042be90) · [`0042bec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md#insn-0042bec8)

~~~diff
- 0042be64 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042be64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042be64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042be64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042be64 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042be64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042be64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042be64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042be64 bytes 29291c91
+ 0042be64 bytes 29d91991
- 0042be90 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042be90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042be90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042be90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042be90 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042be90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042be90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042be90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042be90 bytes 21e41791
+ 0042be90 bytes 21181a91
- 0042bec8 ["COPY", "tmp:0:8", ["const:35c:8"]]
- 0042bec8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bec8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bec8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bec8 ["COPY", "tmp:0:8", ["const:355:8"]]
+ 0042bec8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bec8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bec8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bec8 bytes 21700d91
+ 0042bec8 bytes 21540d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e7928e4d276ce41da48ca13c168ea7e"></a>

### [`0042bf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bf64.md) → [`0042bf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bf64.md) FUN_0042bf64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0075900c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075900c.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0075900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075900c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042bf8c",
      "incomplete_value": true,
      "site": "0042bf9c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bf8c",
      "incomplete_value": true,
      "site": "0042bf9c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042bfa0",
      "incomplete_value": true,
      "site": "0042bfa0",
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
      "definition_site": "0042bfa0",
      "incomplete_value": true,
      "site": "0042bfa0",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042bfac",
      "incomplete_value": false,
      "site": "0042bfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bfac",
      "incomplete_value": false,
      "site": "0042bfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042bf8c",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042bf94",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042bfac",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042bf8c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042bf94",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042bfac",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bf64.md#insn-0042bf80) · [`0042bfac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bf64.md#insn-0042bfac)
- 新版 [`0042bf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bf64.md#insn-0042bf80) · [`0042bfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bf64.md#insn-0042bfac)

~~~diff
- 0042bf80 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042bf80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042bf80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042bf80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042bf80 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042bf80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bf80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042bf80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042bf80 bytes 29291c91
+ 0042bf80 bytes 29d91991
- 0042bfac ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042bfac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042bfac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042bfac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042bfac ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042bfac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bfac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042bfac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042bfac bytes 21e41791
+ 0042bfac bytes 21181a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-005aec0683c31919ec3a7c67a118c1c1"></a>

### [`0042c07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md) → [`0042c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md) FUN_0042c07c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`008746c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746c0.md) [`00874958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874958.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 3件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`008746c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746c0.md) [`00874958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874958.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042c0a8",
      "incomplete_value": true,
      "site": "0042c0bc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c0a8",
      "incomplete_value": true,
      "site": "0042c0bc",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042c0c0",
      "incomplete_value": true,
      "site": "0042c0c0",
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
      "definition_site": "0042c0c0",
      "incomplete_value": true,
      "site": "0042c0c0",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042c0cc",
      "incomplete_value": false,
      "site": "0042c0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c0cc",
      "incomplete_value": false,
      "site": "0042c0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042c0a8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042c0b4",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042c0cc",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042c0a8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042c0b4",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042c0cc",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md#insn-0042c09c) · [`0042c0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md#insn-0042c0cc) · [`0042c104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md#insn-0042c104)
- 新版 [`0042c09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md#insn-0042c09c) · [`0042c0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md#insn-0042c0cc) · [`0042c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md#insn-0042c104)

~~~diff
- 0042c09c ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042c09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042c09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042c09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042c09c ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042c09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042c09c bytes 29291c91
+ 0042c09c bytes 29d91991
- 0042c0cc ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042c0cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c0cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c0cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c0cc ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042c0cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c0cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c0cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c0cc bytes 21e41791
+ 0042c0cc bytes 21181a91
- 0042c104 ["COPY", "tmp:0:8", ["const:43f:8"]]
- 0042c104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c104 ["COPY", "tmp:0:8", ["const:445:8"]]
+ 0042c104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c104 bytes 21fc1091
+ 0042c104 bytes 21141191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18104ddff822ef0456a2a419a0354592"></a>

### [`0042c288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c288.md) → [`0042c288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c288.md) FUN_0042c288

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042c2b0",
      "incomplete_value": true,
      "site": "0042c2c0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c2b0",
      "incomplete_value": true,
      "site": "0042c2c0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042c2c4",
      "incomplete_value": true,
      "site": "0042c2c4",
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
      "definition_site": "0042c2c4",
      "incomplete_value": true,
      "site": "0042c2c4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042c2d0",
      "incomplete_value": false,
      "site": "0042c2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c2d0",
      "incomplete_value": false,
      "site": "0042c2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042c2b0",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042c2b8",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042c2d0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042c2b0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042c2b8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042c2d0",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c288.md#insn-0042c2a4) · [`0042c2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c288.md#insn-0042c2d0)
- 新版 [`0042c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c288.md#insn-0042c2a4) · [`0042c2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c288.md#insn-0042c2d0)

~~~diff
- 0042c2a4 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042c2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042c2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042c2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042c2a4 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042c2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042c2a4 bytes 29291c91
+ 0042c2a4 bytes 29d91991
- 0042c2d0 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042c2d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c2d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c2d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c2d0 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042c2d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c2d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c2d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c2d0 bytes 21e41791
+ 0042c2d0 bytes 21181a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca417b3de197cc49389e6a2a56e624d8"></a>

### [`0042c3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c3a0.md) → [`0042c3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c3a0.md) FUN_0042c3a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042c3c8",
      "incomplete_value": true,
      "site": "0042c3d8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c3c8",
      "incomplete_value": true,
      "site": "0042c3d8",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:70a:8"
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
      "definition_site": "0042c3dc",
      "incomplete_value": true,
      "site": "0042c3dc",
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
      "definition_site": "0042c3dc",
      "incomplete_value": true,
      "site": "0042c3dc",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042c3e8",
      "incomplete_value": false,
      "site": "0042c3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c3e8",
      "incomplete_value": false,
      "site": "0042c3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0042c3c8",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "0042c3d0",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "0042c3e8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042c3c8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0042c3d0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0042c3e8",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c3a0.md#insn-0042c3bc) · [`0042c3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c3a0.md#insn-0042c3e8) · [`0042c420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c3a0.md#insn-0042c420)
- 新版 [`0042c3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c3a0.md#insn-0042c3bc) · [`0042c3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c3a0.md#insn-0042c3e8) · [`0042c420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c3a0.md#insn-0042c420)

~~~diff
- 0042c3bc ["COPY", "tmp:0:8", ["const:70a:8"]]
- 0042c3bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042c3bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042c3bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042c3bc ["COPY", "tmp:0:8", ["const:676:8"]]
+ 0042c3bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c3bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042c3bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042c3bc bytes 29291c91
+ 0042c3bc bytes 29d91991
- 0042c3e8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 0042c3e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c3e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c3e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c3e8 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 0042c3e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c3e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c3e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c3e8 bytes 21e41791
+ 0042c3e8 bytes 21181a91
- 0042c420 ["COPY", "tmp:0:8", ["const:306:8"]]
- 0042c420 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c420 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c420 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c420 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 0042c420 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c420 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c420 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c420 bytes 21180c91
+ 0042c420 bytes 21c80991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb8d46d83c49977ab07bbff2c245c6d"></a>

### [`0042c4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c4b8.md) → [`0042c4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c4b8.md) FUN_0042c4b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008446e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/008446e4.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`008446e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008446e4.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042c4e4",
      "incomplete_value": false,
      "site": "0042c4ec",
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
            "const:229:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c4e4",
      "incomplete_value": false,
      "site": "0042c4ec",
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
            "const:19c:8"
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
      "definition_site": "0042c4f4",
      "incomplete_value": false,
      "site": "0042c500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:6a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c4f4",
      "incomplete_value": false,
      "site": "0042c500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
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
      "0042c4e4",
      "PARAM",
      [
        "storage",
        "0029b19c",
        null,
        "string"
      ]
    ],
    [
      "0042c4f4",
      "PARAM",
      [
        "storage",
        "002ae735",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042c4e4",
      "PARAM",
      [
        "storage",
        "0029b229",
        null,
        "string"
      ]
    ],
    [
      "0042c4f4",
      "PARAM",
      [
        "storage",
        "002ae6a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c4b8.md#insn-0042c4e4) · [`0042c4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c4b8.md#insn-0042c4f4)
- 新版 [`0042c4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c4b8.md#insn-0042c4e4) · [`0042c4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c4b8.md#insn-0042c4f4)

~~~diff
- 0042c4e4 ["COPY", "tmp:0:8", ["const:19c:8"]]
- 0042c4e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c4e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c4e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c4e4 ["COPY", "tmp:0:8", ["const:229:8"]]
+ 0042c4e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c4e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c4e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c4e4 bytes 21700691
+ 0042c4e4 bytes 21a40891
- 0042c4f4 ["COPY", "tmp:0:8", ["const:735:8"]]
- 0042c4f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0042c4f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0042c4f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0042c4f4 ["COPY", "tmp:0:8", ["const:6a1:8"]]
+ 0042c4f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0042c4f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0042c4f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0042c4f4 bytes 00d41c91
+ 0042c4f4 bytes 00841a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1782ecf9187566ab2aa68d2f1a0905b3"></a>

### [`0042c564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c564.md) → [`0042c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c564.md) FUN_0042c564

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008446e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/008446e4.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`008446e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008446e4.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

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
      "definition_site": "0042c590",
      "incomplete_value": false,
      "site": "0042c598",
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
            "const:229:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c590",
      "incomplete_value": false,
      "site": "0042c598",
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
            "const:19c:8"
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
      "0042c590",
      "PARAM",
      [
        "storage",
        "0029b19c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042c590",
      "PARAM",
      [
        "storage",
        "0029b229",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c564.md#insn-0042c590)
- 新版 [`0042c590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c564.md#insn-0042c590)

~~~diff
- 0042c590 ["COPY", "tmp:0:8", ["const:19c:8"]]
- 0042c590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042c590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042c590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042c590 ["COPY", "tmp:0:8", ["const:229:8"]]
+ 0042c590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042c590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042c590 bytes 21700691
+ 0042c590 bytes 21a40891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed4858f507b87e094a72640d304215b"></a>

### [`0042c610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c610.md) → [`0042c610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c610.md) _INIT_10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 82.16% / 新版 82.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 7件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042c64c",
      "incomplete_value": true,
      "site": "0042c668",
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
      "definition_site": "0042c64c",
      "incomplete_value": true,
      "site": "0042c668",
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
      "definition_site": "0042c670",
      "incomplete_value": true,
      "site": "0042c68c",
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
      "definition_site": "0042c670",
      "incomplete_value": true,
      "site": "0042c68c",
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
      "definition_site": "0042c690",
      "incomplete_value": true,
      "site": "0042c6ac",
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
      "definition_site": "0042c690",
      "incomplete_value": true,
      "site": "0042c6ac",
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
      "0042c64c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0042c670",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0042c690",
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
      "0042c64c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0042c670",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0042c690",
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

- 旧版 [`0042c848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c610.md#insn-0042c848) · [`0042c63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c610.md#insn-0042c63c)
- 新版 [`0042c848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c610.md#insn-0042c848) · [`0042c63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c610.md#insn-0042c63c)

~~~diff
- 0042c848 ["INT_ADD", "register:40f0:8", ["const:42c848:8", "const:4:8"]]
- 0042c848 ["CALL", null, ["callee:00bdaf90:8"]]
- 0042c848 bytes a6b91e94
+ 0042c848 ["INT_ADD", "register:40f0:8", ["const:42c848:8", "const:4:8"]]
+ 0042c848 ["CALL", null, ["callee:00bdaf90:8"]]
+ 0042c848 bytes d2b91e94
- 0042c63c ["COPY", "tmp:0:8", ["const:a90:8"]]
- 0042c63c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0042c63c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0042c63c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0042c63c ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 0042c63c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0042c63c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0042c63c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0042c63c bytes 73422a91
+ 0042c63c bytes 73422d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8916a7b17ab3fbaa395c6c6c90cac4ad"></a>

### [`0042c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md) → [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) FUN_0042c9c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0083b3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md) [`0083bad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bad8.md) [`00873c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c68.md) [`008740c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740c4.md) [`008742c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008742c4.md) · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 6件 [`0083b3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md) [`0083bad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bad8.md) [`00873c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c68.md) [`008740c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md) [`008742c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008742c4.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "definition_site": "0042c9ec",
      "incomplete_value": false,
      "site": "0042c9f0",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9ec",
      "incomplete_value": false,
      "site": "0042c9f0",
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
            "const:ae0:8"
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
      "definition_site": "0042c9fc",
      "incomplete_value": false,
      "site": "0042ca00",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9fc",
      "incomplete_value": false,
      "site": "0042ca00",
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
            "const:ae0:8"
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
      "definition_site": "0042c9dc",
      "incomplete_value": true,
      "site": "0042c9e4",
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9dc",
      "incomplete_value": true,
      "site": "0042c9e4",
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
                "const:ad8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042c9d0",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042c9dc",
      "READ",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "0042c9ec",
      "PARAM",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042c9d0",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042c9dc",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ],
    [
      "0042c9ec",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md#insn-0042c9cc) · [`0042c9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md#insn-0042c9dc) · [`0042c9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md#insn-0042c9ec)
- 新版 [`0042c9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md#insn-0042c9cc) · [`0042c9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md#insn-0042c9dc) · [`0042c9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md#insn-0042c9ec)

~~~diff
- 0042c9cc ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0042c9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042c9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042c9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042c9cc ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0042c9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042c9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042c9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042c9cc bytes 08812b91
+ 0042c9cc bytes 08812e91
- 0042c9dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad8:8"]]
- 0042c9dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042c9dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
+ 0042c9dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0042c9dc bytes 006d45f9
+ 0042c9dc bytes 00cd45f9
- 0042c9ec ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0042c9ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0042c9ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0042c9ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0042c9ec ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0042c9ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0042c9ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0042c9ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0042c9ec bytes 00802b91
+ 0042c9ec bytes 00802e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d69ec9fb25b35b41e26de2c8d467968b"></a>

### [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) → [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) FUN_0042ca08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 23件 [`004537f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00454/00454af4.md) [`00576eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576eec.md) [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`00770bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00770/00770bfc.md) · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 23件 [`004537f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454af4.md) [`00576eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576eec.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00770bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770bfc.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042ca34",
      "incomplete_value": false,
      "site": "0042ca38",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca34",
      "incomplete_value": false,
      "site": "0042ca38",
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
            "const:ae0:8"
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
      "definition_site": "0042ca44",
      "incomplete_value": false,
      "site": "0042ca48",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca44",
      "incomplete_value": false,
      "site": "0042ca48",
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
            "const:ae0:8"
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
      "definition_site": "0042ca24",
      "incomplete_value": false,
      "site": "0042ca2c",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca24",
      "incomplete_value": false,
      "site": "0042ca2c",
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
            "const:ad8:8"
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
      "0042ca18",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042ca24",
      "DATA",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "0042ca34",
      "PARAM",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042ca18",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042ca24",
      "DATA",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ],
    [
      "0042ca34",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ca14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md#insn-0042ca14) · [`0042ca24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md#insn-0042ca24) · [`0042ca34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md#insn-0042ca34)
- 新版 [`0042ca14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md#insn-0042ca14) · [`0042ca24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md#insn-0042ca24) · [`0042ca34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md#insn-0042ca34)

~~~diff
- 0042ca14 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0042ca14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042ca14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042ca14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042ca14 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0042ca14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042ca14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042ca14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042ca14 bytes 08812b91
+ 0042ca14 bytes 08812e91
- 0042ca24 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0042ca24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0042ca24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0042ca24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0042ca24 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0042ca24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0042ca24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0042ca24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0042ca24 bytes 00602b91
+ 0042ca24 bytes 00602e91
- 0042ca34 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0042ca34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0042ca34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0042ca34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0042ca34 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0042ca34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0042ca34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0042ca34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0042ca34 bytes 00802b91
+ 0042ca34 bytes 00802e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe81f7239032cbaf9c520e17b388e6e"></a>

### [`0042ca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md) → [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) FUN_0042ca70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084177c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/0084177c.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md) [`004370c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004370c8.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0084177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/0084177c.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md) [`004370c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004370c8.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042cbc4",
      "incomplete_value": false,
      "site": "0042cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cbc4",
      "incomplete_value": false,
      "site": "0042cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042caa4",
      "incomplete_value": false,
      "site": "0042caac",
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
            "const:371:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042caa4",
      "incomplete_value": false,
      "site": "0042caac",
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
            "const:378:8"
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
      "definition_site": "0042cb10",
      "incomplete_value": true,
      "site": "0042cb18",
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cb10",
      "incomplete_value": true,
      "site": "0042cb18",
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
                "const:cd8:8"
              ]
            ]
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
      "0042caa4",
      "PARAM",
      [
        "storage",
        "002a5378",
        null,
        "string"
      ]
    ],
    [
      "0042cb10",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0042cb10",
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042caa4",
      "PARAM",
      [
        "storage",
        "002a5371",
        null,
        "string"
      ]
    ],
    [
      "0042cb10",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0042cb10",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042caa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md#insn-0042caa4) · [`0042cb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md#insn-0042cb10) · [`0042cbbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md#insn-0042cbbc)
- 新版 [`0042caa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md#insn-0042caa4) · [`0042cb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md#insn-0042cb10) · [`0042cbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md#insn-0042cbbc)

~~~diff
- 0042caa4 ["COPY", "tmp:0:8", ["const:378:8"]]
- 0042caa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042caa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042caa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042caa4 ["COPY", "tmp:0:8", ["const:371:8"]]
+ 0042caa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042caa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042caa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042caa4 bytes 21e00d91
+ 0042caa4 bytes 21c40d91
- 0042cb10 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 0042cb10 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042cb10 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0042cb10 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0042cb10 bytes 006c46f9
+ 0042cb10 bytes 00c446f9
- 0042cbbc ["COPY", "tmp:0:8", ["const:760:8"]]
- 0042cbbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042cbbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042cbbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042cbbc ["COPY", "tmp:0:8", ["const:810:8"]]
+ 0042cbbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042cbbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042cbbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042cbbc bytes 08811d91
+ 0042cbbc bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0290e0616931232bd842ec3e8b552161"></a>

### [`0042ce34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ce34.md) → [`0042ce34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md) FUN_0042ce34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md) [`00437890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437890.md) [`00437894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437894.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md) [`00437890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437890.md) [`00437894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437894.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042cf08",
      "incomplete_value": false,
      "site": "0042cf08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cf08",
      "incomplete_value": false,
      "site": "0042cf08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042cecc",
      "incomplete_value": true,
      "site": "0042ced4",
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cecc",
      "incomplete_value": true,
      "site": "0042ced4",
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
                "const:cd8:8"
              ]
            ]
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
      "0042cecc",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0042cecc",
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ],
    [
      "0042cf08",
      "DATA",
      [
        "storage",
        "00be6840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042cecc",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0042cecc",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042cf08",
      "DATA",
      [
        "storage",
        "00be68f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042cecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ce34.md#insn-0042cecc) · [`0042cefc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ce34.md#insn-0042cefc)
- 新版 [`0042cecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md#insn-0042cecc) · [`0042cefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md#insn-0042cefc)

~~~diff
- 0042cecc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 0042cecc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042cecc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0042cecc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0042cecc bytes 006c46f9
+ 0042cecc bytes 00c446f9
- 0042cefc ["COPY", "tmp:0:8", ["const:840:8"]]
- 0042cefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042cefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042cefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042cefc ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 0042cefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042cefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042cefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042cefc bytes 08012191
+ 0042cefc bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab7a99bb0b62b0760d70b82d89ef074"></a>

### [`0042d2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md) → [`0042d2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md) FUN_0042d2a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0042d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d484.md) [`00442a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00442/00442a64.md) [`005891dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058a/0058a2e0.md) · 呼出先 14件 [`0041b014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b014.md) [`00423a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423a40.md) [`00428620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428620.md) [`0052dd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd60.md) [`0053bda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053bda8.md)
- 新版 呼出元 4件 [`0042d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d484.md) [`00442a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00442/00442a64.md) [`005891dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058a/0058a2e0.md) · 呼出先 14件 [`0041b014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b014.md) [`00423a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423a40.md) [`00428620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428620.md) [`0052dd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd60.md) [`0053bda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bda8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042d304",
      "incomplete_value": false,
      "site": "0042d310",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d304",
      "incomplete_value": false,
      "site": "0042d310",
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
            "const:b08:8"
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
      "definition_site": "0042d374",
      "incomplete_value": false,
      "site": "0042d378",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d374",
      "incomplete_value": false,
      "site": "0042d378",
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
            "const:b00:8"
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
      "definition_site": "0042d398",
      "incomplete_value": true,
      "site": "0042d3a4",
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d398",
      "incomplete_value": true,
      "site": "0042d3a4",
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042d2d8",
      "READ",
      [
        "storage",
        "00c24b00",
        null,
        "undefined1"
      ]
    ],
    [
      "0042d2e8",
      "READ",
      [
        "storage",
        "00c24b18",
        null,
        "undefined1"
      ]
    ],
    [
      "0042d304",
      "PARAM",
      [
        "storage",
        "00c24b08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0042d2d8",
      "READ",
      [
        "storage",
        "00c24bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042d2e8",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "0042d304",
      "PARAM",
      [
        "storage",
        "00c24bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042d2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md#insn-0042d2d4) · [`0042d2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md#insn-0042d2e4) · [`0042d304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md#insn-0042d304)
- 新版 [`0042d2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md#insn-0042d2d4) · [`0042d2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md#insn-0042d2e4) · [`0042d304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md#insn-0042d304)

~~~diff
- 0042d2d4 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0042d2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042d2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042d2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042d2d4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0042d2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042d2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042d2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042d2d4 bytes 08012c91
+ 0042d2d4 bytes 08012f91
- 0042d2e4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0042d2e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042d2e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042d2e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042d2e4 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 0042d2e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042d2e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042d2e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042d2e4 bytes 08612c91
+ 0042d2e4 bytes 08612f91
- 0042d304 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0042d304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042d304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042d304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042d304 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 0042d304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042d304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042d304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042d304 bytes 21202c91
+ 0042d304 bytes 21202f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0990fae2e84febe0708f571a4af43eb5"></a>

### [`0042d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d484.md) → [`0042d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d484.md) FUN_0042d484

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0042d878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d878.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042d2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md) [`00574054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574054.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`0042d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d878.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042d2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042d51c",
      "incomplete_value": true,
      "site": "0042d51c",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d51c",
      "incomplete_value": true,
      "site": "0042d51c",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:5e1:8"
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
      "0042d50c",
      "READ",
      [
        "storage",
        "002a65e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042d50c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042d504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d484.md#insn-0042d504)
- 新版 [`0042d504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d484.md#insn-0042d504)

~~~diff
- 0042d504 ["COPY", "tmp:0:8", ["const:5e1:8"]]
- 0042d504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042d504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042d504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042d504 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0042d504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042d504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042d504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042d504 bytes 29851791
+ 0042d504 bytes 29691791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8861b1780eb4481ffd57f7799a19d9f9"></a>

### [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) → [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) FUN_0042d974

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0042f000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md) [`00430dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 5件 [`0042f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) [`00430dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042da24",
      "incomplete_value": true,
      "site": "0042da38",
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042da24",
      "incomplete_value": true,
      "site": "0042da38",
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
                "const:d18:8"
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
      "0042da24",
      "READ",
      [
        "storage",
        "00c1ad18",
        null,
        "pointer"
      ]
    ],
    [
      "0042da24",
      "PARAM",
      [
        "storage",
        "00c25d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042da24",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0042da24",
      "PARAM",
      [
        "storage",
        "00c25de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042da24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md#insn-0042da24)
- 新版 [`0042da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md#insn-0042da24)

~~~diff
- 0042da24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d18:8"]]
- 0042da24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042da24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:dc8:8"]]
+ 0042da24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0042da24 bytes 218c46f9
+ 0042da24 bytes 21e446f9
~~~


<a id="compare-96ab003ac6dc684b72710083685c2fd9"></a>

### [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) → [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) FUN_0042dad8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`0043196c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md) [`00431e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md) [`00432420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md) [`00432904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042d084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d084.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md)
- 新版 呼出元 11件 [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`0043196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md) [`00431e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md) [`00432420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md) [`00432904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042d084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d084.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042dc40",
      "incomplete_value": true,
      "site": "0042dc48",
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
      "definition_site": "0042dc40",
      "incomplete_value": true,
      "site": "0042dc48",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
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
                "const:40:8"
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
      "0042dc3c",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0042dc40",
      "READ",
      [
        "storage",
        "00c13240",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0042dc44",
      "READ",
      [
        "storage",
        "00c13280",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "0042dc3c",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "0042dc40",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0042dc44",
      "READ",
      [
        "storage",
        "00c13330",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042dc3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md#insn-0042dc3c) · [`0042dc58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md#insn-0042dc58) · [`0042dd4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md#insn-0042dd4c)
- 新版 [`0042dc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md#insn-0042dc3c) · [`0042dc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md#insn-0042dc58) · [`0042dd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md#insn-0042dd4c)

~~~diff
- 0042dc3c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d20:8"]]
- 0042dc3c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042dc3c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd0:8"]]
+ 0042dc3c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 0042dc3c bytes 5a9346f9
+ 0042dc3c bytes 5aeb46f9
- 0042dc58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 0042dc58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042dc58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0042dc58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0042dc58 bytes 086946f9
+ 0042dc58 bytes 08c146f9
- 0042dd4c ["COPY", "tmp:0:8", ["const:569:8"]]
- 0042dd4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0042dd4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0042dd4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0042dd4c ["COPY", "tmp:0:8", ["const:5f6:8"]]
+ 0042dd4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0042dd4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0042dd4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0042dd4c bytes 00a41591
+ 0042dd4c bytes 00d81791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941395fcb33540fa7ba767eee828433b"></a>

### [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) → [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) FUN_0042e8c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 16件 [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042f000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00435e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435e50.md) [`00436518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436518.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 16件 [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00435e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435e50.md) [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042e910",
      "incomplete_value": false,
      "site": "0042e914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042e910",
      "incomplete_value": false,
      "site": "0042e914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042e914",
      "DATA",
      [
        "storage",
        "00be66a0",
        null,
        "pointer"
      ]
    ],
    [
      "0042e960",
      "READ",
      [
        "storage",
        "00be66a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042e914",
      "DATA",
      [
        "storage",
        "00be6750",
        null,
        "pointer"
      ]
    ],
    [
      "0042e960",
      "READ",
      [
        "storage",
        "00be6758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042e910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md#insn-0042e910)
- 新版 [`0042e910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md#insn-0042e910)

~~~diff
- 0042e910 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0042e910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042e910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042e910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042e910 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 0042e910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042e910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042e910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042e910 bytes 08811a91
+ 0042e910 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3220e00d19bf586d800fb4c50718d571"></a>

### [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) → [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) FUN_0042e9d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`00434024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md) [`004744e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004744e8.md) · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 15件 [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00434024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) [`004744e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004744e8.md) · 呼出先 2件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042ea1c",
      "incomplete_value": true,
      "site": "0042ea1c",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ea1c",
      "incomplete_value": true,
      "site": "0042ea1c",
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
            "const:68:8"
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
      "definition_site": "0042ea20",
      "incomplete_value": true,
      "site": "0042ea20",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ea20",
      "incomplete_value": true,
      "site": "0042ea20",
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
            "const:40:8"
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
      "definition_site": "0042ea18",
      "incomplete_value": true,
      "site": "0042ea28",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ea18",
      "incomplete_value": true,
      "site": "0042ea28",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042e9fc",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0042ea08",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0042ea18",
      "READ",
      [
        "storage",
        "00c13250",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0042e9fc",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "0042ea08",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "0042ea18",
      "READ",
      [
        "storage",
        "00c13300",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042e9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md#insn-0042e9fc) · [`0042ea04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md#insn-0042ea04)
- 新版 [`0042e9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md#insn-0042e9fc) · [`0042ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md#insn-0042ea04)

~~~diff
- 0042e9fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d28:8"]]
- 0042e9fc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042e9fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:dd8:8"]]
+ 0042e9fc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0042e9fc bytes f79646f9
+ 0042e9fc bytes f7ee46f9
- 0042ea04 ["COPY", "register:40d0:8", ["register:4000:8"]]
- 0042ea04 bytes fa0300aa
+ 0042ea04 ["COPY", "register:40d0:8", ["register:4000:8"]]
+ 0042ea04 bytes fa0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b66547aefbeb6242c20fcc0ee027b5"></a>

### [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) → [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) FUN_0042eb00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`00434024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md) · 呼出先 7件 [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md)
- 新版 呼出元 13件 [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00434024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) · 呼出先 7件 [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.90% / 新版 91.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042ebac",
      "incomplete_value": false,
      "site": "0042ebb4",
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
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ebac",
      "incomplete_value": false,
      "site": "0042ebb4",
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
            "const:39b:8"
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
      "definition_site": "0042ebf8",
      "incomplete_value": false,
      "site": "0042ec00",
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
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ebf8",
      "incomplete_value": false,
      "site": "0042ec00",
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
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042ec68",
      "incomplete_value": false,
      "site": "0042ec70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:6b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ec68",
      "incomplete_value": false,
      "site": "0042ec70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:74a:8"
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
      "0042ebac",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "0042ebf8",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "0042ec68",
      "PARAM",
      [
        "storage",
        "002ae74a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0042ebac",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "0042ebf8",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "0042ec68",
      "PARAM",
      [
        "storage",
        "002ae6b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042eb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md#insn-0042eb68) · [`0042eba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md#insn-0042eba0) · [`0042ebf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md#insn-0042ebf8)
- 新版 [`0042eb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md#insn-0042eb68) · [`0042eba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md#insn-0042eba0) · [`0042ebf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md#insn-0042ebf8)

~~~diff
- 0042eb68 ["COPY", "tmp:0:8", ["const:21d:8"]]
- 0042eb68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042eb68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042eb68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042eb68 ["COPY", "tmp:0:8", ["const:2aa:8"]]
+ 0042eb68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042eb68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042eb68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042eb68 bytes 29750891
+ 0042eb68 bytes 29a90a91
- 0042eba0 ["COPY", "tmp:0:8", ["const:39b:8"]]
- 0042eba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042eba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042eba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042eba0 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 0042eba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042eba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042eba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042eba0 bytes 086d0e91
+ 0042eba0 bytes 08510e91
- 0042ebf8 ["COPY", "tmp:0:8", ["const:39b:8"]]
- 0042ebf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042ebf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042ebf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042ebf8 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 0042ebf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ebf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042ebf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042ebf8 bytes 216c0e91
+ 0042ebf8 bytes 21500e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2545bd646791b3ab3ca7c309d1ed3d64"></a>

### [`0042ee74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042ee74.md) → [`0042ee74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042ee74.md) FUN_0042ee74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb070.md) [`00bdb270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md) [`00bdb320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042ee98",
      "incomplete_value": true,
      "site": "0042eea0",
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
      "definition_site": "0042ee98",
      "incomplete_value": true,
      "site": "0042eea0",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
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
                "const:40:8"
              ]
            ]
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
      "0042ee90",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0042ee98",
      "READ",
      [
        "storage",
        "00c13240",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0042ee9c",
      "READ",
      [
        "storage",
        "00c13280",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "0042ee90",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "0042ee98",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0042ee9c",
      "READ",
      [
        "storage",
        "00c13330",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042ee74.md#insn-0042ee90) · [`0042ee94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042ee74.md#insn-0042ee94)
- 新版 [`0042ee90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042ee74.md#insn-0042ee90) · [`0042ee94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042ee74.md#insn-0042ee94)

~~~diff
- 0042ee90 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d20:8"]]
- 0042ee90 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0042ee90 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dd0:8"]]
+ 0042ee90 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0042ee90 bytes b59246f9
+ 0042ee90 bytes b5ea46f9
- 0042ee94 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0042ee94 bytes f30300aa
+ 0042ee94 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0042ee94 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469a8b4d06023c117e5000eb1e1e35fc"></a>

### [`0042f000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md) → [`0042f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) FUN_0042f000

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084d6d0.md) · 呼出先 16件 [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md) · 呼出先 16件 [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ef4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042f088",
      "incomplete_value": false,
      "site": "0042f090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f088",
      "incomplete_value": false,
      "site": "0042f090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042f0b0",
      "incomplete_value": false,
      "site": "0042f0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f0b0",
      "incomplete_value": false,
      "site": "0042f0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "definition_site": "0042f14c",
      "incomplete_value": true,
      "site": "0042f158",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:78d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f14c",
      "incomplete_value": true,
      "site": "0042f158",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:700:8"
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
      "0042f048",
      "PARAM",
      [
        "storage",
        "002a7350",
        null,
        "string"
      ]
    ],
    [
      "0042f090",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "0042f0b0",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0042f048",
      "PARAM",
      [
        "storage",
        "002a7349",
        null,
        "string"
      ]
    ],
    [
      "0042f090",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "0042f0b0",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042f048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md#insn-0042f048) · [`0042f088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md#insn-0042f088) · [`0042f08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md#insn-0042f08c)
- 新版 [`0042f048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md#insn-0042f048) · [`0042f088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md#insn-0042f088)

~~~diff
- 0042f048 ["COPY", "tmp:0:8", ["const:350:8"]]
- 0042f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042f048 ["COPY", "tmp:0:8", ["const:349:8"]]
+ 0042f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042f048 bytes 21400d91
+ 0042f048 bytes 21240d91
- 0042f088 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 0042f088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042f088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042f088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042f088 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 0042f088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042f088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042f088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042f088 bytes 08412791
+ 0042f088 bytes 08012a91
- 0042f08c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0042f08c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60bc4a79034e0f78a95cd09104d2a1de"></a>

### [`0042f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md) → [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) FUN_0042f610

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084d6d0.md) · 呼出先 20件 [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042fcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fcec.md) [`00438ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md) · 呼出先 20件 [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042fcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fcec.md) [`00438ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ef4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.20% / 新版 87.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042f6e4",
      "incomplete_value": true,
      "site": "0042f6e4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6e4",
      "incomplete_value": true,
      "site": "0042f6e4",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042f6ec",
      "incomplete_value": true,
      "site": "0042f6ec",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6ec",
      "incomplete_value": true,
      "site": "0042f6ec",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042f6fc",
      "incomplete_value": true,
      "site": "0042f6fc",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6fc",
      "incomplete_value": true,
      "site": "0042f6fc",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042f654",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "0042f664",
      "READ",
      [
        "storage",
        "00c24b68",
        null,
        "undefined1"
      ]
    ],
    [
      "0042f670",
      "PARAM",
      [
        "storage",
        "00c24b20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0042f654",
      "READ",
      [
        "storage",
        "00c24c08",
        null,
        "undefined1"
      ]
    ],
    [
      "0042f664",
      "READ",
      [
        "storage",
        "00c24c28",
        null,
        "undefined1"
      ]
    ],
    [
      "0042f670",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042f6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md#insn-0042f6e4) · [`0042f6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md#insn-0042f6ec) · [`0042f6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md#insn-0042f6fc)
- 新版 [`0042f6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md#insn-0042f6e4) · [`0042f6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md#insn-0042f6ec) · [`0042f6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md#insn-0042f6fc)

~~~diff
- 0042f6e4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b58:8"]]
- 0042f6e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0042f6e4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c18:8"]]
+ 0042f6e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042f6e4 bytes c0ae05f9
+ 0042f6e4 bytes c00e06f9
- 0042f6ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b58:8"]]
- 0042f6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0042f6ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c18:8"]]
+ 0042f6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042f6ec bytes c0ae05f9
+ 0042f6ec bytes c00e06f9
- 0042f6fc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0042f6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:b70:8"]]
- 0042f6fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0042f6fc ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0042f6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:c30:8"]]
+ 0042f6fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0042f6fc bytes 09c12d39
+ 0042f6fc bytes 09c13039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf660fd16b5f61ac685a996452944eb"></a>

### [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) → [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) FUN_0042fd7c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00437c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md) [`00576eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576eec.md) [`00770bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00770/00770bfc.md) [`0084dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084dd1c.md) [`00873c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c68.md) · 呼出先 24件 [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00430300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430300.md) [`00436bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436bf8.md)
- 新版 呼出元 5件 [`00437c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md) [`00576eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576eec.md) [`00770bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00770/00770bfc.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md) [`00873c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c68.md) · 呼出先 24件 [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00430300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430300.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.88% / 新版 83.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042fe50",
      "incomplete_value": true,
      "site": "0042fe50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe50",
      "incomplete_value": true,
      "site": "0042fe50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042fe58",
      "incomplete_value": true,
      "site": "0042fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe58",
      "incomplete_value": true,
      "site": "0042fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042fe68",
      "incomplete_value": true,
      "site": "0042fe68",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe68",
      "incomplete_value": true,
      "site": "0042fe68",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042fdc0",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042fdd0",
      "READ",
      [
        "storage",
        "00c24bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "0042fddc",
      "PARAM",
      [
        "storage",
        "00c24b74",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0042fdc0",
      "READ",
      [
        "storage",
        "00c24c60",
        null,
        "undefined1"
      ]
    ],
    [
      "0042fdd0",
      "READ",
      [
        "storage",
        "00c24c80",
        null,
        "undefined1"
      ]
    ],
    [
      "0042fddc",
      "PARAM",
      [
        "storage",
        "00c24c34",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042fe50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md#insn-0042fe50) · [`0042fe58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md#insn-0042fe58) · [`0042fe68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md#insn-0042fe68)
- 新版 [`0042fe50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md#insn-0042fe50) · [`0042fe58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md#insn-0042fe58) · [`0042fe68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md#insn-0042fe68)

~~~diff
- 0042fe50 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:bb0:8"]]
- 0042fe50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0042fe50 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c70:8"]]
+ 0042fe50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042fe50 bytes 00db05f9
+ 0042fe50 bytes 003b06f9
- 0042fe58 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:bb0:8"]]
- 0042fe58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0042fe58 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c70:8"]]
+ 0042fe58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042fe58 bytes 00db05f9
+ 0042fe58 bytes 003b06f9
- 0042fe68 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0042fe68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:bc8:8"]]
- 0042fe68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0042fe68 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0042fe68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:c88:8"]]
+ 0042fe68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0042fe68 bytes 09212f39
+ 0042fe68 bytes 09213239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1e920b5161d5d419f2db066f8d0313c"></a>

### [`004303e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md) → [`004303e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) FUN_004303e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00430b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00428904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428904.md) [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md)
- 新版 呼出元 1件 [`00430b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00428904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428904.md) [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430480",
      "incomplete_value": false,
      "site": "00430488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430480",
      "incomplete_value": false,
      "site": "00430488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430494",
      "incomplete_value": false,
      "site": "00430494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430494",
      "incomplete_value": false,
      "site": "00430494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00430538",
      "incomplete_value": true,
      "site": "00430548",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:176:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430538",
      "incomplete_value": true,
      "site": "00430548",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:17d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00430488",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "00430494",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ],
    [
      "00430538",
      "READ",
      [
        "storage",
        "002a317d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00430488",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "00430494",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00430538",
      "READ",
      [
        "storage",
        "002a3176",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md#insn-00430480) · [`00430484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md#insn-00430484)
- 新版 [`00430480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md#insn-00430480) · [`00430484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md#insn-00430484)

~~~diff
- 00430480 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00430480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00430480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00430480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00430480 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00430480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00430480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00430480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00430480 bytes 08412791
+ 00430480 bytes 08012a91
- 00430484 ["COPY", "register:40e0:8", ["register:4000:8"]]
- 00430484 bytes fc0300aa
+ 00430484 ["COPY", "register:40e0:8", ["register:4000:8"]]
+ 00430484 bytes fc0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2caf667ac4d5943951fddc0c962cae02"></a>

### [`00430b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md) → [`00430b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md) FUN_00430b04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004537f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00454/00454af4.md) · 呼出先 12件 [`004303e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md) [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`0043bf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf84.md) [`0043cb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cb64.md) [`0043cbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043c/0043cbb4.md)
- 新版 呼出元 2件 [`004537f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00454/00454af4.md) · 呼出先 12件 [`004303e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`0043bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf84.md) [`0043cb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cb64.md) [`0043cbb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cbb4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430b5c",
      "incomplete_value": false,
      "site": "00430b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430b5c",
      "incomplete_value": false,
      "site": "00430b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00430b90",
      "incomplete_value": false,
      "site": "00430b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430b90",
      "incomplete_value": false,
      "site": "00430b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430c04",
      "incomplete_value": false,
      "site": "00430c04",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430c04",
      "incomplete_value": false,
      "site": "00430c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00430b6c",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "pointer"
      ]
    ],
    [
      "00430b98",
      "DATA",
      [
        "storage",
        "00be6e00",
        null,
        "undefined *"
      ]
    ],
    [
      "00430c04",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00430b6c",
      "DATA",
      [
        "storage",
        "00be6e60",
        null,
        "pointer"
      ]
    ],
    [
      "00430b98",
      "DATA",
      [
        "storage",
        "00be6eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00430c04",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md#insn-00430b5c) · [`00430b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md#insn-00430b90) · [`00430bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430b04.md#insn-00430bf8)
- 新版 [`00430b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md#insn-00430b5c) · [`00430b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md#insn-00430b90) · [`00430bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430b04.md#insn-00430bf8)

~~~diff
- 00430b5c ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00430b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00430b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00430b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00430b5c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00430b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00430b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00430b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00430b5c bytes 08c13691
+ 00430b5c bytes 08813991
- 00430b90 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00430b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00430b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00430b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00430b90 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 00430b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00430b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00430b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00430b90 bytes 08013891
+ 00430b90 bytes 08c13a91
- 00430bf8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00430bf8 ["COPY", "register:4040:8", ["const:be7000:8"]]
- 00430bf8 bytes a83d00d0
+ 00430bf8 bytes a83d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2df9e519a78d92ee9922592d639545"></a>

### [`00430dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md) → [`00430dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) FUN_00430dd8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00841c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00428954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428954.md) [`0042d974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d974.md) [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00428954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428954.md) [`0042d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d974.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ef4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430e6c",
      "incomplete_value": false,
      "site": "00430e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430e6c",
      "incomplete_value": false,
      "site": "00430e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00430e88",
      "incomplete_value": false,
      "site": "00430e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430e88",
      "incomplete_value": false,
      "site": "00430e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00430fbc",
      "incomplete_value": true,
      "site": "00430fc4",
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
      "definition_site": "00430fbc",
      "incomplete_value": true,
      "site": "00430fc4",
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
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00430e2c",
      "PARAM",
      [
        "storage",
        "0029c31d",
        null,
        "string"
      ]
    ],
    [
      "00430e74",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "00430e88",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00430e2c",
      "PARAM",
      [
        "storage",
        "0029c3aa",
        null,
        "string"
      ]
    ],
    [
      "00430e74",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "00430e88",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md#insn-00430e2c) · [`00430e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md#insn-00430e6c) · [`00430e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md#insn-00430e70)
- 新版 [`00430e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md#insn-00430e2c) · [`00430e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md#insn-00430e6c)

~~~diff
- 00430e2c ["COPY", "tmp:0:8", ["const:31d:8"]]
- 00430e2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00430e2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00430e2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00430e2c ["COPY", "tmp:0:8", ["const:3aa:8"]]
+ 00430e2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00430e2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00430e2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00430e2c bytes 21740c91
+ 00430e2c bytes 21a80e91
- 00430e6c ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00430e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00430e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00430e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00430e6c ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00430e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00430e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00430e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00430e6c bytes 08412791
+ 00430e6c bytes 08012a91
- 00430e70 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00430e70 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8c5f6503adee4a04859d18917bb350"></a>

### [`00431534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md) → [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) FUN_00431534

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084e780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084e/0084e780.md) · 呼出先 15件 [`004289f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289f4.md) [`0043d22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d22c.md) [`0043d230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d230.md) [`0053e18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md)
- 新版 呼出元 1件 [`0084e780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md) · 呼出先 15件 [`004289f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md) [`0043d22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d22c.md) [`0043d230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d230.md) [`0053e18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.48% / 新版 94.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00431664",
      "incomplete_value": true,
      "site": "00431674",
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
                "const:8de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431664",
      "incomplete_value": true,
      "site": "00431674",
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
                "const:851:8"
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
      "definition_site": "00431668",
      "incomplete_value": true,
      "site": "00431678",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431668",
      "incomplete_value": true,
      "site": "00431678",
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
                "const:10:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004316d8",
      "incomplete_value": false,
      "site": "004316d8",
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
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004316d8",
      "incomplete_value": false,
      "site": "004316d8",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043156c",
      "PARAM",
      [
        "storage",
        "002a811e",
        null,
        "string"
      ]
    ],
    [
      "004315dc",
      "READ",
      [
        "storage",
        "00c1ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004315dc",
      "PARAM",
      [
        "storage",
        "00c25d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0043156c",
      "PARAM",
      [
        "storage",
        "002a808a",
        null,
        "string"
      ]
    ],
    [
      "004315dc",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004315dc",
      "PARAM",
      [
        "storage",
        "00c25de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043156c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md#insn-0043156c) · [`004315dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md#insn-004315dc) · [`0043165c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431534.md#insn-0043165c)
- 新版 [`0043156c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md#insn-0043156c) · [`004315dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md#insn-004315dc) · [`0043165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md#insn-0043165c)

~~~diff
- 0043156c ["COPY", "tmp:0:8", ["const:11e:8"]]
- 0043156c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0043156c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0043156c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0043156c ["COPY", "tmp:0:8", ["const:8a:8"]]
+ 0043156c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0043156c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0043156c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0043156c bytes 21780491
+ 0043156c bytes 21280291
- 004315dc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d18:8"]]
- 004315dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 004315dc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dc8:8"]]
+ 004315dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 004315dc bytes 008c46f9
+ 004315dc bytes 00e446f9
- 0043165c ["COPY", "tmp:0:8", ["const:851:8"]]
- 0043165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043165c ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 0043165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043165c bytes 08452191
+ 0043165c bytes 08792391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94200275ba840be458bdceaebb05c32"></a>

### [`0043196c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md) → [`0043196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md) FUN_0043196c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00987b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00987/00987b70.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0043d868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043d/0043d868.md) [`0043f32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f32c.md)
- 新版 呼出元 1件 [`00987b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00987/00987b70.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0043d868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d868.md) [`0043f32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f32c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00431aac",
      "incomplete_value": false,
      "site": "00431aac",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431aac",
      "incomplete_value": false,
      "site": "00431aac",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00431b4c",
      "incomplete_value": false,
      "site": "00431b4c",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431b4c",
      "incomplete_value": false,
      "site": "00431b4c",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004319ac",
      "incomplete_value": false,
      "site": "004319b4",
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
            "const:284:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004319ac",
      "incomplete_value": false,
      "site": "004319b4",
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
            "const:318:8"
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
      "004319ac",
      "PARAM",
      [
        "storage",
        "002a9318",
        null,
        "string"
      ]
    ],
    [
      "00431aac",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ],
    [
      "00431b4c",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004319ac",
      "PARAM",
      [
        "storage",
        "002a9284",
        null,
        "string"
      ]
    ],
    [
      "00431aac",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ],
    [
      "00431b4c",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004319ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md#insn-004319ac) · [`00431aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md#insn-00431aa4) · [`00431b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/0043196c.md#insn-00431b44)
- 新版 [`004319ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md#insn-004319ac) · [`00431aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md#insn-00431aa4) · [`00431b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/0043196c.md#insn-00431b44)

~~~diff
- 004319ac ["COPY", "tmp:0:8", ["const:318:8"]]
- 004319ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004319ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004319ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004319ac ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004319ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004319ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004319ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004319ac bytes 21600c91
+ 004319ac bytes 21100a91
- 00431aa4 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00431aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00431aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00431aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00431aa4 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00431aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00431aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00431aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00431aa4 bytes 08610591
+ 00431aa4 bytes 08210891
- 00431b44 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00431b44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00431b44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00431b44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00431b44 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00431b44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00431b44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00431b44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00431b44 bytes 08610791
+ 00431b44 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ed047a26fa77a73e72a07e42f352ad"></a>

### [`00431e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md) → [`00431e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md) FUN_00431e50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00984ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00984/00984ce0.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0043f6bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f6bc.md) [`0043f97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043f97c.md)
- 新版 呼出元 1件 [`00984ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/00984ce0.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0043f6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f6bc.md) [`0043f97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f97c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432028",
      "incomplete_value": false,
      "site": "00432028",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432028",
      "incomplete_value": false,
      "site": "00432028",
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
            "const:258:8"
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
      "definition_site": "004320c8",
      "incomplete_value": false,
      "site": "004320c8",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004320c8",
      "incomplete_value": false,
      "site": "004320c8",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00431e94",
      "incomplete_value": false,
      "site": "00431e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:2db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431e94",
      "incomplete_value": false,
      "site": "00431e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:24e:8"
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
      "00431e94",
      "PARAM",
      [
        "storage",
        "0029d24e",
        null,
        "string"
      ]
    ],
    [
      "00431ef4",
      "PARAM",
      [
        "storage",
        "0029457f",
        null,
        "string"
      ]
    ],
    [
      "00432028",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00431e94",
      "PARAM",
      [
        "storage",
        "0029d2db",
        null,
        "string"
      ]
    ],
    [
      "00431ef4",
      "PARAM",
      [
        "storage",
        "0029460c",
        null,
        "string"
      ]
    ],
    [
      "00432028",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00431e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md#insn-00431e94) · [`00431ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md#insn-00431ef4) · [`00432020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00431/00431e50.md#insn-00432020)
- 新版 [`00431e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md#insn-00431e94) · [`00431ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md#insn-00431ef4) · [`00432020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431e50.md#insn-00432020)

~~~diff
- 00431e94 ["COPY", "tmp:0:8", ["const:24e:8"]]
- 00431e94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00431e94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00431e94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00431e94 ["COPY", "tmp:0:8", ["const:2db:8"]]
+ 00431e94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00431e94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00431e94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00431e94 bytes 21380991
+ 00431e94 bytes 216c0b91
- 00431ef4 ["COPY", "tmp:0:8", ["const:57f:8"]]
- 00431ef4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00431ef4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00431ef4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00431ef4 ["COPY", "tmp:0:8", ["const:60c:8"]]
+ 00431ef4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00431ef4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00431ef4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00431ef4 bytes 21fc1591
+ 00431ef4 bytes 21301891
- 00432020 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00432020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00432020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00432020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00432020 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00432020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00432020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00432020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00432020 bytes 08610991
+ 00432020 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b4e52bf7d576fbbad881b71f3e406d7"></a>

### [`00432420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md) → [`00432420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md) FUN_00432420

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2c36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a2c/00a2c36c.md) [`00a3c6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3c/00a3c6d0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0043fc3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043f/0043fc3c.md) [`004400b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00440/004400b8.md)
- 新版 呼出元 2件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) [`00a3c6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c6d0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0043fc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fc3c.md) [`004400b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00440/004400b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432560",
      "incomplete_value": false,
      "site": "00432560",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432560",
      "incomplete_value": false,
      "site": "00432560",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432600",
      "incomplete_value": false,
      "site": "00432600",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432600",
      "incomplete_value": false,
      "site": "00432600",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00432460",
      "incomplete_value": false,
      "site": "00432468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:2e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432460",
      "incomplete_value": false,
      "site": "00432468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:25c:8"
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
      "00432460",
      "PARAM",
      [
        "storage",
        "0029d25c",
        null,
        "string"
      ]
    ],
    [
      "00432560",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ],
    [
      "00432600",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00432460",
      "PARAM",
      [
        "storage",
        "0029d2e9",
        null,
        "string"
      ]
    ],
    [
      "00432560",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ],
    [
      "00432600",
      "DATA",
      [
        "storage",
        "00be7488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md#insn-00432460) · [`00432558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md#insn-00432558) · [`004325f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432420.md#insn-004325f8)
- 新版 [`00432460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md#insn-00432460) · [`00432558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md#insn-00432558) · [`004325f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432420.md#insn-004325f8)

~~~diff
- 00432460 ["COPY", "tmp:0:8", ["const:25c:8"]]
- 00432460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00432460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00432460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00432460 ["COPY", "tmp:0:8", ["const:2e9:8"]]
+ 00432460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00432460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00432460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00432460 bytes 21700991
+ 00432460 bytes 21a40b91
- 00432558 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00432558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00432558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00432558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00432558 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00432558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00432558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00432558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00432558 bytes 08610d91
+ 00432558 bytes 08211091
- 004325f8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 004325f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004325f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004325f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004325f8 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 004325f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004325f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004325f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004325f8 bytes 08610f91
+ 004325f8 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc6121c17f1e14a5066f4730204754c"></a>

### [`00432904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md) → [`00432904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) FUN_00432904

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00853228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853228.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`00438ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ef4.md) [`00440380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00440/00440380.md)
- 新版 呼出元 1件 [`00853228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853228.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00438ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ef4.md) [`00440380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00440/00440380.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432990",
      "incomplete_value": false,
      "site": "00432998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432990",
      "incomplete_value": false,
      "site": "00432998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004329b4",
      "incomplete_value": false,
      "site": "004329b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004329b4",
      "incomplete_value": false,
      "site": "004329b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "definition_site": "00432a98",
      "incomplete_value": false,
      "site": "00432a98",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432a98",
      "incomplete_value": false,
      "site": "00432a98",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00432948",
      "PARAM",
      [
        "storage",
        "0029b1b3",
        null,
        "string"
      ]
    ],
    [
      "00432998",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "004329b4",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00432948",
      "PARAM",
      [
        "storage",
        "0029b240",
        null,
        "string"
      ]
    ],
    [
      "00432998",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "004329b4",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md#insn-00432948) · [`00432990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md#insn-00432990) · [`00432994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md#insn-00432994)
- 新版 [`00432948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md#insn-00432948) · [`00432990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md#insn-00432990)

~~~diff
- 00432948 ["COPY", "tmp:0:8", ["const:1b3:8"]]
- 00432948 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00432948 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00432948 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00432948 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00432948 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00432948 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00432948 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00432948 bytes 21cc0691
+ 00432948 bytes 21000991
- 00432990 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00432990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00432990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00432990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00432990 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00432990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00432990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00432990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00432990 bytes 08412791
+ 00432990 bytes 08012a91
- 00432994 ["COPY", "register:4048:8", ["register:4000:8"]]
- 00432994 bytes e90300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d783d936193295678d9f0dc75d98f5d"></a>

### [`00432e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432e80.md) → [`00432e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432e80.md) FUN_00432e80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00438ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00438ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ef4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432f10",
      "incomplete_value": false,
      "site": "00432f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432f10",
      "incomplete_value": false,
      "site": "00432f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00432f38",
      "incomplete_value": false,
      "site": "00432f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432f38",
      "incomplete_value": false,
      "site": "00432f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00433054",
      "incomplete_value": false,
      "site": "00433054",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00433054",
      "incomplete_value": false,
      "site": "00433054",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00432ec8",
      "PARAM",
      [
        "storage",
        "002a4270",
        null,
        "string"
      ]
    ],
    [
      "00432f18",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "00432f38",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00432ec8",
      "PARAM",
      [
        "storage",
        "002a4269",
        null,
        "string"
      ]
    ],
    [
      "00432f18",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "00432f38",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432e80.md#insn-00432ec8) · [`00432f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432e80.md#insn-00432f10) · [`00432f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432e80.md#insn-00432f14)
- 新版 [`00432ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432e80.md#insn-00432ec8) · [`00432f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432e80.md#insn-00432f10)

~~~diff
- 00432ec8 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00432ec8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00432ec8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00432ec8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00432ec8 ["COPY", "tmp:0:8", ["const:269:8"]]
+ 00432ec8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00432ec8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00432ec8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00432ec8 bytes 21c00991
+ 00432ec8 bytes 21a40991
- 00432f10 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00432f10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00432f10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00432f10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00432f10 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00432f10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00432f10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00432f10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00432f10 bytes 08412791
+ 00432f10 bytes 08012a91
- 00432f14 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00432f14 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e21be54b4f4bb9621fcfd0d2ab51de50"></a>

### [`0043344c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/0043344c.md) → [`0043344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md) FUN_0043344c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`0084e780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084e/0084e780.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`00441100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/00441100.md) [`00441e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/00441e04.md)
- 新版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0084e780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00441100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/00441100.md) [`00441e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/00441e04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043358c",
      "incomplete_value": false,
      "site": "0043358c",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043358c",
      "incomplete_value": false,
      "site": "0043358c",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043362c",
      "incomplete_value": false,
      "site": "0043362c",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043362c",
      "incomplete_value": false,
      "site": "0043362c",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043348c",
      "incomplete_value": false,
      "site": "00433494",
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
            "const:3bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043348c",
      "incomplete_value": false,
      "site": "00433494",
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
            "const:32f:8"
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
      "0043348c",
      "PARAM",
      [
        "storage",
        "0029c32f",
        null,
        "string"
      ]
    ],
    [
      "0043358c",
      "DATA",
      [
        "storage",
        "00be7658",
        null,
        "undefined *"
      ]
    ],
    [
      "0043362c",
      "DATA",
      [
        "storage",
        "00be76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043348c",
      "PARAM",
      [
        "storage",
        "0029c3bc",
        null,
        "string"
      ]
    ],
    [
      "0043358c",
      "DATA",
      [
        "storage",
        "00be7708",
        null,
        "undefined *"
      ]
    ],
    [
      "0043362c",
      "DATA",
      [
        "storage",
        "00be7788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043348c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/0043344c.md#insn-0043348c) · [`00433584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/0043344c.md#insn-00433584) · [`00433624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/0043344c.md#insn-00433624)
- 新版 [`0043348c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md#insn-0043348c) · [`00433584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md#insn-00433584) · [`00433624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md#insn-00433624)

~~~diff
- 0043348c ["COPY", "tmp:0:8", ["const:32f:8"]]
- 0043348c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0043348c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0043348c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0043348c ["COPY", "tmp:0:8", ["const:3bc:8"]]
+ 0043348c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0043348c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0043348c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0043348c bytes 21bc0c91
+ 0043348c bytes 21f00e91
- 00433584 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00433584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00433584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00433584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00433584 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00433584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00433584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00433584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00433584 bytes 08611991
+ 00433584 bytes 08211c91
- 00433624 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00433624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00433624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00433624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00433624 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00433624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00433624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00433624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00433624 bytes 08611b91
+ 00433624 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ebf6a5a05d30a5d2d8eeec40e08428d"></a>

### [`00433930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md) → [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) FUN_00433930

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0083b3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md) [`00853acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853acc.md) · 呼出先 11件 [`0044210c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00442/0044210c.md) [`0053e13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e13c.md) [`0053e18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e1dc.md) [`0053e9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053e9d0.md)
- 新版 呼出元 2件 [`0083b3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md) [`00853acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853acc.md) · 呼出先 11件 [`0044210c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00442/0044210c.md) [`0053e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e13c.md) [`0053e18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md) [`0053e9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e9d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004339bc",
      "incomplete_value": true,
      "site": "004339bc",
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
                "const:365:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004339bc",
      "incomplete_value": true,
      "site": "004339bc",
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
                "const:36c:8"
              ]
            ]
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
      "definition_site": "00433a88",
      "incomplete_value": true,
      "site": "00433a88",
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
                "const:cb6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00433a88",
      "incomplete_value": true,
      "site": "00433a88",
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
                "const:c29:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00433a8c",
      "incomplete_value": true,
      "site": "00433a8c",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00433a8c",
      "incomplete_value": true,
      "site": "00433a8c",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043396c",
      "READ",
      [
        "storage",
        "00c1ad18",
        null,
        "pointer"
      ]
    ],
    [
      "0043396c",
      "PARAM",
      [
        "storage",
        "00c25d28",
        null,
        "undefined1"
      ]
    ],
    [
      "004339a4",
      "READ",
      [
        "storage",
        "002a736c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043396c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0043396c",
      "PARAM",
      [
        "storage",
        "00c25de8",
        null,
        "undefined1"
      ]
    ],
    [
      "004339a4",
      "READ",
      [
        "storage",
        "002a7365",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043396c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md#insn-0043396c) · [`004339a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md#insn-004339a0) · [`00433a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md#insn-00433a64)
- 新版 [`0043396c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md#insn-0043396c) · [`004339a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md#insn-004339a0) · [`00433a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md#insn-00433a64)

~~~diff
- 0043396c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d18:8"]]
- 0043396c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043396c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dc8:8"]]
+ 0043396c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043396c bytes 008c46f9
+ 0043396c bytes 00e446f9
- 004339a0 ["COPY", "tmp:0:8", ["const:36c:8"]]
- 004339a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004339a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004339a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004339a0 ["COPY", "tmp:0:8", ["const:365:8"]]
+ 004339a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004339a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004339a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004339a0 bytes 29b10d91
+ 004339a0 bytes 29950d91
- 00433a64 ["COPY", "tmp:0:8", ["const:c29:8"]]
- 00433a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00433a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00433a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00433a64 ["COPY", "tmp:0:8", ["const:cb6:8"]]
+ 00433a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00433a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00433a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00433a64 bytes 29a53091
+ 00433a64 bytes 29d93291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f0f77c85885240a988f84c16130153c"></a>

### [`00434024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md) → [`00434024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md) FUN_00434024

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.47% / 新版 94.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00434208",
      "incomplete_value": false,
      "site": "00434208",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00434208",
      "incomplete_value": false,
      "site": "00434208",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043420c",
      "incomplete_value": false,
      "site": "0043420c",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043420c",
      "incomplete_value": false,
      "site": "0043420c",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004342f8",
      "incomplete_value": true,
      "site": "00434300",
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
      "definition_site": "004342f8",
      "incomplete_value": true,
      "site": "00434300",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043406c",
      "PARAM",
      [
        "storage",
        "002a027c",
        null,
        "string"
      ]
    ],
    [
      "00434208",
      "DATA",
      [
        "storage",
        "00be77d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043420c",
      "DATA",
      [
        "storage",
        "00be7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043406c",
      "PARAM",
      [
        "storage",
        "002a0309",
        null,
        "string"
      ]
    ],
    [
      "00434208",
      "DATA",
      [
        "storage",
        "00be7888",
        null,
        "undefined *"
      ]
    ],
    [
      "0043420c",
      "DATA",
      [
        "storage",
        "00be7908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043406c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md#insn-0043406c) · [`004341ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md#insn-004341ec) · [`00434204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434024.md#insn-00434204)
- 新版 [`0043406c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md#insn-0043406c) · [`004341ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md#insn-004341ec) · [`00434204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434024.md#insn-00434204)

~~~diff
- 0043406c ["COPY", "tmp:0:8", ["const:27c:8"]]
- 0043406c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0043406c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0043406c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0043406c ["COPY", "tmp:0:8", ["const:309:8"]]
+ 0043406c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0043406c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0043406c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0043406c bytes 21f00991
+ 0043406c bytes 21240c91
- 004341ec ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 004341ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004341ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004341ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004341ec ["COPY", "tmp:0:8", ["const:888:8"]]
+ 004341ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004341ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004341ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004341ec bytes 29611f91
+ 004341ec bytes 29212291
- 00434204 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00434204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00434204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00434204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00434204 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00434204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00434204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00434204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00434204 bytes 08612191
+ 00434204 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f84d05e4324d64dae26a702cfbfeb6f"></a>

### [`00434528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md) → [`00434528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md) FUN_00434528

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00853f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853f6c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md)
- 新版 呼出元 1件 [`00853f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853f6c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.87% / 新版 93.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004346e0",
      "incomplete_value": false,
      "site": "004346e0",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004346e0",
      "incomplete_value": false,
      "site": "004346e0",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004346e4",
      "incomplete_value": false,
      "site": "004346e4",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004346e4",
      "incomplete_value": false,
      "site": "004346e4",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004347a0",
      "incomplete_value": true,
      "site": "004347a8",
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
      "definition_site": "004347a0",
      "incomplete_value": true,
      "site": "004347a8",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00434570",
      "PARAM",
      [
        "storage",
        "0029793b",
        null,
        "string"
      ]
    ],
    [
      "004346e0",
      "DATA",
      [
        "storage",
        "00be78d8",
        null,
        "undefined *"
      ]
    ],
    [
      "004346e4",
      "DATA",
      [
        "storage",
        "00be7958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00434570",
      "PARAM",
      [
        "storage",
        "002979c8",
        null,
        "string"
      ]
    ],
    [
      "004346e0",
      "DATA",
      [
        "storage",
        "00be7988",
        null,
        "undefined *"
      ]
    ],
    [
      "004346e4",
      "DATA",
      [
        "storage",
        "00be7a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00434570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md#insn-00434570) · [`004346c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md#insn-004346c4) · [`004346dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/00434528.md#insn-004346dc)
- 新版 [`00434570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md#insn-00434570) · [`004346c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md#insn-004346c4) · [`004346dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/00434528.md#insn-004346dc)

~~~diff
- 00434570 ["COPY", "tmp:0:8", ["const:93b:8"]]
- 00434570 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00434570 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00434570 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00434570 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00434570 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00434570 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00434570 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00434570 bytes 21ec2491
+ 00434570 bytes 21202791
- 004346c4 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 004346c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004346c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004346c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004346c4 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 004346c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004346c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004346c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004346c4 bytes 29612391
+ 004346c4 bytes 29212691
- 004346dc ["COPY", "tmp:0:8", ["const:958:8"]]
- 004346dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004346dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004346dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004346dc ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 004346dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004346dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004346dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004346dc bytes 08612591
+ 004346dc bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f878044c44c4448de24044008d6b541"></a>

### [`004349a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md) → [`004349a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md) FUN_004349a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00860de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md)
- 新版 呼出元 1件 [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004349f8",
      "incomplete_value": false,
      "site": "00434a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004349f8",
      "incomplete_value": false,
      "site": "00434a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "definition_site": "00434a0c",
      "incomplete_value": false,
      "site": "00434a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00434a0c",
      "incomplete_value": false,
      "site": "00434a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "definition_site": "00434ac4",
      "incomplete_value": true,
      "site": "00434ac4",
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
                "const:cab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00434ac4",
      "incomplete_value": true,
      "site": "00434ac4",
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
                "const:c1e:8"
              ]
            ]
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
      "00434a00",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "00434a0c",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ],
    [
      "00434ab4",
      "READ",
      [
        "storage",
        "00298c1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00434a00",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "00434a0c",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00434ab4",
      "READ",
      [
        "storage",
        "00298cab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004349f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md#insn-004349f8) · [`004349fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00434/004349a0.md#insn-004349fc)
- 新版 [`004349f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md#insn-004349f8) · [`004349fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00434/004349a0.md#insn-004349fc)

~~~diff
- 004349f8 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 004349f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004349f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004349f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004349f8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 004349f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004349f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004349f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004349f8 bytes 08412791
+ 004349f8 bytes 08012a91
- 004349fc ["COPY", "register:40a8:8", ["register:4000:8"]]
- 004349fc bytes f50300aa
+ 004349fc ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 004349fc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b87436e6bd0969d0637b5f1246e61d0"></a>

### [`00435358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md) → [`00435358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md) FUN_00435358

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c390.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436bf8.md)
- 新版 呼出元 1件 [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00435430",
      "incomplete_value": false,
      "site": "00435438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00435430",
      "incomplete_value": false,
      "site": "00435438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "definition_site": "00435454",
      "incomplete_value": false,
      "site": "00435454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00435454",
      "incomplete_value": false,
      "site": "00435454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004354bc",
      "incomplete_value": true,
      "site": "004354bc",
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
                "const:cab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004354bc",
      "incomplete_value": true,
      "site": "004354bc",
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
                "const:c1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043539c",
      "PARAM",
      [
        "storage",
        "002a318e",
        null,
        "string"
      ]
    ],
    [
      "00435438",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ],
    [
      "00435454",
      "DATA",
      [
        "storage",
        "00be6a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043539c",
      "PARAM",
      [
        "storage",
        "002a3187",
        null,
        "string"
      ]
    ],
    [
      "00435438",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ],
    [
      "00435454",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043539c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md#insn-0043539c) · [`00435430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md#insn-00435430) · [`00435434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435358.md#insn-00435434)
- 新版 [`0043539c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md#insn-0043539c) · [`00435430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435358.md#insn-00435430)

~~~diff
- 0043539c ["COPY", "tmp:0:8", ["const:18e:8"]]
- 0043539c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0043539c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0043539c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0043539c ["COPY", "tmp:0:8", ["const:187:8"]]
+ 0043539c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0043539c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0043539c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0043539c bytes 21380691
+ 0043539c bytes 211c0691
- 00435430 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00435430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00435430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00435430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00435430 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00435430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00435430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00435430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00435430 bytes 08412791
+ 00435430 bytes 08012a91
- 00435434 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00435434 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad75141f1bbe7d737b7fa01e936e6e5"></a>

### [`004357f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/004357f4.md) → [`004357f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/004357f4.md) FUN_004357f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00435c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00443e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00443/00443e34.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00443e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00443/00443e34.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004359fc",
      "incomplete_value": false,
      "site": "004359fc",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004359fc",
      "incomplete_value": false,
      "site": "004359fc",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043598c",
      "incomplete_value": true,
      "site": "00435994",
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043598c",
      "incomplete_value": true,
      "site": "00435994",
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
                "const:cd8:8"
              ]
            ]
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
      "0043591c",
      "READ",
      [
        "storage",
        "0029583f",
        null,
        "undefined4"
      ]
    ],
    [
      "00435920",
      "READ",
      [
        "storage",
        "00295843",
        null,
        "undefined1"
      ]
    ],
    [
      "0043598c",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043591c",
      "READ",
      [
        "storage",
        "002958cc",
        null,
        "undefined4"
      ]
    ],
    [
      "00435920",
      "READ",
      [
        "storage",
        "002958d0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043598c",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00435898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/004357f4.md#insn-00435898) · [`004358a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/004357f4.md#insn-004358a4) · [`0043598c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/004357f4.md#insn-0043598c)
- 新版 [`00435898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/004357f4.md#insn-00435898) · [`004358a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/004357f4.md#insn-004358a4) · [`0043598c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/004357f4.md#insn-0043598c)

~~~diff
- 00435898 ["COPY", "tmp:0:8", ["const:c39:8"]]
- 00435898 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00435898 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00435898 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00435898 ["COPY", "tmp:0:8", ["const:cc6:8"]]
+ 00435898 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00435898 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00435898 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00435898 bytes 5ae73091
+ 00435898 bytes 5a1b3391
- 004358a4 ["COPY", "tmp:0:8", ["const:83f:8"]]
- 004358a4 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 004358a4 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 004358a4 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 004358a4 ["COPY", "tmp:0:8", ["const:8cc:8"]]
+ 004358a4 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 004358a4 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 004358a4 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 004358a4 bytes 5aff2091
+ 004358a4 bytes 5a332391
- 0043598c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 0043598c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043598c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0043598c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043598c bytes 006c46f9
+ 0043598c bytes 00c446f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5861db3a03b089b88e5e797a9b038fb"></a>

### [`00435c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md) → [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) FUN_00435c18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428cb4.md) [`00428dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428dc8.md) [`004357f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/004357f4.md) [`00444068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444068.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md) [`00428dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428dc8.md) [`004357f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/004357f4.md) [`00444068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444068.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00435ca0",
      "incomplete_value": false,
      "site": "00435ca8",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00435ca0",
      "incomplete_value": false,
      "site": "00435ca8",
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
            "const:bd8:8"
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
      "00435ca8",
      "DATA",
      [
        "storage",
        "00be7bd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00435d08",
      "READ",
      [
        "storage",
        "00be7bf8",
        null,
        "pointer"
      ]
    ],
    [
      "00435d08",
      "READ",
      [
        "storage",
        "00be7c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00435ca8",
      "DATA",
      [
        "storage",
        "00be7c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00435d08",
      "READ",
      [
        "storage",
        "00be7ca8",
        null,
        "pointer"
      ]
    ],
    [
      "00435d08",
      "READ",
      [
        "storage",
        "00be7cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00435ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00435/00435c18.md#insn-00435ca0)
- 新版 [`00435ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md#insn-00435ca0)

~~~diff
- 00435ca0 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00435ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00435ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00435ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00435ca0 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00435ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00435ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00435ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00435ca0 bytes 08612f91
+ 00435ca0 bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec5868c7f2f5e70489e7217f1134b22"></a>

### [`004364f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004364f8.md) → [`004364f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004364f8.md) FUN_004364f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00436500",
      "incomplete_value": false,
      "site": "00436504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436500",
      "incomplete_value": false,
      "site": "00436504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00436504",
      "DATA",
      [
        "storage",
        "00be66a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00436504",
      "DATA",
      [
        "storage",
        "00be6750",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004364f8.md#insn-00436500)
- 新版 [`00436500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004364f8.md#insn-00436500)

~~~diff
- 00436500 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00436500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00436500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00436500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00436500 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00436500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00436500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00436500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00436500 bytes 29811a91
+ 00436500 bytes 29411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1af2d3fefdb6a1dfaa64e2c48121e32"></a>

### [`00436518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436518.md) → [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md) FUN_00436518

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`00575024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00575/00575024.md) [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) [`0076e98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076e/0076e98c.md) [`00aaeab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaeab8.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 5件 [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`00575024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00575/00575024.md) [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`00aaeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00436520",
      "incomplete_value": false,
      "site": "00436524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436520",
      "incomplete_value": false,
      "site": "00436524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00436524",
      "DATA",
      [
        "storage",
        "00be66a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00436524",
      "DATA",
      [
        "storage",
        "00be6750",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436518.md#insn-00436520)
- 新版 [`00436520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md#insn-00436520)

~~~diff
- 00436520 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00436520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00436520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00436520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00436520 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00436520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00436520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00436520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00436520 bytes 29811a91
+ 00436520 bytes 29411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e06900682b9ae345a330954e9ed4f0"></a>

### [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) → [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) FUN_004365f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`00444070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444070.md) [`0045543c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00455/0045543c.md) [`004656ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/004656ac.md) [`0046a090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a090.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436790.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md)
- 新版 呼出元 25件 [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00444070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444070.md) [`0045543c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00455/0045543c.md) [`004656ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004656ac.md) [`0046a090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a090.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436790.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00436678",
      "incomplete_value": true,
      "site": "0043667c",
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436678",
      "incomplete_value": true,
      "site": "0043667c",
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
                "const:d40:8"
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
      "00436678",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00436678",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00436678",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00436678",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md#insn-00436678)
- 新版 [`00436678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md#insn-00436678)

~~~diff
- 00436678 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 00436678 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00436678 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 00436678 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00436678 bytes 21a046f9
+ 00436678 bytes 21f846f9
~~~


<a id="compare-cde86d08b52b308ae478f6f93e30e79c"></a>

### [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) → [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) FUN_00436e9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 169件 [`00437118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437118.md) [`00437c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437c94.md) [`004389fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00438/004389fc.md) [`004391e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/004391e0.md) [`00439a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439a30.md) · 呼出先 3件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 169件 [`00437118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md) [`00437c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md) [`004389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md) [`004391e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004391e0.md) [`00439a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439a30.md) · 呼出先 3件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00436ebc",
      "incomplete_value": true,
      "site": "00436ec0",
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
      "definition_site": "00436ebc",
      "incomplete_value": true,
      "site": "00436ec0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00436ec4",
      "incomplete_value": true,
      "site": "00436ecc",
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436ec4",
      "incomplete_value": true,
      "site": "00436ecc",
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
                "const:d50:8"
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
      "definition_site": "00436ec8",
      "incomplete_value": true,
      "site": "00436ecc",
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436ec8",
      "incomplete_value": true,
      "site": "00436ecc",
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
                "const:d58:8"
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
      "00436eb8",
      "READ",
      [
        "storage",
        "00c1ad48",
        null,
        "pointer"
      ]
    ],
    [
      "00436ec0",
      "DATA",
      [
        "storage",
        "00be6738",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00436ec4",
      "READ",
      [
        "storage",
        "00c1ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00436eb8",
      "READ",
      [
        "storage",
        "00c1adf8",
        null,
        "pointer"
      ]
    ],
    [
      "00436ec0",
      "DATA",
      [
        "storage",
        "00be67e8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00436ec4",
      "READ",
      [
        "storage",
        "00c1ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md#insn-00436eb8) · [`00436ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md#insn-00436ec4) · [`00436ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md#insn-00436ec8)
- 新版 [`00436eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md#insn-00436eb8) · [`00436ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md#insn-00436ec4) · [`00436ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md#insn-00436ec8)

~~~diff
- 00436eb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
- 00436eb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00436eb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00436eb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00436eb8 bytes 08a546f9
+ 00436eb8 bytes 08fd46f9
- 00436ec4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d50:8"]]
- 00436ec4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00436ec4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e00:8"]]
+ 00436ec4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00436ec4 bytes 21a846f9
+ 00436ec4 bytes 210047f9
- 00436ec8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d58:8"]]
- 00436ec8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00436ec8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e08:8"]]
+ 00436ec8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00436ec8 bytes 42ac46f9
+ 00436ec8 bytes 420447f9
~~~


<a id="compare-060ef1ac3ebe825ad1b952363304576f"></a>

### [`00436ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436ef4.md) → [`00436ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436ef4.md) FUN_00436ef4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00436f00",
      "incomplete_value": false,
      "site": "00436f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436f00",
      "incomplete_value": false,
      "site": "00436f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00436f0c",
      "DATA",
      [
        "storage",
        "00be6760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00436f0c",
      "DATA",
      [
        "storage",
        "00be6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436ef4.md#insn-00436f00)
- 新版 [`00436f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436ef4.md#insn-00436f00)

~~~diff
- 00436f00 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00436f00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00436f00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00436f00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00436f00 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00436f00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00436f00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00436f00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00436f00 bytes 4a811d91
+ 00436f00 bytes 4a412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77cde7193ca6c05126695819c47f3623"></a>

### [`00436f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436f38.md) → [`00436f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436f38.md) FUN_00436f38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00436f50",
      "incomplete_value": false,
      "site": "00436f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436f50",
      "incomplete_value": false,
      "site": "00436f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00436f5c",
      "DATA",
      [
        "storage",
        "00be6760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00436f5c",
      "DATA",
      [
        "storage",
        "00be6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436f38.md#insn-00436f50)
- 新版 [`00436f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436f38.md#insn-00436f50)

~~~diff
- 00436f50 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00436f50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00436f50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00436f50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00436f50 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00436f50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00436f50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00436f50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00436f50 bytes 08811d91
+ 00436f50 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5574a6f8e5d58bc34a06ffa58081f495"></a>

### [`00436f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436f94.md) → [`00436f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436f94.md) FUN_00436f94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00436fc0",
      "incomplete_value": false,
      "site": "00436fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436fc0",
      "incomplete_value": false,
      "site": "00436fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00436fc0",
      "DATA",
      [
        "storage",
        "00be6760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00436fc0",
      "DATA",
      [
        "storage",
        "00be6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436f94.md#insn-00436fb8)
- 新版 [`00436fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436f94.md#insn-00436fb8)

~~~diff
- 00436fb8 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00436fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00436fb8 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00436fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00436fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00436fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 bytes 08811d91
+ 00436fb8 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e23c37bd74eb0189179876645816a75"></a>

### [`0043701c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/0043701c.md) → [`0043701c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/0043701c.md) FUN_0043701c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00437038",
      "incomplete_value": false,
      "site": "00437038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437038",
      "incomplete_value": false,
      "site": "00437038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00437038",
      "DATA",
      [
        "storage",
        "00be6760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437038",
      "DATA",
      [
        "storage",
        "00be6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/0043701c.md#insn-00437034)
- 新版 [`00437034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/0043701c.md#insn-00437034)

~~~diff
- 00437034 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00437034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437034 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00437034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437034 bytes 29811d91
+ 00437034 bytes 29412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5a749a9603af1eb6532beceae7d3e7"></a>

### [`00437118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437118.md) → [`00437118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md) FUN_00437118

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00573e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00573/00573e38.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043723c",
      "incomplete_value": true,
      "site": "0043723c",
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
                "const:396:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043723c",
      "incomplete_value": true,
      "site": "0043723c",
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
                "const:39d:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0043729c",
      "incomplete_value": true,
      "site": "0043729c",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043729c",
      "incomplete_value": true,
      "site": "0043729c",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043728c",
      "incomplete_value": true,
      "site": "0043729c",
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043728c",
      "incomplete_value": true,
      "site": "0043729c",
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
                "const:ad8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043722c",
      "READ",
      [
        "storage",
        "002a539d",
        null,
        "string"
      ]
    ],
    [
      "00437280",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043728c",
      "READ",
      [
        "storage",
        "00c24ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043722c",
      "READ",
      [
        "storage",
        "002a5396",
        null,
        "string"
      ]
    ],
    [
      "00437280",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043728c",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437118.md#insn-00437224) · [`0043727c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437118.md#insn-0043727c) · [`0043728c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437118.md#insn-0043728c)
- 新版 [`00437224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md#insn-00437224) · [`0043727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md#insn-0043727c) · [`0043728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437118.md#insn-0043728c)

~~~diff
- 00437224 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00437224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437224 ["COPY", "tmp:0:8", ["const:396:8"]]
+ 00437224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437224 bytes 29750e91
+ 00437224 bytes 29590e91
- 0043727c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0043727c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043727c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043727c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043727c ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0043727c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043727c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043727c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043727c bytes 08812b91
+ 0043727c bytes 08812e91
- 0043728c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad8:8"]]
- 0043728c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043728c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
+ 0043728c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043728c bytes 006d45f9
+ 0043728c bytes 00cd45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b99996b1872ee21cd6c69b9a68aa703f"></a>

### [`00437688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437688.md) → [`00437688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437688.md) FUN_00437688

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004376a0",
      "incomplete_value": true,
      "site": "004376a4",
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
      "definition_site": "004376a0",
      "incomplete_value": true,
      "site": "004376a4",
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
      "0043769c",
      "READ",
      [
        "storage",
        "00c1ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004376a4",
      "DATA",
      [
        "storage",
        "00be67e0",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0043769c",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "004376a4",
      "DATA",
      [
        "storage",
        "00be6890",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043769c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/00437688.md#insn-0043769c)
- 新版 [`0043769c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437688.md#insn-0043769c)

~~~diff
- 0043769c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d10:8"]]
- 0043769c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043769c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0043769c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043769c bytes 088946f9
+ 0043769c bytes 08e146f9
~~~


<a id="compare-d4cae6fcd4ac63cbf67c450163233dde"></a>

### [`004376c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004376c8.md) → [`004376c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004376c8.md) FUN_004376c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004376bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004376bc.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377f0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`004376bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004376bc.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043776c",
      "incomplete_value": true,
      "site": "00437770",
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
      "definition_site": "0043776c",
      "incomplete_value": true,
      "site": "00437770",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00437748",
      "incomplete_value": true,
      "site": "00437750",
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437748",
      "incomplete_value": true,
      "site": "00437750",
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
                "const:d68:8"
              ]
            ]
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
      "00437748",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "00437748",
      "PARAM",
      [
        "storage",
        "00c12e08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00437768",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00437748",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00437748",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00437768",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004376c8.md#insn-00437748) · [`00437768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004376c8.md#insn-00437768)
- 新版 [`00437748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004376c8.md#insn-00437748) · [`00437768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004376c8.md#insn-00437768)

~~~diff
- 00437748 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d68:8"]]
- 00437748 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00437748 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
+ 00437748 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00437748 bytes 21b446f9
+ 00437748 bytes 210c47f9
- 00437768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00437768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00437768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 00437768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00437768 bytes 08b946f9
+ 00437768 bytes 081147f9
~~~


