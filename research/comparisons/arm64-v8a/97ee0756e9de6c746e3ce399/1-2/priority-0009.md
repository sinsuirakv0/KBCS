# v15.7.3 → v15.7.4 · 最優先の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-6a7bfe64f5c7dde06f6e088043bd09d3"></a>

### [`004a8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8a10.md) → [`004a8a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8a10.md) FUN_004a8a10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e3f4.md) [`0050dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dd3c.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md)
- 新版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dd3c.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8a3c",
      "incomplete_value": true,
      "site": "004a8a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8a3c",
      "incomplete_value": true,
      "site": "004a8a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8aa4",
      "incomplete_value": true,
      "site": "004a8aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8aa4",
      "incomplete_value": true,
      "site": "004a8aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8b38",
      "incomplete_value": true,
      "site": "004a8b40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8b38",
      "incomplete_value": true,
      "site": "004a8b40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8a30",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8a44",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8a90",
      "READ",
      [
        "storage",
        "00c1b108",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8a30",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004a8a44",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8a90",
      "READ",
      [
        "storage",
        "00c1b158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8a10.md#insn-004a8a30) · [`004a8a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8a10.md#insn-004a8a90) · [`004a8b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8a10.md#insn-004a8b30)
- 新版 `004a8a30`（命令位置の公開資料なし） · `004a8a90`（命令位置の公開資料なし） · `004a8b30`（命令位置の公開資料なし）

~~~diff
- 004a8a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004a8a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004a8a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8a30 bytes 087d40f9
+ 004a8a30 bytes 08a540f9
- 004a8a90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
- 004a8a90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8a90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 004a8a90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8a90 bytes 088540f9
+ 004a8a90 bytes 08ad40f9
- 004a8b30 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a8b30 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a8b30 bytes 823b00d0
+ 004a8b30 bytes 823b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3ed2591aa80ff252bafcbe05c12ec5f"></a>

### [`004a8bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8bc4.md) → [`004a8bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md) FUN_004a8bc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e3f4.md) [`0050dee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dee4.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md)
- 新版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050dee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dee4.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8bf0",
      "incomplete_value": true,
      "site": "004a8bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8bf0",
      "incomplete_value": true,
      "site": "004a8bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8c58",
      "incomplete_value": true,
      "site": "004a8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8c58",
      "incomplete_value": true,
      "site": "004a8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8cec",
      "incomplete_value": true,
      "site": "004a8cf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8cec",
      "incomplete_value": true,
      "site": "004a8cf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8be4",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bf8",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8c44",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8be4",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bf8",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8c44",
      "READ",
      [
        "storage",
        "00c1b160",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8bc4.md#insn-004a8be4) · [`004a8c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8bc4.md#insn-004a8c44) · [`004a8ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8bc4.md#insn-004a8ce4)
- 新版 `004a8be4`（命令位置の公開資料なし） · `004a8c44`（命令位置の公開資料なし） · `004a8ce4`（命令位置の公開資料なし）

~~~diff
- 004a8be4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004a8be4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8be4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004a8be4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8be4 bytes 087d40f9
+ 004a8be4 bytes 08a540f9
- 004a8c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
- 004a8c44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:160:8"]]
+ 004a8c44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8c44 bytes 088940f9
+ 004a8c44 bytes 08b140f9
- 004a8ce4 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a8ce4 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a8ce4 bytes 823b00d0
+ 004a8ce4 bytes 823b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c43aaad390b20464b96782b9e19b7ee"></a>

### [`004a8d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8d78.md) → [`004a8d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md) FUN_004a8d78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e3f4.md) [`0050d508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d508.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb90.md)
- 新版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d508.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8da4",
      "incomplete_value": true,
      "site": "004a8dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8da4",
      "incomplete_value": true,
      "site": "004a8dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8e10",
      "incomplete_value": true,
      "site": "004a8e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8e10",
      "incomplete_value": true,
      "site": "004a8e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8ec8",
      "incomplete_value": true,
      "site": "004a8ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8ec8",
      "incomplete_value": true,
      "site": "004a8ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8d98",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8dac",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8dfc",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8d98",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004a8dac",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004a8dfc",
      "READ",
      [
        "storage",
        "00c1b168",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8d78.md#insn-004a8d98) · [`004a8dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8d78.md#insn-004a8dfc) · [`004a8ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a8d78.md#insn-004a8ec0)
- 新版 `004a8d98`（命令位置の公開資料なし） · `004a8dfc`（命令位置の公開資料なし） · `004a8ec0`（命令位置の公開資料なし）

~~~diff
- 004a8d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004a8d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004a8d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8d98 bytes 087d40f9
+ 004a8d98 bytes 08a540f9
- 004a8dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
- 004a8dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:168:8"]]
+ 004a8dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8dfc bytes 088d40f9
+ 004a8dfc bytes 08b540f9
- 004a8ec0 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004a8ec0 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004a8ec0 bytes 823b00d0
+ 004a8ec0 bytes 823b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bcfac52b9e66e91fbcd713a64478bee"></a>

### [`004a933c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a933c.md) → [`004a933c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a933c.md) _ZN5Botan16ieee1363_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a9450",
      "incomplete_value": false,
      "site": "004a9458",
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
            "const:48c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9450",
      "incomplete_value": false,
      "site": "004a9458",
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
            "const:401:8"
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
      "definition_site": "004a9494",
      "incomplete_value": false,
      "site": "004a949c",
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
            "const:373:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9494",
      "incomplete_value": false,
      "site": "004a949c",
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
            "const:375:8"
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
      "004a9450",
      "PARAM",
      [
        "storage",
        "0029c401",
        null,
        "string"
      ]
    ],
    [
      "004a9494",
      "PARAM",
      [
        "storage",
        "0029b375",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a9450",
      "PARAM",
      [
        "storage",
        "0029c48c",
        null,
        "string"
      ]
    ],
    [
      "004a9494",
      "PARAM",
      [
        "storage",
        "0029b373",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a933c.md#insn-004a9450) · [`004a9494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a933c.md#insn-004a9494)
- 新版 `004a9450`（命令位置の公開資料なし） · `004a9494`（命令位置の公開資料なし）

~~~diff
- 004a9450 ["COPY", "tmp:0:8", ["const:401:8"]]
- 004a9450 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a9450 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a9450 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a9450 ["COPY", "tmp:0:8", ["const:48c:8"]]
+ 004a9450 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9450 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9450 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a9450 bytes 21041091
+ 004a9450 bytes 21301291
- 004a9494 ["COPY", "tmp:0:8", ["const:375:8"]]
- 004a9494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a9494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a9494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a9494 ["COPY", "tmp:0:8", ["const:373:8"]]
+ 004a9494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a9494 bytes 21d40d91
+ 004a9494 bytes 21cc0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a4997ace545d139d4ea0247228c1c3"></a>

### [`004a94c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a94c8.md) → [`004a94c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a94c8.md) _ZN5Botan10hex_decodeEPhPKcmRmb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc2a0.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2f0.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a9590",
      "incomplete_value": false,
      "site": "004a95a4",
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
            "const:457:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9590",
      "incomplete_value": false,
      "site": "004a95a4",
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
            "const:3cc:8"
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
      "definition_site": "004a9600",
      "incomplete_value": false,
      "site": "004a9608",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9600",
      "incomplete_value": false,
      "site": "004a9608",
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
            "const:2a8:8"
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
      "definition_site": "004a9630",
      "incomplete_value": false,
      "site": "004a9638",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9630",
      "incomplete_value": false,
      "site": "004a9638",
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
            "const:48f:8"
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
      "004a9590",
      "PARAM",
      [
        "storage",
        "0029e3cc",
        null,
        null
      ]
    ],
    [
      "004a9600",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "004a9630",
      "PARAM",
      [
        "storage",
        "0029f48f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a9590",
      "PARAM",
      [
        "storage",
        "0029e457",
        null,
        null
      ]
    ],
    [
      "004a9600",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "004a9630",
      "PARAM",
      [
        "storage",
        "0029f51a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a94c8.md#insn-004a9590) · [`004a9600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a94c8.md#insn-004a9600) · [`004a9630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a94c8.md#insn-004a9630)
- 新版 `004a9590`（命令位置の公開資料なし） · `004a9600`（命令位置の公開資料なし） · `004a9630`（命令位置の公開資料なし）

~~~diff
- 004a9590 ["COPY", "tmp:0:8", ["const:3cc:8"]]
- 004a9590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a9590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a9590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a9590 ["COPY", "tmp:0:8", ["const:457:8"]]
+ 004a9590 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9590 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9590 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a9590 bytes 21300f91
+ 004a9590 bytes 215c1191
- 004a9600 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 004a9600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a9600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a9600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a9600 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 004a9600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a9600 bytes 21a00a91
+ 004a9600 bytes 21cc0c91
- 004a9630 ["COPY", "tmp:0:8", ["const:48f:8"]]
- 004a9630 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a9630 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a9630 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a9630 ["COPY", "tmp:0:8", ["const:51a:8"]]
+ 004a9630 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9630 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a9630 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a9630 bytes 213c1291
+ 004a9630 bytes 21681491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13085a6278afbb6a1e131d0372afd5f8"></a>

### [`004a9770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9770.md) → [`004a9770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9770.md) _ZN5Botan10hex_decodeEPhPKcmb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc40.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a97e8",
      "incomplete_value": false,
      "site": "004a97f0",
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
            "const:615:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a97e8",
      "incomplete_value": false,
      "site": "004a97f0",
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
            "const:58a:8"
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
      "definition_site": "004a9824",
      "incomplete_value": true,
      "site": "004a9830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a9824",
      "incomplete_value": true,
      "site": "004a9830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a97e8",
      "PARAM",
      [
        "storage",
        "002a558a",
        null,
        "string"
      ]
    ],
    [
      "004a9824",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004a9824",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a97e8",
      "PARAM",
      [
        "storage",
        "002a5615",
        null,
        "string"
      ]
    ],
    [
      "004a9824",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004a9824",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a97e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9770.md#insn-004a97e8) · [`004a9824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9770.md#insn-004a9824)
- 新版 `004a97e8`（命令位置の公開資料なし） · `004a9824`（命令位置の公開資料なし）

~~~diff
- 004a97e8 ["COPY", "tmp:0:8", ["const:58a:8"]]
- 004a97e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a97e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a97e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a97e8 ["COPY", "tmp:0:8", ["const:615:8"]]
+ 004a97e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a97e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a97e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a97e8 bytes 21281691
+ 004a97e8 bytes 21541891
- 004a9824 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004a9824 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a9824 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004a9824 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a9824 bytes 217847f9
+ 004a9824 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7ae418208ba7133b5c6cf4d5459c2fa"></a>

### [`004a9ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9ad4.md) → [`004a9ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9ad4.md) _ZN5Botan4HMAC8add_dataEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md)

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
      "definition_site": "004a9b88",
      "incomplete_value": true,
      "site": "004a9b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9b88",
      "incomplete_value": true,
      "site": "004a9b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
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
      "004a9b88",
      "READ",
      [
        "storage",
        "00c1aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004a9b88",
      "PARAM",
      [
        "storage",
        "00becb48",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a9b88",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004a9b88",
      "PARAM",
      [
        "storage",
        "00becb98",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9ad4.md#insn-004a9b88)
- 新版 `004a9b88`（命令位置の公開資料なし）

~~~diff
- 004a9b88 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed0:8"]]
- 004a9b88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a9b88 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f20:8"]]
+ 004a9b88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a9b88 bytes 216847f9
+ 004a9b88 bytes 219047f9
~~~


<a id="compare-c7dc741fda782ea99402a2c35a8b0c79"></a>

### [`004a9be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9be8.md) → [`004a9be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9be8.md) _ZN5Botan4HMAC12final_resultEPh

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a9d08",
      "incomplete_value": true,
      "site": "004a9d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9d08",
      "incomplete_value": true,
      "site": "004a9d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
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
      "004a9d08",
      "READ",
      [
        "storage",
        "00c1aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004a9d08",
      "PARAM",
      [
        "storage",
        "00becb48",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a9d08",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004a9d08",
      "PARAM",
      [
        "storage",
        "00becb98",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a9/004a9be8.md#insn-004a9d08)
- 新版 `004a9d08`（命令位置の公開資料なし）

~~~diff
- 004a9d08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed0:8"]]
- 004a9d08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a9d08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f20:8"]]
+ 004a9d08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004a9d08 bytes 216847f9
+ 004a9d08 bytes 219047f9
~~~


<a id="compare-21c193604a08a85ef6e2a0add4241c66"></a>

### [`004aa2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa2ec.md) → [`004aa2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md) _ZNK5Botan4HMAC4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc2f0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bdc340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aa350",
      "incomplete_value": false,
      "site": "004aa358",
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
            "const:284:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa350",
      "incomplete_value": false,
      "site": "004aa358",
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
            "const:286:8"
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
      "004aa350",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004aa350",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa2ec.md#insn-004aa350)
- 新版 `004aa350`（命令位置の公開資料なし）

~~~diff
- 004aa350 ["COPY", "tmp:0:8", ["const:286:8"]]
- 004aa350 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004aa350 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004aa350 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004aa350 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004aa350 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004aa350 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004aa350 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004aa350 bytes 21180a91
+ 004aa350 bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2d1512e117ef4c5b5ddff485062129"></a>

### [`004aa464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa464.md) → [`004aa464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa464.md) _ZN5Botan4HMACC1EPNS_12HashFunctionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc300.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00bdc350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc350.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:98:8"
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
      "definition_site": "004aa51c",
      "incomplete_value": false,
      "site": "004aa528",
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
            "const:571:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa51c",
      "incomplete_value": false,
      "site": "004aa528",
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
            "const:4d7:8"
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
      "004aa488",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004aa4a4",
      "DATA",
      [
        "storage",
        "00be9c00",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004aa4a4",
      "DATA",
      [
        "storage",
        "00be9c88",
        null,
        "undefined1[200]"
      ]
    ]
  ],
  "added": [
    [
      "004aa488",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "004aa4a4",
      "DATA",
      [
        "storage",
        "00be9c50",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004aa4a4",
      "DATA",
      [
        "storage",
        "00be9cd8",
        null,
        "undefined1[200]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa464.md#insn-004aa488) · [`004aa51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa464.md#insn-004aa51c) · [`004aa570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa464.md#insn-004aa570)
- 新版 `004aa488`（命令位置の公開資料なし） · `004aa51c`（命令位置の公開資料なし） · `004aa570`（命令位置の公開資料なし）

~~~diff
- 004aa488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
- 004aa488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aa488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
+ 004aa488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004aa488 bytes 089140f9
+ 004aa488 bytes 08b940f9
- 004aa51c ["COPY", "tmp:0:8", ["const:4d7:8"]]
- 004aa51c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004aa51c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004aa51c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004aa51c ["COPY", "tmp:0:8", ["const:571:8"]]
+ 004aa51c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004aa51c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004aa51c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004aa51c bytes 425c1391
+ 004aa51c bytes 42c41591
- 004aa570 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004aa570 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aa570 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004aa570 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004aa570 bytes 217847f9
+ 004aa570 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242dcf61c4756ecfac75d39404abd248"></a>

### [`004aa79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa79c.md) → [`004aa79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa79c.md) _ZN5Botan3KDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aa814",
      "incomplete_value": false,
      "site": "004aa81c",
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
            "const:7c4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa814",
      "incomplete_value": false,
      "site": "004aa81c",
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
            "const:851:8"
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
      "definition_site": "004aa854",
      "incomplete_value": true,
      "site": "004aa860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa854",
      "incomplete_value": true,
      "site": "004aa860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004aa814",
      "PARAM",
      [
        "storage",
        "00292851",
        null,
        null
      ]
    ],
    [
      "004aa854",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004aa854",
      "PARAM",
      [
        "storage",
        "00be93e8",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004aa814",
      "PARAM",
      [
        "storage",
        "002927c4",
        null,
        null
      ]
    ],
    [
      "004aa854",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004aa854",
      "PARAM",
      [
        "storage",
        "00be9438",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa79c.md#insn-004aa814) · [`004aa848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa79c.md#insn-004aa848) · [`004aa854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa79c.md#insn-004aa854)
- 新版 `004aa814`（命令位置の公開資料なし） · `004aa848`（命令位置の公開資料なし） · `004aa854`（命令位置の公開資料なし）

~~~diff
- 004aa814 ["COPY", "tmp:0:8", ["const:851:8"]]
- 004aa814 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004aa814 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004aa814 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004aa814 ["COPY", "tmp:0:8", ["const:7c4:8"]]
+ 004aa814 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004aa814 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004aa814 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004aa814 bytes 21442191
+ 004aa814 bytes 21101f91
- 004aa848 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004aa848 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004aa848 bytes 813b0090
+ 004aa848 bytes 813b00b0
- 004aa854 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004aa854 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aa854 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004aa854 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004aa854 bytes 21f447f9
+ 004aa854 bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5858a6e9d890a3237eb01095394664d9"></a>

### [`004aab0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aab0c.md) → [`004aab0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aab0c.md) _ZN5Botan7get_kdfERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc320.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc370.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.21% / 新版 99.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aacf4",
      "incomplete_value": true,
      "site": "004aacfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004aacf4",
      "incomplete_value": true,
      "site": "004aacfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004aacf4",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004aacf4",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004aacf4",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004aacf4",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aacf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aab0c.md#insn-004aacf4)
- 新版 `004aacf4`（命令位置の公開資料なし）

~~~diff
- 004aacf4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004aacf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aacf4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004aacf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004aacf4 bytes 214840f9
+ 004aacf4 bytes 217040f9
~~~


<a id="compare-373c15d35cba5b05b1bc4a673459778b"></a>

### [`004aad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aad54.md) → [`004aad54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md) _ZN5Botan7KeyPair28encryption_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004aaec0",
      "incomplete_value": true,
      "site": "004aaec0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aaec0",
      "incomplete_value": true,
      "site": "004aaec0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004aafa8",
      "incomplete_value": true,
      "site": "004aafa8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aafa8",
      "incomplete_value": true,
      "site": "004aafa8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004aaeb0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004aaf98",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aaeb0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004aaf98",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aaeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aad54.md#insn-004aaeb0) · [`004aaf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aad54.md#insn-004aaf98)
- 新版 `004aaeb0`（命令位置の公開資料なし） · `004aaf98`（命令位置の公開資料なし）

~~~diff
- 004aaeb0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004aaeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aaeb0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004aaeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004aaeb0 bytes 499743f9
+ 004aaeb0 bytes 49bf43f9
- 004aaf98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004aaf98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aaf98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004aaf98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004aaf98 bytes 499743f9
+ 004aaf98 bytes 49bf43f9
~~~


<a id="compare-d4074e580377183d95966030a58b60d6"></a>

### [`004ababc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md) → [`004ababc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md) _ZNK5Botan3MD510copy_stateEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "004abaf0",
      "incomplete_value": true,
      "site": "004abaf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004abaf0",
      "incomplete_value": true,
      "site": "004abaf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004abb1c",
      "incomplete_value": true,
      "site": "004abb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004abb1c",
      "incomplete_value": true,
      "site": "004abb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004abae4",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004abaf4",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004abb0c",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004abae4",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004abaf4",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004abb0c",
      "READ",
      [
        "storage",
        "00c1b168",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004abae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md#insn-004abae4) · [`004abb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md#insn-004abb0c)
- 新版 `004abae4`（命令位置の公開資料なし） · `004abb0c`（命令位置の公開資料なし）

~~~diff
- 004abae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004abae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004abae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004abae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004abae4 bytes 087d40f9
+ 004abae4 bytes 08a540f9
- 004abb0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
- 004abb0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004abb0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:168:8"]]
+ 004abb0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004abb0c bytes 088d40f9
+ 004abb0c bytes 08b540f9
~~~


<a id="compare-30e6817dd7d17126a308742bc763518d"></a>

### [`004ac6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac6b0.md) → [`004ac6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac6b0.md) _ZN5Botan16MDx_HashFunctionC2Embbm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)

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
      "definition_site": "004ac6dc",
      "incomplete_value": true,
      "site": "004ac6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ac6dc",
      "incomplete_value": true,
      "site": "004ac6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004ac6cc",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac6dc",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "004ac6cc",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004ac6dc",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac6b0.md#insn-004ac6cc)
- 新版 `004ac6cc`（命令位置の公開資料なし）

~~~diff
- 004ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 004ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ac6cc bytes 087d40f9
+ 004ac6cc bytes 08a540f9
~~~


<a id="compare-a45b65943b5f01ccdf482fc6f2f825a5"></a>

### [`004ac930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac930.md) → [`004ac930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac930.md) _ZN5Botan16MDx_HashFunction11write_countEPh

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ac9e0",
      "incomplete_value": false,
      "site": "004ac9e8",
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
            "const:9c4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ac9e0",
      "incomplete_value": false,
      "site": "004ac9e8",
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
            "const:a51:8"
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
      "definition_site": "004aca18",
      "incomplete_value": true,
      "site": "004aca24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004aca18",
      "incomplete_value": true,
      "site": "004aca24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aca3c",
      "incomplete_value": false,
      "site": "004aca44",
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
            "const:4bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aca3c",
      "incomplete_value": false,
      "site": "004aca44",
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
            "const:432:8"
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
      "004ac9e0",
      "PARAM",
      [
        "storage",
        "00291a51",
        null,
        "string"
      ]
    ],
    [
      "004aca18",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004aca18",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ac9e0",
      "PARAM",
      [
        "storage",
        "002919c4",
        null,
        "string"
      ]
    ],
    [
      "004aca18",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004aca18",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac930.md#insn-004ac9e0) · [`004aca18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac930.md#insn-004aca18) · [`004aca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac930.md#insn-004aca3c)
- 新版 `004ac9e0`（命令位置の公開資料なし） · `004aca18`（命令位置の公開資料なし） · `004aca3c`（命令位置の公開資料なし）

~~~diff
- 004ac9e0 ["COPY", "tmp:0:8", ["const:a51:8"]]
- 004ac9e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ac9e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ac9e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ac9e0 ["COPY", "tmp:0:8", ["const:9c4:8"]]
+ 004ac9e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ac9e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ac9e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ac9e0 bytes 21442991
+ 004ac9e0 bytes 21102791
- 004aca18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004aca18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aca18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004aca18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004aca18 bytes 217847f9
+ 004aca18 bytes 21a047f9
- 004aca3c ["COPY", "tmp:0:8", ["const:432:8"]]
- 004aca3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004aca3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004aca3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004aca3c ["COPY", "tmp:0:8", ["const:4bd:8"]]
+ 004aca3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004aca3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004aca3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004aca3c bytes 21c81091
+ 004aca3c bytes 21f41291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0390b02749e07f44c5c36af22dd7c65"></a>

### [`004acad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004acad0.md) → [`004acad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acad0.md) _ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf60.md) · 呼出先 4件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00bdbfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfb0.md) · 呼出先 4件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004acca4",
      "incomplete_value": true,
      "site": "004acca4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004acca4",
      "incomplete_value": true,
      "site": "004acca4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004acc94",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004acc94",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004acc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004acad0.md#insn-004acc94)
- 新版 `004acc94`（命令位置の公開資料なし）

~~~diff
- 004acc94 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 004acc94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004acc94 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 004acc94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004acc94 bytes 699743f9
+ 004acc94 bytes 69bf43f9
~~~


<a id="compare-e518e37c48094a9bfcd63c4bbe323e7c"></a>

### [`004ae010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae010.md) → [`004ae010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md) _ZN5Botan8split_onERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc3f0.md) · 呼出先 4件 [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc110.md)
- 新版 呼出元 1件 [`00bdc440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc440.md) · 呼出先 4件 [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md)

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
      "definition_site": "004ae034",
      "incomplete_value": false,
      "site": "004ae038",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae034",
      "incomplete_value": false,
      "site": "004ae038",
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
      "004ae038",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ae070",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004ae070",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ae038",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ae070",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004ae070",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae010.md#insn-004ae034)
- 新版 `004ae034`（命令位置の公開資料なし）

~~~diff
- 004ae034 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004ae034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ae034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ae034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ae034 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004ae034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ae034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ae034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ae034 bytes 29811a91
+ 004ae034 bytes 29c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62084c48725d7e6d5021c21924ac2a9b"></a>

### [`004ae0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae0e8.md) → [`004ae0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae0e8.md) _ZN5Botan20parse_algorithm_nameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc120.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md)
- 新版 呼出元 1件 [`00bdc170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc170.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.70% / 新版 99.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ae9e4",
      "incomplete_value": true,
      "site": "004ae9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae9e4",
      "incomplete_value": true,
      "site": "004ae9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aeac4",
      "incomplete_value": true,
      "site": "004aeacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aeac4",
      "incomplete_value": true,
      "site": "004aeacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
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
      "004ae9e4",
      "READ",
      [
        "storage",
        "00c1b150",
        null,
        "pointer"
      ]
    ],
    [
      "004ae9e4",
      "PARAM",
      [
        "storage",
        "00bea730",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004aeac4",
      "READ",
      [
        "storage",
        "00c1b150",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ae9e4",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "004ae9e4",
      "PARAM",
      [
        "storage",
        "00bea780",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004aeac4",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae0e8.md#insn-004ae9e4) · [`004aeac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae0e8.md#insn-004aeac4)
- 新版 `004ae9e4`（命令位置の公開資料なし） · `004aeac4`（命令位置の公開資料なし）

~~~diff
- 004ae9e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:150:8"]]
- 004ae9e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ae9e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1a0:8"]]
+ 004ae9e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ae9e4 bytes 21a840f9
+ 004ae9e4 bytes 21d040f9
- 004aeac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:150:8"]]
- 004aeac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aeac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1a0:8"]]
+ 004aeac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004aeac4 bytes 21a840f9
+ 004aeac4 bytes 21d040f9
~~~


<a id="compare-66b07ce2f19de0e86f50a182c08c965c"></a>

### [`004b3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md) → [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md) FUN_004b3cec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004950f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b4a30.md) [`004b87c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b87c8.md) · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 5件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) [`004b87c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b3e18",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:9cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3e18",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:a5c:8"
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
      "definition_site": "004b3e20",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:63f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3e20",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:5b4:8"
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
      "definition_site": "004b3e28",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3e28",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:e2f:8"
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
      "004b3e18",
      "PARAM",
      [
        "storage",
        "00296a5c",
        null,
        "string"
      ]
    ],
    [
      "004b3e20",
      "PARAM",
      [
        "storage",
        "002a55b4",
        null,
        "string"
      ]
    ],
    [
      "004b3e28",
      "PARAM",
      [
        "storage",
        "00298e2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b3e18",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "004b3e20",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "004b3e28",
      "PARAM",
      [
        "storage",
        "00298da2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b3e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md#insn-004b3e18) · [`004b3e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md#insn-004b3e20) · [`004b3e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md#insn-004b3e28)
- 新版 `004b3e18`（命令位置の公開資料なし） · `004b3e20`（命令位置の公開資料なし） · `004b3e28`（命令位置の公開資料なし）

~~~diff
- 004b3e18 ["COPY", "tmp:0:8", ["const:a5c:8"]]
- 004b3e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b3e18 ["COPY", "tmp:0:8", ["const:9cf:8"]]
+ 004b3e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b3e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b3e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 bytes 00702991
+ 004b3e18 bytes 003c2791
- 004b3e20 ["COPY", "tmp:0:8", ["const:5b4:8"]]
- 004b3e20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b3e20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b3e20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b3e20 ["COPY", "tmp:0:8", ["const:63f:8"]]
+ 004b3e20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b3e20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b3e20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b3e20 bytes 21d01691
+ 004b3e20 bytes 21fc1891
- 004b3e28 ["COPY", "tmp:0:8", ["const:e2f:8"]]
- 004b3e28 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004b3e28 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004b3e28 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004b3e28 ["COPY", "tmp:0:8", ["const:da2:8"]]
+ 004b3e28 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004b3e28 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004b3e28 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004b3e28 bytes 42bc3891
+ 004b3e28 bytes 42883691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d885d537e405172257af8d2a2c1c4a42"></a>

### [`004b47ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b47ec.md) → [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) FUN_004b47ec

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004b868c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b868c.md) [`004bd550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd550.md) · 呼出先 9件 [`004aef94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004aef94.md) [`004af240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004af/004af240.md) [`004af83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004af/004af83c.md) [`004b02e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b0/004b02e0.md) [`004b105c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b1/004b105c.md)
- 新版 呼出元 2件 [`004b868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md) [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) · 呼出先 9件 [`004aef94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aef94.md) [`004af240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af240.md) [`004af83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af83c.md) [`004b02e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b0/004b02e0.md) [`004b105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b1/004b105c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b498c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:a3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b498c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:acb:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b4994",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:db1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4994",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:e3e:8"
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
      "definition_site": "004b499c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:58b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b499c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:4f1:8"
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
      "004b498c",
      "PARAM",
      [
        "storage",
        "00295acb",
        null,
        "string"
      ]
    ],
    [
      "004b4994",
      "PARAM",
      [
        "storage",
        "00298e3e",
        null,
        "string"
      ]
    ],
    [
      "004b499c",
      "PARAM",
      [
        "storage",
        "002a94f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b498c",
      "PARAM",
      [
        "storage",
        "00295a3e",
        null,
        "string"
      ]
    ],
    [
      "004b4994",
      "PARAM",
      [
        "storage",
        "00298db1",
        null,
        "string"
      ]
    ],
    [
      "004b499c",
      "PARAM",
      [
        "storage",
        "002a958b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b498c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b47ec.md#insn-004b498c) · [`004b4994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b47ec.md#insn-004b4994) · [`004b499c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b47ec.md#insn-004b499c)
- 新版 `004b498c`（命令位置の公開資料なし） · `004b4994`（命令位置の公開資料なし） · `004b499c`（命令位置の公開資料なし）

~~~diff
- 004b498c ["COPY", "tmp:0:8", ["const:acb:8"]]
- 004b498c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b498c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b498c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b498c ["COPY", "tmp:0:8", ["const:a3e:8"]]
+ 004b498c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b498c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b498c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b498c bytes 002c2b91
+ 004b498c bytes 00f82891
- 004b4994 ["COPY", "tmp:0:8", ["const:e3e:8"]]
- 004b4994 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b4994 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b4994 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b4994 ["COPY", "tmp:0:8", ["const:db1:8"]]
+ 004b4994 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4994 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4994 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b4994 bytes 21f83891
+ 004b4994 bytes 21c43691
- 004b499c ["COPY", "tmp:0:8", ["const:4f1:8"]]
- 004b499c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004b499c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004b499c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004b499c ["COPY", "tmp:0:8", ["const:58b:8"]]
+ 004b499c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004b499c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004b499c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004b499c bytes 42c41391
+ 004b499c bytes 422c1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6bc24e99ad76000782cee548945d4a5"></a>

### [`004b5004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5004.md) → [`004b5004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mmRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc410.md) · 呼出先 25件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00bdc460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc460.md) · 呼出先 25件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5094",
      "incomplete_value": false,
      "site": "004b50a0",
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
            "const:64e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5094",
      "incomplete_value": false,
      "site": "004b50a0",
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
            "const:5c3:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b50c0",
      "incomplete_value": false,
      "site": "004b50c8",
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
            "const:83d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b50c0",
      "incomplete_value": false,
      "site": "004b50c8",
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
            "const:8ca:8"
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
      "definition_site": "004b5104",
      "incomplete_value": false,
      "site": "004b510c",
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
            "const:5f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5104",
      "incomplete_value": false,
      "site": "004b510c",
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
            "const:559:8"
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
      "004b5094",
      "PARAM",
      [
        "storage",
        "002a55c3",
        null,
        "string"
      ]
    ],
    [
      "004b50c0",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ],
    [
      "004b5104",
      "PARAM",
      [
        "storage",
        "002a7559",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5094",
      "PARAM",
      [
        "storage",
        "002a564e",
        null,
        "string"
      ]
    ],
    [
      "004b50c0",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "004b5104",
      "PARAM",
      [
        "storage",
        "002a75f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5004.md#insn-004b5094) · [`004b50c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5004.md#insn-004b50c0) · [`004b5104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5004.md#insn-004b5104)
- 新版 `004b5094`（命令位置の公開資料なし） · `004b50c0`（命令位置の公開資料なし） · `004b5104`（命令位置の公開資料なし）

~~~diff
- 004b5094 ["COPY", "tmp:0:8", ["const:5c3:8"]]
- 004b5094 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004b5094 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004b5094 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004b5094 ["COPY", "tmp:0:8", ["const:64e:8"]]
+ 004b5094 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004b5094 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004b5094 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004b5094 bytes 420c1791
+ 004b5094 bytes 42381991
- 004b50c0 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 004b50c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b50c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b50c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b50c0 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004b50c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b50c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b50c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b50c0 bytes 21282391
+ 004b50c0 bytes 21f42091
- 004b5104 ["COPY", "tmp:0:8", ["const:559:8"]]
- 004b5104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b5104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b5104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b5104 ["COPY", "tmp:0:8", ["const:5f3:8"]]
+ 004b5104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b5104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b5104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b5104 bytes 21641591
+ 004b5104 bytes 21cc1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-596660ba80f9ee81b4b8323c604d8f18"></a>

### [`004b5c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5c14.md) → [`004b5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5c14.md) _ZN5Botan8is_primeERKNS_6BigIntERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc420.md) · 呼出先 14件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md) [`00bdbe20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe20.md)
- 新版 呼出元 1件 [`00bdc470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc470.md) · 呼出先 14件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdbe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe70.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

アドレスに依存する影響 `call_target` 10件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b63e0",
      "incomplete_value": true,
      "site": "004b63e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004b63e0",
      "incomplete_value": true,
      "site": "004b63e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5c94",
      "incomplete_value": true,
      "site": "004b5c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5c94",
      "incomplete_value": true,
      "site": "004b5c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5d04",
      "incomplete_value": true,
      "site": "004b5d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5d04",
      "incomplete_value": true,
      "site": "004b5d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b5c84",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b5cf4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b5d34",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b5c84",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b5cf4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b5d34",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5c14.md#insn-004b5c84) · [`004b5cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5c14.md#insn-004b5cf4) · [`004b5d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b5/004b5c14.md#insn-004b5d34)
- 新版 `004b5c84`（命令位置の公開資料なし） · `004b5cf4`（命令位置の公開資料なし） · `004b5d34`（命令位置の公開資料なし）

~~~diff
- 004b5c84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004b5c84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b5c84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004b5c84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b5c84 bytes 299543f9
+ 004b5c84 bytes 29bd43f9
- 004b5cf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004b5cf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b5cf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004b5cf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b5cf4 bytes 299543f9
+ 004b5cf4 bytes 29bd43f9
- 004b5d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004b5d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b5d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004b5d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b5d34 bytes 299543f9
+ 004b5d34 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f9ae1502641c021e1a755cf2da427f"></a>

### [`004b6640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6640.md) → [`004b6640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) _ZN5Botan6jacobiERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc490.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4e0.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.78% / 新版 93.78%

CFGの説明率　旧版 97.01% / 新版 97.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b66d0",
      "incomplete_value": true,
      "site": "004b66d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b66d0",
      "incomplete_value": true,
      "site": "004b66d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b6744",
      "incomplete_value": true,
      "site": "004b6744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b6744",
      "incomplete_value": true,
      "site": "004b6744",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b67b0",
      "incomplete_value": true,
      "site": "004b67b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b67b0",
      "incomplete_value": true,
      "site": "004b67b0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b666c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6b54"
      ]
    ],
    [
      "004b667c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6bb0"
      ]
    ],
    [
      "004b6684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6bb0"
      ]
    ]
  ],
  "added": [
    [
      "004b666c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6bb0"
      ]
    ],
    [
      "004b667c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6b54"
      ]
    ],
    [
      "004b6684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004b6b54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b6b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6640.md#insn-004b6b6c) · [`004b6ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6640.md#insn-004b6ba8) · [`004b6bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6640.md#insn-004b6bc8)
- 新版 `004b6bc8`（命令位置の公開資料なし） · `004b6c04`（命令位置の公開資料なし） · `004b6b6c`（命令位置の公開資料なし）

~~~diff
- 004b6b6c ["INT_ADD", "register:40f0:8", ["const:4b6b6c:8", "const:4:8"]]
- 004b6b6c ["CALL", null, ["callee:0041b298:8"]]
+ 004b6bc8 ["INT_ADD", "register:40f0:8", ["const:4b6bc8:8", "const:4:8"]]
+ 004b6bc8 ["CALL", null, ["callee:0041b298:8"]]
- 004b6b6c bytes cb91fd97
+ 004b6bc8 bytes b491fd97
- 004b6ba8 ["INT_ADD", "register:40f0:8", ["const:4b6ba8:8", "const:4:8"]]
- 004b6ba8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 004b6c04 ["INT_ADD", "register:40f0:8", ["const:4b6c04:8", "const:4:8"]]
+ 004b6c04 ["CALL", null, ["callee:00bdb0c0:8"]]
- 004b6ba8 bytes 32911c94
+ 004b6c04 bytes 2f911c94
- 004b6bc8 ["INT_ADD", "register:40f0:8", ["const:4b6bc8:8", "const:4:8"]]
- 004b6bc8 ["CALL", null, ["callee:0041b298:8"]]
+ 004b6b6c ["INT_ADD", "register:40f0:8", ["const:4b6b6c:8", "const:4:8"]]
+ 004b6b6c ["CALL", null, ["callee:0041b298:8"]]
- 004b6bc8 bytes b491fd97
+ 004b6b6c bytes cb91fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034baef3910a5dbd8281d489e0292808"></a>

### [`004b6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md) → [`004b6d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md) _ZN5Botan12random_primeERNS_21RandomNumberGeneratorEmRKNS_6BigIntEmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4a0.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004b76d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b76d8.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4f0.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004b76d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 8件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b6ddc",
      "incomplete_value": true,
      "site": "004b6ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b6ddc",
      "incomplete_value": true,
      "site": "004b6ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7098",
      "incomplete_value": true,
      "site": "004b7098",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7098",
      "incomplete_value": true,
      "site": "004b7098",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7134",
      "incomplete_value": true,
      "site": "004b7134",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7134",
      "incomplete_value": true,
      "site": "004b7134",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b6dcc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b6f44",
      "READ",
      [
        "storage",
        "00c1b168",
        null,
        "pointer"
      ]
    ],
    [
      "004b7088",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b6dcc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b6f44",
      "READ",
      [
        "storage",
        "00c1b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "004b7088",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b6dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md#insn-004b6dcc) · [`004b6f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md#insn-004b6f44) · [`004b7088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md#insn-004b7088)
- 新版 `004b6dcc`（命令位置の公開資料なし） · `004b6f44`（命令位置の公開資料なし） · `004b7088`（命令位置の公開資料なし）

~~~diff
- 004b6dcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004b6dcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b6dcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004b6dcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b6dcc bytes 299543f9
+ 004b6dcc bytes 29bd43f9
- 004b6f44 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:168:8"]]
- 004b6f44 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b6f44 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:1b8:8"]]
+ 004b6f44 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 004b6f44 bytes f7b640f9
+ 004b6f44 bytes f7de40f9
- 004b7088 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 004b7088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b7088 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 004b7088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b7088 bytes 899743f9
+ 004b7088 bytes 89bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1b47301aeb224e5f7a66d85ce26b854"></a>

### [`004b76d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b76d8.md) → [`004b76d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md) FUN_004b76d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md) · 呼出先 7件 [`00521f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00521/00521f70.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`004b6d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md) · 呼出先 7件 [`00521f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f70.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b779c",
      "incomplete_value": true,
      "site": "004b77a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b779c",
      "incomplete_value": true,
      "site": "004b77a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b77a0",
      "incomplete_value": true,
      "site": "004b77a4",
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
            "const:c1b000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b77a0",
      "incomplete_value": true,
      "site": "004b77a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b779c",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004b779c",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b77a0",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b779c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004b779c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b77a0",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b76d8.md#insn-004b7794) · [`004b779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b76d8.md#insn-004b779c) · [`004b77a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b76d8.md#insn-004b77a0)
- 新版 `004b7794`（命令位置の公開資料なし） · `004b779c`（命令位置の公開資料なし） · `004b77a0`（命令位置の公開資料なし）

~~~diff
- 004b7794 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004b7794 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004b7794 bytes 023b00f0
+ 004b7794 bytes 223b0090
- 004b779c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004b779c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b779c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004b779c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004b779c bytes 21d447f9
+ 004b779c bytes 21fc47f9
- 004b77a0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 004b77a0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b77a0 ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 004b77a0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004b77a0 bytes 42d847f9
+ 004b77a0 bytes 420040f9
~~~


<a id="compare-22878aeedffbeabcc7473978b78127f8"></a>

### [`004b77d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md) → [`004b77d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md) _ZN5Botan3gcdERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4c0.md) · 呼出先 9件 [`00496d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496d60.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md)
- 新版 呼出元 1件 [`00bdc510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc510.md) · 呼出先 9件 [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7924",
      "incomplete_value": true,
      "site": "004b7924",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7924",
      "incomplete_value": true,
      "site": "004b7924",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7950",
      "incomplete_value": true,
      "site": "004b7950",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7950",
      "incomplete_value": true,
      "site": "004b7950",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8108",
      "incomplete_value": true,
      "site": "004b8108",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8108",
      "incomplete_value": true,
      "site": "004b8108",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b7914",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b7940",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b80f8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7914",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b7940",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b80f8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md#insn-004b7914) · [`004b7940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md#insn-004b7940) · [`004b80f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md#insn-004b80f8)
- 新版 `004b7914`（命令位置の公開資料なし） · `004b7940`（命令位置の公開資料なし） · `004b80f8`（命令位置の公開資料なし）

~~~diff
- 004b7914 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b7914 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b7914 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b7914 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b7914 bytes 099743f9
+ 004b7914 bytes 09bf43f9
- 004b7940 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b7940 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b7940 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b7940 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b7940 bytes 099743f9
+ 004b7940 bytes 09bf43f9
- 004b80f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b80f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b80f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b80f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b80f8 bytes 099743f9
+ 004b80f8 bytes 09bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60a6580c4f01c7dc773b5e1066395c05"></a>

### [`004b8210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8210.md) → [`004b8210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8210.md) _ZN5Botan17random_safe_primeERNS_21RandomNumberGeneratorEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 15件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.09% / 新版 94.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b83d0",
      "incomplete_value": true,
      "site": "004b83d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b83d0",
      "incomplete_value": true,
      "site": "004b83d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b83fc",
      "incomplete_value": true,
      "site": "004b83fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b83fc",
      "incomplete_value": true,
      "site": "004b83fc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8428",
      "incomplete_value": true,
      "site": "004b8428",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8428",
      "incomplete_value": true,
      "site": "004b8428",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b83c0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b83ec",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b8418",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b83c0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b83ec",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b8418",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b83c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8210.md#insn-004b83c0) · [`004b83ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8210.md#insn-004b83ec) · [`004b8418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8210.md#insn-004b8418)
- 新版 `004b83c0`（命令位置の公開資料なし） · `004b83ec`（命令位置の公開資料なし） · `004b8418`（命令位置の公開資料なし）

~~~diff
- 004b83c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004b83c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b83c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004b83c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b83c0 bytes 299743f9
+ 004b83c0 bytes 29bf43f9
- 004b83ec ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004b83ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b83ec ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004b83ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b83ec bytes 299743f9
+ 004b83ec bytes 29bf43f9
- 004b8418 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004b8418 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8418 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004b8418 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8418 bytes 299743f9
+ 004b8418 bytes 29bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1092652c31de34312eb3b1e872c52824"></a>

### [`004b87c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b87c8.md) → [`004b87c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) _ZN5Botan7mul_addERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4d0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`004b3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md) [`004b3f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3f90.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdc520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc520.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

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
      "definition_site": "004b89a0",
      "incomplete_value": true,
      "site": "004b89a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b89a0",
      "incomplete_value": true,
      "site": "004b89a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b89e4",
      "incomplete_value": false,
      "site": "004b89ec",
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
            "const:dcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b89e4",
      "incomplete_value": false,
      "site": "004b89ec",
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
            "const:e58:8"
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
      "definition_site": "004b8a1c",
      "incomplete_value": true,
      "site": "004b8a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8a1c",
      "incomplete_value": true,
      "site": "004b8a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b8990",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b89e4",
      "PARAM",
      [
        "storage",
        "00298e58",
        null,
        "string"
      ]
    ],
    [
      "004b8a1c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b8990",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b89e4",
      "PARAM",
      [
        "storage",
        "00298dcb",
        null,
        "string"
      ]
    ],
    [
      "004b8a1c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b87c8.md#insn-004b8990) · [`004b89e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b87c8.md#insn-004b89e4) · [`004b8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b87c8.md#insn-004b8a1c)
- 新版 `004b8990`（命令位置の公開資料なし） · `004b89e4`（命令位置の公開資料なし） · `004b8a1c`（命令位置の公開資料なし）

~~~diff
- 004b8990 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004b8990 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8990 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004b8990 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8990 bytes 299543f9
+ 004b8990 bytes 29bd43f9
- 004b89e4 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 004b89e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b89e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b89e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b89e4 ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 004b89e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b89e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b89e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b89e4 bytes 21603991
+ 004b89e4 bytes 212c3791
- 004b8a1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004b8a1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8a1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004b8a1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8a1c bytes 217847f9
+ 004b8a1c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b8d5241d73a84ef892d3169443b4d1c"></a>

### [`004b8aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8aa0.md) → [`004b8aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8aa0.md) _ZN5Botan7sub_mulERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4e0.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc530.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8b34",
      "incomplete_value": false,
      "site": "004b8b3c",
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
            "const:3a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8b34",
      "incomplete_value": false,
      "site": "004b8b3c",
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
            "const:3a9:8"
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
      "definition_site": "004b8b6c",
      "incomplete_value": true,
      "site": "004b8b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8b6c",
      "incomplete_value": true,
      "site": "004b8b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b8b34",
      "PARAM",
      [
        "storage",
        "0029b3a9",
        null,
        "string"
      ]
    ],
    [
      "004b8b6c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004b8b6c",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004b8b34",
      "PARAM",
      [
        "storage",
        "0029b3a7",
        null,
        "string"
      ]
    ],
    [
      "004b8b6c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004b8b6c",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8aa0.md#insn-004b8b34) · [`004b8b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8aa0.md#insn-004b8b6c)
- 新版 `004b8b34`（命令位置の公開資料なし） · `004b8b6c`（命令位置の公開資料なし）

~~~diff
- 004b8b34 ["COPY", "tmp:0:8", ["const:3a9:8"]]
- 004b8b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b8b34 ["COPY", "tmp:0:8", ["const:3a7:8"]]
+ 004b8b34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8b34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8b34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8b34 bytes 21a40e91
+ 004b8b34 bytes 219c0e91
- 004b8b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004b8b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8b6c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004b8b6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8b6c bytes 217847f9
+ 004b8b6c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c50c3bb6d87171b95d908e96fccd75de"></a>

### [`004b8bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8bd8.md) → [`004b8bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8bd8.md) _ZN5Botan7mul_subERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8c94",
      "incomplete_value": true,
      "site": "004b8ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8c94",
      "incomplete_value": true,
      "site": "004b8ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b8c94",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004b8c94",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004b8c94",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004b8c94",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8bd8.md#insn-004b8c94)
- 新版 `004b8c94`（命令位置の公開資料なし）

~~~diff
- 004b8c94 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004b8c94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8c94 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004b8c94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8c94 bytes 217847f9
+ 004b8c94 bytes 21a047f9
~~~


<a id="compare-21b51b65a4e44695ded9c7183b6e6b84"></a>

### [`004b8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8d44.md) → [`004b8d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md) _ZN5Botan3lcmERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4f0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdbdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbdb0.md) [`00bdbdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbdf0.md) [`00bdc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4c0.md)
- 新版 呼出元 1件 [`00bdc540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) [`00bdbe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe40.md) [`00bdc510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc510.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8dbc",
      "incomplete_value": true,
      "site": "004b8dbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8dbc",
      "incomplete_value": true,
      "site": "004b8dbc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8de8",
      "incomplete_value": true,
      "site": "004b8de8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8de8",
      "incomplete_value": true,
      "site": "004b8de8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b8dac",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b8dd8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b8dac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b8dd8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8d44.md#insn-004b8dac) · [`004b8dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8d44.md#insn-004b8dd8)
- 新版 `004b8dac`（命令位置の公開資料なし） · `004b8dd8`（命令位置の公開資料なし）

~~~diff
- 004b8dac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004b8dac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8dac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004b8dac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8dac bytes 899643f9
+ 004b8dac bytes 89be43f9
- 004b8dd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004b8dd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8dd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004b8dd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8dd8 bytes 899643f9
+ 004b8dd8 bytes 89be43f9
~~~


<a id="compare-c759bd7ff9e563a3d86d740e77222c93"></a>

### [`004b8e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8e58.md) → [`004b8e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md) _ZN5Botan25almost_montgomery_inverseERNS_6BigIntERKS0_S3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc500.md) · 呼出先 10件 [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc30.md)
- 新版 呼出元 1件 [`00bdc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md) · 呼出先 10件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8f18",
      "incomplete_value": true,
      "site": "004b8f18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8f18",
      "incomplete_value": true,
      "site": "004b8f18",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b95c8",
      "incomplete_value": true,
      "site": "004b95c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b95c8",
      "incomplete_value": true,
      "site": "004b95c8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b9640",
      "incomplete_value": true,
      "site": "004b9640",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9640",
      "incomplete_value": true,
      "site": "004b9640",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b8f08",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b95bc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b9630",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b8f08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b95bc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b9630",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8e58.md#insn-004b8f08) · [`004b95bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8e58.md#insn-004b95bc) · [`004b95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8e58.md#insn-004b95c0)
- 新版 `004b8f08`（命令位置の公開資料なし） · `004b95bc`（命令位置の公開資料なし）

~~~diff
- 004b8f08 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004b8f08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8f08 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004b8f08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8f08 bytes 299743f9
+ 004b8f08 bytes 29bf43f9
- 004b95bc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004b95bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b95bc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004b95bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b95bc bytes 299743f9
+ 004b95bc bytes 29bf43f9
- 004b95c0 ["COPY", "register:4000:8", ["register:40b0:8"]]
- 004b95c0 bytes e00316aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-616073294d26ba3ce0cce0c3b74105c4"></a>

### [`004b9948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b9/004b9948.md) → [`004b9948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b9948.md) _ZN5Botan26ct_inverse_mod_odd_modulusERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc510.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048924c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048924c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc560.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048924c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b99f8",
      "incomplete_value": true,
      "site": "004b99f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b99f8",
      "incomplete_value": true,
      "site": "004b99f8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b9a54",
      "incomplete_value": true,
      "site": "004b9a54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9a54",
      "incomplete_value": true,
      "site": "004b9a54",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b9a80",
      "incomplete_value": true,
      "site": "004b9a80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9a80",
      "incomplete_value": true,
      "site": "004b9a80",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b99e8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a44",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a70",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b99e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a44",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a70",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b99e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b9/004b9948.md#insn-004b99e8) · [`004b9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b9/004b9948.md#insn-004b9a44) · [`004b9a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b9/004b9948.md#insn-004b9a70)
- 新版 `004b99e8`（命令位置の公開資料なし） · `004b9a44`（命令位置の公開資料なし） · `004b9a70`（命令位置の公開資料なし）

~~~diff
- 004b99e8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b99e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b99e8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b99e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b99e8 bytes 099743f9
+ 004b99e8 bytes 09bf43f9
- 004b9a44 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b9a44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b9a44 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b9a44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b9a44 bytes 099743f9
+ 004b9a44 bytes 09bf43f9
- 004b9a70 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004b9a70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b9a70 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004b9a70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b9a70 bytes 099743f9
+ 004b9a70 bytes 09bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a689462c38c121099f17e9d8457d6e6f"></a>

### [`004ba430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ba/004ba430.md) → [`004ba430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md) _ZN5Botan11inverse_modERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc520.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc570.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.34% / 新版 97.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 7件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ba4f4",
      "incomplete_value": true,
      "site": "004ba4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ba4f4",
      "incomplete_value": true,
      "site": "004ba4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ba518",
      "incomplete_value": true,
      "site": "004ba51c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ba518",
      "incomplete_value": true,
      "site": "004ba51c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc8:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004bad4c",
      "incomplete_value": true,
      "site": "004bad4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bad4c",
      "incomplete_value": true,
      "site": "004bad4c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ba4e0",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "004ba4f8",
      "DATA",
      [
        "storage",
        "00becc50",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ba518",
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ba4e0",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004ba4f8",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ba518",
      "READ",
      [
        "storage",
        "00c1b018",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ba4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ba/004ba430.md#insn-004ba4cc) · [`004ba4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ba/004ba430.md#insn-004ba4e0) · [`004ba50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ba/004ba430.md#insn-004ba50c)
- 新版 `004ba4cc`（命令位置の公開資料なし） · `004ba4e0`（命令位置の公開資料なし） · `004ba50c`（命令位置の公開資料なし）

~~~diff
- 004ba4cc ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004ba4cc ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 004ba4cc bytes 093b0090
+ 004ba4cc bytes 093b00b0
- 004ba4e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
- 004ba4e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ba4e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
+ 004ba4e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ba4e0 bytes 29e147f9
+ 004ba4e0 bytes 290940f9
- 004ba50c ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004ba50c ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004ba50c bytes 013b0090
+ 004ba50c bytes 013b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a7e8fb53eee3356912d709c6c6d8c86"></a>

### [`004bb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb030.md) → [`004bb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md) _ZN5Botan13monty_inverseEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc530.md) · 呼出先 8件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00498c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc580.md) · 呼出先 8件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb0ec",
      "incomplete_value": false,
      "site": "004bb0f4",
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
            "const:b0e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb0ec",
      "incomplete_value": false,
      "site": "004bb0f4",
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
            "const:b9b:8"
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
      "definition_site": "004bb128",
      "incomplete_value": true,
      "site": "004bb134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb128",
      "incomplete_value": true,
      "site": "004bb134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb14c",
      "incomplete_value": false,
      "site": "004bb16c",
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
            "const:3be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb14c",
      "incomplete_value": false,
      "site": "004bb16c",
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
            "const:333:8"
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
      "004bb0ec",
      "PARAM",
      [
        "storage",
        "00297b9b",
        null,
        "string"
      ]
    ],
    [
      "004bb128",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004bb128",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bb0ec",
      "PARAM",
      [
        "storage",
        "00297b0e",
        null,
        "string"
      ]
    ],
    [
      "004bb128",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "004bb128",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb030.md#insn-004bb0ec) · [`004bb128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb030.md#insn-004bb128) · [`004bb14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb030.md#insn-004bb14c)
- 新版 `004bb0ec`（命令位置の公開資料なし） · `004bb128`（命令位置の公開資料なし） · `004bb14c`（命令位置の公開資料なし）

~~~diff
- 004bb0ec ["COPY", "tmp:0:8", ["const:b9b:8"]]
- 004bb0ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bb0ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bb0ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bb0ec ["COPY", "tmp:0:8", ["const:b0e:8"]]
+ 004bb0ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb0ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb0ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bb0ec bytes 216c2e91
+ 004bb0ec bytes 21382c91
- 004bb128 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 004bb128 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb128 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 004bb128 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb128 bytes 21a447f9
+ 004bb128 bytes 21cc47f9
- 004bb14c ["COPY", "tmp:0:8", ["const:333:8"]]
- 004bb14c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bb14c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bb14c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bb14c ["COPY", "tmp:0:8", ["const:3be:8"]]
+ 004bb14c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb14c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb14c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bb14c bytes 00cc0c91
+ 004bb14c bytes 00f80e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca65893b29136c02a7bd7d02e8ad9d7"></a>

### [`004bb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb3f0.md) → [`004bb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb3f0.md) _ZNK5Botan9Power_Mod8set_baseERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc450.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb460",
      "incomplete_value": false,
      "site": "004bb468",
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
            "const:a05:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb460",
      "incomplete_value": false,
      "site": "004bb468",
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
            "const:a92:8"
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
      "definition_site": "004bb49c",
      "incomplete_value": true,
      "site": "004bb4a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb49c",
      "incomplete_value": true,
      "site": "004bb4a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb500",
      "incomplete_value": false,
      "site": "004bb508",
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
            "const:a41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb500",
      "incomplete_value": false,
      "site": "004bb508",
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
            "const:ad5:8"
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
      "004bb460",
      "PARAM",
      [
        "storage",
        "00296a92",
        null,
        "string"
      ]
    ],
    [
      "004bb49c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004bb49c",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bb460",
      "PARAM",
      [
        "storage",
        "00296a05",
        null,
        "string"
      ]
    ],
    [
      "004bb49c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004bb49c",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb3f0.md#insn-004bb460) · [`004bb49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb3f0.md#insn-004bb49c) · [`004bb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb3f0.md#insn-004bb500)
- 新版 `004bb460`（命令位置の公開資料なし） · `004bb49c`（命令位置の公開資料なし） · `004bb500`（命令位置の公開資料なし）

~~~diff
- 004bb460 ["COPY", "tmp:0:8", ["const:a92:8"]]
- 004bb460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bb460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bb460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bb460 ["COPY", "tmp:0:8", ["const:a05:8"]]
+ 004bb460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bb460 bytes 21482a91
+ 004bb460 bytes 21142891
- 004bb49c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004bb49c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb49c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004bb49c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb49c bytes 217847f9
+ 004bb49c bytes 21a047f9
- 004bb500 ["COPY", "tmp:0:8", ["const:ad5:8"]]
- 004bb500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bb500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bb500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bb500 ["COPY", "tmp:0:8", ["const:a41:8"]]
+ 004bb500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bb500 bytes 21542b91
+ 004bb500 bytes 21042991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92db763fb5f30266809c7fc36e49755f"></a>

### [`004bb59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb59c.md) → [`004bb59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb59c.md) _ZNK5Botan9Power_Mod12set_exponentERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc560.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5b0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb648",
      "incomplete_value": true,
      "site": "004bb654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb648",
      "incomplete_value": true,
      "site": "004bb654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb670",
      "incomplete_value": false,
      "site": "004bb678",
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
            "const:5c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb670",
      "incomplete_value": false,
      "site": "004bb678",
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
            "const:53e:8"
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
      "definition_site": "004bb6ac",
      "incomplete_value": true,
      "site": "004bb6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb6ac",
      "incomplete_value": true,
      "site": "004bb6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "004bb648",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004bb648",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004bb670",
      "PARAM",
      [
        "storage",
        "0029c53e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bb648",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004bb648",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004bb670",
      "PARAM",
      [
        "storage",
        "0029c5c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb59c.md#insn-004bb648) · [`004bb670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb59c.md#insn-004bb670) · [`004bb6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb59c.md#insn-004bb6a0)
- 新版 `004bb648`（命令位置の公開資料なし） · `004bb670`（命令位置の公開資料なし） · `004bb6a0`（命令位置の公開資料なし）

~~~diff
- 004bb648 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004bb648 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb648 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004bb648 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb648 bytes 217847f9
+ 004bb648 bytes 21a047f9
- 004bb670 ["COPY", "tmp:0:8", ["const:53e:8"]]
- 004bb670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bb670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bb670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bb670 ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 004bb670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bb670 bytes 21f81491
+ 004bb670 bytes 21241791
- 004bb6a0 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004bb6a0 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004bb6a0 bytes e13a00f0
+ 004bb6a0 bytes 013b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bd32a78017a1fe5585f0bf2c8a8742"></a>

### [`004bb70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb70c.md) → [`004bb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb70c.md) _ZNK5Botan9Power_Mod7executeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc460.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4b0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb774",
      "incomplete_value": false,
      "site": "004bb77c",
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
            "const:7d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb774",
      "incomplete_value": false,
      "site": "004bb77c",
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
            "const:85f:8"
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
      "definition_site": "004bb7b0",
      "incomplete_value": true,
      "site": "004bb7bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb7b0",
      "incomplete_value": true,
      "site": "004bb7bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "004bb774",
      "PARAM",
      [
        "storage",
        "0029285f",
        null,
        "string"
      ]
    ],
    [
      "004bb7b0",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "004bb7b0",
      "PARAM",
      [
        "storage",
        "00be93b8",
        "_ZTIN5Botan14Internal_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bb774",
      "PARAM",
      [
        "storage",
        "002927d2",
        null,
        "string"
      ]
    ],
    [
      "004bb7b0",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "004bb7b0",
      "PARAM",
      [
        "storage",
        "00be9408",
        "_ZTIN5Botan14Internal_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb70c.md#insn-004bb774) · [`004bb7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb70c.md#insn-004bb7a4) · [`004bb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb70c.md#insn-004bb7b0)
- 新版 `004bb774`（命令位置の公開資料なし） · `004bb7a4`（命令位置の公開資料なし） · `004bb7b0`（命令位置の公開資料なし）

~~~diff
- 004bb774 ["COPY", "tmp:0:8", ["const:85f:8"]]
- 004bb774 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bb774 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bb774 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bb774 ["COPY", "tmp:0:8", ["const:7d2:8"]]
+ 004bb774 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb774 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bb774 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bb774 bytes 217c2191
+ 004bb774 bytes 21481f91
- 004bb7a4 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004bb7a4 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004bb7a4 bytes e13a00f0
+ 004bb7a4 bytes 013b0090
- 004bb7b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
- 004bb7b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb7b0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
+ 004bb7b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb7b0 bytes 21dc47f9
+ 004bb7b0 bytes 210440f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb49e28e0d6a0cb49163b3c46beb0d6"></a>

### [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) → [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) FUN_004bb810

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0050ffa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050ffa4.md) [`005100e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005100e0.md) [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md) [`005162fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005162fc.md) [`005163b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005163b4.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 7件 [`0050ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) [`005100e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) [`005162fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005162fc.md) [`005163b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005163b4.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bb848",
      "incomplete_value": true,
      "site": "004bb848",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb848",
      "incomplete_value": true,
      "site": "004bb848",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bb874",
      "incomplete_value": true,
      "site": "004bb874",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb874",
      "incomplete_value": true,
      "site": "004bb874",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bb8a0",
      "incomplete_value": true,
      "site": "004bb8a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8a0",
      "incomplete_value": true,
      "site": "004bb8a0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bb838",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bb864",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bb890",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bb838",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bb864",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bb890",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md#insn-004bb838) · [`004bb864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md#insn-004bb864) · [`004bb890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md#insn-004bb890)
- 新版 `004bb838`（命令位置の公開資料なし） · `004bb864`（命令位置の公開資料なし） · `004bb890`（命令位置の公開資料なし）

~~~diff
- 004bb838 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004bb838 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb838 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004bb838 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb838 bytes a99643f9
+ 004bb838 bytes a9be43f9
- 004bb864 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004bb864 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb864 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004bb864 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb864 bytes a99643f9
+ 004bb864 bytes a9be43f9
- 004bb890 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004bb890 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb890 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004bb890 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb890 bytes a99643f9
+ 004bb890 bytes a9be43f9
~~~


<a id="compare-b5ddcc60cda8005ae6a8d9eb9fbed937"></a>

### [`004bb8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb8d4.md) → [`004bb8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb8d4.md) _ZN5Botan9Power_ModC1ERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc550.md) · 呼出先 1件 [`00bdc570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc570.md)
- 新版 呼出元 1件 [`00bdc5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5a0.md) · 呼出先 1件 [`00bdc5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bb8f0",
      "incomplete_value": true,
      "site": "004bb8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bb8f0",
      "incomplete_value": true,
      "site": "004bb8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004bb8e8",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "004bb8f0",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004bb8e8",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004bb8f0",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb8d4.md#insn-004bb8e8)
- 新版 `004bb8e8`（命令位置の公開資料なし）

~~~diff
- 004bb8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 004bb8e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 004bb8e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb8e8 bytes 08b940f9
+ 004bb8e8 bytes 08e140f9
~~~


<a id="compare-93f00ceab7f8f99046021c42720be57b"></a>

### [`004bb928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb928.md) → [`004bb928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md) _ZNK5Botan9Power_Mod11set_modulusERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc570.md) · 呼出先 8件 [`004bd8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd8d4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md)
- 新版 呼出元 1件 [`00bdc5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5c0.md) · 呼出先 8件 [`004bd8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

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
      "definition_site": "004bba20",
      "incomplete_value": false,
      "site": "004bba20",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bba20",
      "incomplete_value": false,
      "site": "004bba20",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bb9bc",
      "incomplete_value": true,
      "site": "004bb9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb9bc",
      "incomplete_value": true,
      "site": "004bb9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004bb9ac",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bba20",
      "DATA",
      [
        "storage",
        "00be9da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004bb9ac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bba20",
      "DATA",
      [
        "storage",
        "00be9df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb928.md#insn-004bb9ac) · [`004bba1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb928.md#insn-004bba1c)
- 新版 `004bb9ac`（命令位置の公開資料なし） · `004bba1c`（命令位置の公開資料なし）

~~~diff
- 004bb9ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bb9ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bb9ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bb9ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb9ac bytes 299543f9
+ 004bb9ac bytes 29bd43f9
- 004bba1c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 004bba1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004bba1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004bba1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004bba1c ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 004bba1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004bba1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004bba1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004bba1c bytes 08a13691
+ 004bba1c bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7fc950376e496993f5c52b2c22588d6"></a>

### [`004bbab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbab8.md) → [`004bbab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbab8.md) _ZN5Botan9Power_ModC1ERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bbad8",
      "incomplete_value": true,
      "site": "004bbadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bbad8",
      "incomplete_value": true,
      "site": "004bbadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004bbacc",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "004bbadc",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004bbacc",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004bbadc",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bbacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbab8.md#insn-004bbacc)
- 新版 `004bbacc`（命令位置の公開資料なし）

~~~diff
- 004bbacc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 004bbacc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbacc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 004bbacc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbacc bytes 08b940f9
+ 004bbacc bytes 08e140f9
~~~


<a id="compare-cd284ea12255a40b5c3f9b3dbd9d1a38"></a>

### [`004bbdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbdd8.md) → [`004bbdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbdd8.md) _ZN5Botan20Fixed_Base_Power_ModC1ERKNS_6BigIntES3_NS_9Power_Mod11Usage_HintsE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md) [`00bdc450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc450.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bbf7c",
      "incomplete_value": true,
      "site": "004bbf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bbf7c",
      "incomplete_value": true,
      "site": "004bbf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004bbf9c",
      "incomplete_value": true,
      "site": "004bbfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bbf9c",
      "incomplete_value": true,
      "site": "004bbfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004bbe54",
      "incomplete_value": true,
      "site": "004bbe54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbe54",
      "incomplete_value": true,
      "site": "004bbe54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004bbe44",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bbf74",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "004bbf7c",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004bbe44",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bbf74",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004bbf7c",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bbe44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbdd8.md#insn-004bbe44) · [`004bbf74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbdd8.md#insn-004bbf74) · [`004bbf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbdd8.md#insn-004bbf98)
- 新版 `004bbe44`（命令位置の公開資料なし） · `004bbf74`（命令位置の公開資料なし） · `004bbf98`（命令位置の公開資料なし）

~~~diff
- 004bbe44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bbe44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbe44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bbe44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbe44 bytes 299543f9
+ 004bbe44 bytes 29bd43f9
- 004bbf74 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:170:8"]]
- 004bbf74 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbf74 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:1c0:8"]]
+ 004bbf74 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbf74 bytes f7ba40f9
+ 004bbf74 bytes f7e240f9
- 004bbf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:180:8"]]
- 004bbf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1d0:8"]]
+ 004bbf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbf98 bytes 08c140f9
+ 004bbf98 bytes 08e940f9
~~~


<a id="compare-87cb4149f58d19054adc3902865859e0"></a>

### [`004bc070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc070.md) → [`004bc070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md) FUN_004bc070

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00521f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00521/00521f84.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00521f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f84.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc208",
      "incomplete_value": true,
      "site": "004bc208",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc208",
      "incomplete_value": true,
      "site": "004bc208",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc294",
      "incomplete_value": true,
      "site": "004bc294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc294",
      "incomplete_value": true,
      "site": "004bc294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc378",
      "incomplete_value": true,
      "site": "004bc378",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc378",
      "incomplete_value": true,
      "site": "004bc378",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bc1f8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bc284",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bc368",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc1f8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bc284",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bc368",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc070.md#insn-004bc1f8) · [`004bc284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc070.md#insn-004bc284) · [`004bc368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc070.md#insn-004bc368)
- 新版 `004bc1f8`（命令位置の公開資料なし） · `004bc284`（命令位置の公開資料なし） · `004bc368`（命令位置の公開資料なし）

~~~diff
- 004bc1f8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004bc1f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc1f8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004bc1f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc1f8 bytes 299743f9
+ 004bc1f8 bytes 29bf43f9
- 004bc284 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bc284 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc284 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bc284 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc284 bytes 299543f9
+ 004bc284 bytes 29bd43f9
- 004bc368 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004bc368 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc368 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004bc368 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc368 bytes 499743f9
+ 004bc368 bytes 49bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584f4ad934ebd964ae2dac2f3f5add5a"></a>

### [`004bc440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc440.md) → [`004bc440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md) FUN_004bc440

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbdb0.md) [`00bdbe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe70.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) [`00bdbec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbec0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc5bc",
      "incomplete_value": true,
      "site": "004bc5bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc5bc",
      "incomplete_value": true,
      "site": "004bc5bc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc620",
      "incomplete_value": true,
      "site": "004bc620",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc620",
      "incomplete_value": true,
      "site": "004bc620",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc688",
      "incomplete_value": true,
      "site": "004bc688",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc688",
      "incomplete_value": true,
      "site": "004bc688",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bc5ac",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bc610",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bc678",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc5ac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bc610",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bc678",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc440.md#insn-004bc5ac) · [`004bc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc440.md#insn-004bc610) · [`004bc678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc440.md#insn-004bc678)
- 新版 `004bc5ac`（命令位置の公開資料なし） · `004bc610`（命令位置の公開資料なし） · `004bc678`（命令位置の公開資料なし）

~~~diff
- 004bc5ac ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 004bc5ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc5ac ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 004bc5ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc5ac bytes 699743f9
+ 004bc5ac bytes 69bf43f9
- 004bc610 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 004bc610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc610 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 004bc610 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc610 bytes 699743f9
+ 004bc610 bytes 69bf43f9
- 004bc678 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 004bc678 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc678 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 004bc678 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc678 bytes 699743f9
+ 004bc678 bytes 69bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-923f6893d4280e11480e3e028cf3ae83"></a>

### [`004bc804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc804.md) → [`004bc804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md) FUN_004bc804

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3f90.md) [`004b4c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b4c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.54% / 新版 99.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bc99c",
      "incomplete_value": true,
      "site": "004bc99c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc99c",
      "incomplete_value": true,
      "site": "004bc99c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bca54",
      "incomplete_value": true,
      "site": "004bca54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bca54",
      "incomplete_value": true,
      "site": "004bca54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bcba0",
      "incomplete_value": true,
      "site": "004bcba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcba0",
      "incomplete_value": true,
      "site": "004bcba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004bc98c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bca44",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bcb90",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc98c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bca44",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bcb90",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc804.md#insn-004bc98c) · [`004bca44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc804.md#insn-004bca44) · [`004bcb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bc804.md#insn-004bcb90)
- 新版 `004bc98c`（命令位置の公開資料なし） · `004bca44`（命令位置の公開資料なし） · `004bcb90`（命令位置の公開資料なし）

~~~diff
- 004bc98c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004bc98c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bc98c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004bc98c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bc98c bytes e99643f9
+ 004bc98c bytes e9be43f9
- 004bca44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bca44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bca44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bca44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bca44 bytes 299543f9
+ 004bca44 bytes 29bd43f9
- 004bcb90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bcb90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bcb90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bcb90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bcb90 bytes 299543f9
+ 004bcb90 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a23470eb96aad04b3c785903ef11eba"></a>

### [`004bcf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bcf24.md) → [`004bcf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md) _ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc480.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`004958dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004958dc.md) [`00496d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdc4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4d0.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd364",
      "incomplete_value": true,
      "site": "004bd364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd364",
      "incomplete_value": true,
      "site": "004bd364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd3f8",
      "incomplete_value": true,
      "site": "004bd3f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd3f8",
      "incomplete_value": true,
      "site": "004bd3f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 20,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd428",
      "incomplete_value": true,
      "site": "004bd428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd428",
      "incomplete_value": true,
      "site": "004bd428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bd354",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bd3e8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bd418",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bd354",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bd3e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bd418",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bcf24.md#insn-004bd354) · [`004bd3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bcf24.md#insn-004bd3e8) · [`004bd418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bc/004bcf24.md#insn-004bd418)
- 新版 `004bd354`（命令位置の公開資料なし） · `004bd3e8`（命令位置の公開資料なし） · `004bd418`（命令位置の公開資料なし）

~~~diff
- 004bd354 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bd354 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd354 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bd354 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd354 bytes 299543f9
+ 004bd354 bytes 29bd43f9
- 004bd3e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bd3e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd3e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bd3e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd3e8 bytes 299543f9
+ 004bd3e8 bytes 29bd43f9
- 004bd418 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004bd418 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd418 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004bd418 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd418 bytes 299543f9
+ 004bd418 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f1f3c4729839c5c68c5ebc05096142"></a>

### [`004bd550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd550.md) → [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) FUN_004bd550

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3f90.md) [`004b47ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b47ec.md) [`004b4c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`004b4c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd7d4",
      "incomplete_value": true,
      "site": "004bd7d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd7d4",
      "incomplete_value": true,
      "site": "004bd7d4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd800",
      "incomplete_value": true,
      "site": "004bd800",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd800",
      "incomplete_value": true,
      "site": "004bd800",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd82c",
      "incomplete_value": true,
      "site": "004bd82c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd82c",
      "incomplete_value": true,
      "site": "004bd82c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bd7c4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bd7f0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bd81c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bd7c4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bd7f0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bd81c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd550.md#insn-004bd7c4) · [`004bd7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd550.md#insn-004bd7f0) · [`004bd81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd550.md#insn-004bd81c)
- 新版 `004bd7c4`（命令位置の公開資料なし） · `004bd7f0`（命令位置の公開資料なし） · `004bd81c`（命令位置の公開資料なし）

~~~diff
- 004bd7c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004bd7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd7c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004bd7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd7c4 bytes 899643f9
+ 004bd7c4 bytes 89be43f9
- 004bd7f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004bd7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd7f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004bd7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd7f0 bytes 899643f9
+ 004bd7f0 bytes 89be43f9
- 004bd81c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004bd81c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bd81c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004bd81c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bd81c bytes 899643f9
+ 004bd81c bytes 89be43f9
~~~


<a id="compare-8524f99ee021e0c85297559b661cd38f"></a>

### [`004bd8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd8d4.md) → [`004bd8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md) FUN_004bd8d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004bb928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb928.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`004bb928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004bd908",
      "incomplete_value": false,
      "site": "004bd918",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd908",
      "incomplete_value": false,
      "site": "004bd918",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bda94",
      "incomplete_value": true,
      "site": "004bda94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bda94",
      "incomplete_value": true,
      "site": "004bda94",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bdadc",
      "incomplete_value": true,
      "site": "004bdadc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdadc",
      "incomplete_value": true,
      "site": "004bdadc",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bd918",
      "DATA",
      [
        "storage",
        "00be9de8",
        null,
        "undefined *"
      ]
    ],
    [
      "004bda84",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bdacc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bd918",
      "DATA",
      [
        "storage",
        "00be9e38",
        null,
        "undefined *"
      ]
    ],
    [
      "004bda84",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bdacc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd8d4.md#insn-004bd908) · [`004bda84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd8d4.md#insn-004bda84) · [`004bdacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bd8d4.md#insn-004bdacc)
- 新版 `004bd908`（命令位置の公開資料なし） · `004bda84`（命令位置の公開資料なし） · `004bdacc`（命令位置の公開資料なし）

~~~diff
- 004bd908 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 004bd908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004bd908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004bd908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004bd908 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 004bd908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004bd908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004bd908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004bd908 bytes 29a13791
+ 004bd908 bytes 29e13891
- 004bda84 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004bda84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bda84 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004bda84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bda84 bytes 099743f9
+ 004bda84 bytes 09bf43f9
- 004bdacc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 004bdacc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bdacc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 004bdacc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bdacc bytes 099743f9
+ 004bdacc bytes 09bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc6680c97edeab3f177745512f4365ff"></a>

### [`004bdcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdcd0.md) → [`004bdcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdcd0.md) FUN_004bdcd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bdd38",
      "incomplete_value": true,
      "site": "004bdd38",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdd38",
      "incomplete_value": true,
      "site": "004bdd38",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bdd28",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bdd28",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bdd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdcd0.md#insn-004bdd28)
- 新版 `004bdd28`（命令位置の公開資料なし）

~~~diff
- 004bdd28 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004bdd28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bdd28 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004bdd28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bdd28 bytes c99643f9
+ 004bdd28 bytes c9be43f9
~~~


<a id="compare-e26b3a530371cfc24945f7f8b4dd7526"></a>

### [`004bdd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdd7c.md) → [`004bdd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md) _ZN5Botan15Modular_ReducerC2ERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc440.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc490.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bde20",
      "incomplete_value": true,
      "site": "004bde20",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bde20",
      "incomplete_value": true,
      "site": "004bde20",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bdee8",
      "incomplete_value": true,
      "site": "004bdee8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdee8",
      "incomplete_value": true,
      "site": "004bdee8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bdfa0",
      "incomplete_value": true,
      "site": "004bdfa0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdfa0",
      "incomplete_value": true,
      "site": "004bdfa0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bde10",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bded8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004bdf90",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bde10",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bded8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bdf90",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bde10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdd7c.md#insn-004bde10) · [`004bded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdd7c.md#insn-004bded8) · [`004bdf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bd/004bdd7c.md#insn-004bdf90)
- 新版 `004bde10`（命令位置の公開資料なし） · `004bded8`（命令位置の公開資料なし） · `004bdf90`（命令位置の公開資料なし）

~~~diff
- 004bde10 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004bde10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bde10 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004bde10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bde10 bytes 499743f9
+ 004bde10 bytes 49bf43f9
- 004bded8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004bded8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bded8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004bded8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bded8 bytes 499743f9
+ 004bded8 bytes 49bf43f9
- 004bdf90 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004bdf90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bdf90 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004bdf90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bdf90 bytes 499743f9
+ 004bdf90 bytes 49bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02cce442a567121a6a3f83d8e85fdfcf"></a>

### [`004be0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004be/004be0f4.md) → [`004be0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004be/004be0f4.md) _ZN5Botan6ressolERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.84% / 新版 90.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 42件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004be170",
      "incomplete_value": true,
      "site": "004be170",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be170",
      "incomplete_value": true,
      "site": "004be170",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004be1c0",
      "incomplete_value": true,
      "site": "004be1c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be1c0",
      "incomplete_value": true,
      "site": "004be1c0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004be224",
      "incomplete_value": true,
      "site": "004be224",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be224",
      "incomplete_value": true,
      "site": "004be224",
      "value": [
        "LOAD",
        "8",
        [
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
      "004be160",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004be1b0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004be214",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004be160",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004be1b0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004be214",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004be/004be0f4.md#insn-004be160) · [`004be174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004be/004be0f4.md#insn-004be174)
- 新版 `004be160`（命令位置の公開資料なし） · `004be174`（命令位置の公開資料なし）

~~~diff
- 004be160 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004be160 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004be160 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004be160 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004be160 bytes 299743f9
+ 004be160 bytes 29bf43f9
- 004be174 ["COPY", "register:4000:8", ["register:40b8:8"]]
- 004be174 bytes e00317aa
+ 004be174 ["COPY", "register:4000:8", ["register:40b8:8"]]
+ 004be174 bytes e00317aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345d5f99e40bec31e5938e2f6637ed68"></a>

### [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) → [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) FUN_004bf57c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`004bf520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf520.md) [`004c0520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c0520.md) [`004c05d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05d4.md) [`004c8d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8d94.md) [`004c94e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c94e0.md) · 呼出先 40件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md)
- 新版 呼出元 6件 [`004bf520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf520.md) [`004c0520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0520.md) [`004c05d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05d4.md) [`004c8d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md) [`004c94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md) · 呼出先 40件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.98% / 新版 94.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 11件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004bf624",
      "incomplete_value": false,
      "site": "004bf624",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf624",
      "incomplete_value": false,
      "site": "004bf624",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bf9bc",
      "incomplete_value": true,
      "site": "004bf9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:29a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf9bc",
      "incomplete_value": true,
      "site": "004bf9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:29c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bfa18",
      "incomplete_value": true,
      "site": "004bfa18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfa18",
      "incomplete_value": true,
      "site": "004bfa18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bf5e0",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ],
    [
      "004bf624",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004bf668",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bf5e0",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "004bf624",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004bf668",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md#insn-004bf5e0) · [`004bf61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md#insn-004bf61c) · [`004bf750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md#insn-004bf750)
- 新版 `004bf5e0`（命令位置の公開資料なし） · `004bf61c`（命令位置の公開資料なし） · `004bf750`（命令位置の公開資料なし）

~~~diff
- 004bf5e0 ["COPY", "tmp:0:8", ["const:286:8"]]
- 004bf5e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bf5e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bf5e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bf5e0 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004bf5e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf5e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf5e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bf5e0 bytes 21180a91
+ 004bf5e0 bytes 21100a91
- 004bf61c ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004bf61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004bf61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004bf61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004bf61c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004bf61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004bf61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004bf61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004bf61c bytes 08811a91
+ 004bf61c bytes 08c11b91
- 004bf750 ["COPY", "tmp:0:8", ["const:e7c:8"]]
- 004bf750 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bf750 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bf750 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bf750 ["COPY", "tmp:0:8", ["const:def:8"]]
+ 004bf750 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf750 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf750 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bf750 bytes 00f03991
+ 004bf750 bytes 00bc3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aea57d637ee5fb0644abe7e93a1eb06a"></a>

### [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) → [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) _ZN5Botan13pbes2_decryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5b0.md) · 呼出先 36件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00513138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513138.md)
- 新版 呼出元 1件 [`00bdc600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc600.md) · 呼出先 36件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00513138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 8件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c063c",
      "incomplete_value": true,
      "site": "004c063c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c063c",
      "incomplete_value": true,
      "site": "004c063c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c07d0",
      "incomplete_value": true,
      "site": "004c07d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c07d0",
      "incomplete_value": true,
      "site": "004c07d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:330:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c09f8",
      "incomplete_value": false,
      "site": "004c09f8",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c09f8",
      "incomplete_value": false,
      "site": "004c09f8",
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
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c0628",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004c063c",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c0670",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004c0628",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004c063c",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c0670",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md#insn-004c0628) · [`004c0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md#insn-004c0718) · [`004c075c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md#insn-004c075c)
- 新版 `004c0628`（命令位置の公開資料なし） · `004c0718`（命令位置の公開資料なし） · `004c075c`（命令位置の公開資料なし）

~~~diff
- 004c0628 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:ef8:8"]]
- 004c0628 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0628 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:f48:8"]]
+ 004c0628 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c0628 bytes f77e47f9
+ 004c0628 bytes f7a647f9
- 004c0718 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 004c0718 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0718 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 004c0718 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c0718 bytes 899743f9
+ 004c0718 bytes 89bf43f9
- 004c075c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 004c075c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c075c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 004c075c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c075c bytes 899743f9
+ 004c075c bytes 89bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69bdf8b728b177ff3ddef4b1bf8b2bd4"></a>

### [`004c1804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1804.md) → [`004c1804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1804.md) _ZN5Botan5PBKDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc580.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00bdc5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5d0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.50% / 新版 99.50%

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
      "definition_site": "004c1b0c",
      "incomplete_value": true,
      "site": "004c1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c1b0c",
      "incomplete_value": true,
      "site": "004c1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c1a68",
      "incomplete_value": false,
      "site": "004c1a70",
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
            "const:284:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1a68",
      "incomplete_value": false,
      "site": "004c1a70",
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
            "const:286:8"
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
      "004c1a68",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ],
    [
      "004c1b00",
      "READ",
      [
        "storage",
        "00c1b188",
        null,
        "pointer"
      ]
    ],
    [
      "004c1b0c",
      "DATA",
      [
        "storage",
        "00beb520",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "004c1a68",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "004c1b00",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c1b0c",
      "DATA",
      [
        "storage",
        "00beb570",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1804.md#insn-004c1a68) · [`004c1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1804.md#insn-004c1b00)
- 新版 `004c1a68`（命令位置の公開資料なし） · `004c1b00`（命令位置の公開資料なし）

~~~diff
- 004c1a68 ["COPY", "tmp:0:8", ["const:286:8"]]
- 004c1a68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c1a68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c1a68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c1a68 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 004c1a68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c1a68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c1a68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c1a68 bytes 21180a91
+ 004c1a68 bytes 21100a91
- 004c1b00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:188:8"]]
- 004c1b00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1b00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1d8:8"]]
+ 004c1b00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1b00 bytes 08c540f9
+ 004c1b00 bytes 08ed40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d32b218f8fc3bd491c9654937c8d729c"></a>

### [`004c1c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1c00.md) → [`004c1c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1c00.md) _ZN5Botan5PBKDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c1c78",
      "incomplete_value": false,
      "site": "004c1c80",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1c78",
      "incomplete_value": false,
      "site": "004c1c80",
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
            "const:565:8"
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
      "definition_site": "004c1cb8",
      "incomplete_value": true,
      "site": "004c1cc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1cb8",
      "incomplete_value": true,
      "site": "004c1cc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004c1c78",
      "PARAM",
      [
        "storage",
        "002a1565",
        null,
        "string"
      ]
    ],
    [
      "004c1cb8",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004c1cb8",
      "PARAM",
      [
        "storage",
        "00be93e8",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c1c78",
      "PARAM",
      [
        "storage",
        "002a15f0",
        null,
        "string"
      ]
    ],
    [
      "004c1cb8",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004c1cb8",
      "PARAM",
      [
        "storage",
        "00be9438",
        "_ZTIN5Botan12Lookup_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1c00.md#insn-004c1c78) · [`004c1cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1c00.md#insn-004c1cac) · [`004c1cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1c00.md#insn-004c1cb8)
- 新版 `004c1c78`（命令位置の公開資料なし） · `004c1cac`（命令位置の公開資料なし） · `004c1cb8`（命令位置の公開資料なし）

~~~diff
- 004c1c78 ["COPY", "tmp:0:8", ["const:565:8"]]
- 004c1c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c1c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c1c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c1c78 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004c1c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c1c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c1c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c1c78 bytes 21941591
+ 004c1c78 bytes 21c01791
- 004c1cac ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004c1cac ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004c1cac bytes c13a00b0
+ 004c1cac bytes c13a00d0
- 004c1cb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004c1cb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1cb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004c1cb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1cb8 bytes 21f447f9
+ 004c1cb8 bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152776570fdcf8f30ec04a72a7ce6953"></a>

### [`004c1fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1fec.md) → [`004c1fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fec.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc590.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bdc5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5e0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c20d0",
      "incomplete_value": true,
      "site": "004c20dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c20d0",
      "incomplete_value": true,
      "site": "004c20dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c20fc",
      "incomplete_value": false,
      "site": "004c2114",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c20fc",
      "incomplete_value": false,
      "site": "004c2114",
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
            "const:e84:8"
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
      "definition_site": "004c2104",
      "incomplete_value": false,
      "site": "004c2114",
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
            "const:a59:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2104",
      "incomplete_value": false,
      "site": "004c2114",
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
            "const:ae6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c20d0",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004c20d0",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004c20fc",
      "PARAM",
      [
        "storage",
        "00298e84",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c20d0",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c20d0",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004c20fc",
      "PARAM",
      [
        "storage",
        "00298df7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c20d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1fec.md#insn-004c20d0) · [`004c20fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1fec.md#insn-004c20fc) · [`004c2104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1fec.md#insn-004c2104)
- 新版 `004c20d0`（命令位置の公開資料なし） · `004c20fc`（命令位置の公開資料なし） · `004c2104`（命令位置の公開資料なし）

~~~diff
- 004c20d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004c20d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c20d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004c20d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c20d0 bytes 217847f9
+ 004c20d0 bytes 21a047f9
- 004c20fc ["COPY", "tmp:0:8", ["const:e84:8"]]
- 004c20fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c20fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c20fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c20fc ["COPY", "tmp:0:8", ["const:df7:8"]]
+ 004c20fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c20fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c20fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c20fc bytes 21103a91
+ 004c20fc bytes 21dc3791
- 004c2104 ["COPY", "tmp:0:8", ["const:ae6:8"]]
- 004c2104 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004c2104 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004c2104 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004c2104 ["COPY", "tmp:0:8", ["const:a59:8"]]
+ 004c2104 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004c2104 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004c2104 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004c2104 bytes 42982b91
+ 004c2104 bytes 42642991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa3d365d33e03fe2139a99b5eae33c3"></a>

### [`004c222c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c222c.md) → [`004c222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c222c.md) _ZN5Botan6pbkdf2ERNS_25MessageAuthenticationCodeEPhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPKhmmNS3_6chrono8du

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5e0.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00bdb020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb020.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdc630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc630.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00bdb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb070.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

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
      "definition_site": "004c26e4",
      "incomplete_value": true,
      "site": "004c26e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c26e4",
      "incomplete_value": true,
      "site": "004c26e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2744",
      "incomplete_value": false,
      "site": "004c2764",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2744",
      "incomplete_value": false,
      "site": "004c2764",
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
            "const:96f:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c274c",
      "incomplete_value": false,
      "site": "004c2764",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c274c",
      "incomplete_value": false,
      "site": "004c2764",
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
            "const:511:8"
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
      "004c26d4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c2744",
      "PARAM",
      [
        "storage",
        "0029296f",
        null,
        "string"
      ]
    ],
    [
      "004c274c",
      "PARAM",
      [
        "storage",
        "0029b511",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c26d4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c2744",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "004c274c",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c26d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c222c.md#insn-004c26d4) · [`004c2744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c222c.md#insn-004c2744) · [`004c274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c222c.md#insn-004c274c)
- 新版 `004c26d4`（命令位置の公開資料なし） · `004c2744`（命令位置の公開資料なし） · `004c274c`（命令位置の公開資料なし）

~~~diff
- 004c26d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c26d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c26d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c26d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c26d4 bytes 299543f9
+ 004c26d4 bytes 29bd43f9
- 004c2744 ["COPY", "tmp:0:8", ["const:96f:8"]]
- 004c2744 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c2744 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c2744 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c2744 ["COPY", "tmp:0:8", ["const:8e2:8"]]
+ 004c2744 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2744 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2744 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c2744 bytes 00bc2591
+ 004c2744 bytes 00882391
- 004c274c ["COPY", "tmp:0:8", ["const:511:8"]]
- 004c274c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c274c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c274c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c274c ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 004c274c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c274c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c274c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c274c bytes 21441491
+ 004c274c bytes 213c1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5da094b724767c862654a60fd21be6a"></a>

### [`004c2990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2990.md) → [`004c2990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2990.md) _ZN5Botan8PEM_Code6encodeEPKhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c29c0",
      "incomplete_value": false,
      "site": "004c29d8",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c29c0",
      "incomplete_value": false,
      "site": "004c29d8",
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
            "const:567:8"
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
      "definition_site": "004c2a18",
      "incomplete_value": false,
      "site": "004c2a24",
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
            "const:59e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2a18",
      "incomplete_value": false,
      "site": "004c2a24",
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
            "const:513:8"
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
      "004c29c0",
      "PARAM",
      [
        "storage",
        "0029c567",
        null,
        "string"
      ]
    ],
    [
      "004c2a18",
      "PARAM",
      [
        "storage",
        "002a0513",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c29c0",
      "PARAM",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004c2a18",
      "PARAM",
      [
        "storage",
        "002a059e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c29c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2990.md#insn-004c29c0) · [`004c2a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2990.md#insn-004c2a18)
- 新版 `004c29c0`（命令位置の公開資料なし） · `004c2a18`（命令位置の公開資料なし）

~~~diff
- 004c29c0 ["COPY", "tmp:0:8", ["const:567:8"]]
- 004c29c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c29c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c29c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c29c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 004c29c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c29c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c29c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c29c0 bytes 009c1591
+ 004c29c0 bytes 00c81791
- 004c2a18 ["COPY", "tmp:0:8", ["const:513:8"]]
- 004c2a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c2a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c2a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c2a18 ["COPY", "tmp:0:8", ["const:59e:8"]]
+ 004c2a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c2a18 bytes 004c1491
+ 004c2a18 bytes 00781691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8283fb71453f38b0256ac8a13901ab6f"></a>

### [`004c2d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md) → [`004c2d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md) _ZN5Botan8PEM_Code18decode_check_labelERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc600.md) · 呼出先 11件 [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md) · 呼出先 11件 [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2e40",
      "incomplete_value": false,
      "site": "004c2e48",
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
            "const:3d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e40",
      "incomplete_value": false,
      "site": "004c2e48",
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
            "const:3d3:8"
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
      "definition_site": "004c2e50",
      "incomplete_value": false,
      "site": "004c2e58",
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
            "const:b55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e50",
      "incomplete_value": false,
      "site": "004c2e58",
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
            "const:be2:8"
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
      "definition_site": "004c2eb0",
      "incomplete_value": true,
      "site": "004c2ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2eb0",
      "incomplete_value": true,
      "site": "004c2ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c2e40",
      "PARAM",
      [
        "storage",
        "0029b3d3",
        null,
        "string"
      ]
    ],
    [
      "004c2e50",
      "PARAM",
      [
        "storage",
        "00297be2",
        null,
        "string"
      ]
    ],
    [
      "004c2eb0",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c2e40",
      "PARAM",
      [
        "storage",
        "0029b3d1",
        null,
        "string"
      ]
    ],
    [
      "004c2e50",
      "PARAM",
      [
        "storage",
        "00297b55",
        null,
        "string"
      ]
    ],
    [
      "004c2eb0",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md#insn-004c2e40) · [`004c2e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md#insn-004c2e50) · [`004c2eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md#insn-004c2eb0)
- 新版 `004c2e40`（命令位置の公開資料なし） · `004c2e50`（命令位置の公開資料なし） · `004c2eb0`（命令位置の公開資料なし）

~~~diff
- 004c2e40 ["COPY", "tmp:0:8", ["const:3d3:8"]]
- 004c2e40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c2e40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c2e40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c2e40 ["COPY", "tmp:0:8", ["const:3d1:8"]]
+ 004c2e40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2e40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c2e40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c2e40 bytes 004c0f91
+ 004c2e40 bytes 00440f91
- 004c2e50 ["COPY", "tmp:0:8", ["const:be2:8"]]
- 004c2e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c2e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c2e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c2e50 ["COPY", "tmp:0:8", ["const:b55:8"]]
+ 004c2e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c2e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c2e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c2e50 bytes 21882f91
+ 004c2e50 bytes 21542d91
- 004c2eb0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004c2eb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c2eb0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004c2eb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c2eb0 bytes 218847f9
+ 004c2eb0 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3efe50846b1fd4f91ac1be069b4023cf"></a>

### [`004c2f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md) → [`004c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md) _ZN5Botan8PEM_Code6decodeERNS_10DataSourceERNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc610.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00426e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00bdc660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c3008",
      "incomplete_value": true,
      "site": "004c3008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3008",
      "incomplete_value": true,
      "site": "004c3008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:567:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c30e8",
      "incomplete_value": false,
      "site": "004c30f4",
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
            "const:59e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c30e8",
      "incomplete_value": false,
      "site": "004c30f4",
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
            "const:513:8"
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
      "definition_site": "004c30fc",
      "incomplete_value": false,
      "site": "004c3104",
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
            "const:825:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c30fc",
      "incomplete_value": false,
      "site": "004c3104",
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
            "const:8b2:8"
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
      "004c2ff4",
      "READ",
      [
        "storage",
        "0029c567",
        null,
        "string"
      ]
    ],
    [
      "004c30e8",
      "PARAM",
      [
        "storage",
        "002a0513",
        null,
        "string"
      ]
    ],
    [
      "004c30fc",
      "PARAM",
      [
        "storage",
        "002928b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c2ff4",
      "READ",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004c30e8",
      "PARAM",
      [
        "storage",
        "002a059e",
        null,
        "string"
      ]
    ],
    [
      "004c30fc",
      "PARAM",
      [
        "storage",
        "00292825",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md#insn-004c2ff0) · [`004c30e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md#insn-004c30e8) · [`004c30fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md#insn-004c30fc)
- 新版 `004c2ff0`（命令位置の公開資料なし） · `004c30e8`（命令位置の公開資料なし） · `004c30fc`（命令位置の公開資料なし）

~~~diff
- 004c2ff0 ["COPY", "tmp:0:8", ["const:567:8"]]
- 004c2ff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c2ff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c2ff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004c2ff0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 004c2ff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004c2ff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004c2ff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c2ff0 bytes 089d1591
+ 004c2ff0 bytes 08c91791
- 004c30e8 ["COPY", "tmp:0:8", ["const:513:8"]]
- 004c30e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c30e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c30e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c30e8 ["COPY", "tmp:0:8", ["const:59e:8"]]
+ 004c30e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c30e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c30e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c30e8 bytes 004c1491
+ 004c30e8 bytes 00781691
- 004c30fc ["COPY", "tmp:0:8", ["const:8b2:8"]]
- 004c30fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c30fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c30fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c30fc ["COPY", "tmp:0:8", ["const:825:8"]]
+ 004c30fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c30fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c30fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c30fc bytes 21c82291
+ 004c30fc bytes 21942091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ebb9879e83d468105e318a0e4841a57"></a>

### [`004c3890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3890.md) → [`004c3890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3890.md) _ZN5Botan8PEM_Code7matchesERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc630.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`00bdc680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc680.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c38b0",
      "incomplete_value": false,
      "site": "004c38c4",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c38b0",
      "incomplete_value": false,
      "site": "004c38c4",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c397c",
      "incomplete_value": true,
      "site": "004c397c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c397c",
      "incomplete_value": true,
      "site": "004c397c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c38b0",
      "PARAM",
      [
        "storage",
        "0029c567",
        null,
        "string"
      ]
    ],
    [
      "004c396c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c38b0",
      "PARAM",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004c396c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c38b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3890.md#insn-004c38b0) · [`004c396c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3890.md#insn-004c396c)
- 新版 `004c38b0`（命令位置の公開資料なし） · `004c396c`（命令位置の公開資料なし）

~~~diff
- 004c38b0 ["COPY", "tmp:0:8", ["const:567:8"]]
- 004c38b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c38b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c38b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c38b0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 004c38b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c38b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c38b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c38b0 bytes 009c1591
+ 004c38b0 bytes 00c81791
- 004c396c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c396c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c396c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c396c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c396c bytes 299543f9
+ 004c396c bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-112d8226fe52ae0d72358e300255ec69"></a>

### [`004c3a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a08.md) → [`004c3a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a08.md) _ZN5Botan7get_emeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3a38",
      "incomplete_value": true,
      "site": "004c3a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004c3a38",
      "incomplete_value": true,
      "site": "004c3a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c3a38",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004c3a38",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c3a38",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004c3a38",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a08.md#insn-004c3a38)
- 新版 `004c3a38`（命令位置の公開資料なし）

~~~diff
- 004c3a38 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004c3a38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c3a38 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004c3a38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c3a38 bytes 214840f9
+ 004c3a38 bytes 217040f9
~~~


<a id="compare-2c7e85a8974cae7bdfebd93a690cd403"></a>

### [`004c3a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a84.md) → [`004c3a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a84.md) _ZNK5Botan4EMSA15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3acc",
      "incomplete_value": false,
      "site": "004c3ad8",
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
            "const:a2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3acc",
      "incomplete_value": false,
      "site": "004c3ad8",
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
            "const:ab7:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3af8",
      "incomplete_value": false,
      "site": "004c3b00",
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
            "const:c43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3af8",
      "incomplete_value": false,
      "site": "004c3b00",
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
            "const:cd0:8"
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
      "definition_site": "004c3b48",
      "incomplete_value": true,
      "site": "004c3b54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c3b48",
      "incomplete_value": true,
      "site": "004c3b54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c3acc",
      "PARAM",
      [
        "storage",
        "00296ab7",
        null,
        "string"
      ]
    ],
    [
      "004c3af8",
      "PARAM",
      [
        "storage",
        "00299cd0",
        null,
        "string"
      ]
    ],
    [
      "004c3b48",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c3acc",
      "PARAM",
      [
        "storage",
        "00296a2a",
        null,
        "string"
      ]
    ],
    [
      "004c3af8",
      "PARAM",
      [
        "storage",
        "00299c43",
        null,
        "string"
      ]
    ],
    [
      "004c3b48",
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

- 旧版 [`004c3acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a84.md#insn-004c3acc) · [`004c3af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a84.md#insn-004c3af8) · [`004c3b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3a84.md#insn-004c3b48)
- 新版 `004c3acc`（命令位置の公開資料なし） · `004c3af8`（命令位置の公開資料なし） · `004c3b48`（命令位置の公開資料なし）

~~~diff
- 004c3acc ["COPY", "tmp:0:8", ["const:ab7:8"]]
- 004c3acc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004c3acc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004c3acc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004c3acc ["COPY", "tmp:0:8", ["const:a2a:8"]]
+ 004c3acc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004c3acc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004c3acc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004c3acc bytes 42dc2a91
+ 004c3acc bytes 42a82891
- 004c3af8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 004c3af8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c3af8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c3af8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c3af8 ["COPY", "tmp:0:8", ["const:c43:8"]]
+ 004c3af8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c3af8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c3af8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c3af8 bytes 21403391
+ 004c3af8 bytes 210c3191
- 004c3b48 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:190:8"]]
- 004c3b48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c3b48 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1e0:8"]]
+ 004c3b48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c3b48 bytes 21c840f9
+ 004c3b48 bytes 21f040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ace6d5e6463e3b5bf62c8e737d98dc3"></a>

### [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) → [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) _ZN5Botan8get_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc650.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c42e4",
      "incomplete_value": true,
      "site": "004c42ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004c42e4",
      "incomplete_value": true,
      "site": "004c42ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c42e4",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004c42e4",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c42e4",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004c42e4",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c42e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md#insn-004c42e4)
- 新版 `004c42e4`（命令位置の公開資料なし）

~~~diff
- 004c42e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004c42e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c42e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004c42e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c42e4 bytes 214840f9
+ 004c42e4 bytes 217040f9
~~~


<a id="compare-c36cbe2ae9b10fd1919a42dc6e0fd6b6"></a>

### [`004c476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c476c.md) → [`004c476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md) _ZN5Botan16get_sig_paddingsENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf30.md) · 呼出先 5件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00522664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522664.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdbf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf80.md) · 呼出先 5件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c47a4",
      "incomplete_value": true,
      "site": "004c47a4",
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
      "definition_site": "004c47a4",
      "incomplete_value": true,
      "site": "004c47a4",
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
      "definition_site": "004c4870",
      "incomplete_value": false,
      "site": "004c487c",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4870",
      "incomplete_value": false,
      "site": "004c487c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c47a0",
      "READ",
      [
        "storage",
        "00c25370",
        null,
        "undefined8"
      ]
    ],
    [
      "004c4870",
      "PARAM",
      [
        "storage",
        "00c25368",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c47a0",
      "READ",
      [
        "storage",
        "00c253b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004c4870",
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c47a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c476c.md#insn-004c47a0) · [`004c4870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c476c.md#insn-004c4870)
- 新版 `004c47a0`（命令位置の公開資料なし） · `004c4870`（命令位置の公開資料なし）

~~~diff
- 004c47a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:370:8"]]
- 004c47a0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c47a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3b0:8"]]
+ 004c47a0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c47a0 bytes 39b941f9
+ 004c47a0 bytes 39d941f9
- 004c4870 ["COPY", "tmp:0:8", ["const:368:8"]]
- 004c4870 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c4870 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c4870 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c4870 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 004c4870 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c4870 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c4870 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c4870 bytes 00a00d91
+ 004c4870 bytes 00a00e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c37061c06f45eee907f1020411789be6"></a>

### [`004c4900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4900.md) → [`004c4900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4900.md) _ZN5Botan7BlinderC2ERKNS_6BigIntERNS_21RandomNumberGeneratorENSt6__ndk18functionIFS1_S3_EEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0f0.md) · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc440.md) [`00bdc4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4b0.md)
- 新版 呼出元 1件 [`00bdd140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd140.md) · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc490.md) [`00bdc500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc500.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4af8",
      "incomplete_value": true,
      "site": "004c4af8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4af8",
      "incomplete_value": true,
      "site": "004c4af8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4b7c",
      "incomplete_value": true,
      "site": "004c4b7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4b7c",
      "incomplete_value": true,
      "site": "004c4b7c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4ba8",
      "incomplete_value": true,
      "site": "004c4ba8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4ba8",
      "incomplete_value": true,
      "site": "004c4ba8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c4ae8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b6c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b98",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4ae8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b6c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b98",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4900.md#insn-004c4ae8) · [`004c4b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4900.md#insn-004c4b6c) · [`004c4b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4900.md#insn-004c4b98)
- 新版 `004c4ae8`（命令位置の公開資料なし） · `004c4b6c`（命令位置の公開資料なし） · `004c4b98`（命令位置の公開資料なし）

~~~diff
- 004c4ae8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004c4ae8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4ae8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004c4ae8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4ae8 bytes 499743f9
+ 004c4ae8 bytes 49bf43f9
- 004c4b6c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004c4b6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b6c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004c4b6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4b6c bytes 499743f9
+ 004c4b6c bytes 49bf43f9
- 004c4b98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004c4b98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004c4b98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4b98 bytes 499743f9
+ 004c4b98 bytes 49bf43f9
~~~


<a id="compare-b1dee113223aa15d5aaaa55259baff42"></a>

### [`004c4ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4ce8.md) → [`004c4ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4ce8.md) _ZNK5Botan7Blinder5blindERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6b0.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc700.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4dd0",
      "incomplete_value": true,
      "site": "004c4dd0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4dd0",
      "incomplete_value": true,
      "site": "004c4dd0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4e58",
      "incomplete_value": true,
      "site": "004c4e58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4e58",
      "incomplete_value": true,
      "site": "004c4e58",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c4e88",
      "incomplete_value": true,
      "site": "004c4e88",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4e88",
      "incomplete_value": true,
      "site": "004c4e88",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c4dc0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e48",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e78",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4dc0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e48",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e78",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4ce8.md#insn-004c4dc0) · [`004c4e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4ce8.md#insn-004c4e48) · [`004c4e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4ce8.md#insn-004c4e78)
- 新版 `004c4dc0`（命令位置の公開資料なし） · `004c4e48`（命令位置の公開資料なし） · `004c4e78`（命令位置の公開資料なし）

~~~diff
- 004c4dc0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004c4dc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4dc0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004c4dc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4dc0 bytes 299743f9
+ 004c4dc0 bytes 29bf43f9
- 004c4e48 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004c4e48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4e48 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004c4e48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4e48 bytes 299743f9
+ 004c4e48 bytes 29bf43f9
- 004c4e78 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004c4e78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4e78 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004c4e78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4e78 bytes 299743f9
+ 004c4e78 bytes 29bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7350cc1e3708b9d2ff57b70cc7ad1845"></a>

### [`004c5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5180.md) → [`004c5180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5180.md) _ZNK5Botan7Blinder7unblindERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6c0.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc710.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "definition_site": "004c51f8",
      "incomplete_value": true,
      "site": "004c51f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c51f8",
      "incomplete_value": true,
      "site": "004c51f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c5238",
      "incomplete_value": false,
      "site": "004c5240",
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
            "const:4cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5238",
      "incomplete_value": false,
      "site": "004c5240",
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
            "const:442:8"
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
      "definition_site": "004c5270",
      "incomplete_value": true,
      "site": "004c527c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5270",
      "incomplete_value": true,
      "site": "004c527c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c51e8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c5238",
      "PARAM",
      [
        "storage",
        "0029e442",
        null,
        "string"
      ]
    ],
    [
      "004c5270",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c51e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c5238",
      "PARAM",
      [
        "storage",
        "0029e4cd",
        null,
        "string"
      ]
    ],
    [
      "004c5270",
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

- 旧版 [`004c51e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5180.md#insn-004c51e8) · [`004c5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5180.md#insn-004c5238) · [`004c5270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5180.md#insn-004c5270)
- 新版 `004c51e8`（命令位置の公開資料なし） · `004c5238`（命令位置の公開資料なし） · `004c5270`（命令位置の公開資料なし）

~~~diff
- 004c51e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c51e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c51e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c51e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c51e8 bytes 299543f9
+ 004c51e8 bytes 29bd43f9
- 004c5238 ["COPY", "tmp:0:8", ["const:442:8"]]
- 004c5238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c5238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c5238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c5238 ["COPY", "tmp:0:8", ["const:4cd:8"]]
+ 004c5238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c5238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c5238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c5238 bytes 21081191
+ 004c5238 bytes 21341391
- 004c5270 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 004c5270 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5270 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 004c5270 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5270 bytes 21a447f9
+ 004c5270 bytes 21cc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7a298c08a4dcc3f5b018919cc1687db"></a>

### [`004c52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md) → [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) _ZN5Botan15load_public_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS3_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6d0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5320",
      "incomplete_value": false,
      "site": "004c5328",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5320",
      "incomplete_value": false,
      "site": "004c5328",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c54b8",
      "incomplete_value": false,
      "site": "004c54c4",
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
            "const:a9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c54b8",
      "incomplete_value": false,
      "site": "004c54c4",
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
            "const:b31:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c54f4",
      "incomplete_value": true,
      "site": "004c5500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c54f4",
      "incomplete_value": true,
      "site": "004c5500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c5328",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004c536c",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004c536c",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c5328",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004c536c",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004c536c",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md#insn-004c5320) · [`004c54b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md#insn-004c54b8) · [`004c54f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md#insn-004c54f4)
- 新版 `004c5320`（命令位置の公開資料なし） · `004c54b8`（命令位置の公開資料なし） · `004c54f4`（命令位置の公開資料なし）

~~~diff
- 004c5320 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004c5320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c5320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c5320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004c5320 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004c5320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004c5320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004c5320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c5320 bytes 08811a91
+ 004c5320 bytes 08c11b91
- 004c54b8 ["COPY", "tmp:0:8", ["const:b31:8"]]
- 004c54b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c54b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c54b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c54b8 ["COPY", "tmp:0:8", ["const:a9d:8"]]
+ 004c54b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c54b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c54b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c54b8 bytes 00c42c91
+ 004c54b8 bytes 00742a91
- 004c54f4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004c54f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c54f4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004c54f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c54f4 bytes 218847f9
+ 004c54f4 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e617d8e488ee91679c30bb2dc4f66843"></a>

### [`004c56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md) → [`004c56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6e0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md)
- 新版 呼出元 1件 [`00bdc730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.86% / 新版 91.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c56e0",
      "incomplete_value": true,
      "site": "004c56e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c56e0",
      "incomplete_value": true,
      "site": "004c56e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c5790",
      "incomplete_value": true,
      "site": "004c5790",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5790",
      "incomplete_value": true,
      "site": "004c5790",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c57d4",
      "incomplete_value": true,
      "site": "004c57d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c57d4",
      "incomplete_value": true,
      "site": "004c57d4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c56d0",
      "READ",
      [
        "storage",
        "00c1b198",
        null,
        "pointer"
      ]
    ],
    [
      "004c56e8",
      "DATA",
      [
        "storage",
        "00bea098",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004c5780",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c56d0",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c56e8",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004c5780",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c56d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md#insn-004c56d0) · [`004c5780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md#insn-004c5780) · [`004c57c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md#insn-004c57c4)
- 新版 `004c56d0`（命令位置の公開資料なし） · `004c5780`（命令位置の公開資料なし） · `004c57c4`（命令位置の公開資料なし）

~~~diff
- 004c56d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 004c56d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c56d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 004c56d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c56d0 bytes 08cd40f9
+ 004c56d0 bytes 08f540f9
- 004c5780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004c5780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004c5780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5780 bytes 899643f9
+ 004c5780 bytes 89be43f9
- 004c57c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004c57c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c57c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004c57c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c57c4 bytes 899643f9
+ 004c57c4 bytes 89be43f9
~~~


<a id="compare-312c54ca3357c9fba1bb5dba664ce482"></a>

### [`004c585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md) → [`004c585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md) _ZN5Botan16load_private_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md) · 呼出先 12件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc740.md) · 呼出先 12件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c5950",
      "incomplete_value": false,
      "site": "004c595c",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5950",
      "incomplete_value": false,
      "site": "004c595c",
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
            "const:51d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c59a4",
      "incomplete_value": true,
      "site": "004c59b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c59a4",
      "incomplete_value": true,
      "site": "004c59b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c59c8",
      "incomplete_value": false,
      "site": "004c59d4",
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
            "const:a9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c59c8",
      "incomplete_value": false,
      "site": "004c59d4",
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
            "const:b31:8"
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
      "004c5950",
      "PARAM",
      [
        "storage",
        "002a051d",
        null,
        "string"
      ]
    ],
    [
      "004c59a4",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c59a4",
      "PARAM",
      [
        "storage",
        "00be92b0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c5950",
      "PARAM",
      [
        "storage",
        "002a05a8",
        null,
        "string"
      ]
    ],
    [
      "004c59a4",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "004c59a4",
      "PARAM",
      [
        "storage",
        "00be9300",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md#insn-004c5950) · [`004c59a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md#insn-004c59a4) · [`004c59c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md#insn-004c59c8)
- 新版 `004c5950`（命令位置の公開資料なし） · `004c59a4`（命令位置の公開資料なし） · `004c59c8`（命令位置の公開資料なし）

~~~diff
- 004c5950 ["COPY", "tmp:0:8", ["const:51d:8"]]
- 004c5950 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004c5950 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004c5950 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004c5950 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 004c5950 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004c5950 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004c5950 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004c5950 bytes 42741491
+ 004c5950 bytes 42a01691
- 004c59a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 004c59a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c59a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 004c59a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c59a4 bytes 218847f9
+ 004c59a4 bytes 21b047f9
- 004c59c8 ["COPY", "tmp:0:8", ["const:b31:8"]]
- 004c59c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c59c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c59c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c59c8 ["COPY", "tmp:0:8", ["const:a9d:8"]]
+ 004c59c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c59c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c59c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c59c8 bytes 00c42c91
+ 004c59c8 bytes 00742a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fdc399dfcbe31eb2fd798a047a9841b"></a>

### [`004c5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5ac8.md) → [`004c5ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc700.md) · 呼出先 14件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdc750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc750.md) · 呼出先 14件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.71% / 新版 91.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5b38",
      "incomplete_value": true,
      "site": "004c5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c5b38",
      "incomplete_value": true,
      "site": "004c5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c5b14",
      "incomplete_value": true,
      "site": "004c5b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c5b14",
      "incomplete_value": true,
      "site": "004c5b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5bcc",
      "incomplete_value": true,
      "site": "004c5be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:529:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5bcc",
      "incomplete_value": true,
      "site": "004c5be8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5af4",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "004c5b38",
      "DATA",
      [
        "storage",
        "00bea2a8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004c5b54",
      "DATA",
      [
        "storage",
        "00bea188",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004c5af4",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004c5b38",
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004c5b54",
      "DATA",
      [
        "storage",
        "00bea1d8",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5ac8.md#insn-004c5af4) · [`004c5b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5ac8.md#insn-004c5b10)
- 新版 `004c5af4`（命令位置の公開資料なし） · `004c5b10`（命令位置の公開資料なし）

~~~diff
- 004c5af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
- 004c5af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
+ 004c5af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5af4 bytes 08d140f9
+ 004c5af4 bytes 08f940f9
- 004c5b10 ["COPY", "register:40d8:8", ["register:4000:8"]]
- 004c5b10 bytes fb0300aa
+ 004c5b10 ["COPY", "register:40d8:8", ["register:4000:8"]]
+ 004c5b10 bytes fb0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bac9e5ce52348a9059155dfea0f551f"></a>

### [`004c5f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5f28.md) → [`004c5f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md) _ZN5Botan14RSA_PrivateKeyC1ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc710.md) · 呼出先 17件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdc760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc760.md) · 呼出先 17件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 2件

アドレスに依存する影響 `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5f78",
      "incomplete_value": true,
      "site": "004c5f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c5f78",
      "incomplete_value": true,
      "site": "004c5f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5f98",
      "incomplete_value": true,
      "site": "004c5f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c5f98",
      "incomplete_value": true,
      "site": "004c5f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c6098",
      "incomplete_value": true,
      "site": "004c6098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6098",
      "incomplete_value": true,
      "site": "004c6098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c5f64",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "004c5f80",
      "DATA",
      [
        "storage",
        "00bea188",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004c5f98",
      "DATA",
      [
        "storage",
        "00bea2a8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004c5f64",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004c5f80",
      "DATA",
      [
        "storage",
        "00bea1d8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004c5f98",
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5f28.md#insn-004c5f64) · [`004c6088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5f28.md#insn-004c6088) · [`004c6128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5f28.md#insn-004c6128)
- 新版 `004c5f64`（命令位置の公開資料なし） · `004c6088`（命令位置の公開資料なし） · `004c6128`（命令位置の公開資料なし）

~~~diff
- 004c5f64 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1a0:8"]]
- 004c5f64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5f64 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1f0:8"]]
+ 004c5f64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5f64 bytes 29d140f9
+ 004c5f64 bytes 29f940f9
- 004c6088 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c6088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6088 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c6088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c6088 bytes 299543f9
+ 004c6088 bytes 29bd43f9
- 004c6128 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c6128 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6128 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c6128 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c6128 bytes 299543f9
+ 004c6128 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90aee0d0ce730627a1a64bf19366a39"></a>

### [`004c734c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c734c.md) → [`004c734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c734c.md) FUN_004c734c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "definition_site": "004c7368",
      "incomplete_value": true,
      "site": "004c7368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7368",
      "incomplete_value": true,
      "site": "004c7368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c739c",
      "incomplete_value": true,
      "site": "004c73a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c739c",
      "incomplete_value": true,
      "site": "004c73a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c7360",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7368",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c7398",
      "READ",
      [
        "storage",
        "00c1b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c7360",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7368",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c7398",
      "READ",
      [
        "storage",
        "00c1b200",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c734c.md#insn-004c7360) · [`004c7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c734c.md#insn-004c7398)
- 新版 `004c7360`（命令位置の公開資料なし） · `004c7398`（命令位置の公開資料なし）

~~~diff
- 004c7360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7360 bytes 08c947f9
+ 004c7360 bytes 08f147f9
- 004c7398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c7398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c7398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7398 bytes 08d940f9
+ 004c7398 bytes 080141f9
~~~


<a id="compare-9e4e10c568a8080f6a5d801ee0b4ef8a"></a>

### [`004c73c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c73c4.md) → [`004c73c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md) _ZNK5Botan11Private_Key16private_key_infoEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc740.md) · 呼出先 11件 [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00bdc790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc790.md) · 呼出先 11件 [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c7450",
      "incomplete_value": true,
      "site": "004c7450",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7450",
      "incomplete_value": true,
      "site": "004c7450",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c74e4",
      "incomplete_value": true,
      "site": "004c74e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c74e4",
      "incomplete_value": true,
      "site": "004c74e4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c7570",
      "incomplete_value": true,
      "site": "004c7570",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7570",
      "incomplete_value": true,
      "site": "004c7570",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c7440",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c74d4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c7560",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c7440",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c74d4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c7560",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c73c4.md#insn-004c7440) · [`004c74d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c73c4.md#insn-004c74d4) · [`004c7560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c73c4.md#insn-004c7560)
- 新版 `004c7440`（命令位置の公開資料なし） · `004c74d4`（命令位置の公開資料なし） · `004c7560`（命令位置の公開資料なし）

~~~diff
- 004c7440 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004c7440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7440 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004c7440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7440 bytes e99643f9
+ 004c7440 bytes e9be43f9
- 004c74d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004c74d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c74d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004c74d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c74d4 bytes e99643f9
+ 004c74d4 bytes e9be43f9
- 004c7560 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004c7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7560 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004c7560 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7560 bytes e99643f9
+ 004c7560 bytes e9be43f9
~~~


<a id="compare-1bba21d21327bc95269f144ad5aa5eb4"></a>

### [`004c7790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7790.md) → [`004c7790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7790.md) _ZNK5Botan10Public_Key20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

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
      "definition_site": "004c7818",
      "incomplete_value": true,
      "site": "004c7818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7818",
      "incomplete_value": true,
      "site": "004c7818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7850",
      "incomplete_value": true,
      "site": "004c7854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7850",
      "incomplete_value": true,
      "site": "004c7854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7874",
      "incomplete_value": true,
      "site": "004c787c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7874",
      "incomplete_value": true,
      "site": "004c787c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004c7804",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7818",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c784c",
      "READ",
      [
        "storage",
        "00c1b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c7804",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7818",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c784c",
      "READ",
      [
        "storage",
        "00c1b200",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7790.md#insn-004c7804) · [`004c784c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7790.md#insn-004c784c) · [`004c7868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7790.md#insn-004c7868)
- 新版 `004c7804`（命令位置の公開資料なし） · `004c784c`（命令位置の公開資料なし） · `004c7868`（命令位置の公開資料なし）

~~~diff
- 004c7804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7804 bytes 08c947f9
+ 004c7804 bytes 08f147f9
- 004c784c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c784c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c784c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c784c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c784c bytes 08d940f9
+ 004c784c bytes 080141f9
- 004c7868 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004c7868 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004c7868 bytes 813a00f0
+ 004c7868 bytes a13a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a57a5d5a2bbb3b87f97185d59fbadd"></a>

### [`004c7914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7914.md) → [`004c7914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7914.md) _ZNK5Botan10Public_Key24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

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
      "definition_site": "004c799c",
      "incomplete_value": true,
      "site": "004c799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c799c",
      "incomplete_value": true,
      "site": "004c799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c79d4",
      "incomplete_value": true,
      "site": "004c79d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c79d4",
      "incomplete_value": true,
      "site": "004c79d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7960",
      "incomplete_value": false,
      "site": "004c7968",
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
            "const:3e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7960",
      "incomplete_value": false,
      "site": "004c7968",
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
      "004c7960",
      "PARAM",
      [
        "storage",
        "002a3357",
        null,
        "string"
      ]
    ],
    [
      "004c7988",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c799c",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004c7960",
      "PARAM",
      [
        "storage",
        "002a33e2",
        null,
        "string"
      ]
    ],
    [
      "004c7988",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c799c",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7914.md#insn-004c7960) · [`004c7988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7914.md#insn-004c7988) · [`004c79d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7914.md#insn-004c79d0)
- 新版 `004c7960`（命令位置の公開資料なし） · `004c7988`（命令位置の公開資料なし） · `004c79d0`（命令位置の公開資料なし）

~~~diff
- 004c7960 ["COPY", "tmp:0:8", ["const:357:8"]]
- 004c7960 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c7960 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c7960 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c7960 ["COPY", "tmp:0:8", ["const:3e2:8"]]
+ 004c7960 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7960 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7960 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c7960 bytes 215c0d91
+ 004c7960 bytes 21880f91
- 004c7988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7988 bytes 08c947f9
+ 004c7988 bytes 08f147f9
- 004c79d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c79d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c79d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c79d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c79d0 bytes 08d940f9
+ 004c79d0 bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3291b35c59679ff10ee4d4e2ed838fb2"></a>

### [`004c7a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7a98.md) → [`004c7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7a98.md) _ZNK5Botan10Public_Key22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

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
      "definition_site": "004c7b20",
      "incomplete_value": true,
      "site": "004c7b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7b20",
      "incomplete_value": true,
      "site": "004c7b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7b58",
      "incomplete_value": true,
      "site": "004c7b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7b58",
      "incomplete_value": true,
      "site": "004c7b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7ae4",
      "incomplete_value": false,
      "site": "004c7aec",
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
            "const:a34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7ae4",
      "incomplete_value": false,
      "site": "004c7aec",
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
            "const:ac1:8"
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
      "004c7ae4",
      "PARAM",
      [
        "storage",
        "00296ac1",
        null,
        "string"
      ]
    ],
    [
      "004c7b0c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7b20",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004c7ae4",
      "PARAM",
      [
        "storage",
        "00296a34",
        null,
        "string"
      ]
    ],
    [
      "004c7b0c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7b20",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7a98.md#insn-004c7ae4) · [`004c7b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7a98.md#insn-004c7b0c) · [`004c7b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7a98.md#insn-004c7b54)
- 新版 `004c7ae4`（命令位置の公開資料なし） · `004c7b0c`（命令位置の公開資料なし） · `004c7b54`（命令位置の公開資料なし）

~~~diff
- 004c7ae4 ["COPY", "tmp:0:8", ["const:ac1:8"]]
- 004c7ae4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c7ae4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c7ae4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c7ae4 ["COPY", "tmp:0:8", ["const:a34:8"]]
+ 004c7ae4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7ae4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7ae4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c7ae4 bytes 21042b91
+ 004c7ae4 bytes 21d02891
- 004c7b0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7b0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7b0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7b0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7b0c bytes 08c947f9
+ 004c7b0c bytes 08f147f9
- 004c7b54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c7b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7b54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c7b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7b54 bytes 08d940f9
+ 004c7b54 bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac77abec5362980bd706d0bda68d5a1"></a>

### [`004c7c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7c1c.md) → [`004c7c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7c1c.md) _ZNK5Botan11Private_Key20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004c7cac",
      "incomplete_value": true,
      "site": "004c7cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7cac",
      "incomplete_value": true,
      "site": "004c7cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7ce4",
      "incomplete_value": true,
      "site": "004c7ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7ce4",
      "incomplete_value": true,
      "site": "004c7ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7c70",
      "incomplete_value": false,
      "site": "004c7c78",
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
            "const:403:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7c70",
      "incomplete_value": false,
      "site": "004c7c78",
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
      "004c7c70",
      "PARAM",
      [
        "storage",
        "002a3378",
        null,
        "string"
      ]
    ],
    [
      "004c7c98",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7cac",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004c7c70",
      "PARAM",
      [
        "storage",
        "002a3403",
        null,
        "string"
      ]
    ],
    [
      "004c7c98",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7cac",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7c1c.md#insn-004c7c70) · [`004c7c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7c1c.md#insn-004c7c98) · [`004c7ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7c1c.md#insn-004c7ce0)
- 新版 `004c7c70`（命令位置の公開資料なし） · `004c7c98`（命令位置の公開資料なし） · `004c7ce0`（命令位置の公開資料なし）

~~~diff
- 004c7c70 ["COPY", "tmp:0:8", ["const:378:8"]]
- 004c7c70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c7c70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c7c70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c7c70 ["COPY", "tmp:0:8", ["const:403:8"]]
+ 004c7c70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7c70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7c70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c7c70 bytes 21e00d91
+ 004c7c70 bytes 210c1091
- 004c7c98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7c98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7c98 bytes 08c947f9
+ 004c7c98 bytes 08f147f9
- 004c7ce0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c7ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7ce0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c7ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7ce0 bytes 08d940f9
+ 004c7ce0 bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f3dd7d8600fe34ce006af21bbecd11"></a>

### [`004c7da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7da8.md) → [`004c7da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7da8.md) _ZNK5Botan11Private_Key24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocato

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004c7e38",
      "incomplete_value": true,
      "site": "004c7e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7e38",
      "incomplete_value": true,
      "site": "004c7e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7e70",
      "incomplete_value": true,
      "site": "004c7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7e70",
      "incomplete_value": true,
      "site": "004c7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7dfc",
      "incomplete_value": false,
      "site": "004c7e04",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7dfc",
      "incomplete_value": false,
      "site": "004c7e04",
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
      "004c7dfc",
      "PARAM",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "004c7e24",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e38",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004c7dfc",
      "PARAM",
      [
        "storage",
        "002a95b0",
        null,
        "string"
      ]
    ],
    [
      "004c7e24",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e38",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7da8.md#insn-004c7dfc) · [`004c7e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7da8.md#insn-004c7e24) · [`004c7e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7da8.md#insn-004c7e6c)
- 新版 `004c7dfc`（命令位置の公開資料なし） · `004c7e24`（命令位置の公開資料なし） · `004c7e6c`（命令位置の公開資料なし）

~~~diff
- 004c7dfc ["COPY", "tmp:0:8", ["const:516:8"]]
- 004c7dfc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c7dfc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c7dfc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c7dfc ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 004c7dfc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7dfc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7dfc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c7dfc bytes 21581491
+ 004c7dfc bytes 21c01691
- 004c7e24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7e24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7e24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7e24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7e24 bytes 08c947f9
+ 004c7e24 bytes 08f147f9
- 004c7e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c7e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c7e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7e6c bytes 08d940f9
+ 004c7e6c bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4007d1c8632d32019e914a2f7537f168"></a>

### [`004c7f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7f34.md) → [`004c7f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md) _ZNK5Botan11Private_Key19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004c7fc4",
      "incomplete_value": true,
      "site": "004c7fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7fc4",
      "incomplete_value": true,
      "site": "004c7fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7ffc",
      "incomplete_value": true,
      "site": "004c8000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c7ffc",
      "incomplete_value": true,
      "site": "004c8000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7f88",
      "incomplete_value": false,
      "site": "004c7f90",
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
            "const:659:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7f88",
      "incomplete_value": false,
      "site": "004c7f90",
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
            "const:5bf:8"
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
      "004c7f88",
      "PARAM",
      [
        "storage",
        "002a75bf",
        null,
        "string"
      ]
    ],
    [
      "004c7fb0",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fc4",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004c7f88",
      "PARAM",
      [
        "storage",
        "002a7659",
        null,
        "string"
      ]
    ],
    [
      "004c7fb0",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fc4",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7f34.md#insn-004c7f88) · [`004c7fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7f34.md#insn-004c7fb0) · [`004c7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c7f34.md#insn-004c7ff8)
- 新版 `004c7f88`（命令位置の公開資料なし） · `004c7fb0`（命令位置の公開資料なし） · `004c7ff8`（命令位置の公開資料なし）

~~~diff
- 004c7f88 ["COPY", "tmp:0:8", ["const:5bf:8"]]
- 004c7f88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c7f88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c7f88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c7f88 ["COPY", "tmp:0:8", ["const:659:8"]]
+ 004c7f88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7f88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c7f88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c7f88 bytes 21fc1691
+ 004c7f88 bytes 21641991
- 004c7fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c7fb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c7fb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7fb0 bytes 08c947f9
+ 004c7fb0 bytes 08f147f9
- 004c7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7ff8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c7ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7ff8 bytes 08d940f9
+ 004c7ff8 bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1dad693a59094cdbaad5755d6180e87"></a>

### [`004c80c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c80c0.md) → [`004c80c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c80c0.md) _ZNK5Botan11Private_Key23create_key_agreement_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

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
      "definition_site": "004c8150",
      "incomplete_value": true,
      "site": "004c8150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c8150",
      "incomplete_value": true,
      "site": "004c8150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c8188",
      "incomplete_value": true,
      "site": "004c818c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c8188",
      "incomplete_value": true,
      "site": "004c818c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c81ac",
      "incomplete_value": true,
      "site": "004c81b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c81ac",
      "incomplete_value": true,
      "site": "004c81b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
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
      "004c813c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c8150",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c8184",
      "READ",
      [
        "storage",
        "00c1b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c813c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c8150",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004c8184",
      "READ",
      [
        "storage",
        "00c1b200",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c813c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c80c0.md#insn-004c813c) · [`004c8184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c80c0.md#insn-004c8184) · [`004c81a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c80c0.md#insn-004c81a0)
- 新版 `004c813c`（命令位置の公開資料なし） · `004c8184`（命令位置の公開資料なし） · `004c81a0`（命令位置の公開資料なし）

~~~diff
- 004c813c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 004c813c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c813c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004c813c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c813c bytes 08c947f9
+ 004c813c bytes 08f147f9
- 004c8184 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 004c8184 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8184 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 004c8184 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8184 bytes 08d940f9
+ 004c8184 bytes 080141f9
- 004c81a0 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004c81a0 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004c81a0 bytes 813a00d0
+ 004c81a0 bytes 813a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42828f72af81173e2e2ad99f5e1c812e"></a>

### [`004c824c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c824c.md) → [`004c824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md) FUN_004c824c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d29f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d29f8.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md) [`00bdc650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc650.md)
- 新版 呼出元 1件 [`004d29f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8260",
      "incomplete_value": false,
      "site": "004c8268",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8260",
      "incomplete_value": false,
      "site": "004c8268",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c82c4",
      "incomplete_value": true,
      "site": "004c82cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004c82c4",
      "incomplete_value": true,
      "site": "004c82cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c8268",
      "DATA",
      [
        "storage",
        "00be9e58",
        null,
        "undefined *"
      ]
    ],
    [
      "004c82c4",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004c82c4",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c8268",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "004c82c4",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004c82c4",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c824c.md#insn-004c8260) · [`004c82c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c824c.md#insn-004c82c4)
- 新版 `004c8260`（命令位置の公開資料なし） · `004c82c4`（命令位置の公開資料なし）

~~~diff
- 004c8260 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 004c8260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c8260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c8260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004c8260 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 004c8260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004c8260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004c8260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c8260 bytes 08613991
+ 004c8260 bytes 08a13a91
- 004c82c4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004c82c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c82c4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004c82c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c82c4 bytes 214840f9
+ 004c82c4 bytes 217040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ed117872defb763c55885f3a972ad4"></a>

### [`004c8434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8434.md) → [`004c8434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8434.md) FUN_004c8434

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c84f0",
      "incomplete_value": true,
      "site": "004c84f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c84f0",
      "incomplete_value": true,
      "site": "004c84f0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c851c",
      "incomplete_value": true,
      "site": "004c851c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c851c",
      "incomplete_value": true,
      "site": "004c851c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c84e0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c850c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c84e0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c850c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c84e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8434.md#insn-004c84e0) · [`004c850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8434.md#insn-004c850c)
- 新版 `004c84e0`（命令位置の公開資料なし） · `004c850c`（命令位置の公開資料なし）

~~~diff
- 004c84e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004c84e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c84e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004c84e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c84e0 bytes 899643f9
+ 004c84e0 bytes 89be43f9
- 004c850c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 004c850c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c850c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 004c850c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c850c bytes 899643f9
+ 004c850c bytes 89be43f9
~~~


<a id="compare-f56c4e487111173e0ea651b7fb5408eb"></a>

### [`004c8590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8590.md) → [`004c8590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md) FUN_004c8590

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d2528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2528.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdc100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc100.md) [`00bdc650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc650.md)
- 新版 呼出元 1件 [`004d2528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c85a4",
      "incomplete_value": false,
      "site": "004c85ac",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c85a4",
      "incomplete_value": false,
      "site": "004c85ac",
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
            "const:ea8:8"
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
      "definition_site": "004c8608",
      "incomplete_value": true,
      "site": "004c8610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004c8608",
      "incomplete_value": true,
      "site": "004c8610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c85ac",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "004c8608",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ],
    [
      "004c8608",
      "PARAM",
      [
        "storage",
        "00be9a08",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c85ac",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "004c8608",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004c8608",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c85a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8590.md#insn-004c85a4) · [`004c8608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8590.md#insn-004c8608)
- 新版 `004c85a4`（命令位置の公開資料なし） · `004c8608`（命令位置の公開資料なし）

~~~diff
- 004c85a4 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 004c85a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004c85a4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 004c85a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004c85a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004c85a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 bytes 08a13a91
+ 004c85a4 bytes 08e13b91
- 004c8608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:90:8"]]
- 004c8608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004c8608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8608 bytes 214840f9
+ 004c8608 bytes 217040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ddf515aa3e0a16504c88f7f284ad46"></a>

### [`004c898c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c898c.md) → [`004c898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md) FUN_004c898c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8a74",
      "incomplete_value": true,
      "site": "004c8a74",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8a74",
      "incomplete_value": true,
      "site": "004c8a74",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8ab8",
      "incomplete_value": true,
      "site": "004c8ab8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8ab8",
      "incomplete_value": true,
      "site": "004c8ab8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c8a64",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c8aa8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8a64",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c8aa8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c898c.md#insn-004c8a64) · [`004c8aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c898c.md#insn-004c8aa8)
- 新版 `004c8a64`（命令位置の公開資料なし） · `004c8aa8`（命令位置の公開資料なし）

~~~diff
- 004c8a64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c8a64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8a64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c8a64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8a64 bytes a99643f9
+ 004c8a64 bytes a9be43f9
- 004c8aa8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c8aa8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8aa8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c8aa8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8aa8 bytes a99643f9
+ 004c8aa8 bytes a9be43f9
~~~


<a id="compare-8ca0c2373c9fa5327258f3c6a789e786"></a>

### [`004c8c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8c88.md) → [`004c8c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8c88.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc750.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) [`00bdc740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc740.md)
- 新版 呼出元 1件 [`00bdc7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7a0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc790.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8ce0",
      "incomplete_value": true,
      "site": "004c8ce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8ce0",
      "incomplete_value": true,
      "site": "004c8ce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae7:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004c8d28",
      "incomplete_value": true,
      "site": "004c8d28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8d28",
      "incomplete_value": true,
      "site": "004c8d28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c8ccc",
      "READ",
      [
        "storage",
        "00291ae7",
        null,
        "string"
      ]
    ],
    [
      "004c8d18",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8ccc",
      "READ",
      [
        "storage",
        "00291a5a",
        null,
        "string"
      ]
    ],
    [
      "004c8d18",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8c88.md#insn-004c8cbc) · [`004c8d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8c88.md#insn-004c8d18)
- 新版 `004c8cbc`（命令位置の公開資料なし） · `004c8d18`（命令位置の公開資料なし）

~~~diff
- 004c8cbc ["COPY", "tmp:0:8", ["const:ae7:8"]]
- 004c8cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c8cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c8cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c8cbc ["COPY", "tmp:0:8", ["const:a5a:8"]]
+ 004c8cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c8cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c8cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c8cbc bytes 299d2b91
+ 004c8cbc bytes 29692991
- 004c8d18 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004c8d18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8d18 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004c8d18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8d18 bytes 299543f9
+ 004c8d18 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-033691bd7dfd68154d0c613eeaea8366"></a>

### [`004c8d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8d94.md) → [`004c8d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md) _ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc760.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md)
- 新版 呼出元 1件 [`00bdc7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7b0.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.90% / 新版 96.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8e90",
      "incomplete_value": false,
      "site": "004c8e90",
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
            "const:b7d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8e90",
      "incomplete_value": false,
      "site": "004c8e90",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9070",
      "incomplete_value": false,
      "site": "004c9070",
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
            "const:31f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9070",
      "incomplete_value": false,
      "site": "004c9070",
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
            "const:321:8"
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
      "definition_site": "004c90ec",
      "incomplete_value": true,
      "site": "004c90ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c90ec",
      "incomplete_value": true,
      "site": "004c90ec",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c8e90",
      "DATA",
      [
        "storage",
        "00299c0a",
        null,
        "string"
      ]
    ],
    [
      "004c9070",
      "DATA",
      [
        "storage",
        "0029b321",
        null,
        "string"
      ]
    ],
    [
      "004c90dc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8e90",
      "DATA",
      [
        "storage",
        "00299b7d",
        null,
        "string"
      ]
    ],
    [
      "004c9070",
      "DATA",
      [
        "storage",
        "0029b31f",
        null,
        "string"
      ]
    ],
    [
      "004c90dc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8d94.md#insn-004c8e8c) · [`004c9064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8d94.md#insn-004c9064) · [`004c9068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8d94.md#insn-004c9068)
- 新版 `004c8e8c`（命令位置の公開資料なし） · `004c9064`（命令位置の公開資料なし）

~~~diff
- 004c8e8c ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 004c8e8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c8e8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c8e8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c8e8c ["COPY", "tmp:0:8", ["const:b7d:8"]]
+ 004c8e8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c8e8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c8e8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c8e8c bytes 29293091
+ 004c8e8c bytes 29f52d91
- 004c9064 ["COPY", "tmp:0:8", ["const:321:8"]]
- 004c9064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c9064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c9064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004c9064 ["COPY", "tmp:0:8", ["const:31f:8"]]
+ 004c9064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004c9064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004c9064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c9064 bytes 08850c91
+ 004c9064 bytes 087d0c91
- 004c9068 ["COPY", "register:4048:8", ["const:2aa000:8"]]
- 004c9068 bytes 09efffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e528effe57855f47eaa648e4b64fb4aa"></a>

### [`004c93c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c93c4.md) → [`004c93c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) [`00bdc750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc750.md) [`00bdc760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc760.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7a0.md) [`00bdc7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9418",
      "incomplete_value": true,
      "site": "004c9428",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9418",
      "incomplete_value": true,
      "site": "004c9428",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:488:8"
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
      "definition_site": "004c942c",
      "incomplete_value": true,
      "site": "004c942c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "004c942c",
      "incomplete_value": true,
      "site": "004c942c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "004c9418",
      "READ",
      [
        "storage",
        "002a4488",
        null,
        "string"
      ]
    ],
    [
      "004c941c",
      "READ",
      [
        "storage",
        "002a4495",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c9418",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004c941c",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c940c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c93c4.md#insn-004c940c)
- 新版 `004c940c`（命令位置の公開資料なし）

~~~diff
- 004c940c ["COPY", "tmp:0:8", ["const:488:8"]]
- 004c940c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c940c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c940c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c940c ["COPY", "tmp:0:8", ["const:513:8"]]
+ 004c940c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c940c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c940c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c940c bytes 29211291
+ 004c940c bytes 294d1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-468ba0ae0c5b73e448938da49e04a59c"></a>

### [`004c94e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c94e0.md) → [`004c94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc770.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7c0.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c965c",
      "incomplete_value": true,
      "site": "004c965c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c965c",
      "incomplete_value": true,
      "site": "004c965c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9724",
      "incomplete_value": true,
      "site": "004c9724",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9724",
      "incomplete_value": true,
      "site": "004c9724",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c964c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c9714",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c964c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c9714",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c94e0.md#insn-004c964c) · [`004c9714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c94e0.md#insn-004c9714)
- 新版 `004c964c`（命令位置の公開資料なし） · `004c9714`（命令位置の公開資料なし）

~~~diff
- 004c964c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c964c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c964c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c964c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c964c bytes a99643f9
+ 004c964c bytes a9be43f9
- 004c9714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c9714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c9714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c9714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9714 bytes a99643f9
+ 004c9714 bytes a9be43f9
~~~


<a id="compare-44593a22a34bada9539e2f11899529a9"></a>

### [`004c9804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9804.md) → [`004c9804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9804.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) [`00bdc770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc770.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9840",
      "incomplete_value": true,
      "site": "004c9850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9840",
      "incomplete_value": true,
      "site": "004c9850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:488:8"
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
      "definition_site": "004c9854",
      "incomplete_value": true,
      "site": "004c9854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "004c9854",
      "incomplete_value": true,
      "site": "004c9854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "004c9840",
      "READ",
      [
        "storage",
        "002a4488",
        null,
        "string"
      ]
    ],
    [
      "004c9844",
      "READ",
      [
        "storage",
        "002a4495",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c9840",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004c9844",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9804.md#insn-004c9834)
- 新版 `004c9834`（命令位置の公開資料なし）

~~~diff
- 004c9834 ["COPY", "tmp:0:8", ["const:488:8"]]
- 004c9834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c9834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c9834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c9834 ["COPY", "tmp:0:8", ["const:513:8"]]
+ 004c9834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c9834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c9834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c9834 bytes 29211291
+ 004c9834 bytes 294d1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c56f2401b81460e4bb34060d236d9ee"></a>

### [`004c98e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c98e8.md) → [`004c98e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c98e8.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc780.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7d0.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.77% / 新版 97.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9a7c",
      "incomplete_value": true,
      "site": "004c9a7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9a7c",
      "incomplete_value": true,
      "site": "004c9a7c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9b44",
      "incomplete_value": true,
      "site": "004c9b44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9b44",
      "incomplete_value": true,
      "site": "004c9b44",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c9a6c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004c9b34",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c9a6c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c9b34",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c98e8.md#insn-004c9a6c) · [`004c9b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c98e8.md#insn-004c9b34)
- 新版 `004c9a6c`（命令位置の公開資料なし） · `004c9b34`（命令位置の公開資料なし）

~~~diff
- 004c9a6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c9a6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c9a6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c9a6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9a6c bytes a99643f9
+ 004c9a6c bytes a9be43f9
- 004c9b34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004c9b34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c9b34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004c9b34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9b34 bytes a99643f9
+ 004c9b34 bytes a9be43f9
~~~


<a id="compare-6ba9381b0cccf21682d98deb35465829"></a>

### [`004c9c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9c28.md) → [`004c9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9c28.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) [`00bdc780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc780.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9c64",
      "incomplete_value": true,
      "site": "004c9c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9c64",
      "incomplete_value": true,
      "site": "004c9c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:488:8"
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
      "definition_site": "004c9c78",
      "incomplete_value": true,
      "site": "004c9c78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "definition_site": "004c9c78",
      "incomplete_value": true,
      "site": "004c9c78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
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
      "004c9c64",
      "READ",
      [
        "storage",
        "002a4488",
        null,
        "string"
      ]
    ],
    [
      "004c9c68",
      "READ",
      [
        "storage",
        "002a4495",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c9c64",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004c9c68",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9c28.md#insn-004c9c58)
- 新版 `004c9c58`（命令位置の公開資料なし）

~~~diff
- 004c9c58 ["COPY", "tmp:0:8", ["const:488:8"]]
- 004c9c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c9c58 ["COPY", "tmp:0:8", ["const:513:8"]]
+ 004c9c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c9c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c9c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 bytes 29211291
+ 004c9c58 bytes 294d1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3713f9ece5d1314c98134b32b87f862f"></a>

### [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) → [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) FUN_004c9e38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`004c9d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9d0c.md) [`004cadbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cadbc.md) [`004caf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004caf04.md) [`004cafdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md) [`004cb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb140.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 9件 [`004c9d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md) [`004cadbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md) [`004caf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md) [`004cafdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md) [`004cb140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.39% / 新版 94.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9e7c",
      "incomplete_value": true,
      "site": "004c9e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c9e7c",
      "incomplete_value": true,
      "site": "004c9e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca0c4",
      "incomplete_value": true,
      "site": "004ca0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca0c4",
      "incomplete_value": true,
      "site": "004ca0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca36c",
      "incomplete_value": true,
      "site": "004ca380",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ca36c",
      "incomplete_value": true,
      "site": "004ca380",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99b:8"
              ]
            ]
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
      "004c9e68",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9e84",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c9efc",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004c9e68",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004c9e84",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c9efc",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md#insn-004c9e68) · [`004c9f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md#insn-004c9f9c) · [`004ca0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md#insn-004ca0b4)
- 新版 `004c9e68`（命令位置の公開資料なし） · `004c9f9c`（命令位置の公開資料なし） · `004ca0b4`（命令位置の公開資料なし）

~~~diff
- 004c9e68 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ef8:8"]]
- 004c9e68 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c9e68 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:f48:8"]]
+ 004c9e68 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9e68 bytes 397f47f9
+ 004c9e68 bytes 39a747f9
- 004c9f9c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004c9f9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c9f9c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004c9f9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9f9c bytes 299743f9
+ 004c9f9c bytes 29bf43f9
- 004ca0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 004ca0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca0b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004ca0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ca0b4 bytes 08d147f9
+ 004ca0b4 bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b7aedafbd67d1210397a1b67a583cd"></a>

### [`004cadbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cadbc.md) → [`004cadbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc790.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`005229d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/005229d4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdc7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7e0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`005229d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005229d4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "004cae2c",
      "incomplete_value": false,
      "site": "004cae2c",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cae2c",
      "incomplete_value": false,
      "site": "004cae2c",
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
            "const:510:8"
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
      "004cae2c",
      "DATA",
      [
        "storage",
        "00bed510",
        null,
        "undefined *"
      ]
    ],
    [
      "004cae70",
      "READ",
      [
        "storage",
        "00bed538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004cae2c",
      "DATA",
      [
        "storage",
        "00bed560",
        null,
        "undefined *"
      ]
    ],
    [
      "004cae70",
      "READ",
      [
        "storage",
        "00bed588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cadbc.md#insn-004cae28)
- 新版 `004cae28`（命令位置の公開資料なし）

~~~diff
- 004cae28 ["COPY", "tmp:0:8", ["const:510:8"]]
- 004cae28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cae28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cae28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004cae28 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 004cae28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004cae28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004cae28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cae28 bytes 29411491
+ 004cae28 bytes 29811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e8e8cc39c7eb2cb1925569d885c51d"></a>

### [`004caf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004caf04.md) → [`004caf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7a0.md) · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7f0.md) · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
            "const:5f0:8"
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
            "const:5a0:8"
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
  ],
  "added": [
    [
      "004caf2c",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004caf64",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004caf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004caf04.md#insn-004caf1c)
- 新版 `004caf1c`（命令位置の公開資料なし）

~~~diff
- 004caf1c ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 004caf1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004caf1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004caf1c bytes 4a811691
+ 004caf1c bytes 4ac11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a124afd936b422df71fa4ff7671e15"></a>

### [`004cafdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md) → [`004cafdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7b0.md) · 呼出先 9件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdc800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc800.md) · 呼出先 9件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
            "const:5f0:8"
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
            "const:5a0:8"
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
                "const:778:8"
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
                "const:728:8"
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
  ],
  "added": [
    [
      "004cb030",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004cb070",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md#insn-004cb028) · [`004cb08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md#insn-004cb08c)
- 新版 `004cb028`（命令位置の公開資料なし） · `004cb08c`（命令位置の公開資料なし）

~~~diff
- 004cb028 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 004cb028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004cb028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004cb028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004cb028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004cb028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004cb028 bytes 08811691
+ 004cb028 bytes 08c11791
- 004cb08c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004cb08c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cb08c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004cb08c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cb08c bytes 299543f9
+ 004cb08c bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a97a6f6e25e86913667ce8fe35ea4630"></a>

### [`004cb37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb37c.md) → [`004cb37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522a9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
            "const:5f0:8"
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
            "const:5a0:8"
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
  ],
  "added": [
    [
      "004cb3a4",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004cb3e0",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cb/004cb37c.md#insn-004cb394)
- 新版 `004cb394`（命令位置の公開資料なし）

~~~diff
- 004cb394 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 004cb394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004cb394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004cb394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cb394 bytes 29811691
+ 004cb394 bytes 29c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

