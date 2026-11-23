# v15.7.2 → v15.7.3 · 最優先の変更候補 (42)

[一覧の目次](README.md)

<a id="compare-928d9df4ddc37152754b841b28ea3a2a"></a>

### [`0085c704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c704.md) → [`0085c704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md) FUN_0085c704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db3c.md) [`0085cc88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cc88.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0085cc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc88.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085c738",
      "incomplete_value": true,
      "site": "0085c748",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c738",
      "incomplete_value": true,
      "site": "0085c748",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cdd:8"
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
      "definition_site": "0085c74c",
      "incomplete_value": true,
      "site": "0085c74c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085c74c",
      "incomplete_value": true,
      "site": "0085c74c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085c888",
      "incomplete_value": false,
      "site": "0085c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c888",
      "incomplete_value": false,
      "site": "0085c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0085c738",
      "READ",
      [
        "storage",
        "00294cdd",
        null,
        "string"
      ]
    ],
    [
      "0085c73c",
      "READ",
      [
        "storage",
        "00294cec",
        null,
        "string"
      ]
    ],
    [
      "0085c888",
      "DATA",
      [
        "storage",
        "00c03930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c738",
      "READ",
      [
        "storage",
        "00294d6a",
        null,
        "string"
      ]
    ],
    [
      "0085c73c",
      "READ",
      [
        "storage",
        "00294d79",
        null,
        "string"
      ]
    ],
    [
      "0085c888",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c704.md#insn-0085c730) · [`0085c734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c704.md#insn-0085c734)
- 新版 [`0085c730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md#insn-0085c730) · [`0085c734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md#insn-0085c734)

~~~diff
- 0085c730 ["COPY", "tmp:0:8", ["const:cdd:8"]]
- 0085c730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["COPY", "tmp:0:8", ["const:d6a:8"]]
+ 0085c730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c730 bytes 08753391
+ 0085c730 bytes 08a93591
- 0085c734 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0085c734 bytes a9d2ff90
+ 0085c734 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0085c734 bytes a9d2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fcd6f89ac05afd66d273066a10cca5"></a>

### [`0085cb4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cb4c.md) → [`0085cb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cb4c.md) FUN_0085cb4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0085cb60",
      "incomplete_value": false,
      "site": "0085cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cb60",
      "incomplete_value": false,
      "site": "0085cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0085cb64",
      "DATA",
      [
        "storage",
        "00c03930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cb64",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cb4c.md#insn-0085cb60)
- 新版 [`0085cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cb4c.md#insn-0085cb60)

~~~diff
- 0085cb60 ["COPY", "tmp:0:8", ["const:930:8"]]
- 0085cb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0085cb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 bytes 08c12491
+ 0085cb60 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41168f389c73a5d268870ce3403e728c"></a>

### [`0085cba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cba8.md) → [`0085cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cba8.md) FUN_0085cba8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0085cbc0",
      "incomplete_value": false,
      "site": "0085cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cbc0",
      "incomplete_value": false,
      "site": "0085cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0085cbc4",
      "DATA",
      [
        "storage",
        "00c03930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cbc4",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cba8.md#insn-0085cbc0)
- 新版 [`0085cbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cba8.md#insn-0085cbc0)

~~~diff
- 0085cbc0 ["COPY", "tmp:0:8", ["const:930:8"]]
- 0085cbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0085cbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 bytes 08c12491
+ 0085cbc0 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1da273bb61cf8e4abfb3831cef3ea43"></a>

### [`0085cc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cc04.md) → [`0085cc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc04.md) FUN_0085cc04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0085cc28",
      "incomplete_value": false,
      "site": "0085cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc28",
      "incomplete_value": false,
      "site": "0085cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0085cc28",
      "DATA",
      [
        "storage",
        "00c03930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cc28",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cc04.md#insn-0085cc24)
- 新版 [`0085cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc04.md#insn-0085cc24)

~~~diff
- 0085cc24 ["COPY", "tmp:0:8", ["const:930:8"]]
- 0085cc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0085cc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 bytes 29c12491
+ 0085cc24 bytes 29812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c288ef1f6ce190e482844d61bc01c9"></a>

### [`0085cc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cc54.md) → [`0085cc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc54.md) FUN_0085cc54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "0085cc60",
      "incomplete_value": false,
      "site": "0085cc60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc60",
      "incomplete_value": false,
      "site": "0085cc60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "0085cc60",
      "DATA",
      [
        "storage",
        "00c03930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cc60",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cc54.md#insn-0085cc5c)
- 新版 [`0085cc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc54.md#insn-0085cc5c)

~~~diff
- 0085cc5c ["COPY", "tmp:0:8", ["const:930:8"]]
- 0085cc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 0085cc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c bytes 29c12491
+ 0085cc5c bytes 29812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98684540298a8502722b850f959e6932"></a>

### [`0085cd84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cd84.md) → [`0085cd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cd84.md) FUN_0085cd84

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
      "definition_site": "0085cd98",
      "incomplete_value": false,
      "site": "0085cd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cd98",
      "incomplete_value": false,
      "site": "0085cd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0085cd9c",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cd9c",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cd98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cd84.md#insn-0085cd98)
- 新版 [`0085cd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cd84.md#insn-0085cd98)

~~~diff
- 0085cd98 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 0085cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0085cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 bytes 08012791
+ 0085cd98 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe90829c0010ba81c4f11be0edbd5fd"></a>

### [`0085cda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cda8.md) → [`0085cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cda8.md) FUN_0085cda8

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
      "definition_site": "0085cdac",
      "incomplete_value": false,
      "site": "0085cdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cdac",
      "incomplete_value": false,
      "site": "0085cdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0085cdb0",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cdb0",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cdac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cda8.md#insn-0085cdac)
- 新版 [`0085cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cda8.md#insn-0085cdac)

~~~diff
- 0085cdac ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 0085cdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0085cdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cdac bytes 08012791
+ 0085cdac bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c2ca2cba6ca3e5f57a22a9659db82b9"></a>

### [`0085cdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cdc0.md) → [`0085cdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md) FUN_0085cdc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db3c.md) [`0085d1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d1d8.md) [`0085d228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d228.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0085d1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1d8.md) [`0085d228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d228.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085cdf8",
      "incomplete_value": true,
      "site": "0085cdf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cdf8",
      "incomplete_value": true,
      "site": "0085cdf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1c:8"
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
      "definition_site": "0085cdf0",
      "incomplete_value": true,
      "site": "0085cdfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085cdf0",
      "incomplete_value": true,
      "site": "0085cdfc",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ce8c",
      "incomplete_value": false,
      "site": "0085ce8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ce8c",
      "incomplete_value": false,
      "site": "0085ce8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0085cde4",
      "READ",
      [
        "storage",
        "002a6d1c",
        null,
        "string"
      ]
    ],
    [
      "0085cdf0",
      "READ",
      [
        "storage",
        "002a6d23",
        null,
        "string"
      ]
    ],
    [
      "0085ce8c",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cde4",
      "READ",
      [
        "storage",
        "002a6d15",
        null,
        "string"
      ]
    ],
    [
      "0085cdf0",
      "READ",
      [
        "storage",
        "002a6d1c",
        null,
        "string"
      ]
    ],
    [
      "0085ce8c",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cdc0.md#insn-0085cddc) · [`0085ce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085cdc0.md#insn-0085ce84)
- 新版 [`0085cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md#insn-0085cddc) · [`0085ce84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md#insn-0085ce84)

~~~diff
- 0085cddc ["COPY", "tmp:0:8", ["const:d1c:8"]]
- 0085cddc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cddc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cddc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["COPY", "tmp:0:8", ["const:d15:8"]]
+ 0085cddc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cddc bytes 29713491
+ 0085cddc bytes 29553491
- 0085ce84 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0085ce84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0085ce84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 bytes 08c12891
+ 0085ce84 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b9f3003464a71a5b96093b6fa610925"></a>

### [`0085d09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d09c.md) → [`0085d09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d09c.md) FUN_0085d09c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0085d0b0",
      "incomplete_value": false,
      "site": "0085d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d0b0",
      "incomplete_value": false,
      "site": "0085d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0085d0b4",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d0b4",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d09c.md#insn-0085d0b0)
- 新版 [`0085d0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d09c.md#insn-0085d0b0)

~~~diff
- 0085d0b0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0085d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0085d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 bytes 08c12891
+ 0085d0b0 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4c8758f52f40cec6402d03a7181fc21"></a>

### [`0085d0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d0f8.md) → [`0085d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d0f8.md) FUN_0085d0f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0085d110",
      "incomplete_value": false,
      "site": "0085d114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d110",
      "incomplete_value": false,
      "site": "0085d114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0085d114",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d114",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d0f8.md#insn-0085d110)
- 新版 [`0085d110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d0f8.md#insn-0085d110)

~~~diff
- 0085d110 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0085d110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085d110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085d110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0085d110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085d110 bytes 08c12891
+ 0085d110 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994e14205c4a10f98fc7852c1b6624f6"></a>

### [`0085d154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d154.md) → [`0085d154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d154.md) FUN_0085d154

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0085d178",
      "incomplete_value": false,
      "site": "0085d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d178",
      "incomplete_value": false,
      "site": "0085d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0085d178",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d178",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d154.md#insn-0085d174)
- 新版 [`0085d174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d154.md#insn-0085d174)

~~~diff
- 0085d174 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0085d174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085d174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085d174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0085d174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085d174 bytes 29c12891
+ 0085d174 bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bc356f0b7de84c56f3ec31644a5144"></a>

### [`0085d1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d1a4.md) → [`0085d1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1a4.md) FUN_0085d1a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "0085d1b0",
      "incomplete_value": false,
      "site": "0085d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d1b0",
      "incomplete_value": false,
      "site": "0085d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0085d1b0",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d1b0",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d1a4.md#insn-0085d1ac)
- 新版 [`0085d1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1a4.md#insn-0085d1ac)

~~~diff
- 0085d1ac ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0085d1ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0085d1ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac bytes 29c12891
+ 0085d1ac bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d2746adad3c1a01aaf24e60ad29b58"></a>

### [`0085d2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d2a4.md) → [`0085d2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md) _INIT_161

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
      "definition_site": "0085d2e0",
      "incomplete_value": true,
      "site": "0085d2fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0085d2e0",
      "incomplete_value": true,
      "site": "0085d2fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0085d304",
      "incomplete_value": true,
      "site": "0085d320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0085d304",
      "incomplete_value": true,
      "site": "0085d320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0085d324",
      "incomplete_value": true,
      "site": "0085d340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0085d324",
      "incomplete_value": true,
      "site": "0085d340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0085d2e0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0085d304",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0085d324",
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
      "0085d2e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0085d304",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0085d324",
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

- 旧版 [`0085d2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d2a4.md#insn-0085d2d0) · [`0085d2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d2a4.md#insn-0085d2d8)
- 新版 [`0085d2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md#insn-0085d2d0) · [`0085d2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md#insn-0085d2d8)

~~~diff
- 0085d2d0 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0085d2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 0085d2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 bytes 73021591
+ 0085d2d0 bytes 73021891
- 0085d2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0085d2d8 bytes 49d2ffd0
+ 0085d2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0085d2d8 bytes 49d2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09a9aa18529eb6921f28e93a6206990"></a>

### [`0085e130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e130.md) → [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) FUN_0085e130

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 14件 [`006fd890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd890.md) [`0085e2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e2f8.md) [`0085fc14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc14.md) [`0085fc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc18.md) [`00ad900c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad9/00ad900c.md)
- 新版 呼出元 2件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 14件 [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`0085e2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e2f8.md) [`0085fc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc14.md) [`0085fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc18.md) [`00ad90d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.82% / 新版 75.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e1ac",
      "incomplete_value": true,
      "site": "0085e1b8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0085e1ac",
      "incomplete_value": true,
      "site": "0085e1b8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9e3:8"
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
      "value": [
        "LOAD",
        "16",
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
      "0085e154",
      "READ",
      [
        "storage",
        "0109e5a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0085e180",
      "PARAM",
      [
        "storage",
        "0109e570",
        null,
        "undefined8"
      ]
    ],
    [
      "0085e1a8",
      "READ",
      [
        "storage",
        "0029c9e3",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085e154",
      "READ",
      [
        "storage",
        "0109e660",
        null,
        "undefined1"
      ]
    ],
    [
      "0085e180",
      "PARAM",
      [
        "storage",
        "0109e630",
        null,
        "undefined8"
      ]
    ],
    [
      "0085e1a8",
      "READ",
      [
        "storage",
        "0029ca70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085e150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e130.md#insn-0085e150) · [`0085e180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e130.md#insn-0085e180) · [`0085e1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e130.md#insn-0085e1a0)
- 新版 [`0085e150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e150) · [`0085e180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e180) · [`0085e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e1a0)

~~~diff
- 0085e150 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 0085e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0085e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085e150 bytes 08811691
+ 0085e150 bytes 08811991
- 0085e180 ["COPY", "tmp:0:8", ["const:570:8"]]
- 0085e180 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085e180 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085e180 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 0085e180 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085e180 bytes 00c01591
+ 0085e180 bytes 00c01891
- 0085e1a0 ["COPY", "tmp:0:8", ["const:9e3:8"]]
- 0085e1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0085e1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 bytes 088d2791
+ 0085e1a0 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9011581bae7fc5969485bc2df4601c57"></a>

### [`0085e328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md) → [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) FUN_0085e328

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e66c",
      "incomplete_value": false,
      "site": "0085e66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e66c",
      "incomplete_value": false,
      "site": "0085e66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "definition_site": "0085e72c",
      "incomplete_value": false,
      "site": "0085e72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e72c",
      "incomplete_value": false,
      "site": "0085e72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e73c",
      "incomplete_value": false,
      "site": "0085e73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e73c",
      "incomplete_value": false,
      "site": "0085e73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0085e66c",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e6ec",
      "READ",
      [
        "storage",
        "00c03d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e72c",
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085e66c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e6ec",
      "READ",
      [
        "storage",
        "00c03e28",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e72c",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085e668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md#insn-0085e668) · [`0085e720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md#insn-0085e720) · [`0085e734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md#insn-0085e734)
- 新版 [`0085e668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md#insn-0085e668) · [`0085e720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md#insn-0085e720)

~~~diff
- 0085e668 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0085e668 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0085e668 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0085e668 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0085e668 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0085e668 bytes 4a413591
+ 0085e668 bytes 4a013891
- 0085e720 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 0085e720 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0085e720 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0085e720 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 0085e720 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0085e720 bytes 4a413791
+ 0085e720 bytes 4a013a91
- 0085e734 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085e734 bytes 291d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789ff272502bb9e9638f203920281262"></a>

### [`0085eb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085eb90.md) → [`0085eb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md) FUN_0085eb90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0085ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md) [`0085f460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008602c0.md) · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0085fcb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fcb4.md) [`0085fcb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fcb8.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md)
- 新版 呼出元 4件 [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) [`0085f460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602c0.md) · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0085fcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fcb4.md) [`0085fcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fcb8.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ebdc",
      "incomplete_value": true,
      "site": "0085ebec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:45:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ebdc",
      "incomplete_value": true,
      "site": "0085ebec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb8:8"
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
      "definition_site": "0085ebe0",
      "incomplete_value": true,
      "site": "0085ebf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085ebe0",
      "incomplete_value": true,
      "site": "0085ebf0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ec18",
      "incomplete_value": true,
      "site": "0085ec28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bd4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ec18",
      "incomplete_value": true,
      "site": "0085ec28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bce:8"
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
      "0085ebdc",
      "READ",
      [
        "storage",
        "00295fb8",
        null,
        "string"
      ]
    ],
    [
      "0085ebe0",
      "READ",
      [
        "storage",
        "00295fc8",
        null,
        "string"
      ]
    ],
    [
      "0085ec18",
      "READ",
      [
        "storage",
        "002aabce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0085ebdc",
      "READ",
      [
        "storage",
        "00296045",
        null,
        "string"
      ]
    ],
    [
      "0085ebe0",
      "READ",
      [
        "storage",
        "00296055",
        null,
        "string"
      ]
    ],
    [
      "0085ec18",
      "READ",
      [
        "storage",
        "002aabd4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085ebd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085eb90.md#insn-0085ebd0) · [`0085ebd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085eb90.md#insn-0085ebd4) · [`0085ebd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085eb90.md#insn-0085ebd8)
- 新版 [`0085ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md#insn-0085ebd0) · [`0085ebd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md#insn-0085ebd4)

~~~diff
- 0085ebd0 ["COPY", "register:4040:8", ["const:295000:8"]]
+ 0085ebd0 ["COPY", "register:4040:8", ["const:296000:8"]]
- 0085ebd0 bytes a8d1fff0
+ 0085ebd0 bytes c8d1ff90
- 0085ebd4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0085ebd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["COPY", "tmp:0:8", ["const:45:8"]]
+ 0085ebd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 bytes 08e13e91
+ 0085ebd4 bytes 08150191
- 0085ebd8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0085ebd8 bytes 89d2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6569afdb45a39fb13fad7964151b43"></a>

### [`0085ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md) → [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) FUN_0085ef84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0085fed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fed0.md) [`00860de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md) · 呼出先 16件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459f48.md) [`00459f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459f50.md) [`0056c55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c55c.md)
- 新版 呼出元 3件 [`0085fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fed0.md) [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md) · 呼出先 16件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f48.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`0056c55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c55c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085f2b4",
      "incomplete_value": false,
      "site": "0085f2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f2b4",
      "incomplete_value": false,
      "site": "0085f2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0085f2bc",
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f2c8",
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f314",
      "READ",
      [
        "storage",
        "00c03ff0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0085f2bc",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f2c8",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f314",
      "READ",
      [
        "storage",
        "00c040a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md#insn-0085f2b0) · [`0085f2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md#insn-0085f2b4) · [`0085f2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md#insn-0085f2c0)
- 新版 [`0085f2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md#insn-0085f2b0) · [`0085f2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md#insn-0085f2b4)

~~~diff
- 0085f2b0 ["COPY", "register:4040:8", ["const:c03000:8"]]
+ 0085f2b0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 0085f2b0 bytes 281d0090
+ 0085f2b0 bytes 281d00b0
- 0085f2b4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0085f2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0085f2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 bytes 08413d91
+ 0085f2b4 bytes 08010091
- 0085f2c0 ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085f2c0 bytes 281d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c005143a1281bd853ac3c54cfe961fb"></a>

### [`0085f5e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f5e8.md) → [`0085f5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f5e8.md) FUN_0085f5e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0085d778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085d/0085d778.md) [`0085e328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0085d778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d778.md) [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0085f5f4",
      "incomplete_value": false,
      "site": "0085f5f8",
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
      "definition_site": "0085f5f4",
      "incomplete_value": false,
      "site": "0085f5f8",
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
      "0085f5f4",
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
      "0085f5f4",
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

- 旧版 [`0085f5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f5e8.md#insn-0085f5f4)
- 新版 [`0085f5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f5e8.md#insn-0085f5f4)

~~~diff
- 0085f5f4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0085f5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0085f5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 bytes 00280c91
+ 0085f5f4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b83a89ef05767dea38337732c7d2bd"></a>

### [`0085f600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f600.md) → [`0085f600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f600.md) FUN_0085f600

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
      "definition_site": "0085f614",
      "incomplete_value": false,
      "site": "0085f618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f614",
      "incomplete_value": false,
      "site": "0085f618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "0085f618",
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f618",
      "DATA",
      [
        "storage",
        "00c03b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f600.md#insn-0085f614)
- 新版 [`0085f614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f600.md#insn-0085f614)

~~~diff
- 0085f614 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0085f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 0085f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f614 bytes 08012b91
+ 0085f614 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cb2543948661d2a389b2e355f2f3fa1"></a>

### [`0085f624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f624.md) → [`0085f624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f624.md) FUN_0085f624

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
      "definition_site": "0085f628",
      "incomplete_value": false,
      "site": "0085f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f628",
      "incomplete_value": false,
      "site": "0085f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "0085f62c",
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f62c",
      "DATA",
      [
        "storage",
        "00c03b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f624.md#insn-0085f628)
- 新版 [`0085f628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f624.md#insn-0085f628)

~~~diff
- 0085f628 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0085f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 0085f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f628 bytes 08012b91
+ 0085f628 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-906030c41429781b2a3b9ff7d743ee9c"></a>

### [`0085f74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f74c.md) → [`0085f74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f74c.md) FUN_0085f74c

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
      "definition_site": "0085f760",
      "incomplete_value": false,
      "site": "0085f764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f760",
      "incomplete_value": false,
      "site": "0085f764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0085f764",
      "DATA",
      [
        "storage",
        "00c03b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f764",
      "DATA",
      [
        "storage",
        "00c03bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f74c.md#insn-0085f760)
- 新版 [`0085f760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f74c.md#insn-0085f760)

~~~diff
- 0085f760 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0085f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 0085f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f760 bytes 08012d91
+ 0085f760 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e799b42fe263e2d8ea48d7f1d43d2279"></a>

### [`0085f770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f770.md) → [`0085f770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f770.md) FUN_0085f770

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
      "definition_site": "0085f774",
      "incomplete_value": false,
      "site": "0085f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f774",
      "incomplete_value": false,
      "site": "0085f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0085f778",
      "DATA",
      [
        "storage",
        "00c03b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f778",
      "DATA",
      [
        "storage",
        "00c03bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f770.md#insn-0085f774)
- 新版 [`0085f774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f770.md#insn-0085f774)

~~~diff
- 0085f774 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0085f774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 0085f774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f774 bytes 08012d91
+ 0085f774 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58677674efe6c1d978b1826b6ae0a2bc"></a>

### [`0085f788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f788.md) → [`0085f788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md) FUN_0085f788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085f7f8",
      "incomplete_value": true,
      "site": "0085f808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f7f8",
      "incomplete_value": true,
      "site": "0085f808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b96:8"
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
      "0085f7f8",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "0085f8d0",
      "DATA",
      [
        "storage",
        "00c03bb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f928",
      "READ",
      [
        "storage",
        "00c03bd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0085f7f8",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "0085f8d0",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f928",
      "READ",
      [
        "storage",
        "00c03c80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f788.md#insn-0085f7f0) · [`0085f8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085f788.md#insn-0085f8c8)
- 新版 [`0085f7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md#insn-0085f7f0) · [`0085f8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md#insn-0085f8c8)

~~~diff
- 0085f7f0 ["COPY", "tmp:0:8", ["const:b96:8"]]
- 0085f7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["COPY", "tmp:0:8", ["const:c23:8"]]
+ 0085f7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 bytes 29592e91
+ 0085f7f0 bytes 298d3091
- 0085f8c8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0085f8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0085f8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 bytes 08c12e91
+ 0085f8c8 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3386bede6be3ced6b6bd5514b4c1b06"></a>

### [`0085fb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fb30.md) → [`0085fb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb30.md) FUN_0085fb30

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
      "definition_site": "0085fb44",
      "incomplete_value": false,
      "site": "0085fb48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb44",
      "incomplete_value": false,
      "site": "0085fb48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "0085fb48",
      "DATA",
      [
        "storage",
        "00c03bb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fb48",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fb30.md#insn-0085fb44)
- 新版 [`0085fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb30.md#insn-0085fb44)

~~~diff
- 0085fb44 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0085fb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0085fb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 bytes 08c12e91
+ 0085fb44 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed6f21176df34753a2c82c475b23d4f"></a>

### [`0085fb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fb54.md) → [`0085fb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb54.md) FUN_0085fb54

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
      "definition_site": "0085fb58",
      "incomplete_value": false,
      "site": "0085fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb58",
      "incomplete_value": false,
      "site": "0085fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "0085fb5c",
      "DATA",
      [
        "storage",
        "00c03bb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fb5c",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fb54.md#insn-0085fb58)
- 新版 [`0085fb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb54.md#insn-0085fb58)

~~~diff
- 0085fb58 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0085fb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0085fb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 bytes 08c12e91
+ 0085fb58 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1794be68a291db477012aaba578b2d36"></a>

### [`0085fbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fbe0.md) → [`0085fbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fbe0.md) FUN_0085fbe0

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
      "definition_site": "0085fbf4",
      "incomplete_value": false,
      "site": "0085fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fbf4",
      "incomplete_value": false,
      "site": "0085fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0085fbf8",
      "DATA",
      [
        "storage",
        "00c03c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fbf8",
      "DATA",
      [
        "storage",
        "00c03d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fbe0.md#insn-0085fbf4)
- 新版 [`0085fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fbe0.md#insn-0085fbf4)

~~~diff
- 0085fbf4 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0085fbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0085fbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 bytes 08413191
+ 0085fbf4 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cea5694d49ac8d55b3b87103d4b3017"></a>

### [`0085fc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc04.md) → [`0085fc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc04.md) FUN_0085fc04

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
      "definition_site": "0085fc08",
      "incomplete_value": false,
      "site": "0085fc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc08",
      "incomplete_value": false,
      "site": "0085fc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "0085fc0c",
      "DATA",
      [
        "storage",
        "00c03c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fc0c",
      "DATA",
      [
        "storage",
        "00c03d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc04.md#insn-0085fc08)
- 新版 [`0085fc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc04.md#insn-0085fc08)

~~~diff
- 0085fc08 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0085fc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0085fc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 bytes 08413191
+ 0085fc08 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e48bf337a897deeadecbc61bedc0e57b"></a>

### [`0085fc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc80.md) → [`0085fc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc80.md) FUN_0085fc80

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
      "definition_site": "0085fc94",
      "incomplete_value": false,
      "site": "0085fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc94",
      "incomplete_value": false,
      "site": "0085fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0085fc98",
      "DATA",
      [
        "storage",
        "00c03cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fc98",
      "DATA",
      [
        "storage",
        "00c03d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fc80.md#insn-0085fc94)
- 新版 [`0085fc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc80.md#insn-0085fc94)

~~~diff
- 0085fc94 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0085fc94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0085fc94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 bytes 08413391
+ 0085fc94 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc8f231dc54ce2253dead27df850dec2"></a>

### [`0085fca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fca4.md) → [`0085fca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fca4.md) FUN_0085fca4

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
      "definition_site": "0085fca8",
      "incomplete_value": false,
      "site": "0085fcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fca8",
      "incomplete_value": false,
      "site": "0085fcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0085fcac",
      "DATA",
      [
        "storage",
        "00c03cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fcac",
      "DATA",
      [
        "storage",
        "00c03d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fca4.md#insn-0085fca8)
- 新版 [`0085fca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fca4.md#insn-0085fca8)

~~~diff
- 0085fca8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0085fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0085fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 bytes 08413391
+ 0085fca8 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8cc73225c1bb290951be7b2ed240163"></a>

### [`0085fd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd2c.md) → [`0085fd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd2c.md) FUN_0085fd2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0085e328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085e328.md) [`0085ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085e/0085ef84.md) [`0085fed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fed0.md) [`00860170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008602c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) [`0085fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fed0.md) [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0085fd38",
      "incomplete_value": false,
      "site": "0085fd3c",
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
      "definition_site": "0085fd38",
      "incomplete_value": false,
      "site": "0085fd3c",
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
      "0085fd38",
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
      "0085fd38",
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

- 旧版 [`0085fd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd2c.md#insn-0085fd38)
- 新版 [`0085fd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd2c.md#insn-0085fd38)

~~~diff
- 0085fd38 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0085fd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0085fd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 bytes 00280c91
+ 0085fd38 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d95a5635283d4c303ea09d100caddf78"></a>

### [`0085fd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd40.md) → [`0085fd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd40.md) FUN_0085fd40

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
      "definition_site": "0085fd48",
      "incomplete_value": false,
      "site": "0085fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd48",
      "incomplete_value": false,
      "site": "0085fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "0085fd4c",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fd4c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd40.md#insn-0085fd48)
- 新版 [`0085fd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd40.md#insn-0085fd48)

~~~diff
- 0085fd48 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0085fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0085fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 bytes 29413591
+ 0085fd48 bytes 29013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b7d77ad904e8bb04898c7151a2f724"></a>

### [`0085fd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd60.md) → [`0085fd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd60.md) FUN_0085fd60

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
      "definition_site": "0085fd68",
      "incomplete_value": false,
      "site": "0085fd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd68",
      "incomplete_value": false,
      "site": "0085fd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "0085fd6c",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fd6c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fd68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fd60.md#insn-0085fd68)
- 新版 [`0085fd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd60.md#insn-0085fd68)

~~~diff
- 0085fd68 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0085fd68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0085fd68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 bytes 29413591
+ 0085fd68 bytes 29013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a351a24f91939ae5254610f912a12d4"></a>

### [`0085fda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fda0.md) → [`0085fda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fda0.md) FUN_0085fda0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fdd0",
      "incomplete_value": false,
      "site": "0085fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fdd0",
      "incomplete_value": false,
      "site": "0085fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "0085fdd0",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fdd0",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fda0.md#insn-0085fdc4)
- 新版 [`0085fdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fda0.md#insn-0085fdc4)

~~~diff
- 0085fdc4 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0085fdc4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0085fdc4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 bytes 6b413591
+ 0085fdc4 bytes 6b013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7395de5e8e9045b1a4fa7f195b94ae0"></a>

### [`0085fe24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fe24.md) → [`0085fe24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md) FUN_0085fe24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fe44",
      "incomplete_value": false,
      "site": "0085fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fe44",
      "incomplete_value": false,
      "site": "0085fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "0085fe44",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fe44",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fe38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fe24.md#insn-0085fe38) · [`0085fe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085f/0085fe24.md#insn-0085fe40)
- 新版 [`0085fe38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md#insn-0085fe38) · [`0085fe40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md#insn-0085fe40)

~~~diff
- 0085fe38 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 0085fe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0085fe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 bytes 29413591
+ 0085fe38 bytes 29013891
- 0085fe40 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0085fe40 bytes f40300aa
+ 0085fe40 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 0085fe40 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28725c474c2c5690f33ed578019694ae"></a>

### [`00860118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860118.md) → [`00860118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860118.md) FUN_00860118

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00860138",
      "incomplete_value": false,
      "site": "0086013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860138",
      "incomplete_value": false,
      "site": "0086013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "0086013c",
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086013c",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860118.md#insn-00860138)
- 新版 [`00860138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860118.md#insn-00860138)

~~~diff
- 00860138 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00860138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00860138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860138 bytes 08413791
+ 00860138 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8ad57d3eb604b7d0185fb050ba22a5a"></a>

### [`00860150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860150.md) → [`00860150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860150.md) FUN_00860150

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00860154",
      "incomplete_value": false,
      "site": "00860158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860154",
      "incomplete_value": false,
      "site": "00860158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "00860158",
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00860158",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860150.md#insn-00860154)
- 新版 [`00860154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860150.md#insn-00860154)

~~~diff
- 00860154 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00860154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00860154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860154 bytes 08413791
+ 00860154 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97603bb5297d5461b0693a8121713f7"></a>

### [`008602a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008602a0.md) → [`008602a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602a0.md) FUN_008602a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008602a4",
      "incomplete_value": false,
      "site": "008602a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008602a4",
      "incomplete_value": false,
      "site": "008602a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "008602a8",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008602a8",
      "DATA",
      [
        "storage",
        "00c03f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008602a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008602a0.md#insn-008602a4)
- 新版 [`008602a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602a0.md#insn-008602a4)

~~~diff
- 008602a4 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008602a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008602a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008602a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 008602a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008602a4 bytes 08413991
+ 008602a4 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82877517943ea086e55c27b7defcea6"></a>

### [`008603b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008603b4.md) → [`008603b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603b4.md) FUN_008603b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008603d4",
      "incomplete_value": false,
      "site": "008603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603d4",
      "incomplete_value": false,
      "site": "008603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "008603d8",
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008603d8",
      "DATA",
      [
        "storage",
        "00c03f80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008603d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008603b4.md#insn-008603d4)
- 新版 [`008603d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603b4.md#insn-008603d4)

~~~diff
- 008603d4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008603d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008603d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008603d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008603d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008603d4 bytes 08413b91
+ 008603d4 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1792857e49dc2bd7444d2d980f384745"></a>

### [`008603ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008603ec.md) → [`008603ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603ec.md) FUN_008603ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008603f0",
      "incomplete_value": false,
      "site": "008603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603f0",
      "incomplete_value": false,
      "site": "008603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "008603f4",
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008603f4",
      "DATA",
      [
        "storage",
        "00c03f80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008603f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008603ec.md#insn-008603f0)
- 新版 [`008603f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603ec.md#insn-008603f0)

~~~diff
- 008603f0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008603f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008603f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008603f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 008603f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008603f0 bytes 08413b91
+ 008603f0 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1151c1869241f673361b5e62a1725b7b"></a>

### [`008604b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604b0.md) → [`008604b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604b0.md) FUN_008604b0

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
      "definition_site": "008604c4",
      "incomplete_value": false,
      "site": "008604c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604c4",
      "incomplete_value": false,
      "site": "008604c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "008604c8",
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008604c8",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008604c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604b0.md#insn-008604c0) · [`008604c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604b0.md#insn-008604c4)
- 新版 [`008604c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604b0.md#insn-008604c0) · [`008604c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604b0.md#insn-008604c4)

~~~diff
- 008604c0 ["COPY", "register:4040:8", ["const:c03000:8"]]
+ 008604c0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008604c0 bytes 081d00f0
+ 008604c0 bytes 281d0090
- 008604c4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 008604c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008604c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008604c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 008604c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008604c4 bytes 08413d91
+ 008604c4 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42fa76e331e3fc2f5c804034cb0334f3"></a>

### [`008604d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604d4.md) → [`008604d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604d4.md) FUN_008604d4

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
      "definition_site": "008604d8",
      "incomplete_value": false,
      "site": "008604dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604d8",
      "incomplete_value": false,
      "site": "008604dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "008604dc",
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008604dc",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008604d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604d4.md#insn-008604d4) · [`008604d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008604d4.md#insn-008604d8)
- 新版 [`008604d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604d4.md#insn-008604d4) · [`008604d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604d4.md#insn-008604d8)

~~~diff
- 008604d4 ["COPY", "register:4040:8", ["const:c03000:8"]]
+ 008604d4 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 008604d4 bytes 081d00f0
+ 008604d4 bytes 281d0090
- 008604d8 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 008604d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008604d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008604d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 008604d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008604d8 bytes 08413d91
+ 008604d8 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9ea7e2254b7557ba40ea7f8f27641e"></a>

### [`0086051c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/0086051c.md) → [`0086051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/0086051c.md) FUN_0086051c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0086053c",
      "incomplete_value": false,
      "site": "00860540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086053c",
      "incomplete_value": false,
      "site": "00860540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "00860540",
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00860540",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/0086051c.md#insn-00860538) · [`0086053c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/0086051c.md#insn-0086053c)
- 新版 [`00860538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/0086051c.md#insn-00860538) · [`0086053c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/0086051c.md#insn-0086053c)

~~~diff
- 00860538 ["COPY", "register:4040:8", ["const:c03000:8"]]
+ 00860538 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00860538 bytes 081d00f0
+ 00860538 bytes 281d0090
- 0086053c ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 0086053c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086053c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086053c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["COPY", "tmp:0:8", ["const:80:8"]]
+ 0086053c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086053c bytes 08413f91
+ 0086053c bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0b762d3c9a87de7e70b1987a662029"></a>

### [`00860554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860554.md) → [`00860554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860554.md) FUN_00860554

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00860558",
      "incomplete_value": false,
      "site": "0086055c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860558",
      "incomplete_value": false,
      "site": "0086055c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "0086055c",
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086055c",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860554.md#insn-00860554) · [`00860558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860554.md#insn-00860558)
- 新版 [`00860554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860554.md#insn-00860554) · [`00860558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860554.md#insn-00860558)

~~~diff
- 00860554 ["COPY", "register:4040:8", ["const:c03000:8"]]
+ 00860554 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 00860554 bytes 081d00f0
+ 00860554 bytes 281d0090
- 00860558 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00860558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00860558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860558 bytes 08413f91
+ 00860558 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe994b51f6842ae82c9c52438cb1a19"></a>

### [`008605f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008605f0.md) → [`008605f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md) _INIT_162

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086062c",
      "incomplete_value": true,
      "site": "00860648",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0086062c",
      "incomplete_value": true,
      "site": "00860648",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00860670",
      "incomplete_value": true,
      "site": "0086068c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00860670",
      "incomplete_value": true,
      "site": "0086068c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008606ac",
      "incomplete_value": true,
      "site": "008606c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008606ac",
      "incomplete_value": true,
      "site": "008606c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0086062c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00860650",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00860670",
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
      "0086062c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00860650",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00860670",
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

- 旧版 [`0086061c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008605f0.md#insn-0086061c) · [`00860624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008605f0.md#insn-00860624)
- 新版 [`0086061c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md#insn-0086061c) · [`00860624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008605f0.md#insn-00860624)

~~~diff
- 0086061c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0086061c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0086061c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0086061c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0086061c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0086061c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0086061c bytes 73621591
+ 0086061c bytes 73621891
- 00860624 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00860624 bytes 29d2fff0
+ 00860624 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00860624 bytes 29d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25ddbe8236adb14f03799ba85ea984e1"></a>

### [`008609f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008609f4.md) → [`008609f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md) FUN_008609f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md) [`0046fd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fd28.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md) [`0046fd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fd28.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00860aa0",
      "incomplete_value": true,
      "site": "00860ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860aa0",
      "incomplete_value": true,
      "site": "00860ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fd1:8"
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
      "definition_site": "00860aa4",
      "incomplete_value": true,
      "site": "00860ab8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00860aa4",
      "incomplete_value": true,
      "site": "00860ab8",
      "value": [
        "LOAD",
        "16",
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
      "00860aa0",
      "READ",
      [
        "storage",
        "00295fd1",
        null,
        "string"
      ]
    ],
    [
      "00860aa4",
      "READ",
      [
        "storage",
        "00295fde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00860aa0",
      "READ",
      [
        "storage",
        "0029605e",
        null,
        "string"
      ]
    ],
    [
      "00860aa4",
      "READ",
      [
        "storage",
        "0029606b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008609f4.md#insn-00860a94) · [`00860a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008609f4.md#insn-00860a98) · [`00860aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008609f4.md#insn-00860aa8)
- 新版 [`00860a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md#insn-00860a94) · [`00860a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md#insn-00860a98)

~~~diff
- 00860a94 ["COPY", "register:4040:8", ["const:295000:8"]]
+ 00860a94 ["COPY", "register:4040:8", ["const:296000:8"]]
- 00860a94 bytes a8d1ffb0
+ 00860a94 bytes a8d1ffd0
- 00860a98 ["COPY", "tmp:0:8", ["const:fd1:8"]]
- 00860a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["COPY", "tmp:0:8", ["const:5e:8"]]
+ 00860a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860a98 bytes 08453f91
+ 00860a98 bytes 08790191
- 00860aa8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 00860aa8 bytes 88d2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bd1be07268ac48c6719cc42e513a631"></a>

### [`00860de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md) → [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) FUN_00860de0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 52件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c894.md) [`0041c8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md)
- 新版 呼出元 0件  · 呼出先 52件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c894.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.31% / 新版 94.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 41件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00860e3c",
      "incomplete_value": true,
      "site": "00860e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cdf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860e3c",
      "incomplete_value": true,
      "site": "00860e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd9:8"
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
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c51:8"
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
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00860e80",
      "incomplete_value": true,
      "site": "00860e94",
      "value": [
        "LOAD",
        "16",
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
      "00860e2c",
      "READ",
      [
        "storage",
        "002abcd9",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c51",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00860e2c",
      "READ",
      [
        "storage",
        "002abcdf",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c4a",
        null,
        "string"
      ]
    ],
    [
      "00860e80",
      "READ",
      [
        "storage",
        "002a5c5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md#insn-00860e24) · [`00860e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md#insn-00860e78) · [`00860e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860de0.md#insn-00860e7c)
- 新版 [`00860e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md#insn-00860e24) · [`00860e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md#insn-00860e78)

~~~diff
- 00860e24 ["COPY", "tmp:0:8", ["const:cd9:8"]]
- 00860e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00860e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00860e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00860e24 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00860e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00860e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00860e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00860e24 bytes 29653391
+ 00860e24 bytes 297d3391
- 00860e78 ["COPY", "tmp:0:8", ["const:c51:8"]]
- 00860e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["COPY", "tmp:0:8", ["const:c4a:8"]]
+ 00860e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860e78 bytes 08453191
+ 00860e78 bytes 08293191
- 00860e7c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00860e7c bytes 89d2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0aede37235bb993f1f945a7f1487051"></a>

### [`008629ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md) → [`008629ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md) FUN_008629ec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 99件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cc4c.md)
- 新版 呼出元 0件  · 呼出先 99件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.92% / 新版 93.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_value` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00862a98",
      "incomplete_value": true,
      "site": "00862aa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862a98",
      "incomplete_value": true,
      "site": "00862aa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d0:8"
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
      "definition_site": "00862b44",
      "incomplete_value": true,
      "site": "00862b58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862b44",
      "incomplete_value": true,
      "site": "00862b58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a6c:8"
              ]
            ]
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
      "definition_site": "00862be0",
      "incomplete_value": true,
      "site": "00862be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862be0",
      "incomplete_value": true,
      "site": "00862be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a81:8"
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
      "00862a98",
      "READ",
      [
        "storage",
        "002a65d0",
        null,
        "string"
      ]
    ],
    [
      "00862b44",
      "READ",
      [
        "storage",
        "002a7a6c",
        null,
        "string"
      ]
    ],
    [
      "00862bc8",
      "READ",
      [
        "storage",
        "002a7a81",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00862a98",
      "READ",
      [
        "storage",
        "002a65c9",
        null,
        "string"
      ]
    ],
    [
      "00862b44",
      "READ",
      [
        "storage",
        "002a79d8",
        null,
        "string"
      ]
    ],
    [
      "00862bc8",
      "READ",
      [
        "storage",
        "002a79ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00862a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md#insn-00862a90) · [`00862b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md#insn-00862b3c) · [`00862bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md#insn-00862bc4)
- 新版 [`00862a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862a90) · [`00862b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862b3c) · [`00862bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md#insn-00862bc4)

~~~diff
- 00862a90 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00862a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 00862a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862a90 bytes 29411791
+ 00862a90 bytes 29251791
- 00862b3c ["COPY", "tmp:0:8", ["const:a6c:8"]]
- 00862b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00862b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862b3c bytes 29b12991
+ 00862b3c bytes 29612791
- 00862bc4 ["COPY", "tmp:0:8", ["const:a81:8"]]
- 00862bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["COPY", "tmp:0:8", ["const:9ed:8"]]
+ 00862bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00862bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00862bc4 bytes 29052a91
+ 00862bc4 bytes 29b52791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ca3300b741995fec236941fb8a20275"></a>

### [`008648a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md) → [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) FUN_008648a8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 57件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md)
- 新版 呼出元 0件  · 呼出先 57件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.54% / 新版 91.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_value` 72件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:87f:8"
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
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008649a0",
      "incomplete_value": true,
      "site": "008649c0",
      "value": [
        "LOAD",
        "16",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008649b8",
      "incomplete_value": true,
      "site": "008649c4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008649b8",
      "incomplete_value": true,
      "site": "008649c4",
      "value": [
        "LOAD",
        "16",
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
      "00864940",
      "PARAM",
      [
        "storage",
        "0029b991",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d87f",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d88f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00864940",
      "PARAM",
      [
        "storage",
        "0029ba1e",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d90c",
        null,
        "string"
      ]
    ],
    [
      "008649a0",
      "READ",
      [
        "storage",
        "0029d91c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00864940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md#insn-00864940) · [`00864998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md#insn-00864998) · [`00864a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md#insn-00864a48)
- 新版 [`00864940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864940) · [`00864998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864998) · [`00864a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md#insn-00864a48)

~~~diff
- 00864940 ["COPY", "tmp:0:8", ["const:991:8"]]
- 00864940 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00864940 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00864940 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["COPY", "tmp:0:8", ["const:a1e:8"]]
+ 00864940 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00864940 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00864940 bytes 42442691
+ 00864940 bytes 42782891
- 00864998 ["COPY", "tmp:0:8", ["const:87f:8"]]
- 00864998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00864998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00864998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["COPY", "tmp:0:8", ["const:90c:8"]]
+ 00864998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00864998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00864998 bytes 4afd2191
+ 00864998 bytes 4a312491
- 00864a48 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00864a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00864a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00864a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["COPY", "tmp:0:8", ["const:b5:8"]]
+ 00864a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00864a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00864a48 bytes 08a10091
+ 00864a48 bytes 08d50291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40b76382b615239892ca39822b0f1bd0"></a>

### [`008673f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00867/008673f0.md) → [`008673f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md) FUN_008673f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008648a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 14件 [`004512c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fdf4.md) [`006fd890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fdbdc.md)
- 新版 呼出元 2件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 14件 [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.60% / 新版 91.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2bb:8"
              ]
            ]
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
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008675d8",
      "incomplete_value": true,
      "site": "008675e8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00867644",
      "incomplete_value": true,
      "site": "00867654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00867644",
      "incomplete_value": true,
      "site": "00867654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f1a:8"
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
      "00867480",
      "READ",
      [
        "storage",
        "00294fba",
        null,
        "string"
      ]
    ],
    [
      "00867480",
      "READ",
      [
        "storage",
        "00294fca",
        null,
        "string"
      ]
    ],
    [
      "0086748c",
      "PARAM",
      [
        "storage",
        "0029e21d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00867480",
      "READ",
      [
        "storage",
        "00295047",
        null,
        "string"
      ]
    ],
    [
      "00867480",
      "READ",
      [
        "storage",
        "00295057",
        null,
        "string"
      ]
    ],
    [
      "0086748c",
      "PARAM",
      [
        "storage",
        "0029e2aa",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00867470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00867/008673f0.md#insn-00867470) · [`00867478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00867/008673f0.md#insn-00867478) · [`0086747c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00867/008673f0.md#insn-0086747c)
- 新版 [`00867470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-00867470) · [`00867478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-00867478) · [`0086747c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00867/008673f0.md#insn-0086747c)

~~~diff
- 00867470 ["COPY", "tmp:0:8", ["const:21d:8"]]
- 00867470 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00867470 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00867470 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["COPY", "tmp:0:8", ["const:2aa:8"]]
+ 00867470 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00867470 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00867470 bytes f7760891
+ 00867470 bytes f7aa0a91
- 00867478 ["COPY", "register:4040:8", ["const:294000:8"]]
+ 00867478 ["COPY", "register:4040:8", ["const:295000:8"]]
- 00867478 bytes 68d1ffb0
+ 00867478 bytes 68d1ffd0
- 0086747c ["COPY", "tmp:0:8", ["const:fba:8"]]
- 0086747c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086747c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086747c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["COPY", "tmp:0:8", ["const:47:8"]]
+ 0086747c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086747c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086747c bytes 08e93e91
+ 0086747c bytes 081d0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26252c6433ba459e1e68be82c4b4aca9"></a>

### [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) → [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) FUN_00868124

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`00428714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428714.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`00428714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008687f0",
      "incomplete_value": false,
      "site": "008687f8",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008687f0",
      "incomplete_value": false,
      "site": "008687f8",
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
            "const:c2b:8"
          ]
        ]
      ]
    },
    "ordinal": 104,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008688e8",
      "incomplete_value": false,
      "site": "008688f0",
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
            "const:8a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008688e8",
      "incomplete_value": false,
      "site": "008688f0",
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
            "const:939:8"
          ]
        ]
      ]
    },
    "ordinal": 118,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008687f0",
      "PARAM",
      [
        "storage",
        "00293c2b",
        null,
        "string"
      ]
    ],
    [
      "008688e8",
      "PARAM",
      [
        "storage",
        "002a7939",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008687f0",
      "PARAM",
      [
        "storage",
        "00293cb8",
        null,
        "string"
      ]
    ],
    [
      "008688e8",
      "PARAM",
      [
        "storage",
        "002a78a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008687f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md#insn-008687f0) · [`008688e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md#insn-008688e8)
- 新版 [`008687f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md#insn-008687f0) · [`008688e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md#insn-008688e8)

~~~diff
- 008687f0 ["COPY", "tmp:0:8", ["const:c2b:8"]]
- 008687f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008687f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008687f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 008687f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008687f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008687f0 bytes 21ac3091
+ 008687f0 bytes 21e03291
- 008688e8 ["COPY", "tmp:0:8", ["const:939:8"]]
- 008688e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008688e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008688e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["COPY", "tmp:0:8", ["const:8a5:8"]]
+ 008688e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008688e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008688e8 bytes 21e42491
+ 008688e8 bytes 21942291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729f2fd640a01449ac2a950ae02891e3"></a>

### [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) → [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) FUN_00868b14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 69件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md)
- 新版 呼出元 0件  · 呼出先 69件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00868ecc",
      "incomplete_value": true,
      "site": "00868edc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a2e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00868ecc",
      "incomplete_value": true,
      "site": "00868edc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ac2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00868ed0",
      "incomplete_value": true,
      "site": "00868ee0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00868ed0",
      "incomplete_value": true,
      "site": "00868ee0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00869020",
      "incomplete_value": true,
      "site": "00869038",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00869020",
      "incomplete_value": true,
      "site": "00869038",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a6c:8"
              ]
            ]
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
      "00868dec",
      "READ",
      [
        "storage",
        "0029b96e",
        null,
        "string"
      ]
    ],
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029b97e",
        null,
        "string"
      ]
    ],
    [
      "00868ecc",
      "READ",
      [
        "storage",
        "002a7ac2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029b9fb",
        null,
        "string"
      ]
    ],
    [
      "00868dec",
      "READ",
      [
        "storage",
        "0029ba0b",
        null,
        "string"
      ]
    ],
    [
      "00868ecc",
      "READ",
      [
        "storage",
        "002a7a2e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00868de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md#insn-00868de8) · [`00868ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md#insn-00868ec4) · [`00869018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md#insn-00869018)
- 新版 [`00868de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00868de8) · [`00868ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00868ec4) · [`00869018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md#insn-00869018)

~~~diff
- 00868de8 ["COPY", "tmp:0:8", ["const:96e:8"]]
- 00868de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00868de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00868de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["COPY", "tmp:0:8", ["const:9fb:8"]]
+ 00868de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00868de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00868de8 bytes 08b92591
+ 00868de8 bytes 08ed2791
- 00868ec4 ["COPY", "tmp:0:8", ["const:ac2:8"]]
- 00868ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["COPY", "tmp:0:8", ["const:a2e:8"]]
+ 00868ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00868ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00868ec4 bytes 08092b91
+ 00868ec4 bytes 08b92891
- 00869018 ["COPY", "tmp:0:8", ["const:a6c:8"]]
- 00869018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00869018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00869018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00869018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00869018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00869018 bytes 29b12991
+ 00869018 bytes 29612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e61d290fdfaf70b470d7b446e079c84"></a>

### [`0086a350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md) → [`0086a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md) FUN_0086a350

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 52件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0044fcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fce4.md) [`0044fe84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fe84.md)
- 新版 呼出元 0件  · 呼出先 52件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044fcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fce4.md) [`0044fe84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fe84.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.57% / 新版 97.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086a454",
      "incomplete_value": true,
      "site": "0086a454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086a454",
      "incomplete_value": true,
      "site": "0086a454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8fb:8"
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
      "definition_site": "0086a588",
      "incomplete_value": true,
      "site": "0086a5a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dbd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086a588",
      "incomplete_value": true,
      "site": "0086a5a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:db7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086a648",
      "incomplete_value": true,
      "site": "0086a648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086a648",
      "incomplete_value": true,
      "site": "0086a648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dac:8"
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
      "0086a440",
      "READ",
      [
        "storage",
        "0029d8fb",
        null,
        "string"
      ]
    ],
    [
      "0086a588",
      "READ",
      [
        "storage",
        "002abdb7",
        null,
        "string"
      ]
    ],
    [
      "0086a634",
      "READ",
      [
        "storage",
        "00292dac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086a440",
      "READ",
      [
        "storage",
        "0029d988",
        null,
        "string"
      ]
    ],
    [
      "0086a588",
      "READ",
      [
        "storage",
        "002abdbd",
        null,
        "string"
      ]
    ],
    [
      "0086a634",
      "READ",
      [
        "storage",
        "00292e39",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086a438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md#insn-0086a438) · [`0086a580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md#insn-0086a580) · [`0086a62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086a/0086a350.md#insn-0086a62c)
- 新版 [`0086a438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md#insn-0086a438) · [`0086a580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md#insn-0086a580) · [`0086a62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md#insn-0086a62c)

~~~diff
- 0086a438 ["COPY", "tmp:0:8", ["const:8fb:8"]]
- 0086a438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086a438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086a438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086a438 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 0086a438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086a438 bytes 29ed2391
+ 0086a438 bytes 29212691
- 0086a580 ["COPY", "tmp:0:8", ["const:db7:8"]]
- 0086a580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086a580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086a580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086a580 ["COPY", "tmp:0:8", ["const:dbd:8"]]
+ 0086a580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086a580 bytes 29dd3691
+ 0086a580 bytes 29f53691
- 0086a62c ["COPY", "tmp:0:8", ["const:dac:8"]]
- 0086a62c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086a62c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086a62c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086a62c ["COPY", "tmp:0:8", ["const:e39:8"]]
+ 0086a62c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a62c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086a62c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086a62c bytes 29b13691
+ 0086a62c bytes 29e53891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e322feb879506314a17f400bda006bf7"></a>

### [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) → [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) FUN_0086b704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 153件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b014.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md)
- 新版 呼出元 0件  · 呼出先 153件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b014.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 32件, `store_destination` 1件, `store_value` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:87f:8"
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
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0086b7b8",
      "incomplete_value": true,
      "site": "0086b7c8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086b7cc",
      "incomplete_value": true,
      "site": "0086b7e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0086b7cc",
      "incomplete_value": true,
      "site": "0086b7e0",
      "value": [
        "LOAD",
        "16",
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
      "0086b75c",
      "PARAM",
      [
        "storage",
        "0029b991",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d87f",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d88f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086b75c",
      "PARAM",
      [
        "storage",
        "0029ba1e",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d90c",
        null,
        "string"
      ]
    ],
    [
      "0086b7b8",
      "READ",
      [
        "storage",
        "0029d91c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md#insn-0086bd8c) · [`0086b75c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md#insn-0086b75c) · [`0086b7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md#insn-0086b7b0)
- 新版 [`0086bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086bd8c) · [`0086b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086b75c) · [`0086b7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md#insn-0086b7b0)

~~~diff
- 0086bd8c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0086bd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:5f0:8"]]
- 0086bd8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0086bd8c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0086bd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:6b0:8"]]
+ 0086bd8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0086bd8c bytes 09c11739
+ 0086bd8c bytes 09c11a39
- 0086b75c ["COPY", "tmp:0:8", ["const:991:8"]]
- 0086b75c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0086b75c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0086b75c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["COPY", "tmp:0:8", ["const:a1e:8"]]
+ 0086b75c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0086b75c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0086b75c bytes 42442691
+ 0086b75c bytes 42782891
- 0086b7b0 ["COPY", "tmp:0:8", ["const:87f:8"]]
- 0086b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086b7b0 ["COPY", "tmp:0:8", ["const:90c:8"]]
+ 0086b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086b7b0 bytes 08fd2191
+ 0086b7b0 bytes 08312491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56aaee8fedcdd27da67bbc733976e730"></a>

### [`008710b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008710b4.md) → [`008710b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710b4.md) FUN_008710b4

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
      "definition_site": "008710b8",
      "incomplete_value": false,
      "site": "008710bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008710b8",
      "incomplete_value": false,
      "site": "008710bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008710bc",
      "DATA",
      [
        "storage",
        "00c040c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008710bc",
      "DATA",
      [
        "storage",
        "00c04178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008710b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008710b4.md#insn-008710b8)
- 新版 [`008710b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710b4.md#insn-008710b8)

~~~diff
- 008710b8 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 008710b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008710b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008710b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 008710b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008710b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008710b8 bytes 08210391
+ 008710b8 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7116e0aa79536028e9fbd690798fc6f6"></a>

### [`008710cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008710cc.md) → [`008710cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710cc.md) FUN_008710cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871200.md) [`00871204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871204.md) [`00ada4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada4e4.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00871200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871200.md) [`00871204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871204.md) [`00ada5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008710e4",
      "incomplete_value": false,
      "site": "008710f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008710e4",
      "incomplete_value": false,
      "site": "008710f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "008710f4",
      "DATA",
      [
        "storage",
        "00c04138",
        null,
        "undefined *"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04158",
        null,
        "pointer"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008710f4",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04208",
        null,
        "pointer"
      ]
    ],
    [
      "00871128",
      "READ",
      [
        "storage",
        "00c04210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008710e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008710cc.md#insn-008710e4)
- 新版 [`008710e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008710cc.md#insn-008710e4)

~~~diff
- 008710e4 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008710e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008710e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008710e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 008710e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008710e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008710e4 bytes 29e10491
+ 008710e4 bytes 29a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15404d5799c1074d0ed53e1f9d89e89e"></a>

### [`008711cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008711cc.md) → [`008711cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711cc.md) FUN_008711cc

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
      "definition_site": "008711e0",
      "incomplete_value": false,
      "site": "008711e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008711e0",
      "incomplete_value": false,
      "site": "008711e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "008711e4",
      "DATA",
      [
        "storage",
        "00c04138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008711e4",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008711e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008711cc.md#insn-008711e0)
- 新版 [`008711e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711cc.md#insn-008711e0)

~~~diff
- 008711e0 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008711e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008711e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008711e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 008711e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008711e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008711e0 bytes 08e10491
+ 008711e0 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eff991c00c8f1043367eab1a91885bf"></a>

### [`008711f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008711f0.md) → [`008711f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711f0.md) FUN_008711f0

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
      "definition_site": "008711f4",
      "incomplete_value": false,
      "site": "008711f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008711f4",
      "incomplete_value": false,
      "site": "008711f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "008711f8",
      "DATA",
      [
        "storage",
        "00c04138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008711f8",
      "DATA",
      [
        "storage",
        "00c041e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008711f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008711f0.md#insn-008711f4)
- 新版 [`008711f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008711f0.md#insn-008711f4)

~~~diff
- 008711f4 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008711f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008711f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008711f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 008711f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008711f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008711f4 bytes 08e10491
+ 008711f4 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc5104581dc85c95bf67d6a3d41e0d35"></a>

### [`00871208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871208.md) → [`00871208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871208.md) FUN_00871208

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00871348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871348.md) [`0087134c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/0087134c.md) [`00ada6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada6ac.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00871348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871348.md) [`0087134c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/0087134c.md) [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "00871234",
      "incomplete_value": false,
      "site": "0087123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871234",
      "incomplete_value": false,
      "site": "0087123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "0087123c",
      "DATA",
      [
        "storage",
        "00c041a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c041c8",
        null,
        "pointer"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c041d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087123c",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c04278",
        null,
        "pointer"
      ]
    ],
    [
      "00871270",
      "READ",
      [
        "storage",
        "00c04280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871208.md#insn-00871234)
- 新版 [`00871234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871208.md#insn-00871234)

~~~diff
- 00871234 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00871234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00871234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871234 bytes 08a10691
+ 00871234 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87137d5f9e91b8026cc2cf966434eca4"></a>

### [`00871314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871314.md) → [`00871314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871314.md) FUN_00871314

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
      "definition_site": "00871328",
      "incomplete_value": false,
      "site": "0087132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871328",
      "incomplete_value": false,
      "site": "0087132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "0087132c",
      "DATA",
      [
        "storage",
        "00c041a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087132c",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871314.md#insn-00871328)
- 新版 [`00871328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871314.md#insn-00871328)

~~~diff
- 00871328 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00871328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00871328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871328 bytes 08a10691
+ 00871328 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb73d10f6479e9559c01e8499042a70"></a>

### [`00871338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871338.md) → [`00871338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871338.md) FUN_00871338

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
      "definition_site": "0087133c",
      "incomplete_value": false,
      "site": "00871340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087133c",
      "incomplete_value": false,
      "site": "00871340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "00871340",
      "DATA",
      [
        "storage",
        "00c041a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871340",
      "DATA",
      [
        "storage",
        "00c04258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087133c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871338.md#insn-0087133c)
- 新版 [`0087133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871338.md#insn-0087133c)

~~~diff
- 0087133c ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 0087133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0087133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087133c bytes 08a10691
+ 0087133c bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8edcc3069a52cb0eb5e30125b21e19"></a>

### [`00871350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871350.md) → [`00871350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md) FUN_00871350

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008713c0",
      "incomplete_value": true,
      "site": "008713d0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:c23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008713c0",
      "incomplete_value": true,
      "site": "008713d0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b96:8"
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
      "definition_site": "00871498",
      "incomplete_value": true,
      "site": "00871498",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871498",
      "incomplete_value": true,
      "site": "00871498",
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
            "const:218:8"
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
      "008713c0",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "00871498",
      "DATA",
      [
        "storage",
        "00c04218",
        null,
        "undefined *"
      ]
    ],
    [
      "008714f0",
      "READ",
      [
        "storage",
        "00c04238",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008713c0",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "00871498",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008714f0",
      "READ",
      [
        "storage",
        "00c042e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008713b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871350.md#insn-008713b8) · [`00871490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871350.md#insn-00871490)
- 新版 [`008713b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md#insn-008713b8) · [`00871490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871350.md#insn-00871490)

~~~diff
- 008713b8 ["COPY", "tmp:0:8", ["const:b96:8"]]
- 008713b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008713b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008713b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["COPY", "tmp:0:8", ["const:c23:8"]]
+ 008713b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008713b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008713b8 bytes 29592e91
+ 008713b8 bytes 298d3091
- 00871490 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00871490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00871490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871490 bytes 08610891
+ 00871490 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-befe75776e25fec1a839543b7e13aa57"></a>

### [`008716f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008716f8.md) → [`008716f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008716f8.md) FUN_008716f8

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
      "definition_site": "0087170c",
      "incomplete_value": false,
      "site": "00871710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087170c",
      "incomplete_value": false,
      "site": "00871710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "00871710",
      "DATA",
      [
        "storage",
        "00c04218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871710",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087170c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008716f8.md#insn-0087170c)
- 新版 [`0087170c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008716f8.md#insn-0087170c)

~~~diff
- 0087170c ["COPY", "tmp:0:8", ["const:218:8"]]
- 0087170c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087170c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087170c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0087170c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087170c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087170c bytes 08610891
+ 0087170c bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a21c9cc75ffe3823355739d129f50b"></a>

### [`008717a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008717a8.md) → [`008717a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717a8.md) FUN_008717a8

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
      "definition_site": "008717bc",
      "incomplete_value": false,
      "site": "008717c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008717bc",
      "incomplete_value": false,
      "site": "008717c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "008717c0",
      "DATA",
      [
        "storage",
        "00c042c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008717c0",
      "DATA",
      [
        "storage",
        "00c04378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008717bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008717a8.md#insn-008717bc)
- 新版 [`008717bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717a8.md#insn-008717bc)

~~~diff
- 008717bc ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 008717bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008717bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008717bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["COPY", "tmp:0:8", ["const:378:8"]]
+ 008717bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008717bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008717bc bytes 08210b91
+ 008717bc bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b29df85fdde52bf627a984621fd6b96"></a>

### [`008717e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008717e4.md) → [`008717e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717e4.md) FUN_008717e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470050.md) [`00470a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470a98.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470050.md) [`00470a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470a98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871840",
      "incomplete_value": true,
      "site": "00871840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:189:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871840",
      "incomplete_value": true,
      "site": "00871840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc:8"
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
      "0087182c",
      "READ",
      [
        "storage",
        "002960fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087182c",
      "READ",
      [
        "storage",
        "00296189",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008717e4.md#insn-00871824)
- 新版 [`00871824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008717e4.md#insn-00871824)

~~~diff
- 00871824 ["COPY", "tmp:0:8", ["const:fc:8"]]
- 00871824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["COPY", "tmp:0:8", ["const:189:8"]]
+ 00871824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871824 bytes 29f10391
+ 00871824 bytes 29250691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507b061a23eb39bb3f211ca5ad63d620"></a>

### [`00871910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871910.md) → [`00871910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871910.md) FUN_00871910

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
      "definition_site": "00871924",
      "incomplete_value": false,
      "site": "00871928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871924",
      "incomplete_value": false,
      "site": "00871928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00871928",
      "DATA",
      [
        "storage",
        "00c04348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871928",
      "DATA",
      [
        "storage",
        "00c043f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871910.md#insn-00871924)
- 新版 [`00871924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871910.md#insn-00871924)

~~~diff
- 00871924 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00871924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00871924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871924 bytes 08210d91
+ 00871924 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01bb0a5a7ebb666b074a07d4c8d65529"></a>

### [`00871934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871934.md) → [`00871934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871934.md) FUN_00871934

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
      "definition_site": "00871938",
      "incomplete_value": false,
      "site": "0087193c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871938",
      "incomplete_value": false,
      "site": "0087193c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "0087193c",
      "DATA",
      [
        "storage",
        "00c04348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087193c",
      "DATA",
      [
        "storage",
        "00c043f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871934.md#insn-00871938)
- 新版 [`00871938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871934.md#insn-00871938)

~~~diff
- 00871938 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00871938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00871938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871938 bytes 08210d91
+ 00871938 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd6ac7ee74de2ef475a547cdb613e2fd"></a>

### [`008719c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008719c0.md) → [`008719c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719c0.md) FUN_008719c0

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
      "definition_site": "008719d4",
      "incomplete_value": false,
      "site": "008719d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008719d4",
      "incomplete_value": false,
      "site": "008719d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "008719d8",
      "DATA",
      [
        "storage",
        "00c043c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719d8",
      "DATA",
      [
        "storage",
        "00c04478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008719c0.md#insn-008719d4)
- 新版 [`008719d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719c0.md#insn-008719d4)

~~~diff
- 008719d4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 008719d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008719d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008719d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 008719d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008719d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008719d4 bytes 08210f91
+ 008719d4 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c55915e091cb5819cbd9f1a26292e44"></a>

### [`008719e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008719e4.md) → [`008719e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719e4.md) FUN_008719e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008719e8",
      "incomplete_value": true,
      "site": "008719ec",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008719e8",
      "incomplete_value": true,
      "site": "008719ec",
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
            "const:3c8:8"
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
      "008719ec",
      "DATA",
      [
        "storage",
        "00c043c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719ec",
      "DATA",
      [
        "storage",
        "00c04478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/008719e4.md#insn-008719e8)
- 新版 [`008719e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/008719e4.md#insn-008719e8)

~~~diff
- 008719e8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 008719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 008719e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008719e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008719e8 bytes 08210f91
+ 008719e8 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8daf2d64f383ff7032d9b4361463f9c9"></a>

### [`00871a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a30.md) → [`00871a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a30.md) FUN_00871a30

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
      "definition_site": "00871a44",
      "incomplete_value": false,
      "site": "00871a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871a44",
      "incomplete_value": false,
      "site": "00871a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00871a48",
      "DATA",
      [
        "storage",
        "00c04448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871a48",
      "DATA",
      [
        "storage",
        "00c044f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a30.md#insn-00871a44)
- 新版 [`00871a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a30.md#insn-00871a44)

~~~diff
- 00871a44 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00871a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00871a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871a44 bytes 08211191
+ 00871a44 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02e2f28809d60698fa50d921741e5c63"></a>

### [`00871a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a6c.md) → [`00871a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md) FUN_00871a6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0042be48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042be48.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0042be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042be48.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871b34",
      "incomplete_value": true,
      "site": "00871b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00871b34",
      "incomplete_value": true,
      "site": "00871b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871b7c",
      "incomplete_value": true,
      "site": "00871b8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:efb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871b7c",
      "incomplete_value": true,
      "site": "00871b8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f8f:8"
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
      "definition_site": "00871b90",
      "incomplete_value": true,
      "site": "00871b90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00871b90",
      "incomplete_value": true,
      "site": "00871b90",
      "value": [
        "LOAD",
        "8",
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
      "00871b24",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ],
    [
      "00871b7c",
      "READ",
      [
        "storage",
        "002adf8f",
        null,
        "string"
      ]
    ],
    [
      "00871b80",
      "READ",
      [
        "storage",
        "002adf9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00871b24",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ],
    [
      "00871b7c",
      "READ",
      [
        "storage",
        "002adefb",
        null,
        "string"
      ]
    ],
    [
      "00871b80",
      "READ",
      [
        "storage",
        "002adf08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a6c.md#insn-00871b1c) · [`00871b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a6c.md#insn-00871b74) · [`00871ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871a6c.md#insn-00871ba8)
- 新版 [`00871b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md#insn-00871b1c) · [`00871b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md#insn-00871b74) · [`00871ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871a6c.md#insn-00871ba8)

~~~diff
- 00871b1c ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 00871b1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871b1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871b1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871b1c ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 00871b1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871b1c bytes 29851291
+ 00871b1c bytes 299d1291
- 00871b74 ["COPY", "tmp:0:8", ["const:f8f:8"]]
- 00871b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871b74 ["COPY", "tmp:0:8", ["const:efb:8"]]
+ 00871b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871b74 bytes 293d3e91
+ 00871b74 bytes 29ed3b91
- 00871ba8 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00871ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00871ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ba8 bytes 08e11291
+ 00871ba8 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a8320fe3fd9265141f998ab30ea592f"></a>

### [`00871d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871d80.md) → [`00871d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871d80.md) FUN_00871d80

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
      "definition_site": "00871d94",
      "incomplete_value": false,
      "site": "00871d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871d94",
      "incomplete_value": false,
      "site": "00871d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "00871d98",
      "DATA",
      [
        "storage",
        "00c044b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871d98",
      "DATA",
      [
        "storage",
        "00c04568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871d80.md#insn-00871d94)
- 新版 [`00871d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871d80.md#insn-00871d94)

~~~diff
- 00871d94 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00871d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00871d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871d94 bytes 08e11291
+ 00871d94 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d60f52d11b324ba21c6bbc8233139298"></a>

### [`00871da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871da4.md) → [`00871da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871da4.md) FUN_00871da4

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
      "definition_site": "00871da8",
      "incomplete_value": false,
      "site": "00871dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871da8",
      "incomplete_value": false,
      "site": "00871dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "00871dac",
      "DATA",
      [
        "storage",
        "00c044b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871dac",
      "DATA",
      [
        "storage",
        "00c04568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871da4.md#insn-00871da8)
- 新版 [`00871da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871da4.md#insn-00871da8)

~~~diff
- 00871da8 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00871da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00871da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871da8 bytes 08e11291
+ 00871da8 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-449f854ead381397bd6548c64e90957d"></a>

### [`00871e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871e30.md) → [`00871e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e30.md) FUN_00871e30

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
      "definition_site": "00871e44",
      "incomplete_value": false,
      "site": "00871e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871e44",
      "incomplete_value": false,
      "site": "00871e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00871e48",
      "DATA",
      [
        "storage",
        "00c04548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871e48",
      "DATA",
      [
        "storage",
        "00c045f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871e30.md#insn-00871e44)
- 新版 [`00871e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e30.md#insn-00871e44)

~~~diff
- 00871e44 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00871e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00871e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871e44 bytes 08211591
+ 00871e44 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8337f279ce16c39c0d8b6aa120579c6"></a>

### [`00871e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871e54.md) → [`00871e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e54.md) FUN_00871e54

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
      "definition_site": "00871e58",
      "incomplete_value": false,
      "site": "00871e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871e58",
      "incomplete_value": false,
      "site": "00871e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00871e5c",
      "DATA",
      [
        "storage",
        "00c04548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871e5c",
      "DATA",
      [
        "storage",
        "00c045f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871e54.md#insn-00871e58)
- 新版 [`00871e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871e54.md#insn-00871e58)

~~~diff
- 00871e58 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00871e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00871e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871e58 bytes 08211591
+ 00871e58 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490a788d7dde70df33ee8f77e7e0531a"></a>

### [`00871eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871eb8.md) → [`00871eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871eb8.md) FUN_00871eb8

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
      "definition_site": "00871ecc",
      "incomplete_value": false,
      "site": "00871ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ecc",
      "incomplete_value": false,
      "site": "00871ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00871ed0",
      "DATA",
      [
        "storage",
        "00c045c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ed0",
      "DATA",
      [
        "storage",
        "00c04678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871eb8.md#insn-00871ecc)
- 新版 [`00871ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871eb8.md#insn-00871ecc)

~~~diff
- 00871ecc ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00871ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00871ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ecc bytes 08211791
+ 00871ecc bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2867abfecc2f7cda7a829aad0e54167"></a>

### [`00871edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871edc.md) → [`00871edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871edc.md) FUN_00871edc

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
      "definition_site": "00871ee0",
      "incomplete_value": false,
      "site": "00871ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ee0",
      "incomplete_value": false,
      "site": "00871ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00871ee4",
      "DATA",
      [
        "storage",
        "00c045c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ee4",
      "DATA",
      [
        "storage",
        "00c04678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871edc.md#insn-00871ee0)
- 新版 [`00871ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871edc.md#insn-00871ee0)

~~~diff
- 00871ee0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00871ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00871ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871ee0 bytes 08211791
+ 00871ee0 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de90f2fa4af13e7eb164be04d35950bd"></a>

### [`00871ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871ef4.md) → [`00871ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871ef4.md) FUN_00871ef4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c140.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00871fc0",
      "incomplete_value": true,
      "site": "00871fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871fc0",
      "incomplete_value": true,
      "site": "00871fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a96:8"
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
      "definition_site": "00871fd4",
      "incomplete_value": true,
      "site": "00871fd4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00871fd4",
      "incomplete_value": true,
      "site": "00871fd4",
      "value": [
        "LOAD",
        "8",
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
      "00871fc0",
      "READ",
      [
        "storage",
        "002a3a96",
        null,
        "string"
      ]
    ],
    [
      "00871fc4",
      "READ",
      [
        "storage",
        "002a3aa4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00871fc0",
      "READ",
      [
        "storage",
        "002a3a8f",
        null,
        "string"
      ]
    ],
    [
      "00871fc4",
      "READ",
      [
        "storage",
        "002a3a9d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00871/00871ef4.md#insn-00871fb8)
- 新版 [`00871fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00871/00871ef4.md#insn-00871fb8)

~~~diff
- 00871fb8 ["COPY", "tmp:0:8", ["const:a96:8"]]
- 00871fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["COPY", "tmp:0:8", ["const:a8f:8"]]
+ 00871fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871fb8 bytes 29592a91
+ 00871fb8 bytes 293d2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ee42960b7d7071b9742ffbf1719f64d"></a>

### [`0087213c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/0087213c.md) → [`0087213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/0087213c.md) FUN_0087213c

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
      "definition_site": "00872150",
      "incomplete_value": false,
      "site": "00872154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872150",
      "incomplete_value": false,
      "site": "00872154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "00872154",
      "DATA",
      [
        "storage",
        "00c04648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872154",
      "DATA",
      [
        "storage",
        "00c046f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/0087213c.md#insn-00872150)
- 新版 [`00872150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/0087213c.md#insn-00872150)

~~~diff
- 00872150 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00872150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00872150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872150 bytes 08211991
+ 00872150 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef66b4622e86a8e6443b762006bbacbb"></a>

### [`00872160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872160.md) → [`00872160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872160.md) FUN_00872160

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
      "definition_site": "00872164",
      "incomplete_value": false,
      "site": "00872168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872164",
      "incomplete_value": false,
      "site": "00872168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "00872168",
      "DATA",
      [
        "storage",
        "00c04648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872168",
      "DATA",
      [
        "storage",
        "00c046f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872160.md#insn-00872164)
- 新版 [`00872164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872160.md#insn-00872164)

~~~diff
- 00872164 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00872164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00872164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872164 bytes 08211991
+ 00872164 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e73020f4f37d18101d8310a80c6a86e"></a>

### [`00872178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872178.md) → [`00872178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872178.md) FUN_00872178

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "008721ac",
      "incomplete_value": true,
      "site": "008721c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008721ac",
      "incomplete_value": true,
      "site": "008721c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "008721ac",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008721ac",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008721a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872178.md#insn-008721a4)
- 新版 [`008721a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872178.md#insn-008721a4)

~~~diff
- 008721a4 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 008721a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008721a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008721a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 008721a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008721a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008721a4 bytes 29593591
+ 008721a4 bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0b88f6162e82ff75ceea8edb7229e2"></a>

### [`00872294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872294.md) → [`00872294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872294.md) FUN_00872294

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
      "definition_site": "008722a8",
      "incomplete_value": false,
      "site": "008722ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008722a8",
      "incomplete_value": false,
      "site": "008722ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "008722ac",
      "DATA",
      [
        "storage",
        "00c046c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008722ac",
      "DATA",
      [
        "storage",
        "00c04778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008722a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872294.md#insn-008722a8)
- 新版 [`008722a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872294.md#insn-008722a8)

~~~diff
- 008722a8 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 008722a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008722a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008722a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 008722a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008722a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008722a8 bytes 08211b91
+ 008722a8 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aafa3ab5d0b0b3f20741e39789719c2"></a>

### [`008722b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008722b8.md) → [`008722b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722b8.md) FUN_008722b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008722bc",
      "incomplete_value": true,
      "site": "008722c0",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008722bc",
      "incomplete_value": true,
      "site": "008722c0",
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
            "const:6c8:8"
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
      "008722c0",
      "DATA",
      [
        "storage",
        "00c046c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008722c0",
      "DATA",
      [
        "storage",
        "00c04778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008722bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008722b8.md#insn-008722bc)
- 新版 [`008722bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722b8.md#insn-008722bc)

~~~diff
- 008722bc ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 008722bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008722bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008722bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["COPY", "tmp:0:8", ["const:778:8"]]
+ 008722bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008722bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008722bc bytes 08211b91
+ 008722bc bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aabf4cfceccd336595382f1511a5957"></a>

### [`008722d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008722d0.md) → [`008722d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md) FUN_008722d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872368",
      "incomplete_value": true,
      "site": "00872378",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d99:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872368",
      "incomplete_value": true,
      "site": "00872378",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da0:8"
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
      "definition_site": "0087236c",
      "incomplete_value": true,
      "site": "0087237c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0087236c",
      "incomplete_value": true,
      "site": "0087237c",
      "value": [
        "LOAD",
        "8",
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
      "00872368",
      "READ",
      [
        "storage",
        "002a6da0",
        null,
        "string"
      ]
    ],
    [
      "0087236c",
      "READ",
      [
        "storage",
        "002a6db0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872368",
      "READ",
      [
        "storage",
        "002a6d99",
        null,
        "string"
      ]
    ],
    [
      "0087236c",
      "READ",
      [
        "storage",
        "002a6da9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008722d0.md#insn-00872360) · [`00872364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008722d0.md#insn-00872364)
- 新版 [`00872360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md#insn-00872360) · [`00872364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md#insn-00872364)

~~~diff
- 00872360 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00872360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["COPY", "tmp:0:8", ["const:d99:8"]]
+ 00872360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872360 bytes 08813691
+ 00872360 bytes 08653691
- 00872364 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00872364 bytes e9d1ffd0
+ 00872364 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00872364 bytes e9d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ad651bee0342f171b6417cc2ec1a3c"></a>

### [`008725f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008725f4.md) → [`008725f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008725f4.md) FUN_008725f4

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
      "definition_site": "00872608",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872608",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "0087260c",
      "DATA",
      [
        "storage",
        "00c04748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087260c",
      "DATA",
      [
        "storage",
        "00c047f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008725f4.md#insn-00872608)
- 新版 [`00872608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008725f4.md#insn-00872608)

~~~diff
- 00872608 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00872608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00872608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872608 bytes 08211d91
+ 00872608 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c9549115a47c64bdd2d2c287a95419"></a>

### [`00872618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872618.md) → [`00872618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872618.md) FUN_00872618

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
      "definition_site": "0087261c",
      "incomplete_value": false,
      "site": "00872620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087261c",
      "incomplete_value": false,
      "site": "00872620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00872620",
      "DATA",
      [
        "storage",
        "00c04748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872620",
      "DATA",
      [
        "storage",
        "00c047f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087261c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872618.md#insn-0087261c)
- 新版 [`0087261c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872618.md#insn-0087261c)

~~~diff
- 0087261c ["COPY", "tmp:0:8", ["const:748:8"]]
- 0087261c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087261c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087261c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 0087261c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087261c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087261c bytes 08211d91
+ 0087261c bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7660639ff56a1a30fc586af31d55d8b9"></a>

### [`00872630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872630.md) → [`00872630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872630.md) FUN_00872630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008726c4",
      "incomplete_value": true,
      "site": "008726d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008726c4",
      "incomplete_value": true,
      "site": "008726d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "008726c4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008726c4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008726bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872630.md#insn-008726bc)
- 新版 [`008726bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872630.md#insn-008726bc)

~~~diff
- 008726bc ["COPY", "tmp:0:8", ["const:d56:8"]]
- 008726bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008726bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008726bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 008726bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008726bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008726bc bytes 29593591
+ 008726bc bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39813874836e8ab59eef7f7aedf66136"></a>

### [`00872790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872790.md) → [`00872790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872790.md) FUN_00872790

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
      "definition_site": "008727a4",
      "incomplete_value": false,
      "site": "008727a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008727a4",
      "incomplete_value": false,
      "site": "008727a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
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
      "008727a8",
      "DATA",
      [
        "storage",
        "00c047c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008727a8",
      "DATA",
      [
        "storage",
        "00c04878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008727a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872790.md#insn-008727a4)
- 新版 [`008727a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872790.md#insn-008727a4)

~~~diff
- 008727a4 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 008727a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008727a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008727a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 008727a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008727a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008727a4 bytes 08211f91
+ 008727a4 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-960d986525cf78f5ecaa63835810474b"></a>

### [`008727b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008727b4.md) → [`008727b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727b4.md) FUN_008727b4

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
      "definition_site": "008727b8",
      "incomplete_value": false,
      "site": "008727bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008727b8",
      "incomplete_value": false,
      "site": "008727bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
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
      "008727bc",
      "DATA",
      [
        "storage",
        "00c047c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008727bc",
      "DATA",
      [
        "storage",
        "00c04878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008727b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008727b4.md#insn-008727b8)
- 新版 [`008727b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727b4.md#insn-008727b8)

~~~diff
- 008727b8 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 008727b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008727b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008727b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 008727b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008727b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008727b8 bytes 08211f91
+ 008727b8 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134fa095161f8aeecb4796a9e2792354"></a>

### [`008727cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008727cc.md) → [`008727cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727cc.md) FUN_008727cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087292c",
      "incomplete_value": true,
      "site": "00872940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087292c",
      "incomplete_value": true,
      "site": "00872940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:93a:8"
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
      "definition_site": "00872944",
      "incomplete_value": true,
      "site": "00872944",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00872944",
      "incomplete_value": true,
      "site": "00872944",
      "value": [
        "LOAD",
        "8",
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
      "0087292c",
      "READ",
      [
        "storage",
        "0029d93a",
        null,
        "string"
      ]
    ],
    [
      "00872934",
      "READ",
      [
        "storage",
        "0029d947",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087292c",
      "READ",
      [
        "storage",
        "0029d9c7",
        null,
        "string"
      ]
    ],
    [
      "00872934",
      "READ",
      [
        "storage",
        "0029d9d4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/008727cc.md#insn-00872928)
- 新版 [`00872928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008727cc.md#insn-00872928)

~~~diff
- 00872928 ["COPY", "tmp:0:8", ["const:93a:8"]]
- 00872928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["COPY", "tmp:0:8", ["const:9c7:8"]]
+ 00872928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872928 bytes 29e92491
+ 00872928 bytes 291d2791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f4901e031d43f2943a5a9ccc46fcb52"></a>

### [`00872a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a54.md) → [`00872a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a54.md) FUN_00872a54

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
      "definition_site": "00872a68",
      "incomplete_value": false,
      "site": "00872a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872a68",
      "incomplete_value": false,
      "site": "00872a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00872a6c",
      "DATA",
      [
        "storage",
        "00c04848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872a6c",
      "DATA",
      [
        "storage",
        "00c048f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a54.md#insn-00872a68)
- 新版 [`00872a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a54.md#insn-00872a68)

~~~diff
- 00872a68 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00872a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00872a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872a68 bytes 08212191
+ 00872a68 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ad8183c18b16f8df2cc2d277aa6e6d"></a>

### [`00872a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a78.md) → [`00872a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a78.md) FUN_00872a78

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
      "definition_site": "00872a7c",
      "incomplete_value": false,
      "site": "00872a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872a7c",
      "incomplete_value": false,
      "site": "00872a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00872a80",
      "DATA",
      [
        "storage",
        "00c04848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872a80",
      "DATA",
      [
        "storage",
        "00c048f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a78.md#insn-00872a7c)
- 新版 [`00872a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a78.md#insn-00872a7c)

~~~diff
- 00872a7c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00872a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00872a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872a7c bytes 08212191
+ 00872a7c bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ed6c9033e1eeb09d5f7b4cfff1cf66"></a>

### [`00872a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a90.md) → [`00872a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a90.md) FUN_00872a90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872ac4",
      "incomplete_value": true,
      "site": "00872ad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872ac4",
      "incomplete_value": true,
      "site": "00872ad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "00872ac4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872ac4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872a90.md#insn-00872abc)
- 新版 [`00872abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872a90.md#insn-00872abc)

~~~diff
- 00872abc ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00872abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 00872abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872abc bytes 29593591
+ 00872abc bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad58f568c6076c113b2385b7942282c5"></a>

### [`00872bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872bbc.md) → [`00872bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bbc.md) FUN_00872bbc

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
      "definition_site": "00872bd0",
      "incomplete_value": false,
      "site": "00872bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872bd0",
      "incomplete_value": false,
      "site": "00872bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00872bd4",
      "DATA",
      [
        "storage",
        "00c048c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872bd4",
      "DATA",
      [
        "storage",
        "00c04978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872bbc.md#insn-00872bd0)
- 新版 [`00872bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bbc.md#insn-00872bd0)

~~~diff
- 00872bd0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00872bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00872bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872bd0 bytes 08212391
+ 00872bd0 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9167238a4a4a120ce6ae6384e5590d7d"></a>

### [`00872be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872be0.md) → [`00872be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872be0.md) FUN_00872be0

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
      "definition_site": "00872be4",
      "incomplete_value": false,
      "site": "00872be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872be4",
      "incomplete_value": false,
      "site": "00872be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00872be8",
      "DATA",
      [
        "storage",
        "00c048c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872be8",
      "DATA",
      [
        "storage",
        "00c04978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872be0.md#insn-00872be4)
- 新版 [`00872be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872be0.md#insn-00872be4)

~~~diff
- 00872be4 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00872be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00872be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872be4 bytes 08212391
+ 00872be4 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7893103cfcd98bf219f80a0cfabf91"></a>

### [`00872bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872bf8.md) → [`00872bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bf8.md) FUN_00872bf8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`007f96a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f96a4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872d80",
      "incomplete_value": true,
      "site": "00872d94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872d80",
      "incomplete_value": true,
      "site": "00872d94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a96:8"
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
      "definition_site": "00872d98",
      "incomplete_value": true,
      "site": "00872d98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00872d98",
      "incomplete_value": true,
      "site": "00872d98",
      "value": [
        "LOAD",
        "8",
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
      "00872d80",
      "READ",
      [
        "storage",
        "002a3a96",
        null,
        "string"
      ]
    ],
    [
      "00872d88",
      "READ",
      [
        "storage",
        "002a3aa4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872d80",
      "READ",
      [
        "storage",
        "002a3a8f",
        null,
        "string"
      ]
    ],
    [
      "00872d88",
      "READ",
      [
        "storage",
        "002a3a9d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872bf8.md#insn-00872d7c)
- 新版 [`00872d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872bf8.md#insn-00872d7c)

~~~diff
- 00872d7c ["COPY", "tmp:0:8", ["const:a96:8"]]
- 00872d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["COPY", "tmp:0:8", ["const:a8f:8"]]
+ 00872d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872d7c bytes 29592a91
+ 00872d7c bytes 293d2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b52456b69fa27b7b39f555aa136fa13"></a>

### [`00872eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872eb4.md) → [`00872eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872eb4.md) FUN_00872eb4

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
      "definition_site": "00872ec8",
      "incomplete_value": false,
      "site": "00872ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872ec8",
      "incomplete_value": false,
      "site": "00872ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00872ecc",
      "DATA",
      [
        "storage",
        "00c04948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872ecc",
      "DATA",
      [
        "storage",
        "00c049f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872eb4.md#insn-00872ec8)
- 新版 [`00872ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872eb4.md#insn-00872ec8)

~~~diff
- 00872ec8 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00872ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00872ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872ec8 bytes 08212591
+ 00872ec8 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98e76e1c858d81cf3b09a0787b426c1e"></a>

### [`00872ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872ed8.md) → [`00872ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ed8.md) FUN_00872ed8

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
      "definition_site": "00872edc",
      "incomplete_value": false,
      "site": "00872ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872edc",
      "incomplete_value": false,
      "site": "00872ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00872ee0",
      "DATA",
      [
        "storage",
        "00c04948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872ee0",
      "DATA",
      [
        "storage",
        "00c049f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872ed8.md#insn-00872edc)
- 新版 [`00872edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ed8.md#insn-00872edc)

~~~diff
- 00872edc ["COPY", "tmp:0:8", ["const:948:8"]]
- 00872edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00872edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00872edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00872edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00872edc bytes 08212591
+ 00872edc bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6717bfceb701aa60affe2b501660c7f"></a>

### [`00872ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872ef0.md) → [`00872ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ef0.md) FUN_00872ef0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872f84",
      "incomplete_value": true,
      "site": "00872f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872f84",
      "incomplete_value": true,
      "site": "00872f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "00872f84",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872f84",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00872/00872ef0.md#insn-00872f7c)
- 新版 [`00872f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/00872ef0.md#insn-00872f7c)

~~~diff
- 00872f7c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00872f7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872f7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872f7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 00872f7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872f7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872f7c bytes 29593591
+ 00872f7c bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9667c458d1193080cdecfad5413a3b2a"></a>

### [`00873050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873050.md) → [`00873050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873050.md) FUN_00873050

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
      "definition_site": "00873064",
      "incomplete_value": false,
      "site": "00873068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873064",
      "incomplete_value": false,
      "site": "00873068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "00873068",
      "DATA",
      [
        "storage",
        "00c049c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873068",
      "DATA",
      [
        "storage",
        "00c04a78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873050.md#insn-00873064)
- 新版 [`00873064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873050.md#insn-00873064)

~~~diff
- 00873064 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00873064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00873064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873064 bytes 08212791
+ 00873064 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28549422fd872fdda26f7d6dcb822579"></a>

### [`00873074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873074.md) → [`00873074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873074.md) FUN_00873074

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
      "definition_site": "00873078",
      "incomplete_value": false,
      "site": "0087307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873078",
      "incomplete_value": false,
      "site": "0087307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "0087307c",
      "DATA",
      [
        "storage",
        "00c049c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087307c",
      "DATA",
      [
        "storage",
        "00c04a78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873074.md#insn-00873078)
- 新版 [`00873078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873074.md#insn-00873078)

~~~diff
- 00873078 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00873078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00873078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873078 bytes 08212791
+ 00873078 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

