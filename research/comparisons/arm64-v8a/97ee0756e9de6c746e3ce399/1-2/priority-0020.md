# v15.7.3 → v15.7.4 · 最優先の変更候補 (20)

[一覧の目次](README.md)

<a id="compare-7d291c1497e10cfb9248f4f069270ea6"></a>

### [`0057ba58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba58.md) → [`0057ba58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057ba58.md) FUN_0057ba58

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
      "definition_site": "0057ba5c",
      "incomplete_value": false,
      "site": "0057ba60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba5c",
      "incomplete_value": false,
      "site": "0057ba60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "0057ba60",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ba60",
      "DATA",
      [
        "storage",
        "00bf0f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba58.md#insn-0057ba5c)
- 新版 `0057ba5c`（命令位置の公開資料なし）

~~~diff
- 0057ba5c ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 0057ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0057ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba5c bytes 08c13a91
+ 0057ba5c bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c9e36b93e939e5c8f7f781ef51624c"></a>

### [`0057ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba68.md) → [`0057ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057ba68.md) FUN_0057ba68

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
      "definition_site": "0057ba78",
      "incomplete_value": false,
      "site": "0057ba80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ba78",
      "incomplete_value": false,
      "site": "0057ba80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "0057ba80",
      "DATA",
      [
        "storage",
        "00bf0eb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ba80",
      "DATA",
      [
        "storage",
        "00bf0f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057ba68.md#insn-0057ba78)
- 新版 `0057ba78`（命令位置の公開資料なし）

~~~diff
- 0057ba78 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 0057ba78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0057ba78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba78 bytes 08c13a91
+ 0057ba78 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c636ee5d10fa762a0fd96c7f764b8a75"></a>

### [`0057baa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057baa0.md) → [`0057baa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057baa0.md) _INIT_40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0057badc",
      "incomplete_value": true,
      "site": "0057baf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057badc",
      "incomplete_value": true,
      "site": "0057baf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb00",
      "incomplete_value": true,
      "site": "0057bb1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb00",
      "incomplete_value": true,
      "site": "0057bb1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb20",
      "incomplete_value": true,
      "site": "0057bb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057bb20",
      "incomplete_value": true,
      "site": "0057bb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057badc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057bb00",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057bb20",
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
      "0057badc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057bb00",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057bb20",
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

- 旧版 [`0057bacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057baa0.md#insn-0057bacc) · [`0057bad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057baa0.md#insn-0057bad4)
- 新版 `0057bacc`（命令位置の公開資料なし） · `0057bad4`（命令位置の公開資料なし）

~~~diff
- 0057bacc ["COPY", "tmp:0:8", ["const:748:8"]]
- 0057bacc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057bacc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057bacc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0057bacc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057bacc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057bacc bytes 73221d91
+ 0057bacc bytes 73221e91
- 0057bad4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057bad4 bytes 69e9ff90
+ 0057bad4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057bad4 bytes 69e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbde4461de2a631cf663b5fcb11cfa8f"></a>

### [`0057be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057be30.md) → [`0057be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057be30.md) FUN_0057be30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057be84",
      "incomplete_value": true,
      "site": "0057be84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057be84",
      "incomplete_value": true,
      "site": "0057be84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c094",
      "incomplete_value": true,
      "site": "0057c094",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c094",
      "incomplete_value": true,
      "site": "0057c094",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:69d:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c11c",
      "incomplete_value": false,
      "site": "0057c128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c11c",
      "incomplete_value": false,
      "site": "0057c128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057be68",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057c080",
      "READ",
      [
        "storage",
        "0029f69d",
        null,
        "string"
      ]
    ],
    [
      "0057c128",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057be68",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057c080",
      "READ",
      [
        "storage",
        "0029f728",
        null,
        "string"
      ]
    ],
    [
      "0057c128",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057be30.md#insn-0057be5c) · [`0057c078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057be30.md#insn-0057c078) · [`0057c118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057b/0057be30.md#insn-0057c118)
- 新版 `0057be5c`（命令位置の公開資料なし） · `0057c078`（命令位置の公開資料なし） · `0057c118`（命令位置の公開資料なし）

~~~diff
- 0057be5c ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057be5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057be5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057be5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057be5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057be5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057be5c bytes 4a691791
+ 0057be5c bytes 4ad11991
- 0057c078 ["COPY", "tmp:0:8", ["const:69d:8"]]
- 0057c078 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c078 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c078 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 0057c078 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c078 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c078 bytes 29751a91
+ 0057c078 bytes 29a11c91
- 0057c118 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c118 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057c118 bytes a8330090
+ 0057c118 bytes a83300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19493ca3d137bc4e5f1a4fc7a7176686"></a>

### [`0057c274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c274.md) → [`0057c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c274.md) FUN_0057c274

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f9b0.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c290",
      "incomplete_value": false,
      "site": "0057c294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c290",
      "incomplete_value": false,
      "site": "0057c294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "0057c294",
      "DATA",
      [
        "storage",
        "00bf0f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c294",
      "DATA",
      [
        "storage",
        "00bf0f70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c274.md#insn-0057c290)
- 新版 `0057c290`（命令位置の公開資料なし）

~~~diff
- 0057c290 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 0057c290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057c290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c290 bytes 08813c91
+ 0057c290 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963d10feb8ff1ac93b05e6b0ae93df72"></a>

### [`0057c2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c2c0.md) → [`0057c2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c2c0.md) FUN_0057c2c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c2e4",
      "incomplete_value": true,
      "site": "0057c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bf2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c2e4",
      "incomplete_value": true,
      "site": "0057c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c7f:8"
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
      "definition_site": "0057c2f8",
      "incomplete_value": true,
      "site": "0057c2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0057c2f8",
      "incomplete_value": true,
      "site": "0057c2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0057c2e4",
      "READ",
      [
        "storage",
        "00296c7f",
        null,
        "string"
      ]
    ],
    [
      "0057c2e8",
      "READ",
      [
        "storage",
        "00296c8e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057c2e4",
      "READ",
      [
        "storage",
        "00296bf2",
        null,
        "string"
      ]
    ],
    [
      "0057c2e8",
      "READ",
      [
        "storage",
        "00296c01",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c2c0.md#insn-0057c2dc) · [`0057c2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c2c0.md#insn-0057c2e0)
- 新版 `0057c2dc`（命令位置の公開資料なし） · `0057c2e0`（命令位置の公開資料なし）

~~~diff
- 0057c2dc ["COPY", "tmp:0:8", ["const:c7f:8"]]
- 0057c2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["COPY", "tmp:0:8", ["const:bf2:8"]]
+ 0057c2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c2dc bytes 08fd3191
+ 0057c2dc bytes 08c92f91
- 0057c2e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0057c2e0 bytes a9e9ff90
+ 0057c2e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0057c2e0 bytes a9e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4901dc742f538461b133c9bc312aa37e"></a>

### [`0057c468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c468.md) → [`0057c468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c468.md) FUN_0057c468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c484",
      "incomplete_value": false,
      "site": "0057c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c484",
      "incomplete_value": false,
      "site": "0057c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "0057c49c",
      "incomplete_value": false,
      "site": "0057c49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c49c",
      "incomplete_value": false,
      "site": "0057c49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "0057c48c",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ],
    [
      "0057c49c",
      "DATA",
      [
        "storage",
        "00bf0f78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057c48c",
      "DATA",
      [
        "storage",
        "00bf1078",
        null,
        "undefined *"
      ]
    ],
    [
      "0057c49c",
      "DATA",
      [
        "storage",
        "00bf0fc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c468.md#insn-0057c484) · [`0057c490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c468.md#insn-0057c490)
- 新版 `0057c484`（命令位置の公開資料なし） · `0057c490`（命令位置の公開資料なし）

~~~diff
- 0057c484 ["COPY", "tmp:0:8", ["const:28:8"]]
- 0057c484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c484 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0057c484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c484 bytes 08a10091
+ 0057c484 bytes 08e10191
- 0057c490 ["COPY", "register:4040:8", ["const:bf0000:8"]]
- 0057c490 bytes a8330090
+ 0057c490 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c490 bytes a8330090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49753838500332dae0f31edf9c622a9a"></a>

### [`0057c4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c4b0.md) → [`0057c4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c4b0.md) FUN_0057c4b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057c4dc",
      "incomplete_value": false,
      "site": "0057c4e0",
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
                "const:a50:8"
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
      "definition_site": "0057c4dc",
      "incomplete_value": false,
      "site": "0057c4e0",
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
      "0057c4e0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4e0",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c4b0.md#insn-0057c4d4)
- 新版 `0057c4d4`（命令位置の公開資料なし）

~~~diff
- 0057c4d4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4d4 bytes 08012891
+ 0057c4d4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261e2c9131162e626ec72f1c40c88e13"></a>

### [`0057c514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c514.md) → [`0057c514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c514.md) FUN_0057c514

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057c540",
      "incomplete_value": false,
      "site": "0057c544",
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
                "const:a50:8"
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
      "definition_site": "0057c540",
      "incomplete_value": false,
      "site": "0057c544",
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
      "0057c544",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c544",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c514.md#insn-0057c538)
- 新版 `0057c538`（命令位置の公開資料なし）

~~~diff
- 0057c538 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057c538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057c538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c538 bytes 08012891
+ 0057c538 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e5b82bd045d134a39dc34420822f9e"></a>

### [`0057c574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c574.md) → [`0057c574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c574.md) FUN_0057c574

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c5ac",
      "incomplete_value": false,
      "site": "0057c5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c5ac",
      "incomplete_value": false,
      "site": "0057c5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057c5b0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c5b0",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c574.md#insn-0057c5ac)
- 新版 `0057c5ac`（命令位置の公開資料なし）

~~~diff
- 0057c5ac ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057c5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057c5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c5ac bytes 29c12791
+ 0057c5ac bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4def737c8566f097fb71b6cf82820777"></a>

### [`0057c5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c5d4.md) → [`0057c5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c5d4.md) FUN_0057c5d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057c60c",
      "incomplete_value": false,
      "site": "0057c610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c60c",
      "incomplete_value": false,
      "site": "0057c610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057c610",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c610",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c5d4.md#insn-0057c60c)
- 新版 `0057c60c`（命令位置の公開資料なし）

~~~diff
- 0057c60c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057c60c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c60c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c60c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057c60c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c60c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c60c bytes 29c12791
+ 0057c60c bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f7a53b2f4272f46265add0f959c6382"></a>

### [`0057c630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c630.md) → [`0057c630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c630.md) FUN_0057c630

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
      "definition_site": "0057c634",
      "incomplete_value": false,
      "site": "0057c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c634",
      "incomplete_value": false,
      "site": "0057c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0057c638",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c638",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c630.md#insn-0057c630) · [`0057c634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c630.md#insn-0057c634)
- 新版 `0057c630`（命令位置の公開資料なし） · `0057c634`（命令位置の公開資料なし）

~~~diff
- 0057c630 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c630 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057c630 bytes a8330090
+ 0057c630 bytes a83300b0
- 0057c634 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0057c634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0057c634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c634 bytes 08613f91
+ 0057c634 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b47c43c3c023e60f0f57758aa9ac81"></a>

### [`0057c640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c640.md) → [`0057c640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c640.md) FUN_0057c640

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
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0057c658",
      "DATA",
      [
        "storage",
        "00bf0fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c658",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c640.md#insn-0057c64c) · [`0057c650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c640.md#insn-0057c650)
- 新版 `0057c64c`（命令位置の公開資料なし） · `0057c650`（命令位置の公開資料なし）

~~~diff
- 0057c64c ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0057c64c ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057c64c bytes a8330090
+ 0057c64c bytes a83300b0
- 0057c650 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c650 bytes 08613f91
+ 0057c650 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32af9c8564289e38950c5fd35d57eb1e"></a>

### [`0057c670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c670.md) → [`0057c670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c670.md) FUN_0057c670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c6a8",
      "incomplete_value": false,
      "site": "0057c6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6a8",
      "incomplete_value": false,
      "site": "0057c6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057c6ac",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057c6ac",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c670.md#insn-0057c6a8)
- 新版 `0057c6a8`（命令位置の公開資料なし）

~~~diff
- 0057c6a8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057c6a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057c6a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057c6a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057c6a8 bytes 29c12791
+ 0057c6a8 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-352843f4a8828f55397bdc6d2097fb56"></a>

### [`0057c6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6d4.md) → [`0057c6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c6d4.md) FUN_0057c6d4

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
      "definition_site": "0057c6d8",
      "incomplete_value": false,
      "site": "0057c6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6d8",
      "incomplete_value": false,
      "site": "0057c6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "0057c6dc",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c6dc",
      "DATA",
      [
        "storage",
        "00bf1078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6d4.md#insn-0057c6d8)
- 新版 `0057c6d8`（命令位置の公開資料なし）

~~~diff
- 0057c6d8 ["COPY", "tmp:0:8", ["const:28:8"]]
- 0057c6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0057c6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c6d8 bytes 08a10091
+ 0057c6d8 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7aadda681fd03571350a95f9655f4be"></a>

### [`0057c6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6e4.md) → [`0057c6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c6e4.md) FUN_0057c6e4

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
      "definition_site": "0057c6f4",
      "incomplete_value": false,
      "site": "0057c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c6f4",
      "incomplete_value": false,
      "site": "0057c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "0057c6fc",
      "DATA",
      [
        "storage",
        "00bf1028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c6fc",
      "DATA",
      [
        "storage",
        "00bf1078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c6e4.md#insn-0057c6f4)
- 新版 `0057c6f4`（命令位置の公開資料なし）

~~~diff
- 0057c6f4 ["COPY", "tmp:0:8", ["const:28:8"]]
- 0057c6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0057c6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c6f4 bytes 08a10091
+ 0057c6f4 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e485037e4f53e652cd0386eacd45c043"></a>

### [`0057c71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c71c.md) → [`0057c71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c71c.md) _INIT_41

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
      "definition_site": "0057c758",
      "incomplete_value": true,
      "site": "0057c774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c758",
      "incomplete_value": true,
      "site": "0057c774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c77c",
      "incomplete_value": true,
      "site": "0057c798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c77c",
      "incomplete_value": true,
      "site": "0057c798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c79c",
      "incomplete_value": true,
      "site": "0057c7b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c79c",
      "incomplete_value": true,
      "site": "0057c7b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057c758",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057c77c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057c79c",
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
      "0057c758",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057c77c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057c79c",
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

- 旧版 [`0057c748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c71c.md#insn-0057c748) · [`0057c750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057c71c.md#insn-0057c750)
- 新版 `0057c748`（命令位置の公開資料なし） · `0057c750`（命令位置の公開資料なし）

~~~diff
- 0057c748 ["COPY", "tmp:0:8", ["const:760:8"]]
- 0057c748 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057c748 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057c748 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0057c748 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c748 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057c748 bytes 73821d91
+ 0057c748 bytes 73821e91
- 0057c750 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057c750 bytes 49e9fff0
+ 0057c750 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057c750 bytes 49e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a491b8efd6ad2fb0dfa56e234241c905"></a>

### [`0057caac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057caac.md) → [`0057caac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057caac.md) FUN_0057caac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057caf8",
      "incomplete_value": true,
      "site": "0057caf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057caf8",
      "incomplete_value": true,
      "site": "0057caf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cba8",
      "incomplete_value": false,
      "site": "0057cbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cba8",
      "incomplete_value": false,
      "site": "0057cbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "0057cbcc",
      "incomplete_value": false,
      "site": "0057cbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cbcc",
      "incomplete_value": false,
      "site": "0057cbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "0057cadc",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057cbb4",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbd4",
      "DATA",
      [
        "storage",
        "00bf1078",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cadc",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057cbb4",
      "DATA",
      [
        "storage",
        "00bf11a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbd4",
      "DATA",
      [
        "storage",
        "00bf10c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057caac.md#insn-0057cad0) · [`0057cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057caac.md#insn-0057cba8) · [`0057cbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057caac.md#insn-0057cbcc)
- 新版 `0057cad0`（命令位置の公開資料なし） · `0057cba8`（命令位置の公開資料なし） · `0057cbcc`（命令位置の公開資料なし）

~~~diff
- 0057cad0 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057cad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057cad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057cad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057cad0 bytes 4a691791
+ 0057cad0 bytes 4ad11991
- 0057cba8 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0057cba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 0057cba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cba8 bytes 08410591
+ 0057cba8 bytes 08810691
- 0057cbcc ["COPY", "tmp:0:8", ["const:78:8"]]
- 0057cbcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cbcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cbcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cbcc ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 0057cbcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cbcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cbcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cbcc bytes 08e10191
+ 0057cbcc bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c551cbfda06160cc6c44fb1c9e2913cc"></a>

### [`0057cc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cc9c.md) → [`0057cc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cc9c.md) FUN_0057cc9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e0ec.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e0ec.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ccb8",
      "incomplete_value": false,
      "site": "0057ccbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ccb8",
      "incomplete_value": false,
      "site": "0057ccbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057ccbc",
      "DATA",
      [
        "storage",
        "00bf1098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ccbc",
      "DATA",
      [
        "storage",
        "00bf10e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ccb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cc9c.md#insn-0057ccb8)
- 新版 `0057ccb8`（命令位置の公開資料なし）

~~~diff
- 0057ccb8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0057ccb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0057ccb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ccb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ccb8 bytes 08610291
+ 0057ccb8 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8bed9304581d3e7414b6ad80a84bbd3"></a>

### [`0057cedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cedc.md) → [`0057cedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cedc.md) FUN_0057cedc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057cf08",
      "incomplete_value": false,
      "site": "0057cf0c",
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
                "const:a50:8"
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
      "definition_site": "0057cf08",
      "incomplete_value": false,
      "site": "0057cf0c",
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
      "0057cf0c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cf0c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cedc.md#insn-0057cf00)
- 新版 `0057cf00`（命令位置の公開資料なし）

~~~diff
- 0057cf00 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057cf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057cf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cf00 bytes 08012891
+ 0057cf00 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3ec2beed7edde608be1d5618ef41fb"></a>

### [`0057cf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cf40.md) → [`0057cf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cf40.md) FUN_0057cf40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057cf6c",
      "incomplete_value": false,
      "site": "0057cf70",
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
                "const:a50:8"
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
      "definition_site": "0057cf6c",
      "incomplete_value": false,
      "site": "0057cf70",
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
      "0057cf70",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cf70",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cf40.md#insn-0057cf64)
- 新版 `0057cf64`（命令位置の公開資料なし）

~~~diff
- 0057cf64 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057cf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057cf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cf64 bytes 08012891
+ 0057cf64 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c682315a53829880f284de3e63c955"></a>

### [`0057cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cfe0.md) → [`0057cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cfe0.md) FUN_0057cfe0

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
      "definition_site": "0057cfe4",
      "incomplete_value": false,
      "site": "0057cfe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cfe4",
      "incomplete_value": false,
      "site": "0057cfe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0057cfe8",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057cfe8",
      "DATA",
      [
        "storage",
        "00bf11a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cfe0.md#insn-0057cfe4)
- 新版 `0057cfe4`（命令位置の公開資料なし）

~~~diff
- 0057cfe4 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0057cfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 0057cfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cfe4 bytes 08410591
+ 0057cfe4 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d56dd12bc4b2ae0f34cf0cd7ba2acb"></a>

### [`0057cff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cff0.md) → [`0057cff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cff0.md) FUN_0057cff0

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
      "definition_site": "0057d000",
      "incomplete_value": false,
      "site": "0057d008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d000",
      "incomplete_value": false,
      "site": "0057d008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "0057d008",
      "DATA",
      [
        "storage",
        "00bf1150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d008",
      "DATA",
      [
        "storage",
        "00bf11a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057c/0057cff0.md#insn-0057d000)
- 新版 `0057d000`（命令位置の公開資料なし）

~~~diff
- 0057d000 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0057d000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 0057d000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d000 bytes 08410591
+ 0057d000 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b6b092232859b4aed8d8556fdf65bc"></a>

### [`0057d020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d020.md) → [`0057d020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d020.md) FUN_0057d020

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057d02c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d02c",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d020.md#insn-0057d028)
- 新版 `0057d028`（命令位置の公開資料なし）

~~~diff
- 0057d028 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057d028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057d028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d028 bytes 29c12791
+ 0057d028 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd2996519a8e1ff2b0643bebe9938094"></a>

### [`0057d054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d054.md) → [`0057d054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d054.md) FUN_0057d054

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
      "definition_site": "0057d064",
      "incomplete_value": false,
      "site": "0057d06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d064",
      "incomplete_value": false,
      "site": "0057d06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "0057d06c",
      "DATA",
      [
        "storage",
        "00bf11a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d06c",
      "DATA",
      [
        "storage",
        "00bf11f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d054.md#insn-0057d064)
- 新版 `0057d064`（命令位置の公開資料なし）

~~~diff
- 0057d064 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0057d064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0057d064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d064 bytes 08810691
+ 0057d064 bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc26e6614793bdf681795d1f570d37a"></a>

### [`0057d08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d08c.md) → [`0057d08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d08c.md) _INIT_42

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0057d0c8",
      "incomplete_value": true,
      "site": "0057d0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d0c8",
      "incomplete_value": true,
      "site": "0057d0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d12c",
      "incomplete_value": true,
      "site": "0057d144",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0057d12c",
      "incomplete_value": true,
      "site": "0057d144",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d148",
      "incomplete_value": true,
      "site": "0057d164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d148",
      "incomplete_value": true,
      "site": "0057d164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057d0c8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057d0ec",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057d10c",
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
      "0057d0c8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057d0ec",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057d10c",
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

- 旧版 [`0057d0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d08c.md#insn-0057d0b8) · [`0057d0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d08c.md#insn-0057d0c0)
- 新版 `0057d0b8`（命令位置の公開資料なし） · `0057d0c0`（命令位置の公開資料なし）

~~~diff
- 0057d0b8 ["COPY", "tmp:0:8", ["const:778:8"]]
- 0057d0b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0057d0b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d0b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057d0b8 bytes 73e21d91
+ 0057d0b8 bytes 73e21e91
- 0057d0c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057d0c0 bytes 49e9ffd0
+ 0057d0c0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057d0c0 bytes 49e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8242320d19b104ddfc17714d70f78ca3"></a>

### [`0057d41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d41c.md) → [`0057d41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d41c.md) FUN_0057d41c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057d424",
      "incomplete_value": false,
      "site": "0057d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d424",
      "incomplete_value": false,
      "site": "0057d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057d428",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d428",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d41c.md#insn-0057d424)
- 新版 `0057d424`（命令位置の公開資料なし）

~~~diff
- 0057d424 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057d424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057d424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d424 bytes 29c12791
+ 0057d424 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e3fcc3ee34b0b54607d1116959a0f3"></a>

### [`0057d43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d43c.md) → [`0057d43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d43c.md) FUN_0057d43c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057d444",
      "incomplete_value": false,
      "site": "0057d448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d444",
      "incomplete_value": false,
      "site": "0057d448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057d448",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d448",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d43c.md#insn-0057d444)
- 新版 `0057d444`（命令位置の公開資料なし）

~~~diff
- 0057d444 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057d444 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d444 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d444 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057d444 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d444 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d444 bytes 29c12791
+ 0057d444 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9145c81bb7e8ecce60da1f65cc3b1139"></a>

### [`0057d47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d47c.md) → [`0057d47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d47c.md) FUN_0057d47c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d4c8",
      "incomplete_value": true,
      "site": "0057d4c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d4c8",
      "incomplete_value": true,
      "site": "0057d4c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d578",
      "incomplete_value": false,
      "site": "0057d584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d578",
      "incomplete_value": false,
      "site": "0057d584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
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
      "definition_site": "0057d59c",
      "incomplete_value": false,
      "site": "0057d5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d59c",
      "incomplete_value": false,
      "site": "0057d5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "0057d4ac",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057d584",
      "DATA",
      [
        "storage",
        "00bf12c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d5a4",
      "DATA",
      [
        "storage",
        "00bf11f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d4ac",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057d584",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d5a4",
      "DATA",
      [
        "storage",
        "00bf1240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d47c.md#insn-0057d4a0) · [`0057d578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d47c.md#insn-0057d578) · [`0057d59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d47c.md#insn-0057d59c)
- 新版 `0057d4a0`（命令位置の公開資料なし） · `0057d578`（命令位置の公開資料なし） · `0057d59c`（命令位置の公開資料なし）

~~~diff
- 0057d4a0 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057d4a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057d4a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d4a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057d4a0 bytes 4a691791
+ 0057d4a0 bytes 4ad11991
- 0057d578 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0057d578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057d578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d578 bytes 08210b91
+ 0057d578 bytes 08610c91
- 0057d59c ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 0057d59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["COPY", "tmp:0:8", ["const:240:8"]]
+ 0057d59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d59c bytes 08c10791
+ 0057d59c bytes 08010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1c949c387589d3061054bc56c0e1137"></a>

### [`0057d670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d670.md) → [`0057d670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d670.md) FUN_0057d670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0057d68c",
      "incomplete_value": true,
      "site": "0057d68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d68c",
      "incomplete_value": true,
      "site": "0057d68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ed:8"
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
      "0057d67c",
      "READ",
      [
        "storage",
        "002a16ed",
        null,
        "string"
      ]
    ],
    [
      "0057d684",
      "READ",
      [
        "storage",
        "002a16f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057d67c",
      "READ",
      [
        "storage",
        "002a1778",
        null,
        "string"
      ]
    ],
    [
      "0057d684",
      "READ",
      [
        "storage",
        "002a177f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d670.md#insn-0057d678)
- 新版 `0057d678`（命令位置の公開資料なし）

~~~diff
- 0057d678 ["COPY", "tmp:0:8", ["const:6ed:8"]]
- 0057d678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057d678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057d678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 0057d678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057d678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057d678 bytes 4ab51b91
+ 0057d678 bytes 4ae11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-551dcd12d98bb0e37b5e895c7f258ac3"></a>

### [`0057d6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d6c8.md) → [`0057d6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d6c8.md) FUN_0057d6c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d6e4",
      "incomplete_value": false,
      "site": "0057d6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d6e4",
      "incomplete_value": false,
      "site": "0057d6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "definition_site": "0057d6fc",
      "incomplete_value": false,
      "site": "0057d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d6fc",
      "incomplete_value": false,
      "site": "0057d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "0057d6ec",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d6fc",
      "DATA",
      [
        "storage",
        "00bf1228",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057d6ec",
      "DATA",
      [
        "storage",
        "00bf1368",
        null,
        "undefined *"
      ]
    ],
    [
      "0057d6fc",
      "DATA",
      [
        "storage",
        "00bf1278",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d6c8.md#insn-0057d6e4) · [`0057d6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d6c8.md#insn-0057d6f0)
- 新版 `0057d6e4`（命令位置の公開資料なし） · `0057d6f0`（命令位置の公開資料なし）

~~~diff
- 0057d6e4 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0057d6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0057d6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d6e4 bytes 08610c91
+ 0057d6e4 bytes 08a10d91
- 0057d6f0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057d6f0 bytes a8330090
+ 0057d6f0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057d6f0 bytes a8330090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa62d61cdac2f6be4b6bd3aa463ed3f4"></a>

### [`0057d710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d710.md) → [`0057d710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d710.md) FUN_0057d710

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d72c",
      "incomplete_value": true,
      "site": "0057d730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0057d72c",
      "incomplete_value": true,
      "site": "0057d730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0057d724",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d730",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d724",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "0057d730",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d710.md#insn-0057d724)
- 新版 `0057d724`（命令位置の公開資料なし）

~~~diff
- 0057d724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 0057d724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057d724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 0057d724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057d724 bytes 087142f9
+ 0057d724 bytes 089942f9
~~~


<a id="compare-b391c8da548bd5bac31a691a22583b66"></a>

### [`0057d760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d760.md) → [`0057d760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d760.md) FUN_0057d760

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
      "definition_site": "0057d764",
      "incomplete_value": false,
      "site": "0057d768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d764",
      "incomplete_value": false,
      "site": "0057d768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "0057d768",
      "DATA",
      [
        "storage",
        "00bf12c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d768",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d760.md#insn-0057d764)
- 新版 `0057d764`（命令位置の公開資料なし）

~~~diff
- 0057d764 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0057d764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057d764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d764 bytes 08210b91
+ 0057d764 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6848d0898a30c30fd32e43f99803c472"></a>

### [`0057d7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7a0.md) → [`0057d7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d7a0.md) FUN_0057d7a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057d7a8",
      "incomplete_value": false,
      "site": "0057d7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7a8",
      "incomplete_value": false,
      "site": "0057d7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057d7ac",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d7ac",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7a0.md#insn-0057d7a8)
- 新版 `0057d7a8`（命令位置の公開資料なし）

~~~diff
- 0057d7a8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057d7a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057d7a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057d7a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057d7a8 bytes 29c12791
+ 0057d7a8 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83d0441639e5802c66675499faf11406"></a>

### [`0057d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7c4.md) → [`0057d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d7c4.md) FUN_0057d7c4

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
      "definition_site": "0057d7c8",
      "incomplete_value": false,
      "site": "0057d7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7c8",
      "incomplete_value": false,
      "site": "0057d7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0057d7cc",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d7cc",
      "DATA",
      [
        "storage",
        "00bf1368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7c4.md#insn-0057d7c8)
- 新版 `0057d7c8`（命令位置の公開資料なし）

~~~diff
- 0057d7c8 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0057d7c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0057d7c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d7c8 bytes 08610c91
+ 0057d7c8 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ace8c928dfb7a2a4552b473e06e6b08"></a>

### [`0057d7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7d4.md) → [`0057d7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d7d4.md) FUN_0057d7d4

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
      "definition_site": "0057d7e4",
      "incomplete_value": false,
      "site": "0057d7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d7e4",
      "incomplete_value": false,
      "site": "0057d7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0057d7ec",
      "DATA",
      [
        "storage",
        "00bf1318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d7ec",
      "DATA",
      [
        "storage",
        "00bf1368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d7d4.md#insn-0057d7e4)
- 新版 `0057d7e4`（命令位置の公開資料なし）

~~~diff
- 0057d7e4 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0057d7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0057d7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057d7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057d7e4 bytes 08610c91
+ 0057d7e4 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58ce0e8cced2b51bba0eb6ee33e59ceb"></a>

### [`0057d80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d80c.md) → [`0057d80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d80c.md) _INIT_43

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
      "definition_site": "0057d848",
      "incomplete_value": true,
      "site": "0057d864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d848",
      "incomplete_value": true,
      "site": "0057d864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d86c",
      "incomplete_value": true,
      "site": "0057d888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d86c",
      "incomplete_value": true,
      "site": "0057d888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d88c",
      "incomplete_value": true,
      "site": "0057d8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057d88c",
      "incomplete_value": true,
      "site": "0057d8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057d848",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057d86c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057d88c",
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
      "0057d848",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057d86c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057d88c",
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

- 旧版 [`0057d838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d80c.md#insn-0057d838) · [`0057d840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057d80c.md#insn-0057d840)
- 新版 `0057d838`（命令位置の公開資料なし） · `0057d840`（命令位置の公開資料なし）

~~~diff
- 0057d838 ["COPY", "tmp:0:8", ["const:790:8"]]
- 0057d838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057d838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057d838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0057d838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057d838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057d838 bytes 73421e91
+ 0057d838 bytes 73421f91
- 0057d840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057d840 bytes 49e9ffd0
+ 0057d840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057d840 bytes 49e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b13bf8b7feb55c53292d22fca7fad6"></a>

### [`0057db9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057db9c.md) → [`0057db9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057db9c.md) FUN_0057db9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dbe8",
      "incomplete_value": true,
      "site": "0057dbe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbe8",
      "incomplete_value": true,
      "site": "0057dbe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dd08",
      "incomplete_value": true,
      "site": "0057dd08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dd08",
      "incomplete_value": true,
      "site": "0057dd08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:752:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dd5c",
      "incomplete_value": false,
      "site": "0057dd68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dd5c",
      "incomplete_value": false,
      "site": "0057dd68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0057dbcc",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057dcf8",
      "READ",
      [
        "storage",
        "002a5752",
        null,
        "string"
      ]
    ],
    [
      "0057dd68",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dbcc",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057dcf8",
      "READ",
      [
        "storage",
        "002a57dd",
        null,
        "string"
      ]
    ],
    [
      "0057dd68",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057db9c.md#insn-0057dbc0) · [`0057dcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057db9c.md#insn-0057dcf0) · [`0057dd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057db9c.md#insn-0057dd5c)
- 新版 `0057dbc0`（命令位置の公開資料なし） · `0057dcf0`（命令位置の公開資料なし） · `0057dd5c`（命令位置の公開資料なし）

~~~diff
- 0057dbc0 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057dbc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057dbc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057dbc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057dbc0 bytes 4a691791
+ 0057dbc0 bytes 4ad11991
- 0057dcf0 ["COPY", "tmp:0:8", ["const:752:8"]]
- 0057dcf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["COPY", "tmp:0:8", ["const:7dd:8"]]
+ 0057dcf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057dcf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057dcf0 bytes 29491d91
+ 0057dcf0 bytes 29751f91
- 0057dd5c ["COPY", "tmp:0:8", ["const:440:8"]]
- 0057dd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0057dd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dd5c bytes 08011191
+ 0057dd5c bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30334b784c1115a27ce6235d2e18e6c"></a>

### [`0057de8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057de8c.md) → [`0057de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057de8c.md) FUN_0057de8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058ff20.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dea8",
      "incomplete_value": false,
      "site": "0057deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dea8",
      "incomplete_value": false,
      "site": "0057deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0057deac",
      "DATA",
      [
        "storage",
        "00bf1388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057deac",
      "DATA",
      [
        "storage",
        "00bf13d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057de8c.md#insn-0057dea8)
- 新版 `0057dea8`（命令位置の公開資料なし）

~~~diff
- 0057dea8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0057dea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0057dea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dea8 bytes 08210e91
+ 0057dea8 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5736be93bcab355eaaa71a0bf48604"></a>

### [`0057df28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057df28.md) → [`0057df28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057df28.md) FUN_0057df28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057df88",
      "incomplete_value": true,
      "site": "0057df88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057df88",
      "incomplete_value": true,
      "site": "0057df88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:169:8"
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
      "definition_site": "0057e05c",
      "incomplete_value": true,
      "site": "0057e05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:571:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e05c",
      "incomplete_value": true,
      "site": "0057e05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
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
      "definition_site": "0057e060",
      "incomplete_value": true,
      "site": "0057e060",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0057e060",
      "incomplete_value": true,
      "site": "0057e060",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0057df80",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "0057e010",
      "PARAM",
      [
        "storage",
        "0029e299",
        null,
        "string"
      ]
    ],
    [
      "0057e030",
      "PARAM",
      [
        "storage",
        "002a65e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057df80",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "0057e010",
      "PARAM",
      [
        "storage",
        "0029e324",
        null,
        "string"
      ]
    ],
    [
      "0057e030",
      "PARAM",
      [
        "storage",
        "002a667f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057df7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057df28.md#insn-0057df7c) · [`0057e010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057df28.md#insn-0057e010) · [`0057e030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057d/0057df28.md#insn-0057e030)
- 新版 `0057df7c`（命令位置の公開資料なし） · `0057e010`（命令位置の公開資料なし） · `0057e030`（命令位置の公開資料なし）

~~~diff
- 0057df7c ["COPY", "tmp:0:8", ["const:169:8"]]
- 0057df7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057df7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057df7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["COPY", "tmp:0:8", ["const:1f4:8"]]
+ 0057df7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057df7c bytes 08a50591
+ 0057df7c bytes 08d10791
- 0057e010 ["COPY", "tmp:0:8", ["const:299:8"]]
- 0057e010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057e010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057e010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["COPY", "tmp:0:8", ["const:324:8"]]
+ 0057e010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057e010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057e010 bytes 21640a91
+ 0057e010 bytes 21900c91
- 0057e030 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0057e030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057e030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057e030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 0057e030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057e030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057e030 bytes 00941791
+ 0057e030 bytes 00fc1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54bc1c912c49a33c0039fb2345e555c9"></a>

### [`0057e1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e1b8.md) → [`0057e1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e1b8.md) FUN_0057e1b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e1d4",
      "incomplete_value": false,
      "site": "0057e1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e1d4",
      "incomplete_value": false,
      "site": "0057e1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "definition_site": "0057e1ec",
      "incomplete_value": false,
      "site": "0057e1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e1ec",
      "incomplete_value": false,
      "site": "0057e1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0057e1dc",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e1ec",
      "DATA",
      [
        "storage",
        "00bf13e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057e1dc",
      "DATA",
      [
        "storage",
        "00bf14e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e1ec",
      "DATA",
      [
        "storage",
        "00bf1430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e1b8.md#insn-0057e1d4) · [`0057e1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e1b8.md#insn-0057e1e0)
- 新版 `0057e1d4`（命令位置の公開資料なし） · `0057e1e0`（命令位置の公開資料なし）

~~~diff
- 0057e1d4 ["COPY", "tmp:0:8", ["const:490:8"]]
- 0057e1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e1d4 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0057e1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e1d4 bytes 08411291
+ 0057e1d4 bytes 08811391
- 0057e1e0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057e1e0 bytes 883300f0
+ 0057e1e0 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057e1e0 bytes 883300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a302919d3291cf5916b42bf4cfa5e0"></a>

### [`0057e200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e200.md) → [`0057e200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e200.md) FUN_0057e200

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057e22c",
      "incomplete_value": false,
      "site": "0057e230",
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
                "const:a50:8"
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
      "definition_site": "0057e22c",
      "incomplete_value": false,
      "site": "0057e230",
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
      "0057e230",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e230",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e200.md#insn-0057e224)
- 新版 `0057e224`（命令位置の公開資料なし）

~~~diff
- 0057e224 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057e224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057e224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e224 bytes 08012891
+ 0057e224 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b2769c63fa83414f84c4bf8815a69a3"></a>

### [`0057e264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e264.md) → [`0057e264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e264.md) FUN_0057e264

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057e290",
      "incomplete_value": false,
      "site": "0057e294",
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
                "const:a50:8"
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
      "definition_site": "0057e290",
      "incomplete_value": false,
      "site": "0057e294",
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
      "0057e294",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e294",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e264.md#insn-0057e288)
- 新版 `0057e288`（命令位置の公開資料なし）

~~~diff
- 0057e288 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e288 bytes 08012891
+ 0057e288 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f7e27190ec380e1dd83beb405572c2"></a>

### [`0057e2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e2c4.md) → [`0057e2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e2c4.md) FUN_0057e2c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057e2d0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057e2d0",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e2c4.md#insn-0057e2cc)
- 新版 `0057e2cc`（命令位置の公開資料なし）

~~~diff
- 0057e2cc ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057e2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057e2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e2cc bytes 29c12791
+ 0057e2cc bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9d6ce5a54325f8a89a8ab776b81736"></a>

### [`0057e304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e304.md) → [`0057e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e304.md) FUN_0057e304

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
      "definition_site": "0057e308",
      "incomplete_value": false,
      "site": "0057e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e308",
      "incomplete_value": false,
      "site": "0057e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0057e30c",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e30c",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e304.md#insn-0057e308)
- 新版 `0057e308`（命令位置の公開資料なし）

~~~diff
- 0057e308 ["COPY", "tmp:0:8", ["const:440:8"]]
- 0057e308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0057e308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e308 bytes 08011191
+ 0057e308 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0357b48ac9db80b6d328f096f6af8e95"></a>

### [`0057e314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e314.md) → [`0057e314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e314.md) FUN_0057e314

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
      "definition_site": "0057e324",
      "incomplete_value": false,
      "site": "0057e32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e324",
      "incomplete_value": false,
      "site": "0057e32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "0057e32c",
      "DATA",
      [
        "storage",
        "00bf1440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e32c",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e314.md#insn-0057e324)
- 新版 `0057e324`（命令位置の公開資料なし）

~~~diff
- 0057e324 ["COPY", "tmp:0:8", ["const:440:8"]]
- 0057e324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 0057e324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e324 bytes 08011191
+ 0057e324 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84fdf2d13715b711aea2500bb295e751"></a>

### [`0057e344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e344.md) → [`0057e344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e344.md) FUN_0057e344

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0057e34c",
      "incomplete_value": false,
      "site": "0057e350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e34c",
      "incomplete_value": false,
      "site": "0057e350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057e350",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057e350",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e344.md#insn-0057e34c)
- 新版 `0057e34c`（命令位置の公開資料なし）

~~~diff
- 0057e34c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057e34c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e34c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e34c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057e34c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e34c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e34c bytes 29c12791
+ 0057e34c bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fed70aed8eb8b7135eb3e123c94194d"></a>

### [`0057e368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e368.md) → [`0057e368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e368.md) FUN_0057e368

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
      "definition_site": "0057e36c",
      "incomplete_value": false,
      "site": "0057e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e36c",
      "incomplete_value": false,
      "site": "0057e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "0057e370",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e370",
      "DATA",
      [
        "storage",
        "00bf14e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e368.md#insn-0057e36c)
- 新版 `0057e36c`（命令位置の公開資料なし）

~~~diff
- 0057e36c ["COPY", "tmp:0:8", ["const:490:8"]]
- 0057e36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0057e36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e36c bytes 08411291
+ 0057e36c bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d89c56d6e70b87db6f01e192f470d7"></a>

### [`0057e378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e378.md) → [`0057e378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e378.md) FUN_0057e378

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
      "definition_site": "0057e388",
      "incomplete_value": false,
      "site": "0057e390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e388",
      "incomplete_value": false,
      "site": "0057e390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "0057e390",
      "DATA",
      [
        "storage",
        "00bf1490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e390",
      "DATA",
      [
        "storage",
        "00bf14e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e378.md#insn-0057e388)
- 新版 `0057e388`（命令位置の公開資料なし）

~~~diff
- 0057e388 ["COPY", "tmp:0:8", ["const:490:8"]]
- 0057e388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0057e388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e388 bytes 08411291
+ 0057e388 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd82bfb3bf36671c87f1a47a8be20d74"></a>

### [`0057e3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e3b0.md) → [`0057e3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e3b0.md) _INIT_44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e3ec",
      "incomplete_value": true,
      "site": "0057e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e3ec",
      "incomplete_value": true,
      "site": "0057e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e410",
      "incomplete_value": true,
      "site": "0057e42c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e410",
      "incomplete_value": true,
      "site": "0057e42c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e430",
      "incomplete_value": true,
      "site": "0057e44c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057e430",
      "incomplete_value": true,
      "site": "0057e44c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057e3ec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057e410",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057e430",
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
      "0057e3ec",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057e410",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057e430",
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

- 旧版 [`0057e3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e3b0.md#insn-0057e3dc) · [`0057e3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e3b0.md#insn-0057e3e4)
- 新版 `0057e3dc`（命令位置の公開資料なし） · `0057e3e4`（命令位置の公開資料なし）

~~~diff
- 0057e3dc ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0057e3dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0057e3dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057e3dc bytes 73a21e91
+ 0057e3dc bytes 73a21f91
- 0057e3e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057e3e4 bytes 49e9ffb0
+ 0057e3e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057e3e4 bytes 49e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4805ebb96519380eb63fa8d8565d6f65"></a>

### [`0057e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md) → [`0057e740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e740.md) FUN_0057e740

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0057f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f400.md) [`0057f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0057f400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f400.md) [`0057f660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f660.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.66% / 新版 97.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e794",
      "incomplete_value": true,
      "site": "0057e794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e794",
      "incomplete_value": true,
      "site": "0057e794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e8b0",
      "incomplete_value": true,
      "site": "0057e8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9bf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e8b0",
      "incomplete_value": true,
      "site": "0057e8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:925:8"
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
      "0057e778",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057e8b0",
      "READ",
      [
        "storage",
        "002a6925",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e778",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057e8b0",
      "READ",
      [
        "storage",
        "002a69bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md#insn-0057e76c) · [`0057e8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md#insn-0057e8a8)
- 新版 `0057e76c`（命令位置の公開資料なし） · `0057e8a8`（命令位置の公開資料なし）

~~~diff
- 0057e76c ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057e76c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057e76c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057e76c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057e76c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057e76c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057e76c bytes 4a691791
+ 0057e76c bytes 4ad11991
- 0057e8a8 ["COPY", "tmp:0:8", ["const:925:8"]]
- 0057e8a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["COPY", "tmp:0:8", ["const:9bf:8"]]
+ 0057e8a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e8a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e8a8 bytes 29952491
+ 0057e8a8 bytes 29fd2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1df099a2338d89cb3108ce9b75b9822"></a>

### [`0057ec78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ec78.md) → [`0057ec78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ec78.md) FUN_0057ec78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00772358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772358.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`00772358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772358.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ec98",
      "incomplete_value": true,
      "site": "0057eca4",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ec98",
      "incomplete_value": true,
      "site": "0057eca4",
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
            "const:500:8"
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
      "0057eca4",
      "DATA",
      [
        "storage",
        "00bf1500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057eca4",
      "DATA",
      [
        "storage",
        "00bf1550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ec98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ec78.md#insn-0057ec98)
- 新版 `0057ec98`（命令位置の公開資料なし）

~~~diff
- 0057ec98 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0057ec98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0057ec98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057ec98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ec98 bytes 29011491
+ 0057ec98 bytes 29411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe10b17bbd09a44ad58c94ab0304e6ef"></a>

### [`0057eccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057eccc.md) → [`0057eccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057eccc.md) FUN_0057eccc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5de:8"
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
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0057ecf0",
      "incomplete_value": true,
      "site": "0057ed04",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
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
      "definition_site": "0057ed08",
      "incomplete_value": true,
      "site": "0057ed08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "0057ed08",
      "incomplete_value": true,
      "site": "0057ed08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5de",
        null,
        "string"
      ]
    ],
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5ee",
        null,
        "string"
      ]
    ],
    [
      "0057ecf8",
      "READ",
      [
        "storage",
        "0029b5fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5dc",
        null,
        "string"
      ]
    ],
    [
      "0057ecf0",
      "READ",
      [
        "storage",
        "0029b5ec",
        null,
        "string"
      ]
    ],
    [
      "0057ecf8",
      "READ",
      [
        "storage",
        "0029b5fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ece8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057eccc.md#insn-0057ece8) · [`0057ecec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057eccc.md#insn-0057ecec)
- 新版 `0057ece8`（命令位置の公開資料なし） · `0057ecec`（命令位置の公開資料なし）

~~~diff
- 0057ece8 ["COPY", "tmp:0:8", ["const:5de:8"]]
- 0057ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 0057ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ece8 bytes 08791791
+ 0057ece8 bytes 08711791
- 0057ecec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0057ecec bytes 89e9fff0
+ 0057ecec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0057ecec bytes 89e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-288212f8dfb2f7aa75ff6fb5b9c09f1d"></a>

### [`0057ed1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ed1c.md) → [`0057ed1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ed1c.md) FUN_0057ed1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00579/0057945c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/0057945c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057ed5c",
      "incomplete_value": false,
      "site": "0057ed64",
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
            "const:ab4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ed5c",
      "incomplete_value": false,
      "site": "0057ed64",
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
            "const:b41:8"
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
      "definition_site": "0057ee04",
      "incomplete_value": false,
      "site": "0057ee0c",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ee04",
      "incomplete_value": false,
      "site": "0057ee0c",
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
            "const:196:8"
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
      "0057ed5c",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "0057ede4",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "0057ee04",
      "PARAM",
      [
        "storage",
        "002a3196",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ed5c",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "0057ede4",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "0057ee04",
      "PARAM",
      [
        "storage",
        "002a3221",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ed5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ed1c.md#insn-0057ed5c) · [`0057ed88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ed1c.md#insn-0057ed88) · [`0057ee04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ed1c.md#insn-0057ee04)
- 新版 `0057ed5c`（命令位置の公開資料なし） · `0057ed88`（命令位置の公開資料なし） · `0057ee04`（命令位置の公開資料なし）

~~~diff
- 0057ed5c ["COPY", "tmp:0:8", ["const:b41:8"]]
- 0057ed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["COPY", "tmp:0:8", ["const:ab4:8"]]
+ 0057ed5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ed5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057ed5c bytes 21042d91
+ 0057ed5c bytes 21d02a91
- 0057ed88 ["COPY", "tmp:0:8", ["const:b43:8"]]
- 0057ed88 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["COPY", "tmp:0:8", ["const:ab6:8"]]
+ 0057ed88 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ed88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0057ed88 bytes b50e2d91
+ 0057ed88 bytes b5da2a91
- 0057ee04 ["COPY", "tmp:0:8", ["const:196:8"]]
- 0057ee04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["COPY", "tmp:0:8", ["const:221:8"]]
+ 0057ee04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057ee04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057ee04 bytes 21580691
+ 0057ee04 bytes 21840891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-820a0dc2b560a354dbe1ac096e839a87"></a>

### [`0057ef60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ef60.md) → [`0057ef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ef60.md) FUN_0057ef60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ef7c",
      "incomplete_value": false,
      "site": "0057ef84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ef7c",
      "incomplete_value": false,
      "site": "0057ef84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "0057ef94",
      "incomplete_value": false,
      "site": "0057ef94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ef94",
      "incomplete_value": false,
      "site": "0057ef94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0057ef84",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ef94",
      "DATA",
      [
        "storage",
        "00bf1558",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ef84",
      "DATA",
      [
        "storage",
        "00bf1658",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ef94",
      "DATA",
      [
        "storage",
        "00bf15a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ef7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ef60.md#insn-0057ef7c) · [`0057ef88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ef60.md#insn-0057ef88)
- 新版 `0057ef7c`（命令位置の公開資料なし） · `0057ef88`（命令位置の公開資料なし）

~~~diff
- 0057ef7c ["COPY", "tmp:0:8", ["const:608:8"]]
- 0057ef7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ef7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ef7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ef7c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0057ef7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ef7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ef7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ef7c bytes 08211891
+ 0057ef7c bytes 08611991
- 0057ef88 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057ef88 bytes 883300f0
+ 0057ef88 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057ef88 bytes 883300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8c51ecb525c5bbc95cc5fa026784011"></a>

### [`0057efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057efa8.md) → [`0057efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057efa8.md) FUN_0057efa8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0057f054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f054.md) [`007718f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00771/007718f4.md) [`0077246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/0077246c.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`0057f054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f054.md) [`007718f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007718f4.md) [`0077246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/0077246c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f014",
      "incomplete_value": false,
      "site": "0057f018",
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
                "const:a50:8"
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
      "definition_site": "0057f014",
      "incomplete_value": false,
      "site": "0057f018",
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
      "0057f018",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f018",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057efa8.md#insn-0057f00c)
- 新版 `0057f00c`（命令位置の公開資料なし）

~~~diff
- 0057f00c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0057f00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0057f00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f00c bytes 08012891
+ 0057f00c bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21de22d1c1970c7ac0072465b07aa212"></a>

### [`0057f078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f078.md) → [`0057f078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f078.md) FUN_0057f078

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f0e0",
      "incomplete_value": false,
      "site": "0057f0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f0e0",
      "incomplete_value": false,
      "site": "0057f0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057f0e4",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f0e4",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f078.md#insn-0057f0e0)
- 新版 `0057f0e0`（命令位置の公開資料なし）

~~~diff
- 0057f0e0 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057f0e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057f0e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f0e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f0e0 bytes 29c12791
+ 0057f0e0 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-792c805f460865b117f6540ae1944b74"></a>

### [`0057f110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f110.md) → [`0057f110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f110.md) FUN_0057f110

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f178",
      "incomplete_value": false,
      "site": "0057f17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f178",
      "incomplete_value": false,
      "site": "0057f17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057f17c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f17c",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f110.md#insn-0057f178)
- 新版 `0057f178`（命令位置の公開資料なし）

~~~diff
- 0057f178 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057f178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057f178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f178 bytes 29c12791
+ 0057f178 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-872aecdcb48b84d12d6e1e86a73a1dc3"></a>

### [`0057f38c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f38c.md) → [`0057f38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f38c.md) FUN_0057f38c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0057f1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f1a0.md) [`0057f400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0057f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f1a0.md) [`0057f400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0057f398",
      "incomplete_value": false,
      "site": "0057f39c",
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
      "definition_site": "0057f398",
      "incomplete_value": false,
      "site": "0057f39c",
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
      "0057f398",
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
      "0057f398",
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

- 旧版 [`0057f398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f38c.md#insn-0057f398)
- 新版 `0057f398`（命令位置の公開資料なし）

~~~diff
- 0057f398 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0057f398 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057f398 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057f398 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0057f398 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057f398 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057f398 bytes 000c0c91
+ 0057f398 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b4e18547edf9d20f3425d364f6c3a0"></a>

### [`0057f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md) → [`0057f660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f660.md) FUN_0057f660

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0057e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057e740.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`0057f1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f1a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0057e740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057e740.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`0057f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f1a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f698",
      "incomplete_value": false,
      "site": "0057f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f698",
      "incomplete_value": false,
      "site": "0057f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0057f6a4",
      "DATA",
      [
        "storage",
        "00bf15b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057f6e0",
      "DATA",
      [
        "storage",
        "00bf14e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f6a4",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ],
    [
      "0057f6e0",
      "DATA",
      [
        "storage",
        "00bf1530",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md#insn-0057f698) · [`0057f6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f660.md#insn-0057f6dc)
- 新版 `0057f698`（命令位置の公開資料なし） · `0057f6dc`（命令位置の公開資料なし）

~~~diff
- 0057f698 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0057f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0057f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f698 bytes 08e11691
+ 0057f698 bytes 08211891
- 0057f6dc ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 0057f6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["COPY", "tmp:0:8", ["const:530:8"]]
+ 0057f6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f6dc bytes 08811391
+ 0057f6dc bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0df2735f16c8f4e3e950d8f520725953"></a>

### [`0057f750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f750.md) → [`0057f750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f750.md) FUN_0057f750

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
      "definition_site": "0057f760",
      "incomplete_value": false,
      "site": "0057f768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f760",
      "incomplete_value": false,
      "site": "0057f768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0057f768",
      "DATA",
      [
        "storage",
        "00bf15b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f768",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f750.md#insn-0057f760)
- 新版 `0057f760`（命令位置の公開資料なし）

~~~diff
- 0057f760 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0057f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0057f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f760 bytes 08e11691
+ 0057f760 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a412a011eb99d66bd52a85fcde6d45e9"></a>

### [`0057f780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f780.md) → [`0057f780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f780.md) FUN_0057f780

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f7e8",
      "incomplete_value": false,
      "site": "0057f7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f7e8",
      "incomplete_value": false,
      "site": "0057f7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0057f7ec",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057f7ec",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f780.md#insn-0057f7e8)
- 新版 `0057f7e8`（命令位置の公開資料なし）

~~~diff
- 0057f7e8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0057f7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0057f7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f7e8 bytes 29c12791
+ 0057f7e8 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03ba951e961d2e6b92f199cb5444844"></a>

### [`0057f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f81c.md) → [`0057f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f81c.md) FUN_0057f81c

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
      "definition_site": "0057f820",
      "incomplete_value": false,
      "site": "0057f824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f820",
      "incomplete_value": false,
      "site": "0057f824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "0057f824",
      "DATA",
      [
        "storage",
        "00bf1608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057f824",
      "DATA",
      [
        "storage",
        "00bf1658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f81c.md#insn-0057f820)
- 新版 `0057f820`（命令位置の公開資料なし）

~~~diff
- 0057f820 ["COPY", "tmp:0:8", ["const:608:8"]]
- 0057f820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057f820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057f820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0057f820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057f820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057f820 bytes 08211891
+ 0057f820 bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e650ac926550f57bce810a8127cc279"></a>

### [`0057f864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f864.md) → [`0057f864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f864.md) _INIT_45

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f8a0",
      "incomplete_value": true,
      "site": "0057f8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057f8a0",
      "incomplete_value": true,
      "site": "0057f8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057fa94",
      "incomplete_value": true,
      "site": "0057fa98",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fa94",
      "incomplete_value": true,
      "site": "0057fa98",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057f8a0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0057f8c4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0057f8e4",
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
      "0057f8a0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057f8c4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057f8e4",
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

- 旧版 [`0057f890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f864.md#insn-0057f890) · [`0057f898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057f864.md#insn-0057f898)
- 新版 `0057f890`（命令位置の公開資料なし） · `0057f898`（命令位置の公開資料なし）

~~~diff
- 0057f890 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 0057f890 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057f890 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057f890 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 0057f890 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057f890 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057f890 bytes 73021f91
+ 0057f890 bytes 73022091
- 0057f898 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0057f898 bytes 49e9ff90
+ 0057f898 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0057f898 bytes 49e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49073776ab76376e21ae968cefb45a4a"></a>

### [`0057fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fbf4.md) → [`0057fbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057fbf4.md) FUN_0057fbf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fdf8",
      "incomplete_value": false,
      "site": "0057fe04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fdf8",
      "incomplete_value": false,
      "site": "0057fe04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fe1c",
      "incomplete_value": false,
      "site": "0057fe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fe1c",
      "incomplete_value": false,
      "site": "0057fe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057fc24",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0057fe04",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ],
    [
      "0057fe24",
      "DATA",
      [
        "storage",
        "00bf1658",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057fc24",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0057fe04",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ],
    [
      "0057fe24",
      "DATA",
      [
        "storage",
        "00bf16a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fbf4.md#insn-0057fc18) · [`0057fdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fbf4.md#insn-0057fdf8) · [`0057fe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fbf4.md#insn-0057fe1c)
- 新版 `0057fc18`（命令位置の公開資料なし） · `0057fdf8`（命令位置の公開資料なし） · `0057fe1c`（命令位置の公開資料なし）

~~~diff
- 0057fc18 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 0057fc18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 0057fc18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fc18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057fc18 bytes 4a691791
+ 0057fc18 bytes 4ad11991
- 0057fdf8 ["COPY", "tmp:0:8", ["const:730:8"]]
- 0057fdf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0057fdf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fdf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057fdf8 bytes 08c11c91
+ 0057fdf8 bytes 08011e91
- 0057fe1c ["COPY", "tmp:0:8", ["const:658:8"]]
- 0057fe1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057fe1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057fe1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057fe1c ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 0057fe1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fe1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057fe1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057fe1c bytes 08611991
+ 0057fe1c bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c493bcf9ea9654c143ff9eea8dc09b9c"></a>

### [`0057ff6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ff6c.md) → [`0057ff6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057ff6c.md) FUN_0057ff6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ff88",
      "incomplete_value": false,
      "site": "0057ff90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ff88",
      "incomplete_value": false,
      "site": "0057ff90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "0057ffa0",
      "incomplete_value": false,
      "site": "0057ffa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ffa0",
      "incomplete_value": false,
      "site": "0057ffa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "0057ff90",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ffa0",
      "DATA",
      [
        "storage",
        "00bf1678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ff90",
      "DATA",
      [
        "storage",
        "00bf17d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ffa0",
      "DATA",
      [
        "storage",
        "00bf16c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ff88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ff6c.md#insn-0057ff88) · [`0057ff94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ff6c.md#insn-0057ff94)
- 新版 `0057ff88`（命令位置の公開資料なし） · `0057ff94`（命令位置の公開資料なし）

~~~diff
- 0057ff88 ["COPY", "tmp:0:8", ["const:780:8"]]
- 0057ff88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0057ff88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ff88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ff88 bytes 08011e91
+ 0057ff88 bytes 08411f91
- 0057ff94 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 0057ff94 bytes 883300d0
+ 0057ff94 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 0057ff94 bytes 883300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90feef0853cfefc3687ed461b7dbd597"></a>

### [`0057ffb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ffb4.md) → [`0057ffb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057ffb4.md) FUN_0057ffb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ffd0",
      "incomplete_value": true,
      "site": "0057ffd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0057ffd0",
      "incomplete_value": true,
      "site": "0057ffd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0057ffc8",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057ffd4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ffc8",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "0057ffd4",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ffc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057ffb4.md#insn-0057ffc8)
- 新版 `0057ffc8`（命令位置の公開資料なし）

~~~diff
- 0057ffc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 0057ffc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057ffc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 0057ffc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057ffc8 bytes 087142f9
+ 0057ffc8 bytes 089942f9
~~~


<a id="compare-b705ad794f5178d686f597d0eef7084f"></a>

### [`00580044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580044.md) → [`00580044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580044.md) FUN_00580044

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
      "definition_site": "00580048",
      "incomplete_value": false,
      "site": "0058004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580048",
      "incomplete_value": false,
      "site": "0058004c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0058004c",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058004c",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580044.md#insn-00580048)
- 新版 `00580048`（命令位置の公開資料なし）

~~~diff
- 00580048 ["COPY", "tmp:0:8", ["const:730:8"]]
- 00580048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00580048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580048 bytes 08c11c91
+ 00580048 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-833cdb721f0258f2d0e4badc615ad3b4"></a>

### [`00580054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580054.md) → [`00580054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580054.md) FUN_00580054

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
      "definition_site": "00580064",
      "incomplete_value": false,
      "site": "0058006c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580064",
      "incomplete_value": false,
      "site": "0058006c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0058006c",
      "DATA",
      [
        "storage",
        "00bf1730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058006c",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580054.md#insn-00580064)
- 新版 `00580064`（命令位置の公開資料なし）

~~~diff
- 00580064 ["COPY", "tmp:0:8", ["const:730:8"]]
- 00580064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00580064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580064 bytes 08c11c91
+ 00580064 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d04ce8d3abaa8d241a6bdea7458e078a"></a>

### [`00580084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580084.md) → [`00580084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580084.md) FUN_00580084

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00580090",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00580090",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058008c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580084.md#insn-0058008c)
- 新版 `0058008c`（命令位置の公開資料なし）

~~~diff
- 0058008c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0058008c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058008c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058008c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0058008c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058008c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058008c bytes 29c12791
+ 0058008c bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ca9a2272ba8f6dbf4ba2a8fe789ec9"></a>

### [`005800a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800a8.md) → [`005800a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/005800a8.md) FUN_005800a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005800ac",
      "incomplete_value": true,
      "site": "005800b0",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800ac",
      "incomplete_value": true,
      "site": "005800b0",
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
            "const:780:8"
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
      "005800b0",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005800b0",
      "DATA",
      [
        "storage",
        "00bf17d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005800ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800a8.md#insn-005800ac)
- 新版 `005800ac`（命令位置の公開資料なし）

~~~diff
- 005800ac ["COPY", "tmp:0:8", ["const:780:8"]]
- 005800ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005800ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005800ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 005800ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005800ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005800ac bytes 08011e91
+ 005800ac bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29f6b0a0f65fed0f5ed95617de34f0a1"></a>

### [`005800b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800b8.md) → [`005800b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/005800b8.md) FUN_005800b8

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
      "definition_site": "005800c8",
      "incomplete_value": false,
      "site": "005800d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800c8",
      "incomplete_value": false,
      "site": "005800d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "005800d0",
      "DATA",
      [
        "storage",
        "00bf1780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005800d0",
      "DATA",
      [
        "storage",
        "00bf17d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005800c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800b8.md#insn-005800c8)
- 新版 `005800c8`（命令位置の公開資料なし）

~~~diff
- 005800c8 ["COPY", "tmp:0:8", ["const:780:8"]]
- 005800c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005800c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005800c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 005800c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005800c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005800c8 bytes 08011e91
+ 005800c8 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbdd794ad90ee81fa2dd88c4bf76c5c4"></a>

### [`005800f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800f0.md) → [`005800f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/005800f0.md) _INIT_46

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580190",
      "incomplete_value": true,
      "site": "005801a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
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
      "definition_site": "00580190",
      "incomplete_value": true,
      "site": "005801a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00580320",
      "incomplete_value": false,
      "site": "00580324",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580320",
      "incomplete_value": false,
      "site": "00580324",
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058012c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00580150",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580170",
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
      "0058012c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00580150",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00580170",
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

- 旧版 [`0058011c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800f0.md#insn-0058011c) · [`00580124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/005800f0.md#insn-00580124)
- 新版 `0058011c`（命令位置の公開資料なし） · `00580124`（命令位置の公開資料なし）

~~~diff
- 0058011c ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0058011c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058011c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058011c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 0058011c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058011c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058011c bytes 73621f91
+ 0058011c bytes 73622091
- 00580124 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00580124 bytes 29e9fff0
+ 00580124 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00580124 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02e2ddd25ef7e45f914b495755d8420f"></a>

### [`00580480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580480.md) → [`00580480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580480.md) _INIT_47

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005806a8",
      "incomplete_value": false,
      "site": "005806b4",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005806a8",
      "incomplete_value": false,
      "site": "005806b4",
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
            "const:7f0:8"
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
      "definition_site": "005806b0",
      "incomplete_value": false,
      "site": "005806b4",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005806b0",
      "incomplete_value": false,
      "site": "005806b4",
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005804bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005804e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580500",
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
      "005804bc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005804e0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00580500",
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

- 旧版 [`005804ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580480.md#insn-005804ac) · [`005804b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580480.md#insn-005804b4)
- 新版 `005804ac`（命令位置の公開資料なし） · `005804b4`（命令位置の公開資料なし）

~~~diff
- 005804ac ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 005804ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005804ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005804ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["COPY", "tmp:0:8", ["const:830:8"]]
+ 005804ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005804ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005804ac bytes 73c21f91
+ 005804ac bytes 73c22091
- 005804b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005804b4 bytes 29e9fff0
+ 005804b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005804b4 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c273c4a3cc8e6ec4b4b0ca368358292"></a>

### [`00580810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580810.md) → [`00580810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580810.md) _INIT_48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005808b0",
      "incomplete_value": true,
      "site": "005808c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "005808b0",
      "incomplete_value": true,
      "site": "005808c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0058084c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00580870",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00580890",
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
      "0058084c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00580870",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00580890",
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

- 旧版 [`0058083c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580810.md#insn-0058083c) · [`00580844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580810.md#insn-00580844)
- 新版 `0058083c`（命令位置の公開資料なし） · `00580844`（命令位置の公開資料なし）

~~~diff
- 0058083c ["COPY", "tmp:0:8", ["const:808:8"]]
- 0058083c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058083c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058083c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 0058083c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058083c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058083c bytes 73222091
+ 0058083c bytes 73222191
- 00580844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00580844 bytes 29e9fff0
+ 00580844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00580844 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066a790e7622e2a3a46c157a782ca1cc"></a>

### [`00580ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md) → [`00580ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580ba0.md) FUN_00580ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00581b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581b20.md) [`00581cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581cd8.md) [`00581e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581e14.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00581b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581b20.md) [`00581cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md) [`00581e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581e14.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581034",
      "incomplete_value": true,
      "site": "00581040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581034",
      "incomplete_value": true,
      "site": "00581040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 82,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005811dc",
      "incomplete_value": true,
      "site": "005811ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:34c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005811dc",
      "incomplete_value": true,
      "site": "005811ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00580bd8",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "00580d40",
      "READ",
      [
        "storage",
        "00299eae",
        null,
        "string"
      ]
    ],
    [
      "00580eac",
      "READ",
      [
        "storage",
        "002a65ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580bd8",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "00580d40",
      "READ",
      [
        "storage",
        "00299eac",
        null,
        "string"
      ]
    ],
    [
      "00580eac",
      "READ",
      [
        "storage",
        "002a6687",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md#insn-00580bcc) · [`00580d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md#insn-00580d38) · [`00580ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md#insn-00580ea4)
- 新版 `00580bcc`（命令位置の公開資料なし） · `00580d38`（命令位置の公開資料なし） · `00580ea4`（命令位置の公開資料なし）

~~~diff
- 00580bcc ["COPY", "tmp:0:8", ["const:5da:8"]]
- 00580bcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00580bcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00580bcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["COPY", "tmp:0:8", ["const:674:8"]]
+ 00580bcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00580bcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00580bcc bytes 4a691791
+ 00580bcc bytes 4ad11991
- 00580d38 ["COPY", "tmp:0:8", ["const:eae:8"]]
- 00580d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00580d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00580d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["COPY", "tmp:0:8", ["const:eac:8"]]
+ 00580d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00580d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00580d38 bytes 29b93a91
+ 00580d38 bytes 29b13a91
- 00580ea4 ["COPY", "tmp:0:8", ["const:5ed:8"]]
- 00580ea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["COPY", "tmp:0:8", ["const:687:8"]]
+ 00580ea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00580ea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00580ea4 bytes 4ab51791
+ 00580ea4 bytes 4a1d1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42211f95922743fecdd639fa6cf3a721"></a>

### [`005818b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/005818b0.md) → [`005818b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/005818b0.md) FUN_005818b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005818e4",
      "incomplete_value": true,
      "site": "005818e8",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005818e4",
      "incomplete_value": true,
      "site": "005818e8",
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
            "const:9f0:8"
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
      "005818e8",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005818e8",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005818e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/005818b0.md#insn-005818e4)
- 新版 `005818e4`（命令位置の公開資料なし）

~~~diff
- 005818e4 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 005818e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005818e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005818e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005818e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005818e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005818e4 bytes 29c12791
+ 005818e4 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b67e40205d21a6037415c31669656b0"></a>

### [`0058190c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/0058190c.md) → [`0058190c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md) FUN_0058190c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581940",
      "incomplete_value": true,
      "site": "00581944",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581940",
      "incomplete_value": true,
      "site": "00581944",
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
            "const:9f0:8"
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
      "00581944",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00581944",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/0058190c.md#insn-00581940)
- 新版 `00581940`（命令位置の公開資料なし）

~~~diff
- 00581940 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00581940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00581940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00581940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00581940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00581940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00581940 bytes 29c12791
+ 00581940 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d3ad965e25a76b70b86672b4dfefd7"></a>

### [`00581aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581aec.md) → [`00581aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581aec.md) FUN_00581aec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00581964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581964.md) [`00581e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581e14.md) [`007726fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/007726fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00581964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581964.md) [`00581e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581e14.md) [`007726fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007726fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00581af8",
      "incomplete_value": false,
      "site": "00581afc",
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
      "definition_site": "00581af8",
      "incomplete_value": false,
      "site": "00581afc",
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
      "00581af8",
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
      "00581af8",
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

- 旧版 [`00581af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581aec.md#insn-00581af8)
- 新版 `00581af8`（命令位置の公開資料なし）

~~~diff
- 00581af8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00581af8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00581af8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00581af8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00581af8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00581af8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00581af8 bytes 000c0c91
+ 00581af8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb246ff148be3a26ccd8d146e504fe00"></a>

### [`0058219c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058219c.md) → [`0058219c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/0058219c.md) FUN_0058219c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00580ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00580/00580ba0.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00581964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581964.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00580ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580ba0.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00581964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581964.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005821d4",
      "incomplete_value": false,
      "site": "005821e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005821d4",
      "incomplete_value": false,
      "site": "005821e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "005821e0",
      "DATA",
      [
        "storage",
        "00bf18a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058221c",
      "DATA",
      [
        "storage",
        "00bf17d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005821e0",
      "DATA",
      [
        "storage",
        "00bf18f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058221c",
      "DATA",
      [
        "storage",
        "00bf1820",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058219c.md#insn-005821d4) · [`00582218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058219c.md#insn-00582218)
- 新版 `005821d4`（命令位置の公開資料なし） · `00582218`（命令位置の公開資料なし）

~~~diff
- 005821d4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 005821d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005821d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005821d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 005821d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005821d4 bytes 08a12291
+ 005821d4 bytes 08e12391
- 00582218 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00582218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00582218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582218 bytes 08411f91
+ 00582218 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeb7e75c79f75e43df79868c9099ddff"></a>

### [`005822bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/005822bc.md) → [`005822bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/005822bc.md) FUN_005822bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581d88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005822f0",
      "incomplete_value": false,
      "site": "005822f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005822f0",
      "incomplete_value": false,
      "site": "005822f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "005822f4",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005822f4",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005822f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/005822bc.md#insn-005822f0)
- 新版 `005822f0`（命令位置の公開資料なし）

~~~diff
- 005822f0 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 005822f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005822f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005822f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005822f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005822f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005822f0 bytes 29c12791
+ 005822f0 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e70f3dc9e08781f2cd1b3c3b34742250"></a>

### [`0058231c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058231c.md) → [`0058231c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/0058231c.md) FUN_0058231c

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
      "definition_site": "00582320",
      "incomplete_value": false,
      "site": "00582324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582320",
      "incomplete_value": false,
      "site": "00582324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "00582324",
      "DATA",
      [
        "storage",
        "00bf18f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582324",
      "DATA",
      [
        "storage",
        "00bf1948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058231c.md#insn-00582320)
- 新版 `00582320`（命令位置の公開資料なし）

~~~diff
- 00582320 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00582320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582320 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00582320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582320 bytes 08e12391
+ 00582320 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d517eb0ed415149d1b9b5ae200d46dc5"></a>

### [`0058232c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058232c.md) → [`0058232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/0058232c.md) FUN_0058232c

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
      "definition_site": "0058233c",
      "incomplete_value": false,
      "site": "00582344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058233c",
      "incomplete_value": false,
      "site": "00582344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "00582344",
      "DATA",
      [
        "storage",
        "00bf18f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582344",
      "DATA",
      [
        "storage",
        "00bf1948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/0058232c.md#insn-0058233c)
- 新版 `0058233c`（命令位置の公開資料なし）

~~~diff
- 0058233c ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0058233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058233c ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0058233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058233c bytes 08e12391
+ 0058233c bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a0c72fce0acebd399864a569365f764"></a>

### [`00582364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582364.md) → [`00582364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582364.md) _INIT_49

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
      "definition_site": "005823a0",
      "incomplete_value": true,
      "site": "005823bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005823a0",
      "incomplete_value": true,
      "site": "005823bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005823c4",
      "incomplete_value": true,
      "site": "005823e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005823c4",
      "incomplete_value": true,
      "site": "005823e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005823e4",
      "incomplete_value": true,
      "site": "00582400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005823e4",
      "incomplete_value": true,
      "site": "00582400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005823a0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005823c4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005823e4",
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
      "005823a0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005823c4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005823e4",
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

- 旧版 [`00582390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582364.md#insn-00582390) · [`00582398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582364.md#insn-00582398)
- 新版 `00582390`（命令位置の公開資料なし） · `00582398`（命令位置の公開資料なし）

~~~diff
- 00582390 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00582390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00582390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00582390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00582390 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00582390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00582390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00582390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00582390 bytes 73822091
+ 00582390 bytes 73822191
- 00582398 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00582398 bytes 29e9ffb0
+ 00582398 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00582398 bytes 29e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bbbdab1df3a1bc21d00250024ec8a8"></a>

### [`00582d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582d54.md) → [`00582d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582d54.md) FUN_00582d54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb330.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb380.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00582d84",
      "incomplete_value": true,
      "site": "00582d90",
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
            "const:aa3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d84",
      "incomplete_value": true,
      "site": "00582d90",
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
            "const:b37:8"
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
      "00582d84",
      "PARAM",
      [
        "storage",
        "002aeb37",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582d84",
      "PARAM",
      [
        "storage",
        "002aeaa3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582d54.md#insn-00582d84)
- 新版 `00582d84`（命令位置の公開資料なし）

~~~diff
- 00582d84 ["COPY", "tmp:0:8", ["const:b37:8"]]
- 00582d84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00582d84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00582d84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00582d84 ["COPY", "tmp:0:8", ["const:aa3:8"]]
+ 00582d84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00582d84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00582d84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00582d84 bytes 42dc2c91
+ 00582d84 bytes 428c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b274ada1eef6a4a3fd41634dbe6caf3e"></a>

### [`00582e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582e3c.md) → [`00582e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e3c.md) FUN_00582e3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582e58",
      "incomplete_value": false,
      "site": "00582e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582e58",
      "incomplete_value": false,
      "site": "00582e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "definition_site": "00582e70",
      "incomplete_value": false,
      "site": "00582e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582e70",
      "incomplete_value": false,
      "site": "00582e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00582e60",
      "DATA",
      [
        "storage",
        "00bf1a70",
        null,
        "undefined *"
      ]
    ],
    [
      "00582e70",
      "DATA",
      [
        "storage",
        "00bf19c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00582e60",
      "DATA",
      [
        "storage",
        "00bf1ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582e70",
      "DATA",
      [
        "storage",
        "00bf1a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582e3c.md#insn-00582e58) · [`00582e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582e3c.md#insn-00582e64)
- 新版 `00582e58`（命令位置の公開資料なし） · `00582e64`（命令位置の公開資料なし）

~~~diff
- 00582e58 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00582e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582e58 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00582e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582e58 bytes 08c12991
+ 00582e58 bytes 08012b91
- 00582e64 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 00582e64 bytes 683300f0
+ 00582e64 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 00582e64 bytes 683300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e31ad9b86ad846581bdc0a21096e69"></a>

### [`00582e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582e84.md) → [`00582e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e84.md) FUN_00582e84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00582ea0",
      "incomplete_value": true,
      "site": "00582ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00582ea0",
      "incomplete_value": true,
      "site": "00582ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00582e98",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "00582ea4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582e98",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "00582ea4",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582e84.md#insn-00582e98)
- 新版 `00582e98`（命令位置の公開資料なし）

~~~diff
- 00582e98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 00582e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00582e98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 00582e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00582e98 bytes 087142f9
+ 00582e98 bytes 089942f9
~~~


<a id="compare-7f954545d3b4a31d29b8dc91f4e01174"></a>

### [`00582ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582ed4.md) → [`00582ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582ed4.md) FUN_00582ed4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00582f38",
      "incomplete_value": false,
      "site": "00582f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582f38",
      "incomplete_value": false,
      "site": "00582f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00582f3c",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582f3c",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582ed4.md#insn-00582f38)
- 新版 `00582f38`（命令位置の公開資料なし）

~~~diff
- 00582f38 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00582f38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582f38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582f38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582f38 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00582f38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582f38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582f38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582f38 bytes 29c12791
+ 00582f38 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d5dc52bc17c2a687ddbc631589c883"></a>

### [`00582f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582f68.md) → [`00582f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582f68.md) FUN_00582f68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00582fcc",
      "incomplete_value": false,
      "site": "00582fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582fcc",
      "incomplete_value": false,
      "site": "00582fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00582fd0",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582fd0",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582f68.md#insn-00582fcc)
- 新版 `00582fcc`（命令位置の公開資料なし）

~~~diff
- 00582fcc ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00582fcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582fcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582fcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582fcc ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00582fcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582fcc bytes 29c12791
+ 00582fcc bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c499f83991441c4a14552870e3862a76"></a>

### [`005831d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/005831d8.md) → [`005831d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005831d8.md) FUN_005831d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00582ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582ff4.md) [`00583240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583240.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00582ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582ff4.md) [`00583240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005831e4",
      "incomplete_value": false,
      "site": "005831e8",
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
      "definition_site": "005831e4",
      "incomplete_value": false,
      "site": "005831e8",
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
      "005831e4",
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
      "005831e4",
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

- 旧版 [`005831e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/005831d8.md#insn-005831e4)
- 新版 `005831e4`（命令位置の公開資料なし）

~~~diff
- 005831e4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005831e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005831e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005831e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005831e4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005831e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005831e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005831e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005831e4 bytes 000c0c91
+ 005831e4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c66f3d146baaa461e133adf7e0ce070"></a>

### [`0058349c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058349c.md) → [`0058349c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/0058349c.md) FUN_0058349c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005826f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/005826f4.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00582ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`005826f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/005826f4.md) · 呼出先 3件 [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00582ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005834dc",
      "incomplete_value": false,
      "site": "005834e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005834dc",
      "incomplete_value": false,
      "site": "005834e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "005834e8",
      "DATA",
      [
        "storage",
        "00bf1a20",
        null,
        "undefined *"
      ]
    ],
    [
      "0058350c",
      "DATA",
      [
        "storage",
        "00bf1948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005834e8",
      "DATA",
      [
        "storage",
        "00bf1a70",
        null,
        "undefined *"
      ]
    ],
    [
      "0058350c",
      "DATA",
      [
        "storage",
        "00bf1998",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005834dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058349c.md#insn-005834dc) · [`00583500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058349c.md#insn-00583500)
- 新版 `005834dc`（命令位置の公開資料なし） · `00583500`（命令位置の公開資料なし）

~~~diff
- 005834dc ["COPY", "tmp:0:8", ["const:a20:8"]]
- 005834dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005834dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005834dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005834dc ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 005834dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005834dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005834dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005834dc bytes 08812891
+ 005834dc bytes 08c12991
- 00583500 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00583500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583500 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00583500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583500 bytes 08212591
+ 00583500 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7626cd8d90713e4c442cbefbfefe092f"></a>

### [`0058358c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058358c.md) → [`0058358c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/0058358c.md) FUN_0058358c

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
      "definition_site": "0058359c",
      "incomplete_value": false,
      "site": "005835a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058359c",
      "incomplete_value": false,
      "site": "005835a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
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
      "005835a4",
      "DATA",
      [
        "storage",
        "00bf1a20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005835a4",
      "DATA",
      [
        "storage",
        "00bf1a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058358c.md#insn-0058359c)
- 新版 `0058359c`（命令位置の公開資料なし）

~~~diff
- 0058359c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 0058359c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058359c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058359c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058359c ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0058359c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058359c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058359c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058359c bytes 08812891
+ 0058359c bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7328fe2aa1d27ba81c90396055ed0f2"></a>

### [`005835bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/005835bc.md) → [`005835bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005835bc.md) FUN_005835bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00583620",
      "incomplete_value": false,
      "site": "00583624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583620",
      "incomplete_value": false,
      "site": "00583624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "00583624",
      "DATA",
      [
        "storage",
        "00bf09f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00583624",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/005835bc.md#insn-00583620)
- 新版 `00583620`（命令位置の公開資料なし）

~~~diff
- 00583620 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00583620 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00583620 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00583620 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00583620 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00583620 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00583620 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00583620 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00583620 bytes 29c12791
+ 00583620 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ccd5733545b59397a05b33aa03216c"></a>

### [`00583654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583654.md) → [`00583654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583654.md) FUN_00583654

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
      "definition_site": "00583658",
      "incomplete_value": false,
      "site": "0058365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583658",
      "incomplete_value": false,
      "site": "0058365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "0058365c",
      "DATA",
      [
        "storage",
        "00bf1a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058365c",
      "DATA",
      [
        "storage",
        "00bf1ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583654.md#insn-00583658)
- 新版 `00583658`（命令位置の公開資料なし）

~~~diff
- 00583658 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00583658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583658 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00583658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583658 bytes 08c12991
+ 00583658 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1db47e1dd6b587187c584ca7e9c721"></a>

### [`00583664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583664.md) → [`00583664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583664.md) FUN_00583664

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
      "definition_site": "00583674",
      "incomplete_value": false,
      "site": "0058367c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583674",
      "incomplete_value": false,
      "site": "0058367c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "0058367c",
      "DATA",
      [
        "storage",
        "00bf1a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058367c",
      "DATA",
      [
        "storage",
        "00bf1ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583664.md#insn-00583674)
- 新版 `00583674`（命令位置の公開資料なし）

~~~diff
- 00583674 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00583674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583674 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00583674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583674 bytes 08c12991
+ 00583674 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6dd15d31ee1f4652fea61343725f2b4"></a>

### [`0058369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058369c.md) → [`0058369c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/0058369c.md) _INIT_50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "005836d8",
      "incomplete_value": true,
      "site": "005836f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005836d8",
      "incomplete_value": true,
      "site": "005836f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0058373c",
      "incomplete_value": true,
      "site": "00583754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0058373c",
      "incomplete_value": true,
      "site": "00583754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583758",
      "incomplete_value": true,
      "site": "00583774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583758",
      "incomplete_value": true,
      "site": "00583774",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005836d8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005836fc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0058371c",
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
      "005836d8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005836fc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0058371c",
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

- 旧版 [`005836c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058369c.md#insn-005836c8) · [`005836d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/0058369c.md#insn-005836d0)
- 新版 `005836c8`（命令位置の公開資料なし） · `005836d0`（命令位置の公開資料なし）

~~~diff
- 005836c8 ["COPY", "tmp:0:8", ["const:838:8"]]
- 005836c8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005836c8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005836c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005836c8 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 005836c8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005836c8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005836c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005836c8 bytes 73e22091
+ 005836c8 bytes 73e22191
- 005836d0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005836d0 bytes 29e9ff90
+ 005836d0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005836d0 bytes 29e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf83baff5f245bbec687bc55e987d12"></a>

### [`00583a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583a2c.md) → [`00583a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583a2c.md) FUN_00583a2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578fc4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583a78",
      "incomplete_value": true,
      "site": "00583a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583a78",
      "incomplete_value": true,
      "site": "00583a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00583c30",
      "incomplete_value": false,
      "site": "00583c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583c30",
      "incomplete_value": false,
      "site": "00583c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00583c54",
      "incomplete_value": false,
      "site": "00583c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583c54",
      "incomplete_value": false,
      "site": "00583c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "00583a5c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "00583c3c",
      "DATA",
      [
        "storage",
        "00bf1b98",
        null,
        "undefined *"
      ]
    ],
    [
      "00583c5c",
      "DATA",
      [
        "storage",
        "00bf1ac0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00583a5c",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "00583c3c",
      "DATA",
      [
        "storage",
        "00bf1be8",
        null,
        "undefined *"
      ]
    ],
    [
      "00583c5c",
      "DATA",
      [
        "storage",
        "00bf1b10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583a2c.md#insn-00583a50) · [`00583c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583a2c.md#insn-00583c30) · [`00583c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583a2c.md#insn-00583c54)
- 新版 `00583a50`（命令位置の公開資料なし） · `00583c30`（命令位置の公開資料なし） · `00583c54`（命令位置の公開資料なし）

~~~diff
- 00583a50 ["COPY", "tmp:0:8", ["const:5da:8"]]
- 00583a50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00583a50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00583a50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00583a50 ["COPY", "tmp:0:8", ["const:674:8"]]
+ 00583a50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00583a50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00583a50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00583a50 bytes 4a691791
+ 00583a50 bytes 4ad11991
- 00583c30 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00583c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583c30 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00583c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583c30 bytes 08612e91
+ 00583c30 bytes 08a12f91
- 00583c54 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00583c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583c54 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 00583c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583c54 bytes 08012b91
+ 00583c54 bytes 08412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8462df9ef8fdfd59e506f18e3be54c80"></a>

### [`00583d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d20.md) → [`00583d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md) FUN_00583d20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096fb34.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583d44",
      "incomplete_value": true,
      "site": "00583d48",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583d44",
      "incomplete_value": true,
      "site": "00583d48",
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
            "const:ae0:8"
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
      "00583d48",
      "DATA",
      [
        "storage",
        "00bf1ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583d48",
      "DATA",
      [
        "storage",
        "00bf1b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d20.md#insn-00583d44)
- 新版 `00583d44`（命令位置の公開資料なし）

~~~diff
- 00583d44 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00583d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583d44 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00583d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583d44 bytes 08812b91
+ 00583d44 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ca3e4d2429e5f3ce8a6d88ea6aadbc9"></a>

### [`00583d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d64.md) → [`00583d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d64.md) FUN_00583d64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb330.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb380.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00583d94",
      "incomplete_value": false,
      "site": "00583da0",
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
            "const:aa3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583d94",
      "incomplete_value": false,
      "site": "00583da0",
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
            "const:b37:8"
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
      "00583d94",
      "PARAM",
      [
        "storage",
        "002aeb37",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00583d94",
      "PARAM",
      [
        "storage",
        "002aeaa3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d64.md#insn-00583d94)
- 新版 `00583d94`（命令位置の公開資料なし）

~~~diff
- 00583d94 ["COPY", "tmp:0:8", ["const:b37:8"]]
- 00583d94 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00583d94 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00583d94 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00583d94 ["COPY", "tmp:0:8", ["const:aa3:8"]]
+ 00583d94 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00583d94 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00583d94 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00583d94 bytes 42dc2c91
+ 00583d94 bytes 428c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3636a817cee29146ad030e2d3b079689"></a>

### [`00584008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/00584008.md) → [`00584008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584008.md) FUN_00584008

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00584024",
      "incomplete_value": false,
      "site": "0058402c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584024",
      "incomplete_value": false,
      "site": "0058402c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "0058403c",
      "incomplete_value": false,
      "site": "0058403c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058403c",
      "incomplete_value": false,
      "site": "0058403c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf1000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "0058402c",
      "DATA",
      [
        "storage",
        "00bf1be8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058403c",
      "DATA",
      [
        "storage",
        "00bf1b38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058402c",
      "DATA",
      [
        "storage",
        "00bf1c38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058403c",
      "DATA",
      [
        "storage",
        "00bf1b88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00584024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/00584008.md#insn-00584024) · [`00584030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/00584008.md#insn-00584030)
- 新版 `00584024`（命令位置の公開資料なし） · `00584030`（命令位置の公開資料なし）

~~~diff
- 00584024 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00584024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00584024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00584024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00584024 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00584024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00584024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00584024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00584024 bytes 08a12f91
+ 00584024 bytes 08e13091
- 00584030 ["COPY", "register:4040:8", ["const:bf1000:8"]]
- 00584030 bytes 683300b0
+ 00584030 ["COPY", "register:4040:8", ["const:bf1000:8"]]
+ 00584030 bytes 683300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

