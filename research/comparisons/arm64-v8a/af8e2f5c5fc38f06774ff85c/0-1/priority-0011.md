# v15.7.2 → v15.7.3 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-2185f729b027a287194034a3508e5ca1"></a>

### [`004e01ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e01ec.md) → [`004e01ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e01ec.md) _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb30.md) · 呼出先 17件 [`004f3cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3cec.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528a6c.md)
- 新版 呼出元 1件 [`00bdcbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbe0.md) · 呼出先 17件 [`004f3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3cec.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e03c0",
      "incomplete_value": true,
      "site": "004e03c0",
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
      "definition_site": "004e03c0",
      "incomplete_value": true,
      "site": "004e03c0",
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
      "definition_site": "004e0404",
      "incomplete_value": true,
      "site": "004e0408",
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
      "definition_site": "004e0404",
      "incomplete_value": true,
      "site": "004e0408",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e0314",
      "incomplete_value": false,
      "site": "004e031c",
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
            "const:617:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0314",
      "incomplete_value": false,
      "site": "004e031c",
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
            "const:58a:8"
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
      "004e0314",
      "PARAM",
      [
        "storage",
        "002a058a",
        null,
        "string"
      ]
    ],
    [
      "004e0364",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004e0364",
      "PARAM",
      [
        "storage",
        "00be91e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e0314",
      "PARAM",
      [
        "storage",
        "002a0617",
        null,
        "string"
      ]
    ],
    [
      "004e0364",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004e0364",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e01ec.md#insn-004e0314) · [`004e0364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e01ec.md#insn-004e0364) · [`004e03b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e01ec.md#insn-004e03b0)
- 新版 `004e0314`（命令位置の公開資料なし） · `004e0364`（命令位置の公開資料なし） · `004e03b0`（命令位置の公開資料なし）

~~~diff
- 004e0314 ["COPY", "tmp:0:8", ["const:58a:8"]]
- 004e0314 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e0314 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e0314 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e0314 ["COPY", "tmp:0:8", ["const:617:8"]]
+ 004e0314 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0314 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0314 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e0314 bytes 21281691
+ 004e0314 bytes 215c1891
- 004e0364 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004e0364 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0364 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004e0364 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0364 bytes 212047f9
+ 004e0364 bytes 217847f9
- 004e03b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
- 004e03b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e03b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004e03b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e03b0 bytes 081941f9
+ 004e03b0 bytes 087141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b356ea05ff70e39e93da18ed615f438"></a>

### [`004e0894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md) → [`004e0894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0894.md) _ZN5Botan9CRL_Entry11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb60.md) · 呼出先 16件 [`0048bb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bb9c.md) [`004e0c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0c08.md) [`004f4778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md) [`00525efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525efc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bdcc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc10.md) · 呼出先 16件 [`0048bb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bb9c.md) [`004e0c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0c08.md) [`004f4778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md) [`00525efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525efc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e08e8",
      "incomplete_value": true,
      "site": "004e08e8",
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
      "definition_site": "004e08e8",
      "incomplete_value": true,
      "site": "004e08e8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e090c",
      "incomplete_value": true,
      "site": "004e090c",
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
      "definition_site": "004e090c",
      "incomplete_value": true,
      "site": "004e090c",
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
      "definition_site": "004e09f4",
      "incomplete_value": true,
      "site": "004e09f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e09f4",
      "incomplete_value": true,
      "site": "004e09f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:963:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e08d8",
      "READ",
      [
        "storage",
        "00c1aec0",
        null,
        "pointer"
      ]
    ],
    [
      "004e08e8",
      "DATA",
      [
        "storage",
        "00be92b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e08f8",
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e08d8",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004e08e8",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e08f8",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e08d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md#insn-004e08d8) · [`004e08f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md#insn-004e08f8) · [`004e09dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md#insn-004e09dc)
- 新版 `004e08d8`（命令位置の公開資料なし） · `004e08f8`（命令位置の公開資料なし） · `004e09dc`（命令位置の公開資料なし）

~~~diff
- 004e08d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 004e08d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e08d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004e08d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e08d8 bytes 086147f9
+ 004e08d8 bytes 08b947f9
- 004e08f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
- 004e08f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e08f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
+ 004e08f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e08f8 bytes 081141f9
+ 004e08f8 bytes 086941f9
- 004e09dc ["COPY", "tmp:0:8", ["const:963:8"]]
- 004e09dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e09dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e09dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e09dc ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 004e09dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e09dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e09dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e09dc bytes 298d2591
+ 004e09dc bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e014884fff3707ad02931206a24d7e0"></a>

### [`004e0c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0c08.md) → [`004e0c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0c08.md) FUN_004e0c08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e0894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`004e0894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0894.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004e0c44",
      "incomplete_value": true,
      "site": "004e0c44",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "004e0c44",
      "incomplete_value": true,
      "site": "004e0c44",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e0c80",
      "incomplete_value": false,
      "site": "004e0c88",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0c80",
      "incomplete_value": false,
      "site": "004e0c88",
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
            "const:92d:8"
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
      "definition_site": "004e0cbc",
      "incomplete_value": true,
      "site": "004e0cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0cbc",
      "incomplete_value": true,
      "site": "004e0cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
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
      "004e0c34",
      "READ",
      [
        "storage",
        "00c1b228",
        null,
        "pointer"
      ]
    ],
    [
      "004e0c80",
      "PARAM",
      [
        "storage",
        "0029492d",
        null,
        "string"
      ]
    ],
    [
      "004e0cbc",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e0c34",
      "READ",
      [
        "storage",
        "00c1b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "004e0c80",
      "PARAM",
      [
        "storage",
        "002949ba",
        null,
        "string"
      ]
    ],
    [
      "004e0cbc",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0c08.md#insn-004e0c34) · [`004e0c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0c08.md#insn-004e0c80) · [`004e0cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0c08.md#insn-004e0cbc)
- 新版 `004e0c34`（命令位置の公開資料なし） · `004e0c80`（命令位置の公開資料なし） · `004e0cbc`（命令位置の公開資料なし）

~~~diff
- 004e0c34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 004e0c34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0c34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d8:8"]]
+ 004e0c34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0c34 bytes 081541f9
+ 004e0c34 bytes 086d41f9
- 004e0c80 ["COPY", "tmp:0:8", ["const:92d:8"]]
- 004e0c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e0c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e0c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e0c80 ["COPY", "tmp:0:8", ["const:9ba:8"]]
+ 004e0c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e0c80 bytes 21b42491
+ 004e0c80 bytes 21e82691
- 004e0cbc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 004e0cbc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0cbc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 004e0cbc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0cbc bytes 214c47f9
+ 004e0cbc bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4df09ef24b598a5286dc55ba3b3a74c"></a>

### [`004e0d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0d1c.md) → [`004e0d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0d1c.md) FUN_004e0d1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e0d54",
      "incomplete_value": true,
      "site": "004e0d54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0d54",
      "incomplete_value": true,
      "site": "004e0d54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:963:8"
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
      "004e0d44",
      "READ",
      [
        "storage",
        "00296963",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e0d44",
      "READ",
      [
        "storage",
        "002969f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0d1c.md#insn-004e0d38)
- 新版 `004e0d38`（命令位置の公開資料なし）

~~~diff
- 004e0d38 ["COPY", "tmp:0:8", ["const:963:8"]]
- 004e0d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e0d38 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 004e0d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e0d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e0d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 bytes 298d2591
+ 004e0d38 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea392a034dead7588f0a7626b2a9ef2c"></a>

### [`004e0dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0dc4.md) → [`004e0dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0dc4.md) _ZNK5Botan9CRL_Entry4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb50.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdcc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc00.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e0e24",
      "incomplete_value": false,
      "site": "004e0e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0e24",
      "incomplete_value": false,
      "site": "004e0e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:ae7:8"
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
      "definition_site": "004e0e60",
      "incomplete_value": true,
      "site": "004e0e6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0e60",
      "incomplete_value": true,
      "site": "004e0e6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "004e0e24",
      "PARAM",
      [
        "storage",
        "00291ae7",
        null,
        "string"
      ]
    ],
    [
      "004e0e60",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e60",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e0e24",
      "PARAM",
      [
        "storage",
        "00291b74",
        null,
        "string"
      ]
    ],
    [
      "004e0e60",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e60",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0dc4.md#insn-004e0e24) · [`004e0e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0dc4.md#insn-004e0e60)
- 新版 `004e0e24`（命令位置の公開資料なし） · `004e0e60`（命令位置の公開資料なし）

~~~diff
- 004e0e24 ["COPY", "tmp:0:8", ["const:ae7:8"]]
- 004e0e24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e0e24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e0e24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e0e24 ["COPY", "tmp:0:8", ["const:b74:8"]]
+ 004e0e24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0e24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e0e24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e0e24 bytes 219c2b91
+ 004e0e24 bytes 21d02d91
- 004e0e60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004e0e60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0e60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004e0e60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0e60 bytes 212c47f9
+ 004e0e60 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d24e9a30522e6b5a9968cf80b0c020"></a>

### [`004e13e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e13e0.md) → [`004e13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e13e0.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e14e0",
      "incomplete_value": false,
      "site": "004e14ec",
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
            "const:8e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e14e0",
      "incomplete_value": false,
      "site": "004e14ec",
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
            "const:85a:8"
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
      "definition_site": "004e151c",
      "incomplete_value": true,
      "site": "004e1528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e151c",
      "incomplete_value": true,
      "site": "004e1528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "definition_site": "004e1540",
      "incomplete_value": false,
      "site": "004e154c",
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
            "const:c07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1540",
      "incomplete_value": false,
      "site": "004e154c",
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
            "const:b7a:8"
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
      "004e14e0",
      "PARAM",
      [
        "storage",
        "0029485a",
        null,
        "string"
      ]
    ],
    [
      "004e151c",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004e151c",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e14e0",
      "PARAM",
      [
        "storage",
        "002948e7",
        null,
        "string"
      ]
    ],
    [
      "004e151c",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e151c",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e14e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e13e0.md#insn-004e14e0) · [`004e151c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e13e0.md#insn-004e151c) · [`004e1540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e13e0.md#insn-004e1540)
- 新版 `004e14e0`（命令位置の公開資料なし） · `004e151c`（命令位置の公開資料なし） · `004e1540`（命令位置の公開資料なし）

~~~diff
- 004e14e0 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 004e14e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e14e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e14e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e14e0 ["COPY", "tmp:0:8", ["const:8e7:8"]]
+ 004e14e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e14e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e14e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e14e0 bytes 00682191
+ 004e14e0 bytes 009c2391
- 004e151c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004e151c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e151c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004e151c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e151c bytes 212c47f9
+ 004e151c bytes 218447f9
- 004e1540 ["COPY", "tmp:0:8", ["const:b7a:8"]]
- 004e1540 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e1540 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e1540 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e1540 ["COPY", "tmp:0:8", ["const:c07:8"]]
+ 004e1540 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1540 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1540 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e1540 bytes 00e82d91
+ 004e1540 bytes 001c3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2020bd4a41002fa972a6e37b7ac1955d"></a>

### [`004e15f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e15f0.md) → [`004e15f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e15f0.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e1700",
      "incomplete_value": false,
      "site": "004e170c",
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
            "const:c07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1700",
      "incomplete_value": false,
      "site": "004e170c",
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
            "const:b7a:8"
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
      "definition_site": "004e173c",
      "incomplete_value": true,
      "site": "004e1748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e173c",
      "incomplete_value": true,
      "site": "004e1748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "004e1700",
      "PARAM",
      [
        "storage",
        "00297b7a",
        null,
        "string"
      ]
    ],
    [
      "004e173c",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004e173c",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e1700",
      "PARAM",
      [
        "storage",
        "00297c07",
        null,
        "string"
      ]
    ],
    [
      "004e173c",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e173c",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e15f0.md#insn-004e1700) · [`004e173c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e15f0.md#insn-004e173c)
- 新版 `004e1700`（命令位置の公開資料なし） · `004e173c`（命令位置の公開資料なし）

~~~diff
- 004e1700 ["COPY", "tmp:0:8", ["const:b7a:8"]]
- 004e1700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e1700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e1700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["COPY", "tmp:0:8", ["const:c07:8"]]
+ 004e1700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e1700 bytes 00e82d91
+ 004e1700 bytes 001c3091
- 004e173c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004e173c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e173c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004e173c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e173c bytes 212c47f9
+ 004e173c bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a5d71b9567fd55855b7985a0bb57d2c"></a>

### [`004e17a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e17a8.md) → [`004e17a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e17a8.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e18b4",
      "incomplete_value": false,
      "site": "004e18c0",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e18b4",
      "incomplete_value": false,
      "site": "004e18c0",
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
            "const:9a5:8"
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
      "definition_site": "004e18f0",
      "incomplete_value": true,
      "site": "004e18fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e18f0",
      "incomplete_value": true,
      "site": "004e18fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "004e18b4",
      "PARAM",
      [
        "storage",
        "002ae9a5",
        null,
        "string"
      ]
    ],
    [
      "004e18f0",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004e18f0",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e18b4",
      "PARAM",
      [
        "storage",
        "002ae911",
        null,
        "string"
      ]
    ],
    [
      "004e18f0",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e18f0",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e18b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e17a8.md#insn-004e18b4) · [`004e18f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e17a8.md#insn-004e18f0)
- 新版 `004e18b4`（命令位置の公開資料なし） · `004e18f0`（命令位置の公開資料なし）

~~~diff
- 004e18b4 ["COPY", "tmp:0:8", ["const:9a5:8"]]
- 004e18b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e18b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e18b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e18b4 ["COPY", "tmp:0:8", ["const:911:8"]]
+ 004e18b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e18b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e18b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e18b4 bytes 00942691
+ 004e18b4 bytes 00442491
- 004e18f0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004e18f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e18f0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004e18f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e18f0 bytes 212c47f9
+ 004e18f0 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b52b01016222b73c23fd896dbd4be309"></a>

### [`004e195c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e195c.md) → [`004e195c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e195c.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e1a44",
      "incomplete_value": false,
      "site": "004e1a50",
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
            "const:ba6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1a44",
      "incomplete_value": false,
      "site": "004e1a50",
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
            "const:b19:8"
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
      "definition_site": "004e1a80",
      "incomplete_value": true,
      "site": "004e1a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1a80",
      "incomplete_value": true,
      "site": "004e1a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "004e1a44",
      "PARAM",
      [
        "storage",
        "00295b19",
        null,
        "string"
      ]
    ],
    [
      "004e1a80",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004e1a80",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e1a44",
      "PARAM",
      [
        "storage",
        "00295ba6",
        null,
        "string"
      ]
    ],
    [
      "004e1a80",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004e1a80",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e195c.md#insn-004e1a44) · [`004e1a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e195c.md#insn-004e1a80)
- 新版 `004e1a44`（命令位置の公開資料なし） · `004e1a80`（命令位置の公開資料なし）

~~~diff
- 004e1a44 ["COPY", "tmp:0:8", ["const:b19:8"]]
- 004e1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["COPY", "tmp:0:8", ["const:ba6:8"]]
+ 004e1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e1a44 bytes 00642c91
+ 004e1a44 bytes 00982e91
- 004e1a80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004e1a80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e1a80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004e1a80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e1a80 bytes 212c47f9
+ 004e1a80 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a1ce3a5bfa504e7595efb06003a635f"></a>

### [`004e1f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e1f38.md) → [`004e1f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e1/004e1f38.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00526374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526374.md) [`00526378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526378.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00526374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526374.md) [`00526378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526378.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e1f58",
      "incomplete_value": false,
      "site": "004e1f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1f58",
      "incomplete_value": false,
      "site": "004e1f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "004e1fd4",
      "incomplete_value": true,
      "site": "004e1fd4",
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
      "definition_site": "004e1fd4",
      "incomplete_value": true,
      "site": "004e1fd4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e1f68",
      "DATA",
      [
        "storage",
        "00bed7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed7e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed7e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e1f68",
      "DATA",
      [
        "storage",
        "00bed870",
        null,
        "undefined *"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed890",
        null,
        "pointer"
      ]
    ],
    [
      "004e1fa0",
      "READ",
      [
        "storage",
        "00bed898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e1f38.md#insn-004e1f58) · [`004e1fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e1/004e1f38.md#insn-004e1fb4)
- 新版 `004e1f58`（命令位置の公開資料なし） · `004e1fb4`（命令位置の公開資料なし）

~~~diff
- 004e1f58 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 004e1f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 004e1f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e1f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 bytes 29011f91
+ 004e1f58 bytes 29c12191
- 004e1fb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004e1fb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e1fb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004e1fb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e1fb4 bytes 08f140f9
+ 004e1fb4 bytes 084941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e9a2ca27588df605879717fefd5ce47"></a>

### [`004e21a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e21a8.md) → [`004e21a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e21a8.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0052647c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/0052647c.md) [`00526480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526480.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0052647c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/0052647c.md) [`00526480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526480.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e21d8",
      "incomplete_value": false,
      "site": "004e21d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e21d8",
      "incomplete_value": false,
      "site": "004e21d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:850:8"
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
      "004e21d8",
      "DATA",
      [
        "storage",
        "00bed850",
        null,
        "undefined *"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed870",
        null,
        "pointer"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e21d8",
      "DATA",
      [
        "storage",
        "00bed900",
        null,
        "undefined *"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed920",
        null,
        "pointer"
      ]
    ],
    [
      "004e2210",
      "READ",
      [
        "storage",
        "00bed928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e21c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e21a8.md#insn-004e21c8)
- 新版 `004e21c8`（命令位置の公開資料なし）

~~~diff
- 004e21c8 ["COPY", "tmp:0:8", ["const:850:8"]]
- 004e21c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 004e21c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e21c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 bytes 29412191
+ 004e21c8 bytes 29012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a3951b7f905cdbe514f46fc0dcd30a"></a>

### [`004e242c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e242c.md) → [`004e242c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbd0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bdcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e2498",
      "incomplete_value": true,
      "site": "004e2498",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e2498",
      "incomplete_value": true,
      "site": "004e2498",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba5:8"
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
      "definition_site": "004e249c",
      "incomplete_value": true,
      "site": "004e249c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e249c",
      "incomplete_value": true,
      "site": "004e249c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e24d0",
      "incomplete_value": true,
      "site": "004e24d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a2000:8"
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
      "definition_site": "004e24d0",
      "incomplete_value": true,
      "site": "004e24d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:353:8"
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
      "004e2488",
      "READ",
      [
        "storage",
        "00297ba5",
        null,
        "string"
      ]
    ],
    [
      "004e248c",
      "READ",
      [
        "storage",
        "00297bab",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "READ",
      [
        "storage",
        "002a2353",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e2488",
      "READ",
      [
        "storage",
        "00297c32",
        null,
        "string"
      ]
    ],
    [
      "004e248c",
      "READ",
      [
        "storage",
        "00297c38",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "READ",
      [
        "storage",
        "002a23e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e2480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e242c.md#insn-004e2480) · [`004e24b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e242c.md#insn-004e24b0) · [`004e2550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e242c.md#insn-004e2550)
- 新版 `004e2480`（命令位置の公開資料なし） · `004e24b0`（命令位置の公開資料なし） · `004e2550`（命令位置の公開資料なし）

~~~diff
- 004e2480 ["COPY", "tmp:0:8", ["const:ba5:8"]]
- 004e2480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["COPY", "tmp:0:8", ["const:c32:8"]]
+ 004e2480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e2480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e2480 bytes 29952e91
+ 004e2480 bytes 29c93091
- 004e24b0 ["COPY", "tmp:0:8", ["const:353:8"]]
- 004e24b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 004e24b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e24b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e24b0 bytes 294d0d91
+ 004e24b0 bytes 29810f91
- 004e2550 ["COPY", "tmp:0:8", ["const:880:8"]]
- 004e2550 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004e2550 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004e2550 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["COPY", "tmp:0:8", ["const:90d:8"]]
+ 004e2550 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004e2550 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004e2550 bytes 4a012291
+ 004e2550 bytes 4a352491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9efd7dbf20f302279f526433730d49f"></a>

### [`004e3024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3024.md) → [`004e3024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbe0.md) · 呼出先 10件 [`00483974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdcc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md) · 呼出先 10件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e32f0",
      "incomplete_value": false,
      "site": "004e32f8",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e32f0",
      "incomplete_value": false,
      "site": "004e32f8",
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
            "const:b33:8"
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
      "definition_site": "004e3360",
      "incomplete_value": true,
      "site": "004e336c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3360",
      "incomplete_value": true,
      "site": "004e336c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
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
      "004e32f0",
      "PARAM",
      [
        "storage",
        "00296b33",
        null,
        "string"
      ]
    ],
    [
      "004e3360",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004e3360",
      "PARAM",
      [
        "storage",
        "00be9188",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e32f0",
      "PARAM",
      [
        "storage",
        "00296bc0",
        null,
        "string"
      ]
    ],
    [
      "004e3360",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004e3360",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e32f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3024.md#insn-004e32f0) · [`004e3360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3024.md#insn-004e3360)
- 新版 `004e32f0`（命令位置の公開資料なし） · `004e3360`（命令位置の公開資料なし）

~~~diff
- 004e32f0 ["COPY", "tmp:0:8", ["const:b33:8"]]
- 004e32f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 004e32f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e32f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e32f0 bytes 21cc2c91
+ 004e32f0 bytes 21002f91
- 004e3360 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 004e3360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e3360 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 004e3360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e3360 bytes 214c47f9
+ 004e3360 bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eac988d49ac0b374896eddbbe0db418"></a>

### [`004e3458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3458.md) → [`004e3458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3458.md) _ZN5Botan11GeneralNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc30.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdcce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcce0.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e349c",
      "incomplete_value": true,
      "site": "004e34a4",
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
      "definition_site": "004e349c",
      "incomplete_value": true,
      "site": "004e34a4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e3680",
      "incomplete_value": false,
      "site": "004e3688",
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
            "const:624:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3680",
      "incomplete_value": false,
      "site": "004e3688",
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
            "const:597:8"
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
      "definition_site": "004e36b8",
      "incomplete_value": true,
      "site": "004e36c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e36b8",
      "incomplete_value": true,
      "site": "004e36c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
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
      "004e3484",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      "004e34a4",
      "DATA",
      [
        "storage",
        "00beb010",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3680",
      "PARAM",
      [
        "storage",
        "002a1597",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e3484",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e34a4",
      "DATA",
      [
        "storage",
        "00beb0c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3680",
      "PARAM",
      [
        "storage",
        "002a1624",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e3484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3458.md#insn-004e3484) · [`004e3680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3458.md#insn-004e3680) · [`004e36b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3458.md#insn-004e36b8)
- 新版 `004e3484`（命令位置の公開資料なし） · `004e3680`（命令位置の公開資料なし） · `004e36b8`（命令位置の公開資料なし）

~~~diff
- 004e3484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
- 004e3484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e3484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 004e3484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e3484 bytes 081d41f9
+ 004e3484 bytes 087541f9
- 004e3680 ["COPY", "tmp:0:8", ["const:597:8"]]
- 004e3680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e3680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e3680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["COPY", "tmp:0:8", ["const:624:8"]]
+ 004e3680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e3680 bytes 215c1691
+ 004e3680 bytes 21901891
- 004e36b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004e36b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e36b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004e36b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e36b8 bytes 212047f9
+ 004e36b8 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5c58dc068a2b15118598f0b83042bac"></a>

### [`004e3770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3770.md) → [`004e3770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3770.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdc590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc590.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc640.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e37a4",
      "incomplete_value": true,
      "site": "004e37c0",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e37a4",
      "incomplete_value": true,
      "site": "004e37c0",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a9a:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e37ec",
      "incomplete_value": true,
      "site": "004e37f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e37ec",
      "incomplete_value": true,
      "site": "004e37f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "004e37a4",
      "READ",
      [
        "storage",
        "002ada9a",
        null,
        "string"
      ]
    ],
    [
      "004e37ec",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e37ec",
      "PARAM",
      [
        "storage",
        "00be9d80",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e37a4",
      "READ",
      [
        "storage",
        "002ada91",
        null,
        "string"
      ]
    ],
    [
      "004e37ec",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ],
    [
      "004e37ec",
      "PARAM",
      [
        "storage",
        "00be9e30",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e379c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3770.md#insn-004e379c) · [`004e37ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3770.md#insn-004e37ec)
- 新版 `004e379c`（命令位置の公開資料なし） · `004e37ec`（命令位置の公開資料なし）

~~~diff
- 004e379c ["COPY", "tmp:0:8", ["const:a9a:8"]]
- 004e379c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e379c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e379c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e379c ["COPY", "tmp:0:8", ["const:a91:8"]]
+ 004e379c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e379c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e379c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e379c bytes 29692a91
+ 004e379c bytes 29452a91
- 004e37ec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
- 004e37ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e37ec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:190:8"]]
+ 004e37ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e37ec bytes 217040f9
+ 004e37ec bytes 21c840f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37cd2954d5e08fa0abac3e9e924f6a07"></a>

### [`004e3840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3840.md) → [`004e3840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3840.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 29件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e38cc",
      "incomplete_value": true,
      "site": "004e38cc",
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
      "definition_site": "004e38cc",
      "incomplete_value": true,
      "site": "004e38cc",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e3950",
      "incomplete_value": true,
      "site": "004e3958",
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
      "definition_site": "004e3950",
      "incomplete_value": true,
      "site": "004e3958",
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
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004e3960",
      "incomplete_value": true,
      "site": "004e3960",
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
                "const:b0:8"
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
      "definition_site": "004e3960",
      "incomplete_value": true,
      "site": "004e3960",
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
                "const:b0:8"
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
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e38b4",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e38cc",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3938",
      "PARAM",
      [
        "storage",
        "002a9641",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004e38b4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004e38cc",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3938",
      "PARAM",
      [
        "storage",
        "002a95ad",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e38b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3840.md#insn-004e38b4) · [`004e3938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3840.md#insn-004e3938) · [`004e394c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3840.md#insn-004e394c)
- 新版 `004e38b4`（命令位置の公開資料なし） · `004e3938`（命令位置の公開資料なし） · `004e394c`（命令位置の公開資料なし）

~~~diff
- 004e38b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004e38b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e38b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004e38b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e38b4 bytes 08f140f9
+ 004e38b4 bytes 084941f9
- 004e3938 ["COPY", "tmp:0:8", ["const:641:8"]]
- 004e3938 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e3938 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e3938 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["COPY", "tmp:0:8", ["const:5ad:8"]]
+ 004e3938 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e3938 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e3938 bytes 21041991
+ 004e3938 bytes 21b41691
- 004e394c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 004e394c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e394c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 004e394c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004e394c bytes 739246f9
+ 004e394c bytes 73ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-282c84471b0ed65b1f52d426de43118b"></a>

### [`004e40b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e40b8.md) → [`004e40b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004dcf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcf48.md) [`004f03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md) [`00bdcbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbf0.md) · 呼出先 12件 [`00482aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/00482aa8.md) [`00525f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525f90.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 3件 [`004dcf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md) [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) [`00bdcca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcca0.md) · 呼出先 12件 [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`00525f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525f90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e414c",
      "incomplete_value": true,
      "site": "004e414c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e414c",
      "incomplete_value": true,
      "site": "004e414c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e4284",
      "incomplete_value": true,
      "site": "004e4284",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e4284",
      "incomplete_value": true,
      "site": "004e4284",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e430c",
      "incomplete_value": true,
      "site": "004e430c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e430c",
      "incomplete_value": true,
      "site": "004e430c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e413c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004e4274",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004e42fc",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e413c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e4274",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e42fc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e413c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e40b8.md#insn-004e413c) · [`004e4274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e40b8.md#insn-004e4274) · [`004e42fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e40b8.md#insn-004e42fc)
- 新版 `004e413c`（命令位置の公開資料なし） · `004e4274`（命令位置の公開資料なし） · `004e42fc`（命令位置の公開資料なし）

~~~diff
- 004e413c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004e413c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e413c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004e413c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e413c bytes c93e43f9
+ 004e413c bytes c99643f9
- 004e4274 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004e4274 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4274 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004e4274 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4274 bytes c93e43f9
+ 004e4274 bytes c99643f9
- 004e42fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004e42fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e42fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004e42fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e42fc bytes c93e43f9
+ 004e42fc bytes c99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b248561dbc7aa8f55a7797c1e91b357"></a>

### [`004e4494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md) → [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc00.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`004e4bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4bdc.md)
- 新版 呼出元 1件 [`00bdccb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccb0.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004e4bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4bdc.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
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
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
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
      "definition_site": "004e45e4",
      "incomplete_value": true,
      "site": "004e45e4",
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
      "definition_site": "004e45e4",
      "incomplete_value": true,
      "site": "004e45e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e4544",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "004e4548",
      "READ",
      [
        "storage",
        "00c1b248",
        null,
        "pointer"
      ]
    ],
    [
      "004e4564",
      "DATA",
      [
        "storage",
        "00bed8d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004e4544",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e4548",
      "READ",
      [
        "storage",
        "00c1b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "004e4564",
      "DATA",
      [
        "storage",
        "00bed980",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e4544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md#insn-004e4544) · [`004e4548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md#insn-004e4548) · [`004e45c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md#insn-004e45c8)
- 新版 `004e4544`（命令位置の公開資料なし） · `004e4548`（命令位置の公開資料なし） · `004e45c8`（命令位置の公開資料なし）

~~~diff
- 004e4544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
- 004e4544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004e4544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4544 bytes 082141f9
+ 004e4544 bytes 087941f9
- 004e4548 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:248:8"]]
- 004e4548 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e4548 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2f8:8"]]
+ 004e4548 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e4548 bytes 292541f9
+ 004e4548 bytes 297d41f9
- 004e45c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
- 004e45c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e45c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004e45c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e45c8 bytes 082141f9
+ 004e45c8 bytes 087941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdc55bcd0705684cb87468babd4447d4"></a>

### [`004e4bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4bf4.md) → [`004e4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4bf4.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4d00",
      "incomplete_value": false,
      "site": "004e4d10",
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
      "definition_site": "004e4d00",
      "incomplete_value": false,
      "site": "004e4d10",
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
      "004e4d00",
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
      "004e4d00",
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

- 旧版 [`004e4d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4bf4.md#insn-004e4d00)
- 新版 `004e4d00`（命令位置の公開資料なし）

~~~diff
- 004e4d00 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 004e4d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 004e4d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e4d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e4d00 bytes 00681f91
+ 004e4d00 bytes 009c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a32698ef250072c05b0238f296739e"></a>

### [`004e50d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md) → [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e56e4.md) [`004e5d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5d50.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`00526790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526790.md) [`005267f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/005267f0.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md) [`004e5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5d50.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00526790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526790.md) [`005267f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/005267f0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.66% / 新版 94.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5140",
      "incomplete_value": true,
      "site": "004e5140",
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
      "definition_site": "004e5140",
      "incomplete_value": true,
      "site": "004e5140",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e514c",
      "incomplete_value": true,
      "site": "004e514c",
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
      "definition_site": "004e514c",
      "incomplete_value": true,
      "site": "004e514c",
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
      "definition_site": "004e533c",
      "incomplete_value": true,
      "site": "004e5344",
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
      "definition_site": "004e533c",
      "incomplete_value": true,
      "site": "004e5344",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e5128",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5140",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e514c",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5128",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004e5140",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e514c",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md#insn-004e5128) · [`004e5338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md#insn-004e5338) · [`004e5354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md#insn-004e5354)
- 新版 `004e5128`（命令位置の公開資料なし） · `004e5338`（命令位置の公開資料なし） · `004e5354`（命令位置の公開資料なし）

~~~diff
- 004e5128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004e5128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004e5128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5128 bytes 08f140f9
+ 004e5128 bytes 084941f9
- 004e5338 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d20:8"]]
- 004e5338 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5338 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dd0:8"]]
+ 004e5338 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5338 bytes b59246f9
+ 004e5338 bytes b5ea46f9
- 004e5354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 004e5354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 004e5354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5354 bytes 086946f9
+ 004e5354 bytes 08c146f9
~~~


<a id="compare-3c2c2ea6a3a1bee68148bf4b89df41a1"></a>

### [`004e548c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e548c.md) → [`004e548c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e548c.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e4494.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00463ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00463/00463ea0.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`004e4494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e4494.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00463ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00463/00463ea0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e54c0",
      "incomplete_value": false,
      "site": "004e54c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e54c0",
      "incomplete_value": false,
      "site": "004e54c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "definition_site": "004e5624",
      "incomplete_value": true,
      "site": "004e5630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5624",
      "incomplete_value": true,
      "site": "004e5630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e54c8",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e54c8",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5510",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e54c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e548c.md#insn-004e54c0) · [`004e5624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e548c.md#insn-004e5624)
- 新版 `004e54c0`（命令位置の公開資料なし） · `004e5624`（命令位置の公開資料なし）

~~~diff
- 004e54c0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004e54c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e54c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e54c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e54c0 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 004e54c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e54c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e54c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e54c0 bytes 08c11791
+ 004e54c0 bytes 08811a91
- 004e5624 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004e5624 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5624 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004e5624 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5624 bytes 213047f9
+ 004e5624 bytes 218847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf47b3fcf52040b399ece03b69e29f0"></a>

### [`004e56e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e56e4.md) → [`004e56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md) FUN_004e56e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcbd4.md) [`004e50d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525380.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2a0.md) [`00bdb4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4e0.md)
- 新版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md) [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) [`00bdb590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb590.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.08% / 新版 78.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5734",
      "incomplete_value": true,
      "site": "004e5734",
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
      "definition_site": "004e5734",
      "incomplete_value": true,
      "site": "004e5734",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5738",
      "incomplete_value": true,
      "site": "004e5738",
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
      "definition_site": "004e5738",
      "incomplete_value": true,
      "site": "004e5738",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5730",
      "incomplete_value": true,
      "site": "004e5740",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e5730",
      "incomplete_value": true,
      "site": "004e5740",
      "value": [
        "LOAD",
        "8",
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
      "004e570c",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "004e5718",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "004e5730",
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
      "004e570c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "004e5718",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5730",
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

- 旧版 [`004e570c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e56e4.md#insn-004e570c) · [`004e5714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e56e4.md#insn-004e5714)
- 新版 `004e570c`（命令位置の公開資料なし） · `004e5714`（命令位置の公開資料なし）

~~~diff
- 004e570c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d28:8"]]
- 004e570c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e570c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:dd8:8"]]
+ 004e570c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004e570c bytes 399746f9
+ 004e570c bytes 39ef46f9
- 004e5714 ["COPY", "register:40e0:8", ["register:4000:8"]]
- 004e5714 bytes fc0300aa
+ 004e5714 ["COPY", "register:40e0:8", ["register:4000:8"]]
+ 004e5714 bytes fc0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3582cf36903dbac75353599de2d2462"></a>

### [`004e5850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5850.md) → [`004e5850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5850.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdca40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca40.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004f2498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f2498.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdcaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcaf0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004f2498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f2498.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5b34",
      "incomplete_value": false,
      "site": "004e5b3c",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5b34",
      "incomplete_value": false,
      "site": "004e5b3c",
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
            "const:b43:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5b6c",
      "incomplete_value": true,
      "site": "004e5b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5b6c",
      "incomplete_value": true,
      "site": "004e5b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "004e5b34",
      "PARAM",
      [
        "storage",
        "00296b43",
        null,
        "string"
      ]
    ],
    [
      "004e5b6c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004e5b6c",
      "PARAM",
      [
        "storage",
        "00be91e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e5b34",
      "PARAM",
      [
        "storage",
        "00296bd0",
        null,
        "string"
      ]
    ],
    [
      "004e5b6c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004e5b6c",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5850.md#insn-004e5b34) · [`004e5b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5850.md#insn-004e5b6c)
- 新版 `004e5b34`（命令位置の公開資料なし） · `004e5b6c`（命令位置の公開資料なし）

~~~diff
- 004e5b34 ["COPY", "tmp:0:8", ["const:b43:8"]]
- 004e5b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 004e5b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e5b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e5b34 bytes 210c2d91
+ 004e5b34 bytes 21402f91
- 004e5b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004e5b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004e5b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5b6c bytes 212047f9
+ 004e5b6c bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29738cae15a9ce9850108d0b9ba2f129"></a>

### [`004e5d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5d50.md) → [`004e5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5d50.md) FUN_004e5d50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e50d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e50d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d8c",
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
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d8c",
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
      "004e5d78",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004e5d8c",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5d78",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004e5d8c",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5d50.md#insn-004e5d78)
- 新版 `004e5d78`（命令位置の公開資料なし）

~~~diff
- 004e5d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 004e5d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004e5d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5d78 bytes 082947f9
+ 004e5d78 bytes 088147f9
~~~


<a id="compare-566299a948235fb6ad54940709ada92d"></a>

### [`004e5e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5e70.md) → [`004e5e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e5e70.md) _ZN5Botan14GeneralSubtreeC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
    "new": {
      "definition_site": "004e6164",
      "incomplete_value": false,
      "site": "004e616c",
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
            "const:624:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6164",
      "incomplete_value": false,
      "site": "004e616c",
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
            "const:597:8"
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
      "004e5e9c",
      "READ",
      [
        "storage",
        "00c1b260",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ea4",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ec0",
      "DATA",
      [
        "storage",
        "00beb058",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e5e9c",
      "READ",
      [
        "storage",
        "00c1b310",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ea4",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e5ec0",
      "DATA",
      [
        "storage",
        "00beb108",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5e70.md#insn-004e5e9c) · [`004e5ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5e70.md#insn-004e5ea4) · [`004e6164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e5e70.md#insn-004e6164)
- 新版 `004e5e9c`（命令位置の公開資料なし） · `004e5ea4`（命令位置の公開資料なし） · `004e6164`（命令位置の公開資料なし）

~~~diff
- 004e5e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
- 004e5e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 004e5e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5e9c bytes 083141f9
+ 004e5e9c bytes 088941f9
- 004e5ea4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:238:8"]]
- 004e5ea4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e5ea4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2e8:8"]]
+ 004e5ea4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5ea4 bytes 4a1d41f9
+ 004e5ea4 bytes 4a7541f9
- 004e6164 ["COPY", "tmp:0:8", ["const:597:8"]]
- 004e6164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e6164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e6164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["COPY", "tmp:0:8", ["const:624:8"]]
+ 004e6164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e6164 bytes 215c1691
+ 004e6164 bytes 21901891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28dc5ab4bf80c0ddfa71d56f3f040735"></a>

### [`004e6294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6294.md) → [`004e6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6294.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e62d4",
      "incomplete_value": true,
      "site": "004e62e8",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:91d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e62d4",
      "incomplete_value": true,
      "site": "004e62e8",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:890:8"
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
      "definition_site": "004e62d8",
      "incomplete_value": true,
      "site": "004e62ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e62d8",
      "incomplete_value": true,
      "site": "004e62ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6320",
      "incomplete_value": true,
      "site": "004e632c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6320",
      "incomplete_value": true,
      "site": "004e632c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
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
      "004e62d4",
      "READ",
      [
        "storage",
        "00292890",
        null,
        "string"
      ]
    ],
    [
      "004e62d8",
      "READ",
      [
        "storage",
        "002928a0",
        null,
        "string"
      ]
    ],
    [
      "004e6320",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e62d4",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ],
    [
      "004e62d8",
      "READ",
      [
        "storage",
        "0029292d",
        null,
        "string"
      ]
    ],
    [
      "004e6320",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e62cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6294.md#insn-004e62cc) · [`004e62d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6294.md#insn-004e62d0)
- 新版 `004e62cc`（命令位置の公開資料なし） · `004e62d0`（命令位置の公開資料なし）

~~~diff
- 004e62cc ["COPY", "tmp:0:8", ["const:890:8"]]
- 004e62cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e62cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e62cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["COPY", "tmp:0:8", ["const:91d:8"]]
+ 004e62cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e62cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e62cc bytes 08412291
+ 004e62cc bytes 08752491
- 004e62d0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004e62d0 bytes 49eeffd0
+ 004e62d0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004e62d0 bytes 49eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bd0d0c4b9d8608fd0faa1346f5e9ee6"></a>

### [`004e637c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e637c.md) → [`004e637c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc40.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdccf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccf0.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6424",
      "incomplete_value": true,
      "site": "004e6424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6424",
      "incomplete_value": true,
      "site": "004e6424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6474",
      "incomplete_value": false,
      "site": "004e647c",
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
            "const:eaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6474",
      "incomplete_value": false,
      "site": "004e647c",
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
            "const:e22:8"
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
      "definition_site": "004e64ac",
      "incomplete_value": true,
      "site": "004e64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e64ac",
      "incomplete_value": true,
      "site": "004e64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e6414",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004e6474",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "004e64ac",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6414",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e6474",
      "PARAM",
      [
        "storage",
        "00298eaf",
        null,
        "string"
      ]
    ],
    [
      "004e64ac",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e637c.md#insn-004e6414) · [`004e6474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e637c.md#insn-004e6474) · [`004e64ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e637c.md#insn-004e64ac)
- 新版 `004e6414`（命令位置の公開資料なし） · `004e6474`（命令位置の公開資料なし） · `004e64ac`（命令位置の公開資料なし）

~~~diff
- 004e6414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004e6414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004e6414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6414 bytes 293d43f9
+ 004e6414 bytes 299543f9
- 004e6474 ["COPY", "tmp:0:8", ["const:e22:8"]]
- 004e6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["COPY", "tmp:0:8", ["const:eaf:8"]]
+ 004e6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e6474 bytes 21883891
+ 004e6474 bytes 21bc3a91
- 004e64ac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004e64ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e64ac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004e64ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e64ac bytes 213047f9
+ 004e64ac bytes 218847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6ec39539bf103e3ad77644a5812a14d"></a>

### [`004e6520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6520.md) → [`004e6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md) FUN_004e6520

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004f7f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7f54.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md)
- 新版 呼出元 1件 [`004f7f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e658c",
      "incomplete_value": true,
      "site": "004e6590",
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
      "definition_site": "004e658c",
      "incomplete_value": true,
      "site": "004e6590",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e655c",
      "incomplete_value": false,
      "site": "004e6560",
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
            "const:b43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e655c",
      "incomplete_value": false,
      "site": "004e6560",
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
            "const:ab6:8"
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
      "definition_site": "004e6618",
      "incomplete_value": false,
      "site": "004e6620",
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
            "const:342:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6618",
      "incomplete_value": false,
      "site": "004e6620",
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
            "const:2b5:8"
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
      "004e655c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "004e656c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "004e6584",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e655c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "004e656c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "004e6584",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6520.md#insn-004e6554) · [`004e6558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6520.md#insn-004e6558)
- 新版 `004e6554`（命令位置の公開資料なし） · `004e6558`（命令位置の公開資料なし）

~~~diff
- 004e6554 ["COPY", "tmp:0:8", ["const:ab6:8"]]
- 004e6554 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["COPY", "tmp:0:8", ["const:b43:8"]]
+ 004e6554 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004e6554 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004e6554 bytes b5da2a91
+ 004e6554 bytes b50e2d91
- 004e6558 ["COPY", "register:4010:8", ["const:1:8"]]
- 004e6558 bytes 22008052
+ 004e6558 ["COPY", "register:4010:8", ["const:1:8"]]
+ 004e6558 bytes 22008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39e7424a5f0e06a46d3f7a064500c17d"></a>

### [`004e66d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e66d0.md) → [`004e66d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e66d0.md) _ZN5Botan4OCSP7RequestC1ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518128.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e670c",
      "incomplete_value": true,
      "site": "004e6710",
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
      "definition_site": "004e670c",
      "incomplete_value": true,
      "site": "004e6710",
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
    "kind": "call_target",
    "new": {
      "definition_site": "004e6790",
      "incomplete_value": true,
      "site": "004e6790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6790",
      "incomplete_value": true,
      "site": "004e6790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e67fc",
      "incomplete_value": false,
      "site": "004e6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e67fc",
      "incomplete_value": false,
      "site": "004e6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:52f:8"
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
      "004e6708",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6710",
      "DATA",
      [
        "storage",
        "00bea9c8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e6780",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6708",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6710",
      "DATA",
      [
        "storage",
        "00beaa78",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e6780",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e66d0.md#insn-004e6708) · [`004e6780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e66d0.md#insn-004e6780) · [`004e67fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e66d0.md#insn-004e67fc)
- 新版 `004e6708`（命令位置の公開資料なし） · `004e6780`（命令位置の公開資料なし） · `004e67fc`（命令位置の公開資料なし）

~~~diff
- 004e6708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004e6708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004e6708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6708 bytes 08f940f9
+ 004e6708 bytes 085141f9
- 004e6780 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004e6780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6780 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004e6780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6780 bytes 293d43f9
+ 004e6780 bytes 299543f9
- 004e67fc ["COPY", "tmp:0:8", ["const:52f:8"]]
- 004e67fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e67fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e67fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["COPY", "tmp:0:8", ["const:528:8"]]
+ 004e67fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e67fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e67fc bytes 21bc1491
+ 004e67fc bytes 21a01491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c37a2bb304c48c34f41b125d47f77ee"></a>

### [`004e697c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e697c.md) → [`004e697c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e697c.md) FUN_004e697c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6998",
      "incomplete_value": true,
      "site": "004e699c",
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
      "definition_site": "004e6998",
      "incomplete_value": true,
      "site": "004e699c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e69d8",
      "incomplete_value": true,
      "site": "004e69dc",
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
      "definition_site": "004e69d8",
      "incomplete_value": true,
      "site": "004e69dc",
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
      "004e6990",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e699c",
      "DATA",
      [
        "storage",
        "00bea9c8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e69d0",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6990",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "004e699c",
      "DATA",
      [
        "storage",
        "00beaa78",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "004e69d0",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e697c.md#insn-004e6990) · [`004e69d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e697c.md#insn-004e69d0)
- 新版 `004e6990`（命令位置の公開資料なし） · `004e69d0`（命令位置の公開資料なし）

~~~diff
- 004e6990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004e6990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004e6990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6990 bytes 08f940f9
+ 004e6990 bytes 085141f9
- 004e69d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004e69d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e69d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004e69d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e69d0 bytes 083541f9
+ 004e69d0 bytes 088d41f9
~~~


<a id="compare-5dfc55e0edde4b19378c29abed2f1c58"></a>

### [`004e6aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6aac.md) → [`004e6aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6aac.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc60.md) · 呼出先 10件 [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 1件 [`00bdcd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd10.md) · 呼出先 10件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6b58",
      "incomplete_value": true,
      "site": "004e6b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6b58",
      "incomplete_value": true,
      "site": "004e6b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6c2c",
      "incomplete_value": true,
      "site": "004e6c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6c2c",
      "incomplete_value": true,
      "site": "004e6c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e6b48",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004e6c1c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6b48",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004e6c1c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6aac.md#insn-004e6b48) · [`004e6c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6aac.md#insn-004e6c1c)
- 新版 `004e6b48`（命令位置の公開資料なし） · `004e6c1c`（命令位置の公開資料なし）

~~~diff
- 004e6b48 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004e6b48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6b48 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004e6b48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6b48 bytes e93e43f9
+ 004e6b48 bytes e99643f9
- 004e6c1c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004e6c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6c1c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004e6c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6c1c bytes e93e43f9
+ 004e6c1c bytes e99643f9
~~~


<a id="compare-0fe87076b549a17c32c35bc0617051c4"></a>

### [`004e6d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md) → [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md) [`00482aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/00482aa8.md) [`0048bb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bb9c.md) [`004e7aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7aa4.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`0048bb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bb9c.md) [`004e7aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7aa4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 9件

アドレスに依存する影響 `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6dc4",
      "incomplete_value": true,
      "site": "004e6dc4",
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
      "definition_site": "004e6dc4",
      "incomplete_value": true,
      "site": "004e6dc4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6dec",
      "incomplete_value": true,
      "site": "004e6dec",
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
      "definition_site": "004e6dec",
      "incomplete_value": true,
      "site": "004e6dec",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e6e18",
      "incomplete_value": true,
      "site": "004e6e18",
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
      "definition_site": "004e6e18",
      "incomplete_value": true,
      "site": "004e6e18",
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
      "004e6db8",
      "READ",
      [
        "storage",
        "00c1aec0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6dc4",
      "DATA",
      [
        "storage",
        "00be92b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e6dd4",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e6db8",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004e6dc4",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e6dd4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md#insn-004e6db8) · [`004e6dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md#insn-004e6dd4) · [`004e6de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md#insn-004e6de4)
- 新版 `004e6db8`（命令位置の公開資料なし） · `004e6dd4`（命令位置の公開資料なし）

~~~diff
- 004e6db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 004e6db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004e6db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6db8 bytes 086147f9
+ 004e6db8 bytes 08b947f9
- 004e6dd4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1e0:8"]]
- 004e6dd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e6dd4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:290:8"]]
+ 004e6dd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6dd4 bytes 29f140f9
+ 004e6dd4 bytes 294941f9
- 004e6de4 ["COPY", "register:4048:8", ["register:40a0:8"]]
- 004e6de4 bytes e90314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8e4662d0ba3442d6c5819f8cae0c474"></a>

### [`004e7aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7aa4.md) → [`004e7aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7aa4.md) FUN_004e7aa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e6d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e7bac",
      "incomplete_value": true,
      "site": "004e7bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e7bac",
      "incomplete_value": true,
      "site": "004e7bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e7bac",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004e7bac",
      "PARAM",
      [
        "storage",
        "00be9200",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e7bac",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004e7bac",
      "PARAM",
      [
        "storage",
        "00be92b0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7aa4.md#insn-004e7bac)
- 新版 `004e7bac`（命令位置の公開資料なし）

~~~diff
- 004e7bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004e7bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7bac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004e7bac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7bac bytes 213047f9
+ 004e7bac bytes 218847f9
~~~


<a id="compare-ff0ff0038e5897d225247e736a7f4e85"></a>

### [`004e7fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7fa0.md) → [`004e7fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc90.md) · 呼出先 10件 [`004e9fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9fdc.md) [`005269b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/005269b0.md) [`00526bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526bb4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdcd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd40.md) · 呼出先 10件 [`004e9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md) [`005269b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/005269b0.md) [`00526bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526bb4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e80e4",
      "incomplete_value": true,
      "site": "004e80e4",
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
      "definition_site": "004e80e4",
      "incomplete_value": true,
      "site": "004e80e4",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8104",
      "incomplete_value": true,
      "site": "004e8104",
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
      "definition_site": "004e8104",
      "incomplete_value": true,
      "site": "004e8104",
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
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8100",
      "incomplete_value": true,
      "site": "004e8110",
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
      "definition_site": "004e8100",
      "incomplete_value": true,
      "site": "004e8110",
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
      "004e7ff4",
      "READ",
      [
        "storage",
        "00c1b270",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ff8",
      "READ",
      [
        "storage",
        "00c1b278",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ffc",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e7ff4",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ff8",
      "READ",
      [
        "storage",
        "00c1b328",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ffc",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7fa0.md#insn-004e7ff4) · [`004e7ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7fa0.md#insn-004e7ff8) · [`004e7ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7fa0.md#insn-004e7ffc)
- 新版 `004e7ff4`（命令位置の公開資料なし） · `004e7ff8`（命令位置の公開資料なし） · `004e7ffc`（命令位置の公開資料なし）

~~~diff
- 004e7ff4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:270:8"]]
- 004e7ff4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ff4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:320:8"]]
+ 004e7ff4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ff4 bytes 4a3941f9
+ 004e7ff4 bytes 4a9141f9
- 004e7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
- 004e7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 004e7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ff8 bytes 083d41f9
+ 004e7ff8 bytes 089541f9
- 004e7ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 004e7ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 004e7ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ffc bytes 292547f9
+ 004e7ffc bytes 297d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdd214dd0ed9a7a63fd2308a9366af2e"></a>

### [`004e85ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e85ec.md) → [`004e85ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdccb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccb0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483d44.md) [`00524c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c3c.md) [`00524c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`00bdcd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md) [`00524c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c3c.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e863c",
      "incomplete_value": false,
      "site": "004e863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e863c",
      "incomplete_value": false,
      "site": "004e863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "004e863c",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e863c",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8680",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e85ec.md#insn-004e8634)
- 新版 `004e8634`（命令位置の公開資料なし）

~~~diff
- 004e8634 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004e8634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004e8634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004e8634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 004e8634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004e8634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004e8634 bytes 08c11791
+ 004e8634 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a25225e8ea5dade0fdb6e808d3d460"></a>

### [`004e8a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md) → [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccd0.md) · 呼出先 13件 [`00518128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518128.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md) · 呼出先 13件 [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8d18",
      "incomplete_value": true,
      "site": "004e8d24",
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
                "const:382:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e8d18",
      "incomplete_value": true,
      "site": "004e8d24",
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
                "const:389:8"
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
      "definition_site": "004e8eac",
      "incomplete_value": true,
      "site": "004e8eb0",
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
      "definition_site": "004e8eac",
      "incomplete_value": true,
      "site": "004e8eb0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8ee0",
      "incomplete_value": true,
      "site": "004e8ee4",
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
      "definition_site": "004e8ee0",
      "incomplete_value": true,
      "site": "004e8ee4",
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
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e8d18",
      "READ",
      [
        "storage",
        "002a4389",
        null,
        "string"
      ]
    ],
    [
      "004e8ea4",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e8eb0",
      "DATA",
      [
        "storage",
        "00bed680",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "004e8d18",
      "READ",
      [
        "storage",
        "002a4382",
        null,
        "string"
      ]
    ],
    [
      "004e8ea4",
      "READ",
      [
        "storage",
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "004e8eb0",
      "DATA",
      [
        "storage",
        "00bed730",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md#insn-004e8d10) · [`004e8ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md#insn-004e8ea4) · [`004e8ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md#insn-004e8ed8)
- 新版 `004e8d10`（命令位置の公開資料なし） · `004e8ea4`（命令位置の公開資料なし） · `004e8ed8`（命令位置の公開資料なし）

~~~diff
- 004e8d10 ["COPY", "tmp:0:8", ["const:389:8"]]
- 004e8d10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["COPY", "tmp:0:8", ["const:382:8"]]
+ 004e8d10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004e8d10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e8d10 bytes 29250e91
+ 004e8d10 bytes 29090e91
- 004e8ea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
- 004e8ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e8ea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
+ 004e8ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e8ea4 bytes 08f540f9
+ 004e8ea4 bytes 084d41f9
- 004e8ed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
- 004e8ed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e8ed8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
+ 004e8ed8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e8ed8 bytes 08f540f9
+ 004e8ed8 bytes 084d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06206f37c3a220c204c2873d5f8d69e"></a>

### [`004e8fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8fec.md) → [`004e8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8fec.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcce0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdcd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd90.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e90a0",
      "incomplete_value": true,
      "site": "004e90ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e90a0",
      "incomplete_value": true,
      "site": "004e90ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
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
      "004e90a0",
      "READ",
      [
        "storage",
        "00c1aea8",
        null,
        "pointer"
      ]
    ],
    [
      "004e90a0",
      "PARAM",
      [
        "storage",
        "00be9230",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e90a0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004e90a0",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e90a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8fec.md#insn-004e90a0)
- 新版 `004e90a0`（命令位置の公開資料なし）

~~~diff
- 004e90a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ea8:8"]]
- 004e90a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e90a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004e90a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e90a0 bytes 215447f9
+ 004e90a0 bytes 21ac47f9
~~~


<a id="compare-a1d29692e01fb63781580cdaf1b3a476"></a>

### [`004e9260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9260.md) → [`004e9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9260.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd00.md) · 呼出先 4件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdba90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdba90.md) [`00bdcb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb20.md) [`00bdcd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd10.md)
- 新版 呼出元 1件 [`00bdcdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdb0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb40.md) [`00bdcbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbd0.md) [`00bdcdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdc0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e9320",
      "incomplete_value": true,
      "site": "004e9328",
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
      "definition_site": "004e9320",
      "incomplete_value": true,
      "site": "004e9328",
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
      "004e9314",
      "READ",
      [
        "storage",
        "00c1aec0",
        null,
        "pointer"
      ]
    ],
    [
      "004e9328",
      "DATA",
      [
        "storage",
        "00be92b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e9364",
      "DATA",
      [
        "storage",
        "00be92b8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e9314",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004e9328",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e9364",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9260.md#insn-004e9314)
- 新版 `004e9314`（命令位置の公開資料なし）

~~~diff
- 004e9314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ec0:8"]]
- 004e9314 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e9314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f70:8"]]
+ 004e9314 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004e9314 bytes 736247f9
+ 004e9314 bytes 73ba47f9
~~~


<a id="compare-8cf13dd74e0c3b3508cd424d3ce95b82"></a>

### [`004e97e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e97e0.md) → [`004e97e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e97e0.md) _ZN5Botan4OCSP6CertIDC1ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc50.md) · 呼出先 14件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00490/00490630.md) [`00520804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00520/00520804.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bdcd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd00.md) · 呼出先 14件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e982c",
      "incomplete_value": true,
      "site": "004e9838",
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
      "definition_site": "004e982c",
      "incomplete_value": true,
      "site": "004e9838",
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
      "definition_site": "004e983c",
      "incomplete_value": true,
      "site": "004e983c",
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
      "definition_site": "004e983c",
      "incomplete_value": true,
      "site": "004e983c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e9a70",
      "incomplete_value": true,
      "site": "004e9a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9a70",
      "incomplete_value": true,
      "site": "004e9a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e981c",
      "READ",
      [
        "storage",
        "00c1b278",
        null,
        "pointer"
      ]
    ],
    [
      "004e9820",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004e9838",
      "DATA",
      [
        "storage",
        "00bea758",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e981c",
      "READ",
      [
        "storage",
        "00c1b328",
        null,
        "pointer"
      ]
    ],
    [
      "004e9820",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004e9838",
      "DATA",
      [
        "storage",
        "00bea808",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e981c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e97e0.md#insn-004e981c) · [`004e9820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e97e0.md#insn-004e9820) · [`004e9824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e97e0.md#insn-004e9824)
- 新版 `004e981c`（命令位置の公開資料なし） · `004e9820`（命令位置の公開資料なし）

~~~diff
- 004e981c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:278:8"]]
- 004e981c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e981c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:328:8"]]
+ 004e981c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e981c bytes 293d41f9
+ 004e981c bytes 299541f9
- 004e9820 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004e9820 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e9820 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004e9820 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004e9820 bytes 4a2547f9
+ 004e9820 bytes 4a7d47f9
- 004e9824 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004e9824 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cee06fcb2003d92b68ec957acb0fce3f"></a>

### [`004e9ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9ef4.md) → [`004e9ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9ef4.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e9f80",
      "incomplete_value": true,
      "site": "004e9f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f80",
      "incomplete_value": true,
      "site": "004e9f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
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
      "004e9f80",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e9f80",
      "PARAM",
      [
        "storage",
        "00be9d80",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e9f80",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ],
    [
      "004e9f80",
      "PARAM",
      [
        "storage",
        "00be9e30",
        "_ZTIN5Botan15Not_ImplementedE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9ef4.md#insn-004e9f80)
- 新版 `004e9f80`（命令位置の公開資料なし）

~~~diff
- 004e9f80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
- 004e9f80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e9f80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:190:8"]]
+ 004e9f80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004e9f80 bytes 217040f9
+ 004e9f80 bytes 21c840f9
~~~


<a id="compare-765d5450f8af64460e5f18acc3488f6e"></a>

### [`004e9fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9fdc.md) → [`004e9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004e7fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7fa0.md) · 呼出先 10件 [`0051854c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/0051854c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`004e7fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7fa0.md) · 呼出先 10件 [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea024",
      "incomplete_value": true,
      "site": "004ea024",
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
      "definition_site": "004ea024",
      "incomplete_value": true,
      "site": "004ea024",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea0ac",
      "incomplete_value": true,
      "site": "004ea0ac",
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
      "definition_site": "004ea0ac",
      "incomplete_value": true,
      "site": "004ea0ac",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea194",
      "incomplete_value": true,
      "site": "004ea194",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea194",
      "incomplete_value": true,
      "site": "004ea194",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ea010",
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ],
    [
      "004ea024",
      "DATA",
      [
        "storage",
        "00beb800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ea09c",
      "READ",
      [
        "storage",
        "00c1aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea010",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea024",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ea09c",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9fdc.md#insn-004ea010) · [`004ea09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9fdc.md#insn-004ea09c) · [`004ea184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e9/004e9fdc.md#insn-004ea184)
- 新版 `004ea010`（命令位置の公開資料なし） · `004ea09c`（命令位置の公開資料なし） · `004ea184`（命令位置の公開資料なし）

~~~diff
- 004ea010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:220:8"]]
- 004ea010 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 004ea010 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea010 bytes 941241f9
+ 004ea010 bytes 946a41f9
- 004ea09c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 004ea09c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea09c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004ea09c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea09c bytes 086147f9
+ 004ea09c bytes 08b947f9
- 004ea184 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:678:8"]]
- 004ea184 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea184 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
+ 004ea184 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea184 bytes 293f43f9
+ 004ea184 bytes 299743f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9c99fbbf5cf057913887a67b765054"></a>

### [`004ea498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea498.md) → [`004ea498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea498.md) _ZNK5Botan14PKCS10_Request20alternate_PEM_labelsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea4cc",
      "incomplete_value": true,
      "site": "004ea4dc",
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
                "const:91c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea4cc",
      "incomplete_value": true,
      "site": "004ea4dc",
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
                "const:925:8"
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
      "definition_site": "004ea4e0",
      "incomplete_value": true,
      "site": "004ea4e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ea4e0",
      "incomplete_value": true,
      "site": "004ea4e0",
      "value": [
        "LOAD",
        "8",
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
      "004ea4cc",
      "READ",
      [
        "storage",
        "002ac925",
        null,
        "string"
      ]
    ],
    [
      "004ea4d0",
      "READ",
      [
        "storage",
        "002ac934",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ea4cc",
      "READ",
      [
        "storage",
        "002ac91c",
        null,
        "string"
      ]
    ],
    [
      "004ea4d0",
      "READ",
      [
        "storage",
        "002ac92b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea498.md#insn-004ea4c4) · [`004ea4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea498.md#insn-004ea4c8)
- 新版 `004ea4c4`（命令位置の公開資料なし） · `004ea4c8`（命令位置の公開資料なし）

~~~diff
- 004ea4c4 ["COPY", "tmp:0:8", ["const:925:8"]]
- 004ea4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ea4c4 ["COPY", "tmp:0:8", ["const:91c:8"]]
+ 004ea4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ea4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ea4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 bytes 08952491
+ 004ea4c4 bytes 08712491
- 004ea4c8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004ea4c8 bytes 29eeffd0
+ 004ea4c8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004ea4c8 bytes 29eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbd301dfda325350cc1202d745b9c80"></a>

### [`004ea55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea55c.md) → [`004ea55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea55c.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdcd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004ea5dc",
      "incomplete_value": true,
      "site": "004ea5e4",
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
      "definition_site": "004ea5dc",
      "incomplete_value": true,
      "site": "004ea5e4",
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
      "004ea57c",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004ea584",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004ea59c",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004ea57c",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004ea584",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004ea59c",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea55c.md#insn-004ea57c) · [`004ea584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea55c.md#insn-004ea584) · [`004ea5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea55c.md#insn-004ea5d0)
- 新版 `004ea57c`（命令位置の公開資料なし） · `004ea584`（命令位置の公開資料なし） · `004ea5d0`（命令位置の公開資料なし）

~~~diff
- 004ea57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004ea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004ea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea57c bytes 083541f9
+ 004ea57c bytes 088d41f9
- 004ea584 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004ea584 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea584 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004ea584 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea584 bytes 4a2547f9
+ 004ea584 bytes 4a7d47f9
- 004ea5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 004ea5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 004ea5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea5d0 bytes 084141f9
+ 004ea5d0 bytes 089941f9
~~~


<a id="compare-dcd0b82dd59e8907af92dfdbcafbd5a9"></a>

### [`004ea660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea660.md) → [`004ea660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd30.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md) [`004840c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea6f8",
      "incomplete_value": true,
      "site": "004ea6f8",
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
      "definition_site": "004ea6f8",
      "incomplete_value": true,
      "site": "004ea6f8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea734",
      "incomplete_value": true,
      "site": "004ea734",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea734",
      "incomplete_value": true,
      "site": "004ea734",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea80c",
      "incomplete_value": true,
      "site": "004ea80c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea80c",
      "incomplete_value": true,
      "site": "004ea80c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ea6e8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f8",
      "DATA",
      [
        "storage",
        "00bea2c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ea724",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea6e8",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f8",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ea724",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea660.md#insn-004ea6e8) · [`004ea724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea660.md#insn-004ea724) · [`004ea7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea660.md#insn-004ea7fc)
- 新版 `004ea6e8`（命令位置の公開資料なし） · `004ea724`（命令位置の公開資料なし） · `004ea7fc`（命令位置の公開資料なし）

~~~diff
- 004ea6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 004ea6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004ea6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea6e8 bytes 087947f9
+ 004ea6e8 bytes 08d147f9
- 004ea724 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004ea724 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea724 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004ea724 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea724 bytes a93e43f9
+ 004ea724 bytes a99643f9
- 004ea7fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004ea7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea7fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004ea7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea7fc bytes 293d43f9
+ 004ea7fc bytes 299543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08db6290cf4aba6502212f37cf655419"></a>

### [`004eaec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004eaec8.md) → [`004eaec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004eaec8.md) _ZN5Botan14PKCS10_RequestC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd020.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d4f0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`00bdd0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0d0.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004eaf50",
      "incomplete_value": true,
      "site": "004eaf5c",
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
      "definition_site": "004eaf50",
      "incomplete_value": true,
      "site": "004eaf5c",
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
      "004eaee8",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004eaef0",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004eaf08",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004eaee8",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004eaef0",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004eaf08",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eaee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004eaec8.md#insn-004eaee8) · [`004eaef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004eaec8.md#insn-004eaef0) · [`004eaf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004eaec8.md#insn-004eaf44)
- 新版 `004eaee8`（命令位置の公開資料なし） · `004eaef0`（命令位置の公開資料なし） · `004eaf44`（命令位置の公開資料なし）

~~~diff
- 004eaee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004eaee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004eaee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaee8 bytes 083541f9
+ 004eaee8 bytes 088d41f9
- 004eaef0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004eaef0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaef0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004eaef0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaef0 bytes 4a2547f9
+ 004eaef0 bytes 4a7d47f9
- 004eaf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 004eaf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eaf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 004eaf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eaf44 bytes 084141f9
+ 004eaf44 bytes 089941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598dac731eee65f7a728dda70411a12d"></a>

### [`004eb040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb040.md) → [`004eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb040.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc710.md) [`00bdc720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc720.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004eb0c0",
      "incomplete_value": true,
      "site": "004eb0c8",
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
      "definition_site": "004eb0c0",
      "incomplete_value": true,
      "site": "004eb0c8",
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
      "004eb060",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004eb068",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004eb080",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004eb060",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004eb068",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004eb080",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb040.md#insn-004eb060) · [`004eb068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb040.md#insn-004eb068) · [`004eb0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb040.md#insn-004eb0b4)
- 新版 `004eb060`（命令位置の公開資料なし） · `004eb068`（命令位置の公開資料なし） · `004eb0b4`（命令位置の公開資料なし）

~~~diff
- 004eb060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004eb060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004eb060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb060 bytes 083541f9
+ 004eb060 bytes 088d41f9
- 004eb068 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004eb068 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb068 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004eb068 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb068 bytes 4a2547f9
+ 004eb068 bytes 4a7d47f9
- 004eb0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 004eb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 004eb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb0b4 bytes 084141f9
+ 004eb0b4 bytes 089941f9
~~~


<a id="compare-ba192c5f958b1c5886fb0c4a5f1c1e77"></a>

### [`004eb16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb16c.md) → [`004eb16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004830c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/004830c8.md) [`00483d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483d44.md)
- 新版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004830c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.45% / 新版 96.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 4件

アドレスに依存する影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb5dc",
      "incomplete_value": true,
      "site": "004eb5ec",
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
                "const:811:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eb5dc",
      "incomplete_value": true,
      "site": "004eb5ec",
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
                "const:784:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb5f0",
      "incomplete_value": true,
      "site": "004eb5f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004eb5f0",
      "incomplete_value": true,
      "site": "004eb5f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb7e4",
      "incomplete_value": true,
      "site": "004eb7e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:564:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eb7e4",
      "incomplete_value": true,
      "site": "004eb7e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004eb338",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "004eb38c",
      "DATA",
      [
        "storage",
        "00be9118",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eb3bc",
      "READ",
      [
        "storage",
        "00be9120",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004eb338",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "004eb38c",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eb3bc",
      "READ",
      [
        "storage",
        "00be91d0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb16c.md#insn-004eb338) · [`004eb354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004eb16c.md#insn-004eb354)
- 新版 `004eb338`（命令位置の公開資料なし） · `004eb354`（命令位置の公開資料なし）

~~~diff
- 004eb338 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e68:8"]]
- 004eb338 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eb338 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f18:8"]]
+ 004eb338 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eb338 bytes 293547f9
+ 004eb338 bytes 298d47f9
- 004eb354 ["COPY", "register:40e0:8", ["const:2ac000:8"]]
- 004eb354 bytes 1ceeffb0
+ 004eb354 ["COPY", "register:40e0:8", ["const:2ac000:8"]]
+ 004eb354 bytes 1ceeffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e4ada07c33e200cc2b8e0e3e4ec150"></a>

### [`004ebed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004ebed4.md) → [`004ebed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004ebed4.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd50.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce00.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ebf68",
      "incomplete_value": false,
      "site": "004ebf74",
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
            "const:955:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebf68",
      "incomplete_value": false,
      "site": "004ebf74",
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
            "const:9e9:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ebfe4",
      "incomplete_value": true,
      "site": "004ebff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebfe4",
      "incomplete_value": true,
      "site": "004ebff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
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
      "004ebf68",
      "PARAM",
      [
        "storage",
        "002ae9e9",
        null,
        "string"
      ]
    ],
    [
      "004ebfe4",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004ebfe4",
      "PARAM",
      [
        "storage",
        "00be9188",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ebf68",
      "PARAM",
      [
        "storage",
        "002ae955",
        null,
        "string"
      ]
    ],
    [
      "004ebfe4",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004ebfe4",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ebf68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004ebed4.md#insn-004ebf68) · [`004ebfe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004eb/004ebed4.md#insn-004ebfe4)
- 新版 `004ebf68`（命令位置の公開資料なし） · `004ebfe4`（命令位置の公開資料なし）

~~~diff
- 004ebf68 ["COPY", "tmp:0:8", ["const:9e9:8"]]
- 004ebf68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004ebf68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004ebf68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004ebf68 ["COPY", "tmp:0:8", ["const:955:8"]]
+ 004ebf68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004ebf68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004ebf68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004ebf68 bytes 42a42791
+ 004ebf68 bytes 42542591
- 004ebfe4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 004ebfe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ebfe4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 004ebfe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ebfe4 bytes 214c47f9
+ 004ebfe4 bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbccb55a0c821fee54aee72fccdf6cf1"></a>

### [`004ec0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec0b4.md) → [`004ec0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd40.md) · 呼出先 6件 [`00513e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/00513e2c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdc780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md) [`00bdcd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd70.md)
- 新版 呼出元 1件 [`00bdcdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcdf0.md) · 呼出先 6件 [`00513e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec0ec",
      "incomplete_value": true,
      "site": "004ec0ec",
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
      "definition_site": "004ec0ec",
      "incomplete_value": true,
      "site": "004ec0ec",
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
    "kind": "call_target",
    "new": {
      "definition_site": "004ec134",
      "incomplete_value": true,
      "site": "004ec134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec134",
      "incomplete_value": true,
      "site": "004ec134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ec0dc",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004ec0ec",
      "DATA",
      [
        "storage",
        "00bea2c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ec124",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec0dc",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004ec0ec",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ec124",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec0b4.md#insn-004ec0dc) · [`004ec124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec0b4.md#insn-004ec124)
- 新版 `004ec0dc`（命令位置の公開資料なし） · `004ec124`（命令位置の公開資料なし）

~~~diff
- 004ec0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 004ec0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004ec0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec0dc bytes 087947f9
+ 004ec0dc bytes 08d147f9
- 004ec124 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004ec124 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec124 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004ec124 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec124 bytes 293d43f9
+ 004ec124 bytes 299543f9
~~~


<a id="compare-dbcc3869bc0b97a02739b645c081d20b"></a>

### [`004ec1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec1d0.md) → [`004ec1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec1d0.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ec230",
      "incomplete_value": false,
      "site": "004ec238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b91:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec230",
      "incomplete_value": false,
      "site": "004ec238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b04:8"
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
      "definition_site": "004ec26c",
      "incomplete_value": true,
      "site": "004ec278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec26c",
      "incomplete_value": true,
      "site": "004ec278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ec230",
      "PARAM",
      [
        "storage",
        "00291b04",
        null,
        "string"
      ]
    ],
    [
      "004ec26c",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004ec26c",
      "PARAM",
      [
        "storage",
        "00be9200",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ec230",
      "PARAM",
      [
        "storage",
        "00291b91",
        null,
        "string"
      ]
    ],
    [
      "004ec26c",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004ec26c",
      "PARAM",
      [
        "storage",
        "00be92b0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec1d0.md#insn-004ec230) · [`004ec26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec1d0.md#insn-004ec26c)
- 新版 `004ec230`（命令位置の公開資料なし） · `004ec26c`（命令位置の公開資料なし）

~~~diff
- 004ec230 ["COPY", "tmp:0:8", ["const:b04:8"]]
- 004ec230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ec230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ec230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["COPY", "tmp:0:8", ["const:b91:8"]]
+ 004ec230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ec230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ec230 bytes 21102c91
+ 004ec230 bytes 21442e91
- 004ec26c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004ec26c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec26c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004ec26c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec26c bytes 213047f9
+ 004ec26c bytes 218847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f672a852b8b2520cb5987fbe909be3"></a>

### [`004ec368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec368.md) → [`004ec368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec368.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd80.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb730.md) [`00bdcb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb70.md) [`00bdcd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd70.md)
- 新版 呼出元 1件 [`00bdce30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce30.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) [`00bdcc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc20.md) [`00bdce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce20.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec3ac",
      "incomplete_value": true,
      "site": "004ec3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec3ac",
      "incomplete_value": true,
      "site": "004ec3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb4:8"
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
      "definition_site": "004ec3a0",
      "incomplete_value": true,
      "site": "004ec3b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec3a0",
      "incomplete_value": true,
      "site": "004ec3b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004ec418",
      "incomplete_value": true,
      "site": "004ec418",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "004ec418",
      "incomplete_value": true,
      "site": "004ec418",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ec398",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "004ec3a0",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ],
    [
      "004ec408",
      "READ",
      [
        "storage",
        "00c1b288",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec398",
      "READ",
      [
        "storage",
        "00299c41",
        null,
        "string"
      ]
    ],
    [
      "004ec3a0",
      "READ",
      [
        "storage",
        "00299c48",
        null,
        "string"
      ]
    ],
    [
      "004ec408",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec368.md#insn-004ec394) · [`004ec408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec368.md#insn-004ec408)
- 新版 `004ec394`（命令位置の公開資料なし） · `004ec408`（命令位置の公開資料なし）

~~~diff
- 004ec394 ["COPY", "tmp:0:8", ["const:bb4:8"]]
- 004ec394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["COPY", "tmp:0:8", ["const:c41:8"]]
+ 004ec394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ec394 bytes 29d12e91
+ 004ec394 bytes 29053191
- 004ec408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 004ec408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ec408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 004ec408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ec408 bytes 084541f9
+ 004ec408 bytes 089d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b2aa4c46b758b9273170227f235c9aa"></a>

### [`004ec514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec514.md) → [`004ec514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec514.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcda0.md) · 呼出先 12件 [`0050ecac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ecac.md) [`0051bf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d7fc.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`00bdce50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce50.md) · 呼出先 12件 [`0050ecac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ecac.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec55c",
      "incomplete_value": true,
      "site": "004ec56c",
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
                "const:47c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec55c",
      "incomplete_value": true,
      "site": "004ec56c",
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
                "const:510:8"
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
      "definition_site": "004ec570",
      "incomplete_value": true,
      "site": "004ec570",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec570",
      "incomplete_value": true,
      "site": "004ec570",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004ec5e0",
      "incomplete_value": true,
      "site": "004ec5e0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "004ec5e0",
      "incomplete_value": true,
      "site": "004ec5e0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ec55c",
      "READ",
      [
        "storage",
        "002a9510",
        null,
        "string"
      ]
    ],
    [
      "004ec560",
      "READ",
      [
        "storage",
        "002a951f",
        null,
        "string"
      ]
    ],
    [
      "004ec5d0",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec55c",
      "READ",
      [
        "storage",
        "002a947c",
        null,
        "string"
      ]
    ],
    [
      "004ec560",
      "READ",
      [
        "storage",
        "002a948b",
        null,
        "string"
      ]
    ],
    [
      "004ec5d0",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec514.md#insn-004ec554) · [`004ec558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec514.md#insn-004ec558)
- 新版 `004ec554`（命令位置の公開資料なし） · `004ec558`（命令位置の公開資料なし）

~~~diff
- 004ec554 ["COPY", "tmp:0:8", ["const:510:8"]]
- 004ec554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ec554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ec554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["COPY", "tmp:0:8", ["const:47c:8"]]
+ 004ec554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ec554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ec554 bytes 08411491
+ 004ec554 bytes 08f11191
- 004ec558 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004ec558 bytes 29eeff90
+ 004ec558 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004ec558 bytes 29eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa43401117e8abcdaecd3abcf893ced6"></a>

### [`004eca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004eca70.md) → [`004eca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004eca70.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcdd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdd0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdce80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ecad4",
      "incomplete_value": false,
      "site": "004ecadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:454:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecad4",
      "incomplete_value": false,
      "site": "004ecadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:3c7:8"
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
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "004ecad4",
      "PARAM",
      [
        "storage",
        "002a23c7",
        null,
        "string"
      ]
    ],
    [
      "004ecb10",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004ecb10",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ecad4",
      "PARAM",
      [
        "storage",
        "002a2454",
        null,
        "string"
      ]
    ],
    [
      "004ecb10",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004ecb10",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004eca70.md#insn-004ecad4) · [`004ecb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004eca70.md#insn-004ecb10)
- 新版 `004ecad4`（命令位置の公開資料なし） · `004ecb10`（命令位置の公開資料なし）

~~~diff
- 004ecad4 ["COPY", "tmp:0:8", ["const:3c7:8"]]
- 004ecad4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["COPY", "tmp:0:8", ["const:454:8"]]
+ 004ecad4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecad4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ecad4 bytes 211c0f91
+ 004ecad4 bytes 21501191
- 004ecb10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004ecb10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecb10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004ecb10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecb10 bytes 212c47f9
+ 004ecb10 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca9bfd9af50d557530319ee3b825350f"></a>

### [`004ecb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md) → [`004ecb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`004ed050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed050.md) [`004ed188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004ed050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed050.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecbb8",
      "incomplete_value": true,
      "site": "004ecbb8",
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
      "definition_site": "004ecbb8",
      "incomplete_value": true,
      "site": "004ecbb8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecbf4",
      "incomplete_value": true,
      "site": "004ecbf8",
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
      "definition_site": "004ecbf4",
      "incomplete_value": true,
      "site": "004ecbf8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ecd10",
      "incomplete_value": false,
      "site": "004ecd1c",
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
            "const:607:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecd10",
      "incomplete_value": false,
      "site": "004ecd1c",
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
            "const:57a:8"
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
      "004ecb9c",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004ecbb8",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecbf0",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ecb9c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004ecbb8",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecbf0",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md#insn-004ecb9c) · [`004ecbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md#insn-004ecbf0) · [`004ecd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md#insn-004ecd10)
- 新版 `004ecb9c`（命令位置の公開資料なし） · `004ecbf0`（命令位置の公開資料なし） · `004ecd10`（命令位置の公開資料なし）

~~~diff
- 004ecb9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 004ecb9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecb9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 004ecb9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecb9c bytes 292547f9
+ 004ecb9c bytes 297d47f9
- 004ecbf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004ecbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ecbf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004ecbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ecbf0 bytes 08f940f9
+ 004ecbf0 bytes 085141f9
- 004ecd10 ["COPY", "tmp:0:8", ["const:57a:8"]]
- 004ecd10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["COPY", "tmp:0:8", ["const:607:8"]]
+ 004ecd10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ecd10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ecd10 bytes 21e81591
+ 004ecd10 bytes 211c1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011b85b85e635cb49f97fe49080b8bd7"></a>

### [`004ed188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md) → [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md) FUN_004ed188

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004ecb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md) [`004ef8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef8d4.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) · 呼出先 16件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 5件 [`004ecb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md) [`004ef8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef8d4.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 16件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ed2f0",
      "incomplete_value": false,
      "site": "004ed2fc",
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
            "const:64c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed2f0",
      "incomplete_value": false,
      "site": "004ed2fc",
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
            "const:6e0:8"
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
      "definition_site": "004ed330",
      "incomplete_value": true,
      "site": "004ed33c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed330",
      "incomplete_value": true,
      "site": "004ed33c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "definition_site": "004ed37c",
      "incomplete_value": false,
      "site": "004ed388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed37c",
      "incomplete_value": false,
      "site": "004ed388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:704:8"
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
      "004ed2f0",
      "PARAM",
      [
        "storage",
        "002a96e0",
        null,
        "string"
      ]
    ],
    [
      "004ed330",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004ed330",
      "PARAM",
      [
        "storage",
        "00be91e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ed2f0",
      "PARAM",
      [
        "storage",
        "002a964c",
        null,
        "string"
      ]
    ],
    [
      "004ed330",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004ed330",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ed2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md#insn-004ed2f0) · [`004ed330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md#insn-004ed330) · [`004ed37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md#insn-004ed37c)
- 新版 `004ed2f0`（命令位置の公開資料なし） · `004ed330`（命令位置の公開資料なし） · `004ed37c`（命令位置の公開資料なし）

~~~diff
- 004ed2f0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 004ed2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["COPY", "tmp:0:8", ["const:64c:8"]]
+ 004ed2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004ed2f0 bytes 00801b91
+ 004ed2f0 bytes 00301991
- 004ed330 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004ed330 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ed330 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004ed330 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ed330 bytes 212047f9
+ 004ed330 bytes 217847f9
- 004ed37c ["COPY", "tmp:0:8", ["const:704:8"]]
- 004ed37c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004ed37c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004ed37c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004ed37c ["COPY", "tmp:0:8", ["const:70a:8"]]
+ 004ed37c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed37c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004ed37c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004ed37c bytes 00101c91
+ 004ed37c bytes 00281c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d552a80d6910188c8009d706260f4bc"></a>

### [`004edb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md) → [`004edb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004ed188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518128.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edb70",
      "incomplete_value": true,
      "site": "004edb70",
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
      "definition_site": "004edb70",
      "incomplete_value": true,
      "site": "004edb70",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edbac",
      "incomplete_value": true,
      "site": "004edbb0",
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
      "definition_site": "004edbac",
      "incomplete_value": true,
      "site": "004edbb0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004edcb8",
      "incomplete_value": true,
      "site": "004edcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edcb8",
      "incomplete_value": true,
      "site": "004edcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "004edb50",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004edb70",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004edba8",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004edb50",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004edb70",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004edba8",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md#insn-004edb50) · [`004edba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md#insn-004edba8) · [`004edcb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md#insn-004edcb8)
- 新版 `004edb50`（命令位置の公開資料なし） · `004edba8`（命令位置の公開資料なし） · `004edcb8`（命令位置の公開資料なし）

~~~diff
- 004edb50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 004edb50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edb50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 004edb50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004edb50 bytes 292547f9
+ 004edb50 bytes 297d47f9
- 004edba8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004edba8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edba8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004edba8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edba8 bytes 08f940f9
+ 004edba8 bytes 085141f9
- 004edcb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004edcb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edcb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004edcb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004edcb8 bytes 212047f9
+ 004edcb8 bytes 217847f9
~~~


<a id="compare-5f8c007ee81614b48d383575fb8e709f"></a>

### [`004ede80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md) → [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004e8484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8484.md) [`004ee34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee34c.md) [`004ee760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee760.md) [`0051854c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/0051854c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004e8484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8484.md) [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) [`004ee760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee760.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edf6c",
      "incomplete_value": true,
      "site": "004edf70",
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
      "definition_site": "004edf6c",
      "incomplete_value": true,
      "site": "004edf70",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004edfa0",
      "incomplete_value": true,
      "site": "004edfa4",
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
      "definition_site": "004edfa0",
      "incomplete_value": true,
      "site": "004edfa4",
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
      "definition_site": "004edfe0",
      "incomplete_value": true,
      "site": "004edfec",
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
      "definition_site": "004edfe0",
      "incomplete_value": true,
      "site": "004edfec",
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
      "004edf60",
      "READ",
      [
        "storage",
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "004edf70",
      "DATA",
      [
        "storage",
        "00bea890",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004edf98",
      "READ",
      [
        "storage",
        "00c1b288",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004edf60",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ],
    [
      "004edf70",
      "DATA",
      [
        "storage",
        "00bea940",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004edf98",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md#insn-004edf60) · [`004edf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md#insn-004edf98) · [`004edfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md#insn-004edfd0)
- 新版 `004edf60`（命令位置の公開資料なし） · `004edf98`（命令位置の公開資料なし） · `004edfd0`（命令位置の公開資料なし）

~~~diff
- 004edf60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
- 004edf60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edf60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:348:8"]]
+ 004edf60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edf60 bytes 084d41f9
+ 004edf60 bytes 08a541f9
- 004edf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 004edf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 004edf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edf98 bytes 084541f9
+ 004edf98 bytes 089d41f9
- 004edfd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004edfd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004edfd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 004edfd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004edfd0 bytes 085141f9
+ 004edfd0 bytes 08a941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9adbd53a1ddab4efb4f46dfe9255a9"></a>

### [`004ee34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee34c.md) → [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) FUN_004ee34c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ede80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md) [`00503af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) · 呼出先 7件 [`00519534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519534.md) [`0051bf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d7fc.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 4件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 7件 [`00519534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519534.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

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
      "definition_site": "004ee390",
      "incomplete_value": true,
      "site": "004ee3a4",
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
      "definition_site": "004ee390",
      "incomplete_value": true,
      "site": "004ee3a4",
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
      "004ee380",
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ],
    [
      "004ee3a4",
      "DATA",
      [
        "storage",
        "00beb800",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004ee380",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee3a4",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee34c.md#insn-004ee380)
- 新版 `004ee380`（命令位置の公開資料なし）

~~~diff
- 004ee380 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:220:8"]]
- 004ee380 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee380 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d0:8"]]
+ 004ee380 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee380 bytes 291141f9
+ 004ee380 bytes 296941f9
~~~


<a id="compare-35c7601b6c102ef4d951ad0b956c86e3"></a>

### [`004ee4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee4f4.md) → [`004ee4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee4f4.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcde0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcde0.md) · 呼出先 13件 [`004f3cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3cec.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528a6c.md) [`00528d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528d24.md)
- 新版 呼出元 1件 [`00bdce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md) · 呼出先 13件 [`004f3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3cec.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md) [`00528d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528d24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee588",
      "incomplete_value": true,
      "site": "004ee588",
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
      "definition_site": "004ee588",
      "incomplete_value": true,
      "site": "004ee588",
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
      "definition_site": "004ee5cc",
      "incomplete_value": true,
      "site": "004ee5d0",
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
      "definition_site": "004ee5cc",
      "incomplete_value": true,
      "site": "004ee5d0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ee578",
      "READ",
      [
        "storage",
        "00c1b230",
        null,
        "pointer"
      ]
    ],
    [
      "004ee588",
      "DATA",
      [
        "storage",
        "00bed378",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004ee5c0",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee578",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee588",
      "DATA",
      [
        "storage",
        "00bed428",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004ee5c0",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee4f4.md#insn-004ee578) · [`004ee5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee4f4.md#insn-004ee5c0)
- 新版 `004ee578`（命令位置の公開資料なし） · `004ee5c0`（命令位置の公開資料なし）

~~~diff
- 004ee578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
- 004ee578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004ee578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee578 bytes 081941f9
+ 004ee578 bytes 087141f9
- 004ee5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 004ee5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004ee5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee5c0 bytes 082947f9
+ 004ee5c0 bytes 088147f9
~~~


<a id="compare-4a30cdadbcddce69e585725bdac3337d"></a>

### [`004ee7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee7d8.md) → [`004ee7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce00.md) · 呼出先 16件 [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d614.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdceb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdceb0.md) · 呼出先 16件 [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ee8ac",
      "incomplete_value": true,
      "site": "004ee8ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee8ac",
      "incomplete_value": true,
      "site": "004ee8ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eea74",
      "incomplete_value": true,
      "site": "004eea74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eea74",
      "incomplete_value": true,
      "site": "004eea74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eeae0",
      "incomplete_value": true,
      "site": "004eeae0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eeae0",
      "incomplete_value": true,
      "site": "004eeae0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ee89c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004eea64",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004eead0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee89c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004eea64",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004eead0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee7d8.md#insn-004ee89c) · [`004eea64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee7d8.md#insn-004eea64) · [`004eead0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee7d8.md#insn-004eead0)
- 新版 `004ee89c`（命令位置の公開資料なし） · `004eea64`（命令位置の公開資料なし） · `004eead0`（命令位置の公開資料なし）

~~~diff
- 004ee89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 004ee89c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ee89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 004ee89c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee89c bytes 693e43f9
+ 004ee89c bytes 699643f9
- 004eea64 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
- 004eea64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eea64 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
+ 004eea64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eea64 bytes 893f43f9
+ 004eea64 bytes 899743f9
- 004eead0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
- 004eead0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004eead0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
+ 004eead0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004eead0 bytes 893f43f9
+ 004eead0 bytes 899743f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae6ea8493fb82bcdd1d35f473751317"></a>

### [`004ef204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md) → [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce20.md) · 呼出先 21件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004f43b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`0051854c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/0051854c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdced0.md) · 呼出先 21件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef258",
      "incomplete_value": true,
      "site": "004ef258",
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
      "definition_site": "004ef258",
      "incomplete_value": true,
      "site": "004ef258",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef2a8",
      "incomplete_value": true,
      "site": "004ef2b4",
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
      "definition_site": "004ef2a8",
      "incomplete_value": true,
      "site": "004ef2b4",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef318",
      "incomplete_value": true,
      "site": "004ef31c",
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
      "definition_site": "004ef318",
      "incomplete_value": true,
      "site": "004ef31c",
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
      "004ef240",
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ],
    [
      "004ef258",
      "DATA",
      [
        "storage",
        "00beb800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ef298",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ef240",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ef258",
      "DATA",
      [
        "storage",
        "00beb8b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ef298",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md#insn-004ef240) · [`004ef298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md#insn-004ef298) · [`004ef308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md#insn-004ef308)
- 新版 `004ef240`（命令位置の公開資料なし） · `004ef298`（命令位置の公開資料なし） · `004ef308`（命令位置の公開資料なし）

~~~diff
- 004ef240 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:220:8"]]
- 004ef240 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef240 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d0:8"]]
+ 004ef240 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef240 bytes 291141f9
+ 004ef240 bytes 296941f9
- 004ef298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004ef298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 004ef298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef298 bytes 085141f9
+ 004ef298 bytes 08a941f9
- 004ef308 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004ef308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ef308 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
+ 004ef308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ef308 bytes 085941f9
+ 004ef308 bytes 08b141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dbab22b5b2dfd1a421279f06b40b259"></a>

### [`004efa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efa38.md) → [`004efa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efa38.md) _ZN5Botan8X509_CRLC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdcd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004efab8",
      "incomplete_value": true,
      "site": "004efac0",
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
      "definition_site": "004efab8",
      "incomplete_value": true,
      "site": "004efac0",
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
      "004efa58",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004efa60",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004efa78",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efa58",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efa60",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efa78",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efa58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efa38.md#insn-004efa58) · [`004efa60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efa38.md#insn-004efa60) · [`004efaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efa38.md#insn-004efaac)
- 新版 `004efa58`（命令位置の公開資料なし） · `004efa60`（命令位置の公開資料なし） · `004efaac`（命令位置の公開資料なし）

~~~diff
- 004efa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004efa58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004efa58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efa58 bytes 083541f9
+ 004efa58 bytes 088d41f9
- 004efa60 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004efa60 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efa60 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004efa60 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efa60 bytes 4a2547f9
+ 004efa60 bytes 4a7d47f9
- 004efaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 004efaac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 004efaac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efaac bytes 080141f9
+ 004efaac bytes 085941f9
~~~


<a id="compare-5ff4c444c8748cc9ce518b2aa5eb9387"></a>

### [`004efb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efb8c.md) → [`004efb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d4f0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`00bdcef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004efc14",
      "incomplete_value": true,
      "site": "004efc20",
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
      "definition_site": "004efc14",
      "incomplete_value": true,
      "site": "004efc20",
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
      "004efbac",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004efbb4",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004efbcc",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efbac",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efbb4",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efbcc",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efb8c.md#insn-004efbac) · [`004efbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efb8c.md#insn-004efbb4) · [`004efc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efb8c.md#insn-004efc08)
- 新版 `004efbac`（命令位置の公開資料なし） · `004efbb4`（命令位置の公開資料なし） · `004efc08`（命令位置の公開資料なし）

~~~diff
- 004efbac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004efbac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efbac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004efbac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efbac bytes 083541f9
+ 004efbac bytes 088d41f9
- 004efbb4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004efbb4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efbb4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004efbb4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efbb4 bytes 4a2547f9
+ 004efbb4 bytes 4a7d47f9
- 004efc08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 004efc08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efc08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 004efc08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efc08 bytes 080141f9
+ 004efc08 bytes 085941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc7c6f1dbfe332843aa6c220dc8da48"></a>

### [`004efd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efd04.md) → [`004efd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efd04.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc710.md) [`00bdc720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc720.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004efd84",
      "incomplete_value": true,
      "site": "004efd8c",
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
      "definition_site": "004efd84",
      "incomplete_value": true,
      "site": "004efd8c",
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
      "004efd24",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004efd2c",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004efd44",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efd24",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efd2c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efd44",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efd04.md#insn-004efd24) · [`004efd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efd04.md#insn-004efd2c) · [`004efd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efd04.md#insn-004efd78)
- 新版 `004efd24`（命令位置の公開資料なし） · `004efd2c`（命令位置の公開資料なし） · `004efd78`（命令位置の公開資料なし）

~~~diff
- 004efd24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004efd24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004efd24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd24 bytes 083541f9
+ 004efd24 bytes 088d41f9
- 004efd2c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004efd2c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd2c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004efd2c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd2c bytes 4a2547f9
+ 004efd2c bytes 4a7d47f9
- 004efd78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 004efd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efd78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 004efd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efd78 bytes 080141f9
+ 004efd78 bytes 085941f9
~~~


<a id="compare-3b0a03be679b466d949903d4818fd042"></a>

### [`004efe30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efe30.md) → [`004efe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efe30.md) _ZN5Botan8X509_CRLC2ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00518ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525f90.md) [`00527c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00527/00527c8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00518ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525f90.md) [`00527c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/00527c8c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
      "definition_site": "004efee0",
      "incomplete_value": true,
      "site": "004efee8",
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
      "definition_site": "004efee0",
      "incomplete_value": true,
      "site": "004efee8",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004efe8c",
      "READ",
      [
        "storage",
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004efe90",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004efea4",
      "DATA",
      [
        "storage",
        "00bec960",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004efe8c",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004efe90",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004efea4",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efe8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efe30.md#insn-004efe8c) · [`004efe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efe30.md#insn-004efe90) · [`004efed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efe30.md#insn-004efed4)
- 新版 `004efe8c`（命令位置の公開資料なし） · `004efe90`（命令位置の公開資料なし） · `004efed4`（命令位置の公開資料なし）

~~~diff
- 004efe8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004efe8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efe8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004efe8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efe8c bytes 083541f9
+ 004efe8c bytes 088d41f9
- 004efe90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 004efe90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efe90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 004efe90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004efe90 bytes 292547f9
+ 004efe90 bytes 297d47f9
- 004efed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 004efed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004efed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 004efed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efed4 bytes 080141f9
+ 004efed4 bytes 085941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-accba26c07d95af47d3bfc9a4bee0670"></a>

### [`004f03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md) → [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 6件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0438",
      "incomplete_value": true,
      "site": "004f0438",
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
      "definition_site": "004f0438",
      "incomplete_value": true,
      "site": "004f0438",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0458",
      "incomplete_value": true,
      "site": "004f0458",
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
      "definition_site": "004f0458",
      "incomplete_value": true,
      "site": "004f0458",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0460",
      "incomplete_value": true,
      "site": "004f0460",
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
      "definition_site": "004f0460",
      "incomplete_value": true,
      "site": "004f0460",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f041c",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f0438",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0444",
      "READ",
      [
        "storage",
        "00c1aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f041c",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f0438",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0444",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f041c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md#insn-004f041c) · [`004f0434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md#insn-004f0434)
- 新版 `004f041c`（命令位置の公開資料なし） · `004f0434`（命令位置の公開資料なし）

~~~diff
- 004f041c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004f041c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f041c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004f041c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f041c bytes 08f140f9
+ 004f041c bytes 084941f9
- 004f0434 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004f0434 bytes f40300aa
+ 004f0434 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 004f0434 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef1699ce46f40a49eb0eb1e94adea07"></a>

### [`004f0f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f0f78.md) → [`004f0f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f0f78.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb00.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdcbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbb0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f0fd8",
      "incomplete_value": false,
      "site": "004f0fe0",
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
            "const:aad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0fd8",
      "incomplete_value": false,
      "site": "004f0fe0",
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
            "const:ab6:8"
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
      "definition_site": "004f1014",
      "incomplete_value": true,
      "site": "004f1020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1014",
      "incomplete_value": true,
      "site": "004f1020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "004f0fd8",
      "PARAM",
      [
        "storage",
        "002adab6",
        null,
        "string"
      ]
    ],
    [
      "004f1014",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004f1014",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f0fd8",
      "PARAM",
      [
        "storage",
        "002adaad",
        null,
        "string"
      ]
    ],
    [
      "004f1014",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004f1014",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f0f78.md#insn-004f0fd8) · [`004f1014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f0f78.md#insn-004f1014)
- 新版 `004f0fd8`（命令位置の公開資料なし） · `004f1014`（命令位置の公開資料なし）

~~~diff
- 004f0fd8 ["COPY", "tmp:0:8", ["const:ab6:8"]]
- 004f0fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f0fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f0fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f0fd8 ["COPY", "tmp:0:8", ["const:aad:8"]]
+ 004f0fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f0fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f0fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f0fd8 bytes 21d82a91
+ 004f0fd8 bytes 21b42a91
- 004f1014 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004f1014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1014 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004f1014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1014 bytes 212c47f9
+ 004f1014 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db6e1a926be85d2150ef0de3ead36e1e"></a>

### [`004f10f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f10f4.md) → [`004f10f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f10f4.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdcc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f113c",
      "incomplete_value": true,
      "site": "004f1144",
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
      "definition_site": "004f113c",
      "incomplete_value": true,
      "site": "004f1144",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f1130",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f1144",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f1130",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f1144",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f10f4.md#insn-004f1130)
- 新版 `004f1130`（命令位置の公開資料なし）

~~~diff
- 004f1130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004f1130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004f1130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1130 bytes 08f140f9
+ 004f1130 bytes 084941f9
~~~


<a id="compare-a01c5cda23a2c33395b482af721fe8cb"></a>

### [`004f1394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1394.md) → [`004f1394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1394.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb730.md) [`00bdcbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) [`00bdcc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f13f0",
      "incomplete_value": true,
      "site": "004f13f8",
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
      "definition_site": "004f13f0",
      "incomplete_value": true,
      "site": "004f13f8",
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
      "004f13e4",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f13f8",
      "DATA",
      [
        "storage",
        "00bea938",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f13e4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004f13f8",
      "DATA",
      [
        "storage",
        "00bea9e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f13e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1394.md#insn-004f13e4)
- 新版 `004f13e4`（命令位置の公開資料なし）

~~~diff
- 004f13e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004f13e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f13e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004f13e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f13e4 bytes 08f140f9
+ 004f13e4 bytes 084941f9
~~~


<a id="compare-ddc5f07e387fd2d852ef937249109abf"></a>

### [`004f1734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1734.md) → [`004f1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1734.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc20.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00bdccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdccd0.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.89% / 新版 86.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f18b8",
      "incomplete_value": true,
      "site": "004f18b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:56e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f18b8",
      "incomplete_value": true,
      "site": "004f18b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "004f1914",
      "incomplete_value": true,
      "site": "004f1914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1914",
      "incomplete_value": true,
      "site": "004f1914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:96d:8"
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
      "definition_site": "004f1908",
      "incomplete_value": true,
      "site": "004f1918",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f1908",
      "incomplete_value": true,
      "site": "004f1918",
      "value": [
        "LOAD",
        "8",
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
      "004f1888",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ],
    [
      "004f18a4",
      "READ",
      [
        "storage",
        "002aa568",
        null,
        "string"
      ]
    ],
    [
      "004f18dc",
      "PARAM",
      [
        "storage",
        "002a15b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f1888",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "004f18a4",
      "READ",
      [
        "storage",
        "002aa56e",
        null,
        "string"
      ]
    ],
    [
      "004f18dc",
      "PARAM",
      [
        "storage",
        "002a1645",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1734.md#insn-004f1888) · [`004f189c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1734.md#insn-004f189c) · [`004f18dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1734.md#insn-004f18dc)
- 新版 `004f1888`（命令位置の公開資料なし） · `004f189c`（命令位置の公開資料なし） · `004f18dc`（命令位置の公開資料なし）

~~~diff
- 004f1888 ["COPY", "tmp:0:8", ["const:68a:8"]]
- 004f1888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f1888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f1888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["COPY", "tmp:0:8", ["const:683:8"]]
+ 004f1888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f1888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f1888 bytes 21281a91
+ 004f1888 bytes 210c1a91
- 004f189c ["COPY", "tmp:0:8", ["const:568:8"]]
- 004f189c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f189c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f189c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f189c ["COPY", "tmp:0:8", ["const:56e:8"]]
+ 004f189c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f189c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f189c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f189c bytes 29a11591
+ 004f189c bytes 29b91591
- 004f18dc ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 004f18dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f18dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f18dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["COPY", "tmp:0:8", ["const:645:8"]]
+ 004f18dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f18dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f18dc bytes 21e01691
+ 004f18dc bytes 21141991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3c08ec6a256ba55d3c297c200412190"></a>

### [`004f1ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1ecc.md) → [`004f1ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcbd4.md) [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) · 呼出先 11件 [`004f2228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f2228.md) [`0051d614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d614.md) [`00526790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00526/00526790.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 11件 [`004f2228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f2228.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00526790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526790.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1f5c",
      "incomplete_value": true,
      "site": "004f1f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:56e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1f5c",
      "incomplete_value": true,
      "site": "004f1f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "004f1fa4",
      "incomplete_value": true,
      "site": "004f1fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1fa4",
      "incomplete_value": true,
      "site": "004f1fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:97d:8"
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
      "definition_site": "004f1fec",
      "incomplete_value": true,
      "site": "004f1fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:46d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1fec",
      "incomplete_value": true,
      "site": "004f1fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:474:8"
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
      "004f1f48",
      "READ",
      [
        "storage",
        "002aa568",
        null,
        "string"
      ]
    ],
    [
      "004f1f94",
      "READ",
      [
        "storage",
        "0029697d",
        null,
        "string"
      ]
    ],
    [
      "004f1fdc",
      "READ",
      [
        "storage",
        "002a5474",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f1f48",
      "READ",
      [
        "storage",
        "002aa56e",
        null,
        "string"
      ]
    ],
    [
      "004f1f94",
      "READ",
      [
        "storage",
        "00296a0a",
        null,
        "string"
      ]
    ],
    [
      "004f1fdc",
      "READ",
      [
        "storage",
        "002a546d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1ecc.md#insn-004f1f40) · [`004f1f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1ecc.md#insn-004f1f8c) · [`004f1fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1ecc.md#insn-004f1fd4)
- 新版 `004f1f40`（命令位置の公開資料なし） · `004f1f8c`（命令位置の公開資料なし） · `004f1fd4`（命令位置の公開資料なし）

~~~diff
- 004f1f40 ["COPY", "tmp:0:8", ["const:568:8"]]
- 004f1f40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f1f40 ["COPY", "tmp:0:8", ["const:56e:8"]]
+ 004f1f40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f1f40 bytes 29a11591
+ 004f1f40 bytes 29b91591
- 004f1f8c ["COPY", "tmp:0:8", ["const:97d:8"]]
- 004f1f8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["COPY", "tmp:0:8", ["const:a0a:8"]]
+ 004f1f8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1f8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f1f8c bytes 29f52591
+ 004f1f8c bytes 29292891
- 004f1fd4 ["COPY", "tmp:0:8", ["const:474:8"]]
- 004f1fd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["COPY", "tmp:0:8", ["const:46d:8"]]
+ 004f1fd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f1fd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f1fd4 bytes 29d11191
+ 004f1fd4 bytes 29b51191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c33bef7abc260cc865138a4d16af7a6"></a>

### [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) → [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce90.md) · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`004e0d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0d1c.md) [`004f3788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3788.md) [`004f3830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3830.md) [`004f38d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f38d8.md)
- 新版 呼出元 1件 [`00bdcf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf40.md) · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004e0d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0d1c.md) [`004f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3788.md) [`004f3830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3830.md) [`004f38d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f38d8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2850",
      "incomplete_value": true,
      "site": "004f2850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2850",
      "incomplete_value": true,
      "site": "004f2850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3da:8"
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
      "definition_site": "004f2920",
      "incomplete_value": true,
      "site": "004f2920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2920",
      "incomplete_value": true,
      "site": "004f2920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:300:8"
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
      "definition_site": "004f2a40",
      "incomplete_value": true,
      "site": "004f2a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:564:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2a40",
      "incomplete_value": true,
      "site": "004f2a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f2840",
      "READ",
      [
        "storage",
        "002a43da",
        null,
        "string"
      ]
    ],
    [
      "004f28e8",
      "READ",
      [
        "storage",
        "00c1b2c0",
        null,
        "pointer"
      ]
    ],
    [
      "004f28f4",
      "DATA",
      [
        "storage",
        "00bea968",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "004f2840",
      "READ",
      [
        "storage",
        "002a43d3",
        null,
        "string"
      ]
    ],
    [
      "004f28e8",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "004f28f4",
      "DATA",
      [
        "storage",
        "00beaa18",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md#insn-004f2838) · [`004f28e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md#insn-004f28e8) · [`004f2908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md#insn-004f2908)
- 新版 `004f2838`（命令位置の公開資料なし） · `004f28e8`（命令位置の公開資料なし） · `004f2908`（命令位置の公開資料なし）

~~~diff
- 004f2838 ["COPY", "tmp:0:8", ["const:3da:8"]]
- 004f2838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f2838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f2838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f2838 ["COPY", "tmp:0:8", ["const:3d3:8"]]
+ 004f2838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f2838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f2838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f2838 bytes 29690f91
+ 004f2838 bytes 294d0f91
- 004f28e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 004f28e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f28e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 004f28e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f28e8 bytes 086141f9
+ 004f28e8 bytes 08b941f9
- 004f2908 ["COPY", "tmp:0:8", ["const:300:8"]]
- 004f2908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f2908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f2908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f2908 ["COPY", "tmp:0:8", ["const:38d:8"]]
+ 004f2908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f2908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f2908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f2908 bytes 29010c91
+ 004f2908 bytes 29350e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a9eafbca7574e180f5f8be963237b44"></a>

### [`004f3788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3788.md) → [`004f3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3788.md) FUN_004f3788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f37c0",
      "incomplete_value": true,
      "site": "004f37c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:7ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f37c0",
      "incomplete_value": true,
      "site": "004f37c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:720:8"
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
      "004f37b0",
      "READ",
      [
        "storage",
        "00294720",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f37b0",
      "READ",
      [
        "storage",
        "002947ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f37a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3788.md#insn-004f37a4)
- 新版 `004f37a4`（命令位置の公開資料なし）

~~~diff
- 004f37a4 ["COPY", "tmp:0:8", ["const:720:8"]]
- 004f37a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["COPY", "tmp:0:8", ["const:7ad:8"]]
+ 004f37a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f37a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 bytes 29811c91
+ 004f37a4 bytes 29b51e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e158973f3a87c8e6ab51d1840fb5443d"></a>

### [`004f38d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f38d8.md) → [`004f38d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f38d8.md) FUN_004f38d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3910",
      "incomplete_value": true,
      "site": "004f3910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3910",
      "incomplete_value": true,
      "site": "004f3910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a54:8"
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
      "004f3900",
      "READ",
      [
        "storage",
        "00297a54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3900",
      "READ",
      [
        "storage",
        "00297ae1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f38f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f38d8.md#insn-004f38f4)
- 新版 `004f38f4`（命令位置の公開資料なし）

~~~diff
- 004f38f4 ["COPY", "tmp:0:8", ["const:a54:8"]]
- 004f38f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["COPY", "tmp:0:8", ["const:ae1:8"]]
+ 004f38f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f38f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 bytes 29512991
+ 004f38f4 bytes 29852b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-205bf590d3bb756b1c59c776fc9e3135"></a>

### [`004f3980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3980.md) → [`004f3980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3980.md) FUN_004f3980

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f39b8",
      "incomplete_value": true,
      "site": "004f39b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f39b8",
      "incomplete_value": true,
      "site": "004f39b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
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
      "004f39a8",
      "READ",
      [
        "storage",
        "002ab574",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f39a8",
      "READ",
      [
        "storage",
        "002ab57a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f399c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3980.md#insn-004f399c)
- 新版 `004f399c`（命令位置の公開資料なし）

~~~diff
- 004f399c ["COPY", "tmp:0:8", ["const:574:8"]]
- 004f399c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f399c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f399c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f399c ["COPY", "tmp:0:8", ["const:57a:8"]]
+ 004f399c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f399c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f399c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f399c bytes 29d11591
+ 004f399c bytes 29e91591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c07587130ed02b2c926d8f38ba9846"></a>

### [`004f3a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3a28.md) → [`004f3a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3a28.md) FUN_004f3a28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3a60",
      "incomplete_value": true,
      "site": "004f3a60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3a60",
      "incomplete_value": true,
      "site": "004f3a60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:35f:8"
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
      "004f3a50",
      "READ",
      [
        "storage",
        "0029d35f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3a50",
      "READ",
      [
        "storage",
        "0029d3ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3a28.md#insn-004f3a44)
- 新版 `004f3a44`（命令位置の公開資料なし）

~~~diff
- 004f3a44 ["COPY", "tmp:0:8", ["const:35f:8"]]
- 004f3a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["COPY", "tmp:0:8", ["const:3ec:8"]]
+ 004f3a44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3a44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3a44 bytes 297d0d91
+ 004f3a44 bytes 29b10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9be9282aea27208ff434683a50328a93"></a>

### [`004f3ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3ad0.md) → [`004f3ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3ad0.md) FUN_004f3ad0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3b08",
      "incomplete_value": true,
      "site": "004f3b08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3b08",
      "incomplete_value": true,
      "site": "004f3b08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2de:8"
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
      "004f3af8",
      "READ",
      [
        "storage",
        "0029b2de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3af8",
      "READ",
      [
        "storage",
        "0029b36b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3ad0.md#insn-004f3aec)
- 新版 `004f3aec`（命令位置の公開資料なし）

~~~diff
- 004f3aec ["COPY", "tmp:0:8", ["const:2de:8"]]
- 004f3aec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3aec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3aec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["COPY", "tmp:0:8", ["const:36b:8"]]
+ 004f3aec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3aec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3aec bytes 29790b91
+ 004f3aec bytes 29ad0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d2d9e77b1bf6f890649aec10a0b931"></a>

### [`004f3b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3b78.md) → [`004f3b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3b78.md) FUN_004f3b78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3ba0",
      "incomplete_value": true,
      "site": "004f3bb0",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:412:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3ba0",
      "incomplete_value": true,
      "site": "004f3bb0",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:385:8"
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
      "004f3ba0",
      "READ",
      [
        "storage",
        "002a0385",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f3ba0",
      "READ",
      [
        "storage",
        "002a0412",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3b78.md#insn-004f3b94)
- 新版 `004f3b94`（命令位置の公開資料なし）

~~~diff
- 004f3b94 ["COPY", "tmp:0:8", ["const:385:8"]]
- 004f3b94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["COPY", "tmp:0:8", ["const:412:8"]]
+ 004f3b94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f3b94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f3b94 bytes 29150e91
+ 004f3b94 bytes 29491091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ead764dfda9d130e9a785c37db3164d"></a>

### [`004f3c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3c20.md) → [`004f3c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3c20.md) FUN_004f3c20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "definition_site": "004f3c68",
      "incomplete_value": true,
      "site": "004f3c68",
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
      "004f3c48",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c54",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c68",
      "DATA",
      [
        "storage",
        "00bebe28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "004f3c48",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c54",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f3c68",
      "DATA",
      [
        "storage",
        "00bebed8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3c20.md#insn-004f3c48) · [`004f3c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3c20.md#insn-004f3c50)
- 新版 `004f3c48`（命令位置の公開資料なし） · `004f3c50`（命令位置の公開資料なし）

~~~diff
- 004f3c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 004f3c48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f3c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 004f3c48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f3c48 bytes 087941f9
+ 004f3c48 bytes 08d141f9
- 004f3c50 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004f3c50 bytes f30300aa
+ 004f3c50 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 004f3c50 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a7049db7b9aab265844879742d54ca"></a>

### [`004f3f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3f14.md) → [`004f3f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f3/004f3f14.md) _ZNK5Botan10Extensions20get_extension_objectERKNS_3OIDE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb70.md) · 呼出先 1件 [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md)
- 新版 呼出元 1件 [`00bdcc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc20.md) · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f400c",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:d8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f400c",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:d01:8"
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
      "definition_site": "004f4014",
      "incomplete_value": false,
      "site": "004f402c",
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
      "definition_site": "004f4014",
      "incomplete_value": false,
      "site": "004f402c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4024",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4024",
      "incomplete_value": false,
      "site": "004f402c",
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
            "const:b08:8"
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
      "004f400c",
      "PARAM",
      [
        "storage",
        "00299d01",
        null,
        "string"
      ]
    ],
    [
      "004f4014",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4024",
      "PARAM",
      [
        "storage",
        "002adb08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f400c",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4014",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4024",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f400c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3f14.md#insn-004f400c) · [`004f4014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3f14.md#insn-004f4014) · [`004f4020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f3/004f3f14.md#insn-004f4020)
- 新版 `004f400c`（命令位置の公開資料なし） · `004f4014`（命令位置の公開資料なし） · `004f4020`（命令位置の公開資料なし）

~~~diff
- 004f400c ["COPY", "tmp:0:8", ["const:d01:8"]]
- 004f400c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f400c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f400c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["COPY", "tmp:0:8", ["const:d8e:8"]]
+ 004f400c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f400c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f400c bytes 00043491
+ 004f400c bytes 00383691
- 004f4014 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004f4014 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4014 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4014 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004f4014 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4014 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4014 bytes 21641f91
+ 004f4014 bytes 21982191
- 004f4020 ["COPY", "register:4018:8", ["const:2ad000:8"]]
+ 004f4020 ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 004f4020 bytes c3edffb0
+ 004f4020 bytes a3edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33a9ffa0ccb2e6cac27b193b46e42e5"></a>

### [`004f4030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4030.md) → [`004f4030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4030.md) _ZNK5Botan10Extensions10extensionsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdceb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdceb0.md) · 呼出先 3件 [`00529214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529214.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md)
- 新版 呼出元 1件 [`00bdcf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf60.md) · 呼出先 3件 [`00529214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529214.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f414c",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:d8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f414c",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:d01:8"
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
    "new": {
      "definition_site": "004f4154",
      "incomplete_value": false,
      "site": "004f416c",
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
      "definition_site": "004f4154",
      "incomplete_value": false,
      "site": "004f416c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4164",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4164",
      "incomplete_value": false,
      "site": "004f416c",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f414c",
      "PARAM",
      [
        "storage",
        "00299d01",
        null,
        "string"
      ]
    ],
    [
      "004f4154",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4164",
      "PARAM",
      [
        "storage",
        "002adb08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f414c",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4154",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4164",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f414c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4030.md#insn-004f414c) · [`004f4154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4030.md#insn-004f4154) · [`004f4160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4030.md#insn-004f4160)
- 新版 `004f414c`（命令位置の公開資料なし） · `004f4154`（命令位置の公開資料なし） · `004f4160`（命令位置の公開資料なし）

~~~diff
- 004f414c ["COPY", "tmp:0:8", ["const:d01:8"]]
- 004f414c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f414c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f414c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["COPY", "tmp:0:8", ["const:d8e:8"]]
+ 004f414c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f414c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f414c bytes 00043491
+ 004f414c bytes 00383691
- 004f4154 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004f4154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004f4154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4154 bytes 21641f91
+ 004f4154 bytes 21982191
- 004f4160 ["COPY", "register:4018:8", ["const:2ad000:8"]]
+ 004f4160 ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 004f4160 bytes c3edffb0
+ 004f4160 bytes a3edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dbfae6f9b896082ba02eadedc15ef0b"></a>

### [`004f43b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md) → [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) _ZNK5Botan10Extensions11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ef204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md) · 呼出先 9件 [`004f45b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f45b0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) · 呼出先 9件 [`004f45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f45b0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4558",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:d8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4558",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:d01:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4560",
      "incomplete_value": false,
      "site": "004f4578",
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
      "definition_site": "004f4560",
      "incomplete_value": false,
      "site": "004f4578",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4570",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4570",
      "incomplete_value": false,
      "site": "004f4578",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4558",
      "PARAM",
      [
        "storage",
        "00299d01",
        null,
        "string"
      ]
    ],
    [
      "004f4560",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4570",
      "PARAM",
      [
        "storage",
        "002adb08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f4558",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4560",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004f4570",
      "PARAM",
      [
        "storage",
        "002a9697",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md#insn-004f4558) · [`004f4560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md#insn-004f4560) · [`004f456c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md#insn-004f456c)
- 新版 `004f4558`（命令位置の公開資料なし） · `004f4560`（命令位置の公開資料なし） · `004f456c`（命令位置の公開資料なし）

~~~diff
- 004f4558 ["COPY", "tmp:0:8", ["const:d01:8"]]
- 004f4558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f4558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f4558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["COPY", "tmp:0:8", ["const:d8e:8"]]
+ 004f4558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f4558 bytes 00043491
+ 004f4558 bytes 00383691
- 004f4560 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004f4560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004f4560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4560 bytes 21641f91
+ 004f4560 bytes 21982191
- 004f456c ["COPY", "register:4018:8", ["const:2ad000:8"]]
+ 004f456c ["COPY", "register:4018:8", ["const:2a9000:8"]]
- 004f456c bytes c3edffb0
+ 004f456c bytes a3edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-950af9d0a883ee5ddc058a4f7a282f17"></a>

### [`004f45b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f45b0.md) → [`004f45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f45b0.md) FUN_004f45b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004f43b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f43b8.md) [`00519534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519534.md) [`005273ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00527/005273ec.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 3件 [`004f43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f43b8.md) [`00519534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519534.md) [`005273ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/005273ec.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f45ec",
      "incomplete_value": true,
      "site": "004f45f0",
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
      "definition_site": "004f45ec",
      "incomplete_value": true,
      "site": "004f45f0",
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
      "004f45dc",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004f45f0",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f45dc",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f45f0",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f45dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f45b0.md#insn-004f45dc)
- 新版 `004f45dc`（命令位置の公開資料なし）

~~~diff
- 004f45dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 004f45dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f45dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004f45dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f45dc bytes 082947f9
+ 004f45dc bytes 088147f9
~~~


<a id="compare-b053659845c9c5ea186af278048f7815"></a>

### [`004f4778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md) → [`004f4778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md) _ZN5Botan10Extensions11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004e0894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0894.md) [`004f03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md) · 呼出先 21件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`004f4d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4d5c.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0051854c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/0051854c.md) [`00528a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528a6c.md)
- 新版 呼出元 2件 [`004e0894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0894.md) [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) · 呼出先 21件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`004f4d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4d5c.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/0051854c.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f48e8",
      "incomplete_value": true,
      "site": "004f48e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f48e8",
      "incomplete_value": true,
      "site": "004f48e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f4a84",
      "incomplete_value": true,
      "site": "004f4a84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4a84",
      "incomplete_value": true,
      "site": "004f4a84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4800",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004f48d8",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004f4800",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f48d8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md#insn-004f4800) · [`004f48d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md#insn-004f48d8) · [`004f4a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md#insn-004f4a74)
- 新版 `004f4800`（命令位置の公開資料なし） · `004f48d8`（命令位置の公開資料なし） · `004f4a74`（命令位置の公開資料なし）

~~~diff
- 004f4800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 004f4800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004f4800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4800 bytes 082947f9
+ 004f4800 bytes 088147f9
- 004f48d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:678:8"]]
- 004f48d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f48d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
+ 004f48d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f48d8 bytes 493f43f9
+ 004f48d8 bytes 499743f9
- 004f4a74 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:678:8"]]
- 004f4a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4a74 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
+ 004f4a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4a74 bytes 493f43f9
+ 004f4a74 bytes 499743f9
~~~


<a id="compare-76acde1801479e3a2841f47b70bcea04"></a>

### [`004f4d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4d5c.md) → [`004f4d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4d5c.md) FUN_004f4d5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f4778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4778.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`004f4778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4778.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f4dac",
      "incomplete_value": true,
      "site": "004f4dac",
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
      "definition_site": "004f4dac",
      "incomplete_value": true,
      "site": "004f4dac",
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
      "004f4d98",
      "READ",
      [
        "storage",
        "00c1b230",
        null,
        "pointer"
      ]
    ],
    [
      "004f4dac",
      "DATA",
      [
        "storage",
        "00bed378",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "004f4d98",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f4dac",
      "DATA",
      [
        "storage",
        "00bed428",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f4d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4d5c.md#insn-004f4d98)
- 新版 `004f4d98`（命令位置の公開資料なし）

~~~diff
- 004f4d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
- 004f4d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f4d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 004f4d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f4d98 bytes 081941f9
+ 004f4d98 bytes 087141f9
~~~


<a id="compare-4879ac3c93ecd9bc08231b2b9c6a52d2"></a>

### [`004f4e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4e50.md) → [`004f4e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f4/004f4e50.md) _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdced0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdced0.md) · 呼出先 6件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md)
- 新版 呼出元 1件 [`00bdcf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf80.md) · 呼出先 6件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4fd0",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:d8e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4fd0",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:d01:8"
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
    "new": {
      "definition_site": "004f4fd8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
      "definition_site": "004f4fd8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f4fe8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:697:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4fe8",
      "incomplete_value": false,
      "site": "004f4ff0",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f4edc",
      "PARAM",
      [
        "storage",
        "002a568c",
        null,
        "string"
      ]
    ],
    [
      "004f4fd0",
      "PARAM",
      [
        "storage",
        "00299d01",
        null,
        "string"
      ]
    ],
    [
      "004f4fd8",
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
      "004f4edc",
      "PARAM",
      [
        "storage",
        "002a5685",
        null,
        "string"
      ]
    ],
    [
      "004f4fd0",
      "PARAM",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "004f4fd8",
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

- 旧版 [`004f4e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4e50.md#insn-004f4e90) · [`004f4fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4e50.md#insn-004f4fd0) · [`004f4fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f4/004f4e50.md#insn-004f4fd8)
- 新版 `004f4e90`（命令位置の公開資料なし） · `004f4fd0`（命令位置の公開資料なし） · `004f4fd8`（命令位置の公開資料なし）

~~~diff
- 004f4e90 ["COPY", "tmp:0:8", ["const:68c:8"]]
- 004f4e90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["COPY", "tmp:0:8", ["const:685:8"]]
+ 004f4e90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004f4e90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004f4e90 bytes b5321a91
+ 004f4e90 bytes b5161a91
- 004f4fd0 ["COPY", "tmp:0:8", ["const:d01:8"]]
- 004f4fd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["COPY", "tmp:0:8", ["const:d8e:8"]]
+ 004f4fd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004f4fd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004f4fd0 bytes 00043491
+ 004f4fd0 bytes 00383691
- 004f4fd8 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004f4fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004f4fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f4fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f4fd8 bytes 21641f91
+ 004f4fd8 bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a818a6d60c1ae9caf2f4493951c651ec"></a>

### [`004f52c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f52c8.md) → [`004f52c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f52c8.md) _ZN5Botan14Cert_Extension17Basic_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 8件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md) [`00bdb930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f537c",
      "incomplete_value": true,
      "site": "004f537c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f537c",
      "incomplete_value": true,
      "site": "004f537c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f53c0",
      "incomplete_value": true,
      "site": "004f53c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f53c0",
      "incomplete_value": true,
      "site": "004f53c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f536c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f53b0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f536c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f53b0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f536c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f52c8.md#insn-004f536c) · [`004f53b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f52c8.md#insn-004f53b0)
- 新版 `004f536c`（命令位置の公開資料なし） · `004f53b0`（命令位置の公開資料なし）

~~~diff
- 004f536c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004f536c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f536c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004f536c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f536c bytes c93e43f9
+ 004f536c bytes c99643f9
- 004f53b0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004f53b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f53b0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004f53b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f53b0 bytes c93e43f9
+ 004f53b0 bytes c99643f9
~~~


<a id="compare-b7ded902d81583a608cf5070282762bf"></a>

### [`004f543c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f543c.md) → [`004f543c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f543c.md) _ZNK5Botan14Cert_Extension17Basic_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5478",
      "incomplete_value": true,
      "site": "004f548c",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5478",
      "incomplete_value": true,
      "site": "004f548c",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:6a8:8"
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
      "definition_site": "004f547c",
      "incomplete_value": true,
      "site": "004f5490",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f547c",
      "incomplete_value": true,
      "site": "004f5490",
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
                "const:d:8"
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
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f5504",
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
                "const:670:8"
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
      "004f5478",
      "READ",
      [
        "storage",
        "002aa6a8",
        null,
        "string"
      ]
    ],
    [
      "004f547c",
      "READ",
      [
        "storage",
        "002aa6b5",
        null,
        "string"
      ]
    ],
    [
      "004f54ec",
      "READ",
      [
        "storage",
        "002a7670",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f5478",
      "READ",
      [
        "storage",
        "002aa6ae",
        null,
        "string"
      ]
    ],
    [
      "004f547c",
      "READ",
      [
        "storage",
        "002aa6bb",
        null,
        "string"
      ]
    ],
    [
      "004f54ec",
      "READ",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f543c.md#insn-004f5470) · [`004f5474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f543c.md#insn-004f5474)
- 新版 `004f5470`（命令位置の公開資料なし） · `004f5474`（命令位置の公開資料なし）

~~~diff
- 004f5470 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 004f5470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f5470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f5470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f5470 ["COPY", "tmp:0:8", ["const:6ae:8"]]
+ 004f5470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f5470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f5470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f5470 bytes 08a11a91
+ 004f5470 bytes 08b91a91
- 004f5474 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f5474 bytes e9edff90
+ 004f5474 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f5474 bytes e9edff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-380b976792a1a531e63733d7c8701777"></a>

### [`004f55c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f55c0.md) → [`004f55c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f55c0.md) _ZNK5Botan14Cert_Extension9Key_Usage12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "004f5888",
      "incomplete_value": false,
      "site": "004f5890",
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
            "const:645:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5888",
      "incomplete_value": false,
      "site": "004f5890",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f58c0",
      "incomplete_value": true,
      "site": "004f58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f58c0",
      "incomplete_value": true,
      "site": "004f58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
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
      "004f5888",
      "PARAM",
      [
        "storage",
        "002a05b8",
        null,
        "string"
      ]
    ],
    [
      "004f58c0",
      "READ",
      [
        "storage",
        "00c1aea8",
        null,
        "pointer"
      ]
    ],
    [
      "004f58c0",
      "PARAM",
      [
        "storage",
        "00be9230",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f5888",
      "PARAM",
      [
        "storage",
        "002a0645",
        null,
        "string"
      ]
    ],
    [
      "004f58c0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004f58c0",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f55c0.md#insn-004f5888) · [`004f58c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f55c0.md#insn-004f58c0)
- 新版 `004f5888`（命令位置の公開資料なし） · `004f58c0`（命令位置の公開資料なし）

~~~diff
- 004f5888 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 004f5888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f5888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f5888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["COPY", "tmp:0:8", ["const:645:8"]]
+ 004f5888 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5888 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f5888 bytes 21e01691
+ 004f5888 bytes 21141991
- 004f58c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ea8:8"]]
- 004f58c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f58c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004f58c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f58c0 bytes 215447f9
+ 004f58c0 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced2bb469f5ea258e59428bcc6464ae3"></a>

### [`004f5994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5994.md) → [`004f5994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5994.md) _ZN5Botan14Cert_Extension9Key_Usage12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.68% / 新版 96.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f5c4c",
      "incomplete_value": true,
      "site": "004f5c4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5c4c",
      "incomplete_value": true,
      "site": "004f5c4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f5c90",
      "incomplete_value": true,
      "site": "004f5c90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5c90",
      "incomplete_value": true,
      "site": "004f5c90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f5cd0",
      "incomplete_value": false,
      "site": "004f5cd8",
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
            "const:506:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5cd0",
      "incomplete_value": false,
      "site": "004f5cd8",
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
            "const:479:8"
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
      "004f5c3c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f5c80",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f5cd0",
      "PARAM",
      [
        "storage",
        "0029e479",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f5c3c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f5c80",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f5cd0",
      "PARAM",
      [
        "storage",
        "0029e506",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5994.md#insn-004f5c3c) · [`004f5c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5994.md#insn-004f5c80) · [`004f5cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5994.md#insn-004f5cd0)
- 新版 `004f5c3c`（命令位置の公開資料なし） · `004f5c80`（命令位置の公開資料なし） · `004f5cd0`（命令位置の公開資料なし）

~~~diff
- 004f5c3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004f5c3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5c3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004f5c3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f5c3c bytes c93e43f9
+ 004f5c3c bytes c99643f9
- 004f5c80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004f5c80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5c80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004f5c80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f5c80 bytes c93e43f9
+ 004f5c80 bytes c99643f9
- 004f5cd0 ["COPY", "tmp:0:8", ["const:479:8"]]
- 004f5cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["COPY", "tmp:0:8", ["const:506:8"]]
+ 004f5cd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004f5cd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004f5cd0 bytes 21e41191
+ 004f5cd0 bytes 21181491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef7e42b8e9db60a60853fd783baaea9"></a>

### [`004f5e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5e48.md) → [`004f5e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f5e48.md) _ZNK5Botan14Cert_Extension9Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5e80",
      "incomplete_value": true,
      "site": "004f5e80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5e80",
      "incomplete_value": true,
      "site": "004f5e80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb4:8"
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
      "definition_site": "004f5e78",
      "incomplete_value": true,
      "site": "004f5e84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f5e78",
      "incomplete_value": true,
      "site": "004f5e84",
      "value": [
        "LOAD",
        "8",
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
      "004f5e68",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "004f5e78",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f5e68",
      "READ",
      [
        "storage",
        "00299c41",
        null,
        "string"
      ]
    ],
    [
      "004f5e78",
      "READ",
      [
        "storage",
        "00299c48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f5e48.md#insn-004f5e60)
- 新版 `004f5e60`（命令位置の公開資料なし）

~~~diff
- 004f5e60 ["COPY", "tmp:0:8", ["const:bb4:8"]]
- 004f5e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["COPY", "tmp:0:8", ["const:c41:8"]]
+ 004f5e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f5e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f5e60 bytes 29d12e91
+ 004f5e60 bytes 29053191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13de128ea3b716be66e000c9c301ca18"></a>

### [`004f6118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6118.md) → [`004f6118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6118.md) _ZNK5Botan14Cert_Extension14Subject_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdcba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f6154",
      "incomplete_value": true,
      "site": "004f6164",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:2a9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6154",
      "incomplete_value": true,
      "site": "004f6164",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:21c:8"
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
      "definition_site": "004f6158",
      "incomplete_value": true,
      "site": "004f6168",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6158",
      "incomplete_value": true,
      "site": "004f6168",
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
                "const:b:8"
              ]
            ]
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
      "004f6154",
      "READ",
      [
        "storage",
        "002a221c",
        null,
        "string"
      ]
    ],
    [
      "004f6158",
      "READ",
      [
        "storage",
        "002a2227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f6154",
      "READ",
      [
        "storage",
        "002a22a9",
        null,
        "string"
      ]
    ],
    [
      "004f6158",
      "READ",
      [
        "storage",
        "002a22b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f614c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6118.md#insn-004f614c) · [`004f6150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6118.md#insn-004f6150)
- 新版 `004f614c`（命令位置の公開資料なし） · `004f6150`（命令位置の公開資料なし）

~~~diff
- 004f614c ["COPY", "tmp:0:8", ["const:21c:8"]]
- 004f614c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f614c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f614c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 004f614c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f614c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f614c bytes 08710891
+ 004f614c bytes 08a50a91
- 004f6150 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f6150 bytes c9edfff0
+ 004f6150 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f6150 bytes c9edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60a9f74cb0b724d1cf76eb4dc884d87c"></a>

### [`004f61e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f61e8.md) → [`004f61e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f61e8.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdcea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f6228",
      "incomplete_value": true,
      "site": "004f6230",
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
      "definition_site": "004f6228",
      "incomplete_value": true,
      "site": "004f6230",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f6224",
      "READ",
      [
        "storage",
        "00c1b2c0",
        null,
        "pointer"
      ]
    ],
    [
      "004f6230",
      "DATA",
      [
        "storage",
        "00bea968",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "004f6224",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "004f6230",
      "DATA",
      [
        "storage",
        "00beaa18",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f6224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f61e8.md#insn-004f6224)
- 新版 `004f6224`（命令位置の公開資料なし）

~~~diff
- 004f6224 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c0:8"]]
- 004f6224 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6224 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:370:8"]]
+ 004f6224 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f6224 bytes 296141f9
+ 004f6224 bytes 29b941f9
~~~


<a id="compare-b51627538d42510459c92e0a0d0c82c5"></a>

### [`004f6548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6548.md) → [`004f6548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6548.md) _ZN5Botan14Cert_Extension16Authority_Key_ID12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004e7de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7de0.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7b0.md) [`00bdb930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb930.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004e7de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7de0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f65dc",
      "incomplete_value": true,
      "site": "004f65dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f65dc",
      "incomplete_value": true,
      "site": "004f65dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f6620",
      "incomplete_value": true,
      "site": "004f6620",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6620",
      "incomplete_value": true,
      "site": "004f6620",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f65cc",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f6610",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f65cc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f6610",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f65cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6548.md#insn-004f65cc) · [`004f6610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6548.md#insn-004f6610)
- 新版 `004f65cc`（命令位置の公開資料なし） · `004f6610`（命令位置の公開資料なし）

~~~diff
- 004f65cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004f65cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f65cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004f65cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f65cc bytes a93e43f9
+ 004f65cc bytes a99643f9
- 004f6610 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004f6610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6610 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004f6610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f6610 bytes a93e43f9
+ 004f6610 bytes a99643f9
~~~


<a id="compare-0302173957dac8545cb16ac26ce7e4aa"></a>

### [`004f6690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6690.md) → [`004f6690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f6690.md) _ZNK5Botan14Cert_Extension16Authority_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdcba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f66d8",
      "incomplete_value": true,
      "site": "004f66e8",
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
                "const:584:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f66d8",
      "incomplete_value": true,
      "site": "004f66e8",
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
                "const:57e:8"
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
      "definition_site": "004f66dc",
      "incomplete_value": true,
      "site": "004f66ec",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f66dc",
      "incomplete_value": true,
      "site": "004f66ec",
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
                "const:d:8"
              ]
            ]
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
      "004f66d8",
      "READ",
      [
        "storage",
        "002ab57e",
        null,
        "string"
      ]
    ],
    [
      "004f66dc",
      "READ",
      [
        "storage",
        "002ab58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f66d8",
      "READ",
      [
        "storage",
        "002ab584",
        null,
        "string"
      ]
    ],
    [
      "004f66dc",
      "READ",
      [
        "storage",
        "002ab591",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f66d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6690.md#insn-004f66d0) · [`004f66d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f6690.md#insn-004f66d4)
- 新版 `004f66d0`（命令位置の公開資料なし） · `004f66d4`（命令位置の公開資料なし）

~~~diff
- 004f66d0 ["COPY", "tmp:0:8", ["const:57e:8"]]
- 004f66d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f66d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f66d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f66d0 ["COPY", "tmp:0:8", ["const:584:8"]]
+ 004f66d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f66d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f66d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f66d0 bytes 08f91591
+ 004f66d0 bytes 08111691
- 004f66d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f66d4 bytes c9edfff0
+ 004f66d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f66d4 bytes c9edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afaf68f8fd633f082e8da1161e6b41f4"></a>

### [`004f7170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7170.md) → [`004f7170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7170.md) _ZNK5Botan14Cert_Extension18Extended_Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f71b4",
      "incomplete_value": true,
      "site": "004f71cc",
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
                "const:47c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f71b4",
      "incomplete_value": true,
      "site": "004f71cc",
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
                "const:510:8"
              ]
            ]
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
      "004f71b4",
      "READ",
      [
        "storage",
        "002a9510",
        null,
        "string"
      ]
    ],
    [
      "004f71b8",
      "READ",
      [
        "storage",
        "002a951f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f71b4",
      "READ",
      [
        "storage",
        "002a947c",
        null,
        "string"
      ]
    ],
    [
      "004f71b8",
      "READ",
      [
        "storage",
        "002a948b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f71ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7170.md#insn-004f71ac)
- 新版 `004f71ac`（命令位置の公開資料なし）

~~~diff
- 004f71ac ["COPY", "tmp:0:8", ["const:510:8"]]
- 004f71ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f71ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f71ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["COPY", "tmp:0:8", ["const:47c:8"]]
+ 004f71ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f71ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f71ac bytes 29411491
+ 004f71ac bytes 29f11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95a8fdf9b38252085daeb11efc5611ff"></a>

### [`004f72c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f72c0.md) → [`004f72c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f72c0.md) _ZNK5Botan14Cert_Extension16Name_Constraints12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f7300",
      "incomplete_value": true,
      "site": "004f7314",
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
                "const:bd4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7300",
      "incomplete_value": true,
      "site": "004f7314",
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
                "const:b47:8"
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
      "definition_site": "004f7304",
      "incomplete_value": true,
      "site": "004f7318",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7304",
      "incomplete_value": true,
      "site": "004f7318",
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
                "const:9:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f734c",
      "incomplete_value": true,
      "site": "004f7358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f734c",
      "incomplete_value": true,
      "site": "004f7358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
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
      "004f7300",
      "READ",
      [
        "storage",
        "00295b47",
        null,
        "string"
      ]
    ],
    [
      "004f7304",
      "READ",
      [
        "storage",
        "00295b50",
        null,
        "string"
      ]
    ],
    [
      "004f734c",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f7300",
      "READ",
      [
        "storage",
        "00295bd4",
        null,
        "string"
      ]
    ],
    [
      "004f7304",
      "READ",
      [
        "storage",
        "00295bdd",
        null,
        "string"
      ]
    ],
    [
      "004f734c",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f72f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f72c0.md#insn-004f72f8) · [`004f72fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f72c0.md#insn-004f72fc)
- 新版 `004f72f8`（命令位置の公開資料なし） · `004f72fc`（命令位置の公開資料なし）

~~~diff
- 004f72f8 ["COPY", "tmp:0:8", ["const:b47:8"]]
- 004f72f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["COPY", "tmp:0:8", ["const:bd4:8"]]
+ 004f72f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004f72f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004f72f8 bytes 081d2d91
+ 004f72f8 bytes 08512f91
- 004f72fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004f72fc bytes c9edffd0
+ 004f72fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f72fc bytes c9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8735328fa21cfe5628bced87d3486aa"></a>

### [`004f73a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f73a8.md) → [`004f73a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md) _ZN5Botan14Cert_Extension16Name_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004f7afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7afc.md) [`004f7cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7cc4.md) [`004f7dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7dec.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md)
- 新版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004f7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7afc.md) [`004f7cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7cc4.md) [`004f7dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7dec.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f7500",
      "incomplete_value": true,
      "site": "004f7500",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7500",
      "incomplete_value": true,
      "site": "004f7500",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f752c",
      "incomplete_value": true,
      "site": "004f752c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f752c",
      "incomplete_value": true,
      "site": "004f752c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f7570",
      "incomplete_value": true,
      "site": "004f7570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f7570",
      "incomplete_value": true,
      "site": "004f7570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f74f0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f751c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f7560",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f74f0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f751c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f7560",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f74f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f73a8.md#insn-004f74f0) · [`004f751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f73a8.md#insn-004f751c) · [`004f7560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f73a8.md#insn-004f7560)
- 新版 `004f74f0`（命令位置の公開資料なし） · `004f751c`（命令位置の公開資料なし） · `004f7560`（命令位置の公開資料なし）

~~~diff
- 004f74f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004f74f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f74f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004f74f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f74f0 bytes a93e43f9
+ 004f74f0 bytes a99643f9
- 004f751c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004f751c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f751c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004f751c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f751c bytes a93e43f9
+ 004f751c bytes a99643f9
- 004f7560 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004f7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f7560 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004f7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f7560 bytes a93e43f9
+ 004f7560 bytes a99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2770549cbf87149e29d80b7d9cd5634"></a>

### [`004f7f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7f54.md) → [`004f7f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f7f54.md) _ZNK5Botan14Cert_Extension16Name_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`004e6520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6520.md) [`00525380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525380.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`004e6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md) [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8138",
      "incomplete_value": true,
      "site": "004f8140",
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
      "definition_site": "004f8138",
      "incomplete_value": true,
      "site": "004f8140",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
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
                "const:50:8"
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
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
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
                "const:50:8"
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f8148",
      "incomplete_value": true,
      "site": "004f8148",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298e43",
        null,
        "string"
      ]
    ],
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298e53",
        null,
        "string"
      ]
    ],
    [
      "004f80a4",
      "READ",
      [
        "storage",
        "00293959",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298ed0",
        null,
        "string"
      ]
    ],
    [
      "004f7fe4",
      "READ",
      [
        "storage",
        "00298ee0",
        null,
        "string"
      ]
    ],
    [
      "004f80a4",
      "READ",
      [
        "storage",
        "002939e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f7fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7f54.md#insn-004f7fa4) · [`004f8070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7f54.md#insn-004f8070) · [`004f8134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f7f54.md#insn-004f8134)
- 新版 `004f7fa4`（命令位置の公開資料なし） · `004f8070`（命令位置の公開資料なし） · `004f8134`（命令位置の公開資料なし）

~~~diff
- 004f7fa4 ["COPY", "tmp:0:8", ["const:e43:8"]]
- 004f7fa4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 004f7fa4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f7fa4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 004f7fa4 bytes 390f3991
+ 004f7fa4 bytes 39433b91
- 004f8070 ["COPY", "tmp:0:8", ["const:959:8"]]
- 004f8070 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["COPY", "tmp:0:8", ["const:9e6:8"]]
+ 004f8070 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 004f8070 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 004f8070 bytes 18672591
+ 004f8070 bytes 189b2791
- 004f8134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 004f8134 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8134 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 004f8134 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8134 bytes 739246f9
+ 004f8134 bytes 73ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14a97b69cea3c49d355706f48b25755"></a>

### [`004f8244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md) → [`004f8244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md) _ZN5Botan14Cert_Extension16Name_Constraints8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocatorIS8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0051d9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d9e4.md) [`00529cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529cc4.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0051d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9e4.md) [`00529cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529cc4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
      "definition_site": "004f842c",
      "incomplete_value": true,
      "site": "004f842c",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f84b4",
      "incomplete_value": true,
      "site": "004f84b4",
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
      "definition_site": "004f84b4",
      "incomplete_value": true,
      "site": "004f84b4",
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
      "004f82bc",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ],
    [
      "004f82c0",
      "READ",
      [
        "storage",
        "00295988",
        null,
        "string"
      ]
    ],
    [
      "004f83b8",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f82bc",
      "READ",
      [
        "storage",
        "00295a07",
        null,
        "string"
      ]
    ],
    [
      "004f82c0",
      "READ",
      [
        "storage",
        "00295a15",
        null,
        "string"
      ]
    ],
    [
      "004f83b8",
      "READ",
      [
        "storage",
        "00295a07",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f82b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md#insn-004f82b4) · [`004f8414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md#insn-004f8414) · [`004f8418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md#insn-004f8418)
- 新版 `004f82b4`（命令位置の公開資料なし） · `004f8414`（命令位置の公開資料なし） · `004f8418`（命令位置の公開資料なし）

~~~diff
- 004f82b4 ["COPY", "tmp:0:8", ["const:97a:8"]]
- 004f82b4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["COPY", "tmp:0:8", ["const:a07:8"]]
+ 004f82b4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004f82b4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004f82b4 bytes 94ea2591
+ 004f82b4 bytes 941e2891
- 004f8414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:260:8"]]
- 004f8414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:310:8"]]
+ 004f8414 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8414 bytes 293141f9
+ 004f8414 bytes 298941f9
- 004f8418 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:238:8"]]
- 004f8418 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8418 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2e8:8"]]
+ 004f8418 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8418 bytes 941e41f9
+ 004f8418 bytes 947641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

