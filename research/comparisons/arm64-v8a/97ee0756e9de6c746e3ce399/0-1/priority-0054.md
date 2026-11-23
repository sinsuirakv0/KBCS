# v15.7.2 → v15.7.3 · 最優先の変更候補 (54)

[一覧の目次](README.md)

<a id="compare-e539d95ed4c969fb6ccfadfc255bf1e1"></a>

### [`00a4e288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e288.md) → [`00a4e288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e288.md) FUN_00a4e288

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a45be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a45/00a45be0.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00846/00846f70.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md)
- 新版 呼出元 1件 [`00a45be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a45be0.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f70.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e2bc",
      "incomplete_value": false,
      "site": "00a4e2c0",
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
      "definition_site": "00a4e2bc",
      "incomplete_value": false,
      "site": "00a4e2c0",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e304",
      "incomplete_value": false,
      "site": "00a4e30c",
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
      "definition_site": "00a4e304",
      "incomplete_value": false,
      "site": "00a4e30c",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e354",
      "incomplete_value": false,
      "site": "00a4e35c",
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
            "const:e12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e354",
      "incomplete_value": false,
      "site": "00a4e35c",
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
            "const:d85:8"
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
      "00a4e2c0",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "00a4e2ec",
      "DATA",
      [
        "storage",
        "002a2b96",
        null,
        "string"
      ]
    ],
    [
      "00a4e30c",
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
      "00a4e2c0",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "00a4e2ec",
      "DATA",
      [
        "storage",
        "002a2b8f",
        null,
        "string"
      ]
    ],
    [
      "00a4e30c",
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

- 旧版 [`00a4e2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e288.md#insn-00a4e2bc) · [`00a4e2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e288.md#insn-00a4e2e0) · [`00a4e304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e288.md#insn-00a4e304)
- 新版 [`00a4e2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e288.md#insn-00a4e2bc) · [`00a4e2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e288.md#insn-00a4e2e0) · [`00a4e304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e288.md#insn-00a4e304)

~~~diff
- 00a4e2bc ["COPY", "tmp:0:8", ["const:617:8"]]
- 00a4e2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2bc ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 00a4e2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e2bc bytes 085d1891
+ 00a4e2bc bytes 08911a91
- 00a4e2e0 ["COPY", "tmp:0:8", ["const:b96:8"]]
- 00a4e2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2e0 ["COPY", "tmp:0:8", ["const:b8f:8"]]
+ 00a4e2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e2e0 bytes 08592e91
+ 00a4e2e0 bytes 083d2e91
- 00a4e304 ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 00a4e304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e304 ["COPY", "tmp:0:8", ["const:731:8"]]
+ 00a4e304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e304 bytes 08911a91
+ 00a4e304 bytes 08c51c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e64d89810a443617983911d625bde02"></a>

### [`00a4e50c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e50c.md) → [`00a4e50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e50c.md) FUN_00a4e50c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a45be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a45/00a45be0.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00846/00846f70.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md)
- 新版 呼出元 1件 [`00a45be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a45be0.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00846/00846f70.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e540",
      "incomplete_value": false,
      "site": "00a4e544",
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
      "definition_site": "00a4e540",
      "incomplete_value": false,
      "site": "00a4e544",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e564",
      "incomplete_value": false,
      "site": "00a4e570",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e564",
      "incomplete_value": false,
      "site": "00a4e570",
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
            "const:57b:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e588",
      "incomplete_value": false,
      "site": "00a4e590",
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
      "definition_site": "00a4e588",
      "incomplete_value": false,
      "site": "00a4e590",
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
      "00a4e544",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "00a4e570",
      "DATA",
      [
        "storage",
        "0029957b",
        null,
        "string"
      ]
    ],
    [
      "00a4e590",
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
      "00a4e544",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "00a4e570",
      "DATA",
      [
        "storage",
        "00299608",
        null,
        "string"
      ]
    ],
    [
      "00a4e590",
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

- 旧版 [`00a4e540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e50c.md#insn-00a4e540) · [`00a4e564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e50c.md#insn-00a4e564) · [`00a4e56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e50c.md#insn-00a4e56c)
- 新版 [`00a4e540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e50c.md#insn-00a4e540) · [`00a4e564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e50c.md#insn-00a4e564)

~~~diff
- 00a4e540 ["COPY", "tmp:0:8", ["const:617:8"]]
- 00a4e540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e540 ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 00a4e540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e540 bytes 085d1891
+ 00a4e540 bytes 08911a91
- 00a4e564 ["COPY", "tmp:0:8", ["const:57b:8"]]
- 00a4e564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e564 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00a4e564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e564 bytes 08ed1591
+ 00a4e564 bytes 08211891
- 00a4e56c ["COPY", "register:4008:8", ["register:8:8"]]
- 00a4e56c bytes e1030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeec18b9b67dacf0d861fc62f9bdd491"></a>

### [`00a4e790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e790.md) → [`00a4e790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e790.md) FUN_00a4e790

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`00a4531c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a45/00a4531c.md) [`00a45be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a45/00a45be0.md) [`00a476c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a47/00a476c4.md) [`00a47e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a47/00a47e7c.md) [`00a48eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a48/00a48eb8.md) · 呼出先 10件 [`007cf4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf4b0.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`007d0b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d0/007d0b74.md)
- 新版 呼出元 7件 [`00a4531c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a4531c.md) [`00a45be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a45/00a45be0.md) [`00a476c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a47/00a476c4.md) [`00a47e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a47/00a47e7c.md) [`00a48eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a48/00a48eb8.md) · 呼出先 10件 [`007cf4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf4b0.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`007d0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d0/007d0b74.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e7c0",
      "incomplete_value": false,
      "site": "00a4e7c4",
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
      "definition_site": "00a4e7c0",
      "incomplete_value": false,
      "site": "00a4e7c4",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e7e4",
      "incomplete_value": true,
      "site": "00a4e7f0",
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
            "const:9a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e7e4",
      "incomplete_value": true,
      "site": "00a4e7f0",
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
            "const:9aa:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4e81c",
      "incomplete_value": false,
      "site": "00a4e820",
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
      "definition_site": "00a4e81c",
      "incomplete_value": false,
      "site": "00a4e820",
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
      "00a4e7c4",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "00a4e7f0",
      "DATA",
      [
        "storage",
        "002a69aa",
        null,
        "string"
      ]
    ],
    [
      "00a4e820",
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
      "00a4e7c4",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "00a4e7f0",
      "DATA",
      [
        "storage",
        "002a69a3",
        null,
        "string"
      ]
    ],
    [
      "00a4e820",
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

- 旧版 [`00a4e7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e790.md#insn-00a4e7c0) · [`00a4e7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e790.md#insn-00a4e7e4) · [`00a4e81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4e790.md#insn-00a4e81c)
- 新版 [`00a4e7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e790.md#insn-00a4e7c0) · [`00a4e7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e790.md#insn-00a4e7e4) · [`00a4e81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4e790.md#insn-00a4e81c)

~~~diff
- 00a4e7c0 ["COPY", "tmp:0:8", ["const:617:8"]]
- 00a4e7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7c0 ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 00a4e7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e7c0 bytes 085d1891
+ 00a4e7c0 bytes 08911a91
- 00a4e7e4 ["COPY", "tmp:0:8", ["const:9aa:8"]]
- 00a4e7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7e4 ["COPY", "tmp:0:8", ["const:9a3:8"]]
+ 00a4e7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e7e4 bytes 08a92691
+ 00a4e7e4 bytes 088d2691
- 00a4e81c ["COPY", "tmp:0:8", ["const:6a4:8"]]
- 00a4e81c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e81c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e81c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4e81c ["COPY", "tmp:0:8", ["const:731:8"]]
+ 00a4e81c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e81c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4e81c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e81c bytes 08911a91
+ 00a4e81c bytes 08c51c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f586a48ee685699be10be395a42677a1"></a>

### [`00a4ec40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4ec40.md) → [`00a4ec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md) FUN_00a4ec40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`004508a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/004508a4.md) [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) [`00829bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829bb8.md) [`008594d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md) [`0087ab54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab54.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`005bc058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bc058.md) [`00759ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/00821cb4.md)
- 新版 呼出元 5件 [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00829bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829bb8.md) [`008594d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md) [`0087ab54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab54.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`005bc058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc058.md) [`00759ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4ed14",
      "incomplete_value": false,
      "site": "00a4ed14",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4ed14",
      "incomplete_value": false,
      "site": "00a4ed14",
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
            "const:f45:8"
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
      "definition_site": "00a4ed54",
      "incomplete_value": true,
      "site": "00a4ed54",
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
            "const:731:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4ed54",
      "incomplete_value": true,
      "site": "00a4ed54",
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
            "const:6a4:8"
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
      "definition_site": "00a4eda4",
      "incomplete_value": false,
      "site": "00a4eda4",
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
            "const:22c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4eda4",
      "incomplete_value": false,
      "site": "00a4eda4",
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
            "const:19f:8"
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
      "00a4ecc0",
      "READ",
      [
        "storage",
        "002a9e46",
        null,
        "string"
      ]
    ],
    [
      "00a4ece8",
      "DATA",
      [
        "storage",
        "0029e617",
        null,
        "string"
      ]
    ],
    [
      "00a4ed14",
      "DATA",
      [
        "storage",
        "002a6f45",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a4ecc0",
      "READ",
      [
        "storage",
        "002a9e4c",
        null,
        "string"
      ]
    ],
    [
      "00a4ece8",
      "DATA",
      [
        "storage",
        "0029e6a4",
        null,
        "string"
      ]
    ],
    [
      "00a4ed14",
      "DATA",
      [
        "storage",
        "002a6f3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4ecb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4ec40.md#insn-00a4ecb4) · [`00a4ecd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4ec40.md#insn-00a4ecd4) · [`00a4ed08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4ec40.md#insn-00a4ed08)
- 新版 [`00a4ecb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md#insn-00a4ecb4) · [`00a4ecd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md#insn-00a4ecd4) · [`00a4ed08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md#insn-00a4ed08)

~~~diff
- 00a4ecb4 ["COPY", "tmp:0:8", ["const:e46:8"]]
- 00a4ecb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a4ecb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a4ecb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a4ecb4 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00a4ecb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a4ecb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a4ecb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a4ecb4 bytes 29193991
+ 00a4ecb4 bytes 29313991
- 00a4ecd4 ["COPY", "tmp:0:8", ["const:617:8"]]
- 00a4ecd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4ecd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4ecd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4ecd4 ["COPY", "tmp:0:8", ["const:6a4:8"]]
+ 00a4ecd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4ecd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4ecd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4ecd4 bytes 085d1891
+ 00a4ecd4 bytes 08911a91
- 00a4ed08 ["COPY", "tmp:0:8", ["const:f45:8"]]
- 00a4ed08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4ed08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4ed08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4ed08 ["COPY", "tmp:0:8", ["const:f3e:8"]]
+ 00a4ed08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4ed08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4ed08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4ed08 bytes 08153d91
+ 00a4ed08 bytes 08f93c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6eb254934fc310b4ef7e7bbb4055be"></a>

### [`00a4f438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4f/00a4f438.md) → [`00a4f438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4f438.md) FUN_00a4f438

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md)
- 新版 呼出元 1件 [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.32% / 新版 96.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4f4b0",
      "incomplete_value": false,
      "site": "00a4f4b4",
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
      "definition_site": "00a4f4b0",
      "incomplete_value": false,
      "site": "00a4f4b4",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a4f4cc",
      "incomplete_value": true,
      "site": "00a4f4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4f4cc",
      "incomplete_value": true,
      "site": "00a4f4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c13:8"
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
      "definition_site": "00a4f4cc",
      "incomplete_value": true,
      "site": "00a4f4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "00a4f4cc",
      "incomplete_value": true,
      "site": "00a4f4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a4f4b4",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4f4cc",
      "READ",
      [
        "storage",
        "002a3c13",
        null,
        "string"
      ]
    ],
    [
      "00a4f4cc",
      "READ",
      [
        "storage",
        "002a3c23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a4f4b4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4f4cc",
      "READ",
      [
        "storage",
        "002a3c0c",
        null,
        "string"
      ]
    ],
    [
      "00a4f4cc",
      "READ",
      [
        "storage",
        "002a3c1c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4f4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4f/00a4f438.md#insn-00a4f4b0) · [`00a4f4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4f/00a4f438.md#insn-00a4f4c4) · [`00a4f4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4f/00a4f438.md#insn-00a4f4c8)
- 新版 [`00a4f4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4f438.md#insn-00a4f4b0) · [`00a4f4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4f438.md#insn-00a4f4c4)

~~~diff
- 00a4f4b0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a4f4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4f4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4f4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4b0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a4f4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4f4b0 bytes 08e13191
+ 00a4f4b0 bytes 08a13491
- 00a4f4c4 ["COPY", "tmp:0:8", ["const:c13:8"]]
- 00a4f4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4f4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4f4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4c4 ["COPY", "tmp:0:8", ["const:c0c:8"]]
+ 00a4f4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a4f4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4f4c4 bytes 084d3091
+ 00a4f4c4 bytes 08313091
- 00a4f4c8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00a4f4c8 bytes 09c3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-436051b2496cbb089ee3edde7168a059"></a>

### [`00a5178c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a51/00a5178c.md) → [`00a5178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a5178c.md) FUN_00a5178c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

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
      "definition_site": "00a517d0",
      "incomplete_value": false,
      "site": "00a517dc",
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
      "definition_site": "00a517d0",
      "incomplete_value": false,
      "site": "00a517dc",
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
      "definition_site": "00a51810",
      "incomplete_value": true,
      "site": "00a5182c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a51810",
      "incomplete_value": true,
      "site": "00a5182c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f8f:8"
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
      "definition_site": "00a51830",
      "incomplete_value": true,
      "site": "00a51830",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00a51830",
      "incomplete_value": true,
      "site": "00a51830",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "00a517dc",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a51810",
      "READ",
      [
        "storage",
        "002a5f8f",
        null,
        "string"
      ]
    ],
    [
      "00a51818",
      "READ",
      [
        "storage",
        "002a5f9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a517dc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a51810",
      "READ",
      [
        "storage",
        "002a5f88",
        null,
        "string"
      ]
    ],
    [
      "00a51818",
      "READ",
      [
        "storage",
        "002a5f95",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a517d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a51/00a5178c.md#insn-00a517d0) · [`00a5180c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a51/00a5178c.md#insn-00a5180c) · [`00a51c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a51/00a5178c.md#insn-00a51c7c)
- 新版 [`00a517d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a5178c.md#insn-00a517d0) · [`00a5180c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a5178c.md#insn-00a5180c) · [`00a51c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a5178c.md#insn-00a51c7c)

~~~diff
- 00a517d0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a517d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a517d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a517d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a517d0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a517d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a517d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a517d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a517d0 bytes 08e13191
+ 00a517d0 bytes 08a13491
- 00a5180c ["COPY", "tmp:0:8", ["const:f8f:8"]]
- 00a5180c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a5180c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a5180c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a5180c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a5180c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5180c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5180c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a5180c bytes 293d3e91
+ 00a5180c bytes 29213e91
- 00a51c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00a51c7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a51c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00a51c7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a51c7c bytes 086146f9
+ 00a51c7c bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c14b3e7419d16c2372f18803c1c73a2"></a>

### [`00a534a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a534a0.md) → [`00a534a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534a0.md) FUN_00a534a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00a5178c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a51/00a5178c.md) [`00a52710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a52/00a52710.md) [`00a52904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a52/00a52904.md) [`00a53778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53778.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`00a5178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a51/00a5178c.md) [`00a52710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52710.md) [`00a52904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52904.md) [`00a53778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53778.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00a534ac",
      "incomplete_value": false,
      "site": "00a534b0",
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
      "definition_site": "00a534ac",
      "incomplete_value": false,
      "site": "00a534b0",
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
      "00a534ac",
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
      "00a534ac",
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

- 旧版 [`00a534ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a534a0.md#insn-00a534ac)
- 新版 [`00a534ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a534a0.md#insn-00a534ac)

~~~diff
- 00a534ac ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a534ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a534ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a534ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a534ac ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a534ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a534ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a534ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a534ac bytes 00280c91
+ 00a534ac bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e96cab0a76604d0b97c641ce4861acd"></a>

### [`00a53840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53840.md) → [`00a53840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53840.md) _INIT_229

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
      "definition_site": "00a5387c",
      "incomplete_value": true,
      "site": "00a53898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5387c",
      "incomplete_value": true,
      "site": "00a53898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a538a0",
      "incomplete_value": true,
      "site": "00a538bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a538a0",
      "incomplete_value": true,
      "site": "00a538bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a538c0",
      "incomplete_value": true,
      "site": "00a538dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a538c0",
      "incomplete_value": true,
      "site": "00a538dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5387c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a538a0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a538c0",
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
      "00a5387c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a538a0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a538c0",
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

- 旧版 [`00a5386c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53840.md#insn-00a5386c) · [`00a53874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53840.md#insn-00a53874)
- 新版 [`00a5386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53840.md#insn-00a5386c) · [`00a53874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53840.md#insn-00a53874)

~~~diff
- 00a5386c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00a5386c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5386c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5386c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5386c ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00a5386c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5386c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5386c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5386c bytes 73222191
+ 00a5386c bytes 73222491
- 00a53874 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a53874 bytes a9c2ff90
+ 00a53874 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a53874 bytes a9c2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e23c255b23750a97428b21a38dbde627"></a>

### [`00a53bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53bd0.md) → [`00a53bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53bd0.md) _INIT_230

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a53c50",
      "incomplete_value": true,
      "site": "00a53c6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a53c50",
      "incomplete_value": true,
      "site": "00a53c6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a53c70",
      "incomplete_value": true,
      "site": "00a53c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a53c70",
      "incomplete_value": true,
      "site": "00a53c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "definition_site": "00a53ccc",
      "incomplete_value": true,
      "site": "00a53d10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a53ccc",
      "incomplete_value": true,
      "site": "00a53d10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:526:8"
              ]
            ]
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
      "00a53c0c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a53c30",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a53c50",
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
      "00a53c0c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a53c30",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a53c50",
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

- 旧版 [`00a53bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53bd0.md#insn-00a53bfc) · [`00a53c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53bd0.md#insn-00a53c04)
- 新版 [`00a53bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53bd0.md#insn-00a53bfc) · [`00a53c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53bd0.md#insn-00a53c04)

~~~diff
- 00a53bfc ["COPY", "tmp:0:8", ["const:860:8"]]
- 00a53bfc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a53bfc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a53bfc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a53bfc ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00a53bfc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a53bfc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a53bfc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a53bfc bytes 73822191
+ 00a53bfc bytes 73822491
- 00a53c04 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a53c04 bytes a9c2ff90
+ 00a53c04 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a53c04 bytes a9c2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e767b69efc2262dacea9c92d890bc6ac"></a>

### [`00a53f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53f60.md) → [`00a53f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53f60.md) FUN_00a53f60

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a547f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a547f4.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00657/00657e7c.md) [`00831724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00832/00832580.md)
- 新版 呼出元 1件 [`00a547f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a547f4.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.54% / 新版 89.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 7件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a53f98",
      "incomplete_value": false,
      "site": "00a53f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a53f98",
      "incomplete_value": false,
      "site": "00a53f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00a5401c",
      "incomplete_value": true,
      "site": "00a5401c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a5401c",
      "incomplete_value": true,
      "site": "00a5401c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a54034",
      "incomplete_value": true,
      "site": "00a54034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a54034",
      "incomplete_value": true,
      "site": "00a54034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00a53f9c",
      "DATA",
      [
        "storage",
        "00c0d648",
        null,
        "pointer"
      ]
    ],
    [
      "00a53fec",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a5400c",
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
      "00a53f9c",
      "DATA",
      [
        "storage",
        "00c0d6f8",
        null,
        "pointer"
      ]
    ],
    [
      "00a53fec",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a5400c",
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

- 旧版 [`00a53f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53f60.md#insn-00a53f98) · [`00a53fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a53/00a53f60.md#insn-00a53fa0)
- 新版 [`00a53f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53f60.md#insn-00a53f98) · [`00a53fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a53/00a53f60.md#insn-00a53fa0)

~~~diff
- 00a53f98 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00a53f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a53f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a53f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a53f98 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00a53f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a53f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a53f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a53f98 bytes 08211991
+ 00a53f98 bytes 08e11b91
- 00a53fa0 ["COPY", "register:40c0:8", ["const:c24000:8"]]
- 00a53fa0 bytes 980e00b0
+ 00a53fa0 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 00a53fa0 bytes 980e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a0fa59c77af2f2b5f8dc58a34b71fd9"></a>

### [`00a547f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a547f4.md) → [`00a547f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a547f4.md) FUN_00a547f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 19件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00646dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00646/00646dc4.md) [`007cd294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd294.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 19件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`007cd294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd294.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.84% / 新版 97.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a54840",
      "incomplete_value": false,
      "site": "00a54840",
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
      "definition_site": "00a54840",
      "incomplete_value": false,
      "site": "00a54840",
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a54838",
      "incomplete_value": true,
      "site": "00a54840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a54838",
      "incomplete_value": true,
      "site": "00a54840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a54844",
      "incomplete_value": false,
      "site": "00a54844",
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
      "definition_site": "00a54844",
      "incomplete_value": false,
      "site": "00a54844",
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
      "00a54838",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a5483c",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a54840",
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
      "00a54838",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a5483c",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00a54840",
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

- 旧版 [`00a54840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a547f4.md#insn-00a54840) · [`00a54844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a547f4.md#insn-00a54844) · [`00a54884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a547f4.md#insn-00a54884)
- 新版 [`00a54840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a547f4.md#insn-00a54840) · [`00a54844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a547f4.md#insn-00a54844) · [`00a54884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a547f4.md#insn-00a54884)

~~~diff
- 00a54840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00a54840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00a54840 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 00a54840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a54840 bytes 09d504f9
+ 00a54840 bytes 093505f9
- 00a54844 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 00a54844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00a54844 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00a54844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a54844 bytes cade04f9
+ 00a54844 bytes ca3e05f9
- 00a54884 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 00a54884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00a54884 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00a54884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a54884 bytes d4de04f9
+ 00a54884 bytes d43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe045f5667f3c4fb044cca43afa42a9"></a>

### [`00a54eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a54eb8.md) → [`00a54eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54eb8.md) FUN_00a54eb8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 55件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 55件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.01% / 新版 96.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `store_destination` 11件, `store_value` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a551e4",
      "incomplete_value": false,
      "site": "00a551e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a551e4",
      "incomplete_value": false,
      "site": "00a551e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00a55214",
      "incomplete_value": false,
      "site": "00a55214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a55214",
      "incomplete_value": false,
      "site": "00a55214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a55f04",
      "incomplete_value": false,
      "site": "00a55f04",
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
      "definition_site": "00a55f04",
      "incomplete_value": false,
      "site": "00a55f04",
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
    "ordinal": 108,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a551c4",
      "PARAM",
      [
        "storage",
        "0029308a",
        null,
        "string"
      ]
    ],
    [
      "00a551e4",
      "DATA",
      [
        "storage",
        "00c0d668",
        null,
        "undefined *"
      ]
    ],
    [
      "00a55214",
      "DATA",
      [
        "storage",
        "00c0d6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a551c4",
      "PARAM",
      [
        "storage",
        "00293117",
        null,
        "string"
      ]
    ],
    [
      "00a551e4",
      "DATA",
      [
        "storage",
        "00c0d718",
        null,
        "undefined *"
      ]
    ],
    [
      "00a55214",
      "DATA",
      [
        "storage",
        "00c0d798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a551c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a54eb8.md#insn-00a551c4) · [`00a551e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a54eb8.md#insn-00a551e0) · [`00a55210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a54/00a54eb8.md#insn-00a55210)
- 新版 [`00a551c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54eb8.md#insn-00a551c4) · [`00a551e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54eb8.md#insn-00a551e0) · [`00a55210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a54/00a54eb8.md#insn-00a55210)

~~~diff
- 00a551c4 ["COPY", "tmp:0:8", ["const:8a:8"]]
- 00a551c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a551c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a551c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a551c4 ["COPY", "tmp:0:8", ["const:117:8"]]
+ 00a551c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a551c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a551c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a551c4 bytes 21280291
+ 00a551c4 bytes 215c0491
- 00a551e0 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00a551e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a551e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a551e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a551e0 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00a551e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a551e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a551e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a551e0 bytes 08a11991
+ 00a551e0 bytes 08611c91
- 00a55210 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00a55210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a55210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a55210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a55210 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00a55210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a55210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a55210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a55210 bytes 08a11b91
+ 00a55210 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f84736f44028b84394cb147cdae2b1f"></a>

### [`00a58454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a58/00a58454.md) → [`00a58454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a58/00a58454.md) FUN_00a58454

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 38件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 38件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a584a4",
      "incomplete_value": true,
      "site": "00a584a4",
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
      "definition_site": "00a584a4",
      "incomplete_value": true,
      "site": "00a584a4",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a584b4",
      "incomplete_value": true,
      "site": "00a584b4",
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
      "definition_site": "00a584b4",
      "incomplete_value": true,
      "site": "00a584b4",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a58504",
      "incomplete_value": true,
      "site": "00a58504",
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
      "definition_site": "00a58504",
      "incomplete_value": true,
      "site": "00a58504",
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
      "00a58494",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a584a0",
      "READ",
      [
        "storage",
        "00c24f70",
        null,
        "undefined8"
      ]
    ],
    [
      "00a584b0",
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
      "00a58494",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a584a0",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "00a584b0",
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

- 旧版 [`00a5847c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a58/00a58454.md#insn-00a5847c) · [`00a58480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a58/00a58454.md#insn-00a58480) · [`00a5849c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a58/00a58454.md#insn-00a5849c)
- 新版 [`00a5847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a58/00a58454.md#insn-00a5847c) · [`00a58480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a58/00a58454.md#insn-00a58480) · [`00a5849c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a58/00a58454.md#insn-00a5849c)

~~~diff
- 00a5847c ["COPY", "register:40a0:8", ["const:c24000:8"]]
+ 00a5847c ["COPY", "register:40a0:8", ["const:c25000:8"]]
- 00a5847c bytes 740e0090
+ 00a5847c bytes 740e00b0
- 00a58480 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a58480 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00a58480 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00a58480 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00a58480 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00a58480 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00a58480 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00a58480 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00a58480 bytes 94e23d91
+ 00a58480 bytes 94e20091
- 00a5849c ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00a5849c ["COPY", "register:4098:8", ["const:c25000:8"]]
- 00a5849c bytes 730e0090
+ 00a5849c bytes 730e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3634e6a274305975c210b7e3b0db7c"></a>

### [`00a59a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59a5c.md) → [`00a59a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59a5c.md) FUN_00a59a5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0064c428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a59a6c",
      "incomplete_value": false,
      "site": "00a59a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59a6c",
      "incomplete_value": false,
      "site": "00a59a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00a59a98",
      "incomplete_value": false,
      "site": "00a59a9c",
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
      "definition_site": "00a59a98",
      "incomplete_value": false,
      "site": "00a59a9c",
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
      "00a59a74",
      "DATA",
      [
        "storage",
        "00c0d648",
        null,
        "pointer"
      ]
    ],
    [
      "00a59a9c",
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
      "00a59a74",
      "DATA",
      [
        "storage",
        "00c0d6f8",
        null,
        "pointer"
      ]
    ],
    [
      "00a59a9c",
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

- 旧版 [`00a59a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59a5c.md#insn-00a59a6c) · [`00a59a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59a5c.md#insn-00a59a98)
- 新版 [`00a59a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59a5c.md#insn-00a59a6c) · [`00a59a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59a5c.md#insn-00a59a98)

~~~diff
- 00a59a6c ["COPY", "tmp:0:8", ["const:648:8"]]
- 00a59a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59a6c ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00a59a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59a6c bytes 08211991
+ 00a59a6c bytes 08e11b91
- 00a59a98 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00a59a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59a98 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00a59a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59a98 bytes 08a10791
+ 00a59a98 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4231f1aefcb0f37aa8426dbea2f9eb71"></a>

### [`00a59adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59adc.md) → [`00a59adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59adc.md) FUN_00a59adc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0064c428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a59aec",
      "incomplete_value": false,
      "site": "00a59af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59aec",
      "incomplete_value": false,
      "site": "00a59af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00a59b18",
      "incomplete_value": false,
      "site": "00a59b1c",
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
      "definition_site": "00a59b18",
      "incomplete_value": false,
      "site": "00a59b1c",
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
      "00a59af4",
      "DATA",
      [
        "storage",
        "00c0d648",
        null,
        "pointer"
      ]
    ],
    [
      "00a59b1c",
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
      "00a59af4",
      "DATA",
      [
        "storage",
        "00c0d6f8",
        null,
        "pointer"
      ]
    ],
    [
      "00a59b1c",
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

- 旧版 [`00a59aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59adc.md#insn-00a59aec) · [`00a59b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59adc.md#insn-00a59b18)
- 新版 [`00a59aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59adc.md#insn-00a59aec) · [`00a59b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59adc.md#insn-00a59b18)

~~~diff
- 00a59aec ["COPY", "tmp:0:8", ["const:648:8"]]
- 00a59aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59aec ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00a59aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59aec bytes 08211991
+ 00a59aec bytes 08e11b91
- 00a59b18 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00a59b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59b18 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00a59b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59b18 bytes 08a10791
+ 00a59b18 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c60e31312e7a5fa543415bfbcafe6394"></a>

### [`00a59b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59b68.md) → [`00a59b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59b68.md) FUN_00a59b68

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
      "definition_site": "00a59b8c",
      "incomplete_value": true,
      "site": "00a59b8c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59b8c",
      "incomplete_value": true,
      "site": "00a59b8c",
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
            "const:668:8"
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
      "00a59b8c",
      "DATA",
      [
        "storage",
        "00c0d668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59b8c",
      "DATA",
      [
        "storage",
        "00c0d718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59b68.md#insn-00a59b88)
- 新版 [`00a59b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59b68.md#insn-00a59b88)

~~~diff
- 00a59b88 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00a59b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59b88 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00a59b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59b88 bytes 08a11991
+ 00a59b88 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbcb9b752572d4f127715ac158131829"></a>

### [`00a59b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59b9c.md) → [`00a59b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59b9c.md) FUN_00a59b9c

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
      "definition_site": "00a59ba8",
      "incomplete_value": false,
      "site": "00a59ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59ba8",
      "incomplete_value": false,
      "site": "00a59ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00a59ba8",
      "DATA",
      [
        "storage",
        "00c0d668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59ba8",
      "DATA",
      [
        "storage",
        "00c0d718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59b9c.md#insn-00a59ba4)
- 新版 [`00a59ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59b9c.md#insn-00a59ba4)

~~~diff
- 00a59ba4 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00a59ba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a59ba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a59ba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a59ba4 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00a59ba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59ba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59ba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a59ba4 bytes 29a11991
+ 00a59ba4 bytes 29611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d504ce550b6f13634e738c78d52cf490"></a>

### [`00a59c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59c60.md) → [`00a59c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59c60.md) FUN_00a59c60

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
      "definition_site": "00a59c84",
      "incomplete_value": false,
      "site": "00a59c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59c84",
      "incomplete_value": false,
      "site": "00a59c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "00a59c84",
      "DATA",
      [
        "storage",
        "00c0d6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59c84",
      "DATA",
      [
        "storage",
        "00c0d798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59c60.md#insn-00a59c80)
- 新版 [`00a59c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59c60.md#insn-00a59c80)

~~~diff
- 00a59c80 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00a59c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59c80 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00a59c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59c80 bytes 08a11b91
+ 00a59c80 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2f6e5627cb6ce6b8ce3c91f0b454e48"></a>

### [`00a59c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59c94.md) → [`00a59c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59c94.md) FUN_00a59c94

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
      "definition_site": "00a59ca0",
      "incomplete_value": false,
      "site": "00a59ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59ca0",
      "incomplete_value": false,
      "site": "00a59ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "00a59ca0",
      "DATA",
      [
        "storage",
        "00c0d6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59ca0",
      "DATA",
      [
        "storage",
        "00c0d798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59c94.md#insn-00a59c9c)
- 新版 [`00a59c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59c94.md#insn-00a59c9c)

~~~diff
- 00a59c9c ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00a59c9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a59c9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a59c9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a59c9c ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00a59c9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59c9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59c9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a59c9c bytes 29a11b91
+ 00a59c9c bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdfd93c40fff4e450f2dfcf0116074b"></a>

### [`00a59ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59ef8.md) → [`00a59ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59ef8.md) FUN_00a59ef8

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
      "definition_site": "00a59f1c",
      "incomplete_value": true,
      "site": "00a59f1c",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59f1c",
      "incomplete_value": true,
      "site": "00a59f1c",
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
            "const:768:8"
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
      "00a59f1c",
      "DATA",
      [
        "storage",
        "00c0d768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59f1c",
      "DATA",
      [
        "storage",
        "00c0d818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59ef8.md#insn-00a59f18)
- 新版 [`00a59f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59ef8.md#insn-00a59f18)

~~~diff
- 00a59f18 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00a59f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a59f18 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00a59f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a59f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59f18 bytes 08a11d91
+ 00a59f18 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250837f49873ccc2cf5ea44bce7dc478"></a>

### [`00a59f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f2c.md) → [`00a59f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f2c.md) FUN_00a59f2c

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
      "definition_site": "00a59f38",
      "incomplete_value": false,
      "site": "00a59f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59f38",
      "incomplete_value": false,
      "site": "00a59f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00a59f38",
      "DATA",
      [
        "storage",
        "00c0d768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a59f38",
      "DATA",
      [
        "storage",
        "00c0d818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f2c.md#insn-00a59f34)
- 新版 [`00a59f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f2c.md#insn-00a59f34)

~~~diff
- 00a59f34 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00a59f34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a59f34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a59f34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a59f34 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00a59f34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59f34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a59f34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a59f34 bytes 29a11d91
+ 00a59f34 bytes 29612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d1405e5b22d48f09a97838f0ed94f5"></a>

### [`00a59f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f48.md) → [`00a59f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f48.md) FUN_00a59f48

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`00a5afc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5afc0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00a5afc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5afc0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a59fa0",
      "incomplete_value": true,
      "site": "00a59fa0",
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
      "definition_site": "00a59fa0",
      "incomplete_value": true,
      "site": "00a59fa0",
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
      "00a59f8c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a59fa8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a59fb0",
      "PARAM",
      [
        "storage",
        "00bfac88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a59f8c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a59fa8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a59fb0",
      "PARAM",
      [
        "storage",
        "00bfad38",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f48.md#insn-00a59f8c) · [`00a59fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f48.md#insn-00a59fa8) · [`00a59fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a59/00a59f48.md#insn-00a59fb0)
- 新版 [`00a59f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f48.md#insn-00a59f8c) · [`00a59fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f48.md#insn-00a59fa8) · [`00a59fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a59/00a59f48.md#insn-00a59fb0)

~~~diff
- 00a59f8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a59f8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a59f8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a59f8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a59f8c bytes 00dd44f9
+ 00a59f8c bytes 003d45f9
- 00a59fa8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a59fa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a59fa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a59fa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a59fa8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a59fa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a59fa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a59fa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a59fa8 bytes 21603691
+ 00a59fa8 bytes 21203991
- 00a59fb0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00a59fb0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a59fb0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a59fb0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a59fb0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00a59fb0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a59fb0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a59fb0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a59fb0 bytes 42203291
+ 00a59fb0 bytes 42e03491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5343f7bd9762fbf94075e339e24c19"></a>

### [`00a5a31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a31c.md) → [`00a5a31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a31c.md) _INIT_231

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
      "definition_site": "00a5a358",
      "incomplete_value": true,
      "site": "00a5a374",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5a358",
      "incomplete_value": true,
      "site": "00a5a374",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5a3bc",
      "incomplete_value": true,
      "site": "00a5a3d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5a3bc",
      "incomplete_value": true,
      "site": "00a5a3d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "definition_site": "00a5a3d8",
      "incomplete_value": true,
      "site": "00a5a3f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5a3d8",
      "incomplete_value": true,
      "site": "00a5a3f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5a358",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a5a37c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a5a39c",
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
      "00a5a358",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a5a37c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a5a39c",
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

- 旧版 [`00a5a348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a31c.md#insn-00a5a348) · [`00a5a350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a31c.md#insn-00a5a350)
- 新版 [`00a5a348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a31c.md#insn-00a5a348) · [`00a5a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a31c.md#insn-00a5a350)

~~~diff
- 00a5a348 ["COPY", "tmp:0:8", ["const:878:8"]]
- 00a5a348 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5a348 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5a348 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5a348 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00a5a348 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5a348 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5a348 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5a348 bytes 73e22191
+ 00a5a348 bytes 73e22491
- 00a5a350 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a5a350 bytes 69c2ffb0
+ 00a5a350 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a5a350 bytes 69c2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b893579e7f3453d0d33892053e376b7b"></a>

### [`00a5a6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a6ac.md) → [`00a5a6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md) FUN_00a5a6ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`004618e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00461/004618e8.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`004618e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00461/004618e8.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a5a6ec",
      "incomplete_value": false,
      "site": "00a5a6f0",
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
      "definition_site": "00a5a6ec",
      "incomplete_value": false,
      "site": "00a5a6f0",
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
      "definition_site": "00a5a798",
      "incomplete_value": true,
      "site": "00a5a7a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:219:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5a798",
      "incomplete_value": true,
      "site": "00a5a7a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:18c:8"
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
      "definition_site": "00a5ada0",
      "incomplete_value": true,
      "site": "00a5ada4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a5ada0",
      "incomplete_value": true,
      "site": "00a5ada4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a5a6f0",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5a700",
      "READ",
      [
        "storage",
        "00c1b710",
        null,
        "pointer"
      ]
    ],
    [
      "00a5a704",
      "PARAM",
      [
        "storage",
        "0109c5c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a5a6f0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5a700",
      "READ",
      [
        "storage",
        "00c1b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00a5a704",
      "PARAM",
      [
        "storage",
        "0109c680",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5a6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a6ac.md#insn-00a5a6ec) · [`00a5a700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a6ac.md#insn-00a5a700) · [`00a5a718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5a/00a5a6ac.md#insn-00a5a718)
- 新版 [`00a5a6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md#insn-00a5a6ec) · [`00a5a700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md#insn-00a5a700) · [`00a5a718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5a/00a5a6ac.md#insn-00a5a718)

~~~diff
- 00a5a6ec ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a5a6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a5a6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a5a6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a5a6ec ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a5a6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5a6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5a6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a5a6ec bytes 08e13191
+ 00a5a6ec bytes 08a13491
- 00a5a700 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:710:8"]]
- 00a5a700 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a5a700 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
+ 00a5a700 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00a5a700 bytes 298943f9
+ 00a5a700 bytes 29e143f9
- 00a5a718 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:720:8"]]
- 00a5a718 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a5a718 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7d0:8"]]
+ 00a5a718 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00a5a718 bytes 219043f9
+ 00a5a718 bytes 21e843f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c63fb5746fbbd791ee90e9088e2a68"></a>

### [`00a5b550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b550.md) → [`00a5b550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b550.md) FUN_00a5b550

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a5b3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b3c0.md) [`00a5b5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b5b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00a5b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b3c0.md) [`00a5b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b5b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00a5b55c",
      "incomplete_value": false,
      "site": "00a5b560",
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
      "definition_site": "00a5b55c",
      "incomplete_value": false,
      "site": "00a5b560",
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
      "00a5b55c",
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
      "00a5b55c",
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

- 旧版 [`00a5b55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b550.md#insn-00a5b55c)
- 新版 [`00a5b55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b550.md#insn-00a5b55c)

~~~diff
- 00a5b55c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a5b55c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a5b55c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a5b55c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a5b55c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a5b55c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a5b55c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a5b55c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a5b55c bytes 00280c91
+ 00a5b55c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d52cf6629f14786f5ca71e0ea8dda33"></a>

### [`00a5b980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b980.md) → [`00a5b980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b980.md) _INIT_232

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
      "definition_site": "00a5b9bc",
      "incomplete_value": true,
      "site": "00a5b9d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5b9bc",
      "incomplete_value": true,
      "site": "00a5b9d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5b9e0",
      "incomplete_value": true,
      "site": "00a5b9fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5b9e0",
      "incomplete_value": true,
      "site": "00a5b9fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5ba00",
      "incomplete_value": true,
      "site": "00a5ba1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5ba00",
      "incomplete_value": true,
      "site": "00a5ba1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5b9bc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a5b9e0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a5ba00",
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
      "00a5b9bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a5b9e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a5ba00",
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

- 旧版 [`00a5b9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b980.md#insn-00a5b9ac) · [`00a5b9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5b980.md#insn-00a5b9b4)
- 新版 [`00a5b9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b980.md#insn-00a5b9ac) · [`00a5b9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b980.md#insn-00a5b9b4)

~~~diff
- 00a5b9ac ["COPY", "tmp:0:8", ["const:890:8"]]
- 00a5b9ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5b9ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5b9ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5b9ac ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00a5b9ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5b9ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5b9ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5b9ac bytes 73422291
+ 00a5b9ac bytes 73422591
- 00a5b9b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a5b9b4 bytes 69c2ff90
+ 00a5b9b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a5b9b4 bytes 69c2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15ef9163a40b1fd10cf9482e00e57ce9"></a>

### [`00a5bd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5bd24.md) → [`00a5bd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5bd24.md) FUN_00a5bd24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

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
      "definition_site": "00a5bd60",
      "incomplete_value": false,
      "site": "00a5bd68",
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
      "definition_site": "00a5bd60",
      "incomplete_value": false,
      "site": "00a5bd68",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a5bd80",
      "incomplete_value": true,
      "site": "00a5bd8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cdd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5bd80",
      "incomplete_value": true,
      "site": "00a5bd8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c50:8"
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
      "definition_site": "00a5c1fc",
      "incomplete_value": true,
      "site": "00a5c200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a5c1fc",
      "incomplete_value": true,
      "site": "00a5c200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00a5bd68",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5bd80",
      "READ",
      [
        "storage",
        "0029cc50",
        null,
        "string"
      ]
    ],
    [
      "00a5bea8",
      "READ",
      [
        "storage",
        "002a4cc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a5bd68",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5bd80",
      "READ",
      [
        "storage",
        "0029ccdd",
        null,
        "string"
      ]
    ],
    [
      "00a5bea8",
      "READ",
      [
        "storage",
        "002a4cbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5bd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5bd24.md#insn-00a5bd60) · [`00a5bd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5bd24.md#insn-00a5bd7c) · [`00a5bea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5b/00a5bd24.md#insn-00a5bea0)
- 新版 [`00a5bd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5bd24.md#insn-00a5bd60) · [`00a5bd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5bd24.md#insn-00a5bd7c) · [`00a5bea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5bd24.md#insn-00a5bea0)

~~~diff
- 00a5bd60 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a5bd60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a5bd60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a5bd60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd60 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a5bd60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a5bd60 bytes 08e13191
+ 00a5bd60 bytes 08a13491
- 00a5bd7c ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00a5bd7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a5bd7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a5bd7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd7c ["COPY", "tmp:0:8", ["const:cdd:8"]]
+ 00a5bd7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5bd7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a5bd7c bytes 08413191
+ 00a5bd7c bytes 08753391
- 00a5bea0 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00a5bea0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a5bea0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a5bea0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a5bea0 ["COPY", "tmp:0:8", ["const:cbb:8"]]
+ 00a5bea0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5bea0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5bea0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a5bea0 bytes 29093391
+ 00a5bea0 bytes 29ed3291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbdbd451ed5337e2e04a16792310f35e"></a>

### [`00a5c5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5c/00a5c5d8.md) → [`00a5c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c5d8.md) _INIT_233

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
      "definition_site": "00a5c614",
      "incomplete_value": true,
      "site": "00a5c630",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5c614",
      "incomplete_value": true,
      "site": "00a5c630",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5c638",
      "incomplete_value": true,
      "site": "00a5c654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5c638",
      "incomplete_value": true,
      "site": "00a5c654",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5c658",
      "incomplete_value": true,
      "site": "00a5c674",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5c658",
      "incomplete_value": true,
      "site": "00a5c674",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5c614",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a5c638",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a5c658",
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
      "00a5c614",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a5c638",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a5c658",
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

- 旧版 [`00a5c604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5c/00a5c5d8.md#insn-00a5c604) · [`00a5c60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5c/00a5c5d8.md#insn-00a5c60c)
- 新版 [`00a5c604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c5d8.md#insn-00a5c604) · [`00a5c60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c5d8.md#insn-00a5c60c)

~~~diff
- 00a5c604 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00a5c604 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5c604 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5c604 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5c604 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00a5c604 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5c604 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5c604 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5c604 bytes 73a22291
+ 00a5c604 bytes 73a22591
- 00a5c60c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a5c60c bytes 49c2fff0
+ 00a5c60c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a5c60c bytes 49c2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22307c604ab51f30e00c7f684f01ce97"></a>

### [`00a5d014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d014.md) → [`00a5d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d014.md) _INIT_234

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
      "definition_site": "00a5d050",
      "incomplete_value": true,
      "site": "00a5d06c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d050",
      "incomplete_value": true,
      "site": "00a5d06c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d074",
      "incomplete_value": true,
      "site": "00a5d090",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d074",
      "incomplete_value": true,
      "site": "00a5d090",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d094",
      "incomplete_value": true,
      "site": "00a5d0b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d094",
      "incomplete_value": true,
      "site": "00a5d0b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5d050",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a5d074",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a5d094",
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
      "00a5d050",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a5d074",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a5d094",
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

- 旧版 [`00a5d040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d014.md#insn-00a5d040) · [`00a5d048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d014.md#insn-00a5d048)
- 新版 [`00a5d040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d014.md#insn-00a5d040) · [`00a5d048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d014.md#insn-00a5d048)

~~~diff
- 00a5d040 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00a5d040 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5d040 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5d040 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5d040 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00a5d040 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5d040 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5d040 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5d040 bytes 73022391
+ 00a5d040 bytes 73022691
- 00a5d048 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a5d048 bytes 49c2ffd0
+ 00a5d048 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a5d048 bytes 49c2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81e0aa0d7e89dfec04002b5c797c8399"></a>

### [`00a5d3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d3a4.md) → [`00a5d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d3a4.md) _INIT_235

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
      "definition_site": "00a5d3e0",
      "incomplete_value": true,
      "site": "00a5d3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d3e0",
      "incomplete_value": true,
      "site": "00a5d3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d404",
      "incomplete_value": true,
      "site": "00a5d420",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d404",
      "incomplete_value": true,
      "site": "00a5d420",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d424",
      "incomplete_value": true,
      "site": "00a5d440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a5d424",
      "incomplete_value": true,
      "site": "00a5d440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a5d3e0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a5d404",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a5d424",
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
      "00a5d3e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a5d404",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a5d424",
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

- 旧版 [`00a5d3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d3a4.md#insn-00a5d3d0) · [`00a5d3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d3a4.md#insn-00a5d3d8)
- 新版 [`00a5d3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d3a4.md#insn-00a5d3d0) · [`00a5d3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d3a4.md#insn-00a5d3d8)

~~~diff
- 00a5d3d0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00a5d3d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a5d3d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a5d3d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a5d3d0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00a5d3d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5d3d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a5d3d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a5d3d0 bytes 73622391
+ 00a5d3d0 bytes 73622691
- 00a5d3d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a5d3d8 bytes 49c2ffd0
+ 00a5d3d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a5d3d8 bytes 49c2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e50c05280a14a56753c0706954777d9"></a>

### [`00a5d734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d734.md) → [`00a5d734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d734.md) FUN_00a5d734

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00a5d798",
      "incomplete_value": true,
      "site": "00a5d798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dbe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5d798",
      "incomplete_value": true,
      "site": "00a5d798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d31:8"
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
      "00a5d788",
      "READ",
      [
        "storage",
        "00294d31",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a5d788",
      "READ",
      [
        "storage",
        "00294dbe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5d780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5d/00a5d734.md#insn-00a5d780)
- 新版 [`00a5d780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5d/00a5d734.md#insn-00a5d780)

~~~diff
- 00a5d780 ["COPY", "tmp:0:8", ["const:d31:8"]]
- 00a5d780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a5d780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a5d780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a5d780 ["COPY", "tmp:0:8", ["const:dbe:8"]]
+ 00a5d780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5d780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a5d780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a5d780 bytes 29c53491
+ 00a5d780 bytes 29f93691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea55efcbc73317c09bcb9a20de5ef90"></a>

### [`00a5f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md) → [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) FUN_00a5f6f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 25件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 25件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a5f734",
      "incomplete_value": false,
      "site": "00a5f740",
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
      "definition_site": "00a5f734",
      "incomplete_value": false,
      "site": "00a5f740",
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
      "definition_site": "00a5f758",
      "incomplete_value": true,
      "site": "00a5f758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:233:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5f758",
      "incomplete_value": true,
      "site": "00a5f758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a6:8"
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
      "definition_site": "00a5f75c",
      "incomplete_value": true,
      "site": "00a5f75c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00a5f75c",
      "incomplete_value": true,
      "site": "00a5f75c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a5f740",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5f748",
      "READ",
      [
        "storage",
        "002921a6",
        null,
        "string"
      ]
    ],
    [
      "00a5f750",
      "READ",
      [
        "storage",
        "002921ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a5f740",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a5f748",
      "READ",
      [
        "storage",
        "00292233",
        null,
        "string"
      ]
    ],
    [
      "00a5f750",
      "READ",
      [
        "storage",
        "00292239",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5f734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md#insn-00a5f734) · [`00a5f738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md#insn-00a5f738)
- 新版 [`00a5f734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md#insn-00a5f734) · [`00a5f738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md#insn-00a5f738)

~~~diff
- 00a5f734 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a5f734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a5f734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a5f734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a5f734 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a5f734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5f734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a5f734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a5f734 bytes 08e13191
+ 00a5f734 bytes 08a13491
- 00a5f738 ["COPY", "register:4048:8", ["const:292000:8"]]
- 00a5f738 bytes 89c1fff0
+ 00a5f738 ["COPY", "register:4048:8", ["const:292000:8"]]
+ 00a5f738 bytes 89c1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b63c3764f3b52b97752f887059b2185a"></a>

### [`00a60600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md) → [`00a60600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md) FUN_00a60600

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a6225c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md) [`00a650c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a650c8.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md)
- 新版 呼出元 2件 [`00a6225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md) [`00a650c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a650c8.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 21件, `store_value` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a60814",
      "incomplete_value": true,
      "site": "00a60814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a60814",
      "incomplete_value": true,
      "site": "00a60814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a60814",
      "incomplete_value": true,
      "site": "00a60814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a60814",
      "incomplete_value": true,
      "site": "00a60814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00a60940",
      "incomplete_value": true,
      "site": "00a60950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a60940",
      "incomplete_value": true,
      "site": "00a60950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b65:8"
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
      "00a6063c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a60648",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a60650",
      "PARAM",
      [
        "storage",
        "00c0d7d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a6063c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a60648",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a60650",
      "PARAM",
      [
        "storage",
        "00c0d888",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6063c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md#insn-00a6063c) · [`00a60648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md#insn-00a60648) · [`00a60650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md#insn-00a60650)
- 新版 [`00a6063c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md#insn-00a6063c) · [`00a60648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md#insn-00a60648) · [`00a60650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md#insn-00a60650)

~~~diff
- 00a6063c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a6063c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a6063c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a6063c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a6063c bytes 08dd44f9
+ 00a6063c bytes 083d45f9
- 00a60648 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a60648 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a60648 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a60648 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a60648 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a60648 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a60648 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a60648 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a60648 bytes 21603691
+ 00a60648 bytes 21203991
- 00a60650 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00a60650 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a60650 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a60650 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a60650 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00a60650 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a60650 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a60650 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a60650 bytes 42601f91
+ 00a60650 bytes 42202291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a044d8046cea2c1a4b931cdafd41cf"></a>

### [`00a6158c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a6158c.md) → [`00a6158c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6158c.md) FUN_00a6158c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044beb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md) [`0044d1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d1ec.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044d1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d1ec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "definition_site": "00a6173c",
      "incomplete_value": true,
      "site": "00a61750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6173c",
      "incomplete_value": true,
      "site": "00a61750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:973:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00a616fc",
      "incomplete_value": true,
      "site": "00a616fc",
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
      "definition_site": "00a616fc",
      "incomplete_value": true,
      "site": "00a616fc",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a61704",
      "incomplete_value": false,
      "site": "00a61714",
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
      "definition_site": "00a61704",
      "incomplete_value": false,
      "site": "00a61714",
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
      "00a616f8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a61704",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6170c",
      "PARAM",
      [
        "storage",
        "00be8da8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a616f8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a61704",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a6170c",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a616f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a6158c.md#insn-00a616f8) · [`00a61704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a6158c.md#insn-00a61704) · [`00a6170c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a6158c.md#insn-00a6170c)
- 新版 [`00a616f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6158c.md#insn-00a616f8) · [`00a61704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6158c.md#insn-00a61704) · [`00a6170c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6158c.md#insn-00a6170c)

~~~diff
- 00a616f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a616f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a616f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a616f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a616f8 bytes 00dd44f9
+ 00a616f8 bytes 003d45f9
- 00a61704 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a61704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a61704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a61704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a61704 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a61704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a61704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a61704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a61704 bytes 21603691
+ 00a61704 bytes 21203991
- 00a6170c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00a6170c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a6170c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a6170c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a6170c ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00a6170c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a6170c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a6170c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a6170c bytes 42a03691
+ 00a6170c bytes 42603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede6bdb6050a652c503de435009d9d89"></a>

### [`00a618b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a618b0.md) → [`00a618b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a618b0.md) FUN_00a618b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a6158c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a6158c.md) [`00adcbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adcbcc.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md)
- 新版 呼出元 2件 [`00a6158c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a6158c.md) [`00adcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.18% / 新版 88.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a61908",
      "incomplete_value": true,
      "site": "00a61920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a61908",
      "incomplete_value": true,
      "site": "00a61920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:84a:8"
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
      "definition_site": "00a61928",
      "incomplete_value": true,
      "site": "00a61938",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a61928",
      "incomplete_value": true,
      "site": "00a61938",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:733:8"
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
      "definition_site": "00a61a44",
      "incomplete_value": true,
      "site": "00a61a44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a61a44",
      "incomplete_value": true,
      "site": "00a61a44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a75:8"
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
      "00a618f0",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a61908",
      "READ",
      [
        "storage",
        "0029b84a",
        null,
        "string"
      ]
    ],
    [
      "00a61928",
      "READ",
      [
        "storage",
        "0029d733",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a618f0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a61908",
      "READ",
      [
        "storage",
        "0029b8d7",
        null,
        "string"
      ]
    ],
    [
      "00a61928",
      "READ",
      [
        "storage",
        "0029d7c0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a618e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a618b0.md#insn-00a618e4) · [`00a618e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a618b0.md#insn-00a618e8) · [`00a618fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a618b0.md#insn-00a618fc)
- 新版 [`00a618e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a618b0.md#insn-00a618e4) · [`00a618e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a618b0.md#insn-00a618e8)

~~~diff
- 00a618e4 ["COPY", "register:40c8:8", ["const:c24000:8"]]
+ 00a618e4 ["COPY", "register:40c8:8", ["const:c25000:8"]]
- 00a618e4 bytes 190e00f0
+ 00a618e4 bytes 390e0090
- 00a618e8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a618e8 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00a618e8 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00a618e8 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00a618e8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00a618e8 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00a618e8 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00a618e8 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00a618e8 bytes 39e33d91
+ 00a618e8 bytes 39e30091
- 00a618fc ["COPY", "register:4040:8", ["const:29b000:8"]]
- 00a618fc bytes c8c1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571366a4a7f26d7a793702835ef5a7a6"></a>

### [`00a621ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a621ac.md) → [`00a621ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a621ac.md) FUN_00a621ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d1dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a621f8",
      "incomplete_value": true,
      "site": "00a621fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a621f8",
      "incomplete_value": true,
      "site": "00a621fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a621e4",
      "incomplete_value": false,
      "site": "00a621fc",
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
      "definition_site": "00a621e4",
      "incomplete_value": false,
      "site": "00a621fc",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a621f0",
      "incomplete_value": false,
      "site": "00a621fc",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a621f0",
      "incomplete_value": false,
      "site": "00a621fc",
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
            "const:da8:8"
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
      "00a621e4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a621e8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a621f0",
      "PARAM",
      [
        "storage",
        "00be8da8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a621e4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a621e8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a621f0",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a621e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a621ac.md#insn-00a621e4) · [`00a621e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a621ac.md#insn-00a621e8) · [`00a621f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a621ac.md#insn-00a621f0)
- 新版 [`00a621e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a621ac.md#insn-00a621e4) · [`00a621e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a621ac.md#insn-00a621e8) · [`00a621f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a621ac.md#insn-00a621f0)

~~~diff
- 00a621e4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a621e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a621e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a621e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a621e4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a621e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a621e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a621e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a621e4 bytes 21603691
+ 00a621e4 bytes 21203991
- 00a621e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a621e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a621e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a621e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a621e8 bytes 08dd44f9
+ 00a621e8 bytes 083d45f9
- 00a621f0 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00a621f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a621f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a621f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a621f0 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00a621f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a621f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a621f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a621f0 bytes 42a03691
+ 00a621f0 bytes 42603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f53ee2d816d4f731049827d997bdbf"></a>

### [`00a6225c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md) → [`00a6225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md) FUN_00a6225c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 32件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md) [`009e97c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e97c4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 32件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) [`009e97c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e97c4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a62298",
      "incomplete_value": false,
      "site": "00a62298",
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
      "definition_site": "00a62298",
      "incomplete_value": false,
      "site": "00a62298",
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a62290",
      "incomplete_value": true,
      "site": "00a62298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a62290",
      "incomplete_value": true,
      "site": "00a62298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a6229c",
      "incomplete_value": false,
      "site": "00a6229c",
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
      "definition_site": "00a6229c",
      "incomplete_value": false,
      "site": "00a6229c",
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
      "00a62290",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a62294",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a62298",
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
      "00a62290",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a62294",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00a62298",
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

- 旧版 [`00a62298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md#insn-00a62298) · [`00a6229c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md#insn-00a6229c) · [`00a622b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md#insn-00a622b4)
- 新版 [`00a62298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md#insn-00a62298) · [`00a6229c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md#insn-00a6229c) · [`00a622b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md#insn-00a622b4)

~~~diff
- 00a62298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00a62298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00a62298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 00a62298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a62298 bytes 09d504f9
+ 00a62298 bytes 093505f9
- 00a6229c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 00a6229c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00a6229c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 00a6229c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a6229c bytes aade04f9
+ 00a6229c bytes aa3e05f9
- 00a622b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 00a622b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00a622b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 00a622b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a622b4 bytes b4de04f9
+ 00a622b4 bytes b43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfa1ea8863922fb3b605d1a25b3880e1"></a>

### [`00a62704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62704.md) → [`00a62704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62704.md) FUN_00a62704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 8件 [`0042b768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042b768.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) [`0088482c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/0088482c.md) [`00a699b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a699b4.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 8件 [`0042b768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042b768.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md) [`00a699b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a699b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a627cc",
      "incomplete_value": true,
      "site": "00a627cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a627cc",
      "incomplete_value": true,
      "site": "00a627cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00a627bc",
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
      "00a627bc",
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

- 旧版 [`00a627b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62704.md#insn-00a627b4)
- 新版 [`00a627b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62704.md#insn-00a627b4)

~~~diff
- 00a627b4 ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 00a627b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a627b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a627b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a627b4 ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 00a627b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a627b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a627b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a627b4 bytes 29851291
+ 00a627b4 bytes 299d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4033dced471f1ed6d5b91dcc7b32101d"></a>

### [`00a628a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a628a4.md) → [`00a628a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a628a4.md) FUN_00a628a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 27件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 27件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

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
      "definition_site": "00a628dc",
      "incomplete_value": true,
      "site": "00a628dc",
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
      "definition_site": "00a628dc",
      "incomplete_value": true,
      "site": "00a628dc",
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
      "definition_site": "00a628ec",
      "incomplete_value": false,
      "site": "00a62900",
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
      "definition_site": "00a628ec",
      "incomplete_value": false,
      "site": "00a62900",
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
      "definition_site": "00a628f4",
      "incomplete_value": false,
      "site": "00a62900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a628f4",
      "incomplete_value": false,
      "site": "00a62900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "00a628d8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a628ec",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a628f4",
      "PARAM",
      [
        "storage",
        "00c0d7d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a628d8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a628ec",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a628f4",
      "PARAM",
      [
        "storage",
        "00c0d888",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a628d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a628a4.md#insn-00a628d8) · [`00a628ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a628a4.md#insn-00a628ec) · [`00a628f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a628a4.md#insn-00a628f4)
- 新版 [`00a628d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a628a4.md#insn-00a628d8) · [`00a628ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a628a4.md#insn-00a628ec) · [`00a628f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a628a4.md#insn-00a628f4)

~~~diff
- 00a628d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a628d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a628d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a628d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a628d8 bytes 08dd44f9
+ 00a628d8 bytes 083d45f9
- 00a628ec ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a628ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a628ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a628ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a628ec ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a628ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a628ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a628ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a628ec bytes 21603691
+ 00a628ec bytes 21203991
- 00a628f4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00a628f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a628f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a628f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a628f4 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00a628f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a628f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a628f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a628f4 bytes 42601f91
+ 00a628f4 bytes 42202291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-846321a9c31295ed30cbecf8bc7755e9"></a>

### [`00a62dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62dd8.md) → [`00a62dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62dd8.md) FUN_00a62dd8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00a62de4",
      "incomplete_value": false,
      "site": "00a62de8",
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
      "definition_site": "00a62de4",
      "incomplete_value": false,
      "site": "00a62de8",
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
      "00a62de4",
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
      "00a62de4",
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

- 旧版 [`00a62de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62dd8.md#insn-00a62de4)
- 新版 [`00a62de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62dd8.md#insn-00a62de4)

~~~diff
- 00a62de4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a62de4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a62de4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a62de4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a62de4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a62de4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62de4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62de4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a62de4 bytes 00280c91
+ 00a62de4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e722e302fb221f41ceec87b495d191"></a>

### [`00a62dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62dec.md) → [`00a62dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62dec.md) FUN_00a62dec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00a5f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md) [`00a601cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a601cc.md) [`00a60600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md) [`00a618b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a618b0.md) [`00a63b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b48.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 5件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) [`00a601cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a601cc.md) [`00a60600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md) [`00a618b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a618b0.md) [`00a63b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b48.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "00a62df8",
      "incomplete_value": false,
      "site": "00a62dfc",
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
      "definition_site": "00a62df8",
      "incomplete_value": false,
      "site": "00a62dfc",
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
      "00a62df8",
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
      "00a62df8",
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

- 旧版 [`00a62df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62dec.md#insn-00a62df8)
- 新版 [`00a62df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62dec.md#insn-00a62df8)

~~~diff
- 00a62df8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a62df8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a62df8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a62df8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a62df8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a62df8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62df8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62df8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a62df8 bytes 00280c91
+ 00a62df8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba064fec15f54385721dbf9c20422cbc"></a>

### [`00a62e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62e00.md) → [`00a62e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e00.md) FUN_00a62e00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5f/00a5f6f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a5f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5f/00a5f6f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00a62e0c",
      "incomplete_value": false,
      "site": "00a62e10",
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
      "definition_site": "00a62e0c",
      "incomplete_value": false,
      "site": "00a62e10",
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
      "00a62e0c",
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
      "00a62e0c",
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

- 旧版 [`00a62e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a62e00.md#insn-00a62e0c)
- 新版 [`00a62e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a62e00.md#insn-00a62e0c)

~~~diff
- 00a62e0c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a62e0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a62e0c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a62e0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62e0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62e0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a62e0c bytes 00280c91
+ 00a62e0c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02de74a51d05483b554d56359042f94"></a>

### [`00a63ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63ad8.md) → [`00a63ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63ad8.md) FUN_00a63ad8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a60600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a60/00a60600.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00a60600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a60/00a60600.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "00a63ae4",
      "incomplete_value": false,
      "site": "00a63ae8",
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
      "definition_site": "00a63ae4",
      "incomplete_value": false,
      "site": "00a63ae8",
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
      "00a63ae4",
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
      "00a63ae4",
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

- 旧版 [`00a63ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63ad8.md#insn-00a63ae4)
- 新版 [`00a63ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63ad8.md#insn-00a63ae4)

~~~diff
- 00a63ae4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a63ae4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a63ae4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a63ae4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a63ae4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a63ae4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a63ae4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a63ae4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a63ae4 bytes 00280c91
+ 00a63ae4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87e77379e4737ecc4ac583d6e05023fd"></a>

### [`00a63af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63af0.md) → [`00a63af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63af0.md) FUN_00a63af0

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
      "definition_site": "00a63b10",
      "incomplete_value": false,
      "site": "00a63b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a63b10",
      "incomplete_value": false,
      "site": "00a63b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00a63b14",
      "DATA",
      [
        "storage",
        "00c0d800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a63b14",
      "DATA",
      [
        "storage",
        "00c0d8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a63b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63af0.md#insn-00a63b10)
- 新版 [`00a63b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63af0.md#insn-00a63b10)

~~~diff
- 00a63b10 ["COPY", "tmp:0:8", ["const:800:8"]]
- 00a63b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a63b10 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 00a63b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a63b10 bytes 08012091
+ 00a63b10 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f302ca4d5ee86c13d5a8eac6f172e291"></a>

### [`00a63b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b28.md) → [`00a63b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b28.md) FUN_00a63b28

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
      "definition_site": "00a63b2c",
      "incomplete_value": false,
      "site": "00a63b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a63b2c",
      "incomplete_value": false,
      "site": "00a63b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00a63b30",
      "DATA",
      [
        "storage",
        "00c0d800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a63b30",
      "DATA",
      [
        "storage",
        "00c0d8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a63b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b28.md#insn-00a63b2c)
- 新版 [`00a63b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b28.md#insn-00a63b2c)

~~~diff
- 00a63b2c ["COPY", "tmp:0:8", ["const:800:8"]]
- 00a63b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a63b2c ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 00a63b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a63b2c bytes 08012091
+ 00a63b2c bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1d64433987da0e53cba7f266b026a4"></a>

### [`00a63b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b48.md) → [`00a63b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b48.md) FUN_00a63b48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a63dec",
      "incomplete_value": false,
      "site": "00a63dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a63dec",
      "incomplete_value": false,
      "site": "00a63dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "00a63eb4",
      "incomplete_value": true,
      "site": "00a63eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e89:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a63eb4",
      "incomplete_value": true,
      "site": "00a63eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e83:8"
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
      "definition_site": "00a63eb8",
      "incomplete_value": true,
      "site": "00a63eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00a63eb8",
      "incomplete_value": true,
      "site": "00a63eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "00a63dec",
      "DATA",
      [
        "storage",
        "00c0d870",
        null,
        "undefined *"
      ]
    ],
    [
      "00a63e5c",
      "READ",
      [
        "storage",
        "00c0d890",
        null,
        "pointer"
      ]
    ],
    [
      "00a63e5c",
      "READ",
      [
        "storage",
        "00c0d898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a63dec",
      "DATA",
      [
        "storage",
        "00c0d920",
        null,
        "undefined *"
      ]
    ],
    [
      "00a63e5c",
      "READ",
      [
        "storage",
        "00c0d940",
        null,
        "pointer"
      ]
    ],
    [
      "00a63e5c",
      "READ",
      [
        "storage",
        "00c0d948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a63de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b48.md#insn-00a63de4) · [`00a63e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a63/00a63b48.md#insn-00a63e9c)
- 新版 [`00a63de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b48.md#insn-00a63de4) · [`00a63e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a63/00a63b48.md#insn-00a63e9c)

~~~diff
- 00a63de4 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00a63de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a63de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a63de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a63de4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00a63de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a63de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a63de4 bytes 08c12191
+ 00a63de4 bytes 08812491
- 00a63e9c ["COPY", "tmp:0:8", ["const:e83:8"]]
- 00a63e9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a63e9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a63e9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a63e9c ["COPY", "tmp:0:8", ["const:e89:8"]]
+ 00a63e9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a63e9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a63e9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a63e9c bytes 290d3a91
+ 00a63e9c bytes 29253a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9da02e1e0ac2f1a885af40f61196318"></a>

### [`00a64040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64040.md) → [`00a64040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64040.md) FUN_00a64040

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
      "definition_site": "00a64054",
      "incomplete_value": false,
      "site": "00a64058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64054",
      "incomplete_value": false,
      "site": "00a64058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00a64058",
      "DATA",
      [
        "storage",
        "00c0d870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a64058",
      "DATA",
      [
        "storage",
        "00c0d920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64040.md#insn-00a64054)
- 新版 [`00a64054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64040.md#insn-00a64054)

~~~diff
- 00a64054 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00a64054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64054 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00a64054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64054 bytes 08c12191
+ 00a64054 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86250785cf3f163e9e505ae45ff67191"></a>

### [`00a64064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64064.md) → [`00a64064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64064.md) FUN_00a64064

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
      "definition_site": "00a64068",
      "incomplete_value": false,
      "site": "00a6406c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64068",
      "incomplete_value": false,
      "site": "00a6406c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00a6406c",
      "DATA",
      [
        "storage",
        "00c0d870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6406c",
      "DATA",
      [
        "storage",
        "00c0d920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64064.md#insn-00a64068)
- 新版 [`00a64068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64064.md#insn-00a64068)

~~~diff
- 00a64068 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00a64068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64068 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00a64068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64068 bytes 08c12191
+ 00a64068 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a659e9170b188c2f0da5e706d799d1b"></a>

### [`00a640e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a640e4.md) → [`00a640e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a640e4.md) FUN_00a640e4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a6225c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00657/00657e7c.md) [`00830c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00830/00830c98.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00a6225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00830c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.17% / 新版 89.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `store_destination` 7件, `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a64120",
      "incomplete_value": false,
      "site": "00a64124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64120",
      "incomplete_value": false,
      "site": "00a64124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "definition_site": "00a641a0",
      "incomplete_value": true,
      "site": "00a641a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a641a0",
      "incomplete_value": true,
      "site": "00a641a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a641b8",
      "incomplete_value": true,
      "site": "00a641b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a641b8",
      "incomplete_value": true,
      "site": "00a641b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00a64124",
      "DATA",
      [
        "storage",
        "00c0d900",
        null,
        "pointer"
      ]
    ],
    [
      "00a64170",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a64190",
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
      "00a64124",
      "DATA",
      [
        "storage",
        "00c0d9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00a64170",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a64190",
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

- 旧版 [`00a64120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a640e4.md#insn-00a64120) · [`00a64128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a640e4.md#insn-00a64128)
- 新版 [`00a64120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a640e4.md#insn-00a64120) · [`00a64128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a640e4.md#insn-00a64128)

~~~diff
- 00a64120 ["COPY", "tmp:0:8", ["const:900:8"]]
- 00a64120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64120 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 00a64120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64120 bytes 08012491
+ 00a64120 bytes 08c12691
- 00a64128 ["COPY", "register:40c0:8", ["const:c24000:8"]]
- 00a64128 bytes 180e0090
+ 00a64128 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 00a64128 bytes 180e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e72141d7f98404594c8e268f178311a"></a>

### [`00a64de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64de0.md) → [`00a64de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64de0.md) FUN_00a64de0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a64f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64f58.md) · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00763798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00763/00763798.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00a64f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64f58.md) · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00763798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00763/00763798.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a64df8",
      "incomplete_value": false,
      "site": "00a64dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64df8",
      "incomplete_value": false,
      "site": "00a64dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "definition_site": "00a64f14",
      "incomplete_value": false,
      "site": "00a64f18",
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
      "definition_site": "00a64f14",
      "incomplete_value": false,
      "site": "00a64f18",
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
      "00a64dfc",
      "DATA",
      [
        "storage",
        "00c0d900",
        null,
        "pointer"
      ]
    ],
    [
      "00a64f18",
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
      "00a64dfc",
      "DATA",
      [
        "storage",
        "00c0d9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00a64f18",
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

- 旧版 [`00a64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64de0.md#insn-00a64df8) · [`00a64f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64de0.md#insn-00a64f14)
- 新版 [`00a64df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64de0.md#insn-00a64df8) · [`00a64f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64de0.md#insn-00a64f14)

~~~diff
- 00a64df8 ["COPY", "tmp:0:8", ["const:900:8"]]
- 00a64df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64df8 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 00a64df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64df8 bytes 08012491
+ 00a64df8 bytes 08c12691
- 00a64f14 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00a64f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64f14 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00a64f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64f14 bytes 08a10791
+ 00a64f14 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024c6e4aa093c3420149f8f38f184b8b"></a>

### [`00a64f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64f80.md) → [`00a64f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64f80.md) FUN_00a64f80

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
      "definition_site": "00a64fa4",
      "incomplete_value": false,
      "site": "00a64fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64fa4",
      "incomplete_value": false,
      "site": "00a64fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00a64fa4",
      "DATA",
      [
        "storage",
        "00c0d920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a64fa4",
      "DATA",
      [
        "storage",
        "00c0d9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64f80.md#insn-00a64fa0)
- 新版 [`00a64fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64f80.md#insn-00a64fa0)

~~~diff
- 00a64fa0 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a64fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a64fa0 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00a64fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a64fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64fa0 bytes 08812491
+ 00a64fa0 bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fcdc930cdca7fa87924bb3950937426"></a>

### [`00a64fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64fb4.md) → [`00a64fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64fb4.md) FUN_00a64fb4

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
      "definition_site": "00a64fc0",
      "incomplete_value": false,
      "site": "00a64fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64fc0",
      "incomplete_value": false,
      "site": "00a64fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00a64fc0",
      "DATA",
      [
        "storage",
        "00c0d920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a64fc0",
      "DATA",
      [
        "storage",
        "00c0d9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a64/00a64fb4.md#insn-00a64fbc)
- 新版 [`00a64fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a64/00a64fb4.md#insn-00a64fbc)

~~~diff
- 00a64fbc ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a64fbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a64fbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a64fbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a64fbc ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00a64fbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a64fbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a64fbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a64fbc bytes 29812491
+ 00a64fbc bytes 29412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a15e22ae314f9fcbaa895a3939512d4a"></a>

### [`00a65070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65070.md) → [`00a65070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65070.md) FUN_00a65070

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
      "definition_site": "00a65090",
      "incomplete_value": false,
      "site": "00a65094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65090",
      "incomplete_value": false,
      "site": "00a65094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a65094",
      "DATA",
      [
        "storage",
        "00c0d9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a65094",
      "DATA",
      [
        "storage",
        "00c0da50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65070.md#insn-00a65090)
- 新版 [`00a65090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65070.md#insn-00a65090)

~~~diff
- 00a65090 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a65090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a65090 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00a65090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65090 bytes 08812691
+ 00a65090 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20300268684b31da003e7160672411c3"></a>

### [`00a650a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a650a8.md) → [`00a650a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a650a8.md) FUN_00a650a8

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
      "definition_site": "00a650ac",
      "incomplete_value": false,
      "site": "00a650b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a650ac",
      "incomplete_value": false,
      "site": "00a650b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a650b0",
      "DATA",
      [
        "storage",
        "00c0d9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a650b0",
      "DATA",
      [
        "storage",
        "00c0da50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a650ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a650a8.md#insn-00a650ac)
- 新版 [`00a650ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a650a8.md#insn-00a650ac)

~~~diff
- 00a650ac ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a650ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a650ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a650ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a650ac ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00a650ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a650ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a650ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a650ac bytes 08812691
+ 00a650ac bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41573240a0e3e544eb1dd13583a03d56"></a>

### [`00a65108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65108.md) → [`00a65108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65108.md) FUN_00a65108

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
      "definition_site": "00a6512c",
      "incomplete_value": false,
      "site": "00a6512c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6512c",
      "incomplete_value": false,
      "site": "00a6512c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00a6512c",
      "DATA",
      [
        "storage",
        "00c0da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6512c",
      "DATA",
      [
        "storage",
        "00c0dad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65108.md#insn-00a65128)
- 新版 [`00a65128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65108.md#insn-00a65128)

~~~diff
- 00a65128 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a65128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a65128 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00a65128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65128 bytes 08812891
+ 00a65128 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c65382f9719f4b2237ebd25debf560"></a>

### [`00a6513c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6513c.md) → [`00a6513c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6513c.md) FUN_00a6513c

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
      "definition_site": "00a65148",
      "incomplete_value": false,
      "site": "00a65148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65148",
      "incomplete_value": false,
      "site": "00a65148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00a65148",
      "DATA",
      [
        "storage",
        "00c0da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a65148",
      "DATA",
      [
        "storage",
        "00c0dad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6513c.md#insn-00a65144)
- 新版 [`00a65144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6513c.md#insn-00a65144)

~~~diff
- 00a65144 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a65144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a65144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a65144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a65144 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00a65144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a65144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a65144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a65144 bytes 29812891
+ 00a65144 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fa6b122e4a6525e27de28bed0f94c2"></a>

### [`00a65158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65158.md) → [`00a65158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65158.md) FUN_00a65158

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00a612b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a61/00a612b8.md) [`00a652bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652bc.md) [`00a652c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652c0.md) [`00a6ca00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6c/00a6ca00.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00a612b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a61/00a612b8.md) [`00a652bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652bc.md) [`00a652c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652c0.md) [`00a6ca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ca00.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a65190",
      "incomplete_value": false,
      "site": "00a65190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65190",
      "incomplete_value": false,
      "site": "00a65190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a65190",
      "DATA",
      [
        "storage",
        "00c0da90",
        null,
        "undefined *"
      ]
    ],
    [
      "00a651cc",
      "READ",
      [
        "storage",
        "00c0dab0",
        null,
        "pointer"
      ]
    ],
    [
      "00a651cc",
      "READ",
      [
        "storage",
        "00c0dab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a65190",
      "DATA",
      [
        "storage",
        "00c0db40",
        null,
        "undefined *"
      ]
    ],
    [
      "00a651cc",
      "READ",
      [
        "storage",
        "00c0db60",
        null,
        "pointer"
      ]
    ],
    [
      "00a651cc",
      "READ",
      [
        "storage",
        "00c0db68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65158.md#insn-00a65188)
- 新版 [`00a65188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65158.md#insn-00a65188)

~~~diff
- 00a65188 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a65188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a65188 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00a65188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65188 bytes 08412a91
+ 00a65188 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-393f7ba65a5d2a6eea6e22f3c2e06efc"></a>

### [`00a65274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65274.md) → [`00a65274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65274.md) FUN_00a65274

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
      "definition_site": "00a65298",
      "incomplete_value": false,
      "site": "00a65298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65298",
      "incomplete_value": false,
      "site": "00a65298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a65298",
      "DATA",
      [
        "storage",
        "00c0da90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a65298",
      "DATA",
      [
        "storage",
        "00c0db40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65274.md#insn-00a65294)
- 新版 [`00a65294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65274.md#insn-00a65294)

~~~diff
- 00a65294 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a65294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a65294 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00a65294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65294 bytes 08412a91
+ 00a65294 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af38cfb4fc99adc10bb55e7ceb8bc79"></a>

### [`00a652a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652a8.md) → [`00a652a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652a8.md) FUN_00a652a8

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
      "definition_site": "00a652b4",
      "incomplete_value": false,
      "site": "00a652b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a652b4",
      "incomplete_value": false,
      "site": "00a652b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a652b4",
      "DATA",
      [
        "storage",
        "00c0da90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a652b4",
      "DATA",
      [
        "storage",
        "00c0db40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a652b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652a8.md#insn-00a652b0)
- 新版 [`00a652b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652a8.md#insn-00a652b0)

~~~diff
- 00a652b0 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a652b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a652b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a652b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a652b0 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00a652b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a652b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a652b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a652b0 bytes 29412a91
+ 00a652b0 bytes 29012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcc902c085c21036207fa68c4f3f5d0e"></a>

### [`00a652c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652c4.md) → [`00a652c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652c4.md) FUN_00a652c4

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
      "definition_site": "00a652f8",
      "incomplete_value": false,
      "site": "00a652f8",
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
      "definition_site": "00a652f8",
      "incomplete_value": false,
      "site": "00a652f8",
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
      "definition_site": "00a652ec",
      "incomplete_value": true,
      "site": "00a652f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a652ec",
      "incomplete_value": true,
      "site": "00a652f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a652fc",
      "incomplete_value": false,
      "site": "00a652fc",
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
      "definition_site": "00a652fc",
      "incomplete_value": false,
      "site": "00a652fc",
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
      "00a652ec",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a652f0",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a652f8",
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
      "00a652ec",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a652f0",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00a652f8",
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

- 旧版 [`00a652f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652c4.md#insn-00a652f8) · [`00a652fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652c4.md#insn-00a652fc) · [`00a65324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a652c4.md#insn-00a65324)
- 新版 [`00a652f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652c4.md#insn-00a652f8) · [`00a652fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652c4.md#insn-00a652fc) · [`00a65324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a652c4.md#insn-00a65324)

~~~diff
- 00a652f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00a652f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00a652f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 00a652f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a652f8 bytes 09d504f9
+ 00a652f8 bytes 093505f9
- 00a652fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 00a652fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00a652fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00a652fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a652fc bytes cade04f9
+ 00a652fc bytes ca3e05f9
- 00a65324 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9b8:8"]]
- 00a65324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00a65324 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00a65324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a65324 bytes d4de04f9
+ 00a65324 bytes d43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733b5a8ca9678ddb2da70d09559c2556"></a>

### [`00a653bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a653bc.md) → [`00a653bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a653bc.md) FUN_00a653bc

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
      "definition_site": "00a653e0",
      "incomplete_value": false,
      "site": "00a653e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a653e0",
      "incomplete_value": false,
      "site": "00a653e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00a653e0",
      "DATA",
      [
        "storage",
        "00c0db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a653e0",
      "DATA",
      [
        "storage",
        "00c0dbd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a653dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a653bc.md#insn-00a653dc)
- 新版 [`00a653dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a653bc.md#insn-00a653dc)

~~~diff
- 00a653dc ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a653dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a653dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a653dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a653dc ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 00a653dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a653dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a653dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a653dc bytes 08812c91
+ 00a653dc bytes 08412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109e12a989a1742932727ec51b797e39"></a>

### [`00a653f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a653f0.md) → [`00a653f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a653f0.md) FUN_00a653f0

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
      "definition_site": "00a653fc",
      "incomplete_value": false,
      "site": "00a653fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a653fc",
      "incomplete_value": false,
      "site": "00a653fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00a653fc",
      "DATA",
      [
        "storage",
        "00c0db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a653fc",
      "DATA",
      [
        "storage",
        "00c0dbd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a653f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a653f0.md#insn-00a653f8)
- 新版 [`00a653f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a653f0.md#insn-00a653f8)

~~~diff
- 00a653f8 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a653f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a653f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a653f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a653f8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 00a653f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a653f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a653f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a653f8 bytes 29812c91
+ 00a653f8 bytes 29412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6afdcea1ea19d41f0c540eb9b05ad016"></a>

### [`00a6540c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6540c.md) → [`00a6540c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6540c.md) FUN_00a6540c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/0088482c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md)

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
      "definition_site": "00a654f0",
      "incomplete_value": true,
      "site": "00a65504",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a654f0",
      "incomplete_value": true,
      "site": "00a65504",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6551c",
      "incomplete_value": false,
      "site": "00a65524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6551c",
      "incomplete_value": false,
      "site": "00a65524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00a654f0",
      "READ",
      [
        "storage",
        "002a4279",
        null,
        "string"
      ]
    ],
    [
      "00a65524",
      "DATA",
      [
        "storage",
        "00c0db90",
        null,
        "undefined *"
      ]
    ],
    [
      "00a65570",
      "READ",
      [
        "storage",
        "00c0dbb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a654f0",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "00a65524",
      "DATA",
      [
        "storage",
        "00c0dc40",
        null,
        "undefined *"
      ]
    ],
    [
      "00a65570",
      "READ",
      [
        "storage",
        "00c0dc60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a654e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6540c.md#insn-00a654e8) · [`00a6551c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6540c.md#insn-00a6551c)
- 新版 [`00a654e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6540c.md#insn-00a654e8) · [`00a6551c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6540c.md#insn-00a6551c)

~~~diff
- 00a654e8 ["COPY", "tmp:0:8", ["const:279:8"]]
- 00a654e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a654e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a654e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a654e8 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 00a654e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a654e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a654e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a654e8 bytes 29e50991
+ 00a654e8 bytes 29c90991
- 00a6551c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00a6551c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6551c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6551c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6551c ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00a6551c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6551c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6551c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6551c bytes 08412e91
+ 00a6551c bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e38426c1686152be7cd9a6d12b79ad9c"></a>

### [`00a6567c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6567c.md) → [`00a6567c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6567c.md) FUN_00a6567c

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
      "definition_site": "00a65690",
      "incomplete_value": false,
      "site": "00a65694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65690",
      "incomplete_value": false,
      "site": "00a65694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00a65694",
      "DATA",
      [
        "storage",
        "00c0db90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a65694",
      "DATA",
      [
        "storage",
        "00c0dc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a6567c.md#insn-00a65690)
- 新版 [`00a65690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a6567c.md#insn-00a65690)

~~~diff
- 00a65690 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00a65690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a65690 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00a65690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a65690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65690 bytes 08412e91
+ 00a65690 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a248acdefcd66bd76416cbd378536e24"></a>

### [`00a656a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a656a0.md) → [`00a656a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a656a0.md) FUN_00a656a0

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
      "definition_site": "00a656a4",
      "incomplete_value": false,
      "site": "00a656a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a656a4",
      "incomplete_value": false,
      "site": "00a656a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00a656a8",
      "DATA",
      [
        "storage",
        "00c0db90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a656a8",
      "DATA",
      [
        "storage",
        "00c0dc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a656a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a656a0.md#insn-00a656a4)
- 新版 [`00a656a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a656a0.md#insn-00a656a4)

~~~diff
- 00a656a4 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00a656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a656a4 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00a656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a656a4 bytes 08412e91
+ 00a656a4 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70e728742f204598a628626405e3cbdf"></a>

### [`00a656f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a656f8.md) → [`00a656f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a656f8.md) _INIT_236

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
      "definition_site": "00a65734",
      "incomplete_value": true,
      "site": "00a65750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a65734",
      "incomplete_value": true,
      "site": "00a65750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a65758",
      "incomplete_value": true,
      "site": "00a65774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a65758",
      "incomplete_value": true,
      "site": "00a65774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a65778",
      "incomplete_value": true,
      "site": "00a65794",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a65778",
      "incomplete_value": true,
      "site": "00a65794",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a65734",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a65758",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a65778",
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
      "00a65734",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a65758",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a65778",
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

- 旧版 [`00a65724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a656f8.md#insn-00a65724) · [`00a6572c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a656f8.md#insn-00a6572c)
- 新版 [`00a65724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a656f8.md#insn-00a65724) · [`00a6572c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a656f8.md#insn-00a6572c)

~~~diff
- 00a65724 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00a65724 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a65724 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a65724 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a65724 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 00a65724 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a65724 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a65724 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a65724 bytes 73c22391
+ 00a65724 bytes 73c22691
- 00a6572c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a6572c bytes 09c2ffd0
+ 00a6572c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a6572c bytes 09c2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb94e6c6da78d5d14d4f57a6fb838d83"></a>

### [`00a65a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65a88.md) → [`00a65a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65a88.md) FUN_00a65a88

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 28件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044ab0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ab0c.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 28件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044ab0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab0c.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.63% / 新版 93.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 41件, `store_destination` 28件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a66104",
      "incomplete_value": false,
      "site": "00a66104",
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
      "definition_site": "00a66104",
      "incomplete_value": false,
      "site": "00a66104",
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
    "ordinal": 64,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a66108",
      "incomplete_value": false,
      "site": "00a66108",
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
      "definition_site": "00a66108",
      "incomplete_value": false,
      "site": "00a66108",
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
    "ordinal": 65,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a66104",
      "incomplete_value": false,
      "site": "00a66108",
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
      "definition_site": "00a66104",
      "incomplete_value": false,
      "site": "00a66108",
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
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a65fa4",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00a66020",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a66030",
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
      "00a65fa4",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00a66020",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a66030",
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

- 旧版 [`00a65fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65a88.md#insn-00a65fa4) · [`00a66018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65a88.md#insn-00a66018) · [`00a6601c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a65/00a65a88.md#insn-00a6601c)
- 新版 [`00a65fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65a88.md#insn-00a65fa4) · [`00a66018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65a88.md#insn-00a66018) · [`00a6601c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a65/00a65a88.md#insn-00a6601c)

~~~diff
- 00a65fa4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:db0:8"]]
- 00a65fa4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a65fa4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e60:8"]]
+ 00a65fa4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00a65fa4 bytes 18db46f9
+ 00a65fa4 bytes 183347f9
- 00a66018 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00a66018 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00a66018 bytes e80d00d0
+ 00a66018 bytes e80d00f0
- 00a6601c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a6601c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6601c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6601c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6601c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00a6601c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6601c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6601c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6601c bytes 08e13d91
+ 00a6601c bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-087bd73aaf752999a55a2e8405e6aba9"></a>

### [`00a6731c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md) → [`00a6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md) FUN_00a6731c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 21件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 21件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a67398",
      "incomplete_value": true,
      "site": "00a67398",
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
      "definition_site": "00a67398",
      "incomplete_value": true,
      "site": "00a67398",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a673c8",
      "incomplete_value": true,
      "site": "00a673c8",
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
      "definition_site": "00a673c8",
      "incomplete_value": true,
      "site": "00a673c8",
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
      "definition_site": "00a673a0",
      "incomplete_value": false,
      "site": "00a673b4",
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
      "definition_site": "00a673a0",
      "incomplete_value": false,
      "site": "00a673b4",
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
      "00a67394",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a673a0",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a673a8",
      "PARAM",
      [
        "storage",
        "00bf3c50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a67394",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a673a0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a673a8",
      "PARAM",
      [
        "storage",
        "00bf3d00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6745c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md#insn-00a6745c) · [`00a67578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md#insn-00a67578) · [`00a67394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md#insn-00a67394)
- 新版 [`00a6745c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md#insn-00a6745c) · [`00a67578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md#insn-00a67578) · [`00a67394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md#insn-00a67394)

~~~diff
- 00a6745c ["INT_ADD", "register:40f0:8", ["const:a6745c:8", "const:4:8"]]
- 00a6745c ["CALL", null, ["ram:ace4cc:8"]]
+ 00a6745c ["INT_ADD", "register:40f0:8", ["const:a6745c:8", "const:4:8"]]
+ 00a6745c ["CALL", null, ["ram:ace594:8"]]
- 00a6745c bytes 1c9c0194
+ 00a6745c bytes 4e9c0194
- 00a67578 ["INT_ADD", "register:40f0:8", ["const:a67578:8", "const:4:8"]]
- 00a67578 ["CALL", null, ["ram:ace4cc:8"]]
+ 00a67578 ["INT_ADD", "register:40f0:8", ["const:a67578:8", "const:4:8"]]
+ 00a67578 ["CALL", null, ["ram:ace594:8"]]
- 00a67578 bytes d59b0194
+ 00a67578 bytes 079c0194
- 00a67394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a67394 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a67394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a67394 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00a67394 bytes 16dd44f9
+ 00a67394 bytes 163d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68d9207940fc322369c74558bf6d84c3"></a>

### [`00a68ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a68/00a68ac0.md) → [`00a68ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a68/00a68ac0.md) FUN_00a68ac0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a6731c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md) · 呼出先 13件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00a6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md) · 呼出先 13件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "site": "00a68e10",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a68e10",
      "value": [
        "leaf",
        "ram:ace4cc:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a68f34",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a68f34",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "00a68b60",
      "READ",
      [
        "storage",
        "00c1b5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00a68b78",
      "DATA",
      [
        "storage",
        "00c244c8",
        null,
        null
      ]
    ],
    [
      "00a68e10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      "00a68b60",
      "READ",
      [
        "storage",
        "00c1b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00a68b78",
      "DATA",
      [
        "storage",
        "00c24578",
        null,
        null
      ]
    ],
    [
      "00a68e10",
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

- 旧版 [`00a68e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a68/00a68ac0.md#insn-00a68e10) · [`00a68f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a68/00a68ac0.md#insn-00a68f34) · [`00a68b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a68/00a68ac0.md#insn-00a68b60)
- 新版 [`00a68e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a68/00a68ac0.md#insn-00a68e10) · [`00a68f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a68/00a68ac0.md#insn-00a68f34) · [`00a68b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a68/00a68ac0.md#insn-00a68b60)

~~~diff
- 00a68e10 ["INT_ADD", "register:40f0:8", ["const:a68e10:8", "const:4:8"]]
- 00a68e10 ["CALL", null, ["ram:ace4cc:8"]]
+ 00a68e10 ["INT_ADD", "register:40f0:8", ["const:a68e10:8", "const:4:8"]]
+ 00a68e10 ["CALL", null, ["ram:ace594:8"]]
- 00a68e10 bytes af950194
+ 00a68e10 bytes e1950194
- 00a68f34 ["INT_ADD", "register:40f0:8", ["const:a68f34:8", "const:4:8"]]
- 00a68f34 ["CALL", null, ["ram:ace4cc:8"]]
+ 00a68f34 ["INT_ADD", "register:40f0:8", ["const:a68f34:8", "const:4:8"]]
+ 00a68f34 ["CALL", null, ["ram:ace594:8"]]
- 00a68f34 bytes 66950194
+ 00a68f34 bytes 98950194
- 00a68b60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5f8:8"]]
- 00a68b60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a68b60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6a8:8"]]
+ 00a68b60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00a68b60 bytes 29fd42f9
+ 00a68b60 bytes 295543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3702df725e3c0c23fe7013e5a5e7bf90"></a>

### [`00a69030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a69030.md) → [`00a69030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69030.md) FUN_00a69030

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a6731c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a67/00a6731c.md) · 呼出先 13件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00a6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a67/00a6731c.md) · 呼出先 13件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "site": "00a69380",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a69380",
      "value": [
        "leaf",
        "ram:ace4cc:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a694a4",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a694a4",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "00a690d0",
      "READ",
      [
        "storage",
        "00c1b5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00a690e8",
      "DATA",
      [
        "storage",
        "00c244c8",
        null,
        null
      ]
    ],
    [
      "00a69380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      "00a690d0",
      "READ",
      [
        "storage",
        "00c1b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00a690e8",
      "DATA",
      [
        "storage",
        "00c24578",
        null,
        null
      ]
    ],
    [
      "00a69380",
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

- 旧版 [`00a69380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a69030.md#insn-00a69380) · [`00a694a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a69030.md#insn-00a694a4) · [`00a690d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a69030.md#insn-00a690d0)
- 新版 [`00a69380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69030.md#insn-00a69380) · [`00a694a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69030.md#insn-00a694a4) · [`00a690d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a69030.md#insn-00a690d0)

~~~diff
- 00a69380 ["INT_ADD", "register:40f0:8", ["const:a69380:8", "const:4:8"]]
- 00a69380 ["CALL", null, ["ram:ace4cc:8"]]
+ 00a69380 ["INT_ADD", "register:40f0:8", ["const:a69380:8", "const:4:8"]]
+ 00a69380 ["CALL", null, ["ram:ace594:8"]]
- 00a69380 bytes 53940194
+ 00a69380 bytes 85940194
- 00a694a4 ["INT_ADD", "register:40f0:8", ["const:a694a4:8", "const:4:8"]]
- 00a694a4 ["CALL", null, ["ram:ace4cc:8"]]
+ 00a694a4 ["INT_ADD", "register:40f0:8", ["const:a694a4:8", "const:4:8"]]
+ 00a694a4 ["CALL", null, ["ram:ace594:8"]]
- 00a694a4 bytes 0a940194
+ 00a694a4 bytes 3c940194
- 00a690d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5f8:8"]]
- 00a690d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a690d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6a8:8"]]
+ 00a690d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00a690d0 bytes 29fd42f9
+ 00a690d0 bytes 295543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-574845122cef21b52519eaa41bff80df"></a>

### [`00a695a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a695a0.md) → [`00a695a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a695a0.md) _INIT_237

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
      "definition_site": "00a695dc",
      "incomplete_value": true,
      "site": "00a695f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a695dc",
      "incomplete_value": true,
      "site": "00a695f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a69600",
      "incomplete_value": true,
      "site": "00a6961c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a69600",
      "incomplete_value": true,
      "site": "00a6961c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a69620",
      "incomplete_value": true,
      "site": "00a6963c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a69620",
      "incomplete_value": true,
      "site": "00a6963c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a695dc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a69600",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a69620",
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
      "00a695dc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a69600",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a69620",
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

- 旧版 [`00a695cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a695a0.md#insn-00a695cc) · [`00a695d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a69/00a695a0.md#insn-00a695d4)
- 新版 [`00a695cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a695a0.md#insn-00a695cc) · [`00a695d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a69/00a695a0.md#insn-00a695d4)

~~~diff
- 00a695cc ["COPY", "tmp:0:8", ["const:908:8"]]
- 00a695cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a695cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a695cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a695cc ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00a695cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a695cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a695cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a695cc bytes 73222491
+ 00a695cc bytes 73222791
- 00a695d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a695d4 bytes e9c1ffd0
+ 00a695d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a695d4 bytes e9c1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f49f1bcf0d38a5f0c35292f2463f1aef"></a>

### [`00a6a688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a688.md) → [`00a6a688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a688.md) FUN_00a6a688

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`007f7410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f7410.md) [`007f78c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f7/007f78c4.md) [`0088fde0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0088f/0088fde0.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00a6a7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a7d4.md)
- 新版 呼出元 3件 [`007f7410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7410.md) [`007f78c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f78c4.md) [`0088fde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0088f/0088fde0.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a6a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a7d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6a700",
      "incomplete_value": false,
      "site": "00a6a704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a700",
      "incomplete_value": false,
      "site": "00a6a704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "00a6a704",
      "DATA",
      [
        "storage",
        "00bf6210",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a754",
      "READ",
      [
        "storage",
        "00bf6230",
        null,
        "pointer"
      ]
    ],
    [
      "00a6a754",
      "READ",
      [
        "storage",
        "00bf6238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6a704",
      "DATA",
      [
        "storage",
        "00bf62c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a754",
      "READ",
      [
        "storage",
        "00bf62e0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6a754",
      "READ",
      [
        "storage",
        "00bf62e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6a700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a688.md#insn-00a6a700)
- 新版 [`00a6a700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a688.md#insn-00a6a700)

~~~diff
- 00a6a700 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00a6a700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6a700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6a700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6a700 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00a6a700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6a700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6a700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6a700 bytes 08410891
+ 00a6a700 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53408e6968caf7aff92422438ebeeff2"></a>

### [`00a6a7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a7d4.md) → [`00a6a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a7d4.md) FUN_00a6a7d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`0061d5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0061d/0061d5c8.md) [`006584d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006584d8.md) [`006baf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md) [`007127f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00712/007127f8.md) [`008a8900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8900.md) · 呼出先 5件 [`00a6ce94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6c/00a6ce94.md) [`00a6d034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d034.md) [`00a6d038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d038.md) [`00a6d06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d06c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 12件 [`0061d5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061d/0061d5c8.md) [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`006baf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md) [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`008a8900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a8/008a8900.md) · 呼出先 5件 [`00a6ce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md) [`00a6d034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d034.md) [`00a6d038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d038.md) [`00a6d06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d06c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6a8a0",
      "incomplete_value": false,
      "site": "00a6a8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a8a0",
      "incomplete_value": false,
      "site": "00a6a8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "definition_site": "00a6a8a0",
      "incomplete_value": false,
      "site": "00a6a8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a8a0",
      "incomplete_value": false,
      "site": "00a6a8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00a6a8b4",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a8c0",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a8ec",
      "READ",
      [
        "storage",
        "00c0dc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6a8b4",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a8c0",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a8ec",
      "READ",
      [
        "storage",
        "00c0dcf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6a8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a7d4.md#insn-00a6a8a0)
- 新版 [`00a6a8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a7d4.md#insn-00a6a8a0)

~~~diff
- 00a6a8a0 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a6a8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6a8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6a8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6a8a0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 00a6a8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6a8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6a8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6a8a0 bytes 08813091
+ 00a6a8a0 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16cc676a7562e8e16b45bd63c6116fcc"></a>

### [`00a6aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6aa9c.md) → [`00a6aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6aa9c.md) FUN_00a6aa9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0075e798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00896/00896c7c.md) [`00a144c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a14/00a144c8.md) [`00a6225c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a62/00a6225c.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00a6a7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6a7d4.md)
- 新版 呼出元 5件 [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`00a144c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a14/00a144c8.md) [`00a6225c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a62/00a6225c.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a6a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a7d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6aaf4",
      "incomplete_value": false,
      "site": "00a6aaf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6aaf4",
      "incomplete_value": false,
      "site": "00a6aaf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "00a6aaf8",
      "DATA",
      [
        "storage",
        "00bf6210",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6ab48",
      "READ",
      [
        "storage",
        "00bf6230",
        null,
        "pointer"
      ]
    ],
    [
      "00a6ab48",
      "READ",
      [
        "storage",
        "00bf6238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6aaf8",
      "DATA",
      [
        "storage",
        "00bf62c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6ab48",
      "READ",
      [
        "storage",
        "00bf62e0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6ab48",
      "READ",
      [
        "storage",
        "00bf62e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6aaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6aa9c.md#insn-00a6aaf4)
- 新版 [`00a6aaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6aa9c.md#insn-00a6aaf4)

~~~diff
- 00a6aaf4 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00a6aaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6aaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6aaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6aaf4 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00a6aaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6aaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6aaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6aaf4 bytes 08410891
+ 00a6aaf4 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79308108d3d90dc5a3cd096065fc313c"></a>

### [`00a6b264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b264.md) → [`00a6b264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b264.md) FUN_00a6b264

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007127f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00712/007127f8.md) [`0075e798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075e/0075e798.md) · 呼出先 5件 [`00a6ce94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6c/00a6ce94.md) [`00a6d034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d034.md) [`00a6d038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d038.md) [`00a6d06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d06c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) · 呼出先 5件 [`00a6ce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ce94.md) [`00a6d034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d034.md) [`00a6d038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d038.md) [`00a6d06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d06c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6b314",
      "incomplete_value": false,
      "site": "00a6b328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6b314",
      "incomplete_value": false,
      "site": "00a6b328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "definition_site": "00a6b314",
      "incomplete_value": false,
      "site": "00a6b334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6b314",
      "incomplete_value": false,
      "site": "00a6b334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00a6b328",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6b334",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6b360",
      "READ",
      [
        "storage",
        "00c0dc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6b328",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6b334",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6b360",
      "READ",
      [
        "storage",
        "00c0dcf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6b314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b264.md#insn-00a6b314)
- 新版 [`00a6b314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b264.md#insn-00a6b314)

~~~diff
- 00a6b314 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a6b314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6b314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6b314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6b314 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 00a6b314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6b314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6b314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6b314 bytes 08813091
+ 00a6b314 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b615926d872054a97126631f11e58407"></a>

### [`00a6b918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b918.md) → [`00a6b918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b918.md) FUN_00a6b918

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`0075e798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0089d/0089dc0c.md) [`008ca974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md) · 呼出先 17件 [`00558fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558fd0.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d34.md) [`00883d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d4c.md)
- 新版 呼出元 7件 [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089d/0089dc0c.md) [`008ca974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md) · 呼出先 17件 [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d34.md) [`00883d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d4c.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6bbe0",
      "incomplete_value": false,
      "site": "00a6bbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6bbe0",
      "incomplete_value": false,
      "site": "00a6bbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "00a6ba68",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "00a6ba7c",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6ba94",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6ba68",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00a6ba7c",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6ba94",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6ba68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b918.md#insn-00a6ba68) · [`00a6ba94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b918.md#insn-00a6ba94) · [`00a6bbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6b918.md#insn-00a6bbd4)
- 新版 [`00a6ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b918.md#insn-00a6ba68) · [`00a6ba94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b918.md#insn-00a6ba94) · [`00a6bbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6b918.md#insn-00a6bbd4)

~~~diff
- 00a6ba68 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:470:8"]]
- 00a6ba68 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a6ba68 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
+ 00a6ba68 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00a6ba68 bytes 183b42f9
+ 00a6ba68 bytes 189342f9
- 00a6ba94 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:478:8"]]
- 00a6ba94 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a6ba94 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:528:8"]]
+ 00a6ba94 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00a6ba94 bytes 393f42f9
+ 00a6ba94 bytes 399742f9
- 00a6bbd4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a6bbd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a6bbd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a6bbd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a6bbd4 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00a6bbd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a6bbd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a6bbd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a6bbd4 bytes 29813291
+ 00a6bbd4 bytes 29413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f349061fed197711c0cc235854257903"></a>

### [`00a6bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6bd8c.md) → [`00a6bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6bd8c.md) FUN_00a6bd8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0075e798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00896/00896c7c.md) [`008ca974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ca/008ca974.md) [`009e0d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e0/009e0d20.md) · 呼出先 15件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d34.md)
- 新版 呼出元 6件 [`0075e798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`008ca974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md) [`009e0d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e0/009e0d20.md) · 呼出先 15件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d34.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6befc",
      "incomplete_value": false,
      "site": "00a6bf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6befc",
      "incomplete_value": false,
      "site": "00a6bf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00a6be64",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "00a6be78",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6be90",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a6be64",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00a6be78",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6be90",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6be64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6bd8c.md#insn-00a6be64) · [`00a6be90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6bd8c.md#insn-00a6be90) · [`00a6befc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6b/00a6bd8c.md#insn-00a6befc)
- 新版 [`00a6be64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6bd8c.md#insn-00a6be64) · [`00a6be90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6bd8c.md#insn-00a6be90) · [`00a6befc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6b/00a6bd8c.md#insn-00a6befc)

~~~diff
- 00a6be64 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:470:8"]]
- 00a6be64 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a6be64 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:520:8"]]
+ 00a6be64 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00a6be64 bytes d63a42f9
+ 00a6be64 bytes d69242f9
- 00a6be90 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:478:8"]]
- 00a6be90 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a6be90 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:528:8"]]
+ 00a6be90 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00a6be90 bytes 393f42f9
+ 00a6be90 bytes 399742f9
- 00a6befc ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a6befc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a6befc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a6befc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a6befc ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00a6befc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a6befc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a6befc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a6befc bytes 29813491
+ 00a6befc bytes 29413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1922cbad8c3fe28fe376a69b546b990a"></a>

### [`00a6d000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d000.md) → [`00a6d000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d000.md) FUN_00a6d000

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
      "definition_site": "00a6d014",
      "incomplete_value": false,
      "site": "00a6d018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d014",
      "incomplete_value": false,
      "site": "00a6d018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00a6d018",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d018",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d000.md#insn-00a6d014)
- 新版 [`00a6d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d000.md#insn-00a6d014)

~~~diff
- 00a6d014 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a6d014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d014 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 00a6d014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d014 bytes 08813091
+ 00a6d014 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d6c2f4b87a4c500542243f8e4406df"></a>

### [`00a6d024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d024.md) → [`00a6d024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d024.md) FUN_00a6d024

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
      "definition_site": "00a6d028",
      "incomplete_value": false,
      "site": "00a6d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d028",
      "incomplete_value": false,
      "site": "00a6d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00a6d02c",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d02c",
      "DATA",
      [
        "storage",
        "00c0dcd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d024.md#insn-00a6d028)
- 新版 [`00a6d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d024.md#insn-00a6d028)

~~~diff
- 00a6d028 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a6d028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d028 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 00a6d028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d028 bytes 08813091
+ 00a6d028 bytes 08413391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf860bee37cec11eb3488063a31d5ec"></a>

### [`00a6d1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d1d8.md) → [`00a6d1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d1d8.md) FUN_00a6d1d8

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
      "definition_site": "00a6d1ec",
      "incomplete_value": false,
      "site": "00a6d1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d1ec",
      "incomplete_value": false,
      "site": "00a6d1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "00a6d1f0",
      "DATA",
      [
        "storage",
        "00c0dca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d1f0",
      "DATA",
      [
        "storage",
        "00c0dd50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d1d8.md#insn-00a6d1ec)
- 新版 [`00a6d1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d1d8.md#insn-00a6d1ec)

~~~diff
- 00a6d1ec ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a6d1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d1ec ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00a6d1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d1ec bytes 08813291
+ 00a6d1ec bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613cd2e08888a52ed8091caef10447f5"></a>

### [`00a6d1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d1fc.md) → [`00a6d1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d1fc.md) FUN_00a6d1fc

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
      "definition_site": "00a6d200",
      "incomplete_value": false,
      "site": "00a6d204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d200",
      "incomplete_value": false,
      "site": "00a6d204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "00a6d204",
      "DATA",
      [
        "storage",
        "00c0dca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d204",
      "DATA",
      [
        "storage",
        "00c0dd50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d1fc.md#insn-00a6d200)
- 新版 [`00a6d200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d1fc.md#insn-00a6d200)

~~~diff
- 00a6d200 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a6d200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d200 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00a6d200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d200 bytes 08813291
+ 00a6d200 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98bacb1525e41b5ee152041590d84218"></a>

### [`00a6d33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d33c.md) → [`00a6d33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d33c.md) FUN_00a6d33c

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
      "definition_site": "00a6d350",
      "incomplete_value": false,
      "site": "00a6d354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d350",
      "incomplete_value": false,
      "site": "00a6d354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00a6d354",
      "DATA",
      [
        "storage",
        "00c0dd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d354",
      "DATA",
      [
        "storage",
        "00c0ddd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d33c.md#insn-00a6d350)
- 新版 [`00a6d350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d33c.md#insn-00a6d350)

~~~diff
- 00a6d350 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a6d350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d350 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00a6d350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d350 bytes 08813491
+ 00a6d350 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90358741184ebcc16508366ef4f91e9"></a>

### [`00a6d360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d360.md) → [`00a6d360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d360.md) FUN_00a6d360

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
      "definition_site": "00a6d364",
      "incomplete_value": false,
      "site": "00a6d368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d364",
      "incomplete_value": false,
      "site": "00a6d368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00a6d368",
      "DATA",
      [
        "storage",
        "00c0dd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d368",
      "DATA",
      [
        "storage",
        "00c0ddd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d360.md#insn-00a6d364)
- 新版 [`00a6d364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d360.md#insn-00a6d364)

~~~diff
- 00a6d364 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a6d364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d364 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00a6d364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d364 bytes 08813491
+ 00a6d364 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16bcb194eec0fefe414ab96c63dbd02c"></a>

### [`00a6d4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d4f4.md) → [`00a6d4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d4f4.md) _INIT_238

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
      "definition_site": "00a6d530",
      "incomplete_value": true,
      "site": "00a6d54c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6d530",
      "incomplete_value": true,
      "site": "00a6d54c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6d554",
      "incomplete_value": true,
      "site": "00a6d570",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6d554",
      "incomplete_value": true,
      "site": "00a6d570",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6d574",
      "incomplete_value": true,
      "site": "00a6d590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6d574",
      "incomplete_value": true,
      "site": "00a6d590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a6d530",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a6d554",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a6d574",
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
      "00a6d530",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a6d554",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a6d574",
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

- 旧版 [`00a6d520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d4f4.md#insn-00a6d520) · [`00a6d528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d4f4.md#insn-00a6d528)
- 新版 [`00a6d520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d4f4.md#insn-00a6d520) · [`00a6d528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d4f4.md#insn-00a6d528)

~~~diff
- 00a6d520 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00a6d520 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a6d520 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a6d520 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a6d520 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00a6d520 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a6d520 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a6d520 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a6d520 bytes 73822491
+ 00a6d520 bytes 73822791
- 00a6d528 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a6d528 bytes c9c1ffd0
+ 00a6d528 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a6d528 bytes c9c1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f49674079b34aa262ffc6d8f5e7135f"></a>

### [`00a6d884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d884.md) → [`00a6d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md) FUN_00a6d884

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00707d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00707/00707d84.md) [`009009cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009009cc.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00707d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707d84.md) [`009009cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) · 呼出先 0件 

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
      "definition_site": "00a6d88c",
      "incomplete_value": false,
      "site": "00a6d890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d88c",
      "incomplete_value": false,
      "site": "00a6d890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "00a6d890",
      "DATA",
      [
        "storage",
        "00c0dda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d890",
      "DATA",
      [
        "storage",
        "00c0de50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d884.md#insn-00a6d88c)
- 新版 [`00a6d88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md#insn-00a6d88c)

~~~diff
- 00a6d88c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a6d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d88c ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00a6d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d88c bytes 08813691
+ 00a6d88c bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b2b4722c34daeffc351227804ab2bd"></a>

### [`00a6d8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md) → [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) FUN_00a6d8b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00707e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00707/00707e2c.md) [`00707e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00707/00707e88.md) [`00900d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900d80.md) [`00900e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900e0c.md) [`00a6de44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6de44.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 6件 [`00707e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e2c.md) [`00707e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707e88.md) [`00900d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900d80.md) [`00900e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900e0c.md) [`00a6de44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6de44.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6d8d0",
      "incomplete_value": false,
      "site": "00a6d8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6d8d0",
      "incomplete_value": false,
      "site": "00a6d8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "00a6d8d4",
      "DATA",
      [
        "storage",
        "00c0dda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6d8d4",
      "DATA",
      [
        "storage",
        "00c0de50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6d8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md#insn-00a6d8d0)
- 新版 [`00a6d8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md#insn-00a6d8d0)

~~~diff
- 00a6d8d0 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a6d8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6d8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6d8d0 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00a6d8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6d8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6d8d0 bytes 08813691
+ 00a6d8d0 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf90e79326267e54d92f5fbc315dceb"></a>

### [`00a6db78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6db78.md) → [`00a6db78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6db78.md) FUN_00a6db78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00900ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900ae0.md) · 呼出先 7件 [`00a6dea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6dea4.md) [`00a6defc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6defc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00900ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900ae0.md) · 呼出先 7件 [`00a6dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6dea4.md) [`00a6defc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6defc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6dbc0",
      "incomplete_value": false,
      "site": "00a6dbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6dbc0",
      "incomplete_value": false,
      "site": "00a6dbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "00a6dbc8",
      "DATA",
      [
        "storage",
        "00c0ddd0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6dc2c",
      "READ",
      [
        "storage",
        "00c0dde0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6dbc8",
      "DATA",
      [
        "storage",
        "00c0de80",
        null,
        "pointer"
      ]
    ],
    [
      "00a6dc2c",
      "READ",
      [
        "storage",
        "00c0de90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6dbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6db78.md#insn-00a6dbc0) · [`00a6dbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6db78.md#insn-00a6dbc4)
- 新版 [`00a6dbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6db78.md#insn-00a6dbc0) · [`00a6dbc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6db78.md#insn-00a6dbc4)

~~~diff
- 00a6dbc0 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00a6dbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6dbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6dbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6dbc0 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00a6dbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6dbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6dbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6dbc0 bytes 08413791
+ 00a6dbc0 bytes 08013a91
- 00a6dbc4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00a6dbc4 bytes f50300aa
+ 00a6dbc4 ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 00a6dbc4 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8d940c80845324fad39ba6f565af74"></a>

### [`00a6e058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e058.md) → [`00a6e058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e058.md) FUN_00a6e058

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a6defc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6defc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a6defc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6defc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00a6e064",
      "incomplete_value": false,
      "site": "00a6e068",
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
      "definition_site": "00a6e064",
      "incomplete_value": false,
      "site": "00a6e068",
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
      "00a6e064",
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
      "00a6e064",
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

- 旧版 [`00a6e064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e058.md#insn-00a6e064)
- 新版 [`00a6e064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e058.md#insn-00a6e064)

~~~diff
- 00a6e064 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00a6e064 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a6e064 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a6e064 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6e064 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00a6e064 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6e064 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6e064 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a6e064 bytes 00280c91
+ 00a6e064 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3254c61061518fa0f0550b7a47d7906"></a>

### [`00a6e06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e06c.md) → [`00a6e06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e06c.md) _INIT_239

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
      "definition_site": "00a6e0a8",
      "incomplete_value": true,
      "site": "00a6e0c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6e0a8",
      "incomplete_value": true,
      "site": "00a6e0c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6e0cc",
      "incomplete_value": true,
      "site": "00a6e0e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6e0cc",
      "incomplete_value": true,
      "site": "00a6e0e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6e0ec",
      "incomplete_value": true,
      "site": "00a6e108",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a6e0ec",
      "incomplete_value": true,
      "site": "00a6e108",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a6e0a8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a6e0cc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a6e0ec",
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
      "00a6e0a8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a6e0cc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a6e0ec",
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

- 旧版 [`00a6e098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e06c.md#insn-00a6e098) · [`00a6e0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e06c.md#insn-00a6e0a0)
- 新版 [`00a6e098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e06c.md#insn-00a6e098) · [`00a6e0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e06c.md#insn-00a6e0a0)

~~~diff
- 00a6e098 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00a6e098 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a6e098 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a6e098 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a6e098 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00a6e098 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a6e098 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a6e098 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a6e098 bytes 73e22491
+ 00a6e098 bytes 73e22791
- 00a6e0a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a6e0a0 bytes c9c1ffb0
+ 00a6e0a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a6e0a0 bytes c9c1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e467a8a087bb3f4bd305a7ff8e48b900"></a>

### [`00a6e3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md) → [`00a6e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md) FUN_00a6e3fc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a72648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a72648.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.44% / 新版 88.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 58件, `store_destination` 35件, `store_value` 42件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6e444",
      "incomplete_value": false,
      "site": "00a6e448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6e444",
      "incomplete_value": false,
      "site": "00a6e448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00a6e52c",
      "incomplete_value": true,
      "site": "00a6e52c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a6e52c",
      "incomplete_value": true,
      "site": "00a6e52c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6e548",
      "incomplete_value": true,
      "site": "00a6e548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00a6e548",
      "incomplete_value": true,
      "site": "00a6e548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 69,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a6e448",
      "DATA",
      [
        "storage",
        "00c0de20",
        null,
        "pointer"
      ]
    ],
    [
      "00a6e504",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6e518",
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
      "00a6e448",
      "DATA",
      [
        "storage",
        "00c0ded0",
        null,
        "pointer"
      ]
    ],
    [
      "00a6e504",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a6e518",
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

- 旧版 [`00a6e444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md#insn-00a6e444) · [`00a6e4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md#insn-00a6e4cc) · [`00a6e4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md#insn-00a6e4d0)
- 新版 [`00a6e444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md#insn-00a6e444) · [`00a6e4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md#insn-00a6e4cc) · [`00a6e4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md#insn-00a6e4d0)

~~~diff
- 00a6e444 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00a6e444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6e444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6e444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6e444 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00a6e444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6e444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6e444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6e444 bytes 08813891
+ 00a6e444 bytes 08413b91
- 00a6e4cc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00a6e4cc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00a6e4cc bytes a80d00d0
+ 00a6e4cc bytes a80d00f0
- 00a6e4d0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a6e4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a6e4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a6e4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6e4d0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00a6e4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6e4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6e4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a6e4d0 bytes 08e13d91
+ 00a6e4d0 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18532d6efa81f90895fd3e8223448700"></a>

### [`00a71320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71320.md) → [`00a71320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71320.md) FUN_00a71320

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) [`00a6e3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md) [`00a81e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0071a0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071a/0071a0c4.md) [`009019f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/009019f4.md) [`00a25194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a25/00a25194.md)
- 新版 呼出元 3件 [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`00a6e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md) [`00a81e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00a25194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25194.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.97% / 新版 90.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a71368",
      "incomplete_value": true,
      "site": "00a7137c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:791:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a71368",
      "incomplete_value": true,
      "site": "00a7137c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:798:8"
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
      "definition_site": "00a713ac",
      "incomplete_value": true,
      "site": "00a713c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a713ac",
      "incomplete_value": true,
      "site": "00a713c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a1b:8"
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
      "definition_site": "00a71464",
      "incomplete_value": true,
      "site": "00a71464",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a71464",
      "incomplete_value": true,
      "site": "00a71464",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db:8"
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
      "00a71368",
      "READ",
      [
        "storage",
        "002a2798",
        null,
        "string"
      ]
    ],
    [
      "00a713ac",
      "READ",
      [
        "storage",
        "002aaa1b",
        null,
        "string"
      ]
    ],
    [
      "00a71454",
      "READ",
      [
        "storage",
        "002ac0db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a71368",
      "READ",
      [
        "storage",
        "002a2791",
        null,
        "string"
      ]
    ],
    [
      "00a713ac",
      "READ",
      [
        "storage",
        "002aaa21",
        null,
        "string"
      ]
    ],
    [
      "00a71454",
      "READ",
      [
        "storage",
        "002ac0d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a71360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71320.md#insn-00a71360) · [`00a713a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71320.md#insn-00a713a4) · [`00a7144c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71320.md#insn-00a7144c)
- 新版 [`00a71360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71320.md#insn-00a71360) · [`00a713a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71320.md#insn-00a713a4) · [`00a7144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71320.md#insn-00a7144c)

~~~diff
- 00a71360 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00a71360 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a71360 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a71360 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a71360 ["COPY", "tmp:0:8", ["const:791:8"]]
+ 00a71360 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a71360 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a71360 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a71360 bytes 29611e91
+ 00a71360 bytes 29451e91
- 00a713a4 ["COPY", "tmp:0:8", ["const:a1b:8"]]
- 00a713a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a713a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a713a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a713a4 ["COPY", "tmp:0:8", ["const:a21:8"]]
+ 00a713a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a713a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a713a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a713a4 bytes 296d2891
+ 00a713a4 bytes 29852891
- 00a7144c ["COPY", "tmp:0:8", ["const:db:8"]]
- 00a7144c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a7144c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a7144c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a7144c ["COPY", "tmp:0:8", ["const:d2:8"]]
+ 00a7144c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7144c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a7144c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a7144c bytes 296d0391
+ 00a7144c bytes 29490391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d747cc86b7b683e07817acc728c310a6"></a>

### [`00a715d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a715d4.md) → [`00a715d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a715d4.md) FUN_00a715d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00a6e3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6e/00a6e3fc.md) [`00a81e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md) [`00a8d178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md) [`00a8f828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f828.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 4件 [`00a6e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6e/00a6e3fc.md) [`00a81e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md) [`00a8d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md) [`00a8f828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f828.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.81% / 新版 92.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a717d0",
      "incomplete_value": false,
      "site": "00a717d0",
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
      "definition_site": "00a717d0",
      "incomplete_value": false,
      "site": "00a717d0",
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
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a717a8",
      "incomplete_value": true,
      "site": "00a717ac",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a717a8",
      "incomplete_value": true,
      "site": "00a717ac",
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
            "const:f78:8"
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
      "definition_site": "00a717f0",
      "incomplete_value": false,
      "site": "00a717f4",
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
      "definition_site": "00a717f0",
      "incomplete_value": false,
      "site": "00a717f4",
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
      "00a71608",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a716e4",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00a716e8",
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
      "00a71608",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a716e4",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00a716e8",
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

- 旧版 [`00a71600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a715d4.md#insn-00a71600) · [`00a71604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a715d4.md#insn-00a71604) · [`00a716e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a715d4.md#insn-00a716e0)
- 新版 [`00a71600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a715d4.md#insn-00a71600) · [`00a71604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a715d4.md#insn-00a71604) · [`00a716e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a715d4.md#insn-00a716e0)

~~~diff
- 00a71600 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00a71600 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00a71600 bytes 880d00f0
+ 00a71600 bytes a80d0090
- 00a71604 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a71604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a71604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a71604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a71604 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00a71604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a71604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a71604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a71604 bytes 08e13d91
+ 00a71604 bytes 08e10091
- 00a716e0 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 00a716e0 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 00a716e0 bytes 800d00f0
+ 00a716e0 bytes a00d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f6cf905b57762790625d1797808360e"></a>

### [`00a71a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71a9c.md) → [`00a71a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71a9c.md) FUN_00a71a9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00a72648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a72648.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) [`00a8d178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md) · 呼出先 14件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004752f8.md) [`0060dcac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060dcac.md) [`00640910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00640/00640910.md) [`0066f824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0066f/0066f824.md)
- 新版 呼出元 3件 [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) [`00a8d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md) · 呼出先 14件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`0060dcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md) [`00640910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md) [`0066f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.39% / 新版 91.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_destination` 12件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a71af4",
      "incomplete_value": true,
      "site": "00a71af4",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a71af4",
      "incomplete_value": true,
      "site": "00a71af4",
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
            "const:638:8"
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
      "definition_site": "00a71d84",
      "incomplete_value": true,
      "site": "00a71d84",
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
                "register:4008:8"
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
      "definition_site": "00a71d84",
      "incomplete_value": true,
      "site": "00a71d84",
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
                "register:4008:8"
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a71d88",
      "incomplete_value": true,
      "site": "00a71d88",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a71d88",
      "incomplete_value": true,
      "site": "00a71d88",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a71ae4",
      "READ",
      [
        "storage",
        "00c24638",
        null,
        "undefined4"
      ]
    ],
    [
      "00a71af4",
      "WRITE",
      [
        "storage",
        "00c24638",
        null,
        "undefined4"
      ]
    ],
    [
      "00a71af8",
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
      "00a71ae4",
      "READ",
      [
        "storage",
        "00c246e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00a71af4",
      "WRITE",
      [
        "storage",
        "00c246e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00a71af8",
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

- 旧版 [`00a71af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71a9c.md#insn-00a71af4) · [`00a71ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71a9c.md#insn-00a71ae4) · [`00a71af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a71/00a71a9c.md#insn-00a71af8)
- 新版 [`00a71af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71a9c.md#insn-00a71af4) · [`00a71ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71a9c.md#insn-00a71ae4) · [`00a71af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71a9c.md#insn-00a71af8)

~~~diff
- 00a71af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:638:8"]]
- 00a71af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:4"]]
+ 00a71af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e8:8"]]
+ 00a71af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:4"]]
- 00a71af4 bytes 133906b9
+ 00a71af4 bytes 13e906b9
- 00a71ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:638:8"]]
- 00a71ae4 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00a71ae4 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00a71ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e8:8"]]
+ 00a71ae4 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00a71ae4 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00a71ae4 bytes 093946b9
+ 00a71ae4 bytes 09e946b9
- 00a71af8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 00a71af8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a71af8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 00a71af8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a71af8 bytes 20dd44f9
+ 00a71af8 bytes 203d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58eee2e19efdbbf088ce6005efa297b4"></a>

### [`00a720fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a720fc.md) → [`00a720fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a720fc.md) FUN_00a720fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a8e548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md) [`00a91e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91e14.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md)
- 新版 呼出元 2件 [`00a8e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md) [`00a91e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91e14.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a721b0",
      "incomplete_value": true,
      "site": "00a721b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:26c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a721b0",
      "incomplete_value": true,
      "site": "00a721b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1df:8"
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
      "00a721a0",
      "READ",
      [
        "storage",
        "002921df",
        null,
        "string"
      ]
    ],
    [
      "00a72220",
      "READ",
      [
        "storage",
        "002a8b49",
        null,
        "string"
      ]
    ],
    [
      "00a72288",
      "DATA",
      [
        "storage",
        "00c0de58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a721a0",
      "READ",
      [
        "storage",
        "0029226c",
        null,
        "string"
      ]
    ],
    [
      "00a72220",
      "READ",
      [
        "storage",
        "002a8ab5",
        null,
        "string"
      ]
    ],
    [
      "00a72288",
      "DATA",
      [
        "storage",
        "00c0df08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a72198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a720fc.md#insn-00a72198) · [`00a72218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a720fc.md#insn-00a72218) · [`00a72280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a720fc.md#insn-00a72280)
- 新版 [`00a72198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a720fc.md#insn-00a72198) · [`00a72218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a720fc.md#insn-00a72218) · [`00a72280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a720fc.md#insn-00a72280)

~~~diff
- 00a72198 ["COPY", "tmp:0:8", ["const:1df:8"]]
- 00a72198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a72198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a72198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a72198 ["COPY", "tmp:0:8", ["const:26c:8"]]
+ 00a72198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a72198 bytes 297d0791
+ 00a72198 bytes 29b10991
- 00a72218 ["COPY", "tmp:0:8", ["const:b49:8"]]
- 00a72218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a72218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a72218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a72218 ["COPY", "tmp:0:8", ["const:ab5:8"]]
+ 00a72218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a72218 bytes 29252d91
+ 00a72218 bytes 29d52a91
- 00a72280 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a72280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a72280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a72280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a72280 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00a72280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a72280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a72280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a72280 bytes 08613991
+ 00a72280 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d969645ab8b90bcf81bb64e527ff84"></a>

### [`00a723c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a723c8.md) → [`00a723c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a723c8.md) FUN_00a723c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a8e548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`00887e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/00887e18.md)
- 新版 呼出元 1件 [`00a8e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`00887e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/00887e18.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7242c",
      "incomplete_value": true,
      "site": "00a7242c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c29:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7242c",
      "incomplete_value": true,
      "site": "00a7242c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9c:8"
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
      "definition_site": "00a724a0",
      "incomplete_value": true,
      "site": "00a724b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:276:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a724a0",
      "incomplete_value": true,
      "site": "00a724b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e9:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a72508",
      "incomplete_value": false,
      "site": "00a72508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a72508",
      "incomplete_value": false,
      "site": "00a72508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00a7241c",
      "READ",
      [
        "storage",
        "0029db9c",
        null,
        "string"
      ]
    ],
    [
      "00a724a0",
      "READ",
      [
        "storage",
        "002921e9",
        null,
        "string"
      ]
    ],
    [
      "00a72508",
      "DATA",
      [
        "storage",
        "00c0ded8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7241c",
      "READ",
      [
        "storage",
        "0029dc29",
        null,
        "string"
      ]
    ],
    [
      "00a724a0",
      "READ",
      [
        "storage",
        "00292276",
        null,
        "string"
      ]
    ],
    [
      "00a72508",
      "DATA",
      [
        "storage",
        "00c0df88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a72414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a723c8.md#insn-00a72414) · [`00a72498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a723c8.md#insn-00a72498) · [`00a72500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a723c8.md#insn-00a72500)
- 新版 [`00a72414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a723c8.md#insn-00a72414) · [`00a72498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a723c8.md#insn-00a72498) · [`00a72500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a723c8.md#insn-00a72500)

~~~diff
- 00a72414 ["COPY", "tmp:0:8", ["const:b9c:8"]]
- 00a72414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a72414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a72414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a72414 ["COPY", "tmp:0:8", ["const:c29:8"]]
+ 00a72414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a72414 bytes 29712e91
+ 00a72414 bytes 29a53091
- 00a72498 ["COPY", "tmp:0:8", ["const:1e9:8"]]
- 00a72498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a72498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a72498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a72498 ["COPY", "tmp:0:8", ["const:276:8"]]
+ 00a72498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a72498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a72498 bytes 29a50791
+ 00a72498 bytes 29d90991
- 00a72500 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00a72500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a72500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a72500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a72500 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a72500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a72500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a72500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a72500 bytes 08613b91
+ 00a72500 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad90776a7c7835fb1d40e049391dd36"></a>

### [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) → [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) FUN_00a7888c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 139件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 139件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.42% / 新版 97.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 8件, `call_argument_candidate` 59件, `store_destination` 36件, `store_value` 23件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a7995c",
      "incomplete_value": false,
      "site": "00a79964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a7995c",
      "incomplete_value": false,
      "site": "00a79964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 107,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a79990",
      "incomplete_value": false,
      "site": "00a79998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a79990",
      "incomplete_value": false,
      "site": "00a79998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "ordinal": 110,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a799b0",
      "incomplete_value": false,
      "site": "00a799bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a799b0",
      "incomplete_value": false,
      "site": "00a799bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a78d50",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a78d5c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a78d64",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a78d50",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a78d5c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a78d64",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a78d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md#insn-00a78d50) · [`00a78d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md#insn-00a78d5c) · [`00a78d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md#insn-00a78d64)
- 新版 [`00a78d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md#insn-00a78d50) · [`00a78d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md#insn-00a78d5c) · [`00a78d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md#insn-00a78d64)

~~~diff
- 00a78d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a78d50 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a78d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a78d50 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a78d50 bytes 00dd44f9
+ 00a78d50 bytes 003d45f9
- 00a78d5c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a78d5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a78d5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a78d5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a78d5c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a78d5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a78d5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a78d5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a78d5c bytes 21603691
+ 00a78d5c bytes 21203991
- 00a78d64 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a78d64 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a78d64 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a78d64 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a78d64 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a78d64 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a78d64 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a78d64 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a78d64 bytes 42c03891
+ 00a78d64 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522f260b258db665b2241a4c826e0b6d"></a>

### [`00a806b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a80/00a806b4.md) → [`00a806b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a806b4.md) FUN_00a806b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`007c77c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f354.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 3件 [`007c77c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a811f8",
      "incomplete_value": true,
      "site": "00a81204",
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
            "const:a72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a811f8",
      "incomplete_value": true,
      "site": "00a81204",
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
            "const:a79:8"
          ]
        ]
      ]
    },
    "ordinal": 102,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a81224",
      "incomplete_value": false,
      "site": "00a8122c",
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
            "const:85b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a81224",
      "incomplete_value": false,
      "site": "00a8122c",
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
            "const:855:8"
          ]
        ]
      ]
    },
    "ordinal": 103,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a812a8",
      "incomplete_value": false,
      "site": "00a812b0",
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
            "const:a83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a812a8",
      "incomplete_value": false,
      "site": "00a812b0",
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
            "const:a8c:8"
          ]
        ]
      ]
    },
    "ordinal": 108,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a811f8",
      "PARAM",
      [
        "storage",
        "002a6a79",
        null,
        "string"
      ]
    ],
    [
      "00a81224",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ],
    [
      "00a812a8",
      "PARAM",
      [
        "storage",
        "002aca8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a811f8",
      "PARAM",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ],
    [
      "00a81224",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ],
    [
      "00a812a8",
      "PARAM",
      [
        "storage",
        "002aca83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a811f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a80/00a806b4.md#insn-00a811f8) · [`00a81224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a80/00a806b4.md#insn-00a81224) · [`00a812a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a80/00a806b4.md#insn-00a812a8)
- 新版 [`00a811f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a806b4.md#insn-00a811f8) · [`00a81224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a806b4.md#insn-00a81224) · [`00a812a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a806b4.md#insn-00a812a8)

~~~diff
- 00a811f8 ["COPY", "tmp:0:8", ["const:a79:8"]]
- 00a811f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a811f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a811f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a811f8 ["COPY", "tmp:0:8", ["const:a72:8"]]
+ 00a811f8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a811f8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a811f8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a811f8 bytes 42e42991
+ 00a811f8 bytes 42c82991
- 00a81224 ["COPY", "tmp:0:8", ["const:855:8"]]
- 00a81224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a81224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a81224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a81224 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 00a81224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a81224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a81224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a81224 bytes 21542191
+ 00a81224 bytes 216c2191
- 00a812a8 ["COPY", "tmp:0:8", ["const:a8c:8"]]
- 00a812a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a812a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a812a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a812a8 ["COPY", "tmp:0:8", ["const:a83:8"]]
+ 00a812a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a812a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a812a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a812a8 bytes 21302a91
+ 00a812a8 bytes 210c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef4f9f95822fcf96970603de37ad053"></a>

### [`00a81e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md) → [`00a81e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md) FUN_00a81e60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009121c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00912/009121c4.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) · 呼出先 17件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063f/0063fa4c.md) [`00883d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d5c.md)
- 新版 呼出元 2件 [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 17件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md) [`00883d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d5c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a82258",
      "incomplete_value": false,
      "site": "00a82258",
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
      "definition_site": "00a82258",
      "incomplete_value": false,
      "site": "00a82258",
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
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a8225c",
      "incomplete_value": false,
      "site": "00a8225c",
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
      "definition_site": "00a8225c",
      "incomplete_value": false,
      "site": "00a8225c",
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
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a82258",
      "incomplete_value": false,
      "site": "00a8225c",
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
      "definition_site": "00a82258",
      "incomplete_value": false,
      "site": "00a8225c",
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
      "00a81f64",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a81f70",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a81f78",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a81f64",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a81f70",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a81f78",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a81f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md#insn-00a81f64) · [`00a81f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md#insn-00a81f70) · [`00a81f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a81/00a81e60.md#insn-00a81f78)
- 新版 [`00a81f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md#insn-00a81f64) · [`00a81f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md#insn-00a81f70) · [`00a81f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a81/00a81e60.md#insn-00a81f78)

~~~diff
- 00a81f64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a81f64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a81f64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a81f64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a81f64 bytes 00dd44f9
+ 00a81f64 bytes 003d45f9
- 00a81f70 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a81f70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a81f70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a81f70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a81f70 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a81f70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a81f70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a81f70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a81f70 bytes 21603691
+ 00a81f70 bytes 21203991
- 00a81f78 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a81f78 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a81f78 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a81f78 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a81f78 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a81f78 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a81f78 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a81f78 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a81f78 bytes 42c03891
+ 00a81f78 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78bf047ce78b7d1990edb53d52e58971"></a>

### [`00a82394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a82/00a82394.md) → [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) FUN_00a82394

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 104件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 104件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `store_value` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a825c0",
      "incomplete_value": true,
      "site": "00a825d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a825c0",
      "incomplete_value": true,
      "site": "00a825d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00a825c0",
      "incomplete_value": true,
      "site": "00a825dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a825c0",
      "incomplete_value": true,
      "site": "00a825dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a82a18",
      "incomplete_value": true,
      "site": "00a82a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d27:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a82a18",
      "incomplete_value": true,
      "site": "00a82a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2e:8"
              ]
            ]
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
      "00a823d4",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a823e8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a823f0",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a823d4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a823e8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a823f0",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a823d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a82/00a82394.md#insn-00a823d4) · [`00a823e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a82/00a82394.md#insn-00a823e8) · [`00a823f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a82/00a82394.md#insn-00a823f0)
- 新版 [`00a823d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md#insn-00a823d4) · [`00a823e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md#insn-00a823e8) · [`00a823f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md#insn-00a823f0)

~~~diff
- 00a823d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a823d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a823d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a823d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a823d4 bytes 08dd44f9
+ 00a823d4 bytes 083d45f9
- 00a823e8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a823e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a823e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a823e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a823e8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a823e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a823e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a823e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a823e8 bytes 21603691
+ 00a823e8 bytes 21203991
- 00a823f0 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a823f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a823f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a823f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a823f0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a823f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a823f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a823f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a823f0 bytes 42c03891
+ 00a823f0 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf3443187eac2194db701b1912cd242"></a>

### [`00a8b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8b/00a8b028.md) → [`00a8b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md) FUN_00a8b028

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a82394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a82/00a82394.md) [`00a914b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a914b8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md)
- 新版 呼出元 2件 [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) [`00a914b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a8b05c",
      "incomplete_value": true,
      "site": "00a8b05c",
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
      "definition_site": "00a8b05c",
      "incomplete_value": true,
      "site": "00a8b05c",
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
      "definition_site": "00a8b064",
      "incomplete_value": false,
      "site": "00a8b074",
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
      "definition_site": "00a8b064",
      "incomplete_value": false,
      "site": "00a8b074",
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
      "definition_site": "00a8b06c",
      "incomplete_value": false,
      "site": "00a8b074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8b06c",
      "incomplete_value": false,
      "site": "00a8b074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a8b050",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8b064",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8b06c",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8b050",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8b064",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8b06c",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8b050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8b/00a8b028.md#insn-00a8b050) · [`00a8b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8b/00a8b028.md#insn-00a8b064) · [`00a8b06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8b/00a8b028.md#insn-00a8b06c)
- 新版 [`00a8b050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b050) · [`00a8b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b064) · [`00a8b06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md#insn-00a8b06c)

~~~diff
- 00a8b050 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8b050 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8b050 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8b050 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8b050 bytes 00dd44f9
+ 00a8b050 bytes 003d45f9
- 00a8b064 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8b064 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8b064 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8b064 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8b064 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8b064 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8b064 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8b064 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8b064 bytes 21603691
+ 00a8b064 bytes 21203991
- 00a8b06c ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8b06c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8b06c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8b06c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8b06c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8b06c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8b06c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8b06c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8b06c bytes 42c03891
+ 00a8b06c bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

