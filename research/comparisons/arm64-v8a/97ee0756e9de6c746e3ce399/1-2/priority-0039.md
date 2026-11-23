# v15.7.3 → v15.7.4 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-ad9138d72a965a5463b6ed93793d6114"></a>

### [`00804620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/00804620.md) → [`00804620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804620.md) FUN_00804620

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080446c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080446c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0080446c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/0080446c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0080462c",
      "incomplete_value": false,
      "site": "00804630",
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
      "definition_site": "0080462c",
      "incomplete_value": false,
      "site": "00804630",
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
      "0080462c",
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
      "0080462c",
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

- 旧版 [`0080462c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/00804620.md#insn-0080462c)
- 新版 `0080462c`（命令位置の公開資料なし）

~~~diff
- 0080462c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0080462c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0080462c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0080462c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0080462c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0080462c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0080462c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0080462c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0080462c bytes 000c0c91
+ 0080462c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e5d5e2055a6d41c04dce7dadffe55e2"></a>

### [`00805f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md) → [`00805f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00805/00805f2c.md) FUN_00805f2c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007f99cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f99cc.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00830c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)
- 新版 呼出元 1件 [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00830c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `store_destination` 7件, `store_value` 16件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00805f6c",
      "incomplete_value": false,
      "site": "00805f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00805f6c",
      "incomplete_value": false,
      "site": "00805f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "definition_site": "00805fb0",
      "incomplete_value": true,
      "site": "00805fb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00805fb0",
      "incomplete_value": true,
      "site": "00805fb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00806258",
      "incomplete_value": true,
      "site": "00806258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00806258",
      "incomplete_value": true,
      "site": "00806258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00805f70",
      "DATA",
      [
        "storage",
        "00c00cb0",
        null,
        "pointer"
      ]
    ],
    [
      "00805f80",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00805fa0",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00805f70",
      "DATA",
      [
        "storage",
        "00c00d00",
        null,
        "pointer"
      ]
    ],
    [
      "00805f80",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00805fa0",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00805f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md#insn-00805f6c) · [`00805f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md#insn-00805f74)
- 新版 `00805f6c`（命令位置の公開資料なし） · `00805f74`（命令位置の公開資料なし）

~~~diff
- 00805f6c ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00805f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00805f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00805f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00805f6c ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00805f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00805f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00805f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00805f6c bytes 08c13291
+ 00805f6c bytes 08013491
- 00805f74 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 00805f74 bytes 18210090
+ 00805f74 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 00805f74 bytes 18210090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd918317e1666b1d4d105ed06c10e09"></a>

### [`00806edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806edc.md) → [`00806edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00806/00806edc.md) FUN_00806edc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00806f60",
      "incomplete_value": false,
      "site": "00806f64",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00806f60",
      "incomplete_value": false,
      "site": "00806f64",
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
      "00806ef8",
      "DATA",
      [
        "storage",
        "00c00cb0",
        null,
        "pointer"
      ]
    ],
    [
      "00806f64",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00806ef8",
      "DATA",
      [
        "storage",
        "00c00d00",
        null,
        "pointer"
      ]
    ],
    [
      "00806f64",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00806ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806edc.md#insn-00806ef4) · [`00806f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806edc.md#insn-00806f60)
- 新版 `00806ef4`（命令位置の公開資料なし） · `00806f60`（命令位置の公開資料なし）

~~~diff
- 00806ef4 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00806ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00806ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00806ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00806ef4 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00806ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00806ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00806ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00806ef4 bytes 08c13291
+ 00806ef4 bytes 08013491
- 00806f60 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00806f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00806f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00806f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00806f60 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00806f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00806f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00806f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00806f60 bytes 08610a91
+ 00806f60 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4b7bc74f45ef60602b921f4bb80142"></a>

### [`00806fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806fa4.md) → [`00806fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00806/00806fa4.md) FUN_00806fa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00806fbc",
      "incomplete_value": false,
      "site": "00806fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00806fbc",
      "incomplete_value": false,
      "site": "00806fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "definition_site": "00807028",
      "incomplete_value": false,
      "site": "0080702c",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807028",
      "incomplete_value": false,
      "site": "0080702c",
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
      "00806fc0",
      "DATA",
      [
        "storage",
        "00c00cb0",
        null,
        "pointer"
      ]
    ],
    [
      "0080702c",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00806fc0",
      "DATA",
      [
        "storage",
        "00c00d00",
        null,
        "pointer"
      ]
    ],
    [
      "0080702c",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00806fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806fa4.md#insn-00806fbc) · [`00807028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00806/00806fa4.md#insn-00807028)
- 新版 `00806fbc`（命令位置の公開資料なし） · `00807028`（命令位置の公開資料なし）

~~~diff
- 00806fbc ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00806fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00806fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00806fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00806fbc ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00806fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00806fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00806fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00806fbc bytes 08c13291
+ 00806fbc bytes 08013491
- 00807028 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00807028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00807028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00807028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00807028 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00807028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00807028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00807028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00807028 bytes 08610a91
+ 00807028 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a8605be53aa743b678dcba7f9a789d"></a>

### [`00807078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807078.md) → [`00807078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807078.md) FUN_00807078

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0080709c",
      "incomplete_value": false,
      "site": "0080709c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080709c",
      "incomplete_value": false,
      "site": "0080709c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0080709c",
      "DATA",
      [
        "storage",
        "00c00cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080709c",
      "DATA",
      [
        "storage",
        "00c00d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00807098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807078.md#insn-00807098)
- 新版 `00807098`（命令位置の公開資料なし）

~~~diff
- 00807098 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00807098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00807098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00807098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00807098 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00807098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00807098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00807098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00807098 bytes 08413391
+ 00807098 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-785afdfe2edc65e2900dde37348c583e"></a>

### [`008070ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070ac.md) → [`008070ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008070ac.md) FUN_008070ac

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
      "definition_site": "008070b8",
      "incomplete_value": false,
      "site": "008070b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008070b8",
      "incomplete_value": false,
      "site": "008070b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "008070b8",
      "DATA",
      [
        "storage",
        "00c00cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008070b8",
      "DATA",
      [
        "storage",
        "00c00d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008070b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008070ac.md#insn-008070b4)
- 新版 `008070b4`（命令位置の公開資料なし）

~~~diff
- 008070b4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 008070b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008070b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008070b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008070b4 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 008070b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008070b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008070b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008070b4 bytes 29413391
+ 008070b4 bytes 29813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f2917d5e24f23f4e773786e565eca6"></a>

### [`00807114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807114.md) → [`00807114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807114.md) FUN_00807114

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00807138",
      "incomplete_value": false,
      "site": "00807138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807138",
      "incomplete_value": false,
      "site": "00807138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "00807138",
      "DATA",
      [
        "storage",
        "00c00d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00807138",
      "DATA",
      [
        "storage",
        "00c00da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00807134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807114.md#insn-00807134)
- 新版 `00807134`（命令位置の公開資料なし）

~~~diff
- 00807134 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00807134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00807134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00807134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00807134 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00807134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00807134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00807134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00807134 bytes 08413591
+ 00807134 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-679df72c1d4894af4391f3f72d7d6de4"></a>

### [`00807148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807148.md) → [`00807148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807148.md) FUN_00807148

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
      "definition_site": "00807154",
      "incomplete_value": false,
      "site": "00807154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807154",
      "incomplete_value": false,
      "site": "00807154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "00807154",
      "DATA",
      [
        "storage",
        "00c00d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00807154",
      "DATA",
      [
        "storage",
        "00c00da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00807150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807148.md#insn-00807150)
- 新版 `00807150`（命令位置の公開資料なし）

~~~diff
- 00807150 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00807150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00807150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00807150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00807150 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00807150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00807150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00807150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00807150 bytes 29413591
+ 00807150 bytes 29813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbfa0f66d47fd3ce8e70a4d1b19c03e3"></a>

### [`008071a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071a4.md) → [`008071a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008071a4.md) FUN_008071a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008071c8",
      "incomplete_value": false,
      "site": "008071c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008071c8",
      "incomplete_value": false,
      "site": "008071c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "008071c8",
      "DATA",
      [
        "storage",
        "00c00dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008071c8",
      "DATA",
      [
        "storage",
        "00c00e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008071c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071a4.md#insn-008071c4)
- 新版 `008071c4`（命令位置の公開資料なし）

~~~diff
- 008071c4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 008071c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008071c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008071c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008071c4 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 008071c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008071c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008071c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008071c4 bytes 08413791
+ 008071c4 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a84b9a52422b7551a96925c72a2e84e"></a>

### [`008071d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071d8.md) → [`008071d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008071d8.md) FUN_008071d8

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
      "definition_site": "008071e4",
      "incomplete_value": false,
      "site": "008071e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008071e4",
      "incomplete_value": false,
      "site": "008071e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "008071e4",
      "DATA",
      [
        "storage",
        "00c00dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008071e4",
      "DATA",
      [
        "storage",
        "00c00e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008071e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071d8.md#insn-008071e0)
- 新版 `008071e0`（命令位置の公開資料なし）

~~~diff
- 008071e0 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 008071e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008071e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008071e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008071e0 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 008071e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008071e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008071e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008071e0 bytes 29413791
+ 008071e0 bytes 29813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb5eeb47f5322216f814e3f23bc0f24"></a>

### [`008071f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071f4.md) → [`008071f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008071f4.md) FUN_008071f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`007f7e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7e3c.md) [`00807354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807354.md) [`00807358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807358.md) [`00a6ca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6c/00a6ca00.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007f7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7e3c.md) [`00807354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807354.md) [`00807358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807358.md) [`00a6ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ca44.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00807228",
      "incomplete_value": false,
      "site": "00807228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807228",
      "incomplete_value": false,
      "site": "00807228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00807228",
      "DATA",
      [
        "storage",
        "00c00e40",
        null,
        "undefined *"
      ]
    ],
    [
      "00807264",
      "READ",
      [
        "storage",
        "00c00e60",
        null,
        "pointer"
      ]
    ],
    [
      "00807264",
      "READ",
      [
        "storage",
        "00c00e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00807228",
      "DATA",
      [
        "storage",
        "00c00e90",
        null,
        "undefined *"
      ]
    ],
    [
      "00807264",
      "READ",
      [
        "storage",
        "00c00eb0",
        null,
        "pointer"
      ]
    ],
    [
      "00807264",
      "READ",
      [
        "storage",
        "00c00eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00807220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008071f4.md#insn-00807220)
- 新版 `00807220`（命令位置の公開資料なし）

~~~diff
- 00807220 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00807220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00807220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00807220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00807220 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00807220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00807220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00807220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00807220 bytes 08013991
+ 00807220 bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82d9a963cd5ca4d83b1c21f0d0a608c"></a>

### [`0080730c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080730c.md) → [`0080730c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080730c.md) FUN_0080730c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00807330",
      "incomplete_value": false,
      "site": "00807330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807330",
      "incomplete_value": false,
      "site": "00807330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00807330",
      "DATA",
      [
        "storage",
        "00c00e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00807330",
      "DATA",
      [
        "storage",
        "00c00e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080732c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080730c.md#insn-0080732c)
- 新版 `0080732c`（命令位置の公開資料なし）

~~~diff
- 0080732c ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0080732c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0080732c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0080732c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0080732c ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0080732c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0080732c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0080732c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0080732c bytes 08013991
+ 0080732c bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24942346ac170d67d119c7c2900e167e"></a>

### [`00807340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807340.md) → [`00807340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807340.md) FUN_00807340

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
      "definition_site": "0080734c",
      "incomplete_value": false,
      "site": "0080734c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080734c",
      "incomplete_value": false,
      "site": "0080734c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "0080734c",
      "DATA",
      [
        "storage",
        "00c00e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080734c",
      "DATA",
      [
        "storage",
        "00c00e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00807348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807340.md#insn-00807348)
- 新版 `00807348`（命令位置の公開資料なし）

~~~diff
- 00807348 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00807348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00807348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00807348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00807348 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00807348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00807348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00807348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00807348 bytes 29013991
+ 00807348 bytes 29413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bd84d6db15b88814d9e32812bf2713"></a>

### [`0080735c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080735c.md) → [`0080735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080735c.md) FUN_0080735c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829bb8.md) [`00a6a468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6a468.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829bb8.md) [`00a6a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008073a0",
      "incomplete_value": false,
      "site": "008073a0",
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
    "old": {
      "definition_site": "008073a0",
      "incomplete_value": false,
      "site": "008073a0",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00807394",
      "incomplete_value": true,
      "site": "008073a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807394",
      "incomplete_value": true,
      "site": "008073a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008073a4",
      "incomplete_value": false,
      "site": "008073a4",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008073a4",
      "incomplete_value": false,
      "site": "008073a4",
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
      "00807394",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00807398",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008073a0",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00807394",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00807398",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "008073a0",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008073a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080735c.md#insn-008073a0) · [`008073a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080735c.md#insn-008073a4) · [`008073cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/0080735c.md#insn-008073cc)
- 新版 `008073a0`（命令位置の公開資料なし） · `008073a4`（命令位置の公開資料なし） · `008073cc`（命令位置の公開資料なし）

~~~diff
- 008073a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 008073a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008073a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 008073a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008073a0 bytes 093505f9
+ 008073a0 bytes 095505f9
- 008073a4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 008073a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008073a4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 008073a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008073a4 bytes ca3e05f9
+ 008073a4 bytes ca5e05f9
- 008073cc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 008073cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008073cc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 008073cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008073cc bytes d43e05f9
+ 008073cc bytes d45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b23ca913be5168aa4c56caab3cce698"></a>

### [`00807460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807460.md) → [`00807460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807460.md) _INIT_148

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0080749c",
      "incomplete_value": true,
      "site": "008074b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080749c",
      "incomplete_value": true,
      "site": "008074b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008074c0",
      "incomplete_value": true,
      "site": "008074dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008074c0",
      "incomplete_value": true,
      "site": "008074dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008074e0",
      "incomplete_value": true,
      "site": "008074fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008074e0",
      "incomplete_value": true,
      "site": "008074fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0080749c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008074c0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008074e0",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0080749c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008074c0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008074e0",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807460.md#insn-0080748c) · [`00807494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807460.md#insn-00807494)
- 新版 `0080748c`（命令位置の公開資料なし） · `00807494`（命令位置の公開資料なし）

~~~diff
- 0080748c ["COPY", "tmp:0:8", ["const:100:8"]]
- 0080748c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0080748c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0080748c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0080748c ["COPY", "tmp:0:8", ["const:140:8"]]
+ 0080748c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0080748c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0080748c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0080748c bytes 73020491
+ 0080748c bytes 73020591
- 00807494 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00807494 bytes 09d5ff90
+ 00807494 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00807494 bytes 09d5ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3320ecda30582660c93a72420989bd76"></a>

### [`008077f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008077f0.md) → [`008077f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008077f0.md) _INIT_149

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0080782c",
      "incomplete_value": true,
      "site": "00807848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080782c",
      "incomplete_value": true,
      "site": "00807848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00807850",
      "incomplete_value": true,
      "site": "0080786c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807850",
      "incomplete_value": true,
      "site": "0080786c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00807870",
      "incomplete_value": true,
      "site": "0080788c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00807870",
      "incomplete_value": true,
      "site": "0080788c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0080782c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00807850",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00807870",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0080782c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00807850",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00807870",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008077f0.md#insn-0080781c) · [`00807824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/008077f0.md#insn-00807824)
- 新版 `0080781c`（命令位置の公開資料なし） · `00807824`（命令位置の公開資料なし）

~~~diff
- 0080781c ["COPY", "tmp:0:8", ["const:118:8"]]
- 0080781c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0080781c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0080781c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0080781c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0080781c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0080781c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0080781c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0080781c bytes 73620491
+ 0080781c bytes 73620591
- 00807824 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00807824 bytes 09d5ff90
+ 00807824 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00807824 bytes 09d5ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e720868e301e8d1a2d33e178ca9765b0"></a>

### [`008083a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/008083a0.md) → [`008083a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/008083a0.md) _INIT_150

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00807b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00807/00807b80.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00807b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807b80.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.08% / 新版 86.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008083dc",
      "incomplete_value": true,
      "site": "008083f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008083dc",
      "incomplete_value": true,
      "site": "008083f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00808400",
      "incomplete_value": true,
      "site": "0080841c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00808400",
      "incomplete_value": true,
      "site": "0080841c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00808420",
      "incomplete_value": true,
      "site": "0080843c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00808420",
      "incomplete_value": true,
      "site": "0080843c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008083dc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00808400",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00808420",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008083dc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00808400",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00808420",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008083cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/008083a0.md#insn-008083cc) · [`008083d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/008083a0.md#insn-008083d4)
- 新版 `008083cc`（命令位置の公開資料なし） · `008083d4`（命令位置の公開資料なし）

~~~diff
- 008083cc ["COPY", "tmp:0:8", ["const:130:8"]]
- 008083cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008083cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008083cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008083cc ["COPY", "tmp:0:8", ["const:170:8"]]
+ 008083cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008083cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008083cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008083cc bytes 73c20491
+ 008083cc bytes 73c20591
- 008083d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008083d4 bytes e9d4fff0
+ 008083d4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008083d4 bytes e9d4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cacb3423fd539f6398ad55adaa49f9a"></a>

### [`00808774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/00808774.md) → [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) FUN_00808774

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00818144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00818/00818144.md) · 呼出先 142件 [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449358.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md)
- 新版 呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 142件 [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449358.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.90% / 新版 99.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008087b4",
      "incomplete_value": false,
      "site": "008087bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008087b4",
      "incomplete_value": false,
      "site": "008087bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "0080c590",
      "incomplete_value": false,
      "site": "0080c594",
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
                "const:c02000:8"
              ],
              [
                "leaf",
                "const:1e8:8"
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
      "definition_site": "0080c590",
      "incomplete_value": false,
      "site": "0080c594",
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
                "const:c02000:8"
              ],
              [
                "leaf",
                "const:198:8"
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
    "ordinal": 249,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008087bc",
      "DATA",
      [
        "storage",
        "00c00ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "0080baf8",
      "DATA",
      [
        "storage",
        "002a4db8",
        null,
        "string"
      ]
    ],
    [
      "0080bb3c",
      "DATA",
      [
        "storage",
        "002a4db8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008087bc",
      "DATA",
      [
        "storage",
        "00c00f20",
        null,
        "undefined *"
      ]
    ],
    [
      "0080baf8",
      "DATA",
      [
        "storage",
        "002a4db8",
        null,
        "undefined8"
      ]
    ],
    [
      "0080bb3c",
      "DATA",
      [
        "storage",
        "002a4db8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008087b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/00808774.md#insn-008087b4) · [`0080c58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/00808774.md#insn-0080c58c)
- 新版 `008087b4`（命令位置の公開資料なし） · `0080c58c`（命令位置の公開資料なし）

~~~diff
- 008087b4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008087b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008087b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008087b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008087b4 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 008087b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008087b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008087b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008087b4 bytes 08413b91
+ 008087b4 bytes 08813c91
- 0080c58c ["COPY", "tmp:0:8", ["const:198:8"]]
- 0080c58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0080c58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0080c58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0080c58c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0080c58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0080c58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0080c58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0080c58c bytes 08610691
+ 0080c58c bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba7e51d72ed3708849985098d97a1f5"></a>

### [`0080d900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d900.md) → [`0080d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d900.md) FUN_0080d900

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007e0354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e0/007e0354.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046e4f8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`007e0354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e0354.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0080d984",
      "incomplete_value": true,
      "site": "0080d990",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080d984",
      "incomplete_value": true,
      "site": "0080d990",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:685:8"
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
      "definition_site": "0080da44",
      "incomplete_value": true,
      "site": "0080da44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080da44",
      "incomplete_value": true,
      "site": "0080da44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef4:8"
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
      "definition_site": "0080da4c",
      "incomplete_value": true,
      "site": "0080da4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0080da4c",
      "incomplete_value": true,
      "site": "0080da4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0080d92c",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "0080d938",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ],
    [
      "0080d940",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0080d92c",
      "READ",
      [
        "storage",
        "00c1aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "0080d938",
      "READ",
      [
        "storage",
        "00c25290",
        null,
        "undefined1"
      ]
    ],
    [
      "0080d940",
      "READ",
      [
        "storage",
        "00c25290",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080d92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d900.md#insn-0080d92c) · [`0080d96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d900.md#insn-0080d96c) · [`0080d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d900.md#insn-0080d974)
- 新版 `0080d92c`（命令位置の公開資料なし） · `0080d96c`（命令位置の公開資料なし）

~~~diff
- 0080d92c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e68:8"]]
- 0080d92c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0080d92c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:eb8:8"]]
+ 0080d92c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0080d92c bytes f73647f9
+ 0080d92c bytes f75e47f9
- 0080d96c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 0080d96c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0080d96c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
+ 0080d96c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0080d96c bytes 083947f9
+ 0080d96c bytes 086147f9
- 0080d974 ["COPY", "register:4048:8", ["const:2a8000:8"]]
- 0080d974 bytes c9d4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54601b71b6820a4fcf77404d71276a07"></a>

### [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) → [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) FUN_0080dd1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00818144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00818/00818144.md) · 呼出先 42件 [`00429de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429de8.md) [`00448aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449358.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md)
- 新版 呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 42件 [`00429de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md) [`00448aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449358.md) [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.60% / 新版 99.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0080ec44",
      "incomplete_value": false,
      "site": "0080ec48",
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
                "const:c03000:8"
              ],
              [
                "leaf",
                "const:858:8"
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
      "definition_site": "0080ec44",
      "incomplete_value": false,
      "site": "0080ec48",
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
                "const:c03000:8"
              ],
              [
                "leaf",
                "const:808:8"
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
    "ordinal": 590,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0080ec64",
      "incomplete_value": false,
      "site": "0080ec68",
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
                "const:c04000:8"
              ],
              [
                "leaf",
                "const:140:8"
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
      "definition_site": "0080ec64",
      "incomplete_value": false,
      "site": "0080ec68",
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
                "const:c04000:8"
              ],
              [
                "leaf",
                "const:f0:8"
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
    "ordinal": 592,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0080ffe4",
      "incomplete_value": true,
      "site": "0080fff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:977:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0080ffe4",
      "incomplete_value": true,
      "site": "0080fff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1133,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0080ddcc",
      "DATA",
      [
        "storage",
        "00c00ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "0080ec48",
      "DATA",
      [
        "storage",
        "00c03818",
        null,
        "undefined *"
      ]
    ],
    [
      "0080ec68",
      "DATA",
      [
        "storage",
        "00c04100",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0080ddcc",
      "DATA",
      [
        "storage",
        "00c00f20",
        null,
        "undefined *"
      ]
    ],
    [
      "0080ec48",
      "DATA",
      [
        "storage",
        "00c03868",
        null,
        "undefined *"
      ]
    ],
    [
      "0080ec68",
      "DATA",
      [
        "storage",
        "00c04150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080dd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md#insn-0080dd48) · [`0080ec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md#insn-0080ec40) · [`0080ec60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md#insn-0080ec60)
- 新版 `0080dd48`（命令位置の公開資料なし） · `0080ec40`（命令位置の公開資料なし） · `0080ec60`（命令位置の公開資料なし）

~~~diff
- 0080dd48 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0080dd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0080dd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0080dd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0080dd48 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0080dd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0080dd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0080dd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0080dd48 bytes 29413b91
+ 0080dd48 bytes 29813c91
- 0080ec40 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0080ec40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0080ec40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0080ec40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0080ec40 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0080ec40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0080ec40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0080ec40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0080ec40 bytes 08212091
+ 0080ec40 bytes 08612191
- 0080ec60 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0080ec60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0080ec60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0080ec60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0080ec60 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 0080ec60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0080ec60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0080ec60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0080ec60 bytes 08c10391
+ 0080ec60 bytes 08010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9c45a587627f1f7fb28580b1b2d05a"></a>

### [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) → [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) FUN_0081c6a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) [`00822930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/00822930.md) [`00996ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996ea0.md) [`00a37688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md) · 呼出先 78件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00448aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449290.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 4件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00822930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822930.md) [`00996ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md) [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md) · 呼出先 78件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00448aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 99.63% / 新版 99.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0081d868",
      "incomplete_value": true,
      "site": "0081d868",
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
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081d868",
      "incomplete_value": true,
      "site": "0081d868",
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
            "const:f64:8"
          ]
        ]
      ]
    },
    "ordinal": 530,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0081da2c",
      "incomplete_value": true,
      "site": "0081da2c",
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
      "definition_site": "0081da2c",
      "incomplete_value": true,
      "site": "0081da2c",
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
    "ordinal": 50,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0081d868",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "0081da24",
      "READ",
      [
        "storage",
        "01071020",
        null,
        "undefined8"
      ]
    ],
    [
      "0081da24",
      "READ",
      [
        "storage",
        "01071028",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0081d868",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0081da24",
      "READ",
      [
        "storage",
        "01071060",
        null,
        "undefined8"
      ]
    ],
    [
      "0081da24",
      "READ",
      [
        "storage",
        "01071068",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0081d868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md#insn-0081d868) · [`0081da0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md#insn-0081da0c) · [`0081e3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md#insn-0081e3a4)
- 新版 `0081d868`（命令位置の公開資料なし） · `0081da0c`（命令位置の公開資料なし） · `0081e3a4`（命令位置の公開資料なし）

~~~diff
- 0081d868 ["COPY", "tmp:0:4", ["register:40c0:4"]]
- 0081d868 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:f64:8"]]
- 0081d868 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0081d868 ["COPY", "tmp:0:4", ["register:40c0:4"]]
+ 0081d868 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:fb4:8"]]
+ 0081d868 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0081d868 bytes d8923d39
+ 0081d868 bytes d8d23e39
- 0081da0c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0081da0c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0081da0c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0081da0c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0081da0c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0081da0c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0081da0c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0081da0c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0081da0c bytes 73c20691
+ 0081da0c bytes 73c20791
- 0081e3a4 ["COPY", "tmp:0:8", ["const:866:8"]]
- 0081e3a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0081e3a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0081e3a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0081e3a4 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 0081e3a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0081e3a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0081e3a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0081e3a4 bytes b59a2191
+ 0081e3a4 bytes b5661f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa25697df371dc3f210914c62d503fdf"></a>

### [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) → [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) FUN_0081f580

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2128件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00437c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md) [`004389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md) [`00439a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439a30.md) · 呼出先 0件 
- 新版 呼出元 2128件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) [`004389fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md) [`00439a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439a30.md) · 呼出先 0件 

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
      "definition_site": "0081f584",
      "incomplete_value": false,
      "site": "0081f588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081f584",
      "incomplete_value": false,
      "site": "0081f588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "0081f584",
      "DATA",
      [
        "storage",
        "00c281b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0081f584",
      "DATA",
      [
        "storage",
        "00c281f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0081f584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md#insn-0081f584)
- 新版 `0081f584`（命令位置の公開資料なし）

~~~diff
- 0081f584 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0081f584 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0081f584 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0081f584 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0081f584 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0081f584 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0081f584 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0081f584 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0081f584 bytes 00c00691
+ 0081f584 bytes 00c00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d36e85cefab27efd0210a93786dde47"></a>

### [`0081f58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) → [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) FUN_0081f58c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 41件 [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`00421b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b38.md) [`0044fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fecc.md) [`004502bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004502bc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md)
- 新版 呼出元 0件  · 呼出先 41件 [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`00421b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b38.md) [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`004502bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md)

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
      "definition_site": "0081f898",
      "incomplete_value": false,
      "site": "0081f8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081f898",
      "incomplete_value": false,
      "site": "0081f8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "0081f8a4",
      "DATA",
      [
        "storage",
        "00c010f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0081f8a4",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0081f898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md#insn-0081f898)
- 新版 `0081f898`（命令位置の公開資料なし）

~~~diff
- 0081f898 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 0081f898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0081f898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0081f898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0081f898 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0081f898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0081f898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0081f898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0081f898 bytes 08e10391
+ 0081f898 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfbe63cc6e7b00de5a8bb55aaf7d204d"></a>

### [`0081f9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f9ac.md) → [`0081f9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f9ac.md) FUN_0081f9ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) · 呼出先 4件 [`004684b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00468/004684b8.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) · 呼出先 4件 [`004684b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0081f9e8",
      "incomplete_value": true,
      "site": "0081f9e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081f9e8",
      "incomplete_value": true,
      "site": "0081f9e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
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
      "0081f9cc",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0081f9cc",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0081f9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f9ac.md#insn-0081f9c4)
- 新版 `0081f9c4`（命令位置の公開資料なし）

~~~diff
- 0081f9c4 ["COPY", "tmp:0:8", ["const:952:8"]]
- 0081f9c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0081f9c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0081f9c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0081f9c4 ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 0081f9c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0081f9c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0081f9c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0081f9c4 bytes 4a492591
+ 0081f9c4 bytes 4a152391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f8309d6c93022ffdf544bbedea47e4"></a>

### [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) → [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) FUN_0081fa64

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 20件 [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`0081f9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f9ac.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0083dac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dac4.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md)
- 新版 呼出元 20件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`0081f9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f9ac.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0083dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dac4.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.21% / 新版 90.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `store_destination` 37件, `store_value` 22件

アドレスに依存する影響 `branch_value` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0081fc64",
      "incomplete_value": true,
      "site": "0081fc64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081fc64",
      "incomplete_value": true,
      "site": "0081fc64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dce:8"
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
      "definition_site": "0081fc68",
      "incomplete_value": true,
      "site": "0081fc68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0081fc68",
      "incomplete_value": true,
      "site": "0081fc68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0081fd60",
      "incomplete_value": true,
      "site": "0081fd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0081fd60",
      "incomplete_value": true,
      "site": "0081fd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:abc:8"
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
      "0081fc40",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0081fc54",
      "READ",
      [
        "storage",
        "00293dce",
        null,
        "string"
      ]
    ],
    [
      "0081fc58",
      "READ",
      [
        "storage",
        "00293dd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0081fc40",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0081fc54",
      "READ",
      [
        "storage",
        "00293d41",
        null,
        "string"
      ]
    ],
    [
      "0081fc58",
      "READ",
      [
        "storage",
        "00293d46",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008201d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md#insn-008201d8) · [`00820a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md#insn-00820a10) · [`0081fc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md#insn-0081fc30)
- 新版 `008201d8`（命令位置の公開資料なし） · `00820a10`（命令位置の公開資料なし） · `0081fc30`（命令位置の公開資料なし）

~~~diff
- 008201d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 008201d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008201d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 008201d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 008201d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 008201d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008201d8 bytes 1f3505f9
+ 008201d8 bytes 1f5505f9
- 00820a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00820a10 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00820a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00820a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00820a10 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00820a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00820a10 bytes 1f3505f9
+ 00820a10 bytes 1f5505f9
- 0081fc30 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0081fc30 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0081fc30 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0081fc30 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0081fc30 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0081fc30 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0081fc30 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0081fc30 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0081fc30 bytes 18e30091
+ 0081fc30 bytes 18e30191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f4b742e27052f5f4e85fb328c7932b1"></a>

### [`00821350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md) → [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) FUN_00821350

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0044fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fecc.md) [`00450394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450394.md) [`00450398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450398.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`00450394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450394.md) [`00450398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008214d8",
      "incomplete_value": true,
      "site": "008214d8",
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
                "const:c28000:8"
              ],
              [
                "leaf",
                "const:1f0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "008214d8",
      "incomplete_value": true,
      "site": "008214d8",
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
                "const:c28000:8"
              ],
              [
                "leaf",
                "const:1b0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "definition_site": "008213b8",
      "incomplete_value": false,
      "site": "008213c0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008213b8",
      "incomplete_value": false,
      "site": "008213c0",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008215e4",
      "incomplete_value": false,
      "site": "008215e8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008215e4",
      "incomplete_value": false,
      "site": "008215e8",
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
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008213ac",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008213b8",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "008214d8",
      "WRITE",
      [
        "storage",
        "01055a0b",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008213ac",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008213b8",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "008214d8",
      "WRITE",
      [
        "storage",
        "01055a4b",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008213a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md#insn-008213a8) · [`008213b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md#insn-008213b8) · [`008214cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md#insn-008214cc)
- 新版 `008213a8`（命令位置の公開資料なし） · `008213b8`（命令位置の公開資料なし） · `008214cc`（命令位置の公開資料なし）

~~~diff
- 008213a8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008213a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008213a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008213a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008213a8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008213a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008213a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008213a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008213a8 bytes 08e10091
+ 008213a8 bytes 08e10191
- 008213b8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008213b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008213b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008213b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008213b8 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 008213b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008213b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008213b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008213b8 bytes 00000091
+ 008213b8 bytes 00000191
- 008214cc ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 008214cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008214cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008214cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008214cc ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 008214cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008214cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008214cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008214cc bytes 08c10691
+ 008214cc bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6cba42c2f2190c9d51c94faae66f91"></a>

### [`008216e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md) → [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) FUN_008216e4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00821350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md) · 呼出先 22件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`004665d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004665d0.md) [`00467cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467cf8.md) [`00467d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467d30.md)
- 新版 呼出元 1件 [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) · 呼出先 22件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`004665d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004665d0.md) [`00467cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467cf8.md) [`00467d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467d30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.47% / 新版 95.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082174c",
      "incomplete_value": true,
      "site": "0082174c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082174c",
      "incomplete_value": true,
      "site": "0082174c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
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
      "definition_site": "0082175c",
      "incomplete_value": true,
      "site": "0082175c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:47d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082175c",
      "incomplete_value": true,
      "site": "0082175c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e3:8"
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
      "definition_site": "00821754",
      "incomplete_value": true,
      "site": "00821760",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00821754",
      "incomplete_value": true,
      "site": "00821760",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "00821738",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ],
    [
      "00821750",
      "READ",
      [
        "storage",
        "002a73e3",
        null,
        "string"
      ]
    ],
    [
      "00821754",
      "READ",
      [
        "storage",
        "002a73ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00821738",
      "READ",
      [
        "storage",
        "002a03a0",
        null,
        "string"
      ]
    ],
    [
      "00821750",
      "READ",
      [
        "storage",
        "002a747d",
        null,
        "string"
      ]
    ],
    [
      "00821754",
      "READ",
      [
        "storage",
        "002a7484",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082172c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md#insn-0082172c) · [`00821740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md#insn-00821740)
- 新版 `0082172c`（命令位置の公開資料なし） · `00821740`（命令位置の公開資料なし）

~~~diff
- 0082172c ["COPY", "tmp:0:8", ["const:315:8"]]
- 0082172c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0082172c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0082172c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0082172c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 0082172c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0082172c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0082172c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0082172c bytes 29550c91
+ 0082172c bytes 29810e91
- 00821740 ["COPY", "register:4040:8", ["const:2a7000:8"]]
- 00821740 bytes 28d4ffd0
+ 00821740 ["COPY", "register:4040:8", ["const:2a7000:8"]]
+ 00821740 bytes 28d4ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb8095bf6634f5fa31360974982b71e"></a>

### [`008220d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md) → [`008220d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008220d0.md) FUN_008220d0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 14件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`006989b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006989b8.md) [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 15件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)
- 新版 呼出元 14件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`006989b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/006989b8.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 15件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00822118",
      "incomplete_value": false,
      "site": "00822120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00822118",
      "incomplete_value": false,
      "site": "00822120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00822198",
      "incomplete_value": true,
      "site": "008221ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00822198",
      "incomplete_value": true,
      "site": "008221ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cbc:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00822234",
      "incomplete_value": false,
      "site": "0082223c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00822234",
      "incomplete_value": false,
      "site": "0082223c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "00822120",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00822198",
      "READ",
      [
        "storage",
        "002a6cbc",
        null,
        "string"
      ]
    ],
    [
      "0082223c",
      "DATA",
      [
        "storage",
        "00c01738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00822120",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ],
    [
      "00822198",
      "READ",
      [
        "storage",
        "002a6d56",
        null,
        "string"
      ]
    ],
    [
      "0082223c",
      "DATA",
      [
        "storage",
        "00c01788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00822118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md#insn-00822118) · [`00822190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md#insn-00822190) · [`00822234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md#insn-00822234)
- 新版 `00822118`（命令位置の公開資料なし） · `00822190`（命令位置の公開資料なし） · `00822234`（命令位置の公開資料なし）

~~~diff
- 00822118 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00822118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00822118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00822118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00822118 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00822118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00822118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00822118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00822118 bytes 08e11a91
+ 00822118 bytes 08211c91
- 00822190 ["COPY", "tmp:0:8", ["const:cbc:8"]]
- 00822190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00822190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00822190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00822190 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 00822190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00822190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00822190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00822190 bytes 29f13291
+ 00822190 bytes 29593591
- 00822234 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00822234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00822234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00822234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00822234 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00822234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00822234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00822234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00822234 bytes 08e11c91
+ 00822234 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49fd2730ef3339d56e2050b98338ba65"></a>

### [`0082233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/0082233c.md) → [`0082233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/0082233c.md) FUN_0082233c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`007317b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00731/007317b0.md) [`00821cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cbc.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 14件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)
- 新版 呼出元 4件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 14件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.81% / 新版 84.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00822370",
      "incomplete_value": false,
      "site": "00822378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00822370",
      "incomplete_value": false,
      "site": "00822378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "definition_site": "008223fc",
      "incomplete_value": true,
      "site": "008223fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008223fc",
      "incomplete_value": true,
      "site": "008223fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a7f:8"
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
      "definition_site": "008223f0",
      "incomplete_value": true,
      "site": "00822400",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "008223f0",
      "incomplete_value": true,
      "site": "00822400",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "00822378",
      "DATA",
      [
        "storage",
        "00c017b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008223ec",
      "READ",
      [
        "storage",
        "0029ea7f",
        null,
        "string"
      ]
    ],
    [
      "008223f0",
      "READ",
      [
        "storage",
        "0029ea86",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00822378",
      "DATA",
      [
        "storage",
        "00c01808",
        null,
        "undefined *"
      ]
    ],
    [
      "008223ec",
      "READ",
      [
        "storage",
        "0029eb0a",
        null,
        "string"
      ]
    ],
    [
      "008223f0",
      "READ",
      [
        "storage",
        "0029eb11",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00822370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/0082233c.md#insn-00822370) · [`008223e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/0082233c.md#insn-008223e4) · [`00822420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/0082233c.md#insn-00822420)
- 新版 `00822370`（命令位置の公開資料なし） · `008223e4`（命令位置の公開資料なし） · `00822420`（命令位置の公開資料なし）

~~~diff
- 00822370 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00822370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00822370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00822370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00822370 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00822370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00822370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00822370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00822370 bytes 08e11e91
+ 00822370 bytes 08212091
- 008223e4 ["COPY", "tmp:0:8", ["const:a7f:8"]]
- 008223e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008223e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008223e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008223e4 ["COPY", "tmp:0:8", ["const:b0a:8"]]
+ 008223e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008223e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008223e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008223e4 bytes 29fd2991
+ 008223e4 bytes 29292c91
- 00822420 ["COPY", "tmp:0:8", ["const:acf:8"]]
- 00822420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00822420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00822420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00822420 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 00822420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00822420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00822420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00822420 bytes 293d2b91
+ 00822420 bytes 29692d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64febdfd3f4ce02a74dd50fbe15338b0"></a>

### [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) → [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) FUN_00824eb0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 166件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`00428648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md)
- 新版 呼出元 0件  · 呼出先 166件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00428648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.99% / 新版 95.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 39件, `call_target` 1件, `store_destination` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008253a4",
      "incomplete_value": true,
      "site": "008253b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008253a4",
      "incomplete_value": true,
      "site": "008253b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008253a8",
      "incomplete_value": true,
      "site": "008253b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008253a8",
      "incomplete_value": true,
      "site": "008253b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00825444",
      "incomplete_value": false,
      "site": "00825444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c29000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00825444",
      "incomplete_value": false,
      "site": "00825444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c29000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "ordinal": 69,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00825014",
      "PARAM",
      [
        "storage",
        "00c29ac8",
        null,
        null
      ]
    ],
    [
      "00825054",
      "READ",
      [
        "storage",
        "01052290",
        null,
        "undefined8"
      ]
    ],
    [
      "00825080",
      "READ",
      [
        "storage",
        "01052298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00825014",
      "PARAM",
      [
        "storage",
        "00c29b08",
        null,
        null
      ]
    ],
    [
      "00825054",
      "READ",
      [
        "storage",
        "010522d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00825080",
      "READ",
      [
        "storage",
        "010522d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00825444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md#insn-00825444) · [`00825014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md#insn-00825014) · [`00825048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md#insn-00825048)
- 新版 `00825444`（命令位置の公開資料なし） · `00825014`（命令位置の公開資料なし） · `00825048`（命令位置の公開資料なし）

~~~diff
- 00825444 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00825444 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00825444 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:288:8"]]
- 00825444 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00825444 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00825444 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00825444 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:2c8:8"]]
+ 00825444 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00825444 bytes 3f210a39
+ 00825444 bytes 3f210b39
- 00825014 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00825014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00825014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00825014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00825014 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00825014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00825014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00825014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00825014 bytes 00202b91
+ 00825014 bytes 00202c91
- 00825048 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00825048 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00825048 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00825048 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00825048 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00825048 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00825048 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00825048 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00825048 bytes 39c30691
+ 00825048 bytes 39c30791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b18c7dd3f7920d95196f4fb4f9fac8b5"></a>

### [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) → [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) FUN_00827ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 81件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444d10.md)
- 新版 呼出元 0件  · 呼出先 81件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444d10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00828990",
      "incomplete_value": true,
      "site": "00828990",
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
      "definition_site": "00828990",
      "incomplete_value": true,
      "site": "00828990",
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
    "ordinal": 99,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008289f0",
      "incomplete_value": true,
      "site": "008289f0",
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
      "definition_site": "008289f0",
      "incomplete_value": true,
      "site": "008289f0",
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
    "ordinal": 103,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00827c44",
      "incomplete_value": true,
      "site": "00827c48",
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
      "definition_site": "00827c44",
      "incomplete_value": true,
      "site": "00827c48",
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
    "ordinal": 6,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00827c34",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00827c44",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00827c44",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00827c34",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00827c44",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "00827c44",
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00827c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md#insn-00827c34) · [`00827d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md#insn-00827d34) · [`00827d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md#insn-00827d3c)
- 新版 `00827c34`（命令位置の公開資料なし） · `00827d34`（命令位置の公開資料なし） · `00827d3c`（命令位置の公開資料なし）

~~~diff
- 00827c34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d28:8"]]
- 00827c34 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00827c34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 00827c34 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00827c34 bytes d69646f9
+ 00827c34 bytes d6be46f9
- 00827d34 ["COPY", "tmp:0:8", ["const:460:8"]]
- 00827d34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00827d34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00827d34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00827d34 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 00827d34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00827d34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00827d34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00827d34 bytes 21801191
+ 00827d34 bytes 21c01291
- 00827d3c ["COPY", "tmp:0:8", ["const:470:8"]]
- 00827d3c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00827d3c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00827d3c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00827d3c ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00827d3c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00827d3c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00827d3c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00827d3c bytes 42c01191
+ 00827d3c bytes 42001391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a10495e1c6cc606782f9f00896a48b49"></a>

### [`00828e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00828/00828e28.md) → [`00828e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00828/00828e28.md) FUN_00828e28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00828e60",
      "incomplete_value": true,
      "site": "00828e60",
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
      "definition_site": "00828e60",
      "incomplete_value": true,
      "site": "00828e60",
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
      "definition_site": "00828e68",
      "incomplete_value": false,
      "site": "00828e7c",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00828e68",
      "incomplete_value": false,
      "site": "00828e7c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00828e70",
      "incomplete_value": false,
      "site": "00828e7c",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00828e70",
      "incomplete_value": false,
      "site": "00828e7c",
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
      "00828e5c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00828e68",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00828e70",
      "PARAM",
      [
        "storage",
        "00be8e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00828e5c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00828e68",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00828e70",
      "PARAM",
      [
        "storage",
        "00be8ea8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00828e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00828/00828e28.md#insn-00828e5c) · [`00828e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00828/00828e28.md#insn-00828e68) · [`00828e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00828/00828e28.md#insn-00828e70)
- 新版 `00828e5c`（命令位置の公開資料なし） · `00828e68`（命令位置の公開資料なし） · `00828e70`（命令位置の公開資料なし）

~~~diff
- 00828e5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00828e5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00828e5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00828e5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00828e5c bytes 083d45f9
+ 00828e5c bytes 085d45f9
- 00828e68 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00828e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00828e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00828e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00828e68 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00828e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00828e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00828e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00828e68 bytes 21203991
+ 00828e68 bytes 21603a91
- 00828e70 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00828e70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00828e70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00828e70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00828e70 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00828e70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00828e70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00828e70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00828e70 bytes 42603991
+ 00828e70 bytes 42a03a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdea366e7324e01e53e587c03ba395fc"></a>

### [`00829180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829180.md) → [`00829180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829180.md) FUN_00829180

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`00469f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f74.md) [`0046a3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a3a8.md) [`0080d728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d728.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`00469f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f74.md) [`0046a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md) [`0080d728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d728.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008291f8",
      "incomplete_value": true,
      "site": "008291fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008291f8",
      "incomplete_value": true,
      "site": "008291fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:d28:8"
              ]
            ]
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
      "definition_site": "00829238",
      "incomplete_value": false,
      "site": "0082923c",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00829238",
      "incomplete_value": false,
      "site": "0082923c",
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
            "const:d70:8"
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
      "008291f8",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "008291f8",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00829238",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008291f8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "008291f8",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00829238",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008291f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829180.md#insn-008291f8) · [`00829238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829180.md#insn-00829238)
- 新版 `008291f8`（命令位置の公開資料なし） · `00829238`（命令位置の公開資料なし）

~~~diff
- 008291f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
- 008291f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008291f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d78:8"]]
+ 008291f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008291f8 bytes 009446f9
+ 008291f8 bytes 00bc46f9
- 00829238 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 00829238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00829238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00829238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00829238 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00829238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00829238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00829238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00829238 bytes 00c03591
+ 00829238 bytes 00c03691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fa8c6dbcd83efb58274a9da3655d1c"></a>

### [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) → [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) FUN_00829478

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00845744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845744.md) [`00845a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845a24.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`004724fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004724fc.md)
- 新版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00845744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md) [`00845a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`004724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082952c",
      "incomplete_value": false,
      "site": "00829538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082952c",
      "incomplete_value": false,
      "site": "00829538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008295a8",
      "incomplete_value": false,
      "site": "008295a8",
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
    "old": {
      "definition_site": "008295a8",
      "incomplete_value": false,
      "site": "008295a8",
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
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082959c",
      "incomplete_value": true,
      "site": "008295a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082959c",
      "incomplete_value": true,
      "site": "008295a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "008294b4",
      "PARAM",
      [
        "storage",
        "00be8460",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008294bc",
      "PARAM",
      [
        "storage",
        "00c01ac8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00829538",
      "DATA",
      [
        "storage",
        "00c01af0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008294b4",
      "PARAM",
      [
        "storage",
        "00be84b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008294bc",
      "PARAM",
      [
        "storage",
        "00c01b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00829538",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008295a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md#insn-008295a8) · [`008295ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md#insn-008295ac) · [`008295c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md#insn-008295c8)
- 新版 `008295a8`（命令位置の公開資料なし） · `008295ac`（命令位置の公開資料なし） · `008295c8`（命令位置の公開資料なし）

~~~diff
- 008295a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a68:8"]]
- 008295a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008295a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
+ 008295a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008295a8 bytes 2a3505f9
+ 008295a8 bytes 2a5505f9
- 008295ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 008295ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008295ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 008295ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008295ac bytes a83e05f9
+ 008295ac bytes a85e05f9
- 008295c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 008295c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008295c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
+ 008295c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008295c8 bytes b43e05f9
+ 008295c8 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871eeb6a086f1018018ce9b0e7e30d6b"></a>

### [`0082ae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082ae18.md) → [`0082ae18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082a/0082ae18.md) FUN_0082ae18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) · 呼出先 3件 [`0052dadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dadc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 3件 [`0052dadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dadc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0082ae3c",
      "incomplete_value": true,
      "site": "0082ae58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082ae3c",
      "incomplete_value": true,
      "site": "0082ae58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cbc:8"
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
      "0082ae3c",
      "READ",
      [
        "storage",
        "002a6cbc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0082ae3c",
      "READ",
      [
        "storage",
        "002a6d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082ae34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082ae18.md#insn-0082ae34)
- 新版 `0082ae34`（命令位置の公開資料なし）

~~~diff
- 0082ae34 ["COPY", "tmp:0:8", ["const:cbc:8"]]
- 0082ae34 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0082ae34 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0082ae34 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0082ae34 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0082ae34 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0082ae34 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0082ae34 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0082ae34 bytes 4af13291
+ 0082ae34 bytes 4a593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb5fed274d4250256b2871650044427"></a>

### [`0082af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082af44.md) → [`0082af44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082a/0082af44.md) FUN_0082af44

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`006986e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00698/006986e4.md) [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) [`00a52af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52af8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0071b5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b5d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 5件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`006986e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/006986e4.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) [`00a52b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52b3c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0071b5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b5d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.42% / 新版 96.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082b028",
      "incomplete_value": true,
      "site": "0082b030",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082b028",
      "incomplete_value": true,
      "site": "0082b030",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:18:8"
              ]
            ]
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
      "definition_site": "0082b04c",
      "incomplete_value": true,
      "site": "0082b05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082b04c",
      "incomplete_value": true,
      "site": "0082b05c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c24000:8"
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
      "definition_site": "0082b0b0",
      "incomplete_value": true,
      "site": "0082b0bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082b0b0",
      "incomplete_value": true,
      "site": "0082b0bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38:8"
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
      "0082b028",
      "READ",
      [
        "storage",
        "00c24018",
        null,
        null
      ]
    ],
    [
      "0082b04c",
      "READ",
      [
        "storage",
        "00c24000",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b0b0",
      "READ",
      [
        "storage",
        "00c24038",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0082b028",
      "READ",
      [
        "storage",
        "00c24068",
        null,
        null
      ]
    ],
    [
      "0082b04c",
      "READ",
      [
        "storage",
        "00c24050",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b0b0",
      "READ",
      [
        "storage",
        "00c24088",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082b024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082af44.md#insn-0082b024) · [`0082b04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082af44.md#insn-0082b04c) · [`0082b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082a/0082af44.md#insn-0082b0a8)
- 新版 `0082b024`（命令位置の公開資料なし） · `0082b04c`（命令位置の公開資料なし） · `0082b0a8`（命令位置の公開資料なし）

~~~diff
- 0082b024 ["COPY", "tmp:0:8", ["const:18:8"]]
- 0082b024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0082b024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0082b024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0082b024 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0082b024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0082b024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0082b024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0082b024 bytes 08610091
+ 0082b024 bytes 08a10191
- 0082b04c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0082b04c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082b04c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 0082b04c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082b04c bytes 080140f9
+ 0082b04c bytes 082940f9
- 0082b0a8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0082b0a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 0082b0a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 0082b0a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
+ 0082b0a8 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0082b0a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
+ 0082b0a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
+ 0082b0a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 0082b0a8 bytes 10e20091
+ 0082b0a8 bytes 10220291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af2966e85c4364f9961b51061f46c2c"></a>

### [`0082b53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md) → [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) FUN_0082b53c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00734830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/00734830.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00a52af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a52/00a52af8.md) · 呼出先 33件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00706b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706b94.md) [`00706bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00706/00706bbc.md) [`00707830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00707/00707830.md)
- 新版 呼出元 4件 [`00734830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734830.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00a52b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52b3c.md) · 呼出先 33件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00706b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706b94.md) [`00706bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706bbc.md) [`00707830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/00707830.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.77% / 新版 99.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082bdec",
      "incomplete_value": false,
      "site": "0082bdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082bdec",
      "incomplete_value": false,
      "site": "0082bdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082ba88",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "0082bc80",
      "READ",
      [
        "storage",
        "00c1b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "0082bdec",
      "DATA",
      [
        "storage",
        "00c018b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0082ba88",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "0082bc80",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "0082bdec",
      "DATA",
      [
        "storage",
        "00c01908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082ba88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md#insn-0082ba88) · [`0082bc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md#insn-0082bc80) · [`0082bde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md#insn-0082bde0)
- 新版 `0082ba88`（命令位置の公開資料なし） · `0082bc80`（命令位置の公開資料なし） · `0082bde0`（命令位置の公開資料なし）

~~~diff
- 0082ba88 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:6d8:8"]]
- 0082ba88 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082ba88 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
+ 0082ba88 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0082ba88 bytes 396f43f9
+ 0082ba88 bytes 399743f9
- 0082bc80 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:6d8:8"]]
- 0082bc80 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082bc80 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
+ 0082bc80 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0082bc80 bytes 396f43f9
+ 0082bc80 bytes 399743f9
- 0082bde0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0082bde0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0082bde0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0082bde0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0082bde0 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 0082bde0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0082bde0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0082bde0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0082bde0 bytes 6be12291
+ 0082bde0 bytes 6b212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46ac16946df9272ddb2a0606ee34f75a"></a>

### [`0082ead8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082e/0082ead8.md) → [`0082ead8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082e/0082ead8.md) FUN_0082ead8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1d4.md)
- 新版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0059d1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d1d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.33% / 新版 99.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082f050",
      "incomplete_value": true,
      "site": "0082f050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f050",
      "incomplete_value": true,
      "site": "0082f050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 81,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082f03c",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0082f03c",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082e/0082ead8.md#insn-0082f034)
- 新版 `0082f034`（命令位置の公開資料なし）

~~~diff
- 0082f034 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0082f034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0082f034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0082f034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0082f034 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0082f034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0082f034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0082f034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0082f034 bytes 29850291
+ 0082f034 bytes 29ed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0d2cb12959094893895a76c3f943f46"></a>

### [`0082f3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f3d0.md) → [`0082f3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f3d0.md) FUN_0082f3d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 9件 [`0052dae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae0.md) [`0083f858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f858.md) [`0083f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f85c.md) [`0084a52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a52c.md) [`0084a530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a530.md)
- 新版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 9件 [`0052dae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae0.md) [`0083f858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f858.md) [`0083f85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f85c.md) [`0084a52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a52c.md) [`0084a530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a530.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082f400",
      "incomplete_value": false,
      "site": "0082f400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f400",
      "incomplete_value": false,
      "site": "0082f400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0082f400",
      "DATA",
      [
        "storage",
        "00c01948",
        null,
        "undefined *"
      ]
    ],
    [
      "0082f434",
      "READ",
      [
        "storage",
        "00c01968",
        null,
        "pointer"
      ]
    ],
    [
      "0082f434",
      "READ",
      [
        "storage",
        "00c01970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0082f400",
      "DATA",
      [
        "storage",
        "00c01998",
        null,
        "undefined *"
      ]
    ],
    [
      "0082f434",
      "READ",
      [
        "storage",
        "00c019b8",
        null,
        "pointer"
      ]
    ],
    [
      "0082f434",
      "READ",
      [
        "storage",
        "00c019c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082f3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f3d0.md#insn-0082f3fc)
- 新版 `0082f3fc`（命令位置の公開資料なし）

~~~diff
- 0082f3fc ["COPY", "tmp:0:8", ["const:948:8"]]
- 0082f3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0082f3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0082f3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0082f3fc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0082f3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0082f3fc bytes 08212591
+ 0082f3fc bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3923a9f9a56673ce1d07511dcc9ec8c"></a>

### [`0082f5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f5a4.md) → [`0082f5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f5a4.md) FUN_0082f5a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.79% / 新版 98.79%

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
      "definition_site": "0082f5e8",
      "incomplete_value": false,
      "site": "0082f5f0",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f5e8",
      "incomplete_value": false,
      "site": "0082f5f0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082f618",
      "incomplete_value": true,
      "site": "0082f628",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f618",
      "incomplete_value": true,
      "site": "0082f628",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b98:8"
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
      "definition_site": "00830704",
      "incomplete_value": true,
      "site": "00830708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00830704",
      "incomplete_value": true,
      "site": "00830708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 207,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082f5f0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0082f618",
      "READ",
      [
        "storage",
        "002a9b98",
        null,
        "string"
      ]
    ],
    [
      "008306f4",
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
      "0082f5f0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0082f618",
      "READ",
      [
        "storage",
        "002a9ba7",
        null,
        "string"
      ]
    ],
    [
      "008306f4",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082f5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f5a4.md#insn-0082f5e8) · [`0082f614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f5a4.md#insn-0082f614) · [`008306f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f5a4.md#insn-008306f4)
- 新版 `0082f5e8`（命令位置の公開資料なし） · `0082f614`（命令位置の公開資料なし） · `008306f4`（命令位置の公開資料なし）

~~~diff
- 0082f5e8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0082f5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0082f5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0082f5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0082f5e8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0082f5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0082f5e8 bytes 08a13491
+ 0082f5e8 bytes 08e13591
- 0082f614 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0082f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0082f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0082f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0082f614 ["COPY", "tmp:0:8", ["const:ba7:8"]]
+ 0082f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0082f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0082f614 bytes 08612e91
+ 0082f614 bytes 089d2e91
- 008306f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 008306f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008306f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 008306f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008306f4 bytes 08b946f9
+ 008306f4 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0b4f43f6dc35e23c186686645683af"></a>

### [`008308f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008308f0.md) → [`008308f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/008308f0.md) FUN_008308f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006d6750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6750.md) [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) [`0080420c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00804/0080420c.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fc4.md) [`00444fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fcc.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md)
- 新版 呼出元 3件 [`006d6750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6750.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0080420c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/0080420c.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fc4.md) [`00444fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fcc.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00830920",
      "incomplete_value": true,
      "site": "00830924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830920",
      "incomplete_value": true,
      "site": "00830924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "definition_site": "00830934",
      "incomplete_value": false,
      "site": "00830938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830934",
      "incomplete_value": false,
      "site": "00830938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "00830914",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00830920",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00830934",
      "PARAM",
      [
        "storage",
        "00c281b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00830914",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00830920",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00830934",
      "PARAM",
      [
        "storage",
        "00c281f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008308f0.md#insn-00830914) · [`00830928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008308f0.md#insn-00830928)
- 新版 `00830914`（命令位置の公開資料なし） · `00830928`（命令位置の公開資料なし）

~~~diff
- 00830914 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d28:8"]]
- 00830914 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00830914 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d78:8"]]
+ 00830914 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00830914 bytes f79646f9
+ 00830914 bytes f7be46f9
- 00830928 ["COPY", "register:40c0:8", ["const:c28000:8"]]
- 00830928 bytes d81f0090
+ 00830928 ["COPY", "register:40c0:8", ["const:c28000:8"]]
+ 00830928 bytes d81f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff85c844011ef4f8f39c6d086b61334"></a>

### [`008309c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md) → [`008309c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/008309c8.md) FUN_008309c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00879b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md) · 呼出先 5件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00879b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md) · 呼出先 5件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.66% / 新版 87.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008309f4",
      "incomplete_value": true,
      "site": "008309f4",
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
                "const:c29000:8"
              ],
              [
                "leaf",
                "const:ee0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
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
      "definition_site": "008309f4",
      "incomplete_value": true,
      "site": "008309f4",
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
                "const:c29000:8"
              ],
              [
                "leaf",
                "const:ea0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              [
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008309f8",
      "incomplete_value": false,
      "site": "008309f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c29000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008309f8",
      "incomplete_value": false,
      "site": "008309f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c29000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008309fc",
      "incomplete_value": false,
      "site": "008309fc",
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
                "const:c29000:8"
              ],
              [
                "leaf",
                "const:ee0:8"
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
      "definition_site": "008309fc",
      "incomplete_value": false,
      "site": "008309fc",
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
                "const:c29000:8"
              ],
              [
                "leaf",
                "const:ea0:8"
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
      "008309f4",
      "WRITE",
      [
        "storage",
        "0109c5ca",
        null,
        "undefined2"
      ]
    ],
    [
      "008309f8",
      "WRITE",
      [
        "storage",
        "00c29ea0",
        null,
        "undefined4"
      ]
    ],
    [
      "008309fc",
      "WRITE",
      [
        "storage",
        "00c29ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008309f4",
      "WRITE",
      [
        "storage",
        "0109c60a",
        null,
        "undefined2"
      ]
    ],
    [
      "008309f8",
      "WRITE",
      [
        "storage",
        "00c29ee0",
        null,
        "undefined4"
      ]
    ],
    [
      "008309fc",
      "WRITE",
      [
        "storage",
        "00c29ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008309f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md#insn-008309f0) · [`00830a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md#insn-00830a24) · [`00830a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md#insn-00830a6c)
- 新版 `008309f0`（命令位置の公開資料なし） · `00830a24`（命令位置の公開資料なし） · `00830a6c`（命令位置の公開資料なし）

~~~diff
- 008309f0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 008309f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008309f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008309f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008309f0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 008309f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008309f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008309f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008309f0 bytes 08813a91
+ 008309f0 bytes 08813b91
- 00830a24 ["COPY", "tmp:0:8", ["const:8c4:8"]]
- 00830a24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00830a24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00830a24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00830a24 ["COPY", "tmp:0:8", ["const:94f:8"]]
+ 00830a24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00830a24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00830a24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00830a24 bytes 29112391
+ 00830a24 bytes 293d2591
- 00830a6c ["COPY", "tmp:0:8", ["const:add:8"]]
- 00830a6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00830a6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00830a6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00830a6c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00830a6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00830a6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00830a6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00830a6c bytes 29752b91
+ 00830a6c bytes 29a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a5a2fc28fa5e3ad366fb8810219fdd"></a>

### [`00830c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md) → [`00830c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/00830c98.md) FUN_00830c98

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`006571b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md) [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`00761d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md) [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) [`00805f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 13件 [`006571b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md) [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`00805f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00805/00805f2c.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 86.03% / 新版 86.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 11件, `store_condition` 4件, `store_destination` 12件, `store_value` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00830d04",
      "incomplete_value": true,
      "site": "00830d10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00830d04",
      "incomplete_value": true,
      "site": "00830d10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00830d00",
      "incomplete_value": true,
      "site": "00830d18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:34f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830d00",
      "incomplete_value": true,
      "site": "00830d18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3dc:8"
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
      "definition_site": "00830de4",
      "incomplete_value": true,
      "site": "00830de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830de4",
      "incomplete_value": true,
      "site": "00830de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c01:8"
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
      "00830ccc",
      "PARAM",
      [
        "storage",
        "00c28ca8",
        null,
        null
      ]
    ],
    [
      "00830ce4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00830d00",
      "READ",
      [
        "storage",
        "002993dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00830ccc",
      "PARAM",
      [
        "storage",
        "00c28ce8",
        null,
        null
      ]
    ],
    [
      "00830ce4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00830d00",
      "READ",
      [
        "storage",
        "0029934f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md#insn-00830f34) · [`00831180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md#insn-00831180) · [`0083127c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md#insn-0083127c)
- 新版 `00830f34`（命令位置の公開資料なし） · `00831180`（命令位置の公開資料なし） · `0083127c`（命令位置の公開資料なし）

~~~diff
- 00830f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7f0:8"]]
- 00830f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00830f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:830:8"]]
+ 00830f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00830f34 bytes 09f903f9
+ 00830f34 bytes 091904f9
- 00831180 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:7f0:8"]]
- 00831180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00831180 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00831180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00831180 bytes e8fa03f9
+ 00831180 bytes e81a04f9
- 0083127c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:7f0:8"]]
- 0083127c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0083127c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 0083127c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0083127c bytes e8fa03f9
+ 0083127c bytes e81a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3e827999c5c0a3d819da56f60b96428"></a>

### [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md) → [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md) FUN_00831724

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`00689eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md) [`0089cc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089c/0089cc84.md) [`008acbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md) [`008d40c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d4/008d40c0.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 7件 [`00689eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007118bc.md) [`0089cc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089cc84.md) [`008acbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md) [`008d40c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d4/008d40c0.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 81.53% / 新版 81.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 22件, `store_condition` 4件, `store_destination` 33件, `store_value` 15件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083178c",
      "incomplete_value": true,
      "site": "00831798",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0083178c",
      "incomplete_value": true,
      "site": "00831798",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "00831788",
      "incomplete_value": true,
      "site": "008317a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:34f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831788",
      "incomplete_value": true,
      "site": "008317a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3dc:8"
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
      "definition_site": "0083186c",
      "incomplete_value": true,
      "site": "0083186c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083186c",
      "incomplete_value": true,
      "site": "0083186c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c01:8"
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
      "00831750",
      "PARAM",
      [
        "storage",
        "00c28ca8",
        null,
        null
      ]
    ],
    [
      "0083176c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00831788",
      "READ",
      [
        "storage",
        "002993dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00831750",
      "PARAM",
      [
        "storage",
        "00c28ce8",
        null,
        null
      ]
    ],
    [
      "0083176c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00831788",
      "READ",
      [
        "storage",
        "0029934f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008319bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md#insn-008319bc) · [`00831c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md#insn-00831c04) · [`00831d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md#insn-00831d00)
- 新版 `008319bc`（命令位置の公開資料なし） · `00831c04`（命令位置の公開資料なし） · `00831d00`（命令位置の公開資料なし）

~~~diff
- 008319bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7f0:8"]]
- 008319bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008319bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:830:8"]]
+ 008319bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008319bc bytes 09f903f9
+ 008319bc bytes 091904f9
- 00831c04 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:7f0:8"]]
- 00831c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00831c04 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00831c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00831c04 bytes e8fa03f9
+ 00831c04 bytes e81a04f9
- 00831d00 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:7f0:8"]]
- 00831d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00831d00 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00831d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00831d00 bytes e8fa03f9
+ 00831d00 bytes e81a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e16f5d2a6c8ba1079365f585c91fd02"></a>

### [`008321a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/008321a8.md) → [`008321a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/008321a8.md) FUN_008321a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`0064b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064b/0064b18c.md) [`0072a6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md) [`0072c090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072c/0072c090.md) [`00761d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761d08.md) [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) · 呼出先 9件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 11件 [`0064b18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md) [`0072a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md) [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) · 呼出先 9件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.83% / 新版 73.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 21件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008321f8",
      "incomplete_value": true,
      "site": "00832228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:368:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008321f8",
      "incomplete_value": true,
      "site": "00832228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f5:8"
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
      "definition_site": "008322a0",
      "incomplete_value": true,
      "site": "008322d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008322a0",
      "incomplete_value": true,
      "site": "008322d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a2:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00832420",
      "incomplete_value": false,
      "site": "00832420",
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
                "const:40:8"
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
      "definition_site": "00832420",
      "incomplete_value": false,
      "site": "00832420",
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
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008321e4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008321f8",
      "READ",
      [
        "storage",
        "002993f5",
        null,
        "string"
      ]
    ],
    [
      "00832248",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008321e4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008321f8",
      "READ",
      [
        "storage",
        "00299368",
        null,
        "string"
      ]
    ],
    [
      "00832248",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008321e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/008321a8.md#insn-008321e0) · [`008321f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/008321a8.md#insn-008321f0)
- 新版 `008321e0`（命令位置の公開資料なし） · `008321f0`（命令位置の公開資料なし）

~~~diff
- 008321e0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008321e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008321e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008321e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008321e0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008321e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008321e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008321e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008321e0 bytes 08e10091
+ 008321e0 bytes 08e10191
- 008321f0 ["COPY", "register:4048:8", ["const:299000:8"]]
- 008321f0 bytes 29d3fff0
+ 008321f0 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 008321f0 bytes 29d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0090aa7898a69e7cc2fb368309c1baf5"></a>

### [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md) → [`00832580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832580.md) FUN_00832580

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`006571b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md) [`00689eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md) [`007802c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) [`00805f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00805/00805f2c.md) · 呼出先 9件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 10件 [`006571b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md) [`00689eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007118bc.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`00805f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00805/00805f2c.md) · 呼出先 9件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.83% / 新版 73.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 21件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008325d0",
      "incomplete_value": true,
      "site": "00832600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:368:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008325d0",
      "incomplete_value": true,
      "site": "00832600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f5:8"
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
      "definition_site": "00832678",
      "incomplete_value": true,
      "site": "008326a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832678",
      "incomplete_value": true,
      "site": "008326a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a2:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008327f8",
      "incomplete_value": false,
      "site": "008327f8",
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
                "const:40:8"
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
      "definition_site": "008327f8",
      "incomplete_value": false,
      "site": "008327f8",
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
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008325bc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008325d0",
      "READ",
      [
        "storage",
        "002993f5",
        null,
        "string"
      ]
    ],
    [
      "00832620",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008325bc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008325d0",
      "READ",
      [
        "storage",
        "00299368",
        null,
        "string"
      ]
    ],
    [
      "00832620",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008325b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md#insn-008325b8) · [`008325c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md#insn-008325c8)
- 新版 `008325b8`（命令位置の公開資料なし） · `008325c8`（命令位置の公開資料なし）

~~~diff
- 008325b8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008325b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008325b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008325b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008325b8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008325b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008325b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008325b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008325b8 bytes 08e10091
+ 008325b8 bytes 08e10191
- 008325c8 ["COPY", "register:4048:8", ["const:299000:8"]]
- 008325c8 bytes 29d3fff0
+ 008325c8 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 008325c8 bytes 29d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a748614d811600a5805c14272a747fc"></a>

### [`00832d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832d28.md) → [`00832d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832d28.md) FUN_00832d28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`008722d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00872/008722d0.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`005416b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/005416b0.md)
- 新版 呼出元 2件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`008722d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722d0.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`005416b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00832ef0",
      "incomplete_value": false,
      "site": "00832efc",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832ef0",
      "incomplete_value": false,
      "site": "00832efc",
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
            "const:aa5:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00832f1c",
      "incomplete_value": false,
      "site": "00832f24",
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
            "const:b47:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832f1c",
      "incomplete_value": false,
      "site": "00832f24",
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
            "const:abc:8"
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
      "00832d9c",
      "PARAM",
      [
        "storage",
        "00296908",
        null,
        null
      ]
    ],
    [
      "00832dac",
      "PARAM",
      [
        "storage",
        "00296908",
        null,
        null
      ]
    ],
    [
      "00832ef0",
      "PARAM",
      [
        "storage",
        "002a0aa5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00832d9c",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ],
    [
      "00832dac",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ],
    [
      "00832ef0",
      "PARAM",
      [
        "storage",
        "002a0b30",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00832d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832d28.md#insn-00832d7c) · [`00832ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832d28.md#insn-00832ef0) · [`00832f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832d28.md#insn-00832f1c)
- 新版 `00832d7c`（命令位置の公開資料なし） · `00832ef0`（命令位置の公開資料なし） · `00832f1c`（命令位置の公開資料なし）

~~~diff
- 00832d7c ["COPY", "tmp:0:8", ["const:908:8"]]
- 00832d7c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00832d7c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00832d7c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00832d7c ["COPY", "tmp:0:8", ["const:87b:8"]]
+ 00832d7c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00832d7c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00832d7c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00832d7c bytes 94222491
+ 00832d7c bytes 94ee2191
- 00832ef0 ["COPY", "tmp:0:8", ["const:aa5:8"]]
- 00832ef0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00832ef0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00832ef0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00832ef0 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00832ef0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00832ef0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00832ef0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00832ef0 bytes 42942a91
+ 00832ef0 bytes 42c02c91
- 00832f1c ["COPY", "tmp:0:8", ["const:abc:8"]]
- 00832f1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00832f1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00832f1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00832f1c ["COPY", "tmp:0:8", ["const:b47:8"]]
+ 00832f1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00832f1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00832f1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00832f1c bytes 21f02a91
+ 00832f1c bytes 211c2d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-950fd1e574d1876c43682841084a7e5f"></a>

### [`00833158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md) → [`00833158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833158.md) FUN_00833158

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008737e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737e0.md) [`00873a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a48.md) [`008743ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743ec.md) [`00874574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874574.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)
- 新版 呼出元 4件 [`008737e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/008737e0.md) [`00873a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873a48.md) [`008743ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008743ec.md) [`00874574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874574.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008332b8",
      "incomplete_value": false,
      "site": "008332b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008332b8",
      "incomplete_value": false,
      "site": "008332b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00833378",
      "incomplete_value": false,
      "site": "00833378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00833378",
      "incomplete_value": false,
      "site": "00833378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "008332b8",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00833318",
      "READ",
      [
        "storage",
        "00c01a00",
        null,
        "undefined *"
      ]
    ],
    [
      "00833378",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008332b8",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ],
    [
      "00833318",
      "READ",
      [
        "storage",
        "00c01a50",
        null,
        "undefined *"
      ]
    ],
    [
      "00833378",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008332b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md#insn-008332b4) · [`00833374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md#insn-00833374)
- 新版 `008332b4`（命令位置の公開資料なし） · `00833374`（命令位置の公開資料なし）

~~~diff
- 008332b4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 008332b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008332b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008332b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008332b4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 008332b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008332b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008332b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008332b4 bytes 29612791
+ 008332b4 bytes 29a12891
- 00833374 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00833374 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00833374 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00833374 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00833374 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 00833374 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00833374 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00833374 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00833374 bytes 29612991
+ 00833374 bytes 29a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4394cc9bc7b53ee6e68bee7d663e6ad"></a>

### [`008336f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008336f0.md) → [`008336f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008336f0.md) FUN_008336f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`006fdbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fdbdc.md) [`008338d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008338d4.md) [`00833998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833998.md)
- 新版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) [`008338d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008338d4.md) [`00833998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833998.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008337a0",
      "incomplete_value": false,
      "site": "008337a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008337a0",
      "incomplete_value": false,
      "site": "008337a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0083376c",
      "READ",
      [
        "storage",
        "00293ddc",
        null,
        "string"
      ]
    ],
    [
      "008337a0",
      "DATA",
      [
        "storage",
        "00c020e8",
        null,
        "undefined *"
      ]
    ],
    [
      "008337f4",
      "READ",
      [
        "storage",
        "00c02108",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083376c",
      "READ",
      [
        "storage",
        "00293d4f",
        null,
        "string"
      ]
    ],
    [
      "008337a0",
      "DATA",
      [
        "storage",
        "00c02138",
        null,
        "undefined *"
      ]
    ],
    [
      "008337f4",
      "READ",
      [
        "storage",
        "00c02158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00833764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008336f0.md#insn-00833764) · [`00833798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008336f0.md#insn-00833798)
- 新版 `00833764`（命令位置の公開資料なし） · `00833798`（命令位置の公開資料なし）

~~~diff
- 00833764 ["COPY", "tmp:0:8", ["const:ddc:8"]]
- 00833764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00833764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00833764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00833764 ["COPY", "tmp:0:8", ["const:d4f:8"]]
+ 00833764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00833764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00833764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00833764 bytes 29713791
+ 00833764 bytes 293d3591
- 00833798 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00833798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00833798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00833798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00833798 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00833798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00833798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00833798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00833798 bytes 08a10391
+ 00833798 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3607377cdc4e424e59e5c37ff07b8a40"></a>

### [`008338d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008338d4.md) → [`008338d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008338d4.md) FUN_008338d4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008336f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008336f0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`009d7518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d7518.md) [`009d7520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d7520.md) [`009d7554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d7554.md) [`009d755c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d755c.md)
- 新版 呼出元 1件 [`008336f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008336f0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`009d755c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d7/009d755c.md) [`009d7564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d7/009d7564.md) [`009d7598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d7/009d7598.md) [`009d75a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d7/009d75a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.88% / 新版 93.88%

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
      "site": "0083390c",
      "value": [
        "leaf",
        "ram:9d7598:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083390c",
      "value": [
        "leaf",
        "ram:9d7554:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00833968",
      "value": [
        "leaf",
        "ram:9d755c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00833968",
      "value": [
        "leaf",
        "ram:9d7518:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083390c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d7554"
      ]
    ],
    [
      "00833968",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d7518"
      ]
    ]
  ],
  "added": [
    [
      "0083390c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d7598"
      ]
    ],
    [
      "00833968",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d755c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083390c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008338d4.md#insn-0083390c) · [`00833968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008338d4.md#insn-00833968) · [`008338f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008338d4.md#insn-008338f4)
- 新版 `0083390c`（命令位置の公開資料なし） · `00833968`（命令位置の公開資料なし） · `008338f4`（命令位置の公開資料なし）

~~~diff
- 0083390c ["INT_ADD", "register:40f0:8", ["const:83390c:8", "const:4:8"]]
- 0083390c ["CALL", null, ["ram:9d7554:8"]]
+ 0083390c ["INT_ADD", "register:40f0:8", ["const:83390c:8", "const:4:8"]]
+ 0083390c ["CALL", null, ["ram:9d7598:8"]]
- 0083390c bytes 128f0694
+ 0083390c bytes 238f0694
- 00833968 ["INT_ADD", "register:40f0:8", ["const:833968:8", "const:4:8"]]
- 00833968 ["CALL", null, ["ram:9d7518:8"]]
+ 00833968 ["INT_ADD", "register:40f0:8", ["const:833968:8", "const:4:8"]]
+ 00833968 ["CALL", null, ["ram:9d755c:8"]]
- 00833968 bytes ec8e0694
+ 00833968 bytes fd8e0694
- 008338f4 ["COPY", "register:40b0:8", ["const:4caf:8"]]
+ 008338f4 ["COPY", "register:40b0:8", ["const:4cb0:8"]]
- 008338f4 bytes f6958952
+ 008338f4 bytes 16968952
~~~


<a id="compare-89091a78d39f1edf48d0ee40587fad51"></a>

### [`00833998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833998.md) → [`00833998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833998.md) FUN_00833998

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008336f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/008336f0.md) · 呼出先 6件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`008336f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008336f0.md) · 呼出先 6件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008339ec",
      "incomplete_value": true,
      "site": "008339fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008339ec",
      "incomplete_value": true,
      "site": "008339fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:abf:8"
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
      "definition_site": "008339ec",
      "incomplete_value": true,
      "site": "008339fc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "008339ec",
      "incomplete_value": true,
      "site": "008339fc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "008339ec",
      "READ",
      [
        "storage",
        "002a0abf",
        null,
        "string"
      ]
    ],
    [
      "008339ec",
      "READ",
      [
        "storage",
        "002a0acf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008339ec",
      "READ",
      [
        "storage",
        "002a0b4a",
        null,
        "string"
      ]
    ],
    [
      "008339ec",
      "READ",
      [
        "storage",
        "002a0b5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008339e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833998.md#insn-008339e8)
- 新版 `008339e8`（命令位置の公開資料なし）

~~~diff
- 008339e8 ["COPY", "tmp:0:8", ["const:abf:8"]]
- 008339e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008339e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008339e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008339e8 ["COPY", "tmp:0:8", ["const:b4a:8"]]
+ 008339e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008339e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008339e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008339e8 bytes 08fd2a91
+ 008339e8 bytes 08292d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd79bd0450dc09290c1293cab3743a62"></a>

### [`00833b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833b3c.md) → [`00833b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833b3c.md) FUN_00833b3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`0089f5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089f/0089f5bc.md) [`008a1a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1a48.md) [`008a6770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6770.md) [`008a6e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6e74.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 5件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) [`0089f5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f5bc.md) [`008a1a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1a48.md) [`008a6770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6770.md) [`008a6e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e74.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00833b84",
      "incomplete_value": true,
      "site": "00833b84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00833b84",
      "incomplete_value": true,
      "site": "00833b84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "00833b64",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00833b64",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00833b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833b3c.md#insn-00833b5c)
- 新版 `00833b5c`（命令位置の公開資料なし）

~~~diff
- 00833b5c ["COPY", "tmp:0:8", ["const:a1:8"]]
- 00833b5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00833b5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00833b5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00833b5c ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 00833b5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00833b5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00833b5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00833b5c bytes 4a850291
+ 00833b5c bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2981b05b07fb36d4812a6ef7b2e39fbb"></a>

### [`00837abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837abc.md) → [`00837abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837abc.md) FUN_00837abc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/00808774.md) [`00837abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837abc.md) [`008847b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847b0.md) · 呼出先 3件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00837abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837abc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00837abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837abc.md) [`008847b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847b0.md) · 呼出先 3件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00837abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837abc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00837b58",
      "incomplete_value": true,
      "site": "00837b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00837b58",
      "incomplete_value": true,
      "site": "00837b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00837b50",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00837b58",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00837b50",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "00837b58",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00837b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837abc.md#insn-00837b50)
- 新版 `00837b50`（命令位置の公開資料なし）

~~~diff
- 00837b50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 00837b50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00837b50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 00837b50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00837b50 bytes 089142f9
+ 00837b50 bytes 08b942f9
~~~


<a id="compare-be887019446d6322905902912c82d106"></a>

### [`00838b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b24.md) → [`00838b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838b24.md) FUN_00838b24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00838b30",
      "incomplete_value": false,
      "site": "00838b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b30",
      "incomplete_value": false,
      "site": "00838b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00838b34",
      "DATA",
      [
        "storage",
        "00c00f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838b34",
      "DATA",
      [
        "storage",
        "00c00f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b24.md#insn-00838b30)
- 新版 `00838b30`（命令位置の公開資料なし）

~~~diff
- 00838b30 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00838b30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838b30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838b30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838b30 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838b30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838b30 bytes 29213d91
+ 00838b30 bytes 29613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f87e2d9ec678b90c883ffe638e1d04c6"></a>

### [`00838b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b44.md) → [`00838b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838b44.md) FUN_00838b44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838b4c",
      "incomplete_value": false,
      "site": "00838b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b4c",
      "incomplete_value": false,
      "site": "00838b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00838b50",
      "DATA",
      [
        "storage",
        "00c00f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838b50",
      "DATA",
      [
        "storage",
        "00c00f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b44.md#insn-00838b4c)
- 新版 `00838b4c`（命令位置の公開資料なし）

~~~diff
- 00838b4c ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00838b4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838b4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838b4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838b4c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838b4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838b4c bytes 29213d91
+ 00838b4c bytes 29613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03efb9fb35d1222ea6af41144215c1c4"></a>

### [`00838b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b80.md) → [`00838b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838b80.md) FUN_00838b80

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
      "definition_site": "00838ba4",
      "incomplete_value": false,
      "site": "00838ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838ba4",
      "incomplete_value": false,
      "site": "00838ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00838ba4",
      "DATA",
      [
        "storage",
        "00c00f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838ba4",
      "DATA",
      [
        "storage",
        "00c00f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b80.md#insn-00838ba0)
- 新版 `00838ba0`（命令位置の公開資料なし）

~~~diff
- 00838ba0 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00838ba0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838ba0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 bytes 29213d91
+ 00838ba0 bytes 29613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1e7498bc57c8e3499cf41f726e7122e"></a>

### [`00838da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838da4.md) → [`00838da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838da4.md) FUN_00838da4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00838db0",
      "incomplete_value": false,
      "site": "00838db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838db0",
      "incomplete_value": false,
      "site": "00838db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00838db4",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838db4",
      "DATA",
      [
        "storage",
        "00c01018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838da4.md#insn-00838dac) · [`00838db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838da4.md#insn-00838db0)
- 新版 `00838dac`（命令位置の公開資料なし） · `00838db0`（命令位置の公開資料なし）

~~~diff
- 00838dac ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00838dac ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00838dac bytes 491e0090
+ 00838dac bytes 491e00b0
- 00838db0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00838db0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838db0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838db0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00838db0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838db0 bytes 29213f91
+ 00838db0 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03152d8793d1906df75d1f364a816d63"></a>

### [`00838dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838dc4.md) → [`00838dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838dc4.md) FUN_00838dc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838dcc",
      "incomplete_value": false,
      "site": "00838dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838dcc",
      "incomplete_value": false,
      "site": "00838dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00838dd0",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838dd0",
      "DATA",
      [
        "storage",
        "00c01018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838dc4.md#insn-00838dc8) · [`00838dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838dc4.md#insn-00838dcc)
- 新版 `00838dc8`（命令位置の公開資料なし） · `00838dcc`（命令位置の公開資料なし）

~~~diff
- 00838dc8 ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00838dc8 ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00838dc8 bytes 491e0090
+ 00838dc8 bytes 491e00b0
- 00838dcc ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00838dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00838dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838dcc bytes 29213f91
+ 00838dcc bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f357962332bf1e80e9ee721c2eeb2ba"></a>

### [`00838e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e00.md) → [`00838e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838e00.md) FUN_00838e00

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
      "definition_site": "00838e24",
      "incomplete_value": false,
      "site": "00838e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838e24",
      "incomplete_value": false,
      "site": "00838e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00838e24",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838e24",
      "DATA",
      [
        "storage",
        "00c01018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e00.md#insn-00838e1c) · [`00838e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e00.md#insn-00838e20)
- 新版 `00838e1c`（命令位置の公開資料なし） · `00838e20`（命令位置の公開資料なし）

~~~diff
- 00838e1c ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00838e1c ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00838e1c bytes 491e0090
+ 00838e1c bytes 491e00b0
- 00838e20 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00838e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00838e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838e20 bytes 29213f91
+ 00838e20 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13b13f43d3faee92a484e5e2fe035fa1"></a>

### [`00838e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e50.md) → [`00838e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838e50.md) FUN_00838e50

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
      "definition_site": "00838e5c",
      "incomplete_value": false,
      "site": "00838e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838e5c",
      "incomplete_value": false,
      "site": "00838e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00838e5c",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838e5c",
      "DATA",
      [
        "storage",
        "00c01018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e50.md#insn-00838e54) · [`00838e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e50.md#insn-00838e58)
- 新版 `00838e54`（命令位置の公開資料なし） · `00838e58`（命令位置の公開資料なし）

~~~diff
- 00838e54 ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00838e54 ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00838e54 bytes 491e0090
+ 00838e54 bytes 491e00b0
- 00838e58 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00838e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00838e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838e58 bytes 29213f91
+ 00838e58 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-681823759174e071f0d4a34180b764a4"></a>

### [`00839024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839024.md) → [`00839024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839024.md) FUN_00839024

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
      "definition_site": "00839028",
      "incomplete_value": false,
      "site": "0083902c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839028",
      "incomplete_value": false,
      "site": "0083902c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0083902c",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083902c",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839024.md#insn-00839028)
- 新版 `00839028`（命令位置の公開資料なし）

~~~diff
- 00839028 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00839028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00839028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839028 bytes 08210191
+ 00839028 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad942a16a239f882ecc98b0a0853c230"></a>

### [`00839034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839034.md) → [`00839034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839034.md) FUN_00839034

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
      "definition_site": "00839044",
      "incomplete_value": false,
      "site": "0083904c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839044",
      "incomplete_value": false,
      "site": "0083904c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0083904c",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083904c",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839034.md#insn-00839044)
- 新版 `00839044`（命令位置の公開資料なし）

~~~diff
- 00839044 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00839044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00839044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839044 bytes 08210191
+ 00839044 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfc38fed7c1f8b2e38a30b9093341042"></a>

### [`00839074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839074.md) → [`00839074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md) FUN_00839074

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008216e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md) · 呼出先 3件 [`004759a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004759a4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) · 呼出先 3件 [`004759a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00839094",
      "incomplete_value": false,
      "site": "00839094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839094",
      "incomplete_value": false,
      "site": "00839094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00839094",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839094",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839074.md#insn-00839088)
- 新版 `00839088`（命令位置の公開資料なし）

~~~diff
- 00839088 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00839088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00839088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839088 bytes 08610291
+ 00839088 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8048c20d21d09bb58eeecf16ccb99de2"></a>

### [`00839140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839140.md) → [`00839140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839140.md) FUN_00839140

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00839158",
      "incomplete_value": false,
      "site": "0083915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839158",
      "incomplete_value": false,
      "site": "0083915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "0083915c",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083915c",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839140.md#insn-00839158)
- 新版 `00839158`（命令位置の公開資料なし）

~~~diff
- 00839158 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00839158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00839158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839158 bytes 29610291
+ 00839158 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a10c6a5394d869149619a3855a29498"></a>

### [`008391ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/008391ec.md) → [`008391ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008391ec.md) FUN_008391ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00839204",
      "incomplete_value": false,
      "site": "00839208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839204",
      "incomplete_value": false,
      "site": "00839208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00839208",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839208",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/008391ec.md#insn-00839204)
- 新版 `00839204`（命令位置の公開資料なし）

~~~diff
- 00839204 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00839204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00839204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839204 bytes 29610291
+ 00839204 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f0336a61258d06d02fc7df87ddb90a"></a>

### [`0083a270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a270.md) → [`0083a270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a270.md) FUN_0083a270

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a2b8",
      "incomplete_value": true,
      "site": "0083a2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083a2b8",
      "incomplete_value": true,
      "site": "0083a2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "0083a298",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a298",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a270.md#insn-0083a290)
- 新版 `0083a290`（命令位置の公開資料なし）

~~~diff
- 0083a290 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0083a290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0083a290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a290 bytes 4a850291
+ 0083a290 bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273d45cde6bcd2b9311a84a1e5e8eae4"></a>

### [`0083a718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a718.md) → [`0083a718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a718.md) FUN_0083a718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a760",
      "incomplete_value": true,
      "site": "0083a760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083a760",
      "incomplete_value": true,
      "site": "0083a760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "0083a740",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a740",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a718.md#insn-0083a738)
- 新版 `0083a738`（命令位置の公開資料なし）

~~~diff
- 0083a738 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0083a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0083a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a738 bytes 4a850291
+ 0083a738 bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d01de10eb8c4769b297e3ecdb1a84892"></a>

### [`0083a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a8a8.md) → [`0083a8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a8a8.md) FUN_0083a8a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a8f0",
      "incomplete_value": true,
      "site": "0083a8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083a8f0",
      "incomplete_value": true,
      "site": "0083a8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "0083a8d0",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a8d0",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a8a8.md#insn-0083a8c8)
- 新版 `0083a8c8`（命令位置の公開資料なし）

~~~diff
- 0083a8c8 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0083a8c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0083a8c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 bytes 4a850291
+ 0083a8c8 bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06db363ba2b26b0cfa12697c588a9c46"></a>

### [`0083aa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aa38.md) → [`0083aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aa38.md) FUN_0083aa38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`009dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc2c8.md) [`009dc3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc3f0.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 3件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) [`009dc30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc30c.md) [`009dc434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc434.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083aa80",
      "incomplete_value": true,
      "site": "0083aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083aa80",
      "incomplete_value": true,
      "site": "0083aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "0083aa60",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083aa60",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aa38.md#insn-0083aa58)
- 新版 `0083aa58`（命令位置の公開資料なし）

~~~diff
- 0083aa58 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0083aa58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0083aa58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 bytes 4a850291
+ 0083aa58 bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-467ed896d4f718cb2c7bd208ea9d9556"></a>

### [`0083abc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083abc0.md) → [`0083abc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083abc0.md) FUN_0083abc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083ac08",
      "incomplete_value": true,
      "site": "0083ac08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083ac08",
      "incomplete_value": true,
      "site": "0083ac08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "0083abe8",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083abe8",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083abe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083abc0.md#insn-0083abe0)
- 新版 `0083abe0`（命令位置の公開資料なし）

~~~diff
- 0083abe0 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0083abe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0083abe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 bytes 4a850291
+ 0083abe0 bytes 4aed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e388d566e907b3efe9f59cfb0f560e"></a>

### [`0083aed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aed8.md) → [`0083aed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aed8.md) FUN_0083aed8

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
      "definition_site": "0083aedc",
      "incomplete_value": false,
      "site": "0083aee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083aedc",
      "incomplete_value": false,
      "site": "0083aee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "0083aee0",
      "DATA",
      [
        "storage",
        "00c010f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083aee0",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aed8.md#insn-0083aedc)
- 新版 `0083aedc`（命令位置の公開資料なし）

~~~diff
- 0083aedc ["COPY", "tmp:0:8", ["const:f8:8"]]
- 0083aedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083aedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083aedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0083aedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083aedc bytes 08e10391
+ 0083aedc bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b517a8b935bb9890d19aae6e495ed195"></a>

### [`0083aee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aee8.md) → [`0083aee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aee8.md) FUN_0083aee8

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
      "definition_site": "0083aef8",
      "incomplete_value": false,
      "site": "0083af00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083aef8",
      "incomplete_value": false,
      "site": "0083af00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "0083af00",
      "DATA",
      [
        "storage",
        "00c010f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af00",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aee8.md#insn-0083aef8)
- 新版 `0083aef8`（命令位置の公開資料なし）

~~~diff
- 0083aef8 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 0083aef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0083aef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 bytes 08e10391
+ 0083aef8 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9521179c075f98366b5af883498ced29"></a>

### [`0083af28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af28.md) → [`0083af28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083af28.md) FUN_0083af28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083af4c",
      "incomplete_value": false,
      "site": "0083af4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083af4c",
      "incomplete_value": false,
      "site": "0083af4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "0083af4c",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af4c",
      "DATA",
      [
        "storage",
        "00c01198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083af48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af28.md#insn-0083af48)
- 新版 `0083af48`（命令位置の公開資料なし）

~~~diff
- 0083af48 ["COPY", "tmp:0:8", ["const:148:8"]]
- 0083af48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083af48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083af48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0083af48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083af48 bytes 08210591
+ 0083af48 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-402a9b113827afce4f2de91ca1218e4b"></a>

### [`0083af5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af5c.md) → [`0083af5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083af5c.md) FUN_0083af5c

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
      "definition_site": "0083af68",
      "incomplete_value": false,
      "site": "0083af68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083af68",
      "incomplete_value": false,
      "site": "0083af68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "0083af68",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af68",
      "DATA",
      [
        "storage",
        "00c01198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083af64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af5c.md#insn-0083af64)
- 新版 `0083af64`（命令位置の公開資料なし）

~~~diff
- 0083af64 ["COPY", "tmp:0:8", ["const:148:8"]]
- 0083af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0083af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083af64 bytes 29210591
+ 0083af64 bytes 29610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ddf58bbba67c5e7b0338ddbd0aca16"></a>

### [`0083afec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083afec.md) → [`0083afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083afec.md) FUN_0083afec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b010",
      "incomplete_value": false,
      "site": "0083b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b010",
      "incomplete_value": false,
      "site": "0083b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "0083b010",
      "DATA",
      [
        "storage",
        "00c011c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b010",
      "DATA",
      [
        "storage",
        "00c01218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083afec.md#insn-0083b00c)
- 新版 `0083b00c`（命令位置の公開資料なし）

~~~diff
- 0083b00c ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 0083b00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["COPY", "tmp:0:8", ["const:218:8"]]
+ 0083b00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b00c bytes 08210791
+ 0083b00c bytes 08610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d59ec57c2b606c382e05b7032c1373a"></a>

### [`0083b020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b020.md) → [`0083b020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b020.md) FUN_0083b020

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
      "definition_site": "0083b02c",
      "incomplete_value": false,
      "site": "0083b02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b02c",
      "incomplete_value": false,
      "site": "0083b02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "0083b02c",
      "DATA",
      [
        "storage",
        "00c011c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b02c",
      "DATA",
      [
        "storage",
        "00c01218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b020.md#insn-0083b028)
- 新版 `0083b028`（命令位置の公開資料なし）

~~~diff
- 0083b028 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 0083b028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 0083b028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b028 bytes 29210791
+ 0083b028 bytes 29610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa0eec1ef6232d2183d701b74d52856c"></a>

### [`0083b0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0b0.md) → [`0083b0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b0b0.md) FUN_0083b0b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b0d4",
      "incomplete_value": false,
      "site": "0083b0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b0d4",
      "incomplete_value": false,
      "site": "0083b0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "0083b0d4",
      "DATA",
      [
        "storage",
        "00c01248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b0d4",
      "DATA",
      [
        "storage",
        "00c01298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0b0.md#insn-0083b0d0)
- 新版 `0083b0d0`（命令位置の公開資料なし）

~~~diff
- 0083b0d0 ["COPY", "tmp:0:8", ["const:248:8"]]
- 0083b0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0083b0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 bytes 08210991
+ 0083b0d0 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6569c8ba19722b21256632bcbcc88a2a"></a>

### [`0083b0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0e4.md) → [`0083b0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b0e4.md) FUN_0083b0e4

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
      "definition_site": "0083b0f0",
      "incomplete_value": false,
      "site": "0083b0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b0f0",
      "incomplete_value": false,
      "site": "0083b0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "0083b0f0",
      "DATA",
      [
        "storage",
        "00c01248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b0f0",
      "DATA",
      [
        "storage",
        "00c01298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0e4.md#insn-0083b0ec)
- 新版 `0083b0ec`（命令位置の公開資料なし）

~~~diff
- 0083b0ec ["COPY", "tmp:0:8", ["const:248:8"]]
- 0083b0ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0083b0ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec bytes 29210991
+ 0083b0ec bytes 29610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26652f995ae40cfd9fec10ce29c69b3f"></a>

### [`0083b174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b174.md) → [`0083b174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b174.md) FUN_0083b174

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b198",
      "incomplete_value": false,
      "site": "0083b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b198",
      "incomplete_value": false,
      "site": "0083b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "0083b198",
      "DATA",
      [
        "storage",
        "00c012c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b198",
      "DATA",
      [
        "storage",
        "00c01318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b174.md#insn-0083b194)
- 新版 `0083b194`（命令位置の公開資料なし）

~~~diff
- 0083b194 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0083b194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0083b194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b194 bytes 08210b91
+ 0083b194 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f07d00667851a9e3cfde2e690e6e77a"></a>

### [`0083b1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b1a8.md) → [`0083b1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b1a8.md) FUN_0083b1a8

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
      "definition_site": "0083b1b4",
      "incomplete_value": false,
      "site": "0083b1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b1b4",
      "incomplete_value": false,
      "site": "0083b1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "0083b1b4",
      "DATA",
      [
        "storage",
        "00c012c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b1b4",
      "DATA",
      [
        "storage",
        "00c01318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b1a8.md#insn-0083b1b0)
- 新版 `0083b1b0`（命令位置の公開資料なし）

~~~diff
- 0083b1b0 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0083b1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0083b1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 bytes 29210b91
+ 0083b1b0 bytes 29610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4138ed0292d2833784698772b09b8bc"></a>

### [`0083b238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b238.md) → [`0083b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b238.md) FUN_0083b238

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b25c",
      "incomplete_value": false,
      "site": "0083b25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b25c",
      "incomplete_value": false,
      "site": "0083b25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "0083b25c",
      "DATA",
      [
        "storage",
        "00c01348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b25c",
      "DATA",
      [
        "storage",
        "00c01398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b238.md#insn-0083b258)
- 新版 `0083b258`（命令位置の公開資料なし）

~~~diff
- 0083b258 ["COPY", "tmp:0:8", ["const:348:8"]]
- 0083b258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0083b258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b258 bytes 08210d91
+ 0083b258 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eff1c581a2fbfef36f7086455bc7fe8"></a>

### [`0083b26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b26c.md) → [`0083b26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b26c.md) FUN_0083b26c

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
      "definition_site": "0083b278",
      "incomplete_value": false,
      "site": "0083b278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b278",
      "incomplete_value": false,
      "site": "0083b278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083b278",
      "DATA",
      [
        "storage",
        "00c01348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b278",
      "DATA",
      [
        "storage",
        "00c01398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b26c.md#insn-0083b274)
- 新版 `0083b274`（命令位置の公開資料なし）

~~~diff
- 0083b274 ["COPY", "tmp:0:8", ["const:348:8"]]
- 0083b274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0083b274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b274 bytes 29210d91
+ 0083b274 bytes 29610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e9895498ed14ca6a54de709573efffb"></a>

### [`0083b300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b300.md) → [`0083b300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b300.md) FUN_0083b300

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b324",
      "incomplete_value": true,
      "site": "0083b324",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b324",
      "incomplete_value": true,
      "site": "0083b324",
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
      "0083b324",
      "DATA",
      [
        "storage",
        "00c013c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b324",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b300.md#insn-0083b320)
- 新版 `0083b320`（命令位置の公開資料なし）

~~~diff
- 0083b320 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0083b320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0083b320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b320 bytes 08210f91
+ 0083b320 bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8eea7555b805450924fdd3de367f10a"></a>

### [`0083b334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b334.md) → [`0083b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b334.md) FUN_0083b334

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
      "definition_site": "0083b340",
      "incomplete_value": false,
      "site": "0083b340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b340",
      "incomplete_value": false,
      "site": "0083b340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083b340",
      "DATA",
      [
        "storage",
        "00c013c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b340",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b334.md#insn-0083b33c)
- 新版 `0083b33c`（命令位置の公開資料なし）

~~~diff
- 0083b33c ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0083b33c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b33c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b33c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0083b33c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b33c bytes 29210f91
+ 0083b33c bytes 29611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b281e16a817e4bd1ce15267dcc36b0"></a>

### [`0083b3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3a0.md) → [`0083b3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3a0.md) FUN_0083b3a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083b3c4",
      "incomplete_value": true,
      "site": "0083b3c4",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b3c4",
      "incomplete_value": true,
      "site": "0083b3c4",
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
            "const:448:8"
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
      "0083b3c4",
      "DATA",
      [
        "storage",
        "00c01448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b3c4",
      "DATA",
      [
        "storage",
        "00c01498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3a0.md#insn-0083b3c0)
- 新版 `0083b3c0`（命令位置の公開資料なし）

~~~diff
- 0083b3c0 ["COPY", "tmp:0:8", ["const:448:8"]]
- 0083b3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0083b3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 bytes 08211191
+ 0083b3c0 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeff4c1ab93de2ea14ec908e2d17a4ab"></a>

### [`0083b3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3d4.md) → [`0083b3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3d4.md) FUN_0083b3d4

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
      "definition_site": "0083b3e0",
      "incomplete_value": true,
      "site": "0083b3e0",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b3e0",
      "incomplete_value": true,
      "site": "0083b3e0",
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
            "const:448:8"
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
      "0083b3e0",
      "DATA",
      [
        "storage",
        "00c01448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b3e0",
      "DATA",
      [
        "storage",
        "00c01498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3d4.md#insn-0083b3dc)
- 新版 `0083b3dc`（命令位置の公開資料なし）

~~~diff
- 0083b3dc ["COPY", "tmp:0:8", ["const:448:8"]]
- 0083b3dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0083b3dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc bytes 29211191
+ 0083b3dc bytes 29611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77757565b6f33031bb6ba59e86b049dc"></a>

### [`0083b3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md) → [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) FUN_0083b3f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0042c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b5a0",
      "incomplete_value": true,
      "site": "0083b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b5a0",
      "incomplete_value": true,
      "site": "0083b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b754",
      "incomplete_value": false,
      "site": "0083b758",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:570:8"
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
      "definition_site": "0083b754",
      "incomplete_value": false,
      "site": "0083b758",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:520:8"
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
    "ordinal": 109,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083b5a0",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b700",
      "READ",
      [
        "storage",
        "00c014f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b758",
      "DATA",
      [
        "storage",
        "00be8530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b5a0",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b700",
      "READ",
      [
        "storage",
        "00c01540",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b758",
      "DATA",
      [
        "storage",
        "00be8580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md#insn-0083b598) · [`0083b74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md#insn-0083b74c)
- 新版 `0083b598`（命令位置の公開資料なし） · `0083b74c`（命令位置の公開資料なし）

~~~diff
- 0083b598 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0083b598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083b598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083b598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0083b598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083b598 bytes 4a211391
+ 0083b598 bytes 4a611491
- 0083b74c ["COPY", "tmp:0:8", ["const:520:8"]]
- 0083b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["COPY", "tmp:0:8", ["const:570:8"]]
+ 0083b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b74c bytes 08811491
+ 0083b74c bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a192e1ded7ffccb61c8b38b93cb33e10"></a>

### [`0083b938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b938.md) → [`0083b938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b938.md) FUN_0083b938

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md)

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
      "definition_site": "0083b940",
      "incomplete_value": false,
      "site": "0083b944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b940",
      "incomplete_value": false,
      "site": "0083b944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0083b944",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b944",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b938.md#insn-0083b940)
- 新版 `0083b940`（命令位置の公開資料なし）

~~~diff
- 0083b940 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0083b940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0083b940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b940 bytes 29211391
+ 0083b940 bytes 29611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93afe5835549af267701e946961c3681"></a>

### [`0083b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b958.md) → [`0083b958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b958.md) FUN_0083b958

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b960",
      "incomplete_value": false,
      "site": "0083b964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b960",
      "incomplete_value": false,
      "site": "0083b964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0083b964",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b964",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b958.md#insn-0083b960)
- 新版 `0083b960`（命令位置の公開資料なし）

~~~diff
- 0083b960 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0083b960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0083b960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b960 bytes 29211391
+ 0083b960 bytes 29611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39cea296f2dc05d81f9498e0c80f3be"></a>

### [`0083b994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b994.md) → [`0083b994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b994.md) FUN_0083b994

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b9c8",
      "incomplete_value": true,
      "site": "0083b9c8",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b9c8",
      "incomplete_value": true,
      "site": "0083b9c8",
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
            "const:4c8:8"
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
      "0083b9c8",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b9c8",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b994.md#insn-0083b9b8)
- 新版 `0083b9b8`（命令位置の公開資料なし）

~~~diff
- 0083b9b8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0083b9b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0083b9b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 bytes 29211391
+ 0083b9b8 bytes 29611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1114a4d0f226d0fdc522b162447e8d6"></a>

### [`0083ba24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083ba24.md) → [`0083ba24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083ba24.md) FUN_0083ba24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md)

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
      "definition_site": "0083ba4c",
      "incomplete_value": false,
      "site": "0083ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083ba4c",
      "incomplete_value": false,
      "site": "0083ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0083ba4c",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083ba4c",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ba44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083ba24.md#insn-0083ba44)
- 新版 `0083ba44`（命令位置の公開資料なし）

~~~diff
- 0083ba44 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0083ba44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0083ba44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 bytes 4a211391
+ 0083ba44 bytes 4a611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc68501669fa65de2f019272fc501e0"></a>

### [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) → [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) FUN_0083bb78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00829340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829340.md) [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00829340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829340.md) [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083bce8",
      "incomplete_value": false,
      "site": "0083bcf0",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083bce8",
      "incomplete_value": false,
      "site": "0083bcf0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083bda8",
      "incomplete_value": false,
      "site": "0083bdb0",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083bda8",
      "incomplete_value": false,
      "site": "0083bdb0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083bdc4",
      "incomplete_value": true,
      "site": "0083bdd0",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083bdc4",
      "incomplete_value": true,
      "site": "0083bdd0",
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
            "const:919:8"
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
      "0083bce8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083bda8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0083bdc4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083bce8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0083bda8",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0083bdc4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md#insn-0083bce8) · [`0083bda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md#insn-0083bda8) · [`0083bdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md#insn-0083bdc4)
- 新版 `0083bce8`（命令位置の公開資料なし） · `0083bda8`（命令位置の公開資料なし） · `0083bdc4`（命令位置の公開資料なし）

~~~diff
- 0083bce8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0083bce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0083bce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 bytes 21280c91
+ 0083bce8 bytes 21900e91
- 0083bda8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0083bda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0083bda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 bytes 21b80b91
+ 0083bda8 bytes 21e40d91
- 0083bdc4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0083bdc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083bdc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083bdc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083bdc4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0083bdc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bdc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bdc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083bdc4 bytes 21642491
+ 0083bdc4 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12bc48b0e9960a553aa8cb6a239c04f9"></a>

### [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) → [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) FUN_0083c478

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083c5d0",
      "incomplete_value": false,
      "site": "0083c5d8",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083c5d0",
      "incomplete_value": false,
      "site": "0083c5d8",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083c68c",
      "incomplete_value": false,
      "site": "0083c694",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083c68c",
      "incomplete_value": false,
      "site": "0083c694",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083c7a0",
      "incomplete_value": false,
      "site": "0083c7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083c7a0",
      "incomplete_value": false,
      "site": "0083c7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:919:8"
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
      "0083c5d0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083c68c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0083c6a4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083c5d0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0083c68c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0083c6a4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083c5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md#insn-0083c5d0) · [`0083c68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md#insn-0083c68c) · [`0083c6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md#insn-0083c6a4)
- 新版 `0083c5d0`（命令位置の公開資料なし） · `0083c68c`（命令位置の公開資料なし） · `0083c6a4`（命令位置の公開資料なし）

~~~diff
- 0083c5d0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0083c5d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0083c5d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 bytes 21280c91
+ 0083c5d0 bytes 21900e91
- 0083c68c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0083c68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083c68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083c68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0083c68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083c68c bytes 21b80b91
+ 0083c68c bytes 21e40d91
- 0083c6a4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0083c6a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083c6a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083c6a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083c6a4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0083c6a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c6a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c6a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083c6a4 bytes 21642491
+ 0083c6a4 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0695b2d22d3cf8f736ed5308b2d08e4"></a>

### [`0083cdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md) → [`0083cdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md) FUN_0083cdb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) [`0083cdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md) [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) [`0083cdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083cf00",
      "incomplete_value": false,
      "site": "0083cf08",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083cf00",
      "incomplete_value": false,
      "site": "0083cf08",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083cf24",
      "incomplete_value": false,
      "site": "0083cf30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083cf24",
      "incomplete_value": false,
      "site": "0083cf30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:919:8"
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
      "definition_site": "0083d058",
      "incomplete_value": false,
      "site": "0083d060",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d058",
      "incomplete_value": false,
      "site": "0083d060",
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
      "0083cf00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083cf24",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0083d058",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0083cf00",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0083cf24",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0083d058",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083cf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md#insn-0083cf00) · [`0083cf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md#insn-0083cf24) · [`0083d058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md#insn-0083d058)
- 新版 `0083cf00`（命令位置の公開資料なし） · `0083cf24`（命令位置の公開資料なし） · `0083d058`（命令位置の公開資料なし）

~~~diff
- 0083cf00 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0083cf00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0083cf00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 bytes 21280c91
+ 0083cf00 bytes 21900e91
- 0083cf24 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0083cf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083cf24 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0083cf24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083cf24 bytes 21642491
+ 0083cf24 bytes 21142291
- 0083d058 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0083d058 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083d058 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083d058 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0083d058 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083d058 bytes 21b80b91
+ 0083d058 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1998180213554b3d32675d4d5357e8c8"></a>

### [`0083d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5a0.md) → [`0083d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5a0.md) FUN_0083d5a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083d5c4",
      "incomplete_value": false,
      "site": "0083d5c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d5c4",
      "incomplete_value": false,
      "site": "0083d5c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "0083d5c4",
      "DATA",
      [
        "storage",
        "00c01568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083d5c4",
      "DATA",
      [
        "storage",
        "00c015b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5a0.md#insn-0083d5c0)
- 新版 `0083d5c0`（命令位置の公開資料なし）

~~~diff
- 0083d5c0 ["COPY", "tmp:0:8", ["const:568:8"]]
- 0083d5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0083d5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 bytes 08a11591
+ 0083d5c0 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-122860d9a922ae2a8ebd338a674b3cc1"></a>

### [`0083d5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5d4.md) → [`0083d5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5d4.md) FUN_0083d5d4

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
      "definition_site": "0083d5e0",
      "incomplete_value": false,
      "site": "0083d5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d5e0",
      "incomplete_value": false,
      "site": "0083d5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "0083d5e0",
      "DATA",
      [
        "storage",
        "00c01568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083d5e0",
      "DATA",
      [
        "storage",
        "00c015b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5d4.md#insn-0083d5dc)
- 新版 `0083d5dc`（命令位置の公開資料なし）

~~~diff
- 0083d5dc ["COPY", "tmp:0:8", ["const:568:8"]]
- 0083d5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0083d5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc bytes 29a11591
+ 0083d5dc bytes 29e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cea5152e0c198a8094be6f39819bf1d0"></a>

### [`0083d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md) → [`0083d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md) FUN_0083d5f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`0042aea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`0042aea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083d6d0",
      "incomplete_value": true,
      "site": "0083d6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d6d0",
      "incomplete_value": true,
      "site": "0083d6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc6:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083d7a0",
      "incomplete_value": false,
      "site": "0083d7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d7a0",
      "incomplete_value": false,
      "site": "0083d7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "0083d6d0",
      "READ",
      [
        "storage",
        "00292dc6",
        null,
        "string"
      ]
    ],
    [
      "0083d7a0",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0083d850",
      "READ",
      [
        "storage",
        "00c015f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083d6d0",
      "READ",
      [
        "storage",
        "00292d39",
        null,
        "string"
      ]
    ],
    [
      "0083d7a0",
      "DATA",
      [
        "storage",
        "00c01628",
        null,
        "undefined *"
      ]
    ],
    [
      "0083d850",
      "READ",
      [
        "storage",
        "00c01648",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md#insn-0083d6c8) · [`0083d79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md#insn-0083d79c)
- 新版 `0083d6c8`（命令位置の公開資料なし） · `0083d79c`（命令位置の公開資料なし）

~~~diff
- 0083d6c8 ["COPY", "tmp:0:8", ["const:dc6:8"]]
- 0083d6c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["COPY", "tmp:0:8", ["const:d39:8"]]
+ 0083d6c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 bytes 29193791
+ 0083d6c8 bytes 29e53491
- 0083d79c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0083d79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083d79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083d79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0083d79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083d79c bytes 08611791
+ 0083d79c bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a13a596901f1c8e44c19b9096d44856a"></a>

### [`0083da74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083da74.md) → [`0083da74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083da74.md) FUN_0083da74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0083da98",
      "incomplete_value": true,
      "site": "0083da98",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083da98",
      "incomplete_value": true,
      "site": "0083da98",
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
            "const:5d8:8"
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
      "0083da98",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083da98",
      "DATA",
      [
        "storage",
        "00c01628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083da94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083da74.md#insn-0083da94)
- 新版 `0083da94`（命令位置の公開資料なし）

~~~diff
- 0083da94 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0083da94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083da94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083da94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0083da94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083da94 bytes 08611791
+ 0083da94 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1cc1dcc21161059f68284dca7e5e63"></a>

### [`0083daa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083daa8.md) → [`0083daa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083daa8.md) FUN_0083daa8

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
      "definition_site": "0083dab4",
      "incomplete_value": false,
      "site": "0083dab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dab4",
      "incomplete_value": false,
      "site": "0083dab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "0083dab4",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083dab4",
      "DATA",
      [
        "storage",
        "00c01628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083daa8.md#insn-0083dab0)
- 新版 `0083dab0`（命令位置の公開資料なし）

~~~diff
- 0083dab0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0083dab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0083dab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 bytes 29611791
+ 0083dab0 bytes 29a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ac5849bfe1d68624676404415fe275"></a>

### [`0083db04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db04.md) → [`0083db04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db04.md) FUN_0083db04

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
      "definition_site": "0083db08",
      "incomplete_value": false,
      "site": "0083db0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db08",
      "incomplete_value": false,
      "site": "0083db0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083db0c",
      "DATA",
      [
        "storage",
        "00c01668",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083db0c",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db04.md#insn-0083db08)
- 新版 `0083db08`（命令位置の公開資料なし）

~~~diff
- 0083db08 ["COPY", "tmp:0:8", ["const:668:8"]]
- 0083db08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 0083db08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db08 bytes 08a11991
+ 0083db08 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

