# v15.7.2 → v15.7.3 · 最優先の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-13d1562b16d1f0eca7a142a3cd5a2dae"></a>

### [`0058ee34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ee34.md) → [`0058ee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ee34.md) FUN_0058ee34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00591af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591af4.md) · 呼出先 6件 [`0058ef88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ef88.md) [`00591c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591c30.md) [`00591c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591c34.md) [`00591d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d58.md) [`00591d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d5c.md)
- 新版 呼出元 1件 [`00591af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591af4.md) · 呼出先 6件 [`0058ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md) [`00591c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c30.md) [`00591c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c34.md) [`00591d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d58.md) [`00591d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ee5c",
      "incomplete_value": false,
      "site": "0058ee5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ee5c",
      "incomplete_value": false,
      "site": "0058ee5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "definition_site": "0058ee74",
      "incomplete_value": false,
      "site": "0058ee74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ee74",
      "incomplete_value": false,
      "site": "0058ee74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "0058ee5c",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058ee74",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058eeb0",
      "READ",
      [
        "storage",
        "00bf2ad8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058ee5c",
      "DATA",
      [
        "storage",
        "00bf2ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058ee74",
      "DATA",
      [
        "storage",
        "00bf2b68",
        null,
        "undefined *"
      ]
    ],
    [
      "0058eeb0",
      "READ",
      [
        "storage",
        "00bf2b88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ee58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ee34.md#insn-0058ee58) · [`0058ee6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ee34.md#insn-0058ee6c)
- 新版 [`0058ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ee34.md#insn-0058ee58) · [`0058ee6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ee34.md#insn-0058ee6c)

~~~diff
- 0058ee58 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 0058ee58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ee58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ee58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ee58 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0058ee58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ee58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ee58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ee58 bytes 08e12891
+ 0058ee58 bytes 08a12b91
- 0058ee6c ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 0058ee6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ee6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ee6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ee6c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0058ee6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ee6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ee6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ee6c bytes 08e12a91
+ 0058ee6c bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9d5029f30dae64221d3a9d14e77fd6"></a>

### [`0058ef88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ef88.md) → [`0058ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md) FUN_0058ef88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058ee34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ee34.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`0057a9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057a/0057a9e0.md) [`00593688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593688.md) [`005939d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005939d4.md)
- 新版 呼出元 1件 [`0058ee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ee34.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`0057a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057a/0057a9e0.md) [`00593688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md) [`005939d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005939d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f0c4",
      "incomplete_value": false,
      "site": "0058f0c8",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0058f0c4",
      "incomplete_value": false,
      "site": "0058f0c8",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f158",
      "incomplete_value": false,
      "site": "0058f158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f158",
      "incomplete_value": false,
      "site": "0058f158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "0058f0c8",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f158",
      "DATA",
      [
        "storage",
        "00bf31f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f1cc",
      "READ",
      [
        "storage",
        "00bf3220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f0c8",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f158",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f1cc",
      "READ",
      [
        "storage",
        "00bf32d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ef88.md#insn-0058f0bc) · [`0058f150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ef88.md#insn-0058f150)
- 新版 [`0058f0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md#insn-0058f0bc) · [`0058f150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md#insn-0058f150)

~~~diff
- 0058f0bc ["COPY", "tmp:0:8", ["const:950:8"]]
- 0058f0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f0bc ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0058f0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f0bc bytes 08412591
+ 0058f0bc bytes 08012891
- 0058f150 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 0058f150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f150 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0058f150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f150 bytes 08e10791
+ 0058f150 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3acd783888d1fcffff037a3c9dc8bba"></a>

### [`0058f3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f3b8.md) → [`0058f3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f3b8.md) FUN_0058f3b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008629ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00862/008629ec.md) · 呼出先 6件 [`0058f504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md) [`00591df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591df0.md) [`00591df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591df4.md) [`005920e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005920e8.md) [`005920ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005920ec.md)
- 新版 呼出元 1件 [`008629ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md) · 呼出先 6件 [`0058f504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md) [`00591df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df0.md) [`00591df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df4.md) [`005920e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920e8.md) [`005920ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920ec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f3e0",
      "incomplete_value": false,
      "site": "0058f3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f3e0",
      "incomplete_value": false,
      "site": "0058f3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "definition_site": "0058f3f4",
      "incomplete_value": false,
      "site": "0058f3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f3f4",
      "incomplete_value": false,
      "site": "0058f3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "0058f3e0",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f3f4",
      "DATA",
      [
        "storage",
        "00bf2c18",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f42c",
      "READ",
      [
        "storage",
        "00bf2c38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058f3e0",
      "DATA",
      [
        "storage",
        "00bf2be8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f3f4",
      "DATA",
      [
        "storage",
        "00bf2cc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f42c",
      "READ",
      [
        "storage",
        "00bf2ce8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f3b8.md#insn-0058f3dc) · [`0058f3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f3b8.md#insn-0058f3f0)
- 新版 [`0058f3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f3b8.md#insn-0058f3dc) · [`0058f3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f3b8.md#insn-0058f3f0)

~~~diff
- 0058f3dc ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0058f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f3dc ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0058f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f3dc bytes 08e12c91
+ 0058f3dc bytes 08a12f91
- 0058f3f0 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0058f3f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f3f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f3f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f3f0 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 0058f3f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f3f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f3f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f3f0 bytes 08613091
+ 0058f3f0 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f60d97b783b9f4e8f0a16e61d0eb8c8"></a>

### [`0058f504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md) → [`0058f504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md) FUN_0058f504

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058f3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f3b8.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md) [`00592b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592b14.md) [`00592eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592eb0.md)
- 新版 呼出元 1件 [`0058f3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f3b8.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md) [`00592b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md) [`00592eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f558",
      "incomplete_value": false,
      "site": "0058f55c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:dc8:8"
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
      "definition_site": "0058f558",
      "incomplete_value": false,
      "site": "0058f55c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:d18:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f5d4",
      "incomplete_value": false,
      "site": "0058f5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f5d4",
      "incomplete_value": false,
      "site": "0058f5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "definition_site": "0058f730",
      "incomplete_value": true,
      "site": "0058f734",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0058f730",
      "incomplete_value": true,
      "site": "0058f734",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0058f55c",
      "DATA",
      [
        "storage",
        "00bf0d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f5d4",
      "DATA",
      [
        "storage",
        "00bf30e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f648",
      "READ",
      [
        "storage",
        "00bf3110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f55c",
      "DATA",
      [
        "storage",
        "00bf0dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f5d4",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f648",
      "READ",
      [
        "storage",
        "00bf31c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md#insn-0058f550) · [`0058f5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md#insn-0058f5cc) · [`0058f728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md#insn-0058f728)
- 新版 [`0058f550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md#insn-0058f550) · [`0058f5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md#insn-0058f5cc) · [`0058f728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md#insn-0058f728)

~~~diff
- 0058f550 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0058f550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f550 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 0058f550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f550 bytes 08613491
+ 0058f550 bytes 08213791
- 0058f5cc ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0058f5cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f5cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f5cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f5cc ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0058f5cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f5cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f5cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f5cc bytes 08a10391
+ 0058f5cc bytes 08610691
- 0058f728 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0058f728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f728 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0058f728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f728 bytes 08412591
+ 0058f728 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821a02ffdec2f3c78dea08f0597c8433"></a>

### [`0058f864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f864.md) → [`0058f864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f864.md) FUN_0058f864

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0059153c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059153c.md) · 呼出先 6件 [`0058f9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md) [`00592180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592180.md) [`00592184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592184.md) [`00592208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592208.md) [`0059220c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059220c.md)
- 新版 呼出元 1件 [`0059153c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059153c.md) · 呼出先 6件 [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) [`00592180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592180.md) [`00592184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592184.md) [`00592208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592208.md) [`0059220c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059220c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f88c",
      "incomplete_value": false,
      "site": "0058f88c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f88c",
      "incomplete_value": false,
      "site": "0058f88c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "0058f8a0",
      "incomplete_value": false,
      "site": "0058f8a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f8a0",
      "incomplete_value": false,
      "site": "0058f8a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0058f88c",
      "DATA",
      [
        "storage",
        "00bf2c98",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f8a0",
      "DATA",
      [
        "storage",
        "00bf2d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f8d8",
      "READ",
      [
        "storage",
        "00bf2d48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058f88c",
      "DATA",
      [
        "storage",
        "00bf2d48",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f8a0",
      "DATA",
      [
        "storage",
        "00bf2dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058f8d8",
      "READ",
      [
        "storage",
        "00bf2df8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f864.md#insn-0058f888) · [`0058f89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f864.md#insn-0058f89c)
- 新版 [`0058f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f864.md#insn-0058f888) · [`0058f89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f864.md#insn-0058f89c)

~~~diff
- 0058f888 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0058f888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f888 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0058f888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f888 bytes 08613291
+ 0058f888 bytes 08213591
- 0058f89c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0058f89c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f89c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f89c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f89c ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0058f89c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f89c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f89c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f89c bytes 08a13491
+ 0058f89c bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8b9fe9efb6bacde9571a6283594252"></a>

### [`0058f9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md) → [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) FUN_0058f9b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058f864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f864.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`0057c274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057c/0057c274.md) [`00593e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593e50.md)
- 新版 呼出元 1件 [`0058f864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f864.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`0057c274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c274.md) [`00593e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.71% / 新版 97.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fa6c",
      "incomplete_value": false,
      "site": "0058fa70",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0058fa6c",
      "incomplete_value": false,
      "site": "0058fa70",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0058fa70",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fafc",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fb70",
      "READ",
      [
        "storage",
        "00bf3320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058fa70",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fafc",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fb70",
      "READ",
      [
        "storage",
        "00bf33d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md#insn-0058fa64) · [`0058faf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md#insn-0058faf4)
- 新版 [`0058fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md#insn-0058fa64) · [`0058faf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md#insn-0058faf4)

~~~diff
- 0058fa64 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0058fa64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058fa64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058fa64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058fa64 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0058fa64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fa64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fa64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058fa64 bytes 08412591
+ 0058fa64 bytes 08012891
- 0058faf4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0058faf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058faf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058faf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058faf4 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0058faf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058faf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058faf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058faf4 bytes 08e10b91
+ 0058faf4 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851aa573f33febf582b3b49c57a3c169"></a>

### [`0058fd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058fd5c.md) → [`0058fd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058fd5c.md) FUN_0058fd5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00592188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592188.md) · 呼出先 8件 [`0058ff20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md) [`005922a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005922a0.md) [`005922a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005922a4.md) [`005924c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924c0.md) [`005924c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924c4.md)
- 新版 呼出元 1件 [`00592188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592188.md) · 呼出先 8件 [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) [`005922a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a0.md) [`005922a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a4.md) [`005924c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c0.md) [`005924c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fd84",
      "incomplete_value": false,
      "site": "0058fd84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fd84",
      "incomplete_value": false,
      "site": "0058fd84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "definition_site": "0058fd98",
      "incomplete_value": false,
      "site": "0058fd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fd98",
      "incomplete_value": false,
      "site": "0058fd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "definition_site": "0058fdac",
      "incomplete_value": false,
      "site": "0058fdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fdac",
      "incomplete_value": false,
      "site": "0058fdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0058fd84",
      "DATA",
      [
        "storage",
        "00bf2da8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fd98",
      "DATA",
      [
        "storage",
        "00bf2e38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fdac",
      "DATA",
      [
        "storage",
        "00bf2f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058fd84",
      "DATA",
      [
        "storage",
        "00bf2e58",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fd98",
      "DATA",
      [
        "storage",
        "00bf2ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058fdac",
      "DATA",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058fd5c.md#insn-0058fd80) · [`0058fd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058fd5c.md#insn-0058fd94) · [`0058fda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058fd5c.md#insn-0058fda8)
- 新版 [`0058fd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058fd5c.md#insn-0058fd80) · [`0058fd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058fd5c.md#insn-0058fd94) · [`0058fda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058fd5c.md#insn-0058fda8)

~~~diff
- 0058fd80 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0058fd80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058fd80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058fd80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058fd80 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0058fd80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fd80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fd80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058fd80 bytes 08a13691
+ 0058fd80 bytes 08613991
- 0058fd94 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0058fd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058fd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058fd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058fd94 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058fd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058fd94 bytes 08e13891
+ 0058fd94 bytes 08a13b91
- 0058fda8 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0058fda8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058fda8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058fda8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058fda8 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 0058fda8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fda8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fda8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058fda8 bytes 08613c91
+ 0058fda8 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0981dd9e4592acb9b026c639c6d1f01"></a>

### [`0058ff20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md) → [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) FUN_0058ff20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058fd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058fd5c.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`0057de8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057d/0057de8c.md) [`00588ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00588/00588ce8.md) [`00588db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00588/00588db4.md)
- 新版 呼出元 1件 [`0058fd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058fd5c.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`0057de8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057de8c.md) [`00588ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588ce8.md) [`00588db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588db4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ffe0",
      "incomplete_value": false,
      "site": "0058ffe4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0058ffe0",
      "incomplete_value": false,
      "site": "0058ffe4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590070",
      "incomplete_value": false,
      "site": "00590070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590070",
      "incomplete_value": false,
      "site": "00590070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "0058ffe4",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "00590070",
      "DATA",
      [
        "storage",
        "00bf33c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005900e4",
      "READ",
      [
        "storage",
        "00bf33f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ffe4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "00590070",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "undefined *"
      ]
    ],
    [
      "005900e4",
      "READ",
      [
        "storage",
        "00bf34a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ffd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md#insn-0058ffd8) · [`00590068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md#insn-00590068)
- 新版 [`0058ffd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md#insn-0058ffd8) · [`00590068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md#insn-00590068)

~~~diff
- 0058ffd8 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0058ffd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ffd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ffd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ffd8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0058ffd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ffd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ffd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ffd8 bytes 08412591
+ 0058ffd8 bytes 08012891
- 00590068 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 00590068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590068 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00590068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590068 bytes 08210f91
+ 00590068 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26623d70572869051d17f9ca1662cfb"></a>

### [`005902dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md) → [`005902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md) FUN_005902dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008740c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740c4.md) · 呼出先 6件 [`00590428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md) [`005929a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005929a0.md) [`005929a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005929a4.md) [`00592acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592acc.md) [`00592ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ad0.md)
- 新版 呼出元 1件 [`008740c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md) · 呼出先 6件 [`00590428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md) [`005929a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005929a0.md) [`005929a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005929a4.md) [`00592acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592acc.md) [`00592ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ad0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00590304",
      "incomplete_value": true,
      "site": "00590304",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590304",
      "incomplete_value": true,
      "site": "00590304",
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
            "const:f98:8"
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
      "definition_site": "00590318",
      "incomplete_value": false,
      "site": "00590318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590318",
      "incomplete_value": false,
      "site": "00590318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00590304",
      "DATA",
      [
        "storage",
        "00bf2f98",
        null,
        "undefined *"
      ]
    ],
    [
      "00590318",
      "DATA",
      [
        "storage",
        "00bf3018",
        null,
        "undefined *"
      ]
    ],
    [
      "00590350",
      "READ",
      [
        "storage",
        "00bf3038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00590304",
      "DATA",
      [
        "storage",
        "00bf3048",
        null,
        "undefined *"
      ]
    ],
    [
      "00590318",
      "DATA",
      [
        "storage",
        "00bf30c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00590350",
      "READ",
      [
        "storage",
        "00bf30e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005902fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md#insn-005902fc) · [`00590300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md#insn-00590300) · [`00590314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md#insn-00590314)
- 新版 [`005902fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md#insn-005902fc) · [`00590300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md#insn-00590300) · [`00590314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md#insn-00590314)

~~~diff
- 005902fc ["COPY", "register:4040:8", ["const:bf2000:8"]]
+ 005902fc ["COPY", "register:4040:8", ["const:bf3000:8"]]
- 005902fc bytes 083300d0
+ 005902fc bytes 083300f0
- 00590300 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00590300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590300 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00590300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590300 bytes 08613e91
+ 00590300 bytes 08210191
- 00590314 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00590314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590314 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00590314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590314 bytes 08610091
+ 00590314 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22bf98ee268e8f6489add6a756ee77cb"></a>

### [`00590428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md) → [`00590428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md) FUN_00590428

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005902dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00578/00578ff0.md) [`00594944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594944.md) [`00594c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594c90.md)
- 新版 呼出元 1件 [`005902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md) [`00594944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594944.md) [`00594c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594c90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005904ac",
      "incomplete_value": false,
      "site": "005904b0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "005904ac",
      "incomplete_value": false,
      "site": "005904b0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059053c",
      "incomplete_value": false,
      "site": "0059053c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059053c",
      "incomplete_value": false,
      "site": "0059053c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00590480",
      "DATA",
      [
        "storage",
        "00bf11a8",
        null,
        "undefined *"
      ]
    ],
    [
      "005904b0",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0059053c",
      "DATA",
      [
        "storage",
        "00bf3448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590480",
      "DATA",
      [
        "storage",
        "00bf1258",
        null,
        "undefined *"
      ]
    ],
    [
      "005904b0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0059053c",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md#insn-00590474) · [`005904a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md#insn-005904a4) · [`00590534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md#insn-00590534)
- 新版 [`00590474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md#insn-00590474) · [`005904a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md#insn-005904a4) · [`00590534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md#insn-00590534)

~~~diff
- 00590474 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00590474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590474 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 00590474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590474 bytes 08610691
+ 00590474 bytes 08210991
- 005904a4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 005904a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005904a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005904a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005904a4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005904a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005904a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005904a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005904a4 bytes 08412591
+ 005904a4 bytes 08012891
- 00590534 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00590534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590534 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00590534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590534 bytes 08211191
+ 00590534 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3ba5991b76fd5b81449770fbf303c4"></a>

### [`00590780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590780.md) → [`00590780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590780.md) FUN_00590780

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "005907a4",
      "incomplete_value": false,
      "site": "005907a8",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "005907a4",
      "incomplete_value": false,
      "site": "005907a8",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "005907a8",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005907a8",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059079c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590780.md#insn-0059079c)
- 新版 [`0059079c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590780.md#insn-0059079c)

~~~diff
- 0059079c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059079c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059079c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059079c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059079c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059079c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059079c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059079c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059079c bytes 08412591
+ 0059079c bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25cbf88937e676f130b0b615963f9965"></a>

### [`00590930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590930.md) → [`00590930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590930.md) FUN_00590930

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590964",
      "incomplete_value": false,
      "site": "00590968",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "00590964",
      "incomplete_value": false,
      "site": "00590968",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00590968",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590968",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059095c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590930.md#insn-0059095c)
- 新版 [`0059095c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590930.md#insn-0059095c)

~~~diff
- 0059095c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059095c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059095c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059095c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059095c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059095c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059095c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059095c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059095c bytes 08412591
+ 0059095c bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-387fd1421d4b78da1f5a84c6caf17d33"></a>

### [`005909a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005909a4.md) → [`005909a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005909a4.md) FUN_005909a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005909d8",
      "incomplete_value": false,
      "site": "005909dc",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "005909d8",
      "incomplete_value": false,
      "site": "005909dc",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "005909dc",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005909dc",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005909d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005909a4.md#insn-005909d0)
- 新版 [`005909d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005909a4.md#insn-005909d0)

~~~diff
- 005909d0 ["COPY", "tmp:0:8", ["const:950:8"]]
- 005909d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005909d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005909d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005909d0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005909d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005909d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005909d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005909d0 bytes 08412591
+ 005909d0 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a03ac0b660e51ab6c005bfa387ffec7"></a>

### [`00590a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590a18.md) → [`00590a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590a18.md) FUN_00590a18

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590a4c",
      "incomplete_value": false,
      "site": "00590a50",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "00590a4c",
      "incomplete_value": false,
      "site": "00590a50",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00590a50",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590a50",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590a18.md#insn-00590a44)
- 新版 [`00590a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590a18.md#insn-00590a44)

~~~diff
- 00590a44 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00590a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590a44 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00590a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590a44 bytes 08412591
+ 00590a44 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec9dbd9118f4a517b6c5321b787ce4b"></a>

### [`00590a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590a8c.md) → [`00590a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590a8c.md) FUN_00590a8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590ac0",
      "incomplete_value": false,
      "site": "00590ac4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "00590ac0",
      "incomplete_value": false,
      "site": "00590ac4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00590ac4",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590ac4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590a8c.md#insn-00590ab8)
- 新版 [`00590ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590a8c.md#insn-00590ab8)

~~~diff
- 00590ab8 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00590ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590ab8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00590ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590ab8 bytes 08412591
+ 00590ab8 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b2a0235048ac4b4715a8cf45524fb3"></a>

### [`00590b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590b00.md) → [`00590b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590b00.md) FUN_00590b00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00590b24",
      "incomplete_value": false,
      "site": "00590b28",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "00590b24",
      "incomplete_value": false,
      "site": "00590b28",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00590b28",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590b28",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590b00.md#insn-00590b1c)
- 新版 [`00590b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590b00.md#insn-00590b1c)

~~~diff
- 00590b1c ["COPY", "tmp:0:8", ["const:950:8"]]
- 00590b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590b1c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00590b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590b1c bytes 08412591
+ 00590b1c bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2afb90c56e95e6b040efb4a075df0299"></a>

### [`00590b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590b64.md) → [`00590b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590b64.md) FUN_00590b64

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
      "definition_site": "00590b68",
      "incomplete_value": false,
      "site": "00590b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590b68",
      "incomplete_value": false,
      "site": "00590b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "00590b6c",
      "DATA",
      [
        "storage",
        "00bf2138",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00590b6c",
      "DATA",
      [
        "storage",
        "00bf21e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590b64.md#insn-00590b68)
- 新版 [`00590b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590b64.md#insn-00590b68)

~~~diff
- 00590b68 ["COPY", "tmp:0:8", ["const:138:8"]]
- 00590b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590b68 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00590b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590b68 bytes 08e10491
+ 00590b68 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa63593b93dcb41c3473a52d01acd83"></a>

### [`00590cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590cc8.md) → [`00590cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590cc8.md) FUN_00590cc8

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
      "definition_site": "00590cd4",
      "incomplete_value": false,
      "site": "00590cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590cd4",
      "incomplete_value": false,
      "site": "00590cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00590cd4",
      "DATA",
      [
        "storage",
        "00bf2188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590cd4",
      "DATA",
      [
        "storage",
        "00bf2238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590cc8.md#insn-00590cd0)
- 新版 [`00590cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590cc8.md#insn-00590cd0)

~~~diff
- 00590cd0 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00590cd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590cd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590cd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590cd0 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 00590cd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590cd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590cd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590cd0 bytes 29210691
+ 00590cd0 bytes 29e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55a66ca9fceca5171472f4ec5a61a301"></a>

### [`00590d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590d18.md) → [`00590d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d18.md) FUN_00590d18

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
      "definition_site": "00590d3c",
      "incomplete_value": false,
      "site": "00590d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590d3c",
      "incomplete_value": false,
      "site": "00590d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "00590d3c",
      "DATA",
      [
        "storage",
        "00bf2218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590d3c",
      "DATA",
      [
        "storage",
        "00bf22c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590d18.md#insn-00590d38)
- 新版 [`00590d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d18.md#insn-00590d38)

~~~diff
- 00590d38 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00590d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00590d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590d38 bytes 08610891
+ 00590d38 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aadc9837c9fd8bf9cf39c7c33c78ab1d"></a>

### [`00590d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590d4c.md) → [`00590d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d4c.md) FUN_00590d4c

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
      "definition_site": "00590d58",
      "incomplete_value": false,
      "site": "00590d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590d58",
      "incomplete_value": false,
      "site": "00590d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "00590d58",
      "DATA",
      [
        "storage",
        "00bf2218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590d58",
      "DATA",
      [
        "storage",
        "00bf22c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590d4c.md#insn-00590d54)
- 新版 [`00590d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590d4c.md#insn-00590d54)

~~~diff
- 00590d54 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00590d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00590d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590d54 bytes 29610891
+ 00590d54 bytes 29210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a05d8efbe0a8638c4cae913bfe73e57"></a>

### [`00590dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590dc4.md) → [`00590dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590dc4.md) FUN_00590dc4

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
      "definition_site": "00590dcc",
      "incomplete_value": false,
      "site": "00590dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590dcc",
      "incomplete_value": false,
      "site": "00590dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00590dd0",
      "DATA",
      [
        "storage",
        "00bf22a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590dd0",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590dc4.md#insn-00590dcc)
- 新版 [`00590dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590dc4.md#insn-00590dcc)

~~~diff
- 00590dcc ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00590dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00590dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590dcc bytes 29a10a91
+ 00590dcc bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f865f539b5ecee387f0de7bf2b74f0bc"></a>

### [`00590de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590de4.md) → [`00590de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590de4.md) FUN_00590de4

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
      "definition_site": "00590dec",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590dec",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00590df0",
      "DATA",
      [
        "storage",
        "00bf22a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590df0",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590de4.md#insn-00590dec)
- 新版 [`00590dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590de4.md#insn-00590dec)

~~~diff
- 00590dec ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00590dec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590dec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590dec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00590dec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590dec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590dec bytes 29a10a91
+ 00590dec bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f1c4cfd7ec3089f328052266ed3154"></a>

### [`00590e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590e24.md) → [`00590e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590e24.md) FUN_00590e24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590e54",
      "incomplete_value": false,
      "site": "00590e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e54",
      "incomplete_value": false,
      "site": "00590e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00590e54",
      "DATA",
      [
        "storage",
        "00bf22a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590e54",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590e24.md#insn-00590e48)
- 新版 [`00590e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590e24.md#insn-00590e48)

~~~diff
- 00590e48 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00590e48 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00590e48 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00590e48 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00590e48 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00590e48 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00590e48 bytes 6ba10a91
+ 00590e48 bytes 6b610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5d16b6fd0b544cef976ce98c75ee47"></a>

### [`00590ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590ea0.md) → [`00590ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ea0.md) FUN_00590ea0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "00590eac",
      "incomplete_value": false,
      "site": "00590eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590eac",
      "incomplete_value": false,
      "site": "00590eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00590eac",
      "DATA",
      [
        "storage",
        "00bf22a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590eac",
      "DATA",
      [
        "storage",
        "00bf2358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590ea0.md#insn-00590ea8)
- 新版 [`00590ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ea0.md#insn-00590ea8)

~~~diff
- 00590ea8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00590ea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00590ea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590ea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590ea8 bytes 29a10a91
+ 00590ea8 bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-842ab47006e5d444d8763d8a18abeaa4"></a>

### [`00590f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590f64.md) → [`00590f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f64.md) FUN_00590f64

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
      "definition_site": "00590f88",
      "incomplete_value": false,
      "site": "00590f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590f88",
      "incomplete_value": false,
      "site": "00590f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "00590f88",
      "DATA",
      [
        "storage",
        "00bf2338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590f88",
      "DATA",
      [
        "storage",
        "00bf23e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590f64.md#insn-00590f84)
- 新版 [`00590f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f64.md#insn-00590f84)

~~~diff
- 00590f84 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00590f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00590f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590f84 bytes 08e10c91
+ 00590f84 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adddf2d3ac1679fe4b536194e29c65ad"></a>

### [`00590f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590f98.md) → [`00590f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f98.md) FUN_00590f98

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
      "definition_site": "00590fa4",
      "incomplete_value": false,
      "site": "00590fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590fa4",
      "incomplete_value": false,
      "site": "00590fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "00590fa4",
      "DATA",
      [
        "storage",
        "00bf2338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00590fa4",
      "DATA",
      [
        "storage",
        "00bf23e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590f98.md#insn-00590fa0)
- 新版 [`00590fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590f98.md#insn-00590fa0)

~~~diff
- 00590fa0 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00590fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00590fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590fa0 bytes 29e10c91
+ 00590fa0 bytes 29a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25dfed08156f7d0a4fde5dc0e7182776"></a>

### [`0059101c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059101c.md) → [`0059101c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059101c.md) FUN_0059101c

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
      "definition_site": "00591040",
      "incomplete_value": false,
      "site": "00591040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591040",
      "incomplete_value": false,
      "site": "00591040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "00591040",
      "DATA",
      [
        "storage",
        "00bf23b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591040",
      "DATA",
      [
        "storage",
        "00bf2468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059103c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059101c.md#insn-0059103c)
- 新版 [`0059103c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059101c.md#insn-0059103c)

~~~diff
- 0059103c ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0059103c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059103c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059103c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0059103c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059103c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059103c bytes 08e10e91
+ 0059103c bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb46475abd0d4cc94da1f50b9e14a946"></a>

### [`00591050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591050.md) → [`00591050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591050.md) FUN_00591050

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
      "definition_site": "0059105c",
      "incomplete_value": false,
      "site": "0059105c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059105c",
      "incomplete_value": false,
      "site": "0059105c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "0059105c",
      "DATA",
      [
        "storage",
        "00bf23b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059105c",
      "DATA",
      [
        "storage",
        "00bf2468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591050.md#insn-00591058)
- 新版 [`00591058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591050.md#insn-00591058)

~~~diff
- 00591058 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 00591058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00591058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591058 bytes 29e10e91
+ 00591058 bytes 29a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-640e42ef14b1580f1a21152eb1c61db6"></a>

### [`005910a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005910a0.md) → [`005910a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910a0.md) FUN_005910a0

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
      "definition_site": "005910c4",
      "incomplete_value": false,
      "site": "005910c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005910c4",
      "incomplete_value": false,
      "site": "005910c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "005910c4",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005910c4",
      "DATA",
      [
        "storage",
        "00bf24e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005910c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005910a0.md#insn-005910c0)
- 新版 [`005910c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910a0.md#insn-005910c0)

~~~diff
- 005910c0 ["COPY", "tmp:0:8", ["const:438:8"]]
- 005910c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005910c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005910c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 005910c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005910c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005910c0 bytes 08e11091
+ 005910c0 bytes 08a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae2c6a89aae475c8a173098009bf859"></a>

### [`005910d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005910d4.md) → [`005910d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910d4.md) FUN_005910d4

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
      "definition_site": "005910e0",
      "incomplete_value": false,
      "site": "005910e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005910e0",
      "incomplete_value": false,
      "site": "005910e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "005910e0",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005910e0",
      "DATA",
      [
        "storage",
        "00bf24e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005910dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005910d4.md#insn-005910dc)
- 新版 [`005910dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005910d4.md#insn-005910dc)

~~~diff
- 005910dc ["COPY", "tmp:0:8", ["const:438:8"]]
- 005910dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005910dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005910dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 005910dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005910dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005910dc bytes 29e11091
+ 005910dc bytes 29a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-786bfe5000140ac782c217bf8fc265fe"></a>

### [`00591154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591154.md) → [`00591154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591154.md) FUN_00591154

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
      "definition_site": "00591178",
      "incomplete_value": false,
      "site": "00591178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591178",
      "incomplete_value": false,
      "site": "00591178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "00591178",
      "DATA",
      [
        "storage",
        "00bf24b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591178",
      "DATA",
      [
        "storage",
        "00bf2568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591154.md#insn-00591174)
- 新版 [`00591174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591154.md#insn-00591174)

~~~diff
- 00591174 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00591174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00591174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591174 bytes 08e11291
+ 00591174 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5552b27fe91b305859e033f396d8ecd3"></a>

### [`00591188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591188.md) → [`00591188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591188.md) FUN_00591188

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
      "definition_site": "00591194",
      "incomplete_value": false,
      "site": "00591194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591194",
      "incomplete_value": false,
      "site": "00591194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "00591194",
      "DATA",
      [
        "storage",
        "00bf24b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591194",
      "DATA",
      [
        "storage",
        "00bf2568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591188.md#insn-00591190)
- 新版 [`00591190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591188.md#insn-00591190)

~~~diff
- 00591190 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00591190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00591190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591190 bytes 29e11291
+ 00591190 bytes 29a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c9fb673f675c7507556e3e8edc9a75"></a>

### [`005911a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005911a4.md) → [`005911a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md) FUN_005911a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`00591404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591404.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`00591404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591404.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591220",
      "incomplete_value": false,
      "site": "00591228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591220",
      "incomplete_value": false,
      "site": "00591228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "00591228",
      "DATA",
      [
        "storage",
        "00bf2528",
        null,
        "pointer"
      ]
    ],
    [
      "005912c0",
      "READ",
      [
        "storage",
        "00bf2538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591228",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ],
    [
      "005912c0",
      "READ",
      [
        "storage",
        "00bf25e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005911a4.md#insn-00591220) · [`00591224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005911a4.md#insn-00591224)
- 新版 [`00591220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md#insn-00591220) · [`00591224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005911a4.md#insn-00591224)

~~~diff
- 00591220 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00591220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00591220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591220 bytes 08a11491
+ 00591220 bytes 08611791
- 00591224 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00591224 bytes f30300aa
+ 00591224 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00591224 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d281e9a7b82abdf6d00cfd7c95c2123e"></a>

### [`005913c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005913c4.md) → [`005913c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913c4.md) FUN_005913c4

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
      "definition_site": "005913c8",
      "incomplete_value": false,
      "site": "005913cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913c8",
      "incomplete_value": false,
      "site": "005913cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "005913cc",
      "DATA",
      [
        "storage",
        "00bf2528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005913cc",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005913c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005913c4.md#insn-005913c8)
- 新版 [`005913c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913c4.md#insn-005913c8)

~~~diff
- 005913c8 ["COPY", "tmp:0:8", ["const:528:8"]]
- 005913c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005913c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005913c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 005913c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005913c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005913c8 bytes 08a11491
+ 005913c8 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9673d4aec4c2edb157eb10f6438fbe00"></a>

### [`005913d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005913d4.md) → [`005913d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913d4.md) FUN_005913d4

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
      "definition_site": "005913e4",
      "incomplete_value": false,
      "site": "005913ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913e4",
      "incomplete_value": false,
      "site": "005913ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "005913ec",
      "DATA",
      [
        "storage",
        "00bf2528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005913ec",
      "DATA",
      [
        "storage",
        "00bf25d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005913e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005913d4.md#insn-005913e4)
- 新版 [`005913e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005913d4.md#insn-005913e4)

~~~diff
- 005913e4 ["COPY", "tmp:0:8", ["const:528:8"]]
- 005913e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005913e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005913e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 005913e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005913e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005913e4 bytes 08a11491
+ 005913e4 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d493aa9e7cc60093003bdc9a0cfe520"></a>

### [`00591420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591420.md) → [`00591420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591420.md) FUN_00591420

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
      "definition_site": "00591444",
      "incomplete_value": false,
      "site": "00591444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591444",
      "incomplete_value": false,
      "site": "00591444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00591444",
      "DATA",
      [
        "storage",
        "00bf2588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591444",
      "DATA",
      [
        "storage",
        "00bf2638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591420.md#insn-00591440)
- 新版 [`00591440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591420.md#insn-00591440)

~~~diff
- 00591440 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00591440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 00591440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591440 bytes 08211691
+ 00591440 bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24929e059e501a0fb06e99f1e8ea2fb"></a>

### [`00591454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591454.md) → [`00591454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591454.md) FUN_00591454

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
      "definition_site": "00591460",
      "incomplete_value": false,
      "site": "00591460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591460",
      "incomplete_value": false,
      "site": "00591460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00591460",
      "DATA",
      [
        "storage",
        "00bf2588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591460",
      "DATA",
      [
        "storage",
        "00bf2638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059145c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591454.md#insn-0059145c)
- 新版 [`0059145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591454.md#insn-0059145c)

~~~diff
- 0059145c ["COPY", "tmp:0:8", ["const:588:8"]]
- 0059145c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059145c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059145c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 0059145c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059145c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059145c bytes 29211691
+ 0059145c bytes 29e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5066d207ea119ca229d811597fa211d"></a>

### [`005914e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005914e4.md) → [`005914e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005914e4.md) FUN_005914e4

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
      "definition_site": "00591504",
      "incomplete_value": false,
      "site": "00591508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591504",
      "incomplete_value": false,
      "site": "00591508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "00591508",
      "DATA",
      [
        "storage",
        "00bf2618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591508",
      "DATA",
      [
        "storage",
        "00bf26c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005914e4.md#insn-00591504)
- 新版 [`00591504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005914e4.md#insn-00591504)

~~~diff
- 00591504 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00591504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00591504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591504 bytes 08611891
+ 00591504 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c8c5e0328165008bfafafe55ef11da4"></a>

### [`0059151c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059151c.md) → [`0059151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059151c.md) FUN_0059151c

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
      "definition_site": "00591520",
      "incomplete_value": false,
      "site": "00591524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591520",
      "incomplete_value": false,
      "site": "00591524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "00591524",
      "DATA",
      [
        "storage",
        "00bf2618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591524",
      "DATA",
      [
        "storage",
        "00bf26c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059151c.md#insn-00591520)
- 新版 [`00591520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059151c.md#insn-00591520)

~~~diff
- 00591520 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00591520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00591520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591520 bytes 08611891
+ 00591520 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6d8108980ea8312a7d3e0baefd0bf4f"></a>

### [`0059158c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059158c.md) → [`0059158c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059158c.md) FUN_0059158c

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
      "definition_site": "005915b0",
      "incomplete_value": false,
      "site": "005915b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005915b0",
      "incomplete_value": false,
      "site": "005915b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "005915b0",
      "DATA",
      [
        "storage",
        "00bf2698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005915b0",
      "DATA",
      [
        "storage",
        "00bf2748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005915ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059158c.md#insn-005915ac)
- 新版 [`005915ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059158c.md#insn-005915ac)

~~~diff
- 005915ac ["COPY", "tmp:0:8", ["const:698:8"]]
- 005915ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005915ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005915ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["COPY", "tmp:0:8", ["const:748:8"]]
+ 005915ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005915ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005915ac bytes 08611a91
+ 005915ac bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c063920dedb8e4f3ea2abcffbf235dec"></a>

### [`005915c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005915c0.md) → [`005915c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005915c0.md) FUN_005915c0

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
      "definition_site": "005915cc",
      "incomplete_value": false,
      "site": "005915cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005915cc",
      "incomplete_value": false,
      "site": "005915cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "005915cc",
      "DATA",
      [
        "storage",
        "00bf2698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005915cc",
      "DATA",
      [
        "storage",
        "00bf2748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005915c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005915c0.md#insn-005915c8)
- 新版 [`005915c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005915c0.md#insn-005915c8)

~~~diff
- 005915c8 ["COPY", "tmp:0:8", ["const:698:8"]]
- 005915c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005915c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005915c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 005915c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005915c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005915c8 bytes 29611a91
+ 005915c8 bytes 29211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f87c49e1f0f80a55a637e42b0eaca17"></a>

### [`00591620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591620.md) → [`00591620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591620.md) FUN_00591620

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
      "definition_site": "00591644",
      "incomplete_value": false,
      "site": "00591644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591644",
      "incomplete_value": false,
      "site": "00591644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00591644",
      "DATA",
      [
        "storage",
        "00bf2718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591644",
      "DATA",
      [
        "storage",
        "00bf27c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591620.md#insn-00591640)
- 新版 [`00591640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591620.md#insn-00591640)

~~~diff
- 00591640 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00591640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00591640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591640 bytes 08611c91
+ 00591640 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f502dd600f5e6868906d3d4c6bbbffd"></a>

### [`00591654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591654.md) → [`00591654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591654.md) FUN_00591654

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
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00591660",
      "DATA",
      [
        "storage",
        "00bf2718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591660",
      "DATA",
      [
        "storage",
        "00bf27c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059165c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591654.md#insn-0059165c)
- 新版 [`0059165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591654.md#insn-0059165c)

~~~diff
- 0059165c ["COPY", "tmp:0:8", ["const:718:8"]]
- 0059165c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059165c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059165c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 0059165c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059165c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059165c bytes 29611c91
+ 0059165c bytes 29211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a020a80e2f444bd69bcd552d4cbdc6c"></a>

### [`0059177c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059177c.md) → [`0059177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059177c.md) FUN_0059177c

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
      "definition_site": "00591788",
      "incomplete_value": false,
      "site": "00591788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591788",
      "incomplete_value": false,
      "site": "00591788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00591788",
      "DATA",
      [
        "storage",
        "00bf2798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591788",
      "DATA",
      [
        "storage",
        "00bf2848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059177c.md#insn-00591784)
- 新版 [`00591784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059177c.md#insn-00591784)

~~~diff
- 00591784 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00591784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00591784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591784 bytes 29611e91
+ 00591784 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb565efa1c307030cea350bad718412f"></a>

### [`005917e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005917e0.md) → [`005917e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005917e0.md) FUN_005917e0

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
      "definition_site": "00591800",
      "incomplete_value": false,
      "site": "00591804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591800",
      "incomplete_value": false,
      "site": "00591804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "00591804",
      "DATA",
      [
        "storage",
        "00bf2818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591804",
      "DATA",
      [
        "storage",
        "00bf28c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/005917e0.md#insn-00591800)
- 新版 [`00591800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/005917e0.md#insn-00591800)

~~~diff
- 00591800 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00591800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00591800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591800 bytes 08612091
+ 00591800 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67397b5ce027633b64c0aa269eebf9b2"></a>

### [`00591818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591818.md) → [`00591818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591818.md) FUN_00591818

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059181c",
      "incomplete_value": true,
      "site": "00591820",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059181c",
      "incomplete_value": true,
      "site": "00591820",
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
      "00591820",
      "DATA",
      [
        "storage",
        "00bf2818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591820",
      "DATA",
      [
        "storage",
        "00bf28c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059181c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591818.md#insn-0059181c)
- 新版 [`0059181c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591818.md#insn-0059181c)

~~~diff
- 0059181c ["COPY", "tmp:0:8", ["const:818:8"]]
- 0059181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 0059181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059181c bytes 08612091
+ 0059181c bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-043275de9487f35b97912a51aaf01488"></a>

### [`00591934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591934.md) → [`00591934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591934.md) FUN_00591934

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
      "definition_site": "00591954",
      "incomplete_value": false,
      "site": "00591958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591954",
      "incomplete_value": false,
      "site": "00591958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "00591958",
      "DATA",
      [
        "storage",
        "00bf28a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591958",
      "DATA",
      [
        "storage",
        "00bf2958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591934.md#insn-00591954)
- 新版 [`00591954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591934.md#insn-00591954)

~~~diff
- 00591954 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00591954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00591954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591954 bytes 08a12291
+ 00591954 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-529fea07c7be034e27131244a285b85e"></a>

### [`0059196c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059196c.md) → [`0059196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059196c.md) FUN_0059196c

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
      "definition_site": "00591970",
      "incomplete_value": false,
      "site": "00591974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591970",
      "incomplete_value": false,
      "site": "00591974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "00591974",
      "DATA",
      [
        "storage",
        "00bf28a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591974",
      "DATA",
      [
        "storage",
        "00bf2958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/0059196c.md#insn-00591970)
- 新版 [`00591970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/0059196c.md#insn-00591970)

~~~diff
- 00591970 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00591970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00591970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591970 bytes 08a12291
+ 00591970 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe3ecc2070dd95849067f68ff3c622a"></a>

### [`00591a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591a9c.md) → [`00591a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591a9c.md) FUN_00591a9c

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
      "definition_site": "00591abc",
      "incomplete_value": false,
      "site": "00591ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591abc",
      "incomplete_value": false,
      "site": "00591ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "00591ac0",
      "DATA",
      [
        "storage",
        "00bf2938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591ac0",
      "DATA",
      [
        "storage",
        "00bf29e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591a9c.md#insn-00591abc)
- 新版 [`00591abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591a9c.md#insn-00591abc)

~~~diff
- 00591abc ["COPY", "tmp:0:8", ["const:938:8"]]
- 00591abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00591abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591abc bytes 08e12491
+ 00591abc bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245655e90e3f7f81e31283854b9759ab"></a>

### [`00591ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591ad4.md) → [`00591ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ad4.md) FUN_00591ad4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00591ad8",
      "incomplete_value": true,
      "site": "00591adc",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ad8",
      "incomplete_value": true,
      "site": "00591adc",
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
            "const:938:8"
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
      "00591adc",
      "DATA",
      [
        "storage",
        "00bf2938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591adc",
      "DATA",
      [
        "storage",
        "00bf29e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591ad4.md#insn-00591ad8)
- 新版 [`00591ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ad4.md#insn-00591ad8)

~~~diff
- 00591ad8 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00591ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00591ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591ad8 bytes 08e12491
+ 00591ad8 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc63ecffddbf8d85cae05b810dbc74ac"></a>

### [`00591b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591b34.md) → [`00591b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b34.md) FUN_00591b34

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
      "definition_site": "00591b58",
      "incomplete_value": false,
      "site": "00591b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591b58",
      "incomplete_value": false,
      "site": "00591b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00591b58",
      "DATA",
      [
        "storage",
        "00bf29b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591b58",
      "DATA",
      [
        "storage",
        "00bf2a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591b34.md#insn-00591b54)
- 新版 [`00591b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b34.md#insn-00591b54)

~~~diff
- 00591b54 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00591b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00591b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591b54 bytes 08e12691
+ 00591b54 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2222a25b4912f05c8f0929517cfa57de"></a>

### [`00591b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591b68.md) → [`00591b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b68.md) FUN_00591b68

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
      "definition_site": "00591b74",
      "incomplete_value": false,
      "site": "00591b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591b74",
      "incomplete_value": false,
      "site": "00591b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00591b74",
      "DATA",
      [
        "storage",
        "00bf29b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591b74",
      "DATA",
      [
        "storage",
        "00bf2a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591b68.md#insn-00591b70)
- 新版 [`00591b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591b68.md#insn-00591b70)

~~~diff
- 00591b70 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00591b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00591b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591b70 bytes 29e12691
+ 00591b70 bytes 29a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a15fd7d3173d0c44e294eb59ef63f242"></a>

### [`00591be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591be8.md) → [`00591be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591be8.md) FUN_00591be8

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
      "definition_site": "00591c0c",
      "incomplete_value": false,
      "site": "00591c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591c0c",
      "incomplete_value": false,
      "site": "00591c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "00591c0c",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591c0c",
      "DATA",
      [
        "storage",
        "00bf2ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591be8.md#insn-00591c08)
- 新版 [`00591c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591be8.md#insn-00591c08)

~~~diff
- 00591c08 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00591c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00591c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591c08 bytes 08e12891
+ 00591c08 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5fedb707563659ce5d6251583b17a0"></a>

### [`00591c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591c1c.md) → [`00591c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c1c.md) FUN_00591c1c

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
      "definition_site": "00591c28",
      "incomplete_value": false,
      "site": "00591c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591c28",
      "incomplete_value": false,
      "site": "00591c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "00591c28",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591c28",
      "DATA",
      [
        "storage",
        "00bf2ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591c1c.md#insn-00591c24)
- 新版 [`00591c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591c1c.md#insn-00591c24)

~~~diff
- 00591c24 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00591c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00591c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591c24 bytes 29e12891
+ 00591c24 bytes 29a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd03f8a2197a47046b460504d8d789f9"></a>

### [`00591d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d10.md) → [`00591d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d10.md) FUN_00591d10

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
      "definition_site": "00591d34",
      "incomplete_value": false,
      "site": "00591d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d34",
      "incomplete_value": false,
      "site": "00591d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "00591d34",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591d34",
      "DATA",
      [
        "storage",
        "00bf2b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d10.md#insn-00591d30)
- 新版 [`00591d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d10.md#insn-00591d30)

~~~diff
- 00591d30 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00591d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00591d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591d30 bytes 08e12a91
+ 00591d30 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e467b2b6e9abf8702919aba6a0b0556"></a>

### [`00591d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d44.md) → [`00591d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d44.md) FUN_00591d44

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
      "definition_site": "00591d50",
      "incomplete_value": false,
      "site": "00591d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d50",
      "incomplete_value": false,
      "site": "00591d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "00591d50",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591d50",
      "DATA",
      [
        "storage",
        "00bf2b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591d44.md#insn-00591d4c)
- 新版 [`00591d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591d44.md#insn-00591d4c)

~~~diff
- 00591d4c ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00591d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00591d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591d4c bytes 29e12a91
+ 00591d4c bytes 29a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5480950204464525eabd2458a99747c2"></a>

### [`00591da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591da8.md) → [`00591da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591da8.md) FUN_00591da8

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
      "definition_site": "00591dcc",
      "incomplete_value": false,
      "site": "00591dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591dcc",
      "incomplete_value": false,
      "site": "00591dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00591dcc",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591dcc",
      "DATA",
      [
        "storage",
        "00bf2be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591da8.md#insn-00591dc8)
- 新版 [`00591dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591da8.md#insn-00591dc8)

~~~diff
- 00591dc8 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00591dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00591dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591dc8 bytes 08e12c91
+ 00591dc8 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-594de46fd23ae0525c9dc376da5a0aad"></a>

### [`00591ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591ddc.md) → [`00591ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ddc.md) FUN_00591ddc

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
      "definition_site": "00591de8",
      "incomplete_value": true,
      "site": "00591de8",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591de8",
      "incomplete_value": true,
      "site": "00591de8",
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
            "const:b38:8"
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
      "00591de8",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591de8",
      "DATA",
      [
        "storage",
        "00bf2be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591ddc.md#insn-00591de4)
- 新版 [`00591de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591ddc.md#insn-00591de4)

~~~diff
- 00591de4 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00591de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00591de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591de4 bytes 29e12c91
+ 00591de4 bytes 29a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecca5341d7294572aefd3591bccf1f19"></a>

### [`00591df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591df8.md) → [`00591df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df8.md) FUN_00591df8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0051c140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c140.md) [`0059201c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059201c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md) [`0059201c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059201c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00591e8c",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "pointer"
      ]
    ],
    [
      "00591ef0",
      "READ",
      [
        "storage",
        "00bf2bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591e8c",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ],
    [
      "00591ef0",
      "READ",
      [
        "storage",
        "00bf2c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591df8.md#insn-00591e74)
- 新版 [`00591e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591df8.md#insn-00591e74)

~~~diff
- 00591e74 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00591e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00591e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00591e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00591e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00591e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00591e74 bytes 29e12e91
+ 00591e74 bytes 29a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff637e97ae613fee574ab3fd0e222b3"></a>

### [`00591fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591fdc.md) → [`00591fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fdc.md) FUN_00591fdc

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
      "definition_site": "00591fe0",
      "incomplete_value": false,
      "site": "00591fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591fe0",
      "incomplete_value": false,
      "site": "00591fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00591fe4",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00591fe4",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591fdc.md#insn-00591fe0)
- 新版 [`00591fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fdc.md#insn-00591fe0)

~~~diff
- 00591fe0 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00591fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00591fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591fe0 bytes 08e12e91
+ 00591fe0 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c38d82373fe5de48a6d17571aa4a628"></a>

### [`00591fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591fec.md) → [`00591fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fec.md) FUN_00591fec

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
      "definition_site": "00591ffc",
      "incomplete_value": false,
      "site": "00592004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ffc",
      "incomplete_value": false,
      "site": "00592004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00592004",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592004",
      "DATA",
      [
        "storage",
        "00bf2c68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00591/00591fec.md#insn-00591ffc)
- 新版 [`00591ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00591/00591fec.md#insn-00591ffc)

~~~diff
- 00591ffc ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00591ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00591ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591ffc bytes 08e12e91
+ 00591ffc bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-161c2ae5d90b3756eebcf2d8da3c6887"></a>

### [`005920d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005920d4.md) → [`005920d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920d4.md) FUN_005920d4

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
      "definition_site": "005920e0",
      "incomplete_value": false,
      "site": "005920e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920e0",
      "incomplete_value": false,
      "site": "005920e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "005920e0",
      "DATA",
      [
        "storage",
        "00bf2c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005920e0",
      "DATA",
      [
        "storage",
        "00bf2cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005920dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005920d4.md#insn-005920dc)
- 新版 [`005920dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005920d4.md#insn-005920dc)

~~~diff
- 005920dc ["COPY", "tmp:0:8", ["const:c18:8"]]
- 005920dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005920dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005920dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 005920dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005920dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005920dc bytes 29613091
+ 005920dc bytes 29213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200205bd6867617d316e60ba3093dcb0"></a>

### [`00592138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592138.md) → [`00592138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592138.md) FUN_00592138

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
      "definition_site": "0059215c",
      "incomplete_value": false,
      "site": "0059215c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059215c",
      "incomplete_value": false,
      "site": "0059215c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "0059215c",
      "DATA",
      [
        "storage",
        "00bf2c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059215c",
      "DATA",
      [
        "storage",
        "00bf2d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592138.md#insn-00592158)
- 新版 [`00592158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592138.md#insn-00592158)

~~~diff
- 00592158 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00592158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00592158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592158 bytes 08613291
+ 00592158 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f496e3922f0dea86bd1097da7e19b5d"></a>

### [`0059216c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059216c.md) → [`0059216c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059216c.md) FUN_0059216c

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
      "definition_site": "00592178",
      "incomplete_value": false,
      "site": "00592178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592178",
      "incomplete_value": false,
      "site": "00592178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "00592178",
      "DATA",
      [
        "storage",
        "00bf2c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592178",
      "DATA",
      [
        "storage",
        "00bf2d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059216c.md#insn-00592174)
- 新版 [`00592174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059216c.md#insn-00592174)

~~~diff
- 00592174 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00592174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00592174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592174 bytes 29613291
+ 00592174 bytes 29213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df09e96efeed1132fa5989eca2a2ee53"></a>

### [`005921c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005921c0.md) → [`005921c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921c0.md) FUN_005921c0

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
      "definition_site": "005921e4",
      "incomplete_value": false,
      "site": "005921e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005921e4",
      "incomplete_value": false,
      "site": "005921e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "005921e4",
      "DATA",
      [
        "storage",
        "00bf2d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005921e4",
      "DATA",
      [
        "storage",
        "00bf2dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005921e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005921c0.md#insn-005921e0)
- 新版 [`005921e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921c0.md#insn-005921e0)

~~~diff
- 005921e0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005921e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005921e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005921e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 005921e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005921e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005921e0 bytes 08a13491
+ 005921e0 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-781504506c3e1c080c6b9360c242b42d"></a>

### [`005921f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005921f4.md) → [`005921f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921f4.md) FUN_005921f4

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
      "definition_site": "00592200",
      "incomplete_value": false,
      "site": "00592200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592200",
      "incomplete_value": false,
      "site": "00592200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
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
      "00592200",
      "DATA",
      [
        "storage",
        "00bf2d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592200",
      "DATA",
      [
        "storage",
        "00bf2dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005921fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005921f4.md#insn-005921fc)
- 新版 [`005921fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005921f4.md#insn-005921fc)

~~~diff
- 005921fc ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005921fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005921fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005921fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 005921fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005921fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005921fc bytes 29a13491
+ 005921fc bytes 29613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c83ccb5128134719066e05e35d4e53b"></a>

### [`00592258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592258.md) → [`00592258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592258.md) FUN_00592258

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
      "definition_site": "0059227c",
      "incomplete_value": false,
      "site": "0059227c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059227c",
      "incomplete_value": false,
      "site": "0059227c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "0059227c",
      "DATA",
      [
        "storage",
        "00bf2da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059227c",
      "DATA",
      [
        "storage",
        "00bf2e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592258.md#insn-00592278)
- 新版 [`00592278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592258.md#insn-00592278)

~~~diff
- 00592278 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00592278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00592278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592278 bytes 08a13691
+ 00592278 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ea81d8563c93ce3b1c66613b961107a"></a>

### [`0059228c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059228c.md) → [`0059228c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059228c.md) FUN_0059228c

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
      "definition_site": "00592298",
      "incomplete_value": false,
      "site": "00592298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592298",
      "incomplete_value": false,
      "site": "00592298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "00592298",
      "DATA",
      [
        "storage",
        "00bf2da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592298",
      "DATA",
      [
        "storage",
        "00bf2e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059228c.md#insn-00592294)
- 新版 [`00592294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059228c.md#insn-00592294)

~~~diff
- 00592294 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00592294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00592294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592294 bytes 29a13691
+ 00592294 bytes 29613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012d0c4683cb8245aedf8860e5352581"></a>

### [`005922a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005922a8.md) → [`005922a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md) FUN_005922a8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0058c56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058c/0058c56c.md) [`00590ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590ba4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0058c56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058c56c.md) [`00590ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590ba4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fc1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f34:8"
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
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "005922f0",
      "incomplete_value": true,
      "site": "00592304",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005922f8",
      "incomplete_value": true,
      "site": "00592308",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "005922f8",
      "incomplete_value": true,
      "site": "00592308",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "005922f0",
      "READ",
      [
        "storage",
        "00298f34",
        null,
        null
      ]
    ],
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298f44",
        null,
        null
      ]
    ],
    [
      "005922f8",
      "READ",
      [
        "storage",
        "00298f54",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298fc1",
        null,
        null
      ]
    ],
    [
      "005922f0",
      "READ",
      [
        "storage",
        "00298fd1",
        null,
        null
      ]
    ],
    [
      "005922f8",
      "READ",
      [
        "storage",
        "00298fe1",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005922e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005922a8.md#insn-005922e8) · [`005922ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005922a8.md#insn-005922ec)
- 新版 [`005922e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md#insn-005922e8) · [`005922ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005922a8.md#insn-005922ec)

~~~diff
- 005922e8 ["COPY", "tmp:0:8", ["const:f34:8"]]
- 005922e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005922e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005922e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["COPY", "tmp:0:8", ["const:fc1:8"]]
+ 005922e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005922e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005922e8 bytes 08d13c91
+ 005922e8 bytes 08053f91
- 005922ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 005922ec bytes e9e8fff0
+ 005922ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 005922ec bytes e9e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580e826bdc77c8c9dabf096c09bf6c9f"></a>

### [`00592478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592478.md) → [`00592478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592478.md) FUN_00592478

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
      "definition_site": "0059249c",
      "incomplete_value": false,
      "site": "0059249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059249c",
      "incomplete_value": false,
      "site": "0059249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "0059249c",
      "DATA",
      [
        "storage",
        "00bf2e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059249c",
      "DATA",
      [
        "storage",
        "00bf2ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592478.md#insn-00592498)
- 新版 [`00592498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592478.md#insn-00592498)

~~~diff
- 00592498 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 00592498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00592498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592498 bytes 08e13891
+ 00592498 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b72efd8440482aedf3ff141e774664b"></a>

### [`005924ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924ac.md) → [`005924ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924ac.md) FUN_005924ac

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
      "definition_site": "005924b8",
      "incomplete_value": false,
      "site": "005924b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005924b8",
      "incomplete_value": false,
      "site": "005924b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "005924b8",
      "DATA",
      [
        "storage",
        "00bf2e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005924b8",
      "DATA",
      [
        "storage",
        "00bf2ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005924b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924ac.md#insn-005924b4)
- 新版 [`005924b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924ac.md#insn-005924b4)

~~~diff
- 005924b4 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 005924b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005924b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005924b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 005924b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005924b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005924b4 bytes 29e13891
+ 005924b4 bytes 29a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47ace8b7bbb26c1e7dcdb3caa40f7e65"></a>

### [`005924c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924c8.md) → [`005924c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md) FUN_005924c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0059277c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059277c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0059277c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059277c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059254c",
      "incomplete_value": false,
      "site": "00592554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059254c",
      "incomplete_value": false,
      "site": "00592554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00592554",
      "DATA",
      [
        "storage",
        "00bf2eb8",
        null,
        "pointer"
      ]
    ],
    [
      "0059264c",
      "READ",
      [
        "storage",
        "00bf2ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592554",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ],
    [
      "0059264c",
      "READ",
      [
        "storage",
        "00bf2f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059254c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924c8.md#insn-0059254c) · [`00592550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/005924c8.md#insn-00592550)
- 新版 [`0059254c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md#insn-0059254c) · [`00592550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/005924c8.md#insn-00592550)

~~~diff
- 0059254c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0059254c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059254c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059254c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0059254c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059254c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059254c bytes 08e13a91
+ 0059254c bytes 08a13d91
- 00592550 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 00592550 bytes f60300aa
+ 00592550 ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 00592550 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4146235ab99aba2de069159ff8e7e2ed"></a>

### [`0059273c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059273c.md) → [`0059273c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059273c.md) FUN_0059273c

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
      "definition_site": "00592740",
      "incomplete_value": false,
      "site": "00592744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592740",
      "incomplete_value": false,
      "site": "00592744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00592744",
      "DATA",
      [
        "storage",
        "00bf2eb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592744",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059273c.md#insn-00592740)
- 新版 [`00592740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059273c.md#insn-00592740)

~~~diff
- 00592740 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00592740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00592740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592740 bytes 08e13a91
+ 00592740 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-332241f2b3dfca1d68bd35be1089da7a"></a>

### [`0059274c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059274c.md) → [`0059274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059274c.md) FUN_0059274c

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
      "definition_site": "0059275c",
      "incomplete_value": false,
      "site": "00592764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059275c",
      "incomplete_value": false,
      "site": "00592764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "00592764",
      "DATA",
      [
        "storage",
        "00bf2eb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592764",
      "DATA",
      [
        "storage",
        "00bf2f68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059275c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059274c.md#insn-0059275c)
- 新版 [`0059275c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059274c.md#insn-0059275c)

~~~diff
- 0059275c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0059275c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059275c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059275c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0059275c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059275c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059275c bytes 08e13a91
+ 0059275c bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8cedcecf3336fc3e0de72cd880b497"></a>

### [`0059280c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059280c.md) → [`0059280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059280c.md) FUN_0059280c

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
      "definition_site": "00592830",
      "incomplete_value": false,
      "site": "00592830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592830",
      "incomplete_value": false,
      "site": "00592830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "00592830",
      "DATA",
      [
        "storage",
        "00bf2f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592830",
      "DATA",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059282c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059280c.md#insn-0059282c)
- 新版 [`0059282c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059280c.md#insn-0059282c)

~~~diff
- 0059282c ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0059282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 0059282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059282c bytes 08613c91
+ 0059282c bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ade0a284630b6b8b874411b5febbf131"></a>

### [`00592840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592840.md) → [`00592840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592840.md) FUN_00592840

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
      "definition_site": "0059284c",
      "incomplete_value": false,
      "site": "0059284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059284c",
      "incomplete_value": false,
      "site": "0059284c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0059284c",
      "DATA",
      [
        "storage",
        "00bf2f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059284c",
      "DATA",
      [
        "storage",
        "00bf2fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592840.md#insn-00592848)
- 新版 [`00592848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592840.md#insn-00592848)

~~~diff
- 00592848 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00592848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00592848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592848 bytes 29613c91
+ 00592848 bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb71e82421c17181a00bee894da14e1"></a>

### [`00592958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592958.md) → [`00592958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592958.md) FUN_00592958

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
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "0059297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "0059297c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0059297c",
      "DATA",
      [
        "storage",
        "00bf2f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059297c",
      "DATA",
      [
        "storage",
        "00bf3048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592958.md#insn-00592974) · [`00592978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592958.md#insn-00592978)
- 新版 [`00592974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592958.md#insn-00592974) · [`00592978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592958.md#insn-00592978)

~~~diff
- 00592974 ["COPY", "register:4040:8", ["const:bf2000:8"]]
+ 00592974 ["COPY", "register:4040:8", ["const:bf3000:8"]]
- 00592974 bytes 08330090
+ 00592974 bytes 083300b0
- 00592978 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00592978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00592978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592978 bytes 08613e91
+ 00592978 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a41dbb1a0b552613fafdee8335d5fad4"></a>

### [`0059298c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059298c.md) → [`0059298c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059298c.md) FUN_0059298c

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
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "00592998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "00592998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf2000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00592998",
      "DATA",
      [
        "storage",
        "00bf2f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592998",
      "DATA",
      [
        "storage",
        "00bf3048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059298c.md#insn-00592990) · [`00592994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/0059298c.md#insn-00592994)
- 新版 [`00592990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059298c.md#insn-00592990) · [`00592994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/0059298c.md#insn-00592994)

~~~diff
- 00592990 ["COPY", "register:4048:8", ["const:bf2000:8"]]
+ 00592990 ["COPY", "register:4048:8", ["const:bf3000:8"]]
- 00592990 bytes 09330090
+ 00592990 bytes 093300b0
- 00592994 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00592994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00592994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592994 bytes 29613e91
+ 00592994 bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cf7cd337f9a695905ba8f3b76c4e00c"></a>

### [`00592a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592a84.md) → [`00592a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592a84.md) FUN_00592a84

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
      "definition_site": "00592aa8",
      "incomplete_value": false,
      "site": "00592aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592aa8",
      "incomplete_value": false,
      "site": "00592aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00592aa8",
      "DATA",
      [
        "storage",
        "00bf3018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592aa8",
      "DATA",
      [
        "storage",
        "00bf30c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592a84.md#insn-00592aa4)
- 新版 [`00592aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592a84.md#insn-00592aa4)

~~~diff
- 00592aa4 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00592aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00592aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592aa4 bytes 08610091
+ 00592aa4 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdc62c4a0494e23887b4a322ca7f417"></a>

### [`00592ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ab8.md) → [`00592ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ab8.md) FUN_00592ab8

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
      "definition_site": "00592ac4",
      "incomplete_value": false,
      "site": "00592ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ac4",
      "incomplete_value": false,
      "site": "00592ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00592ac4",
      "DATA",
      [
        "storage",
        "00bf3018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592ac4",
      "DATA",
      [
        "storage",
        "00bf30c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ab8.md#insn-00592ac0)
- 新版 [`00592ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ab8.md#insn-00592ac0)

~~~diff
- 00592ac0 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00592ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00592ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592ac0 bytes 29610091
+ 00592ac0 bytes 29210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dcc5e83acb8dd080e91645f233d7b1f"></a>

### [`00592b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592b14.md) → [`00592b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md) FUN_00592b14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058f504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f504.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058f504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f504.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592b4c",
      "incomplete_value": false,
      "site": "00592b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592b4c",
      "incomplete_value": false,
      "site": "00592b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00592b54",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00592c0c",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592b54",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00592c0c",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592b14.md#insn-00592b4c) · [`00592b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592b14.md#insn-00592b50)
- 新版 [`00592b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md#insn-00592b4c) · [`00592b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592b14.md#insn-00592b50)

~~~diff
- 00592b4c ["COPY", "tmp:0:8", ["const:98:8"]]
- 00592b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00592b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592b4c bytes 08610291
+ 00592b4c bytes 08210591
- 00592b50 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00592b50 bytes f30300aa
+ 00592b50 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00592b50 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68806b2ae4a23b184799ec412714cd26"></a>

### [`00592c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592c8c.md) → [`00592c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c8c.md) FUN_00592c8c

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
      "definition_site": "00592c90",
      "incomplete_value": false,
      "site": "00592c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c90",
      "incomplete_value": false,
      "site": "00592c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00592c94",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592c94",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592c8c.md#insn-00592c90)
- 新版 [`00592c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c8c.md#insn-00592c90)

~~~diff
- 00592c90 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00592c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00592c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c90 bytes 08610291
+ 00592c90 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdd015525c8903aac6662ff4f2259ac1"></a>

### [`00592c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592c9c.md) → [`00592c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c9c.md) FUN_00592c9c

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
      "definition_site": "00592cac",
      "incomplete_value": false,
      "site": "00592cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592cac",
      "incomplete_value": false,
      "site": "00592cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00592cb4",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00592cb4",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592c9c.md#insn-00592cac)
- 新版 [`00592cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592c9c.md#insn-00592cac)

~~~diff
- 00592cac ["COPY", "tmp:0:8", ["const:98:8"]]
- 00592cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00592cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592cac bytes 08610291
+ 00592cac bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ded1c22b7bc7f1421c23915a7aca97"></a>

### [`00592cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592cdc.md) → [`00592cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592cdc.md) FUN_00592cdc

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
      "definition_site": "00592ce8",
      "incomplete_value": false,
      "site": "00592cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ce8",
      "incomplete_value": false,
      "site": "00592cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "00592cf4",
      "DATA",
      [
        "storage",
        "00bf30e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592cf4",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592cdc.md#insn-00592ce8)
- 新版 [`00592ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592cdc.md#insn-00592ce8)

~~~diff
- 00592ce8 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00592ce8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592ce8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00592ce8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00592ce8 bytes 4aa10391
+ 00592ce8 bytes 4a610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777e613693c9255f7848268f32e66ce2"></a>

### [`00592d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592d20.md) → [`00592d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d20.md) FUN_00592d20

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00592d38",
      "incomplete_value": true,
      "site": "00592d44",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592d38",
      "incomplete_value": true,
      "site": "00592d44",
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
            "const:e8:8"
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
      "00592d44",
      "DATA",
      [
        "storage",
        "00bf30e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d44",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592d20.md#insn-00592d38)
- 新版 [`00592d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d20.md#insn-00592d38)

~~~diff
- 00592d38 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00592d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592d38 bytes 08a10391
+ 00592d38 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b77dd089839a909ffb42476e1797742"></a>

### [`00592d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592d7c.md) → [`00592d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d7c.md) FUN_00592d7c

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
      "definition_site": "00592da8",
      "incomplete_value": false,
      "site": "00592da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592da8",
      "incomplete_value": false,
      "site": "00592da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "00592da8",
      "DATA",
      [
        "storage",
        "00bf30e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592da8",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592d7c.md#insn-00592da0)
- 新版 [`00592da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592d7c.md#insn-00592da0)

~~~diff
- 00592da0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00592da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592da0 bytes 08a10391
+ 00592da0 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3db2120964efe66eb8e754b0b37b140"></a>

### [`00592e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592e04.md) → [`00592e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592e04.md) FUN_00592e04

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
      "definition_site": "00592e20",
      "incomplete_value": false,
      "site": "00592e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592e20",
      "incomplete_value": false,
      "site": "00592e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "00592e20",
      "DATA",
      [
        "storage",
        "00bf30e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592e20",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592e04.md#insn-00592e1c)
- 新版 [`00592e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592e04.md#insn-00592e1c)

~~~diff
- 00592e1c ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00592e1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00592e1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00592e1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00592e1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00592e1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00592e1c bytes 29a10391
+ 00592e1c bytes 29610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d75408cb1ec96656c5f30281decf72e"></a>

### [`005930c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005930c4.md) → [`005930c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005930c4.md) FUN_005930c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00593104",
      "incomplete_value": false,
      "site": "00593108",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "00593104",
      "incomplete_value": false,
      "site": "00593108",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00593108",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593108",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005930fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005930c4.md#insn-005930fc)
- 新版 [`005930fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005930c4.md#insn-005930fc)

~~~diff
- 005930fc ["COPY", "tmp:0:8", ["const:950:8"]]
- 005930fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005930fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005930fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005930fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005930fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005930fc bytes 08412591
+ 005930fc bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7db75d5bc2019f12be7af6d3ee3fd91f"></a>

### [`0059313c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/0059313c.md) → [`0059313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md) FUN_0059313c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058d/0058d7b4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058d/0058d7b4.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593174",
      "incomplete_value": false,
      "site": "0059317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593174",
      "incomplete_value": false,
      "site": "0059317c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "0059317c",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00593234",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059317c",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593234",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/0059313c.md#insn-00593174) · [`00593178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/0059313c.md#insn-00593178)
- 新版 [`00593174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md#insn-00593174) · [`00593178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/0059313c.md#insn-00593178)

~~~diff
- 00593174 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00593174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00593174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593174 bytes 08610291
+ 00593174 bytes 08210591
- 00593178 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593178 bytes f30300aa
+ 00593178 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593178 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84506074067175e114bebaab39d53254"></a>

### [`005932b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005932b4.md) → [`005932b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005932b4.md) FUN_005932b4

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
      "definition_site": "005932c0",
      "incomplete_value": false,
      "site": "005932cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005932c0",
      "incomplete_value": false,
      "site": "005932cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "005932cc",
      "DATA",
      [
        "storage",
        "00bf3178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005932cc",
      "DATA",
      [
        "storage",
        "00bf3228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005932c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005932b4.md#insn-005932c0)
- 新版 [`005932c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005932b4.md#insn-005932c0)

~~~diff
- 005932c0 ["COPY", "tmp:0:8", ["const:178:8"]]
- 005932c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005932c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005932c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 005932c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005932c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005932c0 bytes 4ae10591
+ 005932c0 bytes 4aa10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32cc6bb09aab02ba3c348b6f0d101bd6"></a>

### [`00593354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593354.md) → [`00593354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593354.md) FUN_00593354

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
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "00593380",
      "DATA",
      [
        "storage",
        "00bf3178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593380",
      "DATA",
      [
        "storage",
        "00bf3228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593354.md#insn-00593378)
- 新版 [`00593378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593354.md#insn-00593378)

~~~diff
- 00593378 ["COPY", "tmp:0:8", ["const:178:8"]]
- 00593378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00593378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593378 bytes 08e10591
+ 00593378 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c1460d4d76fbdf937d93a822b4450a1"></a>

### [`00593688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593688.md) → [`00593688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md) FUN_00593688

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058ef88.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058ef88.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005936c0",
      "incomplete_value": false,
      "site": "005936c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005936c0",
      "incomplete_value": false,
      "site": "005936c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "005936c8",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00593780",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005936c8",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593780",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005936c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593688.md#insn-005936c0) · [`005936c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593688.md#insn-005936c4)
- 新版 [`005936c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md#insn-005936c0) · [`005936c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593688.md#insn-005936c4)

~~~diff
- 005936c0 ["COPY", "tmp:0:8", ["const:98:8"]]
- 005936c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005936c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005936c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 005936c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005936c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005936c0 bytes 08610291
+ 005936c0 bytes 08210591
- 005936c4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005936c4 bytes f30300aa
+ 005936c4 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 005936c4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89b3893a2b8e4a71c80eb986c7184d00"></a>

### [`00593800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593800.md) → [`00593800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593800.md) FUN_00593800

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
      "definition_site": "0059380c",
      "incomplete_value": false,
      "site": "00593818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059380c",
      "incomplete_value": false,
      "site": "00593818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593818",
      "DATA",
      [
        "storage",
        "00bf31f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593818",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059380c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593800.md#insn-0059380c)
- 新版 [`0059380c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593800.md#insn-0059380c)

~~~diff
- 0059380c ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 0059380c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059380c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059380c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0059380c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059380c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059380c bytes 4ae10791
+ 0059380c bytes 4aa10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72781b453b96c242a544e00c38090f2d"></a>

### [`00593844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593844.md) → [`00593844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593844.md) FUN_00593844

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
      "definition_site": "0059385c",
      "incomplete_value": false,
      "site": "00593868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059385c",
      "incomplete_value": false,
      "site": "00593868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "00593868",
      "DATA",
      [
        "storage",
        "00bf31f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593868",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059385c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593844.md#insn-0059385c)
- 新版 [`0059385c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593844.md#insn-0059385c)

~~~diff
- 0059385c ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 0059385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0059385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059385c bytes 08e10791
+ 0059385c bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a7dae002a39f1057d4911f1a2782d3"></a>

### [`005938a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005938a0.md) → [`005938a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005938a0.md) FUN_005938a0

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
      "definition_site": "005938cc",
      "incomplete_value": false,
      "site": "005938cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005938cc",
      "incomplete_value": false,
      "site": "005938cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "005938cc",
      "DATA",
      [
        "storage",
        "00bf31f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005938cc",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005938c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/005938a0.md#insn-005938c4)
- 新版 [`005938c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/005938a0.md#insn-005938c4)

~~~diff
- 005938c4 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 005938c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005938c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005938c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 005938c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005938c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005938c4 bytes 08e10791
+ 005938c4 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-354b473286778d6b23bf35a18f6df744"></a>

### [`00593928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593928.md) → [`00593928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593928.md) FUN_00593928

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
      "definition_site": "00593944",
      "incomplete_value": false,
      "site": "00593944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593944",
      "incomplete_value": false,
      "site": "00593944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "00593944",
      "DATA",
      [
        "storage",
        "00bf31f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593944",
      "DATA",
      [
        "storage",
        "00bf32a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593928.md#insn-00593940)
- 新版 [`00593940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593928.md#insn-00593940)

~~~diff
- 00593940 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00593940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00593940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00593940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00593940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00593940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00593940 bytes 29e10791
+ 00593940 bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aeeabd240ae56a78548d5056dfc16d0"></a>

### [`00593a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593a6c.md) → [`00593a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md) FUN_00593a6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058e0ec.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e0ec.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593aa4",
      "incomplete_value": false,
      "site": "00593aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593aa4",
      "incomplete_value": false,
      "site": "00593aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00593aac",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00593b64",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593aac",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593b64",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593a6c.md#insn-00593aa4) · [`00593aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593a6c.md#insn-00593aa8)
- 新版 [`00593aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md#insn-00593aa4) · [`00593aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593a6c.md#insn-00593aa8)

~~~diff
- 00593aa4 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00593aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00593aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593aa4 bytes 08610291
+ 00593aa4 bytes 08210591
- 00593aa8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593aa8 bytes f30300aa
+ 00593aa8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593aa8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5648c02e02bc04d58b5603e135ca599d"></a>

### [`00593be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593be4.md) → [`00593be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593be4.md) FUN_00593be4

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
      "definition_site": "00593bf0",
      "incomplete_value": false,
      "site": "00593bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593bf0",
      "incomplete_value": false,
      "site": "00593bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593bfc",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593bfc",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593be4.md#insn-00593bf0)
- 新版 [`00593bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593be4.md#insn-00593bf0)

~~~diff
- 00593bf0 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00593bf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00593bf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00593bf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00593bf0 bytes 4ae10991
+ 00593bf0 bytes 4aa10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d284fcd9eef5fd6d14197f0bfa35196"></a>

### [`00593c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593c28.md) → [`00593c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c28.md) FUN_00593c28

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
      "definition_site": "00593c40",
      "incomplete_value": false,
      "site": "00593c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593c40",
      "incomplete_value": false,
      "site": "00593c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00593c4c",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593c4c",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593c28.md#insn-00593c40)
- 新版 [`00593c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c28.md#insn-00593c40)

~~~diff
- 00593c40 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00593c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00593c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593c40 bytes 08e10991
+ 00593c40 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a46848291316bf1fe972af01de2adb62"></a>

### [`00593c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593c84.md) → [`00593c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c84.md) FUN_00593c84

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
      "definition_site": "00593cb0",
      "incomplete_value": false,
      "site": "00593cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593cb0",
      "incomplete_value": false,
      "site": "00593cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00593cb0",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593cb0",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593c84.md#insn-00593ca8)
- 新版 [`00593ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593c84.md#insn-00593ca8)

~~~diff
- 00593ca8 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00593ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00593ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593ca8 bytes 08e10991
+ 00593ca8 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

