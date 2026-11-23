# v15.7.2 → v15.7.3 · 最優先の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-3a17f3bfa0b5bf1a1875bc02d8e6dead"></a>

### [`00739a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739a10.md) → [`00739a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md) FUN_00739a10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 19件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0053f81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f81c.md) [`0062d23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d23c.md) [`006fdbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fdbdc.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 19件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`0062d23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d23c.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00739af8",
      "incomplete_value": true,
      "site": "00739b00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:770:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00739af8",
      "incomplete_value": true,
      "site": "00739b00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
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
      "00739af8",
      "READ",
      [
        "storage",
        "00c1b6c0",
        null,
        "pointer"
      ]
    ],
    [
      "00739af8",
      "PARAM",
      [
        "storage",
        "0109e3f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00739b78",
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
      "00739af8",
      "READ",
      [
        "storage",
        "00c1b770",
        null,
        "pointer"
      ]
    ],
    [
      "00739af8",
      "PARAM",
      [
        "storage",
        "0109e4b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00739b78",
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

- 旧版 [`00739af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739a10.md#insn-00739af8) · [`00739b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739a10.md#insn-00739b78) · [`00739b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739a10.md#insn-00739b84)
- 新版 [`00739af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739af8) · [`00739b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739b78) · [`00739b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739a10.md#insn-00739b84)

~~~diff
- 00739af8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:6c0:8"]]
- 00739af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739af8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:770:8"]]
+ 00739af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00739af8 bytes 216043f9
+ 00739af8 bytes 21b843f9
- 00739b78 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:db0:8"]]
- 00739b78 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739b78 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e60:8"]]
+ 00739b78 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00739b78 bytes f7da46f9
+ 00739b78 bytes f73247f9
- 00739b84 ["COPY", "register:40a0:8", ["const:c24000:8"]]
+ 00739b84 ["COPY", "register:40a0:8", ["const:c25000:8"]]
- 00739b84 bytes 542700f0
+ 00739b84 bytes 74270090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b34e08564f9db03feda3cbe64ebbd9"></a>

### [`00739da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739da8.md) → [`00739da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md) FUN_00739da8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`007693f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00769/007693f4.md) · 呼出先 9件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00700be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00700/00700be0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 2件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`007693f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/007693f4.md) · 呼出先 9件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00700be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00700/00700be0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd4",
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
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd4",
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
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00739fd8",
      "incomplete_value": false,
      "site": "00739fd8",
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
      "definition_site": "00739fd8",
      "incomplete_value": false,
      "site": "00739fd8",
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
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd8",
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
      "definition_site": "00739fd4",
      "incomplete_value": false,
      "site": "00739fd8",
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00739e98",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00739eec",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00739f00",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00739e98",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00739eec",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00739f00",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00739e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739da8.md#insn-00739e98) · [`00739ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739da8.md#insn-00739ee4) · [`00739ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00739/00739da8.md#insn-00739ee8)
- 新版 [`00739e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739e98) · [`00739ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739ee4) · [`00739ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739da8.md#insn-00739ee8)

~~~diff
- 00739e98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:db0:8"]]
- 00739e98 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00739e98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e60:8"]]
+ 00739e98 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00739e98 bytes 18db46f9
+ 00739e98 bytes 183347f9
- 00739ee4 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00739ee4 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00739ee4 bytes 482700f0
+ 00739ee4 bytes 68270090
- 00739ee8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00739ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00739ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00739ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00739ee8 bytes 08e13d91
+ 00739ee8 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5687083398d262e005045c7ad0b535b3"></a>

### [`0073a424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a424.md) → [`0073a424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md) FUN_0073a424

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0070bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0070b/0070bedc.md) [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0062d23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d23c.md) [`0070959c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00709/0070959c.md)
- 新版 呼出元 5件 [`0070bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070bedc.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bd0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0062d23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d23c.md) [`0070959c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/0070959c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.96% / 新版 93.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073a544",
      "incomplete_value": true,
      "site": "0073a568",
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
                "const:ed2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a544",
      "incomplete_value": true,
      "site": "0073a568",
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
                "const:e45:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0073a4b0",
      "incomplete_value": true,
      "site": "0073a4b0",
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
      "definition_site": "0073a4b0",
      "incomplete_value": true,
      "site": "0073a4b0",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0073a4b8",
      "incomplete_value": false,
      "site": "0073a4c8",
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
      "definition_site": "0073a4b8",
      "incomplete_value": false,
      "site": "0073a4c8",
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
      "0073a4ac",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0073a4b8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073a4c0",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0073a4ac",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0073a4b8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073a4c0",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a4ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a424.md#insn-0073a4ac) · [`0073a4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a424.md#insn-0073a4b8) · [`0073a4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a424.md#insn-0073a4c0)
- 新版 [`0073a4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4ac) · [`0073a4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4b8) · [`0073a4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4c0)

~~~diff
- 0073a4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0073a4ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073a4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0073a4ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0073a4ac bytes 00dd44f9
+ 0073a4ac bytes 003d45f9
- 0073a4b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0073a4b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0073a4b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 bytes 21603691
+ 0073a4b8 bytes 21203991
- 0073a4c0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0073a4c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0073a4c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 bytes 42800f91
+ 0073a4c0 bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a20f7211536c9c6b72d3ecd4ddc8b6"></a>

### [`0073a780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a780.md) → [`0073a780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md) FUN_0073a780

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 10件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md) [`0075b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075b/0075b45c.md) [`0075b460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075b/0075b460.md) [`0075b510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075b/0075b510.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 10件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0075b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b45c.md) [`0075b460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b460.md) [`0075b510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073a7dc",
      "incomplete_value": false,
      "site": "0073a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a7dc",
      "incomplete_value": false,
      "site": "0073a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073a828",
      "incomplete_value": false,
      "site": "0073a828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a828",
      "incomplete_value": false,
      "site": "0073a828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "0073a7dc",
      "DATA",
      [
        "storage",
        "00bfbd78",
        null,
        "undefined *"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbd98",
        null,
        "pointer"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073a7dc",
      "DATA",
      [
        "storage",
        "00bfbe28",
        null,
        "undefined *"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbe48",
        null,
        "pointer"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbe50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a780.md#insn-0073a7d4) · [`0073a820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a780.md#insn-0073a820)
- 新版 [`0073a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md#insn-0073a7d4) · [`0073a820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md#insn-0073a820)

~~~diff
- 0073a7d4 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 0073a7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0073a7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 bytes 08e13591
+ 0073a7d4 bytes 08a13891
- 0073a820 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 0073a820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073a820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073a820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0073a820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073a820 bytes 08e13791
+ 0073a820 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b9c1726c8ea7801c62ae3322a0b52c1"></a>

### [`0073a8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a8e0.md) → [`0073a8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md) FUN_0073a8e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md) [`0073da58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073da58.md) [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 2件 [`00acf804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf804.md) [`00acf894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf894.md)
- 新版 呼出元 7件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0073da58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 2件 [`00acf8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md) [`00acf95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0073a92c",
      "incomplete_value": true,
      "site": "0073a92c",
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
            "const:f64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a92c",
      "incomplete_value": true,
      "site": "0073a92c",
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
            "const:eb4:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0073ab64",
      "incomplete_value": false,
      "site": "0073ab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ab64",
      "incomplete_value": false,
      "site": "0073ab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0073ab8c",
      "incomplete_value": true,
      "site": "0073ab90",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "0073ab8c",
      "incomplete_value": true,
      "site": "0073ab90",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073a8e4",
      "READ",
      [
        "storage",
        "00c23eb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0073a92c",
      "WRITE",
      [
        "storage",
        "00c23eb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0073ab64",
      "WRITE",
      [
        "storage",
        "00c27e20",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0073a8e4",
      "READ",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "0073a92c",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "0073ab64",
      "WRITE",
      [
        "storage",
        "00c27ee0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a8e0.md#insn-0073a92c) · [`0073ab64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a8e0.md#insn-0073ab64) · [`0073a8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a8e0.md#insn-0073a8e4)
- 新版 [`0073a92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073a92c) · [`0073ab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073ab64) · [`0073a8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073a8e4)

~~~diff
- 0073a92c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0073a92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0073a92c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:eb4:8"]]
- 0073a92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0073a92c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0073a92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0073a92c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:f64:8"]]
+ 0073a92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0073a92c bytes 1fd13a39
+ 0073a92c bytes 1f913d39
- 0073ab64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
- 0073ab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0073ab64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 0073ab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0073ab64 bytes 00210eb9
+ 0073ab64 bytes 00e10eb9
- 0073a8e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb4:8"]]
- 0073a8e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0073a8e4 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0073a8e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f64:8"]]
+ 0073a8e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0073a8e4 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0073a8e4 bytes 09d17a39
+ 0073a8e4 bytes 09917d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b3b8e3b190a30ebdebcaa784cda116"></a>

### [`0073addc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073addc.md) → [`0073addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md) FUN_0073addc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md) · 呼出先 21件 [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053baf0.md)
- 新版 呼出元 2件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) · 呼出先 21件 [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae34",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae34",
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
                "const:875:8"
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
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae38",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae38",
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
                "const:875:8"
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
      "definition_site": "0073af00",
      "incomplete_value": true,
      "site": "0073af04",
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
      "definition_site": "0073af00",
      "incomplete_value": true,
      "site": "0073af04",
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
      "0073ae20",
      "READ",
      [
        "storage",
        "0029f875",
        null,
        "string"
      ]
    ],
    [
      "0073aeec",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "0073aef0",
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
      "0073ae20",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073aeec",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0073aef0",
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

- 旧版 [`0073ae1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073addc.md#insn-0073ae1c) · [`0073aeec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073addc.md#insn-0073aeec) · [`0073aef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073addc.md#insn-0073aef0)
- 新版 [`0073ae1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073ae1c) · [`0073aeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073aeec) · [`0073aef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073aef0)

~~~diff
- 0073ae1c ["COPY", "tmp:0:8", ["const:875:8"]]
- 0073ae1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["COPY", "tmp:0:8", ["const:902:8"]]
+ 0073ae1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c bytes 08d52191
+ 0073ae1c bytes 08092491
- 0073aeec ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d98:8"]]
- 0073aeec ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073aeec ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
+ 0073aeec ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073aeec bytes 7bcf46f9
+ 0073aeec bytes 7b2747f9
- 0073aef0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc8:8"]]
- 0073aef0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073aef0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
+ 0073aef0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0073aef0 bytes 296546f9
+ 0073aef0 bytes 29bd46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5d54a03872c244f08508db78a31655"></a>

### [`0073b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md) → [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md) FUN_0073b3dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073bad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bad0.md) · 呼出先 22件 [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053baf0.md) [`0053d580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d580.md)
- 新版 呼出元 1件 [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) · 呼出先 22件 [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md) [`0053d580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d580.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073b438",
      "incomplete_value": true,
      "site": "0073b438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b438",
      "incomplete_value": true,
      "site": "0073b438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae:8"
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
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b4",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b4",
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
                "const:875:8"
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
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b8",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b8",
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073b428",
      "READ",
      [
        "storage",
        "0029a0ae",
        null,
        "string"
      ]
    ],
    [
      "0073b4a0",
      "READ",
      [
        "storage",
        "0029f875",
        null,
        "string"
      ]
    ],
    [
      "0073b568",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0073b428",
      "READ",
      [
        "storage",
        "0029a13b",
        null,
        "string"
      ]
    ],
    [
      "0073b4a0",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073b568",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073b424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md#insn-0073b424) · [`0073b498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md#insn-0073b498) · [`0073b568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md#insn-0073b568)
- 新版 [`0073b424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b424) · [`0073b498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b498) · [`0073b568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b568)

~~~diff
- 0073b424 ["COPY", "tmp:0:8", ["const:ae:8"]]
- 0073b424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073b424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073b424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0073b424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073b424 bytes 29b90291
+ 0073b424 bytes 29ed0491
- 0073b498 ["COPY", "tmp:0:8", ["const:875:8"]]
- 0073b498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073b498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073b498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["COPY", "tmp:0:8", ["const:902:8"]]
+ 0073b498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073b498 bytes 29d52191
+ 0073b498 bytes 29092491
- 0073b568 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d98:8"]]
- 0073b568 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073b568 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
+ 0073b568 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073b568 bytes 7bcf46f9
+ 0073b568 bytes 7b2747f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e54b9a763df29ab10cba539fe264fa53"></a>

### [`0073bad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bad0.md) → [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) FUN_0073bad0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073d968.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436bf8.md) [`00574144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574144.md) [`005742c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/005742c4.md) [`0073b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md)
- 新版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md) [`00574144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md) [`005742c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005742c4.md) [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.56% / 新版 88.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073bb20",
      "incomplete_value": true,
      "site": "0073bb30",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073bb20",
      "incomplete_value": true,
      "site": "0073bb30",
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
                "const:875:8"
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
      "definition_site": "0073bb7c",
      "incomplete_value": true,
      "site": "0073bb7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073bb7c",
      "incomplete_value": true,
      "site": "0073bb7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bea:8"
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
      "definition_site": "0073bb80",
      "incomplete_value": true,
      "site": "0073bb80",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073bb80",
      "incomplete_value": true,
      "site": "0073bb80",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
      "0073bb20",
      "READ",
      [
        "storage",
        "0029f875",
        null,
        "string"
      ]
    ],
    [
      "0073bb6c",
      "READ",
      [
        "storage",
        "00293bea",
        null,
        "string"
      ]
    ],
    [
      "0073bb70",
      "READ",
      [
        "storage",
        "00293bef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073bb20",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073bb6c",
      "READ",
      [
        "storage",
        "00293c77",
        null,
        "string"
      ]
    ],
    [
      "0073bb70",
      "READ",
      [
        "storage",
        "00293c7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bad0.md#insn-0073bb18) · [`0073bb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bad0.md#insn-0073bb64) · [`0073bbfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bad0.md#insn-0073bbfc)
- 新版 [`0073bb18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bb18) · [`0073bb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bb64) · [`0073bbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bbfc)

~~~diff
- 0073bb18 ["COPY", "tmp:0:8", ["const:875:8"]]
- 0073bb18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["COPY", "tmp:0:8", ["const:902:8"]]
+ 0073bb18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 bytes 29d52191
+ 0073bb18 bytes 29092491
- 0073bb64 ["COPY", "tmp:0:8", ["const:bea:8"]]
- 0073bb64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 0073bb64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 bytes 29a92f91
+ 0073bb64 bytes 29dd3191
- 0073bbfc ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 0073bbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 0073bbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc bytes 08412791
+ 0073bbfc bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffb5024ea2c9ed63dc035effe69d9790"></a>

### [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) → [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) FUN_0073bf10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073ef14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ef14.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436518.md)
- 新版 呼出元 1件 [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d4",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d4",
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d8",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d8",
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073c13c",
      "incomplete_value": true,
      "site": "0073c13c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c13c",
      "incomplete_value": true,
      "site": "0073c13c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073bfe0",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "0073bff4",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "0073c01c",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073bfe0",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073bff4",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073c01c",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md#insn-0073bfe0) · [`0073c0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md#insn-0073c0b4) · [`0073c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md#insn-0073c120)
- 新版 [`0073bfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073bfe0) · [`0073c0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073c0b4) · [`0073c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073c120)

~~~diff
- 0073bfe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d30:8"]]
- 0073bfe0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073bfe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
+ 0073bfe0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 0073bfe0 bytes 739a46f9
+ 0073bfe0 bytes 73f246f9
- 0073c0b4 ["COPY", "tmp:0:8", ["const:875:8"]]
- 0073c0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["COPY", "tmp:0:8", ["const:902:8"]]
+ 0073c0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 bytes 29d52191
+ 0073c0b4 bytes 29092491
- 0073c120 ["COPY", "tmp:0:8", ["const:bea:8"]]
- 0073c120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073c120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073c120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 0073c120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073c120 bytes 29a92f91
+ 0073c120 bytes 29dd3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c7197270eb5f1c0e1aee12ae506097"></a>

### [`0073ccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073ccd0.md) → [`0073ccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073ccd0.md) FUN_0073ccd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574344.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574344.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073cd14",
      "incomplete_value": true,
      "site": "0073cd1c",
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
      "definition_site": "0073cd14",
      "incomplete_value": true,
      "site": "0073cd1c",
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
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073cd04",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "0073cd1c",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0073cd04",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073cd1c",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073cd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073ccd0.md#insn-0073cd04)
- 新版 [`0073cd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073ccd0.md#insn-0073cd04)

~~~diff
- 0073cd04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d30:8"]]
- 0073cd04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073cd04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:de0:8"]]
+ 0073cd04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0073cd04 bytes 4a9946f9
+ 0073cd04 bytes 4af146f9
~~~


<a id="compare-a479fecf1e6b733de83261354a012ca0"></a>

### [`0073cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md) → [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) FUN_0073cdfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00670f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00670/00670f08.md) · 呼出先 28件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md)
- 新版 呼出元 1件 [`00670f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670f08.md) · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.74% / 新版 92.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073ced4",
      "incomplete_value": true,
      "site": "0073cedc",
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
      "definition_site": "0073ced4",
      "incomplete_value": true,
      "site": "0073cedc",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb4",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb4",
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
                "const:875:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb8",
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
                "const:902:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb8",
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
                "const:875:8"
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
      "0073cec8",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "0073cedc",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "0073cf04",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073cec8",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073cedc",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073cf04",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073cec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md#insn-0073cec8) · [`0073cf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md#insn-0073cf9c) · [`0073d008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073c/0073cdfc.md#insn-0073d008)
- 新版 [`0073cec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073cec8) · [`0073cf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073cf9c) · [`0073d008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073d008)

~~~diff
- 0073cec8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d30:8"]]
- 0073cec8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073cec8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:de0:8"]]
+ 0073cec8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0073cec8 bytes d69a46f9
+ 0073cec8 bytes d6f246f9
- 0073cf9c ["COPY", "tmp:0:8", ["const:875:8"]]
- 0073cf9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["COPY", "tmp:0:8", ["const:902:8"]]
+ 0073cf9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c bytes 29d52191
+ 0073cf9c bytes 29092491
- 0073d008 ["COPY", "tmp:0:8", ["const:bea:8"]]
- 0073d008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073d008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073d008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 0073d008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073d008 bytes 29a92f91
+ 0073d008 bytes 29dd3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c1764951398ed1d2bb075924465d4a"></a>

### [`0073da58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073da58.md) → [`0073da58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md) FUN_0073da58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`00853f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853f6c.md) · 呼出先 8件 [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574238.md) [`0073a8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a8e0.md) [`0073d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073d968.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00853f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853f6c.md) · 呼出先 8件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`0073a8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073daf4",
      "incomplete_value": true,
      "site": "0073dafc",
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
      "definition_site": "0073daf4",
      "incomplete_value": true,
      "site": "0073dafc",
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
      "0073dae8",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "0073dafc",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "0073db24",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073dae8",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073dafc",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073db24",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073dae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073da58.md#insn-0073dae8)
- 新版 [`0073dae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md#insn-0073dae8)

~~~diff
- 0073dae8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d30:8"]]
- 0073dae8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073dae8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:de0:8"]]
+ 0073dae8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073dae8 bytes f79a46f9
+ 0073dae8 bytes f7f246f9
~~~


<a id="compare-9fbd33fdc79e648a5ed320cacfab8313"></a>

### [`0073dc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073dc48.md) → [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md) FUN_0073dc48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md) [`0073addc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073addc.md) [`0073b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073b3dc.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) [`00adc400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc400.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 17件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0073addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md) [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00adc4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.41% / 新版 95.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073dcbc",
      "incomplete_value": true,
      "site": "0073dcbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073dcbc",
      "incomplete_value": true,
      "site": "0073dcbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:86b:8"
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
      "definition_site": "0073dcb0",
      "incomplete_value": true,
      "site": "0073dcc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073dcb0",
      "incomplete_value": true,
      "site": "0073dcc0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073dcac",
      "READ",
      [
        "storage",
        "002a086b",
        null,
        "string"
      ]
    ],
    [
      "0073dcb0",
      "READ",
      [
        "storage",
        "002a0872",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073dcac",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ],
    [
      "0073dcb0",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073dca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073dc48.md#insn-0073dca4)
- 新版 [`0073dca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md#insn-0073dca4)

~~~diff
- 0073dca4 ["COPY", "tmp:0:8", ["const:86b:8"]]
- 0073dca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0073dca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 bytes 29ad2191
+ 0073dca4 bytes 29e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c337f214a3fbecc7e2c222e66cc5a390"></a>

### [`0073de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073de68.md) → [`0073de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md) FUN_0073de68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00851b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/00851b9c.md) [`009a9ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) [`00845f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00845/00845f8c.md) [`00adc9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc9d0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 2件 [`00851b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00845f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845f8c.md) [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073def0",
      "incomplete_value": true,
      "site": "0073def0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073def0",
      "incomplete_value": true,
      "site": "0073def0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:86b:8"
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
      "definition_site": "0073dee4",
      "incomplete_value": true,
      "site": "0073def4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073dee4",
      "incomplete_value": true,
      "site": "0073def4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073dee0",
      "READ",
      [
        "storage",
        "002a086b",
        null,
        "string"
      ]
    ],
    [
      "0073dee4",
      "READ",
      [
        "storage",
        "002a0872",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073dee0",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ],
    [
      "0073dee4",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073ded8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073de68.md#insn-0073ded8)
- 新版 [`0073ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md#insn-0073ded8)

~~~diff
- 0073ded8 ["COPY", "tmp:0:8", ["const:86b:8"]]
- 0073ded8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0073ded8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 bytes 29ad2191
+ 0073ded8 bytes 29e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f4fc877f8a0ecf1fd4238665d895736"></a>

### [`0073e0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e0c8.md) → [`0073e0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e0c8.md) FUN_0073e0c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00996/00996ea0.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) [`00adcbb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adcbb8.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00996ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996ea0.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00adcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc80.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073e148",
      "incomplete_value": true,
      "site": "0073e158",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073e148",
      "incomplete_value": true,
      "site": "0073e158",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073e15c",
      "incomplete_value": true,
      "site": "0073e15c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073e15c",
      "incomplete_value": true,
      "site": "0073e15c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:86b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073e148",
      "READ",
      [
        "storage",
        "002a0872",
        null,
        "string"
      ]
    ],
    [
      "0073e14c",
      "READ",
      [
        "storage",
        "002a086b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073e148",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ],
    [
      "0073e14c",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073e140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e0c8.md#insn-0073e140)
- 新版 [`0073e140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e0c8.md#insn-0073e140)

~~~diff
- 0073e140 ["COPY", "tmp:0:8", ["const:86b:8"]]
- 0073e140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073e140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073e140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0073e140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073e140 bytes 29ad2191
+ 0073e140 bytes 29e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27a7f691dfb6051eec11220e8f21218"></a>

### [`0073ef14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ef14.md) → [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) FUN_0073ef14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0073f4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f4a8.md) [`0073f8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f8bc.md) [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) [`0085c4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c4c4.md) · 呼出先 11件 [`0051d884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d884.md) [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) [`0073bf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073b/0073bf10.md) [`0073d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073dc48.md)
- 新版 呼出元 6件 [`0073f4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md) [`0073f8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f8bc.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`0085c4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4c4.md) · 呼出先 11件 [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073f224",
      "incomplete_value": false,
      "site": "0073f22c",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f224",
      "incomplete_value": false,
      "site": "0073f22c",
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
            "const:d28:8"
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
      "0073f22c",
      "DATA",
      [
        "storage",
        "00bfad28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073f22c",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073f224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ef14.md#insn-0073f224)
- 新版 [`0073f224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md#insn-0073f224)

~~~diff
- 0073f224 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0073f224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073f224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073f224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0073f224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073f224 bytes 08a13491
+ 0073f224 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c2c27ae93f071f96a9b996ca7d0df24"></a>

### [`0073f4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f4a8.md) → [`0073f4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md) FUN_0073f4a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0084f0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084f/0084f0f8.md) [`008eeba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0073d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073dc48.md) [`0073ef14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ef14.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 2件 [`0084f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f0f8.md) [`008eeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md) [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.32% / 新版 94.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073f5a8",
      "incomplete_value": true,
      "site": "0073f5b8",
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
                "const:77d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f5a8",
      "incomplete_value": true,
      "site": "0073f5b8",
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
                "const:6f0:8"
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
      "definition_site": "0073f5ac",
      "incomplete_value": true,
      "site": "0073f5bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073f5ac",
      "incomplete_value": true,
      "site": "0073f5bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073f740",
      "incomplete_value": true,
      "site": "0073f750",
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
                "const:77d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f740",
      "incomplete_value": true,
      "site": "0073f750",
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
                "const:6f0:8"
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
      "0073f540",
      "READ",
      [
        "storage",
        "00293bea",
        null,
        "string"
      ]
    ],
    [
      "0073f544",
      "READ",
      [
        "storage",
        "00293bef",
        null,
        "string"
      ]
    ],
    [
      "0073f5a8",
      "READ",
      [
        "storage",
        "0029e6f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073f540",
      "READ",
      [
        "storage",
        "00293c77",
        null,
        "string"
      ]
    ],
    [
      "0073f544",
      "READ",
      [
        "storage",
        "00293c7c",
        null,
        "string"
      ]
    ],
    [
      "0073f5a8",
      "READ",
      [
        "storage",
        "0029e77d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073f538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f4a8.md#insn-0073f538) · [`0073f5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f4a8.md#insn-0073f5a0) · [`0073f5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073f4a8.md#insn-0073f5a4)
- 新版 [`0073f538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md#insn-0073f538) · [`0073f5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md#insn-0073f5a0)

~~~diff
- 0073f538 ["COPY", "tmp:0:8", ["const:bea:8"]]
- 0073f538 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["COPY", "tmp:0:8", ["const:c77:8"]]
+ 0073f538 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 bytes d6aa2f91
+ 0073f538 bytes d6de3191
- 0073f5a0 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0073f5a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["COPY", "tmp:0:8", ["const:77d:8"]]
+ 0073f5a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 bytes 08c11b91
+ 0073f5a0 bytes 08f51d91
- 0073f5a4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0073f5a4 bytes 89dbffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1896d3509086eef2a0a0ffedfde0c872"></a>

### [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) → [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) FUN_0073fa38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 267件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 267件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `store_value` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073fec4",
      "incomplete_value": false,
      "site": "0073fed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073fec4",
      "incomplete_value": false,
      "site": "0073fed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "definition_site": "0073fed8",
      "incomplete_value": false,
      "site": "0073fee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073fed8",
      "incomplete_value": false,
      "site": "0073fee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "definition_site": "00740108",
      "incomplete_value": false,
      "site": "00740110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00740108",
      "incomplete_value": false,
      "site": "00740110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073fa70",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0073fa7c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073fa84",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0073fa70",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0073fa7c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073fa84",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073fa70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa70) · [`0073fa7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa7c) · [`0073fa84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa84)
- 新版 [`0073fa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa70) · [`0073fa7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa7c) · [`0073fa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa84)

~~~diff
- 0073fa70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0073fa70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073fa70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0073fa70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0073fa70 bytes 08dd44f9
+ 0073fa70 bytes 083d45f9
- 0073fa7c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0073fa7c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0073fa7c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c bytes 21603691
+ 0073fa7c bytes 21203991
- 0073fa84 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0073fa84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0073fa84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 bytes 42800f91
+ 0073fa84 bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-916c71e37b22da9c34f9907162f5f135"></a>

### [`00748560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00748/00748560.md) → [`00748560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md) FUN_00748560

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md)
- 新版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.22% / 新版 95.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00748670",
      "incomplete_value": true,
      "site": "00748680",
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748670",
      "incomplete_value": true,
      "site": "00748680",
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
                "const:e5b:8"
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
      "definition_site": "00748904",
      "incomplete_value": true,
      "site": "00748918",
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
                "const:efa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748904",
      "incomplete_value": true,
      "site": "00748918",
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
                "const:e6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074891c",
      "incomplete_value": true,
      "site": "0074891c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0074891c",
      "incomplete_value": true,
      "site": "0074891c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00748670",
      "READ",
      [
        "storage",
        "00296e5b",
        null,
        "string"
      ]
    ],
    [
      "00748904",
      "READ",
      [
        "storage",
        "00296e6d",
        null,
        "string"
      ]
    ],
    [
      "0074890c",
      "READ",
      [
        "storage",
        "00296e7b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00748670",
      "READ",
      [
        "storage",
        "00296ee8",
        null,
        "string"
      ]
    ],
    [
      "00748904",
      "READ",
      [
        "storage",
        "00296efa",
        null,
        "string"
      ]
    ],
    [
      "0074890c",
      "READ",
      [
        "storage",
        "00296f08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00748/00748560.md#insn-00748668) · [`007488fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00748/00748560.md#insn-007488fc) · [`00748940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00748/00748560.md#insn-00748940)
- 新版 [`00748668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-00748668) · [`007488fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-007488fc) · [`00748940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-00748940)

~~~diff
- 00748668 ["COPY", "tmp:0:8", ["const:e5b:8"]]
- 00748668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00748668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00748668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00748668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00748668 bytes 296d3991
+ 00748668 bytes 29a13b91
- 007488fc ["COPY", "tmp:0:8", ["const:e6d:8"]]
- 007488fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007488fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007488fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["COPY", "tmp:0:8", ["const:efa:8"]]
+ 007488fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007488fc bytes 08b53991
+ 007488fc bytes 08e93b91
- 00748940 ["COPY", "tmp:0:8", ["const:d1b:8"]]
- 00748940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748940 ["COPY", "tmp:0:8", ["const:d12:8"]]
+ 00748940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748940 bytes 086d3491
+ 00748940 bytes 08493491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b8289e6112852fc499e6d2e87d2590"></a>

### [`00749514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md) → [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) FUN_00749514

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 126件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 126件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074b580",
      "incomplete_value": true,
      "site": "0074b580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:715:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074b580",
      "incomplete_value": true,
      "site": "0074b580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074b584",
      "incomplete_value": true,
      "site": "0074b584",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0074b584",
      "incomplete_value": true,
      "site": "0074b584",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0074954c",
      "incomplete_value": true,
      "site": "0074954c",
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
      "definition_site": "0074954c",
      "incomplete_value": true,
      "site": "0074954c",
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
      "00749548",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0074955c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00749564",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00749548",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0074955c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00749564",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md#insn-00749548) · [`0074955c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md#insn-0074955c) · [`00749564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md#insn-00749564)
- 新版 [`00749548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-00749548) · [`0074955c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-0074955c) · [`00749564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-00749564)

~~~diff
- 00749548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00749548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00749548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00749548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00749548 bytes 08dd44f9
+ 00749548 bytes 083d45f9
- 0074955c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0074955c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0074955c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0074955c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0074955c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0074955c bytes 21603691
+ 0074955c bytes 21203991
- 00749564 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 00749564 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00749564 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00749564 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00749564 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00749564 bytes 42800f91
+ 00749564 bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fd08de30751b0d6c0a457893e479aa"></a>

### [`0074ff74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0074f/0074ff74.md) → [`0074ff74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md) FUN_0074ff74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0074ffac",
      "incomplete_value": true,
      "site": "0074ffac",
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
      "definition_site": "0074ffac",
      "incomplete_value": true,
      "site": "0074ffac",
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
      "definition_site": "0074ffb4",
      "incomplete_value": false,
      "site": "0074ffc8",
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
      "definition_site": "0074ffb4",
      "incomplete_value": false,
      "site": "0074ffc8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0074ffbc",
      "incomplete_value": false,
      "site": "0074ffc8",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074ffbc",
      "incomplete_value": false,
      "site": "0074ffc8",
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
            "const:3e0:8"
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
      "0074ffa8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0074ffb4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0074ffbc",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0074ffa8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0074ffb4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0074ffbc",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074ffa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0074f/0074ff74.md#insn-0074ffa8) · [`0074ffb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0074f/0074ff74.md#insn-0074ffb4) · [`0074ffbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0074f/0074ff74.md#insn-0074ffbc)
- 新版 [`0074ffa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffa8) · [`0074ffb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffb4) · [`0074ffbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffbc)

~~~diff
- 0074ffa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0074ffa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0074ffa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0074ffa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0074ffa8 bytes 08dd44f9
+ 0074ffa8 bytes 083d45f9
- 0074ffb4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0074ffb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0074ffb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 bytes 21603691
+ 0074ffb4 bytes 21203991
- 0074ffbc ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0074ffbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0074ffbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc bytes 42800f91
+ 0074ffbc bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1d25df471a8494bfedaf31797e71677"></a>

### [`00750454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750454.md) → [`00750454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md) FUN_00750454

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00749/00749514.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md) [`0044abfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044abfc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md)
- 新版 呼出元 1件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

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
      "definition_site": "00750490",
      "incomplete_value": true,
      "site": "00750490",
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
      "definition_site": "00750490",
      "incomplete_value": true,
      "site": "00750490",
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
      "definition_site": "00750498",
      "incomplete_value": false,
      "site": "007504ac",
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
      "definition_site": "00750498",
      "incomplete_value": false,
      "site": "007504ac",
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
      "definition_site": "007504a0",
      "incomplete_value": false,
      "site": "007504ac",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007504a0",
      "incomplete_value": false,
      "site": "007504ac",
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
            "const:3e0:8"
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
      "0075048c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00750498",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007504a0",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0075048c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00750498",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007504a0",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075048c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750454.md#insn-0075048c) · [`00750498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750454.md#insn-00750498) · [`007504a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750454.md#insn-007504a0)
- 新版 [`0075048c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-0075048c) · [`00750498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-00750498) · [`007504a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-007504a0)

~~~diff
- 0075048c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0075048c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075048c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0075048c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0075048c bytes 08dd44f9
+ 0075048c bytes 083d45f9
- 00750498 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00750498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00750498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00750498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00750498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00750498 bytes 21603691
+ 00750498 bytes 21203991
- 007504a0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 007504a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007504a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007504a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 007504a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007504a0 bytes 42800f91
+ 007504a0 bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12ceefb10933c80025ec9bf6bb5a5d0"></a>

### [`00750ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750ac4.md) → [`00750ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md) FUN_00750ac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.88% / 新版 89.88%

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
      "definition_site": "00750b08",
      "incomplete_value": false,
      "site": "00750b0c",
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
      "definition_site": "00750b08",
      "incomplete_value": false,
      "site": "00750b0c",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00750b28",
      "incomplete_value": true,
      "site": "00750b38",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:cfa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00750b28",
      "incomplete_value": true,
      "site": "00750b38",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:d03:8"
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
      "definition_site": "00750b3c",
      "incomplete_value": true,
      "site": "00750b3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00750b3c",
      "incomplete_value": true,
      "site": "00750b3c",
      "value": [
        "LOAD",
        "8",
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
      "00750b0c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00750b28",
      "READ",
      [
        "storage",
        "002acd03",
        null,
        "string"
      ]
    ],
    [
      "00750b2c",
      "READ",
      [
        "storage",
        "002acd12",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00750b0c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00750b28",
      "READ",
      [
        "storage",
        "002accfa",
        null,
        "string"
      ]
    ],
    [
      "00750b2c",
      "READ",
      [
        "storage",
        "002acd09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00750b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750ac4.md#insn-00750b08) · [`00750b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750ac4.md#insn-00750b20) · [`00750b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00750/00750ac4.md#insn-00750b24)
- 新版 [`00750b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md#insn-00750b08) · [`00750b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md#insn-00750b20)

~~~diff
- 00750b08 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00750b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00750b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00750b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00750b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00750b08 bytes 29e13191
+ 00750b08 bytes 29a13491
- 00750b20 ["COPY", "tmp:0:8", ["const:d03:8"]]
- 00750b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00750b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00750b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00750b20 ["COPY", "tmp:0:8", ["const:cfa:8"]]
+ 00750b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00750b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00750b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00750b20 bytes 080d3491
+ 00750b20 bytes 08e93391
- 00750b24 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00750b24 bytes 09dbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab140b269501b6e899e81fb80db5bce"></a>

### [`0075171c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/0075171c.md) → [`0075171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md) FUN_0075171c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00751b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751b90.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`0072e2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072e/0072e2e4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00751b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751b90.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`0072e2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e2e4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00751738",
      "incomplete_value": false,
      "site": "0075173c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751738",
      "incomplete_value": false,
      "site": "0075173c",
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
            "const:ce8:8"
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
      "definition_site": "00751b48",
      "incomplete_value": false,
      "site": "00751b4c",
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
      "definition_site": "00751b48",
      "incomplete_value": false,
      "site": "00751b4c",
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
      "0075173c",
      "DATA",
      [
        "storage",
        "00bface8",
        null,
        "pointer"
      ]
    ],
    [
      "00751b10",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "00751b4c",
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
      "0075173c",
      "DATA",
      [
        "storage",
        "00bfad98",
        null,
        "pointer"
      ]
    ],
    [
      "00751b10",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751b4c",
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

- 旧版 [`00751738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/0075171c.md#insn-00751738) · [`00751b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/0075171c.md#insn-00751b0c) · [`00751b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/0075171c.md#insn-00751b48)
- 新版 [`00751738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751738) · [`00751b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751b0c) · [`00751b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751b48)

~~~diff
- 00751738 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00751738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00751738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751738 bytes 08a13391
+ 00751738 bytes 08613691
- 00751b0c ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00751b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00751b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751b0c bytes 08213491
+ 00751b0c bytes 08e13691
- 00751b48 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00751b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00751b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751b48 bytes 08a10791
+ 00751b48 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6873ac8239d1b8a09efd266fa8754494"></a>

### [`00751bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751bb4.md) → [`00751bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md) FUN_00751bb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00751bcc",
      "incomplete_value": false,
      "site": "00751bd0",
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
      "definition_site": "00751bcc",
      "incomplete_value": false,
      "site": "00751bd0",
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
      "definition_site": "00751c08",
      "incomplete_value": false,
      "site": "00751c0c",
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
      "definition_site": "00751c08",
      "incomplete_value": false,
      "site": "00751c0c",
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
      "00751bd0",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "00751c0c",
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
      "00751bd0",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751c0c",
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

- 旧版 [`00751bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751bb4.md#insn-00751bcc) · [`00751c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751bb4.md#insn-00751c08)
- 新版 [`00751bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md#insn-00751bcc) · [`00751c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md#insn-00751c08)

~~~diff
- 00751bcc ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00751bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00751bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751bcc bytes 08213491
+ 00751bcc bytes 08e13691
- 00751c08 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00751c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00751c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751c08 bytes 08a10791
+ 00751c08 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eb8cb159e537a34609328d4def1a479"></a>

### [`00751c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751c4c.md) → [`00751c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md) FUN_00751c4c

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
      "definition_site": "00751c64",
      "incomplete_value": false,
      "site": "00751c68",
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
      "definition_site": "00751c64",
      "incomplete_value": false,
      "site": "00751c68",
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
      "definition_site": "00751ca0",
      "incomplete_value": false,
      "site": "00751ca4",
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
      "definition_site": "00751ca0",
      "incomplete_value": false,
      "site": "00751ca4",
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
      "00751c68",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "00751ca4",
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
      "00751c68",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751ca4",
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

- 旧版 [`00751c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751c4c.md#insn-00751c64) · [`00751ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00751/00751c4c.md#insn-00751ca0)
- 新版 [`00751c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md#insn-00751c64) · [`00751ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md#insn-00751ca0)

~~~diff
- 00751c64 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00751c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00751c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751c64 bytes 08213491
+ 00751c64 bytes 08e13691
- 00751ca0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00751ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00751ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 bytes 08a10791
+ 00751ca0 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e931141bce174c11ed0ad972e0d57d6"></a>

### [`0075233c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/0075233c.md) → [`0075233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075233c.md) FUN_0075233c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00752340",
      "incomplete_value": false,
      "site": "00752344",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752340",
      "incomplete_value": false,
      "site": "00752344",
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
            "const:d28:8"
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
      "00752344",
      "DATA",
      [
        "storage",
        "00bfad28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00752344",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00752340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/0075233c.md#insn-00752340)
- 新版 [`00752340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075233c.md#insn-00752340)

~~~diff
- 00752340 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00752340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00752340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00752340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00752340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00752340 bytes 08a13491
+ 00752340 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc7f3259295cb442a3048a39457bdd3"></a>

### [`0075234c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/0075234c.md) → [`0075234c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075234c.md) FUN_0075234c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075235c",
      "incomplete_value": false,
      "site": "00752364",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075235c",
      "incomplete_value": false,
      "site": "00752364",
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
            "const:d28:8"
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
      "00752364",
      "DATA",
      [
        "storage",
        "00bfad28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00752364",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075235c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/0075234c.md#insn-0075235c)
- 新版 [`0075235c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075234c.md#insn-0075235c)

~~~diff
- 0075235c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0075235c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075235c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075235c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0075235c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075235c bytes 08a13491
+ 0075235c bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0858fa28201fd28af2fe8fdf76a6e606"></a>

### [`007525f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md) → [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) FUN_007525f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0075246c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/0075246c.md) [`007525f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0075246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075246c.md) [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.20% / 新版 99.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075278c",
      "incomplete_value": false,
      "site": "00752794",
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
      "definition_site": "0075278c",
      "incomplete_value": false,
      "site": "00752794",
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
      "definition_site": "00752844",
      "incomplete_value": false,
      "site": "0075284c",
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
      "definition_site": "00752844",
      "incomplete_value": false,
      "site": "0075284c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00752b8c",
      "incomplete_value": false,
      "site": "00752b9c",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752b8c",
      "incomplete_value": false,
      "site": "00752b9c",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0075278c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00752844",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00752b8c",
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
      "0075278c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00752844",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00752b8c",
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

- 旧版 [`0075278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md#insn-0075278c) · [`00752844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md#insn-00752844) · [`00752b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md#insn-00752b8c)
- 新版 [`0075278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-0075278c) · [`00752844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-00752844) · [`00752b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-00752b8c)

~~~diff
- 0075278c ["COPY", "tmp:0:8", ["const:311:8"]]
- 0075278c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075278c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075278c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0075278c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075278c bytes 21440c91
+ 0075278c bytes 21280c91
- 00752844 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00752844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00752844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00752844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00752844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00752844 bytes 21d40b91
+ 00752844 bytes 21b80b91
- 00752b8c ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00752b8c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00752b8c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00752b8c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00752b8c ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00752b8c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00752b8c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00752b8c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00752b8c bytes 63941791
+ 00752b8c bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6efb01addc1b558aa41101594e2dd22f"></a>

### [`007530d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md) → [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) FUN_007530d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007525f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007525f0.md) [`007530d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00753250",
      "incomplete_value": false,
      "site": "00753258",
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
      "definition_site": "00753250",
      "incomplete_value": false,
      "site": "00753258",
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
      "definition_site": "0075330c",
      "incomplete_value": false,
      "site": "00753314",
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
      "definition_site": "0075330c",
      "incomplete_value": false,
      "site": "00753314",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007536d8",
      "incomplete_value": false,
      "site": "007536e8",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007536d8",
      "incomplete_value": false,
      "site": "007536e8",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00753250",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0075330c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "007536d8",
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
      "00753250",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0075330c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "007536d8",
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

- 旧版 [`00753250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md#insn-00753250) · [`0075330c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md#insn-0075330c) · [`007536d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md#insn-007536d8)
- 新版 [`00753250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-00753250) · [`0075330c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-0075330c) · [`007536d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-007536d8)

~~~diff
- 00753250 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00753250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00753250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753250 bytes 21440c91
+ 00753250 bytes 21280c91
- 0075330c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0075330c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075330c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075330c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0075330c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075330c bytes 21d40b91
+ 0075330c bytes 21b80b91
- 007536d8 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 007536d8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 007536d8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 007536d8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 007536d8 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 007536d8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 007536d8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 007536d8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 007536d8 bytes 63941791
+ 007536d8 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1ca38736ffc5b80e5968c4d06b9428"></a>

### [`00753c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md) → [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) FUN_00753c40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007530d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/007530d8.md) [`00753c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00753db0",
      "incomplete_value": false,
      "site": "00753db8",
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
      "definition_site": "00753db0",
      "incomplete_value": false,
      "site": "00753db8",
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
      "definition_site": "00753f08",
      "incomplete_value": false,
      "site": "00753f10",
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
      "definition_site": "00753f08",
      "incomplete_value": false,
      "site": "00753f10",
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
      "definition_site": "00753fb0",
      "incomplete_value": false,
      "site": "00753fbc",
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
      "definition_site": "00753fb0",
      "incomplete_value": false,
      "site": "00753fbc",
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
      "00753db0",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00753f08",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00753fb0",
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
      "00753db0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00753f08",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00753fb0",
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

- 旧版 [`00753db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md#insn-00753db0) · [`00753f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md#insn-00753f08) · [`00753fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md#insn-00753fb0)
- 新版 [`00753db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753db0) · [`00753f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753f08) · [`00753fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753fb0)

~~~diff
- 00753db0 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00753db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00753db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753db0 bytes 21440c91
+ 00753db0 bytes 21280c91
- 00753f08 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00753f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00753f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753f08 bytes 21d40b91
+ 00753f08 bytes 21b80b91
- 00753fb0 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00753fb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753fb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753fb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753fb0 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00753fb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753fb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753fb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753fb0 bytes 21681f91
+ 00753fb0 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c10968faae1ea83c60a18242d4c8f1"></a>

### [`007545ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md) → [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) FUN_007545ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00753c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00753/00753c40.md) [`007545ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00754754",
      "incomplete_value": false,
      "site": "0075475c",
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
      "definition_site": "00754754",
      "incomplete_value": false,
      "site": "0075475c",
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
      "definition_site": "00754954",
      "incomplete_value": false,
      "site": "00754960",
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
      "definition_site": "00754954",
      "incomplete_value": false,
      "site": "00754960",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00754bc8",
      "incomplete_value": false,
      "site": "00754bd8",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00754bc8",
      "incomplete_value": false,
      "site": "00754bd8",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00754754",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "007548ac",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00754954",
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
      "00754754",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "007548ac",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00754954",
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

- 旧版 [`00754754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md#insn-00754754) · [`007548ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md#insn-007548ac) · [`00754954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md#insn-00754954)
- 新版 [`00754754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-00754754) · [`007548ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-007548ac) · [`00754954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-00754954)

~~~diff
- 00754754 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00754754 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00754754 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00754754 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00754754 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00754754 bytes 21440c91
+ 00754754 bytes 21280c91
- 007548ac ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 007548ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007548ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007548ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 007548ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007548ac bytes 21d40b91
+ 007548ac bytes 21b80b91
- 00754954 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00754954 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00754954 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00754954 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00754954 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00754954 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00754954 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00754954 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00754954 bytes 21681f91
+ 00754954 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ff81744b204eb63427aebfe3d5e729"></a>

### [`00754f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md) → [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) FUN_00754f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007545ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/007545ec.md) [`00754f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007550d4",
      "incomplete_value": false,
      "site": "007550dc",
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
      "definition_site": "007550d4",
      "incomplete_value": false,
      "site": "007550dc",
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
      "definition_site": "0075522c",
      "incomplete_value": false,
      "site": "00755234",
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
      "definition_site": "0075522c",
      "incomplete_value": false,
      "site": "00755234",
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
      "definition_site": "007552d4",
      "incomplete_value": false,
      "site": "007552e0",
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
      "definition_site": "007552d4",
      "incomplete_value": false,
      "site": "007552e0",
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
      "007550d4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0075522c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "007552d4",
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
      "007550d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0075522c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "007552d4",
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

- 旧版 [`007550d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md#insn-007550d4) · [`0075522c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md#insn-0075522c) · [`007552d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md#insn-007552d4)
- 新版 [`007550d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-007550d4) · [`0075522c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-0075522c) · [`007552d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-007552d4)

~~~diff
- 007550d4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 007550d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007550d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007550d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 007550d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007550d4 bytes 21440c91
+ 007550d4 bytes 21280c91
- 0075522c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0075522c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075522c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075522c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0075522c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075522c bytes 21d40b91
+ 0075522c bytes 21b80b91
- 007552d4 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 007552d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007552d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007552d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007552d4 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 007552d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007552d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007552d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007552d4 bytes 21681f91
+ 007552d4 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63da9896968efdb5a8b474d0b238ba2e"></a>

### [`007558dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md) → [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) FUN_007558dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00754f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00754/00754f70.md) [`007558dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00755b98",
      "incomplete_value": false,
      "site": "00755ba0",
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
      "definition_site": "00755b98",
      "incomplete_value": false,
      "site": "00755ba0",
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
      "definition_site": "00755f90",
      "incomplete_value": false,
      "site": "00755f98",
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
      "definition_site": "00755f90",
      "incomplete_value": false,
      "site": "00755f98",
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
      "00755a40",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00755b98",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00755c40",
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
      "00755a40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00755b98",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00755c40",
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

- 旧版 [`00755a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md#insn-00755a40) · [`00755b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md#insn-00755b98) · [`00755c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md#insn-00755c40)
- 新版 [`00755a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755a40) · [`00755b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755b98) · [`00755c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755c40)

~~~diff
- 00755a40 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00755a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00755a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755a40 bytes 21440c91
+ 00755a40 bytes 21280c91
- 00755b98 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00755b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00755b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755b98 bytes 21d40b91
+ 00755b98 bytes 21b80b91
- 00755c40 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00755c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755c40 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00755c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755c40 bytes 21681f91
+ 00755c40 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33213be904b1ff77f1761e3cf9672d09"></a>

### [`00756248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md) → [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) FUN_00756248

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007558dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00755/007558dc.md) [`00756248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007563a8",
      "incomplete_value": false,
      "site": "007563b0",
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
      "definition_site": "007563a8",
      "incomplete_value": false,
      "site": "007563b0",
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
      "definition_site": "00756500",
      "incomplete_value": false,
      "site": "00756508",
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
      "definition_site": "00756500",
      "incomplete_value": false,
      "site": "00756508",
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
      "definition_site": "007565a8",
      "incomplete_value": false,
      "site": "007565b4",
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
      "definition_site": "007565a8",
      "incomplete_value": false,
      "site": "007565b4",
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
      "007563a8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00756500",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "007565a8",
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
      "007563a8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00756500",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "007565a8",
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

- 旧版 [`007563a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md#insn-007563a8) · [`00756500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md#insn-00756500) · [`007565a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md#insn-007565a8)
- 新版 [`007563a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-007563a8) · [`00756500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-00756500) · [`007565a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-007565a8)

~~~diff
- 007563a8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 007563a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007563a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007563a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 007563a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007563a8 bytes 21440c91
+ 007563a8 bytes 21280c91
- 00756500 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00756500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00756500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756500 bytes 21d40b91
+ 00756500 bytes 21b80b91
- 007565a8 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 007565a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007565a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007565a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007565a8 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 007565a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007565a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007565a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007565a8 bytes 21681f91
+ 007565a8 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb86083b2294a14d8a63030b1f30d01f"></a>

### [`00756ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756ba0.md) → [`00756ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md) FUN_00756ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00756248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756248.md) [`00756ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756ba0.md) [`00a00ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a00/00a00ca0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) [`00756ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md) [`00a00ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a00/00a00ca0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00756d00",
      "incomplete_value": false,
      "site": "00756d08",
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
      "definition_site": "00756d00",
      "incomplete_value": false,
      "site": "00756d08",
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
      "definition_site": "00756e58",
      "incomplete_value": false,
      "site": "00756e60",
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
      "definition_site": "00756e58",
      "incomplete_value": false,
      "site": "00756e60",
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
      "definition_site": "00756f00",
      "incomplete_value": false,
      "site": "00756f0c",
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
      "definition_site": "00756f00",
      "incomplete_value": false,
      "site": "00756f0c",
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
      "00756d00",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00756e58",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00756f00",
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
      "00756d00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00756e58",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00756f00",
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

- 旧版 [`00756d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756ba0.md#insn-00756d00) · [`00756e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756ba0.md#insn-00756e58) · [`00756f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00756/00756ba0.md#insn-00756f00)
- 新版 [`00756d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756d00) · [`00756e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756e58) · [`00756f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756f00)

~~~diff
- 00756d00 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00756d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00756d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756d00 bytes 21440c91
+ 00756d00 bytes 21280c91
- 00756e58 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00756e58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756e58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756e58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00756e58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756e58 bytes 21d40b91
+ 00756e58 bytes 21b80b91
- 00756f00 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00756f00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756f00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756f00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756f00 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00756f00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756f00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756f00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756f00 bytes 21681f91
+ 00756f00 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4134d2b50d363bf394a0793f261a8623"></a>

### [`00757514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757514.md) → [`00757514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757514.md) FUN_00757514

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
      "definition_site": "00757538",
      "incomplete_value": false,
      "site": "00757538",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757538",
      "incomplete_value": false,
      "site": "00757538",
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
            "const:d78:8"
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
      "00757538",
      "DATA",
      [
        "storage",
        "00bfad78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757538",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757514.md#insn-00757534)
- 新版 [`00757534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757514.md#insn-00757534)

~~~diff
- 00757534 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00757534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00757534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757534 bytes 08e13591
+ 00757534 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36d7b113b724b0fbf301d65943edd7b9"></a>

### [`00757548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757548.md) → [`00757548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757548.md) FUN_00757548

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
      "definition_site": "00757554",
      "incomplete_value": false,
      "site": "00757554",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757554",
      "incomplete_value": false,
      "site": "00757554",
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
            "const:d78:8"
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
      "00757554",
      "DATA",
      [
        "storage",
        "00bfad78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757554",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757548.md#insn-00757550)
- 新版 [`00757550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757548.md#insn-00757550)

~~~diff
- 00757550 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00757550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00757550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757550 bytes 29e13591
+ 00757550 bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bbbe2e97150379c754bcb038c5ab1d9"></a>

### [`007575fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007575fc.md) → [`007575fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007575fc.md) FUN_007575fc

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
      "definition_site": "00757620",
      "incomplete_value": false,
      "site": "00757620",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757620",
      "incomplete_value": false,
      "site": "00757620",
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
            "const:df8:8"
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
      "00757620",
      "DATA",
      [
        "storage",
        "00bfadf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757620",
      "DATA",
      [
        "storage",
        "00bfaea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075761c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007575fc.md#insn-0075761c)
- 新版 [`0075761c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007575fc.md#insn-0075761c)

~~~diff
- 0075761c ["COPY", "tmp:0:8", ["const:df8:8"]]
- 0075761c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0075761c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075761c bytes 08e13791
+ 0075761c bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71f07369e3183cc6d6a2418b07a3cf9"></a>

### [`00757630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757630.md) → [`00757630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757630.md) FUN_00757630

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
      "definition_site": "0075763c",
      "incomplete_value": false,
      "site": "0075763c",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075763c",
      "incomplete_value": false,
      "site": "0075763c",
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
            "const:df8:8"
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
      "0075763c",
      "DATA",
      [
        "storage",
        "00bfadf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075763c",
      "DATA",
      [
        "storage",
        "00bfaea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757630.md#insn-00757638)
- 新版 [`00757638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757630.md#insn-00757638)

~~~diff
- 00757638 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00757638 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757638 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757638 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00757638 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757638 bytes 29e13791
+ 00757638 bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5d64f0e3d6d7ed7e395339f068f8ae"></a>

### [`007576dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007576dc.md) → [`007576dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007576dc.md) FUN_007576dc

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
      "definition_site": "00757700",
      "incomplete_value": true,
      "site": "00757700",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757700",
      "incomplete_value": true,
      "site": "00757700",
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
            "const:e78:8"
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
      "00757700",
      "DATA",
      [
        "storage",
        "00bfae78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757700",
      "DATA",
      [
        "storage",
        "00bfaf28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007576fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007576dc.md#insn-007576fc)
- 新版 [`007576fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007576dc.md#insn-007576fc)

~~~diff
- 007576fc ["COPY", "tmp:0:8", ["const:e78:8"]]
- 007576fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007576fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007576fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007576fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007576fc bytes 08e13991
+ 007576fc bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936df5c6988c13729c018d5ba8fdc092"></a>

### [`00757710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757710.md) → [`00757710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757710.md) FUN_00757710

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
      "definition_site": "0075771c",
      "incomplete_value": false,
      "site": "0075771c",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075771c",
      "incomplete_value": false,
      "site": "0075771c",
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
            "const:e78:8"
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
      "0075771c",
      "DATA",
      [
        "storage",
        "00bfae78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075771c",
      "DATA",
      [
        "storage",
        "00bfaf28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757710.md#insn-00757718)
- 新版 [`00757718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757710.md#insn-00757718)

~~~diff
- 00757718 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00757718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00757718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757718 bytes 29e13991
+ 00757718 bytes 29a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826dd5809a3c314b38583feaab05cbf6"></a>

### [`0075772c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/0075772c.md) → [`0075772c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075772c.md) FUN_0075772c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00883c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883c6c.md) [`00883cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00883c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c6c.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00757868",
      "incomplete_value": false,
      "site": "0075786c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:5cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757868",
      "incomplete_value": false,
      "site": "0075786c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:5d6:8"
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
      "00757868",
      "PARAM",
      [
        "storage",
        "002a35d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00757868",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/0075772c.md#insn-00757868)
- 新版 [`00757868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075772c.md#insn-00757868)

~~~diff
- 00757868 ["COPY", "tmp:0:8", ["const:5d6:8"]]
- 00757868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00757868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00757868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["COPY", "tmp:0:8", ["const:5cf:8"]]
+ 00757868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00757868 bytes 00581791
+ 00757868 bytes 003c1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75b6061e4b71608975d8af27168d8251"></a>

### [`0075789c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/0075789c.md) → [`0075789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075789c.md) FUN_0075789c

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
      "definition_site": "007578c0",
      "incomplete_value": false,
      "site": "007578c0",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007578c0",
      "incomplete_value": false,
      "site": "007578c0",
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
            "const:ef8:8"
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
      "007578c0",
      "DATA",
      [
        "storage",
        "00bfaef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007578c0",
      "DATA",
      [
        "storage",
        "00bfafa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007578bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/0075789c.md#insn-007578bc)
- 新版 [`007578bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075789c.md#insn-007578bc)

~~~diff
- 007578bc ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007578bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007578bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007578bc bytes 08e13b91
+ 007578bc bytes 08a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae8e2023391449456c839e404cff8f5f"></a>

### [`007578d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007578d0.md) → [`007578d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007578d0.md) FUN_007578d0

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
      "definition_site": "007578dc",
      "incomplete_value": false,
      "site": "007578dc",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007578dc",
      "incomplete_value": false,
      "site": "007578dc",
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
            "const:ef8:8"
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
      "007578dc",
      "DATA",
      [
        "storage",
        "00bfaef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007578dc",
      "DATA",
      [
        "storage",
        "00bfafa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007578d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007578d0.md#insn-007578d8)
- 新版 [`007578d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007578d0.md#insn-007578d8)

~~~diff
- 007578d8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007578d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007578d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007578d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007578d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007578d8 bytes 29e13b91
+ 007578d8 bytes 29a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4157708eeadb613dbc3b38c735a0d6b9"></a>

### [`007579a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579a4.md) → [`007579a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579a4.md) FUN_007579a4

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
      "definition_site": "007579c8",
      "incomplete_value": false,
      "site": "007579c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007579c8",
      "incomplete_value": false,
      "site": "007579c8",
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
            "const:f78:8"
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
      "007579c8",
      "DATA",
      [
        "storage",
        "00bfaf78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007579c8",
      "DATA",
      [
        "storage",
        "00bfb028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007579c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579a4.md#insn-007579c0) · [`007579c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579a4.md#insn-007579c4)
- 新版 [`007579c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579a4.md#insn-007579c0) · [`007579c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579a4.md#insn-007579c4)

~~~diff
- 007579c0 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007579c0 ["COPY", "register:4040:8", ["const:bfb000:8"]]
- 007579c0 bytes 082500f0
+ 007579c0 bytes 28250090
- 007579c4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007579c4 bytes 08e13d91
+ 007579c4 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3bd2194d09c9d0fbbfb6c4e1003767f"></a>

### [`007579d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579d8.md) → [`007579d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579d8.md) FUN_007579d8

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
      "definition_site": "007579e4",
      "incomplete_value": false,
      "site": "007579e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007579e4",
      "incomplete_value": false,
      "site": "007579e4",
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
            "const:f78:8"
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
      "007579e4",
      "DATA",
      [
        "storage",
        "00bfaf78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007579e4",
      "DATA",
      [
        "storage",
        "00bfb028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007579dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579d8.md#insn-007579dc) · [`007579e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579d8.md#insn-007579e0)
- 新版 [`007579dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579d8.md#insn-007579dc) · [`007579e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579d8.md#insn-007579e0)

~~~diff
- 007579dc ["COPY", "register:4048:8", ["const:bfa000:8"]]
+ 007579dc ["COPY", "register:4048:8", ["const:bfb000:8"]]
- 007579dc bytes 092500f0
+ 007579dc bytes 29250090
- 007579e0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007579e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007579e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007579e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007579e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007579e0 bytes 29e13d91
+ 007579e0 bytes 29a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-889898ffb75c3b06c2a2530942bb9c1e"></a>

### [`007579f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579f4.md) → [`007579f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md) FUN_007579f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.17% / 新版 93.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00757b8c",
      "incomplete_value": true,
      "site": "00757b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757b8c",
      "incomplete_value": true,
      "site": "00757b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:698:8"
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
      "definition_site": "00757b94",
      "incomplete_value": true,
      "site": "00757b94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00757b94",
      "incomplete_value": true,
      "site": "00757b94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00757ba8",
      "incomplete_value": true,
      "site": "00757ba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00757ba8",
      "incomplete_value": true,
      "site": "00757ba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00757b74",
      "READ",
      [
        "storage",
        "0029d698",
        null,
        "string"
      ]
    ],
    [
      "00757b7c",
      "READ",
      [
        "storage",
        "0029d69e",
        null,
        "string"
      ]
    ],
    [
      "00757b90",
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
      "00757b74",
      "READ",
      [
        "storage",
        "0029d725",
        null,
        "string"
      ]
    ],
    [
      "00757b7c",
      "READ",
      [
        "storage",
        "0029d72b",
        null,
        "string"
      ]
    ],
    [
      "00757b90",
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

- 旧版 [`00757b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579f4.md#insn-00757b70) · [`00757b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/007579f4.md#insn-00757b80)
- 新版 [`00757b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md#insn-00757b70) · [`00757b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md#insn-00757b80)

~~~diff
- 00757b70 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00757b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["COPY", "tmp:0:8", ["const:725:8"]]
+ 00757b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757b70 bytes 29611a91
+ 00757b70 bytes 29951c91
- 00757b80 ["COPY", "register:4048:8", ["const:2aa000:8"]]
- 00757b80 bytes 89dafff0
+ 00757b80 ["COPY", "register:4048:8", ["const:2aa000:8"]]
+ 00757b80 bytes 89dafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af4bf3f51d593a8ef50b3c420fe1bcb"></a>

### [`00757f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f0c.md) → [`00757f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f0c.md) FUN_00757f0c

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
      "definition_site": "00757f20",
      "incomplete_value": false,
      "site": "00757f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757f20",
      "incomplete_value": false,
      "site": "00757f24",
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
            "const:fe8:8"
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
      "00757f24",
      "DATA",
      [
        "storage",
        "00bfafe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757f24",
      "DATA",
      [
        "storage",
        "00bfb098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f0c.md#insn-00757f1c) · [`00757f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f0c.md#insn-00757f20)
- 新版 [`00757f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f0c.md#insn-00757f1c) · [`00757f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f0c.md#insn-00757f20)

~~~diff
- 00757f1c ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00757f1c ["COPY", "register:4040:8", ["const:bfb000:8"]]
- 00757f1c bytes 082500f0
+ 00757f1c bytes 28250090
- 00757f20 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00757f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00757f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757f20 bytes 08a13f91
+ 00757f20 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb86ba181a7bc147d4574df2afab8734"></a>

### [`00757f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f30.md) → [`00757f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f30.md) FUN_00757f30

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
      "definition_site": "00757f34",
      "incomplete_value": false,
      "site": "00757f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757f34",
      "incomplete_value": false,
      "site": "00757f38",
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
            "const:fe8:8"
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
      "00757f38",
      "DATA",
      [
        "storage",
        "00bfafe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757f38",
      "DATA",
      [
        "storage",
        "00bfb098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f30.md#insn-00757f30) · [`00757f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f30.md#insn-00757f34)
- 新版 [`00757f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f30.md#insn-00757f30) · [`00757f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f30.md#insn-00757f34)

~~~diff
- 00757f30 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00757f30 ["COPY", "register:4040:8", ["const:bfb000:8"]]
- 00757f30 bytes 082500f0
+ 00757f30 bytes 28250090
- 00757f34 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00757f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00757f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757f34 bytes 08a13f91
+ 00757f34 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af62ba6d8284d4a973240be6f561ff2"></a>

### [`00757f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f48.md) → [`00757f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md) FUN_00757f48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00757ff0",
      "incomplete_value": true,
      "site": "00758000",
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757ff0",
      "incomplete_value": true,
      "site": "00758000",
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
                "const:ac2:8"
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
      "definition_site": "00758004",
      "incomplete_value": true,
      "site": "00758004",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00758004",
      "incomplete_value": true,
      "site": "00758004",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007580cc",
      "incomplete_value": false,
      "site": "007580cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007580cc",
      "incomplete_value": false,
      "site": "007580cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00757ff0",
      "READ",
      [
        "storage",
        "002abac2",
        null,
        "string"
      ]
    ],
    [
      "00757ff8",
      "READ",
      [
        "storage",
        "002abad0",
        null,
        "string"
      ]
    ],
    [
      "007580cc",
      "DATA",
      [
        "storage",
        "00bfb058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757ff0",
      "READ",
      [
        "storage",
        "002abac8",
        null,
        "string"
      ]
    ],
    [
      "00757ff8",
      "READ",
      [
        "storage",
        "002abad6",
        null,
        "string"
      ]
    ],
    [
      "007580cc",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f48.md#insn-00757fec) · [`007580c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f48.md#insn-007580c4) · [`007580c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00757/00757f48.md#insn-007580c8)
- 新版 [`00757fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md#insn-00757fec) · [`007580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md#insn-007580c4)

~~~diff
- 00757fec ["COPY", "tmp:0:8", ["const:ac2:8"]]
- 00757fec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757fec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757fec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757fec ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00757fec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757fec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757fec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757fec bytes 29092b91
+ 00757fec bytes 29212b91
- 007580c4 ["COPY", "tmp:0:8", ["const:58:8"]]
- 007580c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007580c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007580c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 007580c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007580c4 bytes 08610191
+ 007580c4 bytes 08210491
- 007580c8 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
- 007580c8 bytes b40301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbdfb9aa348e8858f5fe67a9c74951d3"></a>

### [`0075833c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/0075833c.md) → [`0075833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/0075833c.md) FUN_0075833c

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
      "definition_site": "00758350",
      "incomplete_value": false,
      "site": "00758354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758350",
      "incomplete_value": false,
      "site": "00758354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00758354",
      "DATA",
      [
        "storage",
        "00bfb058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758354",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/0075833c.md#insn-00758350)
- 新版 [`00758350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/0075833c.md#insn-00758350)

~~~diff
- 00758350 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00758350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00758350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758350 bytes 08610191
+ 00758350 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae1b0c9da9a4d55e6c4751db13dee8ea"></a>

### [`00758360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758360.md) → [`00758360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758360.md) FUN_00758360

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
      "definition_site": "00758364",
      "incomplete_value": false,
      "site": "00758368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758364",
      "incomplete_value": false,
      "site": "00758368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00758368",
      "DATA",
      [
        "storage",
        "00bfb058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758368",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758360.md#insn-00758364)
- 新版 [`00758364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758360.md#insn-00758364)

~~~diff
- 00758364 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00758364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00758364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758364 bytes 08610191
+ 00758364 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad9ba75b87e2aafb37a642b29a1bb09"></a>

### [`00758378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758378.md) → [`00758378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md) FUN_00758378

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f23b4.md) [`0072f020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072f/0072f020.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md) [`0072f020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072f/0072f020.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00758454",
      "incomplete_value": false,
      "site": "0075845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758454",
      "incomplete_value": false,
      "site": "0075845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0075845c",
      "DATA",
      [
        "storage",
        "00bfb0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "007584b4",
      "READ",
      [
        "storage",
        "00bfb0e8",
        null,
        "pointer"
      ]
    ],
    [
      "007584b4",
      "READ",
      [
        "storage",
        "00bfb0f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075845c",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ],
    [
      "007584b4",
      "READ",
      [
        "storage",
        "00bfb198",
        null,
        "pointer"
      ]
    ],
    [
      "007584b4",
      "READ",
      [
        "storage",
        "00bfb1a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758378.md#insn-00758454) · [`00758458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758378.md#insn-00758458)
- 新版 [`00758454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md#insn-00758454) · [`00758458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md#insn-00758458)

~~~diff
- 00758454 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00758454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758454 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 00758454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758454 bytes 08210391
+ 00758454 bytes 08e10591
- 00758458 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00758458 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00758458 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00758458 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00758458 bytes f5c30091
+ 00758458 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00758458 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 00758458 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 00758458 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 00758458 bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ce32e937b40c6d822dcee6edaaeaac"></a>

### [`007585d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007585d0.md) → [`007585d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585d0.md) FUN_007585d0

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
      "definition_site": "007585e4",
      "incomplete_value": false,
      "site": "007585e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585e4",
      "incomplete_value": false,
      "site": "007585e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "007585e8",
      "DATA",
      [
        "storage",
        "00bfb0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007585e8",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007585d0.md#insn-007585e4)
- 新版 [`007585e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585d0.md#insn-007585e4)

~~~diff
- 007585e4 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 007585e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007585e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585e4 bytes 08210391
+ 007585e4 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc2a6457ff870a13d3dcbc41c7f584ec"></a>

### [`007585f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007585f4.md) → [`007585f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585f4.md) FUN_007585f4

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
      "definition_site": "007585f8",
      "incomplete_value": false,
      "site": "007585fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585f8",
      "incomplete_value": false,
      "site": "007585fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "007585fc",
      "DATA",
      [
        "storage",
        "00bfb0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007585fc",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007585f4.md#insn-007585f8)
- 新版 [`007585f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585f4.md#insn-007585f8)

~~~diff
- 007585f8 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 007585f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 007585f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585f8 bytes 08210391
+ 007585f8 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc4ff8575e1cc59cae059ee78d76233"></a>

### [`007586cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007586cc.md) → [`007586cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586cc.md) FUN_007586cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "007586d8",
      "incomplete_value": false,
      "site": "007586dc",
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
      "definition_site": "007586d8",
      "incomplete_value": false,
      "site": "007586dc",
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
      "007586d8",
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
      "007586d8",
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

- 旧版 [`007586d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007586cc.md#insn-007586d8)
- 新版 [`007586d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586cc.md#insn-007586d8)

~~~diff
- 007586d8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007586d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 007586d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007586d8 bytes 00280c91
+ 007586d8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f13373a6472206220a387d210403e82"></a>

### [`007586e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007586e4.md) → [`007586e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586e4.md) FUN_007586e4

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
      "definition_site": "00758708",
      "incomplete_value": false,
      "site": "00758708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758708",
      "incomplete_value": false,
      "site": "00758708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "00758708",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758708",
      "DATA",
      [
        "storage",
        "00bfb228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007586e4.md#insn-00758704)
- 新版 [`00758704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586e4.md#insn-00758704)

~~~diff
- 00758704 ["COPY", "tmp:0:8", ["const:178:8"]]
- 00758704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00758704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758704 bytes 08e10591
+ 00758704 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28123208b3551079c0cef82022928cb0"></a>

### [`00758718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758718.md) → [`00758718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758718.md) FUN_00758718

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
      "definition_site": "00758724",
      "incomplete_value": false,
      "site": "00758724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758724",
      "incomplete_value": false,
      "site": "00758724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "00758724",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758724",
      "DATA",
      [
        "storage",
        "00bfb228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758718.md#insn-00758720)
- 新版 [`00758720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758718.md#insn-00758720)

~~~diff
- 00758720 ["COPY", "tmp:0:8", ["const:178:8"]]
- 00758720 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00758720 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00758720 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00758720 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00758720 bytes 29e10591
+ 00758720 bytes 29a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4643a441aba9185cff76d8b1910fa764"></a>

### [`007587d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007587d4.md) → [`007587d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587d4.md) FUN_007587d4

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
      "definition_site": "007587e8",
      "incomplete_value": false,
      "site": "007587ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007587e8",
      "incomplete_value": false,
      "site": "007587ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007587ec",
      "DATA",
      [
        "storage",
        "00bfb1f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007587ec",
      "DATA",
      [
        "storage",
        "00bfb2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007587e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007587d4.md#insn-007587e8)
- 新版 [`007587e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587d4.md#insn-007587e8)

~~~diff
- 007587e8 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007587e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007587e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007587e8 bytes 08e10791
+ 007587e8 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1edfb15634de4e4ef6a36df8acff51"></a>

### [`007587f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007587f8.md) → [`007587f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587f8.md) FUN_007587f8

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
      "definition_site": "007587fc",
      "incomplete_value": false,
      "site": "00758800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007587fc",
      "incomplete_value": false,
      "site": "00758800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "00758800",
      "DATA",
      [
        "storage",
        "00bfb1f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758800",
      "DATA",
      [
        "storage",
        "00bfb2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007587fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007587f8.md#insn-007587fc)
- 新版 [`007587fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587f8.md#insn-007587fc)

~~~diff
- 007587fc ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007587fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007587fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007587fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007587fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007587fc bytes 08e10791
+ 007587fc bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c1132c5ced41060b628c655e9c76247"></a>

### [`00758884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758884.md) → [`00758884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758884.md) FUN_00758884

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
      "definition_site": "00758898",
      "incomplete_value": false,
      "site": "0075889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758898",
      "incomplete_value": false,
      "site": "0075889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "0075889c",
      "DATA",
      [
        "storage",
        "00bfb278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075889c",
      "DATA",
      [
        "storage",
        "00bfb328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758884.md#insn-00758898)
- 新版 [`00758898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758884.md#insn-00758898)

~~~diff
- 00758898 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00758898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00758898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758898 bytes 08e10991
+ 00758898 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12b6524196a0e98bce4f6124e27aec5a"></a>

### [`007588a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007588a8.md) → [`007588a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007588a8.md) FUN_007588a8

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
      "definition_site": "007588ac",
      "incomplete_value": false,
      "site": "007588b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007588ac",
      "incomplete_value": false,
      "site": "007588b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "007588b0",
      "DATA",
      [
        "storage",
        "00bfb278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007588b0",
      "DATA",
      [
        "storage",
        "00bfb328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007588ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/007588a8.md#insn-007588ac)
- 新版 [`007588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007588a8.md#insn-007588ac)

~~~diff
- 007588ac ["COPY", "tmp:0:8", ["const:278:8"]]
- 007588ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007588ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007588ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["COPY", "tmp:0:8", ["const:328:8"]]
+ 007588ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007588ac bytes 08e10991
+ 007588ac bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed3f0270ab2fb1c3232fed82196d0af"></a>

### [`00758934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758934.md) → [`00758934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758934.md) FUN_00758934

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
      "definition_site": "00758948",
      "incomplete_value": false,
      "site": "0075894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758948",
      "incomplete_value": false,
      "site": "0075894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0075894c",
      "DATA",
      [
        "storage",
        "00bfb2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075894c",
      "DATA",
      [
        "storage",
        "00bfb3a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758934.md#insn-00758948)
- 新版 [`00758948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758934.md#insn-00758948)

~~~diff
- 00758948 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00758948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00758948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758948 bytes 08e10b91
+ 00758948 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d2cdae1e48c6dcfc00f682bf9045e78"></a>

### [`00758958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758958.md) → [`00758958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758958.md) FUN_00758958

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
      "definition_site": "0075895c",
      "incomplete_value": false,
      "site": "00758960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075895c",
      "incomplete_value": false,
      "site": "00758960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "00758960",
      "DATA",
      [
        "storage",
        "00bfb2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758960",
      "DATA",
      [
        "storage",
        "00bfb3a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075895c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758958.md#insn-0075895c)
- 新版 [`0075895c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758958.md#insn-0075895c)

~~~diff
- 0075895c ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0075895c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075895c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075895c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0075895c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075895c bytes 08e10b91
+ 0075895c bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fa84960e7174f09979a29fefc5d8200"></a>

### [`00758a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758a0c.md) → [`00758a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a0c.md) FUN_00758a0c

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
      "definition_site": "00758a20",
      "incomplete_value": false,
      "site": "00758a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758a20",
      "incomplete_value": false,
      "site": "00758a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00758a24",
      "DATA",
      [
        "storage",
        "00bfb378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758a24",
      "DATA",
      [
        "storage",
        "00bfb428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758a0c.md#insn-00758a20)
- 新版 [`00758a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a0c.md#insn-00758a20)

~~~diff
- 00758a20 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00758a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00758a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758a20 bytes 08e10d91
+ 00758a20 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68187753a07c68a68e59c17278612757"></a>

### [`00758a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758a30.md) → [`00758a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a30.md) FUN_00758a30

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
      "definition_site": "00758a34",
      "incomplete_value": false,
      "site": "00758a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758a34",
      "incomplete_value": false,
      "site": "00758a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00758a38",
      "DATA",
      [
        "storage",
        "00bfb378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758a38",
      "DATA",
      [
        "storage",
        "00bfb428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758a30.md#insn-00758a34)
- 新版 [`00758a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a30.md#insn-00758a34)

~~~diff
- 00758a34 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00758a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00758a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758a34 bytes 08e10d91
+ 00758a34 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29ed73970d5085295a5cbb5da22a5d65"></a>

### [`00758abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758abc.md) → [`00758abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758abc.md) FUN_00758abc

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
      "definition_site": "00758ad0",
      "incomplete_value": false,
      "site": "00758ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ad0",
      "incomplete_value": false,
      "site": "00758ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00758ad4",
      "DATA",
      [
        "storage",
        "00bfb3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ad4",
      "DATA",
      [
        "storage",
        "00bfb4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758abc.md#insn-00758ad0)
- 新版 [`00758ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758abc.md#insn-00758ad0)

~~~diff
- 00758ad0 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00758ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 00758ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 bytes 08e10f91
+ 00758ad0 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd649c712827508e6bae290f32c660a"></a>

### [`00758ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ae0.md) → [`00758ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ae0.md) FUN_00758ae0

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
      "definition_site": "00758ae4",
      "incomplete_value": false,
      "site": "00758ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ae4",
      "incomplete_value": false,
      "site": "00758ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00758ae8",
      "DATA",
      [
        "storage",
        "00bfb3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ae8",
      "DATA",
      [
        "storage",
        "00bfb4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ae0.md#insn-00758ae4)
- 新版 [`00758ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ae0.md#insn-00758ae4)

~~~diff
- 00758ae4 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00758ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 00758ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 bytes 08e10f91
+ 00758ae4 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfc5fbd04223f9303fa6754b916abcbe"></a>

### [`00758b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758b64.md) → [`00758b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b64.md) FUN_00758b64

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
      "definition_site": "00758b78",
      "incomplete_value": false,
      "site": "00758b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758b78",
      "incomplete_value": false,
      "site": "00758b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00758b7c",
      "DATA",
      [
        "storage",
        "00bfb478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758b7c",
      "DATA",
      [
        "storage",
        "00bfb528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758b64.md#insn-00758b78)
- 新版 [`00758b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b64.md#insn-00758b78)

~~~diff
- 00758b78 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00758b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00758b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758b78 bytes 08e11191
+ 00758b78 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45e8958b5cdf2261b1d8545675914d86"></a>

### [`00758b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758b88.md) → [`00758b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b88.md) FUN_00758b88

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
      "definition_site": "00758b8c",
      "incomplete_value": false,
      "site": "00758b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758b8c",
      "incomplete_value": false,
      "site": "00758b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "00758b90",
      "DATA",
      [
        "storage",
        "00bfb478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758b90",
      "DATA",
      [
        "storage",
        "00bfb528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758b88.md#insn-00758b8c)
- 新版 [`00758b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b88.md#insn-00758b8c)

~~~diff
- 00758b8c ["COPY", "tmp:0:8", ["const:478:8"]]
- 00758b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00758b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758b8c bytes 08e11191
+ 00758b8c bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117b7c062cd596e6aa0e57bf977322e6"></a>

### [`00758c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758c34.md) → [`00758c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c34.md) FUN_00758c34

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
      "definition_site": "00758c48",
      "incomplete_value": false,
      "site": "00758c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758c48",
      "incomplete_value": false,
      "site": "00758c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00758c4c",
      "DATA",
      [
        "storage",
        "00bfb4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758c4c",
      "DATA",
      [
        "storage",
        "00bfb5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758c34.md#insn-00758c48)
- 新版 [`00758c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c34.md#insn-00758c48)

~~~diff
- 00758c48 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00758c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00758c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758c48 bytes 08e11391
+ 00758c48 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f6e8f3ecfebd074e7f6625308f5d669"></a>

### [`00758c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758c58.md) → [`00758c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c58.md) FUN_00758c58

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
      "definition_site": "00758c5c",
      "incomplete_value": false,
      "site": "00758c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758c5c",
      "incomplete_value": false,
      "site": "00758c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "00758c60",
      "DATA",
      [
        "storage",
        "00bfb4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758c60",
      "DATA",
      [
        "storage",
        "00bfb5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758c58.md#insn-00758c5c)
- 新版 [`00758c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c58.md#insn-00758c5c)

~~~diff
- 00758c5c ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00758c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00758c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758c5c bytes 08e11391
+ 00758c5c bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e82948c67a46cca1bd2ad766f69c0ec"></a>

### [`00758ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ce4.md) → [`00758ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ce4.md) FUN_00758ce4

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
      "definition_site": "00758cf8",
      "incomplete_value": false,
      "site": "00758cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758cf8",
      "incomplete_value": false,
      "site": "00758cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "00758cfc",
      "DATA",
      [
        "storage",
        "00bfb578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758cfc",
      "DATA",
      [
        "storage",
        "00bfb628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ce4.md#insn-00758cf8)
- 新版 [`00758cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ce4.md#insn-00758cf8)

~~~diff
- 00758cf8 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00758cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00758cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 bytes 08e11591
+ 00758cf8 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5277194a56e6abc8a9519acca184df"></a>

### [`00758d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758d08.md) → [`00758d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d08.md) FUN_00758d08

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
      "definition_site": "00758d0c",
      "incomplete_value": false,
      "site": "00758d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758d0c",
      "incomplete_value": false,
      "site": "00758d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "00758d10",
      "DATA",
      [
        "storage",
        "00bfb578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758d10",
      "DATA",
      [
        "storage",
        "00bfb628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758d08.md#insn-00758d0c)
- 新版 [`00758d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d08.md#insn-00758d0c)

~~~diff
- 00758d0c ["COPY", "tmp:0:8", ["const:578:8"]]
- 00758d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00758d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758d0c bytes 08e11591
+ 00758d0c bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a7a67ae49926f50e7410de2e32069ae"></a>

### [`00758d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758d94.md) → [`00758d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d94.md) FUN_00758d94

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
      "definition_site": "00758da8",
      "incomplete_value": false,
      "site": "00758dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758da8",
      "incomplete_value": false,
      "site": "00758dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00758dac",
      "DATA",
      [
        "storage",
        "00bfb5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758dac",
      "DATA",
      [
        "storage",
        "00bfb6a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758d94.md#insn-00758da8)
- 新版 [`00758da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d94.md#insn-00758da8)

~~~diff
- 00758da8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00758da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00758da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758da8 bytes 08e11791
+ 00758da8 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9a0578f3f3f18d3d84dd4d107ee988"></a>

### [`00758db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758db8.md) → [`00758db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758db8.md) FUN_00758db8

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
      "definition_site": "00758dbc",
      "incomplete_value": false,
      "site": "00758dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758dbc",
      "incomplete_value": false,
      "site": "00758dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00758dc0",
      "DATA",
      [
        "storage",
        "00bfb5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758dc0",
      "DATA",
      [
        "storage",
        "00bfb6a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758db8.md#insn-00758dbc)
- 新版 [`00758dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758db8.md#insn-00758dbc)

~~~diff
- 00758dbc ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00758dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00758dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758dbc bytes 08e11791
+ 00758dbc bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdce0ed43896c22ebf118da7f5272c26"></a>

### [`00758dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758dd0.md) → [`00758dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758dd0.md) FUN_00758dd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00429384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429384.md) [`0042949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/0042949c.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00429384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429384.md) [`0042949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/0042949c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00758e44",
      "incomplete_value": true,
      "site": "00758e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00758e44",
      "incomplete_value": true,
      "site": "00758e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00758e30",
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
      "00758e30",
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

- 旧版 [`00758e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758dd0.md#insn-00758e28)
- 新版 [`00758e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758dd0.md#insn-00758e28)

~~~diff
- 00758e28 ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 00758e28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00758e28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00758e28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00758e28 ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 00758e28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00758e28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00758e28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00758e28 bytes 29851291
+ 00758e28 bytes 299d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-607332d908f4b4da8dd15c4963743121"></a>

### [`00758f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758f24.md) → [`00758f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f24.md) FUN_00758f24

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
      "definition_site": "00758f38",
      "incomplete_value": false,
      "site": "00758f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758f38",
      "incomplete_value": false,
      "site": "00758f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00758f3c",
      "DATA",
      [
        "storage",
        "00bfb678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758f3c",
      "DATA",
      [
        "storage",
        "00bfb728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758f24.md#insn-00758f38)
- 新版 [`00758f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f24.md#insn-00758f38)

~~~diff
- 00758f38 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00758f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00758f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758f38 bytes 08e11991
+ 00758f38 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08088bccc94600d43a25ffcb53261cc8"></a>

### [`00758f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758f48.md) → [`00758f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f48.md) FUN_00758f48

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
      "definition_site": "00758f4c",
      "incomplete_value": false,
      "site": "00758f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758f4c",
      "incomplete_value": false,
      "site": "00758f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00758f50",
      "DATA",
      [
        "storage",
        "00bfb678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758f50",
      "DATA",
      [
        "storage",
        "00bfb728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758f48.md#insn-00758f4c)
- 新版 [`00758f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f48.md#insn-00758f4c)

~~~diff
- 00758f4c ["COPY", "tmp:0:8", ["const:678:8"]]
- 00758f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00758f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758f4c bytes 08e11991
+ 00758f4c bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-260b0a8534d9a31e6a32ba48eff00da7"></a>

### [`00758ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ff4.md) → [`00758ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ff4.md) FUN_00758ff4

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
      "definition_site": "00758ff8",
      "incomplete_value": false,
      "site": "00758ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ff8",
      "incomplete_value": false,
      "site": "00758ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00758ffc",
      "DATA",
      [
        "storage",
        "00bfb6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ffc",
      "DATA",
      [
        "storage",
        "00bfb7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00758/00758ff4.md#insn-00758ff8)
- 新版 [`00758ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ff4.md#insn-00758ff8)

~~~diff
- 00758ff8 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00758ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00758ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 bytes 08e11b91
+ 00758ff8 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc9a8b9d4f2993aae0b2ab820c6683d"></a>

### [`0075900c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075900c.md) → [`0075900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075900c.md) FUN_0075900c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0042bf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bf64.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0042bf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bf64.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00759064",
      "incomplete_value": true,
      "site": "00759064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00759064",
      "incomplete_value": true,
      "site": "00759064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00759054",
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
      "00759054",
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

- 旧版 [`0075904c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075900c.md#insn-0075904c)
- 新版 [`0075904c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075900c.md#insn-0075904c)

~~~diff
- 0075904c ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 0075904c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075904c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075904c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075904c ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 0075904c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075904c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075904c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075904c bytes 29851291
+ 0075904c bytes 299d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fda2b8c3b62173e006f32ee8bc7173"></a>

### [`0075916c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075916c.md) → [`0075916c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075916c.md) FUN_0075916c

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
      "definition_site": "00759180",
      "incomplete_value": false,
      "site": "00759184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759180",
      "incomplete_value": false,
      "site": "00759184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00759184",
      "DATA",
      [
        "storage",
        "00bfb778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759184",
      "DATA",
      [
        "storage",
        "00bfb828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075916c.md#insn-00759180)
- 新版 [`00759180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075916c.md#insn-00759180)

~~~diff
- 00759180 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00759180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00759180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759180 bytes 08e11d91
+ 00759180 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6522c56b9dfbabe7a648910d70fd26c7"></a>

### [`00759190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759190.md) → [`00759190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759190.md) FUN_00759190

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
      "definition_site": "00759194",
      "incomplete_value": false,
      "site": "00759198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759194",
      "incomplete_value": false,
      "site": "00759198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00759198",
      "DATA",
      [
        "storage",
        "00bfb778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759198",
      "DATA",
      [
        "storage",
        "00bfb828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759190.md#insn-00759194)
- 新版 [`00759194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759190.md#insn-00759194)

~~~diff
- 00759194 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00759194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00759194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759194 bytes 08e11d91
+ 00759194 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6655baf4447732b538fed9d3e36fc5"></a>

### [`00759248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759248.md) → [`00759248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759248.md) FUN_00759248

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
      "definition_site": "0075925c",
      "incomplete_value": false,
      "site": "00759260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075925c",
      "incomplete_value": false,
      "site": "00759260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00759260",
      "DATA",
      [
        "storage",
        "00bfb7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759260",
      "DATA",
      [
        "storage",
        "00bfb8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075925c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759248.md#insn-0075925c)
- 新版 [`0075925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759248.md#insn-0075925c)

~~~diff
- 0075925c ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 0075925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0075925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075925c bytes 08e11f91
+ 0075925c bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1abe08149d051fb56fe3e1f3cb9f18"></a>

### [`0075926c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075926c.md) → [`0075926c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075926c.md) FUN_0075926c

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
      "definition_site": "00759270",
      "incomplete_value": false,
      "site": "00759274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759270",
      "incomplete_value": false,
      "site": "00759274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00759274",
      "DATA",
      [
        "storage",
        "00bfb7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759274",
      "DATA",
      [
        "storage",
        "00bfb8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/0075926c.md#insn-00759270)
- 新版 [`00759270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075926c.md#insn-00759270)

~~~diff
- 00759270 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00759270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 00759270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759270 bytes 08e11f91
+ 00759270 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d15e154b23dec0bcf4902c2f59ec3ca"></a>

### [`007592ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/007592ec.md) → [`007592ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/007592ec.md) FUN_007592ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "007592f8",
      "incomplete_value": false,
      "site": "007592fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007592f8",
      "incomplete_value": false,
      "site": "007592fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "007592fc",
      "DATA",
      [
        "storage",
        "00bfb878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007592fc",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007592f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/007592ec.md#insn-007592f8)
- 新版 [`007592f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/007592ec.md#insn-007592f8)

~~~diff
- 007592f8 ["COPY", "tmp:0:8", ["const:878:8"]]
- 007592f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007592f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007592f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 007592f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007592f8 bytes 29e12191
+ 007592f8 bytes 29a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-defb017486ed27a70a4716392dea353c"></a>

### [`00759310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759310.md) → [`00759310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759310.md) FUN_00759310

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00759318",
      "incomplete_value": false,
      "site": "0075931c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759318",
      "incomplete_value": false,
      "site": "0075931c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "0075931c",
      "DATA",
      [
        "storage",
        "00bfb878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075931c",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759310.md#insn-00759318)
- 新版 [`00759318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759310.md#insn-00759318)

~~~diff
- 00759318 ["COPY", "tmp:0:8", ["const:878:8"]]
- 00759318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00759318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00759318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00759318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00759318 bytes 29e12191
+ 00759318 bytes 29a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b52d675bf8e196931ecab7ea6903b63c"></a>

### [`00759350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759350.md) → [`00759350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759350.md) FUN_00759350

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`007523a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00752/007523a8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007523a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007523a8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00759370",
      "incomplete_value": false,
      "site": "00759378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759370",
      "incomplete_value": false,
      "site": "00759378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "00759378",
      "DATA",
      [
        "storage",
        "00bfb878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759378",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759350.md#insn-00759370)
- 新版 [`00759370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759350.md#insn-00759370)

~~~diff
- 00759370 ["COPY", "tmp:0:8", ["const:878:8"]]
- 00759370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00759370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759370 bytes 08e12191
+ 00759370 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe1e09bd18d0f6aad00647e9922aab4f"></a>

### [`00759544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759544.md) → [`00759544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md) FUN_00759544

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.27% / 新版 98.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00759910",
      "incomplete_value": true,
      "site": "00759910",
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
            "const:ff9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759910",
      "incomplete_value": true,
      "site": "00759910",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007599b4",
      "incomplete_value": false,
      "site": "007599b4",
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
      "definition_site": "007599b4",
      "incomplete_value": false,
      "site": "007599b4",
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
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00759a4c",
      "incomplete_value": false,
      "site": "00759a50",
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
            "const:9f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759a4c",
      "incomplete_value": false,
      "site": "00759a50",
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
            "const:9ef:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007598b0",
      "PARAM",
      [
        "storage",
        "002aa9ef",
        null,
        "string"
      ]
    ],
    [
      "00759910",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "00759964",
      "READ",
      [
        "storage",
        "0029e72c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007598b0",
      "PARAM",
      [
        "storage",
        "002aa9f5",
        null,
        "string"
      ]
    ],
    [
      "00759910",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "00759964",
      "READ",
      [
        "storage",
        "0029e7b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007598b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759544.md#insn-007598b0) · [`00759908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759544.md#insn-00759908) · [`00759960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759544.md#insn-00759960)
- 新版 [`007598b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md#insn-007598b0) · [`00759908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md#insn-00759908) · [`00759960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md#insn-00759960)

~~~diff
- 007598b0 ["COPY", "tmp:0:8", ["const:9ef:8"]]
- 007598b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007598b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007598b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007598b0 ["COPY", "tmp:0:8", ["const:9f5:8"]]
+ 007598b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007598b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007598b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007598b0 bytes 42bc2791
+ 007598b0 bytes 42d42791
- 00759908 ["COPY", "tmp:0:8", ["const:f6c:8"]]
- 00759908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["COPY", "tmp:0:8", ["const:ff9:8"]]
+ 00759908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759908 bytes 08b13d91
+ 00759908 bytes 08e53f91
- 00759960 ["COPY", "tmp:0:8", ["const:72c:8"]]
- 00759960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["COPY", "tmp:0:8", ["const:7b9:8"]]
+ 00759960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759960 bytes 08b11c91
+ 00759960 bytes 08e51e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e1e520197875fb41c1cdc1a70ad97d"></a>

### [`00759e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759e68.md) → [`00759e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e68.md) FUN_00759e68

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
      "definition_site": "00759e8c",
      "incomplete_value": false,
      "site": "00759e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759e8c",
      "incomplete_value": false,
      "site": "00759e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00759e8c",
      "DATA",
      [
        "storage",
        "00bfb8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759e8c",
      "DATA",
      [
        "storage",
        "00bfb9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759e68.md#insn-00759e88)
- 新版 [`00759e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e68.md#insn-00759e88)

~~~diff
- 00759e88 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00759e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00759e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759e88 bytes 08e12391
+ 00759e88 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3bb0cb5f1483590aa5482f3f5413f6"></a>

### [`00759e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759e9c.md) → [`00759e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e9c.md) FUN_00759e9c

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
      "definition_site": "00759ea8",
      "incomplete_value": false,
      "site": "00759ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759ea8",
      "incomplete_value": false,
      "site": "00759ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00759ea8",
      "DATA",
      [
        "storage",
        "00bfb8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759ea8",
      "DATA",
      [
        "storage",
        "00bfb9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759e9c.md#insn-00759ea4)
- 新版 [`00759ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e9c.md#insn-00759ea4)

~~~diff
- 00759ea4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00759ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00759ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 bytes 29e12391
+ 00759ea4 bytes 29a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bbb49ee7758632697091827bd2d9bcc"></a>

### [`00759f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759f48.md) → [`00759f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f48.md) FUN_00759f48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00759f6c",
      "incomplete_value": false,
      "site": "00759f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759f6c",
      "incomplete_value": false,
      "site": "00759f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "00759f70",
      "DATA",
      [
        "storage",
        "00bfb978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759f70",
      "DATA",
      [
        "storage",
        "00bfba28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759f48.md#insn-00759f6c)
- 新版 [`00759f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f48.md#insn-00759f6c)

~~~diff
- 00759f6c ["COPY", "tmp:0:8", ["const:978:8"]]
- 00759f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00759f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759f6c bytes 08e12591
+ 00759f6c bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c361ba54a46c3b3e2a5e7498983c1eca"></a>

### [`00759f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759f88.md) → [`00759f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f88.md) FUN_00759f88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00759f8c",
      "incomplete_value": false,
      "site": "00759f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759f8c",
      "incomplete_value": false,
      "site": "00759f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "00759f90",
      "DATA",
      [
        "storage",
        "00bfb978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759f90",
      "DATA",
      [
        "storage",
        "00bfba28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759f88.md#insn-00759f8c)
- 新版 [`00759f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f88.md#insn-00759f8c)

~~~diff
- 00759f8c ["COPY", "tmp:0:8", ["const:978:8"]]
- 00759f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00759f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759f8c bytes 08e12591
+ 00759f8c bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f674b7e6b9b93b1d1226133dc80ef378"></a>

### [`00759fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759fb0.md) → [`00759fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md) FUN_00759fb0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075a0b8",
      "incomplete_value": true,
      "site": "0075a0b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e34:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a0b8",
      "incomplete_value": true,
      "site": "0075a0b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da7:8"
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
      "definition_site": "0075a0ac",
      "incomplete_value": true,
      "site": "0075a0bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0075a0ac",
      "incomplete_value": true,
      "site": "0075a0bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075a0d8",
      "incomplete_value": false,
      "site": "0075a0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a0d8",
      "incomplete_value": false,
      "site": "0075a0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "0075a0a8",
      "READ",
      [
        "storage",
        "00291da7",
        null,
        "string"
      ]
    ],
    [
      "0075a0ac",
      "READ",
      [
        "storage",
        "00291dae",
        null,
        "string"
      ]
    ],
    [
      "0075a0d8",
      "DATA",
      [
        "storage",
        "00bfba68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a0a8",
      "READ",
      [
        "storage",
        "00291e34",
        null,
        "string"
      ]
    ],
    [
      "0075a0ac",
      "READ",
      [
        "storage",
        "00291e3b",
        null,
        "string"
      ]
    ],
    [
      "0075a0d8",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759fb0.md#insn-0075a0a0) · [`0075a0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759fb0.md#insn-0075a0d0) · [`0075a0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759fb0.md#insn-0075a0d4)
- 新版 [`0075a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md#insn-0075a0a0) · [`0075a0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md#insn-0075a0d0)

~~~diff
- 0075a0a0 ["COPY", "tmp:0:8", ["const:da7:8"]]
- 0075a0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["COPY", "tmp:0:8", ["const:e34:8"]]
+ 0075a0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 bytes 299d3691
+ 0075a0a0 bytes 29d13891
- 0075a0d0 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0075a0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0075a0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 bytes 08a12991
+ 0075a0d0 bytes 08612c91
- 0075a0d4 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:b0:8"]]
- 0075a0d4 bytes b3c302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf267c74042787bcebdad8a56708477"></a>

### [`0075a7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075a7b4.md) → [`0075a7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7b4.md) FUN_0075a7b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0075a7d8",
      "incomplete_value": false,
      "site": "0075a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a7d8",
      "incomplete_value": false,
      "site": "0075a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "0075a7dc",
      "DATA",
      [
        "storage",
        "00bfb9e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a7dc",
      "DATA",
      [
        "storage",
        "00bfba98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075a7b4.md#insn-0075a7d8)
- 新版 [`0075a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7b4.md#insn-0075a7d8)

~~~diff
- 0075a7d8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0075a7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0075a7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 bytes 08a12791
+ 0075a7d8 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55cd8c57fc6420a835adf62b0444be4e"></a>

### [`0075a7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075a7f4.md) → [`0075a7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7f4.md) FUN_0075a7f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0075a7f8",
      "incomplete_value": false,
      "site": "0075a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a7f8",
      "incomplete_value": false,
      "site": "0075a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "0075a7fc",
      "DATA",
      [
        "storage",
        "00bfb9e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a7fc",
      "DATA",
      [
        "storage",
        "00bfba98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a7f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075a7f4.md#insn-0075a7f8)
- 新版 [`0075a7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7f4.md#insn-0075a7f8)

~~~diff
- 0075a7f8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0075a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0075a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 bytes 08a12791
+ 0075a7f8 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bec3298bcbbaf166a5b1398af20860e"></a>

### [`0075ac88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075ac88.md) → [`0075ac88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ac88.md) FUN_0075ac88

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
      "definition_site": "0075acac",
      "incomplete_value": false,
      "site": "0075acac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075acac",
      "incomplete_value": false,
      "site": "0075acac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "0075acac",
      "DATA",
      [
        "storage",
        "00bfba68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075acac",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075aca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075ac88.md#insn-0075aca8)
- 新版 [`0075aca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ac88.md#insn-0075aca8)

~~~diff
- 0075aca8 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0075aca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0075aca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 bytes 08a12991
+ 0075aca8 bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfbc1cfe28ab51dd181424ba62cce1bd"></a>

### [`0075acbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075acbc.md) → [`0075acbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075acbc.md) FUN_0075acbc

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
      "definition_site": "0075acc8",
      "incomplete_value": false,
      "site": "0075acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075acc8",
      "incomplete_value": false,
      "site": "0075acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "0075acc8",
      "DATA",
      [
        "storage",
        "00bfba68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075acc8",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075acc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075acbc.md#insn-0075acc4)
- 新版 [`0075acc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075acbc.md#insn-0075acc4)

~~~diff
- 0075acc4 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0075acc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0075acc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 bytes 29a12991
+ 0075acc4 bytes 29612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4735df3701030a89f90b1bc6a4907e50"></a>

### [`0075ada8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075ada8.md) → [`0075ada8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ada8.md) FUN_0075ada8

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
      "definition_site": "0075adbc",
      "incomplete_value": false,
      "site": "0075adc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075adbc",
      "incomplete_value": false,
      "site": "0075adc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "0075adc0",
      "DATA",
      [
        "storage",
        "00bfbaf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075adc0",
      "DATA",
      [
        "storage",
        "00bfbba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075adbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075a/0075ada8.md#insn-0075adbc)
- 新版 [`0075adbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ada8.md#insn-0075adbc)

~~~diff
- 0075adbc ["COPY", "tmp:0:8", ["const:af8:8"]]
- 0075adbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075adbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075adbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 0075adbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075adbc bytes 08e12b91
+ 0075adbc bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

