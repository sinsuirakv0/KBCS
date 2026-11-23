# v15.7.3 → v15.7.4 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-22a1cafaf3442693beb92d081a10201a"></a>

### [`00559da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559da0.md) → [`00559da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md) FUN_00559da0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef000",
        null,
        "undefined *"
      ]
    ],
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef050",
        null,
        "undefined *"
      ]
    ],
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef118",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559da0.md#insn-00559db4)
- 新版 [`00559db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md#insn-00559db4)

~~~diff
- 00559db4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00559db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 00559db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559db4 bytes 08010091
+ 00559db4 bytes 08410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a7af847ff70a6816941886e0e0fa58"></a>

### [`00559fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md) → [`00559fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md) FUN_00559fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055a150",
      "incomplete_value": false,
      "site": "0055a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a150",
      "incomplete_value": false,
      "site": "0055a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "0055a15c",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a15c",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md#insn-0055a150)
- 新版 [`0055a150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md#insn-0055a150)

~~~diff
- 0055a150 ["COPY", "tmp:0:8", ["const:250:8"]]
- 0055a150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055a150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a150 bytes 08410991
+ 0055a150 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5058ab906d28a6350b1ec9f65d44851"></a>

### [`0055a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a5bc.md) → [`0055a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md) FUN_0055a5bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055a734",
      "incomplete_value": false,
      "site": "0055a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a734",
      "incomplete_value": false,
      "site": "0055a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "0055a740",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a740",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a5bc.md#insn-0055a734)
- 新版 [`0055a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md#insn-0055a734)

~~~diff
- 0055a734 ["COPY", "tmp:0:8", ["const:250:8"]]
- 0055a734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055a734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a734 bytes 08410991
+ 0055a734 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbb9158cfb7c480ca53d239e477d8bd2"></a>

### [`0055aad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md) → [`0055aad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md) FUN_0055aad0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dccc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md) [`00bdd2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2c0.md)
- 新版 呼出元 1件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md) [`00bdd310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd310.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.17% / 新版 86.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ab28",
      "incomplete_value": false,
      "site": "0055ab34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab28",
      "incomplete_value": false,
      "site": "0055ab34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "definition_site": "0055ab48",
      "incomplete_value": false,
      "site": "0055ab48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab48",
      "incomplete_value": false,
      "site": "0055ab48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "0055ab4c",
      "incomplete_value": false,
      "site": "0055ab50",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab4c",
      "incomplete_value": false,
      "site": "0055ab50",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055aaf0",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ],
    [
      "0055ab04",
      "READ",
      [
        "storage",
        "00c263b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0055ab34",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055aaf0",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0055ab04",
      "READ",
      [
        "storage",
        "00c263f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0055ab34",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055aaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md#insn-0055aaf0) · [`0055ab28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md#insn-0055ab28) · [`0055ab2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md#insn-0055ab2c)
- 新版 [`0055aaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md#insn-0055aaf0) · [`0055ab28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md#insn-0055ab28)

~~~diff
- 0055aaf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
- 0055aaf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055aaf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 0055aaf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055aaf0 bytes 084942f9
+ 0055aaf0 bytes 087142f9
- 0055ab28 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 0055ab28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0055ab28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 bytes 08810a91
+ 0055ab28 bytes 08c10b91
- 0055ab2c ["COPY", "register:4048:8", ["const:bef000:8"]]
- 0055ab2c bytes a93400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c440b11a197a7a3e2741e536e7c3476c"></a>

### [`0055ac68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac68.md) → [`0055ac68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac68.md) FUN_0055ac68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:130:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef1a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef130",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef1f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac68.md#insn-0055ac6c)
- 新版 [`0055ac6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac68.md#insn-0055ac6c)

~~~diff
- 0055ac6c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0055ac6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["COPY", "tmp:0:8", ["const:130:8"]]
+ 0055ac6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c bytes 08810391
+ 0055ac6c bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff23eacdeffc78f0da89173330b7d78f"></a>

### [`0055ac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac8c.md) → [`0055ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md) FUN_0055ac8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
                "const:130:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef1a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef130",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef1f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac8c.md#insn-0055ac90)
- 新版 [`0055ac90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md#insn-0055ac90)

~~~diff
- 0055ac90 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0055ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 0055ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 bytes 08810391
+ 0055ac90 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113f992c331e6627a5f8695428510faa"></a>

### [`0055acd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055acd0.md) → [`0055acd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055acd0.md) FUN_0055acd0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055acd4",
      "incomplete_value": false,
      "site": "0055acd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055acd4",
      "incomplete_value": false,
      "site": "0055acd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "0055acd8",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055acd8",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055acd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055acd0.md#insn-0055acd4)
- 新版 [`0055acd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055acd0.md#insn-0055acd4)

~~~diff
- 0055acd4 ["COPY", "tmp:0:8", ["const:250:8"]]
- 0055acd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055acd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 bytes 08410991
+ 0055acd4 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925e0517c2bfe9d4f05d36a9015b54eb"></a>

### [`0055ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad20.md) → [`0055ad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad20.md) FUN_0055ad20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055ad24",
      "incomplete_value": false,
      "site": "0055ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad24",
      "incomplete_value": false,
      "site": "0055ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "0055ad28",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad28",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad20.md#insn-0055ad24)
- 新版 [`0055ad24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad20.md#insn-0055ad24)

~~~diff
- 0055ad24 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 0055ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0055ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 bytes 08810a91
+ 0055ad24 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb376c8f75879230ac8bc3ff3654599"></a>

### [`0055ad70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad70.md) → [`0055ad70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad70.md) FUN_0055ad70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055ad74",
      "incomplete_value": false,
      "site": "0055ad78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad74",
      "incomplete_value": false,
      "site": "0055ad78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "0055ad78",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad78",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad70.md#insn-0055ad74)
- 新版 [`0055ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad70.md#insn-0055ad74)

~~~diff
- 0055ad74 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0055ad74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0055ad74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 bytes 08c10b91
+ 0055ad74 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdf5d06033196aee2c2dcefac825ae4d"></a>

### [`0055ad80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad80.md) → [`0055ad80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad80.md) FUN_0055ad80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055ad90",
      "incomplete_value": false,
      "site": "0055ad98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad90",
      "incomplete_value": false,
      "site": "0055ad98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "0055ad98",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad98",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad80.md#insn-0055ad90)
- 新版 [`0055ad90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ad80.md#insn-0055ad90)

~~~diff
- 0055ad90 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0055ad90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0055ad90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 bytes 08c10b91
+ 0055ad90 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a0d64dad8977624656ea6645c730b8"></a>

### [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) → [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) FUN_0055b1b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0052dd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd30.md) [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`0056340c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 3件 [`0052dd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd30.md) [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`0056340c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b1ec",
      "incomplete_value": false,
      "site": "0055b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b1ec",
      "incomplete_value": false,
      "site": "0055b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "0055b1f4",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b20c",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b1f4",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b20c",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md#insn-0055b1ec) · [`0055b200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md#insn-0055b200)
- 新版 [`0055b1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md#insn-0055b1ec) · [`0055b200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md#insn-0055b200)

~~~diff
- 0055b1ec ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0055b1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0055b1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec bytes 08e10e91
+ 0055b1ec bytes 08211091
- 0055b200 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0055b200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055b200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055b200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0055b200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055b200 bytes 29010d91
+ 0055b200 bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886b5d0cd458399f98ca362d1f091ec2"></a>

### [`0055b28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b28c.md) → [`0055b28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md) FUN_0055b28c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b2a4",
      "incomplete_value": true,
      "site": "0055b2a8",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b2a4",
      "incomplete_value": true,
      "site": "0055b2a8",
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
            "const:340:8"
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
      "0055b2a8",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b2a8",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b28c.md#insn-0055b2a4)
- 新版 [`0055b2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md#insn-0055b2a4)

~~~diff
- 0055b2a4 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0055b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0055b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 bytes 08010d91
+ 0055b2a4 bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25764ce75af2f0ce3afecdd87fd9e062"></a>

### [`0055b304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b304.md) → [`0055b304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md) FUN_0055b304

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b31c",
      "incomplete_value": false,
      "site": "0055b320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b31c",
      "incomplete_value": false,
      "site": "0055b320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "0055b320",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b320",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b304.md#insn-0055b31c)
- 新版 [`0055b31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md#insn-0055b31c)

~~~diff
- 0055b31c ["COPY", "tmp:0:8", ["const:340:8"]]
- 0055b31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0055b31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b31c bytes 08010d91
+ 0055b31c bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df064265b22b3b664bb0cb39ba9bb719"></a>

### [`0055b37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b37c.md) → [`0055b37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md) FUN_0055b37c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0055af38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af38.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b3a8",
      "incomplete_value": false,
      "site": "0055b3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b3a8",
      "incomplete_value": false,
      "site": "0055b3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "definition_site": "0055b3b4",
      "incomplete_value": false,
      "site": "0055b3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b3b4",
      "incomplete_value": false,
      "site": "0055b3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "0055b3ac",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b3c4",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b3ac",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b3c4",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b37c.md#insn-0055b3a8) · [`0055b3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b37c.md#insn-0055b3b0)
- 新版 [`0055b3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md#insn-0055b3a8) · [`0055b3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md#insn-0055b3b0)

~~~diff
- 0055b3a8 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0055b3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0055b3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 bytes 08e10e91
+ 0055b3a8 bytes 08211091
- 0055b3b0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 0055b3b0 bytes a8340090
+ 0055b3b0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0055b3b0 bytes a8340090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea01c99c127a9f6df4f446a1ac8a1dc5"></a>

### [`0055b4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4a4.md) → [`0055b4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b4a4.md) FUN_0055b4a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055b4a8",
      "incomplete_value": false,
      "site": "0055b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b4a8",
      "incomplete_value": false,
      "site": "0055b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0055b4ac",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b4ac",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4a4.md#insn-0055b4a8)
- 新版 [`0055b4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b4a4.md#insn-0055b4a8)

~~~diff
- 0055b4a8 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0055b4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0055b4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 bytes 08e10e91
+ 0055b4a8 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b75d447e6b8ea9315d1d6d90e71a5d7"></a>

### [`0055b4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4b4.md) → [`0055b4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b4b4.md) FUN_0055b4b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055b4c4",
      "incomplete_value": false,
      "site": "0055b4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b4c4",
      "incomplete_value": false,
      "site": "0055b4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0055b4cc",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b4cc",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4b4.md#insn-0055b4c4)
- 新版 [`0055b4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b4b4.md#insn-0055b4c4)

~~~diff
- 0055b4c4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0055b4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0055b4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 bytes 08e10e91
+ 0055b4c4 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a407da58a2b5bb4839633603780e001"></a>

### [`0055b604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b604.md) → [`0055b604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md) FUN_0055b604

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0052dd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd54.md) [`0055bd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055bd18.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md)
- 新版 呼出元 2件 [`0052dd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd54.md) [`0055bd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd18.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.48% / 新版 95.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b664",
      "incomplete_value": true,
      "site": "0055b664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b664",
      "incomplete_value": true,
      "site": "0055b664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c56:8"
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
      "definition_site": "0055b71c",
      "incomplete_value": true,
      "site": "0055b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:798:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b71c",
      "incomplete_value": true,
      "site": "0055b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70d:8"
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
      "definition_site": "0055b724",
      "incomplete_value": true,
      "site": "0055b724",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055b724",
      "incomplete_value": true,
      "site": "0055b724",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055b654",
      "READ",
      [
        "storage",
        "00296c56",
        null,
        "string"
      ]
    ],
    [
      "0055b704",
      "READ",
      [
        "storage",
        "002a570d",
        null,
        "string"
      ]
    ],
    [
      "0055b70c",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055b654",
      "READ",
      [
        "storage",
        "00296bc9",
        null,
        "string"
      ]
    ],
    [
      "0055b704",
      "READ",
      [
        "storage",
        "002a5798",
        null,
        "string"
      ]
    ],
    [
      "0055b70c",
      "READ",
      [
        "storage",
        "002a579f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b604.md#insn-0055b650) · [`0055b700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b604.md#insn-0055b700)
- 新版 [`0055b650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md#insn-0055b650) · [`0055b700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md#insn-0055b700)

~~~diff
- 0055b650 ["COPY", "tmp:0:8", ["const:c56:8"]]
- 0055b650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["COPY", "tmp:0:8", ["const:bc9:8"]]
+ 0055b650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b650 bytes 08593191
+ 0055b650 bytes 08252f91
- 0055b700 ["COPY", "tmp:0:8", ["const:70d:8"]]
- 0055b700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055b700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055b700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055b700 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 0055b700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055b700 bytes 29351c91
+ 0055b700 bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496e2aa269c14f005d42b53d55bf593c"></a>

### [`0055b95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b95c.md) → [`0055b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md) FUN_0055b95c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd50.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md)
- 新版 呼出元 1件 [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ba74",
      "incomplete_value": true,
      "site": "0055ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:798:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ba74",
      "incomplete_value": true,
      "site": "0055ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70d:8"
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
      "definition_site": "0055ba7c",
      "incomplete_value": true,
      "site": "0055ba7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055ba7c",
      "incomplete_value": true,
      "site": "0055ba7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055ba5c",
      "READ",
      [
        "storage",
        "002a570d",
        null,
        "string"
      ]
    ],
    [
      "0055ba64",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055ba5c",
      "READ",
      [
        "storage",
        "002a5798",
        null,
        "string"
      ]
    ],
    [
      "0055ba64",
      "READ",
      [
        "storage",
        "002a579f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ba58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b95c.md#insn-0055ba58)
- 新版 [`0055ba58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md#insn-0055ba58)

~~~diff
- 0055ba58 ["COPY", "tmp:0:8", ["const:70d:8"]]
- 0055ba58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 0055ba58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 bytes 29351c91
+ 0055ba58 bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e113c549138b64caf563725c9c052b"></a>

### [`0055c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c104.md) → [`0055c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md) FUN_0055c104

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)

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
      "definition_site": "0055c150",
      "incomplete_value": true,
      "site": "0055c16c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c150",
      "incomplete_value": true,
      "site": "0055c16c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c2c:8"
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
      "0055c150",
      "READ",
      [
        "storage",
        "00295c2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c150",
      "READ",
      [
        "storage",
        "00295b9f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c104.md#insn-0055c140)
- 新版 [`0055c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md#insn-0055c140)

~~~diff
- 0055c140 ["COPY", "tmp:0:8", ["const:c2c:8"]]
- 0055c140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["COPY", "tmp:0:8", ["const:b9f:8"]]
+ 0055c140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c140 bytes 29b13091
+ 0055c140 bytes 297d2e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c851bb1411a5d3d96e4765eb9af337d"></a>

### [`0055c3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c3fc.md) → [`0055c3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md) FUN_0055c3fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c448",
      "incomplete_value": true,
      "site": "0055c458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:745:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c448",
      "incomplete_value": true,
      "site": "0055c458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ba:8"
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
      "definition_site": "0055c460",
      "incomplete_value": true,
      "site": "0055c460",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055c460",
      "incomplete_value": true,
      "site": "0055c460",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055c448",
      "READ",
      [
        "storage",
        "0029c6ba",
        null,
        "string"
      ]
    ],
    [
      "0055c44c",
      "READ",
      [
        "storage",
        "0029c6c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c448",
      "READ",
      [
        "storage",
        "0029c745",
        null,
        "string"
      ]
    ],
    [
      "0055c44c",
      "READ",
      [
        "storage",
        "0029c754",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c3fc.md#insn-0055c440) · [`0055c444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c3fc.md#insn-0055c444)
- 新版 [`0055c440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md#insn-0055c440) · [`0055c444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md#insn-0055c444)

~~~diff
- 0055c440 ["COPY", "tmp:0:8", ["const:6ba:8"]]
- 0055c440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["COPY", "tmp:0:8", ["const:745:8"]]
+ 0055c440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c440 bytes 08e91a91
+ 0055c440 bytes 08151d91
- 0055c444 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0055c444 bytes a9eaff90
+ 0055c444 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0055c444 bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2120ec27bf7dd2b78d4aaf80693c1b7c"></a>

### [`0055c58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c58c.md) → [`0055c58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md) FUN_0055c58c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c5f8",
      "incomplete_value": true,
      "site": "0055c604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:670:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c5f8",
      "incomplete_value": true,
      "site": "0055c604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e5:8"
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
      "definition_site": "0055c608",
      "incomplete_value": true,
      "site": "0055c608",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055c608",
      "incomplete_value": true,
      "site": "0055c608",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055c5f8",
      "READ",
      [
        "storage",
        "002a45e5",
        null,
        "string"
      ]
    ],
    [
      "0055c5fc",
      "READ",
      [
        "storage",
        "002a45f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c5f8",
      "READ",
      [
        "storage",
        "002a4670",
        null,
        "string"
      ]
    ],
    [
      "0055c5fc",
      "READ",
      [
        "storage",
        "002a467e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c58c.md#insn-0055c5f0)
- 新版 [`0055c5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md#insn-0055c5f0)

~~~diff
- 0055c5f0 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0055c5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 0055c5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 bytes 08951791
+ 0055c5f0 bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d04ce217ccc606cd18179daa25d11a9a"></a>

### [`0055c754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c754.md) → [`0055c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md) FUN_0055c754

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c79c",
      "incomplete_value": true,
      "site": "0055c7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c79c",
      "incomplete_value": true,
      "site": "0055c7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71d:8"
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
      "definition_site": "0055c7c8",
      "incomplete_value": true,
      "site": "0055c7d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a4b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c7c8",
      "incomplete_value": true,
      "site": "0055c7d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:adf:8"
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
      "definition_site": "0055c7cc",
      "incomplete_value": true,
      "site": "0055c7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055c7cc",
      "incomplete_value": true,
      "site": "0055c7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055c79c",
      "READ",
      [
        "storage",
        "002a571d",
        null,
        "string"
      ]
    ],
    [
      "0055c7c8",
      "READ",
      [
        "storage",
        "002aeadf",
        null,
        "string"
      ]
    ],
    [
      "0055c7cc",
      "READ",
      [
        "storage",
        "002aeaef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c79c",
      "READ",
      [
        "storage",
        "002a57a8",
        null,
        "string"
      ]
    ],
    [
      "0055c7c8",
      "READ",
      [
        "storage",
        "002aea4b",
        null,
        "string"
      ]
    ],
    [
      "0055c7cc",
      "READ",
      [
        "storage",
        "002aea5b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c754.md#insn-0055c794) · [`0055c7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c754.md#insn-0055c7c0) · [`0055c7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c754.md#insn-0055c7c4)
- 新版 [`0055c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md#insn-0055c794) · [`0055c7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md#insn-0055c7c0)

~~~diff
- 0055c794 ["COPY", "tmp:0:8", ["const:71d:8"]]
- 0055c794 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c794 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c794 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0055c794 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c794 bytes 29751c91
+ 0055c794 bytes 29a11e91
- 0055c7c0 ["COPY", "tmp:0:8", ["const:adf:8"]]
- 0055c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c7c0 ["COPY", "tmp:0:8", ["const:a4b:8"]]
+ 0055c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c7c0 bytes 087d2b91
+ 0055c7c0 bytes 082d2991
- 0055c7c4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0055c7c4 bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f89e036af3068f746e6d4f4ee33440"></a>

### [`0055c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md) → [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) FUN_0055c994

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0055ca04",
      "incomplete_value": true,
      "site": "0055ca04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ca04",
      "incomplete_value": true,
      "site": "0055ca04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e16:8"
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
      "0055c9f0",
      "READ",
      [
        "storage",
        "00299e16",
        null,
        "string"
      ]
    ],
    [
      "0055c9f8",
      "READ",
      [
        "storage",
        "00299e1b",
        null,
        "string"
      ]
    ],
    [
      "0055ca24",
      "READ",
      [
        "storage",
        "0029b540",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c9f0",
      "READ",
      [
        "storage",
        "00299e14",
        null,
        "string"
      ]
    ],
    [
      "0055c9f8",
      "READ",
      [
        "storage",
        "00299e19",
        null,
        "string"
      ]
    ],
    [
      "0055ca24",
      "READ",
      [
        "storage",
        "0029b53e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md#insn-0055c9ec) · [`0055c9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md#insn-0055c9fc)
- 新版 [`0055c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md#insn-0055c9ec) · [`0055c9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md#insn-0055c9fc)

~~~diff
- 0055c9ec ["COPY", "tmp:0:8", ["const:e16:8"]]
- 0055c9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["COPY", "tmp:0:8", ["const:e14:8"]]
+ 0055c9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec bytes 29593891
+ 0055c9ec bytes 29513891
- 0055c9fc ["COPY", "register:40c8:8", ["register:4000:8"]]
- 0055c9fc bytes f90300aa
+ 0055c9fc ["COPY", "register:40c8:8", ["register:4000:8"]]
+ 0055c9fc bytes f90300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf52da5ddf495736cc8dc8d92ccc42d"></a>

### [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) → [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) FUN_0055cc34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005323c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323c0.md) [`0055ce48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ce48.md) [`0055ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ced0.md) [`0055cf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cf7c.md) [`0055d024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d024.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)
- 新版 呼出元 6件 [`005323c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323c0.md) [`0055ce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md) [`0055ced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md) [`0055cf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md) [`0055d024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cc98",
      "incomplete_value": true,
      "site": "0055cc98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc98",
      "incomplete_value": true,
      "site": "0055cc98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:552:8"
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
      "definition_site": "0055cca0",
      "incomplete_value": true,
      "site": "0055cca0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055cca0",
      "incomplete_value": true,
      "site": "0055cca0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cc9c",
      "incomplete_value": true,
      "site": "0055ccb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bdc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc9c",
      "incomplete_value": true,
      "site": "0055ccb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c69:8"
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
      "0055cc80",
      "READ",
      [
        "storage",
        "002a2552",
        null,
        "string"
      ]
    ],
    [
      "0055cc88",
      "READ",
      [
        "storage",
        "002a2557",
        null,
        "string"
      ]
    ],
    [
      "0055cc9c",
      "READ",
      [
        "storage",
        "00291c69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cc80",
      "READ",
      [
        "storage",
        "002a25dd",
        null,
        "string"
      ]
    ],
    [
      "0055cc88",
      "READ",
      [
        "storage",
        "002a25e2",
        null,
        "string"
      ]
    ],
    [
      "0055cc9c",
      "READ",
      [
        "storage",
        "00291bdc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cc7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md#insn-0055cc7c) · [`0055cc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md#insn-0055cc8c)
- 新版 [`0055cc7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md#insn-0055cc7c) · [`0055cc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md#insn-0055cc8c)

~~~diff
- 0055cc7c ["COPY", "tmp:0:8", ["const:552:8"]]
- 0055cc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["COPY", "tmp:0:8", ["const:5dd:8"]]
+ 0055cc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c bytes 29491591
+ 0055cc7c bytes 29751791
- 0055cc8c ["COPY", "register:4048:8", ["const:291000:8"]]
- 0055cc8c bytes a9e9ffb0
+ 0055cc8c ["COPY", "register:4048:8", ["const:291000:8"]]
+ 0055cc8c bytes a9e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-429ab1b45603f44f988468f18487b5b3"></a>

### [`0055ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ced0.md) → [`0055ced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md) FUN_0055ced0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323c8.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005323c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323c8.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0055cf0c",
      "incomplete_value": true,
      "site": "0055cf0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cf0c",
      "incomplete_value": true,
      "site": "0055cf0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d2:8"
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
      "0055cef0",
      "READ",
      [
        "storage",
        "0029c6d2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cef0",
      "READ",
      [
        "storage",
        "0029c75d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ced0.md#insn-0055cee8)
- 新版 [`0055cee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md#insn-0055cee8)

~~~diff
- 0055cee8 ["COPY", "tmp:0:8", ["const:6d2:8"]]
- 0055cee8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["COPY", "tmp:0:8", ["const:75d:8"]]
+ 0055cee8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 bytes 6b491b91
+ 0055cee8 bytes 6b751d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02a5747e7de71e0a096115dc5a4c1801"></a>

### [`0055cf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cf7c.md) → [`0055cf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md) FUN_0055cf7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323cc.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005323cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323cc.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cfb0",
      "incomplete_value": true,
      "site": "0055cfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cfb0",
      "incomplete_value": true,
      "site": "0055cfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75e:8"
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
      "definition_site": "0055cfb4",
      "incomplete_value": true,
      "site": "0055cfb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055cfb4",
      "incomplete_value": true,
      "site": "0055cfb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055cf9c",
      "READ",
      [
        "storage",
        "002a975e",
        null,
        "string"
      ]
    ],
    [
      "0055cfa8",
      "READ",
      [
        "storage",
        "002a9764",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cf9c",
      "READ",
      [
        "storage",
        "002a976d",
        null,
        "string"
      ]
    ],
    [
      "0055cfa8",
      "READ",
      [
        "storage",
        "002a9773",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cf94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cf7c.md#insn-0055cf94)
- 新版 [`0055cf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md#insn-0055cf94)

~~~diff
- 0055cf94 ["COPY", "tmp:0:8", ["const:75e:8"]]
- 0055cf94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["COPY", "tmp:0:8", ["const:76d:8"]]
+ 0055cf94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 bytes 4a791d91
+ 0055cf94 bytes 4ab51d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6727bc7a0fd3c72ba5b02a0b68ec21"></a>

### [`0055d0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d0c8.md) → [`0055d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md) FUN_0055d0c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323d4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005323d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323d4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d0fc",
      "incomplete_value": true,
      "site": "0055d0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d0fc",
      "incomplete_value": true,
      "site": "0055d0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:643:8"
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
      "definition_site": "0055d100",
      "incomplete_value": true,
      "site": "0055d100",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055d100",
      "incomplete_value": true,
      "site": "0055d100",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0055d0e8",
      "READ",
      [
        "storage",
        "0029f643",
        null,
        "string"
      ]
    ],
    [
      "0055d0f4",
      "READ",
      [
        "storage",
        "0029f648",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d0e8",
      "READ",
      [
        "storage",
        "0029f6ce",
        null,
        "string"
      ]
    ],
    [
      "0055d0f4",
      "READ",
      [
        "storage",
        "0029f6d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d0c8.md#insn-0055d0e0)
- 新版 [`0055d0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md#insn-0055d0e0)

~~~diff
- 0055d0e0 ["COPY", "tmp:0:8", ["const:643:8"]]
- 0055d0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["COPY", "tmp:0:8", ["const:6ce:8"]]
+ 0055d0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 bytes 4a0d1991
+ 0055d0e0 bytes 4a391b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-105601c525d3a2a08bcf6d0178ff5bb6"></a>

### [`0055d170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d170.md) → [`0055d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d170.md) FUN_0055d170

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055d174",
      "incomplete_value": false,
      "site": "0055d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d174",
      "incomplete_value": false,
      "site": "0055d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "0055d178",
      "DATA",
      [
        "storage",
        "00bef4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d178",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d170.md#insn-0055d174)
- 新版 [`0055d174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d170.md#insn-0055d174)

~~~diff
- 0055d174 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 0055d174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055d174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d174 bytes 08c11291
+ 0055d174 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-987a1b692b58ae8002544a9d3d04c289"></a>

### [`0055d180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d180.md) → [`0055d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d180.md) FUN_0055d180

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055d190",
      "incomplete_value": false,
      "site": "0055d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d190",
      "incomplete_value": false,
      "site": "0055d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "0055d198",
      "DATA",
      [
        "storage",
        "00bef4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d198",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d180.md#insn-0055d190)
- 新版 [`0055d190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d180.md#insn-0055d190)

~~~diff
- 0055d190 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 0055d190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055d190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d190 bytes 08c11291
+ 0055d190 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40eb0ef41adaf59cd9f5c15b122e5ebb"></a>

### [`0055d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md) → [`0055d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md) FUN_0055d1c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005397f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397f8.md) · 呼出先 17件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`005397fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539804.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`005397f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397f8.md) · 呼出先 17件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`005397fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539804.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d228",
      "incomplete_value": true,
      "site": "0055d228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5eb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d228",
      "incomplete_value": true,
      "site": "0055d228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:560:8"
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:606:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57b:8"
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "0055d214",
      "READ",
      [
        "storage",
        "002a2560",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d57b",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d214",
      "READ",
      [
        "storage",
        "002a25eb",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d606",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d616",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md#insn-0055d208) · [`0055d238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md#insn-0055d238) · [`0055d23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md#insn-0055d23c)
- 新版 [`0055d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md#insn-0055d208) · [`0055d238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md#insn-0055d238)

~~~diff
- 0055d208 ["COPY", "tmp:0:8", ["const:560:8"]]
- 0055d208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055d208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055d208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["COPY", "tmp:0:8", ["const:5eb:8"]]
+ 0055d208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055d208 bytes 29811591
+ 0055d208 bytes 29ad1791
- 0055d238 ["COPY", "tmp:0:8", ["const:57b:8"]]
- 0055d238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["COPY", "tmp:0:8", ["const:606:8"]]
+ 0055d238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d238 bytes 08ed1591
+ 0055d238 bytes 08191891
- 0055d23c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055d23c bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4a1bb20498509e6f1f06d603424f32"></a>

### [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) → [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) FUN_0055d5cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00539948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539948.md) · 呼出先 20件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) [`0055af10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af10.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00539948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539948.md) · 呼出先 20件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) [`0055af10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af10.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cda:8"
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
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055d650",
      "incomplete_value": true,
      "site": "0055d658",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055d650",
      "incomplete_value": true,
      "site": "0055d658",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "0055d63c",
      "READ",
      [
        "storage",
        "00297cda",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297cea",
        null,
        "string"
      ]
    ],
    [
      "0055d650",
      "READ",
      [
        "storage",
        "00297cfa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297c4d",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297c5d",
        null,
        "string"
      ]
    ],
    [
      "0055d650",
      "READ",
      [
        "storage",
        "00297c6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md#insn-0055d634) · [`0055d638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md#insn-0055d638)
- 新版 [`0055d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md#insn-0055d634) · [`0055d638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md#insn-0055d638)

~~~diff
- 0055d634 ["COPY", "tmp:0:8", ["const:cda:8"]]
- 0055d634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["COPY", "tmp:0:8", ["const:c4d:8"]]
+ 0055d634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d634 bytes 08693391
+ 0055d634 bytes 08353191
- 0055d638 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055d638 bytes a9eaff90
+ 0055d638 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0055d638 bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb7f4c860328a06526c23ecfb2501861"></a>

### [`0055d9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d9b0.md) → [`0055d9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md) FUN_0055d9b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d57c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0053d57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d57c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055daf8",
      "incomplete_value": false,
      "site": "0055db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055daf8",
      "incomplete_value": false,
      "site": "0055db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055db04",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055db04",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055daf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d9b0.md#insn-0055daf8)
- 新版 [`0055daf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md#insn-0055daf8)

~~~diff
- 0055daf8 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055daf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055daf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 bytes 08011491
+ 0055daf8 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dadd30f137f0e9c71a0db30f015c95fa"></a>

### [`0055dc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055dc58.md) → [`0055dc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md) FUN_0055dc58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053d584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d584.md) · 呼出先 8件 [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00574734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574734.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0053d584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d584.md) · 呼出先 8件 [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055dcbc",
      "incomplete_value": false,
      "site": "0055dcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dcbc",
      "incomplete_value": false,
      "site": "0055dcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "0055dcc8",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055dcc8",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055dcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055dc58.md#insn-0055dcbc)
- 新版 [`0055dcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md#insn-0055dcbc)

~~~diff
- 0055dcbc ["COPY", "tmp:0:8", ["const:250:8"]]
- 0055dcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055dcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc bytes 08410991
+ 0055dcbc bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d42914d9a5fcc465326e1c0503b78d0"></a>

### [`0055ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md) → [`0055ddc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md) FUN_0055ddc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bda8.md) · 呼出先 9件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00513fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`0053bda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bda8.md) · 呼出先 9件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055de88",
      "incomplete_value": true,
      "site": "0055de88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0055de88",
      "incomplete_value": true,
      "site": "0055de88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0055dedc",
      "incomplete_value": false,
      "site": "0055dee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dedc",
      "incomplete_value": false,
      "site": "0055dee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "definition_site": "0055def4",
      "incomplete_value": false,
      "site": "0055def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055def4",
      "incomplete_value": false,
      "site": "0055def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "0055de70",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0055de88",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0055dee4",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055de70",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0055de88",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0055dee4",
      "DATA",
      [
        "storage",
        "00bef5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md#insn-0055de70) · [`0055dedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md#insn-0055dedc) · [`0055dee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md#insn-0055dee8)
- 新版 [`0055de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md#insn-0055de70) · [`0055dedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md#insn-0055dedc)

~~~diff
- 0055de70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 0055de70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055de70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0055de70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055de70 bytes 08d147f9
+ 0055de70 bytes 08f947f9
- 0055dedc ["COPY", "tmp:0:8", ["const:550:8"]]
- 0055dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0055dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055dedc bytes 08411591
+ 0055dedc bytes 08811691
- 0055dee8 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 0055dee8 bytes 883400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c76d4d56a35a77c69ced21dc095e77"></a>

### [`0055e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e170.md) → [`0055e170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md) FUN_0055e170

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053bdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdac.md) · 呼出先 12件 [`00574734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574734.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0053bdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdac.md) · 呼出先 12件 [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e210",
      "incomplete_value": true,
      "site": "0055e210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e210",
      "incomplete_value": true,
      "site": "0055e210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:643:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055e1ac",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1ac",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "definition_site": "0055e1b4",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1b4",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "0055e1ac",
      "PARAM",
      [
        "storage",
        "00bef5b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1b4",
      "PARAM",
      [
        "storage",
        "00bef658",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1f0",
      "READ",
      [
        "storage",
        "0029e643",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e1ac",
      "PARAM",
      [
        "storage",
        "00bef608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1b4",
      "PARAM",
      [
        "storage",
        "00bef6a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1f0",
      "READ",
      [
        "storage",
        "0029e6ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e170.md#insn-0055e1ac) · [`0055e1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e170.md#insn-0055e1b4) · [`0055e1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e170.md#insn-0055e1e8)
- 新版 [`0055e1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1ac) · [`0055e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1b4) · [`0055e1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1e8)

~~~diff
- 0055e1ac ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0055e1ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0055e1ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac bytes 21e01691
+ 0055e1ac bytes 21201891
- 0055e1b4 ["COPY", "tmp:0:8", ["const:658:8"]]
- 0055e1b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 0055e1b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 bytes 42601991
+ 0055e1b4 bytes 42a01a91
- 0055e1e8 ["COPY", "tmp:0:8", ["const:643:8"]]
- 0055e1e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["COPY", "tmp:0:8", ["const:6ce:8"]]
+ 0055e1e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 bytes 290d1991
+ 0055e1e8 bytes 29391b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9abad5a1568e53eba6e55d0afad99c03"></a>

### [`0055e3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e3a4.md) → [`0055e3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md) FUN_0055e3a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdb0.md) · 呼出先 10件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0053bdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdb0.md) · 呼出先 10件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.79% / 新版 92.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e430",
      "incomplete_value": true,
      "site": "0055e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e430",
      "incomplete_value": true,
      "site": "0055e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:651:8"
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
      "definition_site": "0055e434",
      "incomplete_value": true,
      "site": "0055e444",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0055e434",
      "incomplete_value": true,
      "site": "0055e444",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055e3e0",
      "incomplete_value": false,
      "site": "0055e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e3e0",
      "incomplete_value": false,
      "site": "0055e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0055e3e0",
      "PARAM",
      [
        "storage",
        "00bef5b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e3e8",
      "PARAM",
      [
        "storage",
        "00bef5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e430",
      "READ",
      [
        "storage",
        "0029f651",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e3e0",
      "PARAM",
      [
        "storage",
        "00bef608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e3e8",
      "PARAM",
      [
        "storage",
        "00bef618",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e430",
      "READ",
      [
        "storage",
        "0029f6dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e3a4.md#insn-0055e3e0) · [`0055e3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e3a4.md#insn-0055e3e8) · [`0055e428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e3a4.md#insn-0055e428)
- 新版 [`0055e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e3e0) · [`0055e3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e3e8) · [`0055e428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e428)

~~~diff
- 0055e3e0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0055e3e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0055e3e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 bytes 21e01691
+ 0055e3e0 bytes 21201891
- 0055e3e8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 0055e3e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0055e3e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 bytes 42201791
+ 0055e3e8 bytes 42601891
- 0055e428 ["COPY", "tmp:0:8", ["const:651:8"]]
- 0055e428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["COPY", "tmp:0:8", ["const:6dc:8"]]
+ 0055e428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e428 bytes 08451991
+ 0055e428 bytes 08711b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880090bc7dceceb09c0de594ec2b41ef"></a>

### [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) → [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) FUN_0055e5bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0053be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e64c",
      "incomplete_value": true,
      "site": "0055e658",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055e64c",
      "incomplete_value": true,
      "site": "0055e658",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "0055e640",
      "READ",
      [
        "storage",
        "002a68cb",
        null,
        "string"
      ]
    ],
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a68db",
        null,
        "string"
      ]
    ],
    [
      "0055e64c",
      "READ",
      [
        "storage",
        "002a68eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a6965",
        null,
        "string"
      ]
    ],
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a6975",
        null,
        "string"
      ]
    ],
    [
      "0055e64c",
      "READ",
      [
        "storage",
        "002a6985",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md#insn-0055e63c) · [`0055e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md#insn-0055e778)
- 新版 [`0055e63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md#insn-0055e63c) · [`0055e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md#insn-0055e778)

~~~diff
- 0055e63c ["COPY", "tmp:0:8", ["const:8ab:8"]]
- 0055e63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["COPY", "tmp:0:8", ["const:945:8"]]
+ 0055e63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e63c bytes 08ad2291
+ 0055e63c bytes 08152591
- 0055e778 ["COPY", "tmp:0:8", ["const:680:8"]]
- 0055e778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055e778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e778 bytes 08011a91
+ 0055e778 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d58da597dbd56921b6a19b8b1049f0"></a>

### [`0055e88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md) → [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) FUN_0055e88c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053c1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c1bc.md) [`0053c1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c1c0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 2件 [`0053c1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1bc.md) [`0053c1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ea48",
      "incomplete_value": false,
      "site": "0055ea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ea48",
      "incomplete_value": false,
      "site": "0055ea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "0055e910",
      "READ",
      [
        "storage",
        "002a68cb",
        null,
        "string"
      ]
    ],
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a68db",
        null,
        "string"
      ]
    ],
    [
      "0055e91c",
      "READ",
      [
        "storage",
        "002a68eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a6965",
        null,
        "string"
      ]
    ],
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a6975",
        null,
        "string"
      ]
    ],
    [
      "0055e91c",
      "READ",
      [
        "storage",
        "002a6985",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md#insn-0055e90c) · [`0055ea48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md#insn-0055ea48)
- 新版 [`0055e90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md#insn-0055e90c) · [`0055ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md#insn-0055ea48)

~~~diff
- 0055e90c ["COPY", "tmp:0:8", ["const:8ab:8"]]
- 0055e90c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e90c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["COPY", "tmp:0:8", ["const:945:8"]]
+ 0055e90c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e90c bytes 08ad2291
+ 0055e90c bytes 08152591
- 0055ea48 ["COPY", "tmp:0:8", ["const:680:8"]]
- 0055ea48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055ea48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 bytes 08011a91
+ 0055ea48 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9985f9d7f9b3af2f538c33f9f5c29029"></a>

### [`0055eb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eb5c.md) → [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) FUN_0055eb5c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0053b878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b878.md) [`0053b998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b998.md) [`0053b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b99c.md) · 呼出先 2件 [`0055f8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 3件 [`0053b878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md) [`0053b998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b998.md) [`0053b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md) · 呼出先 2件 [`0055f8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055eb84",
      "incomplete_value": false,
      "site": "0055eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eb84",
      "incomplete_value": false,
      "site": "0055eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0055eb90",
      "DATA",
      [
        "storage",
        "00bef738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055eb90",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055eb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eb5c.md#insn-0055eb84)
- 新版 [`0055eb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md#insn-0055eb84)

~~~diff
- 0055eb84 ["COPY", "tmp:0:8", ["const:738:8"]]
- 0055eb84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0055eb84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 bytes 08e11c91
+ 0055eb84 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7cd4c5f63bd48c713cf19acfe34ad1d"></a>

### [`0055ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ebd0.md) → [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) FUN_0055ebd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md) [`0053bc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bc44.md) · 呼出先 2件 [`0055fe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md) [`0053bc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md) · 呼出先 2件 [`0055fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0055ec00",
      "incomplete_value": false,
      "site": "0055ec0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ec00",
      "incomplete_value": false,
      "site": "0055ec0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0055ec0c",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ec0c",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ec00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ebd0.md#insn-0055ec00)
- 新版 [`0055ec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md#insn-0055ec00)

~~~diff
- 0055ec00 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0055ec00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0055ec00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 bytes 08811f91
+ 0055ec00 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c075fe9ad8955ca2249b3fd9777383f4"></a>

### [`0055eef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eef8.md) → [`0055eef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eef8.md) FUN_0055eef8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055eefc",
      "incomplete_value": false,
      "site": "0055ef00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eefc",
      "incomplete_value": false,
      "site": "0055ef00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055ef00",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055ef00",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055eefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eef8.md#insn-0055eefc)
- 新版 [`0055eefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eef8.md#insn-0055eefc)

~~~diff
- 0055eefc ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055eefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055eefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055eefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055eefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055eefc bytes 08011491
+ 0055eefc bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8297e2f3e64c6ca525c359d958c07159"></a>

### [`0055ef48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef48.md) → [`0055ef48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef48.md) FUN_0055ef48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055ef4c",
      "incomplete_value": false,
      "site": "0055ef50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ef4c",
      "incomplete_value": false,
      "site": "0055ef50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0055ef50",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ef50",
      "DATA",
      [
        "storage",
        "00bef5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ef4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef48.md#insn-0055ef4c)
- 新版 [`0055ef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef48.md#insn-0055ef4c)

~~~diff
- 0055ef4c ["COPY", "tmp:0:8", ["const:550:8"]]
- 0055ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0055ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c bytes 08411591
+ 0055ef4c bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae7ae73bf9e117c810454f420a40ea05"></a>

### [`0055ef58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef58.md) → [`0055ef58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef58.md) FUN_0055ef58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055ef68",
      "incomplete_value": false,
      "site": "0055ef70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ef68",
      "incomplete_value": false,
      "site": "0055ef70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0055ef70",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ef70",
      "DATA",
      [
        "storage",
        "00bef5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ef68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef58.md#insn-0055ef68)
- 新版 [`0055ef68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef58.md#insn-0055ef68)

~~~diff
- 0055ef68 ["COPY", "tmp:0:8", ["const:550:8"]]
- 0055ef68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0055ef68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 bytes 08411591
+ 0055ef68 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa6c7413abbf28b781a1b8898e917cff"></a>

### [`0055efe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055efe8.md) → [`0055efe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055efe8.md) FUN_0055efe8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055efec",
      "incomplete_value": false,
      "site": "0055eff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055efec",
      "incomplete_value": false,
      "site": "0055eff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0055eff0",
      "DATA",
      [
        "storage",
        "00bef5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055eff0",
      "DATA",
      [
        "storage",
        "00bef640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055efe8.md#insn-0055efec)
- 新版 [`0055efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055efe8.md#insn-0055efec)

~~~diff
- 0055efec ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0055efec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055efec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055efec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0055efec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055efec bytes 08c11791
+ 0055efec bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a3dae9f6e16c90b6b31c10295cc34bb"></a>

### [`0055eff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eff8.md) → [`0055eff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eff8.md) FUN_0055eff8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055f008",
      "incomplete_value": false,
      "site": "0055f010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f008",
      "incomplete_value": false,
      "site": "0055f010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0055f010",
      "DATA",
      [
        "storage",
        "00bef5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f010",
      "DATA",
      [
        "storage",
        "00bef640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eff8.md#insn-0055f008)
- 新版 [`0055f008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eff8.md#insn-0055f008)

~~~diff
- 0055f008 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0055f008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0055f008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f008 bytes 08c11791
+ 0055f008 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06156059a9a31c68a95c170895f61149"></a>

### [`0055f094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f094.md) → [`0055f094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f094.md) FUN_0055f094

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055f098",
      "incomplete_value": false,
      "site": "0055f09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f098",
      "incomplete_value": false,
      "site": "0055f09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "0055f09c",
      "DATA",
      [
        "storage",
        "00bef680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f09c",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f094.md#insn-0055f098)
- 新版 [`0055f098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f094.md#insn-0055f098)

~~~diff
- 0055f098 ["COPY", "tmp:0:8", ["const:680:8"]]
- 0055f098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055f098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f098 bytes 08011a91
+ 0055f098 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1850d2ea2a5db35e0a701fcb7fa56add"></a>

### [`0055f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0a4.md) → [`0055f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0a4.md) FUN_0055f0a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055f0b4",
      "incomplete_value": false,
      "site": "0055f0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f0b4",
      "incomplete_value": false,
      "site": "0055f0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "0055f0bc",
      "DATA",
      [
        "storage",
        "00bef680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f0bc",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0a4.md#insn-0055f0b4)
- 新版 [`0055f0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0a4.md#insn-0055f0b4)

~~~diff
- 0055f0b4 ["COPY", "tmp:0:8", ["const:680:8"]]
- 0055f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 bytes 08011a91
+ 0055f0b4 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b4fcc39daf6e12007976ad9dd09ce2"></a>

### [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) → [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) FUN_0055f0e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md) · 呼出先 5件 [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`005668b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) · 呼出先 5件 [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`005668b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f120",
      "incomplete_value": false,
      "site": "0055f120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f120",
      "incomplete_value": false,
      "site": "0055f120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:687:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5fc:8"
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "0055f120",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a45fc",
        null,
        "string"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a460c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055f120",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a4687",
        null,
        "string"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a4697",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md#insn-0055f100) · [`0055f158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md#insn-0055f158) · [`0055f15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md#insn-0055f15c)
- 新版 [`0055f100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md#insn-0055f100) · [`0055f158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md#insn-0055f158)

~~~diff
- 0055f100 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0055f100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 0055f100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f100 bytes 29411b91
+ 0055f100 bytes 29811c91
- 0055f158 ["COPY", "tmp:0:8", ["const:5fc:8"]]
- 0055f158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["COPY", "tmp:0:8", ["const:687:8"]]
+ 0055f158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f158 bytes 08f11791
+ 0055f158 bytes 081d1a91
- 0055f15c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055f15c bytes 89eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4b296a18e0bfd8f747667245149f76"></a>

### [`0055f2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2c0.md) → [`0055f2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2c0.md) FUN_0055f2c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md)

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
      "definition_site": "0055f2c8",
      "incomplete_value": false,
      "site": "0055f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2c8",
      "incomplete_value": false,
      "site": "0055f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "0055f2c8",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f2c8",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2c0.md#insn-0055f2c4)
- 新版 [`0055f2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2c0.md#insn-0055f2c4)

~~~diff
- 0055f2c4 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0055f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 0055f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 bytes 08411b91
+ 0055f2c4 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b06f6a3b62d29fd215f41c24453e5c4"></a>

### [`0055f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2d0.md) → [`0055f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md) FUN_0055f2d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055f2e8",
      "incomplete_value": false,
      "site": "0055f2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2e8",
      "incomplete_value": false,
      "site": "0055f2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "0055f2e8",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f2e8",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2d0.md#insn-0055f2e0)
- 新版 [`0055f2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md#insn-0055f2e0)

~~~diff
- 0055f2e0 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 0055f2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 0055f2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 bytes 08411b91
+ 0055f2e0 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b1073a17d73bbf3e4982c92f39d1e75"></a>

### [`0055f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md) → [`0055f300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md) FUN_0055f300

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566df0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md)

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
      "definition_site": "0055f3dc",
      "incomplete_value": false,
      "site": "0055f3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f3dc",
      "incomplete_value": false,
      "site": "0055f3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055f3e8",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f3e8",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md#insn-0055f3dc)
- 新版 [`0055f3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md#insn-0055f3dc)

~~~diff
- 0055f3dc ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc bytes 08011491
+ 0055f3dc bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c3e908414c01e94fff2deb19fe518cf"></a>

### [`0055f488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f488.md) → [`0055f488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md) FUN_0055f488

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566e98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f56c",
      "incomplete_value": false,
      "site": "0055f578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f56c",
      "incomplete_value": false,
      "site": "0055f578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055f578",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f578",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f488.md#insn-0055f56c)
- 新版 [`0055f56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md#insn-0055f56c)

~~~diff
- 0055f56c ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055f56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055f56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f56c bytes 08011491
+ 0055f56c bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5dce051684815062716f3adfcb31422"></a>

### [`0055f61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f61c.md) → [`0055f61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md) FUN_0055f61c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566e98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f6ec",
      "incomplete_value": false,
      "site": "0055f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f6ec",
      "incomplete_value": false,
      "site": "0055f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055f6f8",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f6f8",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f61c.md#insn-0055f6ec)
- 新版 [`0055f6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md#insn-0055f6ec)

~~~diff
- 0055f6ec ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055f6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055f6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec bytes 08011491
+ 0055f6ec bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf407c0e84dda4a7a9acb841880aca7"></a>

### [`0055f798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f798.md) → [`0055f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md) FUN_0055f798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0055f828",
      "incomplete_value": false,
      "site": "0055f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f828",
      "incomplete_value": false,
      "site": "0055f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0055f834",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f834",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f798.md#insn-0055f828)
- 新版 [`0055f828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md#insn-0055f828)

~~~diff
- 0055f828 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0055f828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055f828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f828 bytes 08011491
+ 0055f828 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e999d9582f6c72c97315050bde3a2c"></a>

### [`0055f8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8a0.md) → [`0055f8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8a0.md) FUN_0055f8a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055f8b0",
      "incomplete_value": false,
      "site": "0055f8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f8b0",
      "incomplete_value": false,
      "site": "0055f8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0055f8b8",
      "DATA",
      [
        "storage",
        "00bef738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f8b8",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8a0.md#insn-0055f8b0)
- 新版 [`0055f8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8a0.md#insn-0055f8b0)

~~~diff
- 0055f8b0 ["COPY", "tmp:0:8", ["const:738:8"]]
- 0055f8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0055f8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 bytes 08e11c91
+ 0055f8b0 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca6d7fc23523bbb4ccc0831f3c8974d"></a>

### [`0055f8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8e0.md) → [`0055f8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md) FUN_0055f8e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055eb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eb5c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf50.md)
- 新版 呼出元 1件 [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f910",
      "incomplete_value": false,
      "site": "0055f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f910",
      "incomplete_value": false,
      "site": "0055f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0055f910",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f910",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8e0.md#insn-0055f900)
- 新版 [`0055f900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md#insn-0055f900)

~~~diff
- 0055f900 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0055f900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0055f900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f900 bytes 29211e91
+ 0055f900 bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da007fdeae51d284db43b1653fe60ab5"></a>

### [`0055fa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fa98.md) → [`0055fa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fa98.md) FUN_0055fa98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055faa8",
      "incomplete_value": false,
      "site": "0055faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055faa8",
      "incomplete_value": false,
      "site": "0055faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0055faa8",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055faa8",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055faa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fa98.md#insn-0055faa4)
- 新版 [`0055faa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fa98.md#insn-0055faa4)

~~~diff
- 0055faa4 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0055faa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0055faa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 bytes 29211e91
+ 0055faa4 bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed4e80df6f70329a6d14d226e62aa3e"></a>

### [`0055fac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fac0.md) → [`0055fac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md) FUN_0055fac0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055facc",
      "incomplete_value": false,
      "site": "0055facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055facc",
      "incomplete_value": false,
      "site": "0055facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0055facc",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055facc",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fac0.md#insn-0055fac8)
- 新版 [`0055fac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md#insn-0055fac8)

~~~diff
- 0055fac8 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0055fac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0055fac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 bytes 29211e91
+ 0055fac8 bytes 29611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4528288c208ffa9ccf618e1f0dfc299"></a>

### [`0055fdb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdb8.md) → [`0055fdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fdb8.md) FUN_0055fdb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0055fdbc",
      "incomplete_value": false,
      "site": "0055fdc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fdbc",
      "incomplete_value": false,
      "site": "0055fdc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0055fdc0",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055fdc0",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdb8.md#insn-0055fdbc)
- 新版 [`0055fdbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fdb8.md#insn-0055fdbc)

~~~diff
- 0055fdbc ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0055fdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0055fdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc bytes 08811f91
+ 0055fdbc bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab56294973404ecb571f90673bb90f6c"></a>

### [`0055fdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdc8.md) → [`0055fdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fdc8.md) FUN_0055fdc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0055fdd8",
      "incomplete_value": false,
      "site": "0055fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fdd8",
      "incomplete_value": false,
      "site": "0055fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0055fde0",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055fde0",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdc8.md#insn-0055fdd8)
- 新版 [`0055fdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fdc8.md#insn-0055fdd8)

~~~diff
- 0055fdd8 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 0055fdd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0055fdd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 bytes 08811f91
+ 0055fdd8 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd807137eb5e1ef0c6da9ac3961057c1"></a>

### [`0055fe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md) → [`0055fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md) FUN_0055fe08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ebd0.md) · 呼出先 4件 [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbff0.md)
- 新版 呼出元 1件 [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) · 呼出先 4件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055fe40",
      "incomplete_value": false,
      "site": "0055fe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe40",
      "incomplete_value": false,
      "site": "0055fe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "definition_site": "0055fe70",
      "incomplete_value": true,
      "site": "0055fe70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe70",
      "incomplete_value": true,
      "site": "0055fe70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0b:8"
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
      "definition_site": "0055ff2c",
      "incomplete_value": true,
      "site": "0055ff2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:95c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ff2c",
      "incomplete_value": true,
      "site": "0055ff2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e9:8"
              ]
            ]
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
      "0055fe40",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ],
    [
      "0055fe60",
      "READ",
      [
        "storage",
        "00297d0b",
        null,
        "string"
      ]
    ],
    [
      "0055ff18",
      "READ",
      [
        "storage",
        "002929e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055fe40",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ],
    [
      "0055fe60",
      "READ",
      [
        "storage",
        "00297c7e",
        null,
        "string"
      ]
    ],
    [
      "0055ff18",
      "READ",
      [
        "storage",
        "0029295c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fe34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md#insn-0055fe34) · [`0055fe58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md#insn-0055fe58) · [`0055ff10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md#insn-0055ff10)
- 新版 [`0055fe34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055fe34) · [`0055fe58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055fe58) · [`0055ff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055ff10)

~~~diff
- 0055fe34 ["COPY", "tmp:0:8", ["const:830:8"]]
- 0055fe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0055fe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 bytes 29c12091
+ 0055fe34 bytes 29012291
- 0055fe58 ["COPY", "tmp:0:8", ["const:d0b:8"]]
- 0055fe58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["COPY", "tmp:0:8", ["const:c7e:8"]]
+ 0055fe58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 bytes 292d3491
+ 0055fe58 bytes 29f93191
- 0055ff10 ["COPY", "tmp:0:8", ["const:9e9:8"]]
- 0055ff10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["COPY", "tmp:0:8", ["const:95c:8"]]
+ 0055ff10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 bytes 29a52791
+ 0055ff10 bytes 29712591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-687209d06190e64024479a1ee41b05c2"></a>

### [`00560124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560124.md) → [`00560124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560124.md) FUN_00560124

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560134",
      "incomplete_value": false,
      "site": "00560134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560134",
      "incomplete_value": false,
      "site": "00560134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "00560134",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560134",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560124.md#insn-00560130)
- 新版 [`00560130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560124.md#insn-00560130)

~~~diff
- 00560130 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00560130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00560130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560130 bytes 29c12091
+ 00560130 bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6406eacf12ecccbd7558a69b13bc2fff"></a>

### [`0056014c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/0056014c.md) → [`0056014c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md) FUN_0056014c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00560158",
      "incomplete_value": false,
      "site": "00560158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560158",
      "incomplete_value": false,
      "site": "00560158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "00560158",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560158",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/0056014c.md#insn-00560154)
- 新版 [`00560154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md#insn-00560154)

~~~diff
- 00560154 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00560154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00560154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560154 bytes 29c12091
+ 00560154 bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861606ea338f8907ec7d520a59eb5f2a"></a>

### [`005605e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005605e0.md) → [`005605e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md) FUN_005605e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00560748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560748.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00560748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560600",
      "incomplete_value": false,
      "site": "00560600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560600",
      "incomplete_value": false,
      "site": "00560600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "00560600",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00560600",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005605f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005605e0.md#insn-005605f8)
- 新版 [`005605f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md#insn-005605f8)

~~~diff
- 005605f8 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 005605f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005605f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005605f8 bytes 08e12291
+ 005605f8 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053605d094b84dbef70f736ec6ff01a4"></a>

### [`00560748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560748.md) → [`00560748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md) FUN_00560748

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee58.md) · 呼出先 2件 [`005605e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005605e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0053ee58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee58.md) · 呼出先 2件 [`005605e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560784",
      "incomplete_value": false,
      "site": "00560790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560784",
      "incomplete_value": false,
      "site": "00560790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "00560790",
      "DATA",
      [
        "storage",
        "00bef9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560790",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560748.md#insn-00560784)
- 新版 [`00560784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md#insn-00560784)

~~~diff
- 00560784 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00560784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00560784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560784 bytes 08e12791
+ 00560784 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7261b541f5f99074f80c2ab2c0ed0a"></a>

### [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) → [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) FUN_005609d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005609cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609cc.md) [`00561a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md) · 呼出先 25件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) [`00564250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564250.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)
- 新版 呼出元 2件 [`005609cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609cc.md) [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 25件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) [`00564250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.13% / 新版 95.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "00560a80",
      "incomplete_value": true,
      "site": "00560a80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560a80",
      "incomplete_value": true,
      "site": "00560a80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:5d:8"
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
      "00560a2c",
      "READ",
      [
        "storage",
        "0029d5ba",
        null,
        "string"
      ]
    ],
    [
      "00560a34",
      "READ",
      [
        "storage",
        "0029d5c0",
        null,
        "string"
      ]
    ],
    [
      "00560a68",
      "READ",
      [
        "storage",
        "00294a86",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00560a2c",
      "READ",
      [
        "storage",
        "0029d645",
        null,
        "string"
      ]
    ],
    [
      "00560a34",
      "READ",
      [
        "storage",
        "0029d64b",
        null,
        "string"
      ]
    ],
    [
      "00560a68",
      "READ",
      [
        "storage",
        "002949f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md#insn-00560a28) · [`00560a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md#insn-00560a64) · [`00560b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md#insn-00560b48)
- 新版 [`00560a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560a28) · [`00560a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560a64) · [`00560b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560b48)

~~~diff
- 00560a28 ["COPY", "tmp:0:8", ["const:5ba:8"]]
- 00560a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["COPY", "tmp:0:8", ["const:645:8"]]
+ 00560a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560a28 bytes 29e91691
+ 00560a28 bytes 29151991
- 00560a64 ["COPY", "tmp:0:8", ["const:a46:8"]]
- 00560a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["COPY", "tmp:0:8", ["const:9b9:8"]]
+ 00560a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560a64 bytes 08192991
+ 00560a64 bytes 08e52691
- 00560b48 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00560b48 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00560b48 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 bytes 39032791
+ 00560b48 bytes 39432891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308a66251f599e46f6a375ed7c859ce3"></a>

### [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) → [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) FUN_00560f00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561074",
      "incomplete_value": false,
      "site": "0056107c",
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
            "const:774:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561074",
      "incomplete_value": false,
      "site": "0056107c",
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
            "const:6e9:8"
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
      "definition_site": "005610d8",
      "incomplete_value": false,
      "site": "005610e0",
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
            "const:743:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005610d8",
      "incomplete_value": false,
      "site": "005610e0",
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
            "const:6b8:8"
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
      "00561074",
      "PARAM",
      [
        "storage",
        "002a06e9",
        null,
        "string"
      ]
    ],
    [
      "005610d8",
      "PARAM",
      [
        "storage",
        "0029c6b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00561074",
      "PARAM",
      [
        "storage",
        "002a0774",
        null,
        "string"
      ]
    ],
    [
      "005610d8",
      "PARAM",
      [
        "storage",
        "0029c743",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md#insn-00561074) · [`005610d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md#insn-005610d8)
- 新版 [`00561074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md#insn-00561074) · [`005610d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md#insn-005610d8)

~~~diff
- 00561074 ["COPY", "tmp:0:8", ["const:6e9:8"]]
- 00561074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00561074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00561074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["COPY", "tmp:0:8", ["const:774:8"]]
+ 00561074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00561074 bytes 21a41b91
+ 00561074 bytes 21d01d91
- 005610d8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 005610d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005610d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005610d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["COPY", "tmp:0:8", ["const:743:8"]]
+ 005610d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005610d8 bytes 21e01a91
+ 005610d8 bytes 210c1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2824e124eb134e3c65c80cf2d1cf26e"></a>

### [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) → [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) FUN_005612d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005612cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612cc.md) · 呼出先 27件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) [`00563938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563938.md) [`00563a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563a9c.md) [`00564374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564374.md)
- 新版 呼出元 1件 [`005612cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612cc.md) · 呼出先 27件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) [`00563938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md) [`00563a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md) [`00564374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.61% / 新版 97.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561648",
      "incomplete_value": false,
      "site": "00561658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561648",
      "incomplete_value": false,
      "site": "00561658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00561338",
      "READ",
      [
        "storage",
        "0029d5ba",
        null,
        "string"
      ]
    ],
    [
      "00561340",
      "READ",
      [
        "storage",
        "0029d5c0",
        null,
        "string"
      ]
    ],
    [
      "00561368",
      "READ",
      [
        "storage",
        "00294a86",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561338",
      "READ",
      [
        "storage",
        "0029d645",
        null,
        "string"
      ]
    ],
    [
      "00561340",
      "READ",
      [
        "storage",
        "0029d64b",
        null,
        "string"
      ]
    ],
    [
      "00561368",
      "READ",
      [
        "storage",
        "002949f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md#insn-00561334) · [`00561360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md#insn-00561360) · [`00561364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md#insn-00561364)
- 新版 [`00561334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md#insn-00561334) · [`00561360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md#insn-00561360)

~~~diff
- 00561334 ["COPY", "tmp:0:8", ["const:5ba:8"]]
- 00561334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00561334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00561334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["COPY", "tmp:0:8", ["const:645:8"]]
+ 00561334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00561334 bytes 29e91691
+ 00561334 bytes 29151991
- 00561360 ["COPY", "tmp:0:8", ["const:a46:8"]]
- 00561360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["COPY", "tmp:0:8", ["const:9b9:8"]]
+ 00561360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561360 bytes 08192991
+ 00561360 bytes 08e52691
- 00561364 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00561364 bytes 89eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22e982db8ca5d7b248c811a0c3eff3f"></a>

### [`00561a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md) → [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) FUN_00561a60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`00564590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564590.md) [`005645f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005645f0.md) [`00564974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564974.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`00564590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564590.md) [`005645f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md) [`00564974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564974.md)

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
      "definition_site": "00561aa4",
      "incomplete_value": false,
      "site": "00561aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561aa4",
      "incomplete_value": false,
      "site": "00561aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "definition_site": "00561ad0",
      "incomplete_value": false,
      "site": "00561ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561ad0",
      "incomplete_value": false,
      "site": "00561ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "00561b40",
      "incomplete_value": false,
      "site": "00561b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b40",
      "incomplete_value": false,
      "site": "00561b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00561aac",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ],
    [
      "00561ad8",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ],
    [
      "00561b40",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561aac",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ],
    [
      "00561ad8",
      "DATA",
      [
        "storage",
        "00befae8",
        null,
        "pointer"
      ]
    ],
    [
      "00561b40",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md#insn-00561aa4) · [`00561ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md#insn-00561ad0) · [`00561b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md#insn-00561b38)
- 新版 [`00561aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561aa4) · [`00561ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561ad0) · [`00561b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561b38)

~~~diff
- 00561aa4 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00561aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00561aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 bytes 08212991
+ 00561aa4 bytes 08612a91
- 00561ad0 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00561ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00561ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 bytes 08612a91
+ 00561ad0 bytes 08a12b91
- 00561b38 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00561b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00561b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561b38 bytes 08812b91
+ 00561b38 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267197d60ef9b68a3edaae21769bc5ce"></a>

### [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) → [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) FUN_005624f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`005636f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/005636f4.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`0056503c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md) [`0056508c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md) [`0056521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056521c.md)
- 新版 呼出元 2件 [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`005636f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005636f4.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0056503c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md) [`0056508c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md) [`0056521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00562720",
      "incomplete_value": true,
      "site": "00562720",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562720",
      "incomplete_value": true,
      "site": "00562720",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00562524",
      "incomplete_value": true,
      "site": "00562524",
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
      "definition_site": "00562524",
      "incomplete_value": true,
      "site": "00562524",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "005625b4",
      "incomplete_value": true,
      "site": "005625b4",
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
      "definition_site": "005625b4",
      "incomplete_value": true,
      "site": "005625b4",
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
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00562520",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "00562568",
      "READ",
      [
        "storage",
        "00c264f0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056258c",
      "PARAM",
      [
        "storage",
        "00c26438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00562520",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "00562568",
      "READ",
      [
        "storage",
        "00c26530",
        null,
        "undefined8"
      ]
    ],
    [
      "0056258c",
      "PARAM",
      [
        "storage",
        "00c26478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md#insn-00562720) · [`0056251c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md#insn-0056251c) · [`0056252c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md#insn-0056252c)
- 新版 [`00562720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-00562720) · [`0056251c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-0056251c) · [`0056252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-0056252c)

~~~diff
- 00562720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
- 00562720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00562720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
+ 00562720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562720 bytes 281102f9
+ 00562720 bytes 283102f9
- 0056251c ["COPY", "tmp:0:8", ["const:440:8"]]
- 0056251c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056251c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056251c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0056251c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056251c bytes 08011191
+ 0056251c bytes 08011291
- 0056252c ["COPY", "tmp:0:8", ["const:440:8"]]
- 0056252c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056252c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056252c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0056252c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056252c bytes 73021191
+ 0056252c bytes 73021291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f114d35dd3632572e9b36afe6d3baa8"></a>

### [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) → [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef38.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef38.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件, `store_condition` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00562950",
      "incomplete_value": false,
      "site": "0056295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562950",
      "incomplete_value": false,
      "site": "0056295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00562cf0",
      "incomplete_value": true,
      "site": "00562cf0",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562cf0",
      "incomplete_value": true,
      "site": "00562cf0",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056283c",
      "incomplete_value": true,
      "site": "0056283c",
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
      "definition_site": "0056283c",
      "incomplete_value": true,
      "site": "0056283c",
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
      "00562834",
      "READ",
      [
        "storage",
        "00c26428",
        null,
        "undefined8"
      ]
    ],
    [
      "00562880",
      "READ",
      [
        "storage",
        "00c26478",
        null,
        "undefined8"
      ]
    ],
    [
      "0056295c",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00562834",
      "READ",
      [
        "storage",
        "00c26468",
        null,
        "undefined8"
      ]
    ],
    [
      "00562880",
      "READ",
      [
        "storage",
        "00c264b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056295c",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md#insn-00562cf0) · [`00562818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md#insn-00562818) · [`00562844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md#insn-00562844)
- 新版 [`00562cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562cf0) · [`00562818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562818) · [`00562844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562844)

~~~diff
- 00562cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
- 00562cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00562cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
+ 00562cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562cf0 bytes 281102f9
+ 00562cf0 bytes 283102f9
- 00562818 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00562818 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00562818 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00562818 bytes 5aa31091
+ 00562818 bytes 5aa31191
- 00562844 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00562844 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00562844 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00562844 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00562844 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00562844 bytes 73a21091
+ 00562844 bytes 73a21191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ddf66ebd429cbdc1a594e3443fb2b64"></a>

### [`00563038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md) → [`00563038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00562e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562e78.md) [`0056547c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00562e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md) [`0056547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056306c",
      "incomplete_value": true,
      "site": "0056306c",
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
      "definition_site": "0056306c",
      "incomplete_value": true,
      "site": "0056306c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "00563184",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "00563184",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00563184"
      ],
      [
        "FALL_THROUGH",
        "00563184"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "005631a4",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "005631a4",
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
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00563064",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "005630c0",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ],
    [
      "0056317c",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00563064",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "005630c0",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ],
    [
      "0056317c",
      "READ",
      [
        "storage",
        "00c26420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md#insn-00563060) · [`00563074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md#insn-00563074) · [`0056317c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md#insn-0056317c)
- 新版 [`00563060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-00563060) · [`00563074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-00563074) · [`0056317c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-0056317c)

~~~diff
- 00563060 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00563060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00563060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563060 bytes 08011191
+ 00563060 bytes 08011291
- 00563074 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00563074 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00563074 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00563074 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00563074 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00563074 bytes d6021191
+ 00563074 bytes d6021291
- 0056317c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
- 0056317c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056317c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 0056317c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056317c bytes 00f141f9
+ 0056317c bytes 001142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8d5345a13e959b2c3fb5b6c4acc5332"></a>

### [`0056340c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md) → [`0056340c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef38.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef38.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056343c",
      "incomplete_value": true,
      "site": "0056343c",
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
      "definition_site": "0056343c",
      "incomplete_value": true,
      "site": "0056343c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056357c",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056357c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "0056357c"
      ],
      [
        "FALL_THROUGH",
        "0056357c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056359c",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056359c",
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
      "00563438",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "00563490",
      "READ",
      [
        "storage",
        "00c264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005634c0",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00563438",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "00563490",
      "READ",
      [
        "storage",
        "00c26500",
        null,
        "undefined8"
      ]
    ],
    [
      "005634c0",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md#insn-00563434) · [`00563444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md#insn-00563444) · [`005634b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md#insn-005634b4)
- 新版 [`00563434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-00563434) · [`00563444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-00563444) · [`005634b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-005634b4)

~~~diff
- 00563434 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00563434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00563434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563434 bytes 08011191
+ 00563434 bytes 08011291
- 00563444 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00563444 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00563444 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00563444 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00563444 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00563444 bytes 18031191
+ 00563444 bytes 18031291
- 005634b4 ["COPY", "tmp:0:8", ["const:500:8"]]
- 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005634b4 bytes 08011491
+ 005634b4 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce9cc7a1f31f0bb4680e94969cf9234c"></a>

### [`00563704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563704.md) → [`00563704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md) FUN_00563704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00563804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563804.md) · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00563804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563804.md) · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00563720",
      "incomplete_value": false,
      "site": "00563724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563720",
      "incomplete_value": false,
      "site": "00563724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00563724",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563724",
      "DATA",
      [
        "storage",
        "00bef928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563704.md#insn-00563720)
- 新版 [`00563720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md#insn-00563720)

~~~diff
- 00563720 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00563720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00563720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563720 bytes 08612391
+ 00563720 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e06cd25978d090a9e7e2f940b5583aca"></a>

### [`00563828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563828.md) → [`00563828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md) FUN_00563828

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "00563844",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00563844",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563828.md#insn-00563840)
- 新版 [`00563840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md#insn-00563840)

~~~diff
- 00563840 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00563840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00563840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563840 bytes 29e12291
+ 00563840 bytes 29212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e7c28e13cd2835aa6cfa0b1f1eb3933"></a>

### [`005638b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/005638b0.md) → [`005638b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md) FUN_005638b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "005638cc",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005638cc",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005638c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/005638b0.md#insn-005638c8)
- 新版 [`005638c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md#insn-005638c8)

~~~diff
- 005638c8 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 005638c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005638c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005638c8 bytes 29e12291
+ 005638c8 bytes 29212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f893f18c5c24580ece5b43e6d322e117"></a>

### [`00564200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564200.md) → [`00564200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564200.md) FUN_00564200

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00564204",
      "incomplete_value": false,
      "site": "00564208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564204",
      "incomplete_value": false,
      "site": "00564208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "00564208",
      "DATA",
      [
        "storage",
        "00bef9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564208",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564200.md#insn-00564204)
- 新版 [`00564204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564200.md#insn-00564204)

~~~diff
- 00564204 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00564204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00564204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564204 bytes 08e12791
+ 00564204 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fccd3a09dd398e7ecb89648bfb5bf7e"></a>

### [`00564550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564550.md) → [`00564550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564550.md) FUN_00564550

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00564554",
      "incomplete_value": false,
      "site": "00564558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564554",
      "incomplete_value": false,
      "site": "00564558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00564558",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00564558",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564550.md#insn-00564554)
- 新版 [`00564554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564550.md#insn-00564554)

~~~diff
- 00564554 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00564554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00564554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564554 bytes 08212991
+ 00564554 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d7f5e047ba48c7304c7a76a0973793"></a>

### [`00564560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564560.md) → [`00564560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564560.md) FUN_00564560

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00564570",
      "incomplete_value": false,
      "site": "00564578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564570",
      "incomplete_value": false,
      "site": "00564578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00564578",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00564578",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564560.md#insn-00564570)
- 新版 [`00564570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564560.md#insn-00564570)

~~~diff
- 00564570 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00564570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00564570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564570 bytes 08212991
+ 00564570 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33c4094f0d241a0da7fa3db3e3c1b4b8"></a>

### [`0056459c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/0056459c.md) → [`0056459c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056459c.md) FUN_0056459c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "005645c0",
      "incomplete_value": true,
      "site": "005645c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005645c0",
      "incomplete_value": true,
      "site": "005645c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005645b4",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005645b4",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
      "DATA",
      [
        "storage",
        "00c12f30",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005645b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/0056459c.md#insn-005645b4)
- 新版 [`005645b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056459c.md#insn-005645b4)

~~~diff
- 005645b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 005645b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005645b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 005645b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005645b4 bytes 080947f9
+ 005645b4 bytes 083147f9
~~~


<a id="compare-21ddda4f6312095ef983a37f3d5ac95e"></a>

### [`00564710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564710.md) → [`00564710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md) FUN_00564710

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564590.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`00564590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564590.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

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
      "definition_site": "005647b4",
      "incomplete_value": true,
      "site": "005647b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005647b4",
      "incomplete_value": true,
      "site": "005647b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00564790",
      "incomplete_value": true,
      "site": "00564798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564790",
      "incomplete_value": true,
      "site": "00564798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00564790",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00564790",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005647b0",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00564790",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "00564790",
      "PARAM",
      [
        "storage",
        "00c12f08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005647b0",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564710.md#insn-00564790) · [`005647b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564710.md#insn-005647b0)
- 新版 [`00564790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md#insn-00564790) · [`005647b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md#insn-005647b0)

~~~diff
- 00564790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 00564790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00564790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e68:8"]]
+ 00564790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00564790 bytes 210c47f9
+ 00564790 bytes 213447f9
- 005647b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
- 005647b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005647b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005647b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005647b0 bytes 081147f9
+ 005647b0 bytes 083947f9
~~~


<a id="compare-be8c4d4129c2de20b60d7560e92221d2"></a>

### [`00564838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564838.md) → [`00564838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md) FUN_00564838

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0056484c",
      "incomplete_value": false,
      "site": "00564850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056484c",
      "incomplete_value": false,
      "site": "00564850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00564850",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564850",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056484c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564838.md#insn-0056484c)
- 新版 [`0056484c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md#insn-0056484c)

~~~diff
- 0056484c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0056484c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0056484c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056484c bytes 08812b91
+ 0056484c bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de3cb1ddbbb646756faa449f023d19a6"></a>

### [`00564894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564894.md) → [`00564894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md) FUN_00564894

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005648ac",
      "incomplete_value": false,
      "site": "005648b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005648ac",
      "incomplete_value": false,
      "site": "005648b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "005648b0",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005648b0",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005648ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564894.md#insn-005648ac)
- 新版 [`005648ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md#insn-005648ac)

~~~diff
- 005648ac ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 005648ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 005648ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005648ac bytes 08812b91
+ 005648ac bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf8d7947410ecb1ee8a8e91d3f7f511"></a>

### [`005648f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005648f0.md) → [`005648f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md) FUN_005648f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00564914",
      "incomplete_value": false,
      "site": "00564914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564914",
      "incomplete_value": false,
      "site": "00564914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00564914",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564914",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005648f0.md#insn-00564910)
- 新版 [`00564910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md#insn-00564910)

~~~diff
- 00564910 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00564910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00564910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564910 bytes 29812b91
+ 00564910 bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75145e168c76ab5e771a9a0d77c4774a"></a>

### [`00564940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564940.md) → [`00564940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md) FUN_00564940

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "0056494c",
      "incomplete_value": false,
      "site": "0056494c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056494c",
      "incomplete_value": false,
      "site": "0056494c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0056494c",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056494c",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564940.md#insn-00564948)
- 新版 [`00564948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md#insn-00564948)

~~~diff
- 00564948 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00564948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00564948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564948 bytes 29812b91
+ 00564948 bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2653120ce278c4cb4f73180419ff9c8a"></a>

### [`00564ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ebc.md) → [`00564ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md) FUN_00564ebc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00564d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564d7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00564d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00564ec8",
      "incomplete_value": false,
      "site": "00564ecc",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564ec8",
      "incomplete_value": false,
      "site": "00564ecc",
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
      "00564ec8",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00564ec8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ebc.md#insn-00564ec8)
- 新版 [`00564ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md#insn-00564ec8)

~~~diff
- 00564ec8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00564ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00564ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 bytes 000c0c91
+ 00564ec8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54999f3aa04d031670c77fb50ec5c531"></a>

### [`00564ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md) → [`00564ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md) FUN_00564ed0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056244c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056244c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0056244c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00564eec",
      "incomplete_value": false,
      "site": "00564eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564eec",
      "incomplete_value": false,
      "site": "00564eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "definition_site": "00564ef8",
      "incomplete_value": false,
      "site": "00564ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564ef8",
      "incomplete_value": false,
      "site": "00564ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00564eec",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ],
    [
      "00564ef8",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564eec",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00564ef8",
      "DATA",
      [
        "storage",
        "00bef928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md#insn-00564ee4) · [`00564ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md#insn-00564ef0)
- 新版 [`00564ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md#insn-00564ee4) · [`00564ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md#insn-00564ef0)

~~~diff
- 00564ee4 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00564ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00564ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 bytes 08812d91
+ 00564ee4 bytes 08c12e91
- 00564ef0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 00564ef0 bytes 483400f0
+ 00564ef0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00564ef0 bytes 483400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f82a3218b8a5843135051f51328a381"></a>

### [`00564fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fac.md) → [`00564fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564fac.md) FUN_00564fac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00564fb0",
      "incomplete_value": false,
      "site": "00564fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fb0",
      "incomplete_value": false,
      "site": "00564fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00564fb4",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564fb4",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fac.md#insn-00564fb0)
- 新版 [`00564fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564fac.md#insn-00564fb0)

~~~diff
- 00564fb0 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00564fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00564fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 bytes 08812d91
+ 00564fb0 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33d29d627ea5a9f4d01797f89e3b070"></a>

### [`00564fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fbc.md) → [`00564fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564fbc.md) FUN_00564fbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564fcc",
      "incomplete_value": true,
      "site": "00564fd4",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fcc",
      "incomplete_value": true,
      "site": "00564fd4",
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
            "const:b60:8"
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
      "00564fd4",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564fd4",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fbc.md#insn-00564fcc)
- 新版 [`00564fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564fbc.md#insn-00564fcc)

~~~diff
- 00564fcc ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00564fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00564fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564fcc bytes 08812d91
+ 00564fcc bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ded7a9025f7ee6369f0054f01fc43b2"></a>

### [`00564ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ffc.md) → [`00564ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ffc.md) FUN_00564ffc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00565000",
      "incomplete_value": false,
      "site": "00565004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565000",
      "incomplete_value": false,
      "site": "00565004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "00565004",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565004",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ffc.md#insn-00565000)
- 新版 [`00565000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ffc.md#insn-00565000)

~~~diff
- 00565000 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00565000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00565000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565000 bytes 08c12e91
+ 00565000 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a9fbe31799a4969cd52998bd4d6f126"></a>

### [`0056500c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056500c.md) → [`0056500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056500c.md) FUN_0056500c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0056501c",
      "incomplete_value": false,
      "site": "00565024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056501c",
      "incomplete_value": false,
      "site": "00565024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00565024",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565024",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056501c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056500c.md#insn-0056501c)
- 新版 [`0056501c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056500c.md#insn-0056501c)

~~~diff
- 0056501c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0056501c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056501c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056501c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 0056501c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056501c bytes 08c12e91
+ 0056501c bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14aa99a896cd198cbd45b634906b42f"></a>

### [`0056503c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md) → [`0056503c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md) FUN_0056503c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005641a0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565050",
      "incomplete_value": false,
      "site": "00565058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565050",
      "incomplete_value": false,
      "site": "00565058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00565058",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565058",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md#insn-00565050)
- 新版 [`00565050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md#insn-00565050)

~~~diff
- 00565050 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00565050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00565050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565050 bytes 08212291
+ 00565050 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1efdeb52b924233d00b5710b7f080927"></a>

### [`0056508c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md) → [`0056508c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md) FUN_0056508c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056513c",
      "incomplete_value": false,
      "site": "00565144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056513c",
      "incomplete_value": false,
      "site": "00565144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00565144",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565144",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056513c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md#insn-0056513c)
- 新版 [`0056513c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md#insn-0056513c)

~~~diff
- 0056513c ["COPY", "tmp:0:8", ["const:888:8"]]
- 0056513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0056513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056513c bytes 29212291
+ 0056513c bytes 29612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e50c137bdfa8cda828a5d2c6dc45cc64"></a>

### [`0056547c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md) → [`0056547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md) FUN_0056547c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00563d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563d44.md)
- 新版 呼出元 2件 [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00563d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565494",
      "incomplete_value": false,
      "site": "00565498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565494",
      "incomplete_value": false,
      "site": "00565498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00565498",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ],
    [
      "005654b0",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565498",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "pointer"
      ]
    ],
    [
      "005654b0",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md#insn-00565494) · [`005654a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md#insn-005654a0)
- 新版 [`00565494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md#insn-00565494) · [`005654a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md#insn-005654a0)

~~~diff
- 00565494 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00565494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00565494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565494 bytes 29c12e91
+ 00565494 bytes 29013091
- 005654a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 005654a0 bytes 483400d0
+ 005654a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005654a0 bytes 483400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc615c12285711a7cf9fdf970d87af2b"></a>

### [`0056554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056554c.md) → [`0056554c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md) _INIT_32

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) [`00560474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560474.md) [`005604a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604a4.md) [`005604ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604ac.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00560444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560444.md) [`00560474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560474.md) [`005604a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604a4.md) [`005604ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604ac.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件, `store_value` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565574",
      "incomplete_value": false,
      "site": "00565574",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:400:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565574",
      "incomplete_value": false,
      "site": "00565574",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565590",
      "incomplete_value": false,
      "site": "00565590",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:430:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565590",
      "incomplete_value": false,
      "site": "00565590",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005655b0",
      "incomplete_value": false,
      "site": "005655b0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:460:8"
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
      "definition_site": "005655b0",
      "incomplete_value": false,
      "site": "005655b0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
      "00565564",
      "PARAM",
      [
        "storage",
        "00c263c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0056556c",
      "PARAM",
      [
        "storage",
        "00560444",
        null,
        null
      ]
    ],
    [
      "00565570",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565564",
      "PARAM",
      [
        "storage",
        "00c26400",
        null,
        "undefined8"
      ]
    ],
    [
      "0056556c",
      "PARAM",
      [
        "storage",
        "00560444",
        null,
        null
      ]
    ],
    [
      "00565570",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056554c.md#insn-00565578) · [`00565594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056554c.md#insn-00565594)
- 新版 [`00565578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md#insn-00565578)

~~~diff
- 00565578 ["INT_ADD", "register:40f0:8", ["const:565578:8", "const:4:8"]]
- 00565578 ["CALL", null, ["callee:00bdafe0:8"]]
- 00565578 bytes 86d61994
+ 00565578 ["INT_ADD", "register:40f0:8", ["const:565578:8", "const:4:8"]]
+ 00565578 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00565578 bytes 9ad61994
- 00565594 ["INT_ADD", "register:40f0:8", ["const:565594:8", "const:4:8"]]
- 00565594 ["CALL", null, ["callee:00bdafe0:8"]]
- 00565594 bytes 7fd61994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2236f234550af442cad6b9b97722f7a"></a>

### [`005655f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005655f0.md) → [`005655f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md) FUN_005655f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574724.md) · 呼出先 2件 [`00571a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a60.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00574724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574724.md) · 呼出先 2件 [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565628",
      "incomplete_value": false,
      "site": "00565634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565628",
      "incomplete_value": false,
      "site": "00565634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "00565634",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565634",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005655f0.md#insn-00565628)
- 新版 [`00565628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md#insn-00565628)

~~~diff
- 00565628 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00565628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00565628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565628 bytes 08013091
+ 00565628 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77fd62f80b13a1f201ab7999515cf3d1"></a>

### [`00565684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565684.md) → [`00565684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565684.md) FUN_00565684

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00565688",
      "incomplete_value": false,
      "site": "0056568c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565688",
      "incomplete_value": false,
      "site": "0056568c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "0056568c",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056568c",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565684.md#insn-00565688)
- 新版 [`00565688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565684.md#insn-00565688)

~~~diff
- 00565688 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00565688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00565688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565688 bytes 08013091
+ 00565688 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4d3014ee59919089f4bdb0dc75cfa1"></a>

### [`00565694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565694.md) → [`00565694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565694.md) FUN_00565694

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005656a4",
      "incomplete_value": false,
      "site": "005656ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005656a4",
      "incomplete_value": false,
      "site": "005656ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "005656ac",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005656ac",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005656a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565694.md#insn-005656a4)
- 新版 [`005656a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565694.md#insn-005656a4)

~~~diff
- 005656a4 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 005656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 005656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005656a4 bytes 08013091
+ 005656a4 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ee879f0f91c79ec3bbfa18529901d78"></a>

### [`00565720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md) → [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) FUN_00565720

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00565ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ce8.md) · 呼出先 7件 [`00565e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565e14.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00565ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md) · 呼出先 7件 [`00565e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565750",
      "incomplete_value": false,
      "site": "00565764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565750",
      "incomplete_value": false,
      "site": "00565764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00565764",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ],
    [
      "00565834",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565764",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00565834",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md#insn-00565750) · [`00565828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md#insn-00565828)
- 新版 [`00565750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md#insn-00565750) · [`00565828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md#insn-00565828)

~~~diff
- 00565750 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00565750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00565750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565750 bytes 08413191
+ 00565750 bytes 08813291
- 00565828 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00565828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00565828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565828 bytes 08410991
+ 00565828 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2585dd52f106272764dc2389fe7ffaa"></a>

### [`00565908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565908.md) → [`00565908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md) FUN_00565908

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0056591c",
      "incomplete_value": false,
      "site": "00565920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056591c",
      "incomplete_value": false,
      "site": "00565920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00565920",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565920",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056591c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565908.md#insn-0056591c)
- 新版 [`0056591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md#insn-0056591c)

~~~diff
- 0056591c ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0056591c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0056591c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056591c bytes 08413191
+ 0056591c bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

