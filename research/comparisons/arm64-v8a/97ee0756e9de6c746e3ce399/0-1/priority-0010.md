# v15.7.2 → v15.7.3 · 最優先の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-ce20a71090545c7c0502e0c3282aed6b"></a>

### [`004caf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004caf04.md) → [`004caf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004caf04.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc6f0.md) · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a9c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdc7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7a0.md) · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004caf1c",
      "incomplete_value": false,
      "site": "004caf2c",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004caf1c",
      "incomplete_value": false,
      "site": "004caf2c",
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
            "const:4f0:8"
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
      "004caf2c",
      "DATA",
      [
        "storage",
        "00bed4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed510",
        null,
        "pointer"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004caf2c",
      "DATA",
      [
        "storage",
        "00bed5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed5c0",
        null,
        "pointer"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004caf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004caf04.md#insn-004caf1c)
- 新版 [`004caf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004caf04.md#insn-004caf1c)

~~~diff
- 004caf1c ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 004caf1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 004caf1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004caf1c bytes 4ac11391
+ 004caf1c bytes 4a811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f29146afb42f4637ef82f70ac6c7a6d0"></a>

### [`004cafdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004cafdc.md) → [`004cafdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc700.md) · 呼出先 9件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a9c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdc7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7b0.md) · 呼出先 9件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb028",
      "incomplete_value": false,
      "site": "004cb030",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb028",
      "incomplete_value": false,
      "site": "004cb030",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cb09c",
      "incomplete_value": true,
      "site": "004cb09c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cb09c",
      "incomplete_value": true,
      "site": "004cb09c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cb030",
      "DATA",
      [
        "storage",
        "00bed4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed510",
        null,
        "pointer"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004cb030",
      "DATA",
      [
        "storage",
        "00bed5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed5c0",
        null,
        "pointer"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004cafdc.md#insn-004cb028) · [`004cb08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004cafdc.md#insn-004cb08c)
- 新版 [`004cb028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md#insn-004cb028) · [`004cb08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md#insn-004cb08c)

~~~diff
- 004cb028 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 004cb028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cb028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cb028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 004cb028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cb028 bytes 08c11391
+ 004cb028 bytes 08811691
- 004cb08c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004cb08c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cb08c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004cb08c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cb08c bytes 293d43f9
+ 004cb08c bytes 299543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d893c6d79f85b74a60c2240a408a52b3"></a>

### [`004cb37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb37c.md) → [`004cb37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb37c.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a9c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb394",
      "incomplete_value": false,
      "site": "004cb3a4",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb394",
      "incomplete_value": false,
      "site": "004cb3a4",
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
            "const:4f0:8"
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
      "004cb3a4",
      "DATA",
      [
        "storage",
        "00bed4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed510",
        null,
        "pointer"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004cb3a4",
      "DATA",
      [
        "storage",
        "00bed5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed5c0",
        null,
        "pointer"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb37c.md#insn-004cb394)
- 新版 [`004cb394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb37c.md#insn-004cb394)

~~~diff
- 004cb394 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 004cb394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 004cb394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cb394 bytes 29c11391
+ 004cb394 bytes 29811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30d64e47fb8b5d6cdc6e911fea579945"></a>

### [`004cb65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb65c.md) → [`004cb65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb65c.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00522c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522c18.md) [`00522cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522cdc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522c18.md) [`00522cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522cdc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb6d4",
      "incomplete_value": false,
      "site": "004cb6d4",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb6d4",
      "incomplete_value": false,
      "site": "004cb6d4",
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
            "const:570:8"
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
      "004cb6d4",
      "DATA",
      [
        "storage",
        "00bed570",
        null,
        "pointer"
      ]
    ],
    [
      "004cb714",
      "READ",
      [
        "storage",
        "00bed580",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb778",
      "READ",
      [
        "storage",
        "00bed598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004cb6d4",
      "DATA",
      [
        "storage",
        "00bed620",
        null,
        "pointer"
      ]
    ],
    [
      "004cb714",
      "READ",
      [
        "storage",
        "00bed630",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb778",
      "READ",
      [
        "storage",
        "00bed648",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb65c.md#insn-004cb6cc) · [`004cb6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb65c.md#insn-004cb6f0)
- 新版 [`004cb6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb65c.md#insn-004cb6cc) · [`004cb6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb65c.md#insn-004cb6f0)

~~~diff
- 004cb6cc ["COPY", "tmp:0:8", ["const:570:8"]]
- 004cb6cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004cb6cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004cb6cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004cb6cc ["COPY", "tmp:0:8", ["const:620:8"]]
+ 004cb6cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004cb6cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004cb6cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004cb6cc bytes 4ac11591
+ 004cb6cc bytes 4a811891
- 004cb6f0 ["COPY", "tmp:0:8", ["const:570:8"]]
- 004cb6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cb6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cb6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cb6f0 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 004cb6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cb6f0 bytes 08c11591
+ 004cb6f0 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8b1d1d121a63d311fef642ca406e4e"></a>

### [`004cb868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb868.md) → [`004cb868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb868.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00522/00522a9c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc710.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb898",
      "incomplete_value": false,
      "site": "004cb8a0",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb898",
      "incomplete_value": false,
      "site": "004cb8a0",
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
            "const:4f0:8"
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
      "004cb8a0",
      "DATA",
      [
        "storage",
        "00bed4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb8e0",
      "READ",
      [
        "storage",
        "00bed510",
        null,
        "pointer"
      ]
    ],
    [
      "004cb8e0",
      "READ",
      [
        "storage",
        "00bed518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004cb8a0",
      "DATA",
      [
        "storage",
        "00bed5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb8e0",
      "READ",
      [
        "storage",
        "00bed5c0",
        null,
        "pointer"
      ]
    ],
    [
      "004cb8e0",
      "READ",
      [
        "storage",
        "00bed5c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb868.md#insn-004cb898)
- 新版 [`004cb898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb868.md#insn-004cb898)

~~~diff
- 004cb898 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 004cb898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cb898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cb898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cb898 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 004cb898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cb898 bytes 08c11391
+ 004cb898 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e9ef9fab599ddfa503f120a35f5f0cd"></a>

### [`004cb9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb9bc.md) → [`004cb9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb9bc.md) _ZNK5Botan12PK_Decryptor7decryptEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc2a0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdc350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc350.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cba7c",
      "incomplete_value": true,
      "site": "004cba88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cba7c",
      "incomplete_value": true,
      "site": "004cba88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cba7c",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004cba7c",
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
      "004cba7c",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004cba7c",
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

- 旧版 [`004cba7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cb9bc.md#insn-004cba7c)
- 新版 [`004cba7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb9bc.md#insn-004cba7c)

~~~diff
- 004cba7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004cba7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cba7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004cba7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cba7c bytes 213047f9
+ 004cba7c bytes 218847f9
~~~


<a id="compare-17a42be4c1999e5f48bc18a4d0f291da"></a>

### [`004cbae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbae4.md) → [`004cbae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbae4.md) _ZNK5Botan12PK_Decryptor17decrypt_or_randomEPKhmmRNS_21RandomNumberGeneratorES2_S2_m

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc730.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d614.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 1件 [`00bdc7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7e0.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cbca0",
      "incomplete_value": true,
      "site": "004cbca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cbca0",
      "incomplete_value": true,
      "site": "004cbca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cbd8c",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:46a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbd8c",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:3dd:8"
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
    "new": {
      "definition_site": "004cbd94",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:1ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbd94",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:280:8"
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
      "004cbc90",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cbd8c",
      "PARAM",
      [
        "storage",
        "0029e3dd",
        null,
        "string"
      ]
    ],
    [
      "004cbd94",
      "PARAM",
      [
        "storage",
        "002a8280",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cbc90",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cbd8c",
      "PARAM",
      [
        "storage",
        "0029e46a",
        null,
        "string"
      ]
    ],
    [
      "004cbd94",
      "PARAM",
      [
        "storage",
        "002a81ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cbc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbae4.md#insn-004cbc90) · [`004cbd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbae4.md#insn-004cbd8c) · [`004cbd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbae4.md#insn-004cbd94)
- 新版 [`004cbc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbae4.md#insn-004cbc90) · [`004cbd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbae4.md#insn-004cbd8c) · [`004cbd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbae4.md#insn-004cbd94)

~~~diff
- 004cbc90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004cbc90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cbc90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004cbc90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cbc90 bytes 293d43f9
+ 004cbc90 bytes 299543f9
- 004cbd8c ["COPY", "tmp:0:8", ["const:3dd:8"]]
- 004cbd8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004cbd8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004cbd8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004cbd8c ["COPY", "tmp:0:8", ["const:46a:8"]]
+ 004cbd8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004cbd8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004cbd8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004cbd8c bytes 00740f91
+ 004cbd8c bytes 00a81191
- 004cbd94 ["COPY", "tmp:0:8", ["const:280:8"]]
- 004cbd94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cbd94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cbd94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cbd94 ["COPY", "tmp:0:8", ["const:1ec:8"]]
+ 004cbd94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cbd94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cbd94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cbd94 bytes 21000a91
+ 004cbd94 bytes 21b00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618d767f9b7a34c4b0748dbe60fc3a66"></a>

### [`004cbe08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbe08.md) → [`004cbe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbe08.md) _ZN5Botan16PK_Encryptor_EMEC1ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc280.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc330.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbe40",
      "incomplete_value": true,
      "site": "004cbe40",
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
      "definition_site": "004cbe40",
      "incomplete_value": true,
      "site": "004cbe40",
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
      "definition_site": "004cbef0",
      "incomplete_value": false,
      "site": "004cbefc",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbef0",
      "incomplete_value": false,
      "site": "004cbefc",
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
            "const:972:8"
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
    "new": {
      "definition_site": "004cbf1c",
      "incomplete_value": false,
      "site": "004cbf24",
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
            "const:a02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbf1c",
      "incomplete_value": false,
      "site": "004cbf24",
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
            "const:a0b:8"
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
      "004cbe30",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ],
    [
      "004cbe40",
      "DATA",
      [
        "storage",
        "00be9eb8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004cbef0",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cbe30",
      "READ",
      [
        "storage",
        "00c1b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "004cbe40",
      "DATA",
      [
        "storage",
        "00be9f68",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004cbef0",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cbe30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbe08.md#insn-004cbe30) · [`004cbef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbe08.md#insn-004cbef0) · [`004cbf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cb/004cbe08.md#insn-004cbf1c)
- 新版 [`004cbe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbe08.md#insn-004cbe30) · [`004cbef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbe08.md#insn-004cbef0) · [`004cbf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cbe08.md#insn-004cbf1c)

~~~diff
- 004cbe30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:118:8"]]
- 004cbe30 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cbe30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1c8:8"]]
+ 004cbe30 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cbe30 bytes 298d40f9
+ 004cbe30 bytes 29e540f9
- 004cbef0 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cbef0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cbef0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cbef0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cbef0 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cbef0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cbef0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cbef0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cbef0 bytes 42c82591
+ 004cbef0 bytes 42782391
- 004cbf1c ["COPY", "tmp:0:8", ["const:a0b:8"]]
- 004cbf1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cbf1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cbf1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cbf1c ["COPY", "tmp:0:8", ["const:a02:8"]]
+ 004cbf1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cbf1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cbf1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cbf1c bytes 212c2891
+ 004cbf1c bytes 21082891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f2a6da8a3e093322b860fb383da25ce"></a>

### [`004cc1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc1c4.md) → [`004cc1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc1c4.md) _ZN5Botan16PK_Decryptor_EMEC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc290.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc340.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cc1fc",
      "incomplete_value": true,
      "site": "004cc1fc",
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
      "definition_site": "004cc1fc",
      "incomplete_value": true,
      "site": "004cc1fc",
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
      "definition_site": "004cc2b4",
      "incomplete_value": false,
      "site": "004cc2c0",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc2b4",
      "incomplete_value": false,
      "site": "004cc2c0",
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
            "const:972:8"
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
    "new": {
      "definition_site": "004cc2e0",
      "incomplete_value": false,
      "site": "004cc2e8",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc2e0",
      "incomplete_value": false,
      "site": "004cc2e8",
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
            "const:37f:8"
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
      "004cc1ec",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004cc1fc",
      "DATA",
      [
        "storage",
        "00be9ee8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004cc2b4",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cc1ec",
      "READ",
      [
        "storage",
        "00c1b1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004cc1fc",
      "DATA",
      [
        "storage",
        "00be9f98",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004cc2b4",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc1c4.md#insn-004cc1ec) · [`004cc2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc1c4.md#insn-004cc2b4) · [`004cc2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc1c4.md#insn-004cc2e0)
- 新版 [`004cc1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc1c4.md#insn-004cc1ec) · [`004cc2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc1c4.md#insn-004cc2b4) · [`004cc2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc1c4.md#insn-004cc2e0)

~~~diff
- 004cc1ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:120:8"]]
- 004cc1ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cc1ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d0:8"]]
+ 004cc1ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cc1ec bytes 299140f9
+ 004cc1ec bytes 29e940f9
- 004cc2b4 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cc2b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cc2b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cc2b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cc2b4 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cc2b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc2b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc2b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cc2b4 bytes 42c82591
+ 004cc2b4 bytes 42782391
- 004cc2e0 ["COPY", "tmp:0:8", ["const:37f:8"]]
- 004cc2e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cc2e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cc2e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cc2e0 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 004cc2e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc2e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc2e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cc2e0 bytes 21fc0d91
+ 004cc2e0 bytes 21e00d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba8ede8609950218d2b5f8ac7ebb23a"></a>

### [`004cc45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc45c.md) → [`004cc45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc45c.md) _ZN5Botan16PK_KEM_EncryptorC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc538",
      "incomplete_value": false,
      "site": "004cc544",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc538",
      "incomplete_value": false,
      "site": "004cc544",
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
            "const:972:8"
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
    "new": {
      "definition_site": "004cc564",
      "incomplete_value": false,
      "site": "004cc56c",
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
            "const:357:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc564",
      "incomplete_value": false,
      "site": "004cc56c",
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
            "const:35e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc5b4",
      "incomplete_value": true,
      "site": "004cc5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cc5b4",
      "incomplete_value": true,
      "site": "004cc5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cc538",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ],
    [
      "004cc564",
      "PARAM",
      [
        "storage",
        "002a335e",
        null,
        "string"
      ]
    ],
    [
      "004cc5b4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cc538",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004cc564",
      "PARAM",
      [
        "storage",
        "002a3357",
        null,
        "string"
      ]
    ],
    [
      "004cc5b4",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc45c.md#insn-004cc538) · [`004cc564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc45c.md#insn-004cc564) · [`004cc5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc45c.md#insn-004cc5b4)
- 新版 [`004cc538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc45c.md#insn-004cc538) · [`004cc564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc45c.md#insn-004cc564) · [`004cc5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc45c.md#insn-004cc5b4)

~~~diff
- 004cc538 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cc538 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cc538 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cc538 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cc538 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cc538 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc538 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc538 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cc538 bytes 42c82591
+ 004cc538 bytes 42782391
- 004cc564 ["COPY", "tmp:0:8", ["const:35e:8"]]
- 004cc564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cc564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cc564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cc564 ["COPY", "tmp:0:8", ["const:357:8"]]
+ 004cc564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cc564 bytes 21780d91
+ 004cc564 bytes 215c0d91
- 004cc5b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cc5b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cc5b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cc5b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cc5b4 bytes 212047f9
+ 004cc5b4 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cff04d0b81f08304c06c258b6524ab"></a>

### [`004cc6bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc6bc.md) → [`004cc6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc6bc.md) _ZN5Botan16PK_KEM_DecryptorC2ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc7a0",
      "incomplete_value": false,
      "site": "004cc7ac",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc7a0",
      "incomplete_value": false,
      "site": "004cc7ac",
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
            "const:972:8"
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
    "new": {
      "definition_site": "004cc7cc",
      "incomplete_value": false,
      "site": "004cc7d4",
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
            "const:516:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc7cc",
      "incomplete_value": false,
      "site": "004cc7d4",
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
            "const:5aa:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc81c",
      "incomplete_value": true,
      "site": "004cc828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cc81c",
      "incomplete_value": true,
      "site": "004cc828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cc7a0",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ],
    [
      "004cc7cc",
      "PARAM",
      [
        "storage",
        "002a95aa",
        null,
        "string"
      ]
    ],
    [
      "004cc81c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cc7a0",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004cc7cc",
      "PARAM",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "004cc81c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc6bc.md#insn-004cc7a0) · [`004cc7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc6bc.md#insn-004cc7cc) · [`004cc81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc6bc.md#insn-004cc81c)
- 新版 [`004cc7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc6bc.md#insn-004cc7a0) · [`004cc7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc6bc.md#insn-004cc7cc) · [`004cc81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc6bc.md#insn-004cc81c)

~~~diff
- 004cc7a0 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cc7a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cc7a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cc7a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cc7a0 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cc7a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc7a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cc7a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cc7a0 bytes 42c82591
+ 004cc7a0 bytes 42782391
- 004cc7cc ["COPY", "tmp:0:8", ["const:5aa:8"]]
- 004cc7cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cc7cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cc7cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cc7cc ["COPY", "tmp:0:8", ["const:516:8"]]
+ 004cc7cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc7cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cc7cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cc7cc bytes 21a81691
+ 004cc7cc bytes 21581491
- 004cc81c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cc81c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cc81c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cc81c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cc81c bytes 212047f9
+ 004cc81c bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be0526a6a0c1144d33b1b29dbab5279c"></a>

### [`004cc924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc924.md) → [`004cc924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc924.md) _ZN5Botan16PK_Key_AgreementC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cca08",
      "incomplete_value": false,
      "site": "004cca14",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cca08",
      "incomplete_value": false,
      "site": "004cca14",
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
            "const:972:8"
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
    "new": {
      "definition_site": "004cca84",
      "incomplete_value": true,
      "site": "004cca90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cca84",
      "incomplete_value": true,
      "site": "004cca90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cca08",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ],
    [
      "004cca84",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004cca84",
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
      "004cca08",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004cca84",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004cca84",
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

- 旧版 [`004cca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc924.md#insn-004cca08) · [`004cca84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004cc924.md#insn-004cca84)
- 新版 [`004cca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc924.md#insn-004cca08) · [`004cca84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc924.md#insn-004cca84)

~~~diff
- 004cca08 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cca08 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cca08 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cca08 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cca08 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cca08 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cca08 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cca08 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cca08 bytes 42c82591
+ 004cca08 bytes 42782391
- 004cca84 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cca84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cca84 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cca84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cca84 bytes 212047f9
+ 004cca84 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d1ebc5867a00fb3748ec7260fbd23a"></a>

### [`004ccca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccca0.md) → [`004ccca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccca0.md) _ZN5Botan9PK_SignerC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc2e0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc390.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ccdc4",
      "incomplete_value": false,
      "site": "004ccdd0",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ccdc4",
      "incomplete_value": false,
      "site": "004ccdd0",
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
            "const:972:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ccdf0",
      "incomplete_value": false,
      "site": "004ccdf8",
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
            "const:a1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ccdf0",
      "incomplete_value": false,
      "site": "004ccdf8",
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
            "const:a28:8"
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
      "definition_site": "004cce40",
      "incomplete_value": true,
      "site": "004cce4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cce40",
      "incomplete_value": true,
      "site": "004cce4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ccdc4",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ],
    [
      "004ccdf0",
      "PARAM",
      [
        "storage",
        "002ada28",
        null,
        "string"
      ]
    ],
    [
      "004cce40",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ccdc4",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004ccdf0",
      "PARAM",
      [
        "storage",
        "002ada1f",
        null,
        "string"
      ]
    ],
    [
      "004cce40",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ccdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccca0.md#insn-004ccdc4) · [`004ccdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccca0.md#insn-004ccdf0) · [`004cce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccca0.md#insn-004cce40)
- 新版 [`004ccdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccca0.md#insn-004ccdc4) · [`004ccdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccca0.md#insn-004ccdf0) · [`004cce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccca0.md#insn-004cce40)

~~~diff
- 004ccdc4 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004ccdc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004ccdc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004ccdc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004ccdc4 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004ccdc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004ccdc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004ccdc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004ccdc4 bytes 42c82591
+ 004ccdc4 bytes 42782391
- 004ccdf0 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 004ccdf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ccdf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ccdf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ccdf0 ["COPY", "tmp:0:8", ["const:a1f:8"]]
+ 004ccdf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ccdf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ccdf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ccdf0 bytes 21a02891
+ 004ccdf0 bytes 217c2891
- 004cce40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cce40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cce40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cce40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cce40 bytes 212047f9
+ 004cce40 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7cc75cdc3df9f012fae2748ca500a4f"></a>

### [`004ccf4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccf4c.md) → [`004ccf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf4c.md) _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc300.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md)
- 新版 呼出元 1件 [`00bdc3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc3b0.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cd014",
      "incomplete_value": true,
      "site": "004cd014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cd014",
      "incomplete_value": true,
      "site": "004cd014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cd1f0",
      "incomplete_value": true,
      "site": "004cd1f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cd1f0",
      "incomplete_value": true,
      "site": "004cd1f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cd254",
      "incomplete_value": true,
      "site": "004cd254",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cd254",
      "incomplete_value": true,
      "site": "004cd254",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cd004",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cd1e0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cd244",
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
      "004cd004",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cd1e0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cd244",
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

- 旧版 [`004cd004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccf4c.md#insn-004cd004) · [`004cd1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccf4c.md#insn-004cd1e0) · [`004cd244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccf4c.md#insn-004cd244)
- 新版 [`004cd004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf4c.md#insn-004cd004) · [`004cd1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf4c.md#insn-004cd1e0) · [`004cd244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf4c.md#insn-004cd244)

~~~diff
- 004cd004 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004cd004 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd004 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004cd004 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd004 bytes 293d43f9
+ 004cd004 bytes 299543f9
- 004cd1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004cd1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004cd1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd1e0 bytes 293d43f9
+ 004cd1e0 bytes 299543f9
- 004cd244 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004cd244 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd244 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004cd244 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd244 bytes a93e43f9
+ 004cd244 bytes a99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b342ffe8a09e394bfe212847f7e693f"></a>

### [`004cd48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd48c.md) → [`004cd48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd48c.md) _ZN5Botan11PK_VerifierC2ERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_16Signature_FormatESC_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc2f0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc3a0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd594",
      "incomplete_value": false,
      "site": "004cd5a0",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd594",
      "incomplete_value": false,
      "site": "004cd5a0",
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
            "const:972:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd5c0",
      "incomplete_value": false,
      "site": "004cd5c8",
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
            "const:af3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd5c0",
      "incomplete_value": false,
      "site": "004cd5c8",
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
            "const:a66:8"
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
      "definition_site": "004cd610",
      "incomplete_value": true,
      "site": "004cd61c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cd610",
      "incomplete_value": true,
      "site": "004cd61c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cd594",
      "PARAM",
      [
        "storage",
        "002ae972",
        null,
        "string"
      ]
    ],
    [
      "004cd5c0",
      "PARAM",
      [
        "storage",
        "00291a66",
        null,
        "string"
      ]
    ],
    [
      "004cd610",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cd594",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004cd5c0",
      "PARAM",
      [
        "storage",
        "00291af3",
        null,
        "string"
      ]
    ],
    [
      "004cd610",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd48c.md#insn-004cd594) · [`004cd5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd48c.md#insn-004cd5c0) · [`004cd610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd48c.md#insn-004cd610)
- 新版 [`004cd594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd48c.md#insn-004cd594) · [`004cd5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd48c.md#insn-004cd5c0) · [`004cd610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd48c.md#insn-004cd610)

~~~diff
- 004cd594 ["COPY", "tmp:0:8", ["const:972:8"]]
- 004cd594 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004cd594 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004cd594 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004cd594 ["COPY", "tmp:0:8", ["const:8de:8"]]
+ 004cd594 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004cd594 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004cd594 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004cd594 bytes 42c82591
+ 004cd594 bytes 42782391
- 004cd5c0 ["COPY", "tmp:0:8", ["const:a66:8"]]
- 004cd5c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cd5c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cd5c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cd5c0 ["COPY", "tmp:0:8", ["const:af3:8"]]
+ 004cd5c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cd5c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cd5c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cd5c0 bytes 21982991
+ 004cd5c0 bytes 21cc2b91
- 004cd610 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cd610 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd610 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cd610 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd610 bytes 212047f9
+ 004cd610 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-188f718650ee5d14ebdf9012074691de"></a>

### [`004cd70c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd70c.md) → [`004cd70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd70c.md) _ZN5Botan11PK_Verifier16set_input_formatENS_16Signature_FormatE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd7b4",
      "incomplete_value": true,
      "site": "004cd7c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cd7b4",
      "incomplete_value": true,
      "site": "004cd7c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004cd7b4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004cd7b4",
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
      "004cd7b4",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004cd7b4",
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

- 旧版 [`004cd7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd70c.md#insn-004cd7b4)
- 新版 [`004cd7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd70c.md#insn-004cd7b4)

~~~diff
- 004cd7b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004cd7b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd7b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004cd7b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd7b4 bytes 212047f9
+ 004cd7b4 bytes 217847f9
~~~


<a id="compare-9b8447618b673173c2b2444406e57819"></a>

### [`004cd86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd86c.md) → [`004cd86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd86c.md) _ZN5Botan11PK_Verifier15check_signatureEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc310.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00490/00490630.md) [`004cdca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cdca8.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bdc3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc3c0.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`004cdca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cdca8.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cd990",
      "incomplete_value": true,
      "site": "004cd990",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cd990",
      "incomplete_value": true,
      "site": "004cd990",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cd9bc",
      "incomplete_value": true,
      "site": "004cd9bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cd9bc",
      "incomplete_value": true,
      "site": "004cd9bc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cda24",
      "incomplete_value": true,
      "site": "004cda24",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cda24",
      "incomplete_value": true,
      "site": "004cda24",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cd980",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cd9ac",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cda14",
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
      "004cd980",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cd9ac",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cda14",
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

- 旧版 [`004cd980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd86c.md#insn-004cd980) · [`004cd9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd86c.md#insn-004cd9ac) · [`004cda14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cd86c.md#insn-004cda14)
- 新版 [`004cd980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd86c.md#insn-004cd980) · [`004cd9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd86c.md#insn-004cd9ac) · [`004cda14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd86c.md#insn-004cda14)

~~~diff
- 004cd980 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004cd980 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd980 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004cd980 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd980 bytes c93e43f9
+ 004cd980 bytes c99643f9
- 004cd9ac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004cd9ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd9ac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004cd9ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd9ac bytes c93e43f9
+ 004cd9ac bytes c99643f9
- 004cda14 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004cda14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cda14 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004cda14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cda14 bytes c93e43f9
+ 004cda14 bytes c99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddeef81908f66e1fc7323584bb8a16a1"></a>

### [`004cdf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cdf20.md) → [`004cdf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cdf20.md) _ZN5Botan4X50910PEM_encodeERKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdc540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc540.md) [`00bdc680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc680.md)
- 新版 呼出元 1件 [`00bdc820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc820.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) [`00bdc730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cdf70",
      "incomplete_value": true,
      "site": "004cdf70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cdf70",
      "incomplete_value": true,
      "site": "004cdf70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:97c:8"
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
      "004cdf5c",
      "READ",
      [
        "storage",
        "002ae97c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cdf5c",
      "READ",
      [
        "storage",
        "002ae8e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cdf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cdf20.md#insn-004cdf50)
- 新版 [`004cdf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cdf20.md#insn-004cdf50)

~~~diff
- 004cdf50 ["COPY", "tmp:0:8", ["const:97c:8"]]
- 004cdf50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004cdf50 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 004cdf50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004cdf50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004cdf50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 bytes 29f12591
+ 004cdf50 bytes 29a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d0092144c2468d83d805d0a73d37e4"></a>

### [`004ce004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md) → [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.39% / 新版 93.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件, `store_value` 2件

アドレスに依存する影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ce038",
      "incomplete_value": true,
      "site": "004ce038",
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
      "definition_site": "004ce038",
      "incomplete_value": true,
      "site": "004ce038",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ce0c4",
      "incomplete_value": true,
      "site": "004ce0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ce0c4",
      "incomplete_value": true,
      "site": "004ce0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:97c:8"
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
      "definition_site": "004ce0f0",
      "incomplete_value": true,
      "site": "004ce0f0",
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
      "definition_site": "004ce0f0",
      "incomplete_value": true,
      "site": "004ce0f0",
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
      "004ce028",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004ce038",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ce0b4",
      "READ",
      [
        "storage",
        "002ae97c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ce028",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004ce038",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ce0b4",
      "READ",
      [
        "storage",
        "002ae8e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ce028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md#insn-004ce028) · [`004ce0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md#insn-004ce0ac) · [`004ce0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md#insn-004ce0e0)
- 新版 [`004ce028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md#insn-004ce028) · [`004ce0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md#insn-004ce0ac) · [`004ce0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md#insn-004ce0e0)

~~~diff
- 004ce028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 004ce028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
+ 004ce028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce028 bytes 082547f9
+ 004ce028 bytes 087d47f9
- 004ce0ac ["COPY", "tmp:0:8", ["const:97c:8"]]
- 004ce0ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ce0ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ce0ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ce0ac ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 004ce0ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ce0ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ce0ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ce0ac bytes 29f12591
+ 004ce0ac bytes 29a12391
- 004ce0e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 004ce0e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce0e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004ce0e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce0e0 bytes 087947f9
+ 004ce0e0 bytes 08d147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c71a57797922f7d724b46583bdc21d1"></a>

### [`004ce6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce6fc.md) → [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7a0.md) · 呼出先 5件 [`00513e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/00513e2c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdc780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00bdc850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md) · 呼出先 5件 [`00513e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "004ce72c",
      "incomplete_value": true,
      "site": "004ce72c",
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
      "definition_site": "004ce72c",
      "incomplete_value": true,
      "site": "004ce72c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ce778",
      "incomplete_value": true,
      "site": "004ce778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004ce778",
      "incomplete_value": true,
      "site": "004ce778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ce718",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004ce72c",
      "DATA",
      [
        "storage",
        "00bea2c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ce768",
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
      "004ce718",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004ce72c",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ce768",
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

- 旧版 [`004ce718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce6fc.md#insn-004ce718) · [`004ce768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce6fc.md#insn-004ce768)
- 新版 [`004ce718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md#insn-004ce718) · [`004ce768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md#insn-004ce768)

~~~diff
- 004ce718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 004ce718 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004ce718 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce718 bytes 087947f9
+ 004ce718 bytes 08d147f9
- 004ce768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004ce768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004ce768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce768 bytes 293d43f9
+ 004ce768 bytes 299543f9
~~~


<a id="compare-0d0ecb36a896f629ebe2320a0de5997d"></a>

### [`004ce7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce7d8.md) → [`004ce7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md) _ZN5Botan4X5098copy_keyERKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdc570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md) [`00bdc770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc620.md) [`00bdc820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc820.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ce84c",
      "incomplete_value": true,
      "site": "004ce84c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004ce84c",
      "incomplete_value": true,
      "site": "004ce84c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ce83c",
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
      "004ce83c",
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

- 旧版 [`004ce83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce7d8.md#insn-004ce83c)
- 新版 [`004ce83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md#insn-004ce83c)

~~~diff
- 004ce83c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004ce83c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce83c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004ce83c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce83c bytes 293d43f9
+ 004ce83c bytes 299543f9
~~~


<a id="compare-4cc0b4e55de319592e6e7406ca7c4cc7"></a>

### [`004cec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004cec60.md) → [`004cec60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004cec60.md) _ZN5Botan21RandomNumberGenerator8make_rngEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a4f:8"
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
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cecb8",
      "incomplete_value": true,
      "site": "004cecc0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004cecb8",
      "incomplete_value": true,
      "site": "004cecc0",
      "value": [
        "LOAD",
        "16",
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
      "004ceca0",
      "READ",
      [
        "storage",
        "002ada4f",
        null,
        "string"
      ]
    ],
    [
      "004ceca0",
      "READ",
      [
        "storage",
        "002ada5f",
        null,
        "string"
      ]
    ],
    [
      "004cecb8",
      "READ",
      [
        "storage",
        "002ada6f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ceca0",
      "READ",
      [
        "storage",
        "002ada46",
        null,
        "string"
      ]
    ],
    [
      "004ceca0",
      "READ",
      [
        "storage",
        "002ada56",
        null,
        "string"
      ]
    ],
    [
      "004cecb8",
      "READ",
      [
        "storage",
        "002ada66",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cec98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004cec60.md#insn-004cec98) · [`004cec9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004cec60.md#insn-004cec9c)
- 新版 [`004cec98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004cec60.md#insn-004cec98) · [`004cec9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004cec60.md#insn-004cec9c)

~~~diff
- 004cec98 ["COPY", "tmp:0:8", ["const:a4f:8"]]
- 004cec98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cec98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cec98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cec98 ["COPY", "tmp:0:8", ["const:a46:8"]]
+ 004cec98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cec98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cec98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cec98 bytes 083d2991
+ 004cec98 bytes 08192991
- 004cec9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004cec9c bytes 09effff0
+ 004cec9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004cec9c bytes 09effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef7241a65f4a83bd3914c0cfc78ce27"></a>

### [`004ced48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ced48.md) → [`004ced48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ced48.md) _ZN5Botan14Serialized_RNGC1Ev

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.36% / 新版 77.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ced7c",
      "incomplete_value": true,
      "site": "004ced84",
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
      "definition_site": "004ced7c",
      "incomplete_value": true,
      "site": "004ced84",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cedb4",
      "incomplete_value": true,
      "site": "004cedc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004cedb4",
      "incomplete_value": true,
      "site": "004cedc8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cedb4",
      "incomplete_value": true,
      "site": "004cedc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004cedb4",
      "incomplete_value": true,
      "site": "004cedc8",
      "value": [
        "LOAD",
        "16",
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
      "004ced6c",
      "READ",
      [
        "storage",
        "00c1b128",
        null,
        "pointer"
      ]
    ],
    [
      "004ced84",
      "DATA",
      [
        "storage",
        "00be9f10",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004cedb4",
      "READ",
      [
        "storage",
        "002aa619",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ced6c",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "004ced84",
      "DATA",
      [
        "storage",
        "00be9fc0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004cedb4",
      "READ",
      [
        "storage",
        "002aa61f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ced6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ced48.md#insn-004ced6c) · [`004cedac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ced48.md#insn-004cedac) · [`004cedb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ced48.md#insn-004cedb0)
- 新版 [`004ced6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ced48.md#insn-004ced6c) · [`004cedac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ced48.md#insn-004cedac)

~~~diff
- 004ced6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:128:8"]]
- 004ced6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ced6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1d8:8"]]
+ 004ced6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ced6c bytes 089540f9
+ 004ced6c bytes 08ed40f9
- 004cedac ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004cedac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cedac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cedac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cedac ["COPY", "tmp:0:8", ["const:5ff:8"]]
+ 004cedac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cedac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cedac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cedac bytes 08e51791
+ 004cedac bytes 08fd1791
- 004cedb0 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004cedb0 bytes 09effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d066ae3a4f19b20d3a54eb26f9701d"></a>

### [`004cf328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf328.md) → [`004cf328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf328.md) _ZN5Botan13RSA_PublicKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md) [`00bdb930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb930.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cf40c",
      "incomplete_value": true,
      "site": "004cf40c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf40c",
      "incomplete_value": true,
      "site": "004cf40c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cf450",
      "incomplete_value": true,
      "site": "004cf450",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf450",
      "incomplete_value": true,
      "site": "004cf450",
      "value": [
        "LOAD",
        "8",
        [
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
      "004cf3fc",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cf440",
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
      "004cf3fc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cf440",
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

- 旧版 [`004cf3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf328.md#insn-004cf3fc) · [`004cf440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf328.md#insn-004cf440)
- 新版 [`004cf3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf328.md#insn-004cf3fc) · [`004cf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf328.md#insn-004cf440)

~~~diff
- 004cf3fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 004cf3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf3fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 004cf3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf3fc bytes 893e43f9
+ 004cf3fc bytes 899643f9
- 004cf440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 004cf440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 004cf440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf440 bytes 893e43f9
+ 004cf440 bytes 899643f9
~~~


<a id="compare-dcc2eede0ecc7cb8d6f64e8f94531bc9"></a>

### [`004cf634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf634.md) → [`004cf634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf634.md) _ZNK5Botan14RSA_PrivateKey16private_key_bitsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb760.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cf6c0",
      "incomplete_value": true,
      "site": "004cf6c0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cf6c0",
      "incomplete_value": true,
      "site": "004cf6c0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cf7e0",
      "incomplete_value": true,
      "site": "004cf7e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cf7e0",
      "incomplete_value": true,
      "site": "004cf7e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004cf6b0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cf7d0",
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
      "004cf6b0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cf7d0",
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

- 旧版 [`004cf6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf634.md#insn-004cf6b0) · [`004cf7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf634.md#insn-004cf7d0)
- 新版 [`004cf6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf634.md#insn-004cf6b0) · [`004cf7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf634.md#insn-004cf7d0)

~~~diff
- 004cf6b0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004cf6b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf6b0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004cf6b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf6b0 bytes e93e43f9
+ 004cf6b0 bytes e99643f9
- 004cf7d0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004cf7d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf7d0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004cf7d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf7d0 bytes e93e43f9
+ 004cf7d0 bytes e99643f9
~~~


<a id="compare-8fca6b001a51f41d13e78683c849c718"></a>

### [`004cf854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf854.md) → [`004cf854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf854.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.36% / 新版 95.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:49e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfa94",
      "incomplete_value": true,
      "site": "004cfa94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cfa94",
      "incomplete_value": true,
      "site": "004cfa94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cf98c",
      "READ",
      [
        "storage",
        "002a44a5",
        null,
        "string"
      ]
    ],
    [
      "004cf98c",
      "READ",
      [
        "storage",
        "002a44b5",
        null,
        "string"
      ]
    ],
    [
      "004cfa84",
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
      "004cf98c",
      "READ",
      [
        "storage",
        "002a449e",
        null,
        "string"
      ]
    ],
    [
      "004cf98c",
      "READ",
      [
        "storage",
        "002a44ae",
        null,
        "string"
      ]
    ],
    [
      "004cfa84",
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

- 旧版 [`004cf984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf854.md#insn-004cf984) · [`004cf988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf854.md#insn-004cf988)
- 新版 [`004cf984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf854.md#insn-004cf984) · [`004cf988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf854.md#insn-004cf988)

~~~diff
- 004cf984 ["COPY", "tmp:0:8", ["const:4a5:8"]]
- 004cf984 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004cf984 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004cf984 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004cf984 ["COPY", "tmp:0:8", ["const:49e:8"]]
+ 004cf984 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004cf984 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004cf984 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004cf984 bytes 4a951291
+ 004cf984 bytes 4a791291
- 004cf988 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 004cf988 bytes 08efffd0
+ 004cf988 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 004cf988 bytes 08efffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea73ba34b8d32f24d282a1bd95a2899a"></a>

### [`004cfc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfc08.md) → [`004cfc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfc08.md) FUN_004cfc08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfc54",
      "incomplete_value": true,
      "site": "004cfc54",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cfc54",
      "incomplete_value": true,
      "site": "004cfc54",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfc80",
      "incomplete_value": true,
      "site": "004cfc80",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cfc80",
      "incomplete_value": true,
      "site": "004cfc80",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cfc44",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cfc70",
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
      "004cfc44",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cfc70",
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

- 旧版 [`004cfc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfc08.md#insn-004cfc44) · [`004cfc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfc08.md#insn-004cfc70)
- 新版 [`004cfc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfc08.md#insn-004cfc44) · [`004cfc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfc08.md#insn-004cfc70)

~~~diff
- 004cfc44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004cfc44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cfc44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004cfc44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cfc44 bytes a93e43f9
+ 004cfc44 bytes a99643f9
- 004cfc70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004cfc70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cfc70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004cfc70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cfc70 bytes a93e43f9
+ 004cfc70 bytes a99643f9
~~~


<a id="compare-32bc2107e7c179ce9afd18e52a79969b"></a>

### [`004cfcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfcb0.md) → [`004cfcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfcb0.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00520/00520804.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb9d0.md) [`00bdbbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbbd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfe68",
      "incomplete_value": true,
      "site": "004cfe68",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cfe68",
      "incomplete_value": true,
      "site": "004cfe68",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfed8",
      "incomplete_value": true,
      "site": "004cfed8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cfed8",
      "incomplete_value": true,
      "site": "004cfed8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cff50",
      "incomplete_value": true,
      "site": "004cff50",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004cff50",
      "incomplete_value": true,
      "site": "004cff50",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cfe58",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cfec8",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004cff40",
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
      "004cfe58",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cfec8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004cff40",
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

- 旧版 [`004cfe58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfcb0.md#insn-004cfe58) · [`004cfec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfcb0.md#insn-004cfec8) · [`004cff40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfcb0.md#insn-004cff40)
- 新版 [`004cfe58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfcb0.md#insn-004cfe58) · [`004cfec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfcb0.md#insn-004cfec8) · [`004cff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfcb0.md#insn-004cff40)

~~~diff
- 004cfe58 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
- 004cfe58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cfe58 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
+ 004cfe58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cfe58 bytes 893f43f9
+ 004cfe58 bytes 899743f9
- 004cfec8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
- 004cfec8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cfec8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
+ 004cfec8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cfec8 bytes 893f43f9
+ 004cfec8 bytes 899743f9
- 004cff40 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:678:8"]]
- 004cff40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cff40 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
+ 004cff40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cff40 bytes 893f43f9
+ 004cff40 bytes 899743f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b499c25ea14233bc459b1af42b2d86"></a>

### [`004d04c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d04c0.md) → [`004d04c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d04c0.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00520/00520804.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb9d0.md) [`00bdbbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbbd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.73% / 新版 91.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d052c",
      "incomplete_value": true,
      "site": "004d052c",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d052c",
      "incomplete_value": true,
      "site": "004d052c",
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
            "const:1a0:8"
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
      "definition_site": "004d0524",
      "incomplete_value": true,
      "site": "004d0540",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d0524",
      "incomplete_value": true,
      "site": "004d0540",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d0644",
      "incomplete_value": true,
      "site": "004d0644",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004d0644",
      "incomplete_value": true,
      "site": "004d0644",
      "value": [
        "LOAD",
        "8",
        [
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
      "004d04f0",
      "READ",
      [
        "storage",
        "00c1b0f0",
        null,
        "pointer"
      ]
    ],
    [
      "004d052c",
      "DATA",
      [
        "storage",
        "00bea1f8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004d0540",
      "DATA",
      [
        "storage",
        "00bea0d8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004d04f0",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "004d052c",
      "DATA",
      [
        "storage",
        "00bea2a8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004d0540",
      "DATA",
      [
        "storage",
        "00bea188",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d04c0.md#insn-004d04f0) · [`004d0634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d04c0.md#insn-004d0634) · [`004d06a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d04c0.md#insn-004d06a4)
- 新版 [`004d04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d04c0.md#insn-004d04f0) · [`004d0634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d04c0.md#insn-004d0634) · [`004d06a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d04c0.md#insn-004d06a4)

~~~diff
- 004d04f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f0:8"]]
- 004d04f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d04f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1a0:8"]]
+ 004d04f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d04f0 bytes 297940f9
+ 004d04f0 bytes 29d140f9
- 004d0634 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:678:8"]]
- 004d0634 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d0634 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
+ 004d0634 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d0634 bytes 693f43f9
+ 004d0634 bytes 699743f9
- 004d06a4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:678:8"]]
- 004d06a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d06a4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
+ 004d06a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d06a4 bytes 693f43f9
+ 004d06a4 bytes 699743f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb02a0443e1bfe62607b91c76d290075"></a>

### [`004d0c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d0c9c.md) → [`004d0c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d0c9c.md) _ZN5Botan14RSA_PrivateKeyC2ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`00483974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d0e3c",
      "incomplete_value": true,
      "site": "004d0e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d0e3c",
      "incomplete_value": true,
      "site": "004d0e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d0ee0",
      "incomplete_value": true,
      "site": "004d0ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d0ee0",
      "incomplete_value": true,
      "site": "004d0ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d0fdc",
      "incomplete_value": true,
      "site": "004d0fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d0fdc",
      "incomplete_value": true,
      "site": "004d0fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d0e2c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004d0ed0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004d0fcc",
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
      "004d0e2c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004d0ed0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004d0fcc",
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

- 旧版 [`004d0e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d0c9c.md#insn-004d0e2c) · [`004d0ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d0c9c.md#insn-004d0ed0) · [`004d0fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d0c9c.md#insn-004d0fcc)
- 新版 [`004d0e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d0c9c.md#insn-004d0e2c) · [`004d0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d0c9c.md#insn-004d0ed0) · [`004d0fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d0c9c.md#insn-004d0fcc)

~~~diff
- 004d0e2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004d0e2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d0e2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004d0e2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d0e2c bytes 293d43f9
+ 004d0e2c bytes 299543f9
- 004d0ed0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004d0ed0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d0ed0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004d0ed0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d0ed0 bytes 293d43f9
+ 004d0ed0 bytes 299543f9
- 004d0fcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004d0fcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d0fcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004d0fcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d0fcc bytes 293d43f9
+ 004d0fcc bytes 299543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79a94f117e7b4cd7656eb01b0a45b743"></a>

### [`004d1904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d1/004d1904.md) → [`004d1904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d1/004d1904.md) _ZNK5Botan14RSA_PrivateKey9check_keyERNS_21RandomNumberGeneratorEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc800.md) · 呼出先 13件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb9d0.md) [`00bdbbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbbd0.md)
- 新版 呼出元 1件 [`00bdc8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc8b0.md) · 呼出先 13件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

アドレスに依存する影響 `call_target` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d1fd8",
      "incomplete_value": true,
      "site": "004d1fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d1fd8",
      "incomplete_value": true,
      "site": "004d1fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4cb:8"
              ]
            ]
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
      "definition_site": "004d1fdc",
      "incomplete_value": true,
      "site": "004d1fdc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004d1fdc",
      "incomplete_value": true,
      "site": "004d1fdc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d1a3c",
      "incomplete_value": true,
      "site": "004d1a3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "004d1a3c",
      "incomplete_value": true,
      "site": "004d1a3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d1a2c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004d1a58",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004d1a84",
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
      "004d1a2c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004d1a58",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004d1a84",
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

- 旧版 [`004d1a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d1/004d1904.md#insn-004d1a2c) · [`004d1a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d1/004d1904.md#insn-004d1a40)
- 新版 [`004d1a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d1/004d1904.md#insn-004d1a2c) · [`004d1a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d1/004d1904.md#insn-004d1a40)

~~~diff
- 004d1a2c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:678:8"]]
- 004d1a2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d1a2c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
+ 004d1a2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d1a2c bytes 093f43f9
+ 004d1a2c bytes 099743f9
- 004d1a40 ["COPY", "register:4000:8", ["register:40b0:8"]]
- 004d1a40 bytes e00316aa
+ 004d1a40 ["COPY", "register:4000:8", ["register:40b0:8"]]
+ 004d1a40 bytes e00316aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171287756f5989f7155e1c803e21374c"></a>

### [`004d21d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d21d0.md) → [`004d21d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d21d0.md) _ZNK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc810.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdc050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc050.md)
- 新版 呼出元 1件 [`00bdc8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc8c0.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d2264",
      "incomplete_value": true,
      "site": "004d226c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2264",
      "incomplete_value": true,
      "site": "004d226c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
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
      "definition_site": "004d22c8",
      "incomplete_value": true,
      "site": "004d22d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d22c8",
      "incomplete_value": true,
      "site": "004d22d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d2264",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004d2264",
      "PARAM",
      [
        "storage",
        "00be9958",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d22c8",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d2264",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004d2264",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d22c8",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d21d0.md#insn-004d2258) · [`004d2264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d21d0.md#insn-004d2264) · [`004d22c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d21d0.md#insn-004d22c8)
- 新版 [`004d2258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d21d0.md#insn-004d2258) · [`004d2264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d21d0.md#insn-004d2264) · [`004d22c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d21d0.md#insn-004d22c8)

~~~diff
- 004d2258 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004d2258 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004d2258 bytes 413a0090
+ 004d2258 bytes 413a00b0
- 004d2264 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe0:8"]]
- 004d2264 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2264 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
+ 004d2264 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2264 bytes 21f047f9
+ 004d2264 bytes 214840f9
- 004d22c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d22c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d22c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d22c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d22c8 bytes 219840f9
+ 004d22c8 bytes 21f040f9
~~~


<a id="compare-04dfe9bf6639e8975005040cd2170760"></a>

### [`004d2348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2348.md) → [`004d2348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2348.md) _ZNK5Botan13RSA_PublicKey24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloca

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc830.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdc8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc8e0.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d23cc",
      "incomplete_value": false,
      "site": "004d23cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d23cc",
      "incomplete_value": false,
      "site": "004d23cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "004d23f4",
      "incomplete_value": false,
      "site": "004d23fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d23f4",
      "incomplete_value": false,
      "site": "004d23fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "definition_site": "004d2480",
      "incomplete_value": true,
      "site": "004d248c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2480",
      "incomplete_value": true,
      "site": "004d248c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d23cc",
      "DATA",
      [
        "storage",
        "00be9e58",
        null,
        "undefined *"
      ]
    ],
    [
      "004d23fc",
      "DATA",
      [
        "storage",
        "00bece28",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2480",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d23cc",
      "DATA",
      [
        "storage",
        "00be9f08",
        null,
        "undefined *"
      ]
    ],
    [
      "004d23fc",
      "DATA",
      [
        "storage",
        "00beced8",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2480",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d23c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2348.md#insn-004d23c8) · [`004d23f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2348.md#insn-004d23f4) · [`004d2480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2348.md#insn-004d2480)
- 新版 [`004d23c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2348.md#insn-004d23c8) · [`004d23f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2348.md#insn-004d23f4) · [`004d2480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2348.md#insn-004d2480)

~~~diff
- 004d23c8 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 004d23c8 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 004d23c8 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 004d23c8 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 004d23c8 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 004d23c8 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 004d23c8 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 004d23c8 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 004d23c8 bytes 18633991
+ 004d23c8 bytes 18233c91
- 004d23f4 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 004d23f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d23f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d23f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d23f4 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 004d23f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d23f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d23f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d23f4 bytes 08a13891
+ 004d23f4 bytes 08613b91
- 004d2480 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d2480 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2480 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d2480 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2480 bytes 219840f9
+ 004d2480 bytes 21f040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff2861eb9a1a5582bc540605eb10e0a"></a>

### [`004d2528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2528.md) → [`004d2528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2528.md) _ZNK5Botan13RSA_PublicKey22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc840.md) · 呼出先 8件 [`004c8590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c8/004c8590.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdc8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc8f0.md) · 呼出先 8件 [`004c8590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8590.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.25% / 新版 96.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d25c8",
      "incomplete_value": false,
      "site": "004d25d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d25c8",
      "incomplete_value": false,
      "site": "004d25d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "definition_site": "004d2654",
      "incomplete_value": true,
      "site": "004d2660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2654",
      "incomplete_value": true,
      "site": "004d2660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d25d0",
      "DATA",
      [
        "storage",
        "00bece90",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2654",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ],
    [
      "004d2654",
      "PARAM",
      [
        "storage",
        "00bea2a0",
        "_ZTIN5Botan18Provider_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004d25d0",
      "DATA",
      [
        "storage",
        "00becf40",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2654",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004d2654",
      "PARAM",
      [
        "storage",
        "00bea350",
        "_ZTIN5Botan18Provider_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d25c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2528.md#insn-004d25c8) · [`004d2654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2528.md#insn-004d2654)
- 新版 [`004d25c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2528.md#insn-004d25c8) · [`004d2654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2528.md#insn-004d2654)

~~~diff
- 004d25c8 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 004d25c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d25c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d25c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d25c8 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 004d25c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d25c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d25c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d25c8 bytes 08413a91
+ 004d25c8 bytes 08013d91
- 004d2654 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d2654 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2654 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d2654 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2654 bytes 219840f9
+ 004d2654 bytes 21f040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1803d347256f8d48b0d48bb7fcff9d07"></a>

### [`004d26e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d26e0.md) → [`004d26e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d26e0.md) _ZNK5Botan14RSA_PrivateKey20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdc050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d2778",
      "incomplete_value": true,
      "site": "004d2780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2778",
      "incomplete_value": true,
      "site": "004d2780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
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
      "definition_site": "004d27d0",
      "incomplete_value": true,
      "site": "004d27dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d27d0",
      "incomplete_value": true,
      "site": "004d27dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d2778",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004d2778",
      "PARAM",
      [
        "storage",
        "00be9958",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d27d0",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d2778",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004d2778",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d27d0",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d276c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d26e0.md#insn-004d276c) · [`004d2778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d26e0.md#insn-004d2778) · [`004d27d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d26e0.md#insn-004d27d0)
- 新版 [`004d276c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d26e0.md#insn-004d276c) · [`004d2778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d26e0.md#insn-004d2778) · [`004d27d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d26e0.md#insn-004d27d0)

~~~diff
- 004d276c ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004d276c ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004d276c bytes 413a0090
+ 004d276c bytes 413a00b0
- 004d2778 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe0:8"]]
- 004d2778 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2778 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
+ 004d2778 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2778 bytes 21f047f9
+ 004d2778 bytes 214840f9
- 004d27d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d27d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d27d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d27d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d27d0 bytes 219840f9
+ 004d27d0 bytes 21f040f9
~~~


<a id="compare-9612ce70c12ce937406010d4ebe7d34e"></a>

### [`004d2830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2830.md) → [`004d2830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2830.md) _ZNK5Botan14RSA_PrivateKey24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00514/0051483c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d28bc",
      "incomplete_value": false,
      "site": "004d28bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d28bc",
      "incomplete_value": false,
      "site": "004d28bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d28e0",
      "incomplete_value": false,
      "site": "004d28e8",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d28e0",
      "incomplete_value": false,
      "site": "004d28e8",
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
            "const:f0:8"
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
      "definition_site": "004d2968",
      "incomplete_value": true,
      "site": "004d2974",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2968",
      "incomplete_value": true,
      "site": "004d2974",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d28bc",
      "DATA",
      [
        "storage",
        "00be9e88",
        null,
        "undefined *"
      ]
    ],
    [
      "004d28e8",
      "DATA",
      [
        "storage",
        "00bed0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2968",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d28bc",
      "DATA",
      [
        "storage",
        "00be9f38",
        null,
        "undefined *"
      ]
    ],
    [
      "004d28e8",
      "DATA",
      [
        "storage",
        "00bed1a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2968",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d28b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2830.md#insn-004d28b8) · [`004d28e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2830.md#insn-004d28e0) · [`004d2968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2830.md#insn-004d2968)
- 新版 [`004d28b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2830.md#insn-004d28b8) · [`004d28e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2830.md#insn-004d28e0) · [`004d2968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2830.md#insn-004d2968)

~~~diff
- 004d28b8 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 004d28b8 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 004d28b8 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 004d28b8 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 004d28b8 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 004d28b8 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 004d28b8 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 004d28b8 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 004d28b8 bytes 39233a91
+ 004d28b8 bytes 39e33c91
- 004d28e0 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 004d28e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d28e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d28e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d28e0 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 004d28e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d28e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d28e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d28e0 bytes 08c10391
+ 004d28e0 bytes 08810691
- 004d2968 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d2968 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2968 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d2968 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2968 bytes 219840f9
+ 004d2968 bytes 21f040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a9cefd0febad437e7ce797ef83b337c"></a>

### [`004d29f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d29f8.md) → [`004d29f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d29f8.md) _ZNK5Botan14RSA_PrivateKey19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004c824c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c8/004c824c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00514/0051483c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004c824c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c824c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d2a94",
      "incomplete_value": false,
      "site": "004d2a9c",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2a94",
      "incomplete_value": false,
      "site": "004d2a9c",
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
            "const:158:8"
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
      "definition_site": "004d2b18",
      "incomplete_value": true,
      "site": "004d2b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2b18",
      "incomplete_value": true,
      "site": "004d2b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
      "004d2a9c",
      "DATA",
      [
        "storage",
        "00bed158",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2b18",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ],
    [
      "004d2b18",
      "PARAM",
      [
        "storage",
        "00bea2a0",
        "_ZTIN5Botan18Provider_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004d2a9c",
      "DATA",
      [
        "storage",
        "00bed208",
        null,
        "undefined *"
      ]
    ],
    [
      "004d2b18",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004d2b18",
      "PARAM",
      [
        "storage",
        "00bea350",
        "_ZTIN5Botan18Provider_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d29f8.md#insn-004d2a94) · [`004d2b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d29f8.md#insn-004d2b18)
- 新版 [`004d2a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d29f8.md#insn-004d2a94) · [`004d2b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d29f8.md#insn-004d2b18)

~~~diff
- 004d2a94 ["COPY", "tmp:0:8", ["const:158:8"]]
- 004d2a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d2a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d2a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d2a94 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 004d2a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d2a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d2a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d2a94 bytes 08610591
+ 004d2a94 bytes 08210891
- 004d2b18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:130:8"]]
- 004d2b18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2b18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004d2b18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2b18 bytes 219840f9
+ 004d2b18 bytes 21f040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-362e401f99e371565ddac7f4bba57f59"></a>

### [`004d2b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2b8c.md) → [`004d2b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2b8c.md) _ZNK5Botan7SHA_16010copy_stateEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d3cc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "004d2bc0",
      "incomplete_value": true,
      "site": "004d2bc4",
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
      "definition_site": "004d2bc0",
      "incomplete_value": true,
      "site": "004d2bc4",
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
      "definition_site": "004d2bec",
      "incomplete_value": true,
      "site": "004d2bf4",
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
      "definition_site": "004d2bec",
      "incomplete_value": true,
      "site": "004d2bf4",
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
      "004d2bb4",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "004d2bc4",
      "DATA",
      [
        "storage",
        "00be9c18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d2bdc",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d2bb4",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004d2bc4",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d2bdc",
      "READ",
      [
        "storage",
        "00c1b100",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2b8c.md#insn-004d2bb4) · [`004d2bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d2/004d2b8c.md#insn-004d2bdc)
- 新版 [`004d2bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2b8c.md#insn-004d2bb4) · [`004d2bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2b8c.md#insn-004d2bdc)

~~~diff
- 004d2bb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 004d2bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2bb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 004d2bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2bb4 bytes 082540f9
+ 004d2bb4 bytes 087d40f9
- 004d2bdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
- 004d2bdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d2bdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 004d2bdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2bdc bytes 082940f9
+ 004d2bdc bytes 088140f9
~~~


<a id="compare-a36231deeaade7d29d269cff91acce91"></a>

### [`004d3aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3aec.md) → [`004d3aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3aec.md) _ZNK5Botan7SHA_22410copy_stateEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d3cc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d3b20",
      "incomplete_value": true,
      "site": "004d3b24",
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
      "definition_site": "004d3b20",
      "incomplete_value": true,
      "site": "004d3b24",
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
      "definition_site": "004d3b4c",
      "incomplete_value": true,
      "site": "004d3b54",
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
      "definition_site": "004d3b4c",
      "incomplete_value": true,
      "site": "004d3b54",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d3b14",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "004d3b24",
      "DATA",
      [
        "storage",
        "00be9c18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d3b3c",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d3b14",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004d3b24",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d3b3c",
      "READ",
      [
        "storage",
        "00c1b108",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d3b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3aec.md#insn-004d3b14) · [`004d3b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3aec.md#insn-004d3b3c)
- 新版 [`004d3b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3aec.md#insn-004d3b14) · [`004d3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3aec.md#insn-004d3b3c)

~~~diff
- 004d3b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 004d3b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d3b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 004d3b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3b14 bytes 082540f9
+ 004d3b14 bytes 087d40f9
- 004d3b3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
- 004d3b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d3b3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
+ 004d3b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3b3c bytes 082d40f9
+ 004d3b3c bytes 088540f9
~~~


<a id="compare-0a91e9ef303ca05f2d6163e9bb0585eb"></a>

### [`004d3ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3ba0.md) → [`004d3ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3ba0.md) _ZNK5Botan7SHA_25610copy_stateEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d3cc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d3bd4",
      "incomplete_value": true,
      "site": "004d3bd8",
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
      "definition_site": "004d3bd4",
      "incomplete_value": true,
      "site": "004d3bd8",
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
      "definition_site": "004d3c00",
      "incomplete_value": true,
      "site": "004d3c08",
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
      "definition_site": "004d3c00",
      "incomplete_value": true,
      "site": "004d3c08",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d3bc8",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "004d3bd8",
      "DATA",
      [
        "storage",
        "00be9c18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d3bf0",
      "READ",
      [
        "storage",
        "00c1b060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d3bc8",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004d3bd8",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004d3bf0",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d3bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3ba0.md#insn-004d3bc8) · [`004d3bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3ba0.md#insn-004d3bf0)
- 新版 [`004d3bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3ba0.md#insn-004d3bc8) · [`004d3bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3ba0.md#insn-004d3bf0)

~~~diff
- 004d3bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 004d3bc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d3bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 004d3bc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3bc8 bytes 082540f9
+ 004d3bc8 bytes 087d40f9
- 004d3bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
- 004d3bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d3bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
+ 004d3bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3bf0 bytes 083140f9
+ 004d3bf0 bytes 088940f9
~~~


<a id="compare-4534aca8cee8dad71c2436bafe08eee4"></a>

### [`004d5ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5ed0.md) → [`004d5ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5ed0.md) _ZN5Botan10system_rngEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc860.md) · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6094.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bdc910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc910.md) · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6094.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d5f04",
      "incomplete_value": false,
      "site": "004d5f08",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f04",
      "incomplete_value": false,
      "site": "004d5f08",
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
            "const:2d0:8"
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
      "definition_site": "004d5f20",
      "incomplete_value": false,
      "site": "004d5f2c",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f20",
      "incomplete_value": false,
      "site": "004d5f2c",
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
            "const:2c0:8"
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
      "definition_site": "004d5f28",
      "incomplete_value": false,
      "site": "004d5f2c",
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
      "definition_site": "004d5f28",
      "incomplete_value": false,
      "site": "004d5f2c",
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
      "004d5ee4",
      "READ",
      [
        "storage",
        "00c252d0",
        null,
        "undefined1"
      ]
    ],
    [
      "004d5ef0",
      "DATA",
      [
        "storage",
        "00c252c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004d5f04",
      "PARAM",
      [
        "storage",
        "00c252d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004d5ee4",
      "READ",
      [
        "storage",
        "00c25390",
        null,
        "undefined1"
      ]
    ],
    [
      "004d5ef0",
      "DATA",
      [
        "storage",
        "00c25380",
        null,
        "undefined8"
      ]
    ],
    [
      "004d5f04",
      "PARAM",
      [
        "storage",
        "00c25390",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5ed0.md#insn-004d5ee0) · [`004d5ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5ed0.md#insn-004d5ef0) · [`004d5f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5ed0.md#insn-004d5f04)
- 新版 [`004d5ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5ed0.md#insn-004d5ee0) · [`004d5ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5ed0.md#insn-004d5ef0) · [`004d5f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5ed0.md#insn-004d5f04)

~~~diff
- 004d5ee0 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 004d5ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d5ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d5ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d5ee0 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 004d5ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d5ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d5ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d5ee0 bytes 08410b91
+ 004d5ee0 bytes 08410e91
- 004d5ef0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 004d5ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d5ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d5ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d5ef0 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 004d5ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d5ef0 bytes 00000b91
+ 004d5ef0 bytes 00000e91
- 004d5f04 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 004d5f04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d5f04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d5f04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d5f04 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 004d5f04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5f04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5f04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d5f04 bytes 00400b91
+ 004d5f04 bytes 00400e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35b86efe0b34ffabd525bf9d9f589ba"></a>

### [`004d5f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5f58.md) → [`004d5f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md) FUN_004d5f58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004d5ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5ed0.md) [`0051308c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/0051308c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 2件 [`004d5ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5ed0.md) [`0051308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051308c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004d5f94",
      "incomplete_value": false,
      "site": "004d5f94",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f94",
      "incomplete_value": false,
      "site": "004d5f94",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d5f90",
      "incomplete_value": false,
      "site": "004d5f94",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f90",
      "incomplete_value": false,
      "site": "004d5f94",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004d5fb8",
      "incomplete_value": false,
      "site": "004d5fb8",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5fb8",
      "incomplete_value": false,
      "site": "004d5fb8",
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
            "const:2c8:8"
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
      "004d5f80",
      "PARAM",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ],
    [
      "004d5f94",
      "WRITE",
      [
        "storage",
        "00c252c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004d5f94",
      "DATA",
      [
        "storage",
        "00bed1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004d5f80",
      "PARAM",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "004d5f94",
      "WRITE",
      [
        "storage",
        "00c25380",
        null,
        "undefined8"
      ]
    ],
    [
      "004d5f94",
      "DATA",
      [
        "storage",
        "00bed290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5f58.md#insn-004d5fb8) · [`004d5f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5f58.md#insn-004d5f74) · [`004d5f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d5/004d5f58.md#insn-004d5f80)
- 新版 [`004d5fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md#insn-004d5fb8) · [`004d5f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md#insn-004d5f74) · [`004d5f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md#insn-004d5f80)

~~~diff
- 004d5fb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
- 004d5fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 004d5fb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 004d5fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 004d5fb8 bytes 00c902b9
+ 004d5fb8 bytes 008903b9
- 004d5f74 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 004d5f74 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004d5f74 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004d5f74 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004d5f74 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 004d5f74 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004d5f74 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004d5f74 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004d5f74 bytes 94020b91
+ 004d5f74 bytes 94020e91
- 004d5f80 ["COPY", "tmp:0:8", ["const:135:8"]]
- 004d5f80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d5f80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d5f80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d5f80 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 004d5f80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5f80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d5f80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d5f80 bytes 00d40491
+ 004d5f80 bytes 00840291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b44caafc7cf15a230b04484ca2af324f"></a>

### [`004d60c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d60c4.md) → [`004d60c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d60c4.md) _ZNK5Botan14calendar_point9to_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d6268",
      "incomplete_value": true,
      "site": "004d6270",
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
      "definition_site": "004d6268",
      "incomplete_value": true,
      "site": "004d6270",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "LOAD",
        "8",
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
      "004d612c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004d612c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004d6178",
      "PARAM",
      [
        "storage",
        "002a8277",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d612c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "004d612c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004d6178",
      "PARAM",
      [
        "storage",
        "002a81e3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d612c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d60c4.md#insn-004d612c) · [`004d6178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d60c4.md#insn-004d6178) · [`004d61a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d60c4.md#insn-004d61a4)
- 新版 [`004d612c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d60c4.md#insn-004d612c) · [`004d6178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d60c4.md#insn-004d6178) · [`004d61a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d60c4.md#insn-004d61a4)

~~~diff
- 004d612c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 004d612c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d612c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 004d612c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d612c bytes 21a046f9
+ 004d612c bytes 21f846f9
- 004d6178 ["COPY", "tmp:0:8", ["const:277:8"]]
- 004d6178 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6178 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6178 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6178 ["COPY", "tmp:0:8", ["const:1e3:8"]]
+ 004d6178 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6178 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6178 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6178 bytes 21dc0991
+ 004d6178 bytes 218c0791
- 004d61a4 ["COPY", "tmp:0:8", ["const:277:8"]]
- 004d61a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d61a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d61a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d61a4 ["COPY", "tmp:0:8", ["const:1e3:8"]]
+ 004d61a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d61a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d61a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d61a4 bytes 21dc0991
+ 004d61a4 bytes 218c0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b35c5ffbd6ce07aceab6ec9e2e75cb"></a>

### [`004d6338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6338.md) → [`004d6338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md) FUN_004d6338

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048aad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048aad4.md) [`0048ac0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048ac0c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 2件 [`0048aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048aad4.md) [`0048ac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ac0c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6460",
      "incomplete_value": false,
      "site": "004d6468",
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
            "const:69c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6460",
      "incomplete_value": false,
      "site": "004d6468",
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
            "const:6a3:8"
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
      "definition_site": "004d6498",
      "incomplete_value": true,
      "site": "004d64a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d6498",
      "incomplete_value": true,
      "site": "004d64a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d64bc",
      "incomplete_value": false,
      "site": "004d64c4",
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
            "const:69c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d64bc",
      "incomplete_value": false,
      "site": "004d64c4",
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
            "const:6a3:8"
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
      "004d6460",
      "PARAM",
      [
        "storage",
        "002a56a3",
        null,
        "string"
      ]
    ],
    [
      "004d6498",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004d6498",
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
      "004d6460",
      "PARAM",
      [
        "storage",
        "002a569c",
        null,
        "string"
      ]
    ],
    [
      "004d6498",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004d6498",
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

- 旧版 [`004d6460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6338.md#insn-004d6460) · [`004d6498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6338.md#insn-004d6498) · [`004d64bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6338.md#insn-004d64bc)
- 新版 [`004d6460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md#insn-004d6460) · [`004d6498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md#insn-004d6498) · [`004d64bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md#insn-004d64bc)

~~~diff
- 004d6460 ["COPY", "tmp:0:8", ["const:6a3:8"]]
- 004d6460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6460 ["COPY", "tmp:0:8", ["const:69c:8"]]
+ 004d6460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6460 bytes 218c1a91
+ 004d6460 bytes 21701a91
- 004d6498 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004d6498 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d6498 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004d6498 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6498 bytes 213047f9
+ 004d6498 bytes 218847f9
- 004d64bc ["COPY", "tmp:0:8", ["const:6a3:8"]]
- 004d64bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d64bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d64bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d64bc ["COPY", "tmp:0:8", ["const:69c:8"]]
+ 004d64bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d64bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d64bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d64bc bytes 218c1a91
+ 004d64bc bytes 21701a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc96f2afefe4216a5da08a5b8f2f9c3"></a>

### [`004d6550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6550.md) → [`004d6550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6550.md) _ZN5Botan7Charset9transcodeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_13Character_SetESA_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00483974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6794",
      "incomplete_value": false,
      "site": "004d679c",
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
            "const:5a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6794",
      "incomplete_value": false,
      "site": "004d679c",
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
            "const:514:8"
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
      "definition_site": "004d67cc",
      "incomplete_value": true,
      "site": "004d67d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d67cc",
      "incomplete_value": true,
      "site": "004d67d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6800",
      "incomplete_value": false,
      "site": "004d680c",
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
            "const:465:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6800",
      "incomplete_value": false,
      "site": "004d680c",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d6794",
      "PARAM",
      [
        "storage",
        "0029e514",
        null,
        "string"
      ]
    ],
    [
      "004d67cc",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004d67cc",
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
      "004d6794",
      "PARAM",
      [
        "storage",
        "0029e5a1",
        null,
        "string"
      ]
    ],
    [
      "004d67cc",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004d67cc",
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

- 旧版 [`004d6794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6550.md#insn-004d6794) · [`004d67cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6550.md#insn-004d67cc) · [`004d6800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6550.md#insn-004d6800)
- 新版 [`004d6794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6550.md#insn-004d6794) · [`004d67cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6550.md#insn-004d67cc) · [`004d6800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6550.md#insn-004d6800)

~~~diff
- 004d6794 ["COPY", "tmp:0:8", ["const:514:8"]]
- 004d6794 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6794 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6794 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6794 ["COPY", "tmp:0:8", ["const:5a1:8"]]
+ 004d6794 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6794 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6794 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6794 bytes 21501491
+ 004d6794 bytes 21841691
- 004d67cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004d67cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d67cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004d67cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d67cc bytes 213047f9
+ 004d67cc bytes 218847f9
- 004d6800 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 004d6800 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004d6800 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004d6800 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004d6800 ["COPY", "tmp:0:8", ["const:465:8"]]
+ 004d6800 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004d6800 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004d6800 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004d6800 bytes 42600f91
+ 004d6800 bytes 42941191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c3a071f29e23b6b7bafca34eb1fc02"></a>

### [`004d6c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c30.md) → [`004d6c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c30.md) _ZN5Botan17DataSource_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md) · 呼出先 1件 [`0051d4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d4f0.md)
- 新版 呼出元 1件 [`00bdc620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc620.md) · 呼出先 1件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md)

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
      "definition_site": "004d6c48",
      "incomplete_value": true,
      "site": "004d6c4c",
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
      "definition_site": "004d6c48",
      "incomplete_value": true,
      "site": "004d6c4c",
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
      "004d6c44",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004d6c4c",
      "DATA",
      [
        "storage",
        "00bea2c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004d6c44",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004d6c4c",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c30.md#insn-004d6c44)
- 新版 [`004d6c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c30.md#insn-004d6c44)

~~~diff
- 004d6c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 004d6c44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d6c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004d6c44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6c44 bytes 087947f9
+ 004d6c44 bytes 08d147f9
~~~


<a id="compare-6768f52807f232df61238c04e2ef5ac4"></a>

### [`004d6c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c8c.md) → [`004d6c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c8c.md) _ZN5Botan17DataSource_Stream4readEPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6d18",
      "incomplete_value": false,
      "site": "004d6d20",
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
            "const:489:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6d18",
      "incomplete_value": false,
      "site": "004d6d20",
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
            "const:3fc:8"
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
      "definition_site": "004d6d54",
      "incomplete_value": true,
      "site": "004d6d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6d54",
      "incomplete_value": true,
      "site": "004d6d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
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
      "004d6d18",
      "PARAM",
      [
        "storage",
        "0029d3fc",
        null,
        "string"
      ]
    ],
    [
      "004d6d54",
      "READ",
      [
        "storage",
        "00c1ae90",
        null,
        "pointer"
      ]
    ],
    [
      "004d6d54",
      "PARAM",
      [
        "storage",
        "00be91a0",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004d6d18",
      "PARAM",
      [
        "storage",
        "0029d489",
        null,
        "string"
      ]
    ],
    [
      "004d6d54",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004d6d54",
      "PARAM",
      [
        "storage",
        "00be9250",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c8c.md#insn-004d6d18) · [`004d6d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c8c.md#insn-004d6d54)
- 新版 [`004d6d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c8c.md#insn-004d6d18) · [`004d6d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c8c.md#insn-004d6d54)

~~~diff
- 004d6d18 ["COPY", "tmp:0:8", ["const:3fc:8"]]
- 004d6d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6d18 ["COPY", "tmp:0:8", ["const:489:8"]]
+ 004d6d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6d18 bytes 21f00f91
+ 004d6d18 bytes 21241291
- 004d6d54 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e90:8"]]
- 004d6d54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d6d54 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004d6d54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6d54 bytes 214847f9
+ 004d6d54 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8858497c7ba14193fb01a542fdd8224"></a>

### [`004d6e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6e20.md) → [`004d6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6e20.md) _ZNK5Botan17DataSource_Stream4peekEPhmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00490630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d6ed0",
      "incomplete_value": true,
      "site": "004d6ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d6ed0",
      "incomplete_value": true,
      "site": "004d6ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6f94",
      "incomplete_value": false,
      "site": "004d6f9c",
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
            "const:482:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6f94",
      "incomplete_value": false,
      "site": "004d6f9c",
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
            "const:3f5:8"
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
      "definition_site": "004d6fcc",
      "incomplete_value": true,
      "site": "004d6fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d6fcc",
      "incomplete_value": true,
      "site": "004d6fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d6ec0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004d6f94",
      "PARAM",
      [
        "storage",
        "0029e3f5",
        null,
        "string"
      ]
    ],
    [
      "004d6fcc",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d6ec0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004d6f94",
      "PARAM",
      [
        "storage",
        "0029e482",
        null,
        "string"
      ]
    ],
    [
      "004d6fcc",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6e20.md#insn-004d6ec0) · [`004d6f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6e20.md#insn-004d6f94) · [`004d6fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6e20.md#insn-004d6fcc)
- 新版 [`004d6ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6e20.md#insn-004d6ec0) · [`004d6f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6e20.md#insn-004d6f94) · [`004d6fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6e20.md#insn-004d6fcc)

~~~diff
- 004d6ec0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004d6ec0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d6ec0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004d6ec0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6ec0 bytes 293d43f9
+ 004d6ec0 bytes 299543f9
- 004d6f94 ["COPY", "tmp:0:8", ["const:3f5:8"]]
- 004d6f94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6f94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6f94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6f94 ["COPY", "tmp:0:8", ["const:482:8"]]
+ 004d6f94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6f94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6f94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6f94 bytes 21d40f91
+ 004d6f94 bytes 21081291
- 004d6fcc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004d6fcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d6fcc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004d6fcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6fcc bytes 212c47f9
+ 004d6fcc bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6754636f248967dfa45f18054e82bf2"></a>

### [`004d717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d717c.md) → [`004d717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d717c.md) _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc710.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004d7338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7338.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004d7338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7338.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d71bc",
      "incomplete_value": true,
      "site": "004d71bc",
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
      "definition_site": "004d71bc",
      "incomplete_value": true,
      "site": "004d71bc",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7260",
      "incomplete_value": false,
      "site": "004d726c",
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
            "const:4b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7260",
      "incomplete_value": false,
      "site": "004d726c",
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
            "const:425:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d729c",
      "incomplete_value": true,
      "site": "004d72a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d729c",
      "incomplete_value": true,
      "site": "004d72a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
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
      "004d71a0",
      "READ",
      [
        "storage",
        "00c1b138",
        null,
        "pointer"
      ]
    ],
    [
      "004d71bc",
      "DATA",
      [
        "storage",
        "00bea318",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004d7260",
      "PARAM",
      [
        "storage",
        "0029e425",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d71a0",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004d71bc",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004d7260",
      "PARAM",
      [
        "storage",
        "0029e4b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d71a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d717c.md#insn-004d71a0) · [`004d7260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d717c.md#insn-004d7260) · [`004d729c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d717c.md#insn-004d729c)
- 新版 [`004d71a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d717c.md#insn-004d71a0) · [`004d7260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d717c.md#insn-004d7260) · [`004d729c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d717c.md#insn-004d729c)

~~~diff
- 004d71a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:138:8"]]
- 004d71a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d71a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 004d71a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d71a0 bytes 089d40f9
+ 004d71a0 bytes 08f540f9
- 004d7260 ["COPY", "tmp:0:8", ["const:425:8"]]
- 004d7260 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d7260 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d7260 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d7260 ["COPY", "tmp:0:8", ["const:4b2:8"]]
+ 004d7260 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7260 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7260 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d7260 bytes 00941091
+ 004d7260 bytes 00c81291
- 004d729c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e90:8"]]
- 004d729c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d729c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004d729c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d729c bytes 214847f9
+ 004d729c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0790f0c07e04c53f9ed32a78614f037"></a>

### [`004d7338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7338.md) → [`004d7338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7338.md) FUN_004d7338

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d717c.md) · 呼出先 4件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdbfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfb0.md) [`00bdbfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfc0.md)
- 新版 呼出元 1件 [`004d717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d717c.md) · 呼出先 4件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc060.md) [`00bdc070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc070.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d737c",
      "incomplete_value": true,
      "site": "004d737c",
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
      "definition_site": "004d737c",
      "incomplete_value": true,
      "site": "004d737c",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7374",
      "incomplete_value": true,
      "site": "004d7380",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7374",
      "incomplete_value": true,
      "site": "004d7380",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004d738c",
      "incomplete_value": true,
      "site": "004d738c",
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
      "definition_site": "004d738c",
      "incomplete_value": true,
      "site": "004d738c",
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
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d735c",
      "READ",
      [
        "storage",
        "00c1b140",
        null,
        "pointer"
      ]
    ],
    [
      "004d7360",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004d7374",
      "READ",
      [
        "storage",
        "00c13208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004d735c",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004d7360",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "004d7374",
      "READ",
      [
        "storage",
        "00c132b8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d735c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7338.md#insn-004d735c) · [`004d7360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7338.md#insn-004d7360)
- 新版 [`004d735c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7338.md#insn-004d735c) · [`004d7360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7338.md#insn-004d7360)

~~~diff
- 004d735c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:140:8"]]
- 004d735c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d735c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:1f0:8"]]
+ 004d735c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004d735c bytes 39a340f9
+ 004d735c bytes 39fb40f9
- 004d7360 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:148:8"]]
- 004d7360 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7360 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:1f8:8"]]
+ 004d7360 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7360 bytes 18a740f9
+ 004d7360 bytes 18ff40f9
~~~


<a id="compare-5aeaac9eaad0b5979e7e4add4fe88936"></a>

### [`004d7450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7450.md) → [`004d7450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7450.md) _ZN5Botan17DataSource_StreamC2ERNSt6__ndk113basic_istreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "004d7470",
      "incomplete_value": true,
      "site": "004d7470",
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
      "definition_site": "004d7470",
      "incomplete_value": true,
      "site": "004d7470",
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
      "004d7468",
      "READ",
      [
        "storage",
        "00c1b138",
        null,
        "pointer"
      ]
    ],
    [
      "004d7470",
      "DATA",
      [
        "storage",
        "00bea318",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004d7468",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004d7470",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7450.md#insn-004d7468)
- 新版 [`004d7468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7450.md#insn-004d7468)

~~~diff
- 004d7468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:138:8"]]
- 004d7468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 004d7468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7468 bytes 089d40f9
+ 004d7468 bytes 08f540f9
~~~


<a id="compare-a7e67ad0b3f52122c5590a5d44fab79d"></a>

### [`004d751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d751c.md) → [`004d751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d751c.md) _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb870.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00bdb920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb920.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "004d7538",
      "incomplete_value": true,
      "site": "004d7538",
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
      "definition_site": "004d7538",
      "incomplete_value": true,
      "site": "004d7538",
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
      "004d7530",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d7538",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d7530",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d7538",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d751c.md#insn-004d7530)
- 新版 [`004d7530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d751c.md#insn-004d7530)

~~~diff
- 004d7530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d7530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d7530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7530 bytes 087147f9
+ 004d7530 bytes 08c947f9
~~~


<a id="compare-dbf6747abf5130efc828b084f6eac25b"></a>

### [`004d7584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7584.md) → [`004d7584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7584.md) _ZN5Botan9ExceptionC2EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d75cc",
      "incomplete_value": true,
      "site": "004d75cc",
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
      "definition_site": "004d75cc",
      "incomplete_value": true,
      "site": "004d75cc",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7648",
      "incomplete_value": false,
      "site": "004d7650",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7648",
      "incomplete_value": false,
      "site": "004d7650",
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
            "const:8e1:8"
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
      "004d75b0",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d75cc",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004d7648",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d75b0",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d75cc",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004d7648",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d75b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7584.md#insn-004d75b0) · [`004d7648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7584.md#insn-004d7648)
- 新版 [`004d75b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7584.md#insn-004d75b0) · [`004d7648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7584.md#insn-004d7648)

~~~diff
- 004d75b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ee0:8"]]
- 004d75b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d75b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f90:8"]]
+ 004d75b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d75b0 bytes 297147f9
+ 004d75b0 bytes 29c947f9
- 004d7648 ["COPY", "tmp:0:8", ["const:8e1:8"]]
- 004d7648 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d7648 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d7648 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d7648 ["COPY", "tmp:0:8", ["const:96e:8"]]
+ 004d7648 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7648 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7648 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d7648 bytes 21842391
+ 004d7648 bytes 21b82591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa3aed9fb442f72d316edc9cc7c84336"></a>

### [`004d7760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7760.md) → [`004d7760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7760.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb720.md) · 呼出先 1件 [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdb7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7d0.md) · 呼出先 1件 [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7788",
      "incomplete_value": true,
      "site": "004d778c",
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
      "definition_site": "004d7788",
      "incomplete_value": true,
      "site": "004d778c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7774",
      "incomplete_value": false,
      "site": "004d777c",
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
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7774",
      "incomplete_value": false,
      "site": "004d777c",
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
            "const:83d:8"
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
      "004d7774",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004d7784",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004d778c",
      "DATA",
      [
        "storage",
        "00bea390",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d7774",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004d7784",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004d778c",
      "DATA",
      [
        "storage",
        "00bea440",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7760.md#insn-004d7774) · [`004d7784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7760.md#insn-004d7784)
- 新版 [`004d7774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7760.md#insn-004d7774) · [`004d7784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7760.md#insn-004d7784)

~~~diff
- 004d7774 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d7774 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d7774 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d7774 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d7774 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d7774 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7774 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7774 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d7774 bytes 21f42091
+ 004d7774 bytes 21282391
- 004d7784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004d7784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 004d7784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7784 bytes 083947f9
+ 004d7784 bytes 089147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e4f3cc678a968280f48b0cb17e01c5"></a>

### [`004d779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d779c.md) → [`004d779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d779c.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d78ec",
      "incomplete_value": true,
      "site": "004d78f0",
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
      "definition_site": "004d78ec",
      "incomplete_value": true,
      "site": "004d78f0",
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
      "definition_site": "004d78b4",
      "incomplete_value": false,
      "site": "004d78c0",
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
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d78b4",
      "incomplete_value": false,
      "site": "004d78c0",
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
            "const:83d:8"
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
      "004d78b4",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004d78e8",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004d78f0",
      "DATA",
      [
        "storage",
        "00bea390",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d78b4",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004d78e8",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004d78f0",
      "DATA",
      [
        "storage",
        "00bea440",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d78b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d779c.md#insn-004d78b4) · [`004d78e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d779c.md#insn-004d78e8)
- 新版 [`004d78b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d779c.md#insn-004d78b4) · [`004d78e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d779c.md#insn-004d78e8)

~~~diff
- 004d78b4 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d78b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d78b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d78b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d78b4 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d78b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d78b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d78b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d78b4 bytes 21f42091
+ 004d78b4 bytes 21282391
- 004d78e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004d78e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d78e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 004d78e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d78e8 bytes 083947f9
+ 004d78e8 bytes 089147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057d03e3681b0a067fc595d0f3bfda50"></a>

### [`004d7984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7984.md) → [`004d7984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7984.md) _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe00.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdbeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbeb0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7aa8",
      "incomplete_value": true,
      "site": "004d7aa8",
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
      "definition_site": "004d7aa8",
      "incomplete_value": true,
      "site": "004d7aa8",
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
      "definition_site": "004d7b00",
      "incomplete_value": true,
      "site": "004d7b04",
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
      "definition_site": "004d7b00",
      "incomplete_value": true,
      "site": "004d7b04",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d79a4",
      "incomplete_value": false,
      "site": "004d79bc",
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
            "const:8f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d79a4",
      "incomplete_value": false,
      "site": "004d79bc",
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
            "const:987:8"
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
      "004d79a4",
      "PARAM",
      [
        "storage",
        "002ae987",
        null,
        "string"
      ]
    ],
    [
      "004d79c4",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "004d7a3c",
      "PARAM",
      [
        "storage",
        "0029c54f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d79a4",
      "PARAM",
      [
        "storage",
        "002ae8f3",
        null,
        "string"
      ]
    ],
    [
      "004d79c4",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ],
    [
      "004d7a3c",
      "PARAM",
      [
        "storage",
        "0029c5dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d79a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7984.md#insn-004d79a4) · [`004d79c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7984.md#insn-004d79c4) · [`004d7a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7984.md#insn-004d7a3c)
- 新版 [`004d79a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7984.md#insn-004d79a4) · [`004d79c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7984.md#insn-004d79c4) · [`004d7a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7984.md#insn-004d7a3c)

~~~diff
- 004d79a4 ["COPY", "tmp:0:8", ["const:987:8"]]
- 004d79a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d79a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d79a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d79a4 ["COPY", "tmp:0:8", ["const:8f3:8"]]
+ 004d79a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d79a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d79a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d79a4 bytes 001c2691
+ 004d79a4 bytes 00cc2391
- 004d79c4 ["COPY", "tmp:0:8", ["const:8e1:8"]]
- 004d79c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d79c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d79c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d79c4 ["COPY", "tmp:0:8", ["const:96e:8"]]
+ 004d79c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d79c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d79c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d79c4 bytes 21842391
+ 004d79c4 bytes 21b82591
- 004d7a3c ["COPY", "tmp:0:8", ["const:54f:8"]]
- 004d7a3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d7a3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d7a3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d7a3c ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 004d7a3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7a3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7a3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d7a3c bytes 003c1591
+ 004d7a3c bytes 00701791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-961a05ce3bb9ee2f5b10857d62a8a163"></a>

### [`004d7c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7c34.md) → [`004d7c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7c34.md) _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdbbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbbb0.md) [`00bdc8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc8d0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00bdbc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc60.md) [`00bdc980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc980.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

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
      "definition_site": "004d7c7c",
      "incomplete_value": true,
      "site": "004d7c7c",
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
      "definition_site": "004d7c7c",
      "incomplete_value": true,
      "site": "004d7c7c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7cb8",
      "incomplete_value": true,
      "site": "004d7cbc",
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
      "definition_site": "004d7cb8",
      "incomplete_value": true,
      "site": "004d7cbc",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7c54",
      "incomplete_value": false,
      "site": "004d7c64",
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
            "const:5ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7c54",
      "incomplete_value": false,
      "site": "004d7c64",
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
            "const:520:8"
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
      "004d7c54",
      "PARAM",
      [
        "storage",
        "002a0520",
        null,
        "string"
      ]
    ],
    [
      "004d7c70",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d7c7c",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d7c54",
      "PARAM",
      [
        "storage",
        "002a05ad",
        null,
        "string"
      ]
    ],
    [
      "004d7c70",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d7c7c",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7c34.md#insn-004d7c54) · [`004d7c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7c34.md#insn-004d7c70) · [`004d7cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7c34.md#insn-004d7cb4)
- 新版 [`004d7c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7c34.md#insn-004d7c54) · [`004d7c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7c34.md#insn-004d7c70) · [`004d7cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7c34.md#insn-004d7cb4)

~~~diff
- 004d7c54 ["COPY", "tmp:0:8", ["const:520:8"]]
- 004d7c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d7c54 ["COPY", "tmp:0:8", ["const:5ad:8"]]
+ 004d7c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 bytes 00801491
+ 004d7c54 bytes 00b41691
- 004d7c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d7c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d7c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7c70 bytes 087147f9
+ 004d7c70 bytes 08c947f9
- 004d7cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:150:8"]]
- 004d7cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004d7cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7cb4 bytes 08a940f9
+ 004d7cb4 bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd86167817dc08bb31ca53055889b560"></a>

### [`004d7d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7d1c.md) → [`004d7d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7d1c.md) _ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe30.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdbee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbee0.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7df0",
      "incomplete_value": true,
      "site": "004d7dfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:89d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7df0",
      "incomplete_value": true,
      "site": "004d7dfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:810:8"
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
      "definition_site": "004d7df4",
      "incomplete_value": true,
      "site": "004d7e00",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004d7df4",
      "incomplete_value": true,
      "site": "004d7e00",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d7e6c",
      "incomplete_value": true,
      "site": "004d7e70",
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
      "definition_site": "004d7e6c",
      "incomplete_value": true,
      "site": "004d7e70",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d7df0",
      "READ",
      [
        "storage",
        "00294810",
        null,
        "string"
      ]
    ],
    [
      "004d7df4",
      "READ",
      [
        "storage",
        "0029481f",
        null,
        "string"
      ]
    ],
    [
      "004d7e50",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7df0",
      "READ",
      [
        "storage",
        "0029489d",
        null,
        "string"
      ]
    ],
    [
      "004d7df4",
      "READ",
      [
        "storage",
        "002948ac",
        null,
        "string"
      ]
    ],
    [
      "004d7e50",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7d1c.md#insn-004d7de8) · [`004d7e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7d1c.md#insn-004d7e50) · [`004d7e64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7d1c.md#insn-004d7e64)
- 新版 [`004d7de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7d1c.md#insn-004d7de8) · [`004d7e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7d1c.md#insn-004d7e50) · [`004d7e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7d1c.md#insn-004d7e64)

~~~diff
- 004d7de8 ["COPY", "tmp:0:8", ["const:810:8"]]
- 004d7de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d7de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d7de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d7de8 ["COPY", "tmp:0:8", ["const:89d:8"]]
+ 004d7de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d7de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d7de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d7de8 bytes 08412091
+ 004d7de8 bytes 08752291
- 004d7e50 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d7e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d7e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d7e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d7e50 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d7e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d7e50 bytes 21f42091
+ 004d7e50 bytes 21282391
- 004d7e64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004d7e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d7e64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 004d7e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7e64 bytes 083947f9
+ 004d7e64 bytes 089147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5343e598fbdec8c704c2134629bc8e2"></a>

### [`004d7f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7f90.md) → [`004d7f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7f90.md) _ZN5Botan17Invalid_IV_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe40.md) · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdbef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbef0.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8070",
      "incomplete_value": true,
      "site": "004d8074",
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
      "definition_site": "004d8070",
      "incomplete_value": true,
      "site": "004d8074",
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
      "definition_site": "004d80a4",
      "incomplete_value": true,
      "site": "004d80a8",
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
      "definition_site": "004d80a4",
      "incomplete_value": true,
      "site": "004d80a8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7fc8",
      "incomplete_value": false,
      "site": "004d7fd4",
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
            "const:4c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7fc8",
      "incomplete_value": false,
      "site": "004d7fd4",
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
            "const:4cc:8"
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
      "004d7fc8",
      "PARAM",
      [
        "storage",
        "002a44cc",
        null,
        "string"
      ]
    ],
    [
      "004d7ff4",
      "PARAM",
      [
        "storage",
        "0029e447",
        null,
        "string"
      ]
    ],
    [
      "004d8054",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7fc8",
      "PARAM",
      [
        "storage",
        "002a44c5",
        null,
        "string"
      ]
    ],
    [
      "004d7ff4",
      "PARAM",
      [
        "storage",
        "0029e4d4",
        null,
        "string"
      ]
    ],
    [
      "004d8054",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7f90.md#insn-004d7fc8) · [`004d7ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7f90.md#insn-004d7ff4) · [`004d8054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7f90.md#insn-004d8054)
- 新版 [`004d7fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7f90.md#insn-004d7fc8) · [`004d7ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7f90.md#insn-004d7ff4) · [`004d8054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7f90.md#insn-004d8054)

~~~diff
- 004d7fc8 ["COPY", "tmp:0:8", ["const:4cc:8"]]
- 004d7fc8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004d7fc8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004d7fc8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004d7fc8 ["COPY", "tmp:0:8", ["const:4c5:8"]]
+ 004d7fc8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004d7fc8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004d7fc8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004d7fc8 bytes 42301391
+ 004d7fc8 bytes 42141391
- 004d7ff4 ["COPY", "tmp:0:8", ["const:447:8"]]
- 004d7ff4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d7ff4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d7ff4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d7ff4 ["COPY", "tmp:0:8", ["const:4d4:8"]]
+ 004d7ff4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7ff4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d7ff4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d7ff4 bytes 211c1191
+ 004d7ff4 bytes 21501391
- 004d8054 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d8054 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8054 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8054 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8054 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d8054 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8054 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8054 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8054 bytes 21f42091
+ 004d8054 bytes 21282391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-784b566695135bdd9df01bbdff9e637b"></a>

### [`004d81b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d81b0.md) → [`004d81b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d81b0.md) _ZN5Botan11Key_Not_SetC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6f0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7a0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d81f8",
      "incomplete_value": true,
      "site": "004d81f8",
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
      "definition_site": "004d81f8",
      "incomplete_value": true,
      "site": "004d81f8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8214",
      "incomplete_value": true,
      "site": "004d821c",
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
      "definition_site": "004d8214",
      "incomplete_value": true,
      "site": "004d821c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8238",
      "incomplete_value": true,
      "site": "004d823c",
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
      "definition_site": "004d8238",
      "incomplete_value": true,
      "site": "004d823c",
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
      "004d81d0",
      "PARAM",
      [
        "storage",
        "00299c6b",
        null,
        "string"
      ]
    ],
    [
      "004d81ec",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d81f8",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d81d0",
      "PARAM",
      [
        "storage",
        "00299cf8",
        null,
        "string"
      ]
    ],
    [
      "004d81ec",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d81f8",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d81d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d81b0.md#insn-004d81d0) · [`004d81ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d81b0.md#insn-004d81ec) · [`004d820c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d81b0.md#insn-004d820c)
- 新版 [`004d81d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d81b0.md#insn-004d81d0) · [`004d81ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d81b0.md#insn-004d81ec) · [`004d820c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d81b0.md#insn-004d820c)

~~~diff
- 004d81d0 ["COPY", "tmp:0:8", ["const:c6b:8"]]
- 004d81d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d81d0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 004d81d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d81d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d81d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 bytes 00ac3191
+ 004d81d0 bytes 00e03391
- 004d81ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d81ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d81ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d81ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d81ec bytes 087147f9
+ 004d81ec bytes 08c947f9
- 004d820c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ee8:8"]]
- 004d820c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d820c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f98:8"]]
+ 004d820c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d820c bytes 297547f9
+ 004d820c bytes 29cd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7064a448159dcd7f2e39b7b6fff3d08e"></a>

### [`004d82b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d82b8.md) → [`004d82b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d82b8.md) _ZN5Botan16Policy_ViolationC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8300",
      "incomplete_value": true,
      "site": "004d8300",
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
      "definition_site": "004d8300",
      "incomplete_value": true,
      "site": "004d8300",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d831c",
      "incomplete_value": true,
      "site": "004d8324",
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
      "definition_site": "004d831c",
      "incomplete_value": true,
      "site": "004d8324",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8340",
      "incomplete_value": true,
      "site": "004d8344",
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
      "definition_site": "004d8340",
      "incomplete_value": true,
      "site": "004d8344",
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
      "004d82d8",
      "PARAM",
      [
        "storage",
        "002a95f9",
        null,
        "string"
      ]
    ],
    [
      "004d82f4",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d8300",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d82d8",
      "PARAM",
      [
        "storage",
        "002a9565",
        null,
        "string"
      ]
    ],
    [
      "004d82f4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d8300",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d82d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d82b8.md#insn-004d82d8) · [`004d82f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d82b8.md#insn-004d82f4) · [`004d8314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d82b8.md#insn-004d8314)
- 新版 [`004d82d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d82b8.md#insn-004d82d8) · [`004d82f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d82b8.md#insn-004d82f4) · [`004d8314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d82b8.md#insn-004d8314)

~~~diff
- 004d82d8 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 004d82d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d82d8 ["COPY", "tmp:0:8", ["const:565:8"]]
+ 004d82d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d82d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d82d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 bytes 00e41791
+ 004d82d8 bytes 00941591
- 004d82f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d82f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d82f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d82f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d82f4 bytes 087147f9
+ 004d82f4 bytes 08c947f9
- 004d8314 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ee8:8"]]
- 004d8314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8314 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f98:8"]]
+ 004d8314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8314 bytes 297547f9
+ 004d8314 bytes 29cd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2261e07e43c0ae498323748c4d9ffc0"></a>

### [`004d83c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d83c0.md) → [`004d83c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d83c0.md) _ZN5Botan13PRNG_UnseededC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd030.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdd0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0e0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8408",
      "incomplete_value": true,
      "site": "004d8408",
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
      "definition_site": "004d8408",
      "incomplete_value": true,
      "site": "004d8408",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8424",
      "incomplete_value": true,
      "site": "004d842c",
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
      "definition_site": "004d8424",
      "incomplete_value": true,
      "site": "004d842c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8448",
      "incomplete_value": true,
      "site": "004d844c",
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
      "definition_site": "004d8448",
      "incomplete_value": true,
      "site": "004d844c",
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
      "004d83fc",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d8408",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004d841c",
      "READ",
      [
        "storage",
        "00c1aee8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d83fc",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d8408",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004d841c",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d83fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d83c0.md#insn-004d83fc) · [`004d841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d83c0.md#insn-004d841c) · [`004d8440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d83c0.md#insn-004d8440)
- 新版 [`004d83fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d83c0.md#insn-004d83fc) · [`004d841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d83c0.md#insn-004d841c) · [`004d8440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d83c0.md#insn-004d8440)

~~~diff
- 004d83fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d83fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d83fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d83fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d83fc bytes 087147f9
+ 004d83fc bytes 08c947f9
- 004d841c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ee8:8"]]
- 004d841c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d841c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f98:8"]]
+ 004d841c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d841c bytes 297547f9
+ 004d841c bytes 29cd47f9
- 004d8440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
- 004d8440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f98:8"]]
+ 004d8440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8440 bytes 087547f9
+ 004d8440 bytes 08cd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1216360b2438dbc32c87f74b22d45db"></a>

### [`004d84c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d84c8.md) → [`004d84c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d84c8.md) _ZN5Botan19Algorithm_Not_FoundC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc050.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d853c",
      "incomplete_value": true,
      "site": "004d853c",
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
      "definition_site": "004d853c",
      "incomplete_value": true,
      "site": "004d853c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004d8564",
      "incomplete_value": true,
      "site": "004d8568",
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
      "definition_site": "004d8564",
      "incomplete_value": true,
      "site": "004d8568",
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
      "definition_site": "004d8584",
      "incomplete_value": true,
      "site": "004d8588",
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
      "definition_site": "004d8584",
      "incomplete_value": true,
      "site": "004d8588",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d84e8",
      "PARAM",
      [
        "storage",
        "002a14ff",
        null,
        "string"
      ]
    ],
    [
      "004d8500",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "004d8528",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d84e8",
      "PARAM",
      [
        "storage",
        "002a158c",
        null,
        "string"
      ]
    ],
    [
      "004d8500",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "004d8528",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d84e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d84c8.md#insn-004d84e8) · [`004d8500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d84c8.md#insn-004d8500) · [`004d8528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d84c8.md#insn-004d8528)
- 新版 [`004d84e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d84c8.md#insn-004d84e8) · [`004d8500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d84c8.md#insn-004d8500) · [`004d8528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d84c8.md#insn-004d8528)

~~~diff
- 004d84e8 ["COPY", "tmp:0:8", ["const:4ff:8"]]
- 004d84e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d84e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d84e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d84e8 ["COPY", "tmp:0:8", ["const:58c:8"]]
+ 004d84e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d84e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d84e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d84e8 bytes 00fc1391
+ 004d84e8 bytes 00301691
- 004d8500 ["COPY", "tmp:0:8", ["const:39b:8"]]
- 004d8500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8500 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 004d8500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8500 bytes 216c0e91
+ 004d8500 bytes 21500e91
- 004d8528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d8528 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d8528 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8528 bytes 087147f9
+ 004d8528 bytes 08c947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa47dd8b3bb4ced165e5f495c9a8e695"></a>

### [`004d8628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8628.md) → [`004d8628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8628.md) _ZN5Botan17No_Provider_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004d869c",
      "incomplete_value": true,
      "site": "004d869c",
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
      "definition_site": "004d869c",
      "incomplete_value": true,
      "site": "004d869c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004d86d4",
      "incomplete_value": true,
      "site": "004d86d8",
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
      "definition_site": "004d86d4",
      "incomplete_value": true,
      "site": "004d86d8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8648",
      "incomplete_value": false,
      "site": "004d8658",
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
            "const:af7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8648",
      "incomplete_value": false,
      "site": "004d8658",
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
            "const:a6a:8"
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
      "004d8648",
      "PARAM",
      [
        "storage",
        "00295a6a",
        null,
        "string"
      ]
    ],
    [
      "004d8660",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "004d8688",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d8648",
      "PARAM",
      [
        "storage",
        "00295af7",
        null,
        "string"
      ]
    ],
    [
      "004d8660",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "004d8688",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8628.md#insn-004d8648) · [`004d8660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8628.md#insn-004d8660) · [`004d8688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8628.md#insn-004d8688)
- 新版 [`004d8648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8628.md#insn-004d8648) · [`004d8660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8628.md#insn-004d8660) · [`004d8688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8628.md#insn-004d8688)

~~~diff
- 004d8648 ["COPY", "tmp:0:8", ["const:a6a:8"]]
- 004d8648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8648 ["COPY", "tmp:0:8", ["const:af7:8"]]
+ 004d8648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8648 bytes 00a82991
+ 004d8648 bytes 00dc2b91
- 004d8660 ["COPY", "tmp:0:8", ["const:39b:8"]]
- 004d8660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8660 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 004d8660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8660 bytes 216c0e91
+ 004d8660 bytes 21500e91
- 004d8688 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d8688 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8688 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d8688 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8688 bytes 087147f9
+ 004d8688 bytes 08c947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d204488d781d03b47393f1498ee5a18"></a>

### [`004d8768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8768.md) → [`004d8768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8768.md) _ZN5Botan18Provider_Not_FoundC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc820.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdc8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc8d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d881c",
      "incomplete_value": true,
      "site": "004d881c",
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
      "definition_site": "004d881c",
      "incomplete_value": true,
      "site": "004d881c",
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
      "definition_site": "004d8844",
      "incomplete_value": true,
      "site": "004d8848",
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
      "definition_site": "004d8844",
      "incomplete_value": true,
      "site": "004d8848",
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
      "definition_site": "004d8874",
      "incomplete_value": true,
      "site": "004d8878",
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
      "definition_site": "004d8874",
      "incomplete_value": true,
      "site": "004d8878",
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
      "004d8790",
      "PARAM",
      [
        "storage",
        "0029284e",
        null,
        "string"
      ]
    ],
    [
      "004d87a8",
      "PARAM",
      [
        "storage",
        "0029c55e",
        null,
        "string"
      ]
    ],
    [
      "004d8808",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d8790",
      "PARAM",
      [
        "storage",
        "002928db",
        null,
        "string"
      ]
    ],
    [
      "004d87a8",
      "PARAM",
      [
        "storage",
        "0029c5eb",
        null,
        "string"
      ]
    ],
    [
      "004d8808",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8768.md#insn-004d8790) · [`004d87a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8768.md#insn-004d87a8) · [`004d8808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8768.md#insn-004d8808)
- 新版 [`004d8790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8768.md#insn-004d8790) · [`004d87a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8768.md#insn-004d87a8) · [`004d8808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8768.md#insn-004d8808)

~~~diff
- 004d8790 ["COPY", "tmp:0:8", ["const:84e:8"]]
- 004d8790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8790 ["COPY", "tmp:0:8", ["const:8db:8"]]
+ 004d8790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8790 bytes 00382191
+ 004d8790 bytes 006c2391
- 004d87a8 ["COPY", "tmp:0:8", ["const:55e:8"]]
- 004d87a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d87a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d87a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d87a8 ["COPY", "tmp:0:8", ["const:5eb:8"]]
+ 004d87a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d87a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d87a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d87a8 bytes 21781591
+ 004d87a8 bytes 21ac1791
- 004d8808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d8808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d8808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8808 bytes 087147f9
+ 004d8808 bytes 08c947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83bb20f748d97180fe0583d418600ecf"></a>

### [`004d8930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8930.md) → [`004d8930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8930.md) _ZN5Botan22Invalid_Algorithm_NameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc350.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdc400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc400.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8980",
      "incomplete_value": true,
      "site": "004d8984",
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
      "definition_site": "004d8980",
      "incomplete_value": true,
      "site": "004d8984",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d899c",
      "incomplete_value": true,
      "site": "004d89a0",
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
      "definition_site": "004d899c",
      "incomplete_value": true,
      "site": "004d89a0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d894c",
      "incomplete_value": false,
      "site": "004d895c",
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
            "const:4ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d894c",
      "incomplete_value": false,
      "site": "004d895c",
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
            "const:45d:8"
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
      "004d894c",
      "PARAM",
      [
        "storage",
        "0029f45d",
        null,
        "string"
      ]
    ],
    [
      "004d8964",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004d8978",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d894c",
      "PARAM",
      [
        "storage",
        "0029f4ea",
        null,
        "string"
      ]
    ],
    [
      "004d8964",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004d8978",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d894c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8930.md#insn-004d894c) · [`004d8964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8930.md#insn-004d8964) · [`004d8978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8930.md#insn-004d8978)
- 新版 [`004d894c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8930.md#insn-004d894c) · [`004d8964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8930.md#insn-004d8964) · [`004d8978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8930.md#insn-004d8978)

~~~diff
- 004d894c ["COPY", "tmp:0:8", ["const:45d:8"]]
- 004d894c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d894c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d894c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d894c ["COPY", "tmp:0:8", ["const:4ea:8"]]
+ 004d894c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d894c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d894c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d894c bytes 00741191
+ 004d894c bytes 00a81391
- 004d8964 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d8964 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8964 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8964 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8964 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d8964 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8964 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8964 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8964 bytes 21f42091
+ 004d8964 bytes 21282391
- 004d8978 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004d8978 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8978 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 004d8978 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8978 bytes 083947f9
+ 004d8978 bytes 089147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df58ea5bd52afbef47f9691929a84fc"></a>

### [`004d89f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d89f4.md) → [`004d89f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d89f4.md) _ZN5Botan14Encoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8e0.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdb990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb990.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8a44",
      "incomplete_value": true,
      "site": "004d8a48",
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
      "definition_site": "004d8a44",
      "incomplete_value": true,
      "site": "004d8a48",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8a60",
      "incomplete_value": true,
      "site": "004d8a64",
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
      "definition_site": "004d8a60",
      "incomplete_value": true,
      "site": "004d8a64",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8a10",
      "incomplete_value": false,
      "site": "004d8a20",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8a10",
      "incomplete_value": false,
      "site": "004d8a20",
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
            "const:e11:8"
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
      "004d8a10",
      "PARAM",
      [
        "storage",
        "00298e11",
        null,
        "string"
      ]
    ],
    [
      "004d8a28",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004d8a3c",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004d8a10",
      "PARAM",
      [
        "storage",
        "00298e9e",
        null,
        "string"
      ]
    ],
    [
      "004d8a28",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004d8a3c",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d89f4.md#insn-004d8a10) · [`004d8a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d89f4.md#insn-004d8a28) · [`004d8a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d89f4.md#insn-004d8a3c)
- 新版 [`004d8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d89f4.md#insn-004d8a10) · [`004d8a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d89f4.md#insn-004d8a28) · [`004d8a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d89f4.md#insn-004d8a3c)

~~~diff
- 004d8a10 ["COPY", "tmp:0:8", ["const:e11:8"]]
- 004d8a10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8a10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8a10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8a10 ["COPY", "tmp:0:8", ["const:e9e:8"]]
+ 004d8a10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8a10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8a10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8a10 bytes 00443891
+ 004d8a10 bytes 00783a91
- 004d8a28 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d8a28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8a28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8a28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8a28 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d8a28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8a28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8a28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8a28 bytes 21f42091
+ 004d8a28 bytes 21282391
- 004d8a3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004d8a3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8a3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 004d8a3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8a3c bytes 083947f9
+ 004d8a3c bytes 089147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4707ead00b6bd1c53e4382c47fa4a8"></a>

### [`004d8ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8ab8.md) → [`004d8ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8ab8.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcea0.md) · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdcf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf50.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8b5c",
      "incomplete_value": true,
      "site": "004d8b60",
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
      "definition_site": "004d8b5c",
      "incomplete_value": true,
      "site": "004d8b60",
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
      "definition_site": "004d8b88",
      "incomplete_value": true,
      "site": "004d8b8c",
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
      "definition_site": "004d8b88",
      "incomplete_value": true,
      "site": "004d8b8c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8ad8",
      "incomplete_value": false,
      "site": "004d8aec",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8ad8",
      "incomplete_value": false,
      "site": "004d8aec",
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
            "const:994:8"
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
      "004d8ad8",
      "PARAM",
      [
        "storage",
        "002ae994",
        null,
        "string"
      ]
    ],
    [
      "004d8af4",
      "PARAM",
      [
        "storage",
        "00292868",
        null,
        "string"
      ]
    ],
    [
      "004d8b40",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d8ad8",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004d8af4",
      "PARAM",
      [
        "storage",
        "002928f5",
        null,
        "string"
      ]
    ],
    [
      "004d8b40",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8ab8.md#insn-004d8ad8) · [`004d8af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8ab8.md#insn-004d8af4) · [`004d8b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8ab8.md#insn-004d8b40)
- 新版 [`004d8ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8ab8.md#insn-004d8ad8) · [`004d8af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8ab8.md#insn-004d8af4) · [`004d8b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8ab8.md#insn-004d8b40)

~~~diff
- 004d8ad8 ["COPY", "tmp:0:8", ["const:994:8"]]
- 004d8ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8ad8 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 004d8ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8ad8 bytes 00502691
+ 004d8ad8 bytes 00002491
- 004d8af4 ["COPY", "tmp:0:8", ["const:868:8"]]
- 004d8af4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8af4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8af4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8af4 ["COPY", "tmp:0:8", ["const:8f5:8"]]
+ 004d8af4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8af4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8af4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8af4 bytes 21a02191
+ 004d8af4 bytes 21d42391
- 004d8b40 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d8b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8b40 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d8b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8b40 bytes 21f42091
+ 004d8b40 bytes 21282391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-897ebad59cfc2b8db096acbe066ac8ef"></a>

### [`004d8c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8c5c.md) → [`004d8c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8c5c.md) _ZN5Botan17Integrity_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

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
      "definition_site": "004d8ca4",
      "incomplete_value": true,
      "site": "004d8ca4",
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
      "definition_site": "004d8ca4",
      "incomplete_value": true,
      "site": "004d8ca4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8ce0",
      "incomplete_value": true,
      "site": "004d8ce4",
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
      "definition_site": "004d8ce0",
      "incomplete_value": true,
      "site": "004d8ce4",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8c7c",
      "incomplete_value": false,
      "site": "004d8c8c",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8c7c",
      "incomplete_value": false,
      "site": "004d8c8c",
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
            "const:a7b:8"
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
      "004d8c7c",
      "PARAM",
      [
        "storage",
        "00296a7b",
        null,
        "string"
      ]
    ],
    [
      "004d8c98",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d8ca4",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d8c7c",
      "PARAM",
      [
        "storage",
        "00296b08",
        null,
        "string"
      ]
    ],
    [
      "004d8c98",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d8ca4",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8c5c.md#insn-004d8c7c) · [`004d8c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8c5c.md#insn-004d8c98) · [`004d8cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8c5c.md#insn-004d8cdc)
- 新版 [`004d8c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8c5c.md#insn-004d8c7c) · [`004d8c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8c5c.md#insn-004d8c98) · [`004d8cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8c5c.md#insn-004d8cdc)

~~~diff
- 004d8c7c ["COPY", "tmp:0:8", ["const:a7b:8"]]
- 004d8c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8c7c ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 004d8c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c bytes 00ec2991
+ 004d8c7c bytes 00202c91
- 004d8c98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d8c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8c98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d8c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8c98 bytes 087147f9
+ 004d8c98 bytes 08c947f9
- 004d8cdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
- 004d8cdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8cdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:258:8"]]
+ 004d8cdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8cdc bytes 08d540f9
+ 004d8cdc bytes 082d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-365e7cf66af475d1572b12e88e70e597"></a>

### [`004d8d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8d44.md) → [`004d8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8d44.md) _ZN5Botan11Invalid_OIDC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb890.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdb940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb940.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8da8",
      "incomplete_value": true,
      "site": "004d8dac",
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
      "definition_site": "004d8da8",
      "incomplete_value": true,
      "site": "004d8dac",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8dc8",
      "incomplete_value": true,
      "site": "004d8dcc",
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
      "definition_site": "004d8dc8",
      "incomplete_value": true,
      "site": "004d8dcc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8de4",
      "incomplete_value": true,
      "site": "004d8de8",
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
      "definition_site": "004d8de4",
      "incomplete_value": true,
      "site": "004d8de8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d8d60",
      "PARAM",
      [
        "storage",
        "002a960c",
        null,
        "string"
      ]
    ],
    [
      "004d8d78",
      "PARAM",
      [
        "storage",
        "002ae994",
        null,
        "string"
      ]
    ],
    [
      "004d8d8c",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d8d60",
      "PARAM",
      [
        "storage",
        "002a9578",
        null,
        "string"
      ]
    ],
    [
      "004d8d78",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004d8d8c",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8d44.md#insn-004d8d60) · [`004d8d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8d44.md#insn-004d8d78) · [`004d8d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8d44.md#insn-004d8d8c)
- 新版 [`004d8d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8d44.md#insn-004d8d60) · [`004d8d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8d44.md#insn-004d8d78) · [`004d8d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8d44.md#insn-004d8d8c)

~~~diff
- 004d8d60 ["COPY", "tmp:0:8", ["const:60c:8"]]
- 004d8d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8d60 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 004d8d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8d60 bytes 00301891
+ 004d8d60 bytes 00e01591
- 004d8d78 ["COPY", "tmp:0:8", ["const:994:8"]]
- 004d8d78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8d78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8d78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8d78 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 004d8d78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8d78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8d78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8d78 bytes 00502691
+ 004d8d78 bytes 00002491
- 004d8d8c ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d8d8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8d8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8d8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8d8c ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 004d8d8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8d8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8d8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8d8c bytes 21f42091
+ 004d8d8c bytes 21282391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794d338f73b02293fa2dcaf919628fc2"></a>

### [`004d8e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8e54.md) → [`004d8e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8e54.md) _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb860.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdb910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb910.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

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
      "definition_site": "004d8e9c",
      "incomplete_value": true,
      "site": "004d8e9c",
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
      "definition_site": "004d8e9c",
      "incomplete_value": true,
      "site": "004d8e9c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8ed8",
      "incomplete_value": true,
      "site": "004d8edc",
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
      "definition_site": "004d8ed8",
      "incomplete_value": true,
      "site": "004d8edc",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8e74",
      "incomplete_value": false,
      "site": "004d8e84",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8e74",
      "incomplete_value": false,
      "site": "004d8e84",
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
            "const:4d7:8"
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
      "004d8e74",
      "PARAM",
      [
        "storage",
        "002a44d7",
        null,
        "string"
      ]
    ],
    [
      "004d8e90",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "004d8e9c",
      "DATA",
      [
        "storage",
        "00bea368",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d8e74",
      "PARAM",
      [
        "storage",
        "002a44d0",
        null,
        "string"
      ]
    ],
    [
      "004d8e90",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d8e9c",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8e54.md#insn-004d8e74) · [`004d8e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8e54.md#insn-004d8e90) · [`004d8ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8e54.md#insn-004d8ed4)
- 新版 [`004d8e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8e54.md#insn-004d8e74) · [`004d8e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8e54.md#insn-004d8e90) · [`004d8ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8e54.md#insn-004d8ed4)

~~~diff
- 004d8e74 ["COPY", "tmp:0:8", ["const:4d7:8"]]
- 004d8e74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8e74 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 004d8e74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8e74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8e74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 bytes 005c1391
+ 004d8e74 bytes 00401391
- 004d8e90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 004d8e90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8e90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 004d8e90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8e90 bytes 087147f9
+ 004d8e90 bytes 08c947f9
- 004d8ed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b8:8"]]
- 004d8ed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8ed4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
+ 004d8ed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8ed4 bytes 08dd40f9
+ 004d8ed4 bytes 083541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00929cd6ffa34fbf0a574fec2ca5d836"></a>

### [`004d8f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8f3c.md) → [`004d8f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8f3c.md) _ZN5Botan17Self_Test_FailureC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdc8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc8d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d8f90",
      "incomplete_value": true,
      "site": "004d8f94",
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
      "definition_site": "004d8f90",
      "incomplete_value": true,
      "site": "004d8f94",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8f58",
      "incomplete_value": false,
      "site": "004d8f68",
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
            "const:5b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8f58",
      "incomplete_value": false,
      "site": "004d8f68",
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
            "const:524:8"
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
      "004d8f58",
      "PARAM",
      [
        "storage",
        "002a1524",
        null,
        "string"
      ]
    ],
    [
      "004d8f8c",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004d8f94",
      "DATA",
      [
        "storage",
        "00bea638",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d8f58",
      "PARAM",
      [
        "storage",
        "002a15b1",
        null,
        "string"
      ]
    ],
    [
      "004d8f8c",
      "READ",
      [
        "storage",
        "00c1b270",
        null,
        "pointer"
      ]
    ],
    [
      "004d8f94",
      "DATA",
      [
        "storage",
        "00bea6e8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8f3c.md#insn-004d8f58) · [`004d8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8f3c.md#insn-004d8f8c)
- 新版 [`004d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8f3c.md#insn-004d8f58) · [`004d8f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8f3c.md#insn-004d8f8c)

~~~diff
- 004d8f58 ["COPY", "tmp:0:8", ["const:524:8"]]
- 004d8f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d8f58 ["COPY", "tmp:0:8", ["const:5b1:8"]]
+ 004d8f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d8f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 bytes 00901491
+ 004d8f58 bytes 00c41691
- 004d8f8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 004d8f8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d8f8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 004d8f8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d8f8c bytes 08e140f9
+ 004d8f8c bytes 083941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca50fcf8e299317125727df5174d504"></a>

### [`004d8fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8fe8.md) → [`004d8fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8fe8.md) _ZN5Botan15Not_ImplementedC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc590.md) · 呼出先 1件 [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00bdc640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc640.md) · 呼出先 1件 [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d9010",
      "incomplete_value": true,
      "site": "004d9014",
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
      "definition_site": "004d9010",
      "incomplete_value": true,
      "site": "004d9014",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d8ffc",
      "incomplete_value": false,
      "site": "004d9004",
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
            "const:503:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8ffc",
      "incomplete_value": false,
      "site": "004d9004",
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
            "const:476:8"
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
      "004d8ffc",
      "PARAM",
      [
        "storage",
        "0029f476",
        null,
        "string"
      ]
    ],
    [
      "004d900c",
      "READ",
      [
        "storage",
        "00c1b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "004d9014",
      "DATA",
      [
        "storage",
        "00bea660",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004d8ffc",
      "PARAM",
      [
        "storage",
        "0029f503",
        null,
        "string"
      ]
    ],
    [
      "004d900c",
      "READ",
      [
        "storage",
        "00c1b278",
        null,
        "pointer"
      ]
    ],
    [
      "004d9014",
      "DATA",
      [
        "storage",
        "00bea710",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8fe8.md#insn-004d8ffc) · [`004d900c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8fe8.md#insn-004d900c)
- 新版 [`004d8ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8fe8.md#insn-004d8ffc) · [`004d900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8fe8.md#insn-004d900c)

~~~diff
- 004d8ffc ["COPY", "tmp:0:8", ["const:476:8"]]
- 004d8ffc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d8ffc ["COPY", "tmp:0:8", ["const:503:8"]]
+ 004d8ffc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8ffc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d8ffc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc bytes 21d81191
+ 004d8ffc bytes 210c1491
- 004d900c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
- 004d900c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d900c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:278:8"]]
+ 004d900c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d900c bytes 08e540f9
+ 004d900c bytes 083d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9719c2ab8553640ce9521fd2cd3f3593"></a>

### [`004d9024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9024.md) → [`004d9024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9024.md) _ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc8e0.md) · 呼出先 20件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00517044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00517/00517044.md) [`005171dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00517/005171dc.md)
- 新版 呼出元 1件 [`00bdc990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc990.md) · 呼出先 20件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00517044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00517/00517044.md) [`005171dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00517/005171dc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.11% / 新版 99.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004d9248",
      "incomplete_value": false,
      "site": "004d9248",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9248",
      "incomplete_value": false,
      "site": "004d9248",
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
            "const:288:8"
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
      "definition_site": "004d925c",
      "incomplete_value": true,
      "site": "004d925c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d925c",
      "incomplete_value": true,
      "site": "004d925c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d9248",
      "DATA",
      [
        "storage",
        "00bed288",
        null,
        "undefined *"
      ]
    ],
    [
      "004d9258",
      "READ",
      [
        "storage",
        "00c1b1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004d95b4",
      "READ",
      [
        "storage",
        "00bed2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004d9248",
      "DATA",
      [
        "storage",
        "00bed338",
        null,
        "undefined *"
      ]
    ],
    [
      "004d9258",
      "READ",
      [
        "storage",
        "00c1b280",
        null,
        "pointer"
      ]
    ],
    [
      "004d95b4",
      "READ",
      [
        "storage",
        "00bed368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9024.md#insn-004d9240) · [`004d9258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9024.md#insn-004d9258)
- 新版 [`004d9240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9024.md#insn-004d9240) · [`004d9258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9024.md#insn-004d9258)

~~~diff
- 004d9240 ["COPY", "tmp:0:8", ["const:288:8"]]
- 004d9240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004d9240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004d9240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004d9240 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 004d9240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004d9240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004d9240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004d9240 bytes 08210a91
+ 004d9240 bytes 08e10c91
- 004d9258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d0:8"]]
- 004d9258 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d9258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:280:8"]]
+ 004d9258 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9258 bytes 29e940f9
+ 004d9258 bytes 294141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151872620a2b44d67a86f1e65230ca89"></a>

### [`004d989c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d989c.md) → [`004d989c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d989c.md) _ZN5Botan15allocate_memoryEmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc920.md) · 呼出先 5件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdbae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbae0.md) [`00bdbaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbaf0.md)
- 新版 呼出元 1件 [`00bdc9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc9d0.md) · 呼出先 5件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d98d8",
      "incomplete_value": true,
      "site": "004d98e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d98d8",
      "incomplete_value": true,
      "site": "004d98e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d98dc",
      "incomplete_value": true,
      "site": "004d98e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d98dc",
      "incomplete_value": true,
      "site": "004d98e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d98d8",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004d98d8",
      "PARAM",
      [
        "storage",
        "00c167f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d98dc",
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
      "004d98d8",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004d98d8",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004d98dc",
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

- 旧版 [`004d98d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d989c.md#insn-004d98d8) · [`004d98dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d989c.md#insn-004d98dc)
- 新版 [`004d98d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d989c.md#insn-004d98d8) · [`004d98dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d989c.md#insn-004d98dc)

~~~diff
- 004d98d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef8:8"]]
- 004d98d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d98d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 004d98d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d98d8 bytes 217c47f9
+ 004d98d8 bytes 21d447f9
- 004d98dc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:f00:8"]]
- 004d98dc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d98dc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
+ 004d98dc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004d98dc bytes 428047f9
+ 004d98dc bytes 42d847f9
~~~


<a id="compare-8b6e995808cb633fbf902ae46c9078aa"></a>

### [`004d98e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d98e4.md) → [`004d98e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d98e4.md) _ZN5Botan17deallocate_memoryEPvmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc930.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00bdc9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc9e0.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9908",
      "incomplete_value": true,
      "site": "004d9908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d9908",
      "incomplete_value": true,
      "site": "004d9908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d9900",
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
      "004d9900",
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

- 旧版 [`004d9900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d98e4.md#insn-004d9900)
- 新版 [`004d9900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d98e4.md#insn-004d9900)

~~~diff
- 004d9900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:678:8"]]
- 004d9900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d9900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:728:8"]]
+ 004d9900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9900 bytes 083d43f9
+ 004d9900 bytes 089543f9
~~~


<a id="compare-e50f5c690b6c85730d2837b58d36bb57"></a>

### [`004d9940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9940.md) → [`004d9940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9940.md) _ZN5Botan2OS25run_cpu_instruction_probeENSt6__ndk18functionIFivEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`004d9b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9b40.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004d9b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9b40.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d99a0",
      "incomplete_value": false,
      "site": "004d99a8",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d99a0",
      "incomplete_value": false,
      "site": "004d99a8",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d9a2c",
      "incomplete_value": false,
      "site": "004d9a34",
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
            "const:513:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9a2c",
      "incomplete_value": false,
      "site": "004d9a34",
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
            "const:486:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d9a68",
      "incomplete_value": true,
      "site": "004d9a70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d9a68",
      "incomplete_value": true,
      "site": "004d9a70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d99a0",
      "PARAM",
      [
        "storage",
        "00c252d8",
        null,
        null
      ]
    ],
    [
      "004d9a2c",
      "PARAM",
      [
        "storage",
        "0029f486",
        null,
        "string"
      ]
    ],
    [
      "004d9a68",
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
      "004d99a0",
      "PARAM",
      [
        "storage",
        "00c25398",
        null,
        null
      ]
    ],
    [
      "004d9a2c",
      "PARAM",
      [
        "storage",
        "0029f513",
        null,
        "string"
      ]
    ],
    [
      "004d9a68",
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

- 旧版 [`004d99a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9940.md#insn-004d99a0) · [`004d9a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9940.md#insn-004d9a2c) · [`004d9a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9940.md#insn-004d9a68)
- 新版 [`004d99a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9940.md#insn-004d99a0) · [`004d9a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9940.md#insn-004d9a2c) · [`004d9a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9940.md#insn-004d9a68)

~~~diff
- 004d99a0 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 004d99a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d99a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d99a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d99a0 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 004d99a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d99a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d99a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d99a0 bytes 00600b91
+ 004d99a0 bytes 00600e91
- 004d9a2c ["COPY", "tmp:0:8", ["const:486:8"]]
- 004d9a2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d9a2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d9a2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d9a2c ["COPY", "tmp:0:8", ["const:513:8"]]
+ 004d9a2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d9a2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d9a2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d9a2c bytes 21181291
+ 004d9a2c bytes 214c1491
- 004d9a68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 004d9a68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d9a68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 004d9a68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9a68 bytes 214c47f9
+ 004d9a68 bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a9ef408a00d2d6e24ce93d07eff89f0"></a>

### [`004d9b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9b58.md) → [`004d9b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9b58.md) _ZN5Botan9to_uint16ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
      "definition_site": "004d9bbc",
      "incomplete_value": false,
      "site": "004d9bc4",
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
            "const:9a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9bbc",
      "incomplete_value": false,
      "site": "004d9bc4",
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
            "const:91c:8"
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
      "definition_site": "004d9bf8",
      "incomplete_value": true,
      "site": "004d9c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d9bf8",
      "incomplete_value": true,
      "site": "004d9c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d9bbc",
      "PARAM",
      [
        "storage",
        "0029391c",
        null,
        "string"
      ]
    ],
    [
      "004d9bf8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004d9bf8",
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
      "004d9bbc",
      "PARAM",
      [
        "storage",
        "002939a9",
        null,
        "string"
      ]
    ],
    [
      "004d9bf8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004d9bf8",
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

- 旧版 [`004d9bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9b58.md#insn-004d9bbc) · [`004d9bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9b58.md#insn-004d9bf8)
- 新版 [`004d9bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9b58.md#insn-004d9bbc) · [`004d9bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9b58.md#insn-004d9bf8)

~~~diff
- 004d9bbc ["COPY", "tmp:0:8", ["const:91c:8"]]
- 004d9bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d9bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d9bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d9bbc ["COPY", "tmp:0:8", ["const:9a9:8"]]
+ 004d9bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d9bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d9bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d9bbc bytes 21702491
+ 004d9bbc bytes 21a42691
- 004d9bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004d9bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d9bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004d9bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9bf8 bytes 212047f9
+ 004d9bf8 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56484846f9c2cb3903b6983943977e99"></a>

### [`004d9c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9c58.md) → [`004d9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9c58.md) _ZN5Botan18timespec_to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d9e20",
      "incomplete_value": false,
      "site": "004d9e2c",
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
            "const:4dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9e20",
      "incomplete_value": false,
      "site": "004d9e2c",
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
            "const:4e3:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d9e5c",
      "incomplete_value": true,
      "site": "004d9e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004d9e5c",
      "incomplete_value": true,
      "site": "004d9e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d9e20",
      "PARAM",
      [
        "storage",
        "002a44e3",
        null,
        "string"
      ]
    ],
    [
      "004d9e5c",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e5c",
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
      "004d9e20",
      "PARAM",
      [
        "storage",
        "002a44dc",
        null,
        "string"
      ]
    ],
    [
      "004d9e5c",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e5c",
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

- 旧版 [`004d9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9c58.md#insn-004d9e20) · [`004d9e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9c58.md#insn-004d9e5c)
- 新版 [`004d9e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9c58.md#insn-004d9e20) · [`004d9e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9c58.md#insn-004d9e5c)

~~~diff
- 004d9e20 ["COPY", "tmp:0:8", ["const:4e3:8"]]
- 004d9e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d9e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d9e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d9e20 ["COPY", "tmp:0:8", ["const:4dc:8"]]
+ 004d9e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d9e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d9e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d9e20 bytes 008c1391
+ 004d9e20 bytes 00701391
- 004d9e5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004d9e5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004d9e5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004d9e5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9e5c bytes 213047f9
+ 004d9e5c bytes 218847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde3ea8f4444773659bd7da1a67551fd"></a>

### [`004d9ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9ed0.md) → [`004d9ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9ed0.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc060.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051dea4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bdc110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc110.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051dea4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004da0e0",
      "incomplete_value": false,
      "site": "004da0ec",
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
            "const:4c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da0e0",
      "incomplete_value": false,
      "site": "004da0ec",
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
            "const:43a:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004da11c",
      "incomplete_value": true,
      "site": "004da128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004da11c",
      "incomplete_value": true,
      "site": "004da128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004da0e0",
      "PARAM",
      [
        "storage",
        "0029d43a",
        null,
        "string"
      ]
    ],
    [
      "004da11c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004da11c",
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
      "004da0e0",
      "PARAM",
      [
        "storage",
        "0029d4c7",
        null,
        "string"
      ]
    ],
    [
      "004da11c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004da11c",
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

- 旧版 [`004da0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9ed0.md#insn-004da0e0) · [`004da11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d9/004d9ed0.md#insn-004da11c)
- 新版 [`004da0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9ed0.md#insn-004da0e0) · [`004da11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9ed0.md#insn-004da11c)

~~~diff
- 004da0e0 ["COPY", "tmp:0:8", ["const:43a:8"]]
- 004da0e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004da0e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004da0e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004da0e0 ["COPY", "tmp:0:8", ["const:4c7:8"]]
+ 004da0e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004da0e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004da0e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004da0e0 bytes 00e81091
+ 004da0e0 bytes 001c1391
- 004da11c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004da11c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004da11c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004da11c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004da11c bytes 212047f9
+ 004da11c bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1789ec56c489672ccbfc5b4c915675be"></a>

### [`004da474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004da474.md) → [`004da474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004da474.md) _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc9b0.md) · 呼出先 11件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c98.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca60.md) · 呼出先 11件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004da498",
      "incomplete_value": false,
      "site": "004da4ac",
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
      "definition_site": "004da498",
      "incomplete_value": false,
      "site": "004da4ac",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004da5c4",
      "incomplete_value": false,
      "site": "004da5d0",
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
            "const:3d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da5c4",
      "incomplete_value": false,
      "site": "004da5d0",
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
            "const:3e0:8"
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
    "new": {
      "definition_site": "004da600",
      "incomplete_value": true,
      "site": "004da60c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004da600",
      "incomplete_value": true,
      "site": "004da60c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004da4ac",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004da4e8",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004da4e8",
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
      "004da4ac",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004da4e8",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004da4e8",
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

- 旧版 [`004da498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004da474.md#insn-004da498) · [`004da5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004da474.md#insn-004da5c4) · [`004da600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004da474.md#insn-004da600)
- 新版 [`004da498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004da474.md#insn-004da498) · [`004da5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004da474.md#insn-004da5c4) · [`004da600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004da474.md#insn-004da600)

~~~diff
- 004da498 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004da498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004da498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004da498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004da498 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 004da498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004da498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004da498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004da498 bytes 29c11791
+ 004da498 bytes 29811a91
- 004da5c4 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 004da5c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004da5c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004da5c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004da5c4 ["COPY", "tmp:0:8", ["const:3d9:8"]]
+ 004da5c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004da5c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004da5c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004da5c4 bytes 00800f91
+ 004da5c4 bytes 00640f91
- 004da600 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e60:8"]]
- 004da600 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004da600 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
+ 004da600 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004da600 bytes 213047f9
+ 004da600 bytes 218847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3674cabd30360aeb6be2bad7b484e8b"></a>

### [`004daaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004daaa4.md) → [`004daaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004daaa4.md) _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc9d0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`0041f280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00bdca80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca80.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004daf1c",
      "incomplete_value": false,
      "site": "004daf28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:7bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004daf1c",
      "incomplete_value": false,
      "site": "004daf28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:7c6:8"
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
      "definition_site": "004daf70",
      "incomplete_value": false,
      "site": "004daf7c",
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
      "definition_site": "004daf70",
      "incomplete_value": false,
      "site": "004daf7c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004daff0",
      "incomplete_value": false,
      "site": "004daff8",
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
      "definition_site": "004daff0",
      "incomplete_value": false,
      "site": "004daff8",
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
      "004daf1c",
      "PARAM",
      [
        "storage",
        "002a67c6",
        null,
        null
      ]
    ],
    [
      "004daf70",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004daff0",
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
      "004daf1c",
      "PARAM",
      [
        "storage",
        "002a67bf",
        null,
        null
      ]
    ],
    [
      "004daf70",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "004daff0",
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

- 旧版 [`004daf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004daaa4.md#insn-004daf1c) · [`004daf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004daaa4.md#insn-004daf70) · [`004daff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004da/004daaa4.md#insn-004daff0)
- 新版 [`004daf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004daaa4.md#insn-004daf1c) · [`004daf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004daaa4.md#insn-004daf70) · [`004daff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004da/004daaa4.md#insn-004daff0)

~~~diff
- 004daf1c ["COPY", "tmp:0:8", ["const:7c6:8"]]
- 004daf1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004daf1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004daf1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004daf1c ["COPY", "tmp:0:8", ["const:7bf:8"]]
+ 004daf1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004daf1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004daf1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004daf1c bytes 21181f91
+ 004daf1c bytes 21fc1e91
- 004daf70 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004daf70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004daf70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004daf70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004daf70 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004daf70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004daf70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004daf70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004daf70 bytes 21641f91
+ 004daf70 bytes 21982191
- 004daff0 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 004daff0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004daff0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004daff0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004daff0 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 004daff0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004daff0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004daff0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004daff0 bytes 21641f91
+ 004daff0 bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8abb206108737c4b0f530b62b026728e"></a>

### [`004db550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004db550.md) → [`004db550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004db550.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00471da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471da4.md) [`00483974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00471da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471da4.md) [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004db9b0",
      "incomplete_value": false,
      "site": "004db9bc",
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
            "const:b29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004db9b0",
      "incomplete_value": false,
      "site": "004db9bc",
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
            "const:a9c:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dba34",
      "incomplete_value": true,
      "site": "004dba40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004dba34",
      "incomplete_value": true,
      "site": "004dba40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004db608",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004db63c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004db9b0",
      "PARAM",
      [
        "storage",
        "00295a9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004db608",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "004db63c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004db9b0",
      "PARAM",
      [
        "storage",
        "00295b29",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004db608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004db550.md#insn-004db608) · [`004db9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004db550.md#insn-004db9b0) · [`004dba34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004db550.md#insn-004dba34)
- 新版 [`004db608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004db550.md#insn-004db608) · [`004db9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004db550.md#insn-004db9b0) · [`004dba34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004db550.md#insn-004dba34)

~~~diff
- 004db608 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d40:8"]]
- 004db608 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004db608 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:df0:8"]]
+ 004db608 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 004db608 bytes d6a246f9
+ 004db608 bytes d6fa46f9
- 004db9b0 ["COPY", "tmp:0:8", ["const:a9c:8"]]
- 004db9b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004db9b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004db9b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004db9b0 ["COPY", "tmp:0:8", ["const:b29:8"]]
+ 004db9b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004db9b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004db9b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004db9b0 bytes 00702a91
+ 004db9b0 bytes 00a42c91
- 004dba34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 004dba34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dba34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 004dba34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004dba34 bytes 214c47f9
+ 004dba34 bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d521e64e756b15a6b781931d39b738eb"></a>

### [`004dbc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc40.md) → [`004dbc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc40.md) _ZN5Botan18short_version_cstrEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004dbc44",
      "incomplete_value": false,
      "site": "004dbc48",
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
            "const:53e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc44",
      "incomplete_value": false,
      "site": "004dbc48",
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
            "const:4b1:8"
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
      "004dbc44",
      "DATA",
      [
        "storage",
        "0029f4b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004dbc44",
      "DATA",
      [
        "storage",
        "0029f53e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc40.md#insn-004dbc44)
- 新版 [`004dbc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc40.md#insn-004dbc44)

~~~diff
- 004dbc44 ["COPY", "tmp:0:8", ["const:4b1:8"]]
- 004dbc44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004dbc44 ["COPY", "tmp:0:8", ["const:53e:8"]]
+ 004dbc44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004dbc44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004dbc44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 bytes 00c41291
+ 004dbc44 bytes 00f81491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f1338c3afbf8190a0b82612fc6b409"></a>

### [`004dbc4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc4c.md) → [`004dbc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc4c.md) _ZN5Botan12version_cstrEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004dbc50",
      "incomplete_value": false,
      "site": "004dbc54",
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
            "const:66b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc50",
      "incomplete_value": false,
      "site": "004dbc54",
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
            "const:665:8"
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
      "004dbc50",
      "DATA",
      [
        "storage",
        "002ab665",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004dbc50",
      "DATA",
      [
        "storage",
        "002ab66b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc4c.md#insn-004dbc50)
- 新版 [`004dbc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc4c.md#insn-004dbc50)

~~~diff
- 004dbc50 ["COPY", "tmp:0:8", ["const:665:8"]]
- 004dbc50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004dbc50 ["COPY", "tmp:0:8", ["const:66b:8"]]
+ 004dbc50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004dbc50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004dbc50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 bytes 00941991
+ 004dbc50 bytes 00ac1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f31803ea8efbd8cc8968904d20a1b2"></a>

### [`004dbc58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc58.md) → [`004dbc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc58.md) _ZN5Botan14version_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004dbc94",
      "incomplete_value": true,
      "site": "004dbc98",
      "value": [
        "LOAD",
        "16",
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
                "const:60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc94",
      "incomplete_value": true,
      "site": "004dbc98",
      "value": [
        "LOAD",
        "16",
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
                "const:60:8"
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
      "004dbc7c",
      "READ",
      [
        "storage",
        "002ab6a5",
        null,
        "string"
      ]
    ],
    [
      "004dbc7c",
      "READ",
      [
        "storage",
        "002ab6b5",
        null,
        "string"
      ]
    ],
    [
      "004dbc84",
      "READ",
      [
        "storage",
        "002ab6d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004dbc7c",
      "READ",
      [
        "storage",
        "002ab6ab",
        null,
        "string"
      ]
    ],
    [
      "004dbc7c",
      "READ",
      [
        "storage",
        "002ab6bb",
        null,
        "string"
      ]
    ],
    [
      "004dbc84",
      "READ",
      [
        "storage",
        "002ab6d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc58.md#insn-004dbc74) · [`004dbc78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbc58.md#insn-004dbc78)
- 新版 [`004dbc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc58.md#insn-004dbc74) · [`004dbc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbc58.md#insn-004dbc78)

~~~diff
- 004dbc74 ["COPY", "tmp:0:8", ["const:665:8"]]
- 004dbc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004dbc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004dbc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004dbc74 ["COPY", "tmp:0:8", ["const:66b:8"]]
+ 004dbc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004dbc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004dbc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004dbc74 bytes 08951991
+ 004dbc74 bytes 08ad1991
- 004dbc78 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004dbc78 bytes a9eeffd0
+ 004dbc78 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004dbc78 bytes a9eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a8449ef9000f07926376528992a1fd"></a>

### [`004dbd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbd04.md) → [`004dbd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbd04.md) _ZN5Botan21runtime_version_checkEjjj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dbd4c",
      "incomplete_value": true,
      "site": "004dbd5c",
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
      "definition_site": "004dbd4c",
      "incomplete_value": true,
      "site": "004dbd5c",
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
      "definition_site": "004dbd54",
      "incomplete_value": true,
      "site": "004dbd64",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbd54",
      "incomplete_value": true,
      "site": "004dbd64",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004dbd6c",
      "incomplete_value": true,
      "site": "004dbd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "004dbd6c",
      "incomplete_value": true,
      "site": "004dbd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "004dbd38",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "004dbd3c",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "004dbd54",
      "READ",
      [
        "storage",
        "00c13360",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004dbd38",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004dbd3c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004dbd54",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbd04.md#insn-004dbd38) · [`004dbd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbd04.md#insn-004dbd3c) · [`004dbdb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbd04.md#insn-004dbdb4)
- 新版 [`004dbd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbd04.md#insn-004dbd38) · [`004dbd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbd04.md#insn-004dbd3c) · [`004dbdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbd04.md#insn-004dbdb4)

~~~diff
- 004dbd38 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d98:8"]]
- 004dbd38 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dbd38 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
+ 004dbd38 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 004dbd38 bytes 7bcf46f9
+ 004dbd38 bytes 7b2747f9
- 004dbd3c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cc8:8"]]
- 004dbd3c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dbd3c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d78:8"]]
+ 004dbd3c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 004dbd3c bytes 5a6746f9
+ 004dbd3c bytes 5abf46f9
- 004dbdb4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:cd0:8"]]
- 004dbdb4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dbdb4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d80:8"]]
+ 004dbdb4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 004dbdb4 bytes f76a46f9
+ 004dbdb4 bytes f7c246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a859ba0e50ca06d7d20e4fe4ac35d95"></a>

### [`004dbf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbf98.md) → [`004dbf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbf98.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbc0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdca00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca00.md)
- 新版 呼出元 1件 [`00bdcc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc70.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dbfe4",
      "incomplete_value": true,
      "site": "004dc00c",
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
      "definition_site": "004dbfe4",
      "incomplete_value": true,
      "site": "004dc00c",
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
      "004dbfc8",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "004dc00c",
      "DATA",
      [
        "storage",
        "00bea6a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004dbfc8",
      "READ",
      [
        "storage",
        "00c1b288",
        null,
        "pointer"
      ]
    ],
    [
      "004dc00c",
      "DATA",
      [
        "storage",
        "00bea758",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbfc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbf98.md#insn-004dbfc8)
- 新版 [`004dbfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbf98.md#insn-004dbfc8)

~~~diff
- 004dbfc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
- 004dbfc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dbfc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
+ 004dbfc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004dbfc8 bytes 29ed40f9
+ 004dbfc8 bytes 294541f9
~~~


<a id="compare-aac0dc8c46657c9dbb44131fabdc9f16"></a>

### [`004dcbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcbd4.md) → [`004dcbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md) FUN_004dcbd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004dc960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc960.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e5/004e56e4.md) [`004f1ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f1/004f1ecc.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`005251c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/005251c0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`004dc960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc960.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e5/004e56e4.md) [`004f1ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f1/004f1ecc.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`005251c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005251c0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
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
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dcc4c",
      "incomplete_value": true,
      "site": "004dcc60",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dcc4c",
      "incomplete_value": true,
      "site": "004dcc60",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
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
      "004dcc30",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "004dcc48",
      "READ",
      [
        "storage",
        "00c13240",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004dcc4c",
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
      "004dcc30",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "004dcc48",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004dcc4c",
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

- 旧版 [`004dcc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcbd4.md#insn-004dcc30) · [`004dcc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcbd4.md#insn-004dcc5c)
- 新版 [`004dcc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md#insn-004dcc30) · [`004dcc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcbd4.md#insn-004dcc5c)

~~~diff
- 004dcc30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 004dcc30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dcc30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004dcc30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dcc30 bytes 089146f9
+ 004dcc30 bytes 08e946f9
- 004dcc5c ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 004dcc5c bytes e93900d0
+ 004dcc5c ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004dcc5c bytes e93900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d650487f5904346cfe1af6d8e75658"></a>

### [`004dcf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcf48.md) → [`004dcf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md) _ZN5Botan15AlternativeName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004dc4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc4a4.md) [`004e40b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e4/004e40b8.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004dc4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc4a4.md) [`004e40b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e4/004e40b8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.29% / 新版 96.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 7件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dcfb8",
      "incomplete_value": true,
      "site": "004dcfbc",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dcfb8",
      "incomplete_value": true,
      "site": "004dcfbc",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
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
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
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
      "004dcf9c",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "004dcfb4",
      "READ",
      [
        "storage",
        "00c13240",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004dcfb8",
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
      "004dcf9c",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "004dcfb4",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004dcfb8",
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

- 旧版 [`004dcf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcf48.md#insn-004dcf9c) · [`004dcfe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcf48.md#insn-004dcfe4) · [`004dcfe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dcf48.md#insn-004dcfe8)
- 新版 [`004dcf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md#insn-004dcf9c) · [`004dcfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md#insn-004dcfe4) · [`004dcfe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dcf48.md#insn-004dcfe8)

~~~diff
- 004dcf9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 004dcf9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dcf9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004dcf9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dcf9c bytes 089146f9
+ 004dcf9c bytes 08e946f9
- 004dcfe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004dcfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dcfe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004dcfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dcfe4 bytes 08f140f9
+ 004dcfe4 bytes 084941f9
- 004dcfe8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cd0:8"]]
- 004dcfe8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dcfe8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
+ 004dcfe8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004dcfe8 bytes 296946f9
+ 004dcfe8 bytes 29c146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-028ffd42fb84de1a431af85915024ea6"></a>

### [`004ddc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dd/004ddc24.md) → [`004ddc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dd/004ddc24.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_7X509_DNE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdca50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca50.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdcb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb00.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ddf64",
      "incomplete_value": false,
      "site": "004ddf6c",
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
      "definition_site": "004ddf64",
      "incomplete_value": false,
      "site": "004ddf6c",
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
      "004dde90",
      "PARAM",
      [
        "storage",
        "002a82fc",
        null,
        null
      ]
    ],
    [
      "004ddee4",
      "PARAM",
      [
        "storage",
        "00296b41",
        null,
        null
      ]
    ],
    [
      "004ddf14",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004dde90",
      "PARAM",
      [
        "storage",
        "002a8268",
        null,
        null
      ]
    ],
    [
      "004ddee4",
      "PARAM",
      [
        "storage",
        "00296bce",
        null,
        null
      ]
    ],
    [
      "004ddf14",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dd/004ddc24.md#insn-004ddc80) · [`004ddc88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dd/004ddc24.md#insn-004ddc88)
- 新版 [`004ddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dd/004ddc24.md#insn-004ddc80) · [`004ddc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dd/004ddc24.md#insn-004ddc88)

~~~diff
- 004ddc80 ["COPY", "tmp:0:8", ["const:2fc:8"]]
- 004ddc80 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004ddc80 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004ddc80 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004ddc80 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 004ddc80 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004ddc80 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004ddc80 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004ddc80 bytes 94f20b91
+ 004ddc80 bytes 94a20991
- 004ddc88 ["COPY", "register:40a8:8", ["const:2a5000:8"]]
- 004ddc88 bytes 55eeff90
+ 004ddc88 ["COPY", "register:40a8:8", ["const:2a5000:8"]]
+ 004ddc88 bytes 55eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59b9e42e423cb792ca8ea5b9da034e4"></a>

### [`004de068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de068.md) → [`004de068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de068.md) _ZN5Botan9to_stringENS_23Certificate_Status_CodeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca70.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdcb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 84.19% / 新版 84.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004de0bc",
      "incomplete_value": false,
      "site": "004de0c0",
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
            "const:54f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de0bc",
      "incomplete_value": false,
      "site": "004de0c0",
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
            "const:4c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004de0f8",
      "incomplete_value": false,
      "site": "004de0fc",
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
            "const:a77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de0f8",
      "incomplete_value": false,
      "site": "004de0fc",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004de12c",
      "incomplete_value": false,
      "site": "004de130",
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
            "const:b7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de12c",
      "incomplete_value": false,
      "site": "004de130",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004de0bc",
      "DATA",
      [
        "storage",
        "0029f4c2",
        null,
        "string"
      ]
    ],
    [
      "004de0f8",
      "DATA",
      [
        "storage",
        "002ada80",
        null,
        "string"
      ]
    ],
    [
      "004de12c",
      "DATA",
      [
        "storage",
        "00296af1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004de0bc",
      "DATA",
      [
        "storage",
        "0029f54f",
        null,
        "string"
      ]
    ],
    [
      "004de0f8",
      "DATA",
      [
        "storage",
        "002ada77",
        null,
        "string"
      ]
    ],
    [
      "004de12c",
      "DATA",
      [
        "storage",
        "00296b7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de068.md#insn-004de0bc) · [`004de0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de068.md#insn-004de0f8) · [`004de12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de068.md#insn-004de12c)
- 新版 [`004de0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de068.md#insn-004de0bc) · [`004de0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de068.md#insn-004de0f8) · [`004de12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de068.md#insn-004de12c)

~~~diff
- 004de0bc ["COPY", "tmp:0:8", ["const:4c2:8"]]
- 004de0bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004de0bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004de0bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004de0bc ["COPY", "tmp:0:8", ["const:54f:8"]]
+ 004de0bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004de0bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004de0bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004de0bc bytes 00081391
+ 004de0bc bytes 003c1591
- 004de0f8 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 004de0f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004de0f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004de0f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004de0f8 ["COPY", "tmp:0:8", ["const:a77:8"]]
+ 004de0f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004de0f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004de0f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004de0f8 bytes 00002a91
+ 004de0f8 bytes 00dc2991
- 004de12c ["COPY", "tmp:0:8", ["const:af1:8"]]
- 004de12c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004de12c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004de12c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004de12c ["COPY", "tmp:0:8", ["const:b7e:8"]]
+ 004de12c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004de12c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004de12c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004de12c bytes 00c42b91
+ 004de12c bytes 00f82d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dada51c2aaf6cc19cf9bb7eab77a8ed"></a>

### [`004de4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de4b0.md) → [`004de4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de4b0.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdca80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca80.md) · 呼出先 10件 [`00518128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518128.md) [`005254d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/005254d0.md) [`005254e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/005254e0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bdcb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb30.md) · 呼出先 10件 [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`005254d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005254d0.md) [`005254e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005254e0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "004de58c",
      "incomplete_value": true,
      "site": "004de590",
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
      "definition_site": "004de58c",
      "incomplete_value": true,
      "site": "004de590",
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
      "definition_site": "004de5a8",
      "incomplete_value": true,
      "site": "004de5b0",
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
      "definition_site": "004de5a8",
      "incomplete_value": true,
      "site": "004de5b0",
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
      "004de584",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004de590",
      "DATA",
      [
        "storage",
        "00bed680",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004de5a4",
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
      "004de584",
      "READ",
      [
        "storage",
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "004de590",
      "DATA",
      [
        "storage",
        "00bed730",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004de5a4",
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

- 旧版 [`004de584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de4b0.md#insn-004de584) · [`004de5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de4b0.md#insn-004de5a4)
- 新版 [`004de584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de4b0.md#insn-004de584) · [`004de5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de4b0.md#insn-004de5a4)

~~~diff
- 004de584 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
- 004de584 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de584 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
+ 004de584 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004de584 bytes 08f540f9
+ 004de584 bytes 084d41f9
- 004de5a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004de5a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de5a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004de5a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004de5a4 bytes 08f940f9
+ 004de5a4 bytes 085141f9
~~~


<a id="compare-ec47892a80803003bba8d9aefc9779cd"></a>

### [`004def78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004def78.md) → [`004def78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004def78.md) _ZNK5Botan27Certificate_Store_In_Memory24find_cert_by_pubkey_sha1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004df190",
      "incomplete_value": false,
      "site": "004df198",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004df190",
      "incomplete_value": false,
      "site": "004df198",
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
            "const:310:8"
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
      "definition_site": "004df1c8",
      "incomplete_value": true,
      "site": "004df1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004df1c8",
      "incomplete_value": true,
      "site": "004df1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004df190",
      "PARAM",
      [
        "storage",
        "002a2310",
        null,
        "string"
      ]
    ],
    [
      "004df1c8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004df1c8",
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
      "004df190",
      "PARAM",
      [
        "storage",
        "002a239d",
        null,
        "string"
      ]
    ],
    [
      "004df1c8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004df1c8",
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

- 旧版 [`004df190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004def78.md#insn-004df190) · [`004df1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004def78.md#insn-004df1c8)
- 新版 [`004df190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004def78.md#insn-004df190) · [`004df1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004def78.md#insn-004df1c8)

~~~diff
- 004df190 ["COPY", "tmp:0:8", ["const:310:8"]]
- 004df190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004df190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004df190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004df190 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 004df190 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004df190 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004df190 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004df190 bytes 21400c91
+ 004df190 bytes 21740e91
- 004df1c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004df1c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004df1c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004df1c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004df1c8 bytes 212047f9
+ 004df1c8 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72231d2031e186a81937614c37f5e91d"></a>

### [`004df290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df290.md) → [`004df290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df290.md) _ZNK5Botan27Certificate_Store_In_Memory34find_cert_by_raw_subject_dn_sha256ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004df4b0",
      "incomplete_value": false,
      "site": "004df4b8",
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
            "const:b59:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004df4b0",
      "incomplete_value": false,
      "site": "004df4b8",
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
            "const:acc:8"
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
      "definition_site": "004df4e8",
      "incomplete_value": true,
      "site": "004df4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004df4e8",
      "incomplete_value": true,
      "site": "004df4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004df4b0",
      "PARAM",
      [
        "storage",
        "00295acc",
        null,
        "string"
      ]
    ],
    [
      "004df4e8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004df4e8",
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
      "004df4b0",
      "PARAM",
      [
        "storage",
        "00295b59",
        null,
        "string"
      ]
    ],
    [
      "004df4e8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004df4e8",
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

- 旧版 [`004df4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df290.md#insn-004df4b0) · [`004df4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df290.md#insn-004df4e8)
- 新版 [`004df4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df290.md#insn-004df4b0) · [`004df4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df290.md#insn-004df4e8)

~~~diff
- 004df4b0 ["COPY", "tmp:0:8", ["const:acc:8"]]
- 004df4b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004df4b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004df4b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004df4b0 ["COPY", "tmp:0:8", ["const:b59:8"]]
+ 004df4b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004df4b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004df4b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004df4b0 bytes 21302b91
+ 004df4b0 bytes 21642d91
- 004df4e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 004df4e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004df4e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 004df4e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004df4e8 bytes 212047f9
+ 004df4e8 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce9f8150102deda2d289529d16d782a0"></a>

### [`004df5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df5b0.md) → [`004df5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df5b0.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlERKNS_8X509_CRLE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00518128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/00518128.md) [`00525bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525bf0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00525bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525bf0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

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
      "definition_site": "004df5f8",
      "incomplete_value": true,
      "site": "004df5fc",
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
      "definition_site": "004df5f8",
      "incomplete_value": true,
      "site": "004df5fc",
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
      "definition_site": "004df614",
      "incomplete_value": true,
      "site": "004df61c",
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
      "definition_site": "004df614",
      "incomplete_value": true,
      "site": "004df61c",
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
      "004df5f0",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "004df5fc",
      "DATA",
      [
        "storage",
        "00bed6d0",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004df610",
      "READ",
      [
        "storage",
        "00c1b200",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004df5f0",
      "READ",
      [
        "storage",
        "00c1b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "004df5fc",
      "DATA",
      [
        "storage",
        "00bed780",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "004df610",
      "READ",
      [
        "storage",
        "00c1b2b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df5b0.md#insn-004df5f0) · [`004df610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df5b0.md#insn-004df610)
- 新版 [`004df5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df5b0.md#insn-004df5f0) · [`004df610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df5b0.md#insn-004df610)

~~~diff
- 004df5f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
- 004df5f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004df5f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
+ 004df5f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004df5f0 bytes 08fd40f9
+ 004df5f0 bytes 085541f9
- 004df610 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 004df610 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004df610 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 004df610 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004df610 bytes 080141f9
+ 004df610 bytes 085941f9
~~~


<a id="compare-d4b735ad5bfce9684303a9b654def545"></a>

### [`004df920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df920.md) → [`004df920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df920.md) FUN_004df920

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004de868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de868.md) [`004df724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df724.md) [`0050645c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/00506ee0.md) [`0052581c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/0052581c.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00517bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00517/00517bcc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 5件 [`004de868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de868.md) [`004df724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df724.md) [`0050645c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/00506ee0.md) [`0052581c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/0052581c.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00517bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00517/00517bcc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

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
      "definition_site": "004df960",
      "incomplete_value": true,
      "site": "004df968",
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
      "definition_site": "004df960",
      "incomplete_value": true,
      "site": "004df968",
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
      "004df950",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "004df968",
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
      "004df950",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "004df968",
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

- 旧版 [`004df950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df920.md#insn-004df950)
- 新版 [`004df950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df920.md#insn-004df950)

~~~diff
- 004df950 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 004df950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004df950 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 004df950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004df950 bytes 08f140f9
+ 004df950 bytes 084941f9
~~~


<a id="compare-61eb5d5cb9e82623c31640f9e773a688"></a>

### [`004dfc64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfc64.md) → [`004dfc64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfc64.md) _ZN5Botan27Certificate_Store_In_MemoryC2ERKNS_16X509_CertificateE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdca80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdcb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dfc88",
      "incomplete_value": true,
      "site": "004dfc8c",
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
      "definition_site": "004dfc88",
      "incomplete_value": true,
      "site": "004dfc8c",
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
      "004dfc80",
      "READ",
      [
        "storage",
        "00c1b208",
        null,
        "pointer"
      ]
    ],
    [
      "004dfc8c",
      "DATA",
      [
        "storage",
        "00bea6d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004dfc80",
      "READ",
      [
        "storage",
        "00c1b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "004dfc8c",
      "DATA",
      [
        "storage",
        "00bea788",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dfc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfc64.md#insn-004dfc80) · [`004dfc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfc64.md#insn-004dfc84)
- 新版 [`004dfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfc64.md#insn-004dfc80) · [`004dfc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfc64.md#insn-004dfc84)

~~~diff
- 004dfc80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:208:8"]]
- 004dfc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dfc80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
+ 004dfc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dfc80 bytes 080541f9
+ 004dfc80 bytes 085d41f9
- 004dfc84 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004dfc84 bytes f40300aa
+ 004dfc84 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 004dfc84 bytes f40300aa
~~~


<a id="compare-f2e4743bcb172cac1337c1c072cf57df"></a>

### [`004dfd64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfd64.md) → [`004dfd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfd64.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005254e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/005254e0.md) [`00525ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525ea0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005254e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005254e0.md) [`00525ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525ea0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dfd9c",
      "incomplete_value": true,
      "site": "004dfda4",
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
      "definition_site": "004dfd9c",
      "incomplete_value": true,
      "site": "004dfda4",
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
      "004dfd90",
      "READ",
      [
        "storage",
        "00c1b208",
        null,
        "pointer"
      ]
    ],
    [
      "004dfda4",
      "DATA",
      [
        "storage",
        "00bea6d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004dfdec",
      "READ",
      [
        "storage",
        "00c1b210",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004dfd90",
      "READ",
      [
        "storage",
        "00c1b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "004dfda4",
      "DATA",
      [
        "storage",
        "00bea788",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004dfdec",
      "READ",
      [
        "storage",
        "00c1b2c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dfd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfd64.md#insn-004dfd90) · [`004dfdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004dfd64.md#insn-004dfdec)
- 新版 [`004dfd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfd64.md#insn-004dfd90) · [`004dfdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfd64.md#insn-004dfdec)

~~~diff
- 004dfd90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:208:8"]]
- 004dfd90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dfd90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
+ 004dfd90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dfd90 bytes 080541f9
+ 004dfd90 bytes 085d41f9
- 004dfdec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:210:8"]]
- 004dfdec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004dfdec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
+ 004dfdec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dfdec bytes 080941f9
+ 004dfdec bytes 086141f9
~~~


<a id="compare-24ffcdcfe00d10db421e485862dbf2ae"></a>

### [`004e0038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0038.md) → [`004e0038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0038.md) _ZN5Botan9CRL_EntryC1ERKNS_16X509_CertificateENS_8CRL_CodeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00525f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525f90.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb630.md) [`00bdcaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcaa0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00525f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525f90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6e0.md) [`00bdcb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

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
      "definition_site": "004e0070",
      "incomplete_value": true,
      "site": "004e0078",
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
      "definition_site": "004e0070",
      "incomplete_value": true,
      "site": "004e0078",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e00a4",
      "incomplete_value": true,
      "site": "004e00a4",
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
      "definition_site": "004e00a4",
      "incomplete_value": true,
      "site": "004e00a4",
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
      "definition_site": "004e00c8",
      "incomplete_value": true,
      "site": "004e00c8",
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
      "definition_site": "004e00c8",
      "incomplete_value": true,
      "site": "004e00c8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e0060",
      "READ",
      [
        "storage",
        "00c1b218",
        null,
        "pointer"
      ]
    ],
    [
      "004e0078",
      "DATA",
      [
        "storage",
        "00bea728",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e0094",
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
      "004e0060",
      "READ",
      [
        "storage",
        "00c1b2c8",
        null,
        "pointer"
      ]
    ],
    [
      "004e0078",
      "DATA",
      [
        "storage",
        "00bea7d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e0094",
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

- 旧版 [`004e0060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0038.md#insn-004e0060) · [`004e0094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0038.md#insn-004e0094) · [`004e00b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e0/004e0038.md#insn-004e00b4)
- 新版 [`004e0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0038.md#insn-004e0060) · [`004e0094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0038.md#insn-004e0094) · [`004e00b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0038.md#insn-004e00b4)

~~~diff
- 004e0060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:218:8"]]
- 004e0060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c8:8"]]
+ 004e0060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0060 bytes 290d41f9
+ 004e0060 bytes 296541f9
- 004e0094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 004e0094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004e0094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0094 bytes 086147f9
+ 004e0094 bytes 08b947f9
- 004e00b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
- 004e00b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e00b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
+ 004e00b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e00b4 bytes 081141f9
+ 004e00b4 bytes 086941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

